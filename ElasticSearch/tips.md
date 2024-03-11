## es 中小 tips

### 高亮显示

[查询结果 高亮显示](https://blog.csdn.net/ma15732625261/article/details/79722791)
[Elasticsearch 实现复合查询,高亮结果等技巧](<[Elasticsearch实现复合查询,高亮结果等技巧](https://www.cnblogs.com/haizhongdenta/p/11496473.html)>)

暂时没有用上，手动标红

### Search API

[Elasticsearch 6.x 版本全文检索学习之 Search API](https://www.cnblogs.com/biehongli/p/11752430.html)
[Elasticsearch 实现复合查询,高亮结果等技巧](<[Elasticsearch实现复合查询,高亮结果等技巧](https://www.cnblogs.com/haizhongdenta/p/11496473.html)>)
[ElasticSearch 常用查询及聚合分析](https://zhuanlan.zhihu.com/p/183816335)

[elasticsearch 短语查询（match_phrase）](https://blog.csdn.net/liuxiao723846/article/details/78365843)
[Elasticsearch——查询//过滤详细总结](https://www.cnblogs.com/kelelipeng/p/12321603.html)
[学习 python 库：elasticsearch-dsl](https://www.cnblogs.com/lit10050528/p/12178822.html)

### Filter 与 Query

在 ES 中，提供了 Query 和 Filter 两种搜索：

- Query Context：会对搜索进行相关性算分
- Filter Context：不需要相关性算分，能够利用缓存来获得更好的性能

当用户输入多个条件进行查询的时候，可以使用 bool 查询，在 bool 查询中，filter 和 must_not 属于 Filter Context，不会对算分结果产生影响；must 和 should 属于 Query Context，会对结果算分产生影响。

在 bool 查询中，查询结构是对相关性算分有影响的，可以通过嵌套的方式修改不同字段在查询中的权重以及直接通过指定字段的 boost 值来控制在搜索中的权重，另外使用 Boosting Query 可以提升搜索的精准性，同时也可以将更多的搜索显示在结果中
[参考](https://zhuanlan.zhihu.com/p/161710475)

### shard & replica

> index 包含多个 shard
> 每个 shard 都是一个最小工作单元，承载部分数据，lucene 实例，完整的建立索引和处理请求的能力
> 增减节点时，shard 会自动在 nodes 中负载均衡
> primary shard 和 replica shard，每个 document 肯定只存在于某一个 primary shard 以及其对应的 replica shard 中，不可能存在于多个 primary shard
> replica shard 是 primary shard 的副本，负责容错，以及承担读请求负载
> primary shard 的数量在创建索引的时候就固定了，replica shard 的数量可以随时修改
> primary shard 的默认数量是 5，replica 默认是 1，默认有 10 个 shard，5 个 primary shard，5 个 replica shard
> primary shard 不能和自己的 replica shard 放在同一个节点上（否则节点宕机，primary shard 和副本都丢失，起不到容错的作用），但是可以和其他 primary shard 的 replica shard 放在同一个节点上

[浅谈 Elasticsearch（三）---shard&replica](https://juejin.cn/post/6918745075761545223)

### size

After 2.x, size=0 for all bucket results won't work anymore, please refer to this thread. Here in my example I just set the size equal 999999. You can pick a large number according to your case.

```python
s = Search(using=client, index="jokes").query("match", jks_content=keywords).extra(size=0)
a = A('terms', field='jks_title.keyword', size=999999)
s.aggs.bucket('by_title', a)
response = s.execute()
```

[elasticsearch-dsl aggregations returns only 10 results. How to change this](https://stackoverflow.com/questions/47219846/)

### Ordering by a sub aggregation

```bash
GET /_search
{
  "aggs": {
    "genres": {
      "terms": {
        "field": "genre",
        "order": { "max_play_count": "desc" }
      },
      "aggs": {
        "max_play_count": { "max": { "field": "play_count" } }
      }
    }
  }
}
```

[Ordering by a sub aggregation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html#_ordering_by_a_sub_aggregation)

### 聚合练习

[聚合语法学习（aggs、bucket、metric、hitogram、date hitogram）](https://blog.csdn.net/Yal_insist/article/details/122245421)

### Reference

[elasticsearch.exceptions.ConnectionTimeout](https://blog.csdn.net/guyu1003/article/details/103584871)
[关于 Elastic Search 的 5 种分片查询](https://www.jianshu.com/p/ad8818eb4fea)

**2021.03.10**
