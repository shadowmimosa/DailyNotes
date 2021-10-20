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
