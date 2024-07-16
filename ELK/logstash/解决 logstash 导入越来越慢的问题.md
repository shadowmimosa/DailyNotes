<font size=4 face='楷体'>

## 解决 logstash 导入越来越慢的问题

使用了 Logstash 同步 Mysql 中数据，但随着数据量的增加 Logstash 的导入速度逐渐变慢。经过分析，发现性能瓶颈主要在于 MySQL 的深度分页问题，logstash 会在我们自己写的的 sql 上又加了一层作为封装

在 logstash 的导入 conf 配置文件中的 statement 代码

```sql
SELECT * FROM table_name
```

Logstash 的实际执行代码（设置了 jdbc 的分页大小为 1000）

```sql
SELECT * FROM (SELECT * FROM table_name) AS `t1` LIMIT 1000 OFFSET 510000
```

这样做造成的结果就是，offset 的值越大，查询的速度会越来越慢，详见[issues/166](https://github.com/logstash-plugins/logstash-input-jdbc/issues/166)

也可以尝试对 logstash 进行配置上的设置，比如调整`pipeline.worker`的数量、增大分配给 Logstash 的内存大小等，虽然有提高速度，但还是远远不够

目前的解决方案是 **按照数据库中的 id 使用偏移量来进行全量入库**，避免 logstash 自己进行分页

```sql
SELECT * FROM (select * from table_name where id > :sql_last_value) AS t1 LIMIT 1000
```

```conf
input {
  jdbc {
    # 指明jdbc驱动包位置和要使用的驱动包类。
    jdbc_driver_library => "logstash-7.6.2/mysql-connector-java-8.0.19.jar"
    jdbc_driver_class => "com.mysql.jdbc.Driver"
     # myqsl数据库的连接信息
    jdbc_connection_string => "jdbc:mysql://localhost:3306/xxxx?serverTimezone=UTC"
    jdbc_user => "user"
    jdbc_password => "password"
    # 设置分页的部分
    record_last_run => true
    use_column_value => true
    tracking_column => "id"
    ; tracking_column_type => "numeric"
    # jdbc_paging_enabled => true
    # jdbc_page_size => "1000"
    # jdbc_fetch_size => 1000
    # info.txt用于存放上次查询id的偏移量
    last_run_metadata_path => "logstash-7.6.2\info.txt"
    # 每分钟执行一次该语句
    statement => "SELECT * from table_name where id > :sql_last_value limit 1000"
    schedule => "* * * * *"
  }
}

output {
  # 将数据输出到ElasticSearch中
    elasticsearch {
    hosts => ["127.0.0.1:9200"]
    # es文档索引和文档数据的id
    index => "index_name"
	document_id => "%{id}"
  }
}
```

### Reference

- [Logstash 导入 mysql 数据到 es 慢的解决方法](https://blog.csdn.net/qq_38798909/article/details/120825512)
- [logstash导入mysql越来越慢](https://blog.csdn.net/xujiamin0022016/article/details/100789622/)

**2024.07.03**
