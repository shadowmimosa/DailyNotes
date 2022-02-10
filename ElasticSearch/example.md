```bash
# 创建index
curl -H "Content-Type: application/json" -XPUT "http://localhost:9200/_index" -d
{
  "settings": {
    "index": {
      "number_of_shards": "3",
      "analysis": {
        "analyzer": {
          "mylike": {
            "filter": [
              "lowercase"
            ],
            "tokenizer": "my_ngram"
          }
        },
        "tokenizer": {
          "my_ngram": {
            "token_chars": [
              "letter",
              "digit"
            ],
            "min_gram": "1",
            "type": "nGram",
            "max_gram": "1"
          }
        }
      },
      "number_of_replicas": "1"
    }
  },
  "mappings": {
    "doc": {
      "properties": {
        "fid": {
          "type": "keyword"
        },
        "r2": {
          "format": "yyyy-MM-dd",
          "type": "date"
        },
        "bt": {
          "analyzer": "mylike",
          "type": "text"
        },
        "w1": {
          "type": "keyword"
        },
        "id": {
          "type": "keyword"
        },
        "w2": {
          "type": "keyword"
        },
        "w5": {
          "analyzer": "mylike",
          "type": "text"
        },
        "yxbj": {
          "type": "keyword"
        }
      }
    }
  }
}
# bool查询
curl _index/_search?preference=_primary_first
{
  "query": {
    "bool": {
      "filter": [
        {
          "match_phrase": {
            "w5": "沈阳"
          }
        },
        {
          "match_phrase": {
            "w5": "保护管"
          }
        },
        {
          "range": {
            "r2": {
              "gte": "20210201",
              "lte": "20210220"
            }
          }
        }
      ]
    }
  },
  "sort": {
    "r2": "desc"
  }
}

# 仅在主分片查询
curl _index/_search?preference=_primary_first
{
  "query": {
    "bool": {
      "filter": [
        {
          "match_phrase": {
            "id": "161699868"
          }
        }
      ]
    }
  },
  "sort": {
    "id": "desc"
  }
}

# 查询多个
curl _index/_search
{
  "query": {
    "ids": {
      "values": [
        "161699868",
        "161699867",
        "161699897",
      ]
    }
  }
}

# 删除多个
curl _index/_delete_by_query
{
  "query": {
    "ids": {
      "values": [
        "161699868",
        "161699867",
        "161699897",
      ]
    }
  }
}

# 排序查询指定字段
curl _index/_search
{
  "size": 2000,
  "_source": [
    "id",
    "r2"
  ],
  "query": {
    "bool": {
      "must": [
        {
          "match_phrase": {
            "w5": "您因为之前访问本页面的频率过高"
          }
        }
      ]
    }
  }
}
```

```bash
# must 与 should 混合嵌套查询

# filter 和 must 结果相同, 可相互替换
# filter 不计算评分, 查询效率高, 有缓存; must 计算评分, 查询效率低, 无缓存

curl _index/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "bool": {
            "filter": [
              {
                "match_phrase": {
                  "bt": "沈阳"
                }
              },
              {
                "match_phrase": {
                  "bt": "箱式变电站"
                }
              }
            ]
          }
        },
        {
          "bool": {
            "filter": [
              {
                "match_phrase": {
                  "bt": "沈阳"
                }
              },
              {
                "match_phrase": {
                  "bt": "保护管"
                }
              }
            ]
          }
        }
      ]
    }
  },
  "sort": {
    "r2": "desc"
  }
}
```

```bash
# 多条件高级检索模板
# https://www.cnblogs.com/zys-blog/p/13207196.html
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "title": "Science"
                    }
                },
                {
                    "match": {
                        "countryArea": "United States"
                    }
                },
                {
                    "bool": {
                        "should": [
                            {
                                "match": {
                                    "sponsor": "National Science Foundation"
                                }
                            },
                            {
                                "match": {
                                    "sponsor": "David and Lucile Packard Foundation"
                                }
                            }
                        ],
                        "minimum_should_match": 1
                    }
                },
                {
                    "bool": {
                        "should": {
                            "nested": {
                                "path": "researchAreas",
                                "query": {
                                    "bool": {
                                        "should": [
                                            {
                                                "match": {
                                                    "researchAreas.subjectName": "Arts and Humanities"
                                                }
                                            },
                                            {
                                                "match": {
                                                    "researchAreas.subjectName": "Ecology"
                                                }
                                            }
                                        ],
                                        "minimum_should_match": 1
                                    }
                                }
                            }
                        }
                    }
                }
            ],
            "must_not": {
                "match": {
                    "fundingType": "Program or Curriculum Development or Provision"
                }
            }
        }
    }
}
```

```bash
# 重建副本

# 删除副本
curl index/_settings
{
  "number_of_replicas": 0
}

# 新建副本
curl index/_settings
{
  "number_of_replicas": 1
}
```


```bash
# 动态增删 replica
# 实测新增replica速度很快，cpu占比不算高，远低于重新索引数据，基本接近远程复制文件的速度。有replica之后，logstash或es会有集群负载均衡，比如replica为1，基本primary和replica CPU占比均衡，性能上ES整体大约多耗用20%CPU，磁盘空间多耗用1倍。

# 获取当前所有 index 配置
curl -XGET http://localhost:9200/_settings

# 获取某些 index 的配置
curl -XGET http://localhost:9200/index_1/_settings

# 动态修改某些 index 配置, 增加 replica
curl -XPUT http://localhost:9200/idnex_1/_settings -d '{"replicas":1}'

# 动态修改某些 index 配置, 删除 replica
curl -XPUT http://localhost:9200/index_1/_settings -d '{"replicas":0}'
```