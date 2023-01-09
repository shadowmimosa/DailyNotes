<font size=4 face='楷体'>

## Mysql 慢查询

### 慢查询日志的配置

正常情况下, 只需要在配置文件中增加 slow_query_log = 1 配置, 即打开慢查询日志, 未指定 slow_query_log_file 的情况下, 会自动生成一个以主机名+'slow'.log 的文件

```sql
-- 查看配置
show variables like '%slow_query%'
```

```sql
-- 查看时间配置
-- 默认情况下记录慢查询的时间阈值为 10s
-- long_query_time 指定超过多少时长的查询需要被记录
show variables like '%long_query_time%'
```

```sql
show variables like '%log_output%'
-- min_examined_row_limit 超过指定行数的扫描查询开关: 默认 0, 代表不限制扫描函数
show variables like '%min_examined_row_limit%';
```

### 慢查询日志打开

- 设置开启 MySQL 慢日志参数: 无需重启即可生效, 但是重启会导致设置失效

```sql
set global long_query_time=0.1;
set global log_queries_not_using_indexes=on;
set global slow_query_log = on;
set log_output = 'FILE,TABLE';
```

- 需要修改配置文件 my.ini 配置文件中配置: 需要重启 MySQL 才可以生效, 命令为 service mysqld restart

```sql
slow_query_log = 1
slow_query_log_file = /var/lib/mysql/slow_query_log_202123.log
log_output = table
long_query_time = 1
```

可以将慢查询日志同时记录在文件以及 mysql.slow_log

### 查询慢查询日志

```sql
select \* from mysql.slow_log
select CONVERT(sql_text USING utf8) sql_text from mysql.slow_log;
```

其中参数
|参数|说明|
|---|---|
|start_time|执行时间|
|user_host|主机名|
|query_time|查询所花费的时间|
|lock_time|查询使用锁的时间|
|rows_sent|查询返回了多少数据给客户端|
|rows_examined|查询扫描了多少行
|db|数据库|
|sql_text|SQL|
|thread_id|id|

```sql
-- 查询慢 sql 日志文件保存位置
show variables like '%slow_query_log_file%';
```

```sql
-- 没有 index 的查询记录开关
show global variables like '%indexes%';
```

```sql
-- log_queries_not_using_indexes 是否开启记录没有 index 的查询
-- log_throttle_queries_not_using_index 做日志记录的流量控制, 一分钟可以记录多少条; 默认 0 是不限制
```

MySQL 中执行 explain 或者 desc 命令查看慢查询语句, 可以看出为什么 SQL 查询慢, 如:

```sql
explain select _ from dbname.tableName
-- 或
desc select _ from dbname.tableName
```

它的输出格式细节可以关注 MySQL explain format, 在输出中最要注意的是:

1. type 字段值:
   system > const > eq_ref > ref > fulltext > ref_or_null > index_merge > unique_subquery >
   index_subquery > range > index > all
   备注: ALL 是效率最差; 若 type 值为 index 或 all, 则需要优化
   2.Extra 字段值: 出现 Using filesort 以及 Using temporary, 表示 mysql 根本不能使用索引, 效率会受到重大影响。应尽可能对此进行优化;
   最主要是要关注在 orderby 和 groupby。
   Using filesort: 表示 mysql 会对结果使用一个外部索引排序, 而不是从表里按索引次序读到相关内容。
   Using temporary: 表示 mysql 对查询结果排序时使用临时表; 常见于 order by 和 group by。

2. key: 是否有使用 Key, key 长度如何

Note: SQL 优化是个很复杂的过程, 有可能出现拆东墙补西墙的情况:
比如给数据库表加入了索引之后, 确实查询快了, 可是存储空间加多了, 插入删除操作耗时也增加了;
如果在一个写多读少的系统中, 执行这种优化可能会起到反效果。
所以优化完之后千万不能大意, 要持续监控系统, 防止出现引入新瓶颈的情况。

[Mysql 慢查询优化方法及优化原则](https://www.jb51.net/article/161441.htm)

1. 日期大小的比较, 传到 xml 中的日期格式要符合'yyyy-MM-dd', 这样才能走索引, 如: 'yyyy'改为'yyyy-MM-dd', 'yyyy-MM'改为'yyyy-MM-dd'【这样 MYSQL 会转换为日期类型】
2. 条件语句中无论是等于、还是大于小于, WHERE 左侧的条件查询字段不要使用函数或表达式或数学运算
3. WHERE 条件语句尝试着调整字段的顺序提升查询速度, 如把索引字段放在最前面、把查询命中率高的字段置前等
4. 保证优化 SQL 前后其查询结果是一致的
5. 在查询的时候通过将 EXPLAIN 命令写在查询语句前, 测试语句是否有走索引【具体用法百度】
6. 禁止使用 SELECT \* FROM 操作, 应只返回需要的字段, 不需要的字段不要返回
7. 可以尝试分解复杂的查询, 在应用层面进行表关联, 以此代替 SQL 层面的表关联
8. WHERE 子句和 ORDER BY 子句涉及到的列建索引
9. 避免在 WHERE 子句中对字段进行 NULL 判断【可以对表字段改造一下, 字符串型字段默认值设置为空字符串, 数字型字段默认值设置为 0, 日期型字段默认值设置为 1990-01-01 等】
10. 避免在 WHERE 子句中使用!=或<>操作符
11. 避免在 WHERE 子句中使用 OR 操作符
12. BETWEEN AND 代替 IN
13. LIKE '%abc%'不会走索引, 而 LIKE 'abc%'会走索引
14. 避免对字段进行表达式操作
15. 避免对字段进行函数操作
16. GROUP BY 操作默认会对 GROUP BY 后面的字段进行排序, 如果你的程序不需要排序, 可在 GROUP BY 语句后面加上 ORDER BY NULL 去除排序
17. 如果是数值型字段, 则尽量设计为数值型字段, 不要为了方便、为了偷懒而给后面维护的同事埋坑
18. 表中所有字段设计为 NOT NULL
19. 返回条数固定时, 用 LIMIT 语句限制返回记录的条数, 如只需要一条记录, 或肯定只有一条记录符合条件, 那建议加上 LIMIT 1
20. 对于枚举类型的字段【即有固定罗列值的字段】, 建议使用 ENUM 而不是 VARCHAR, 如性别、星期、类型、类别等
21. 对于存 IP 地址的字段设计为成 UNSIGNED INT 型
22. 避免在 SQL 中使用 NOW()、CURDATE()、RAND()函数【因为这种方式会导致 MYSQL 无法使用 SQL 缓存】, 可以转化为通过传入参数的方式
23. 对于统计类的查询【如查询连续几个月的数据总量, 或查询同比、环比等】, 可以通过定时查询并统计到统计表的方式提高查询速度

### Reference

[mysql 慢查询](https://www.cnblogs.com/xj63183/p/15855201.html)

**2022.10.13**
