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

-   Query Context：会对搜索进行相关性算分
-   Filter Context：不需要相关性算分，能够利用缓存来获得更好的性能

当用户输入多个条件进行查询的时候，可以使用 bool 查询，在 bool 查询中，filter 和 must_not 属于 Filter Context，不会对算分结果产生影响；must 和 should 属于 Query Context，会对结果算分产生影响。

在 bool 查询中，查询结构是对相关性算分有影响的，可以通过嵌套的方式修改不同字段在查询中的权重以及直接通过指定字段的 boost 值来控制在搜索中的权重，另外使用 Boosting Query 可以提升搜索的精准性，同时也可以将更多的搜索显示在结果中
[参考](https://zhuanlan.zhihu.com/p/161710475)

### Reference

[elasticsearch.exceptions.ConnectionTimeout](https://blog.csdn.net/guyu1003/article/details/103584871)
[关于 Elastic Search 的 5 种分片查询](https://www.jianshu.com/p/ad8818eb4fea)

**2021.03.10**
