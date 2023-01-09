<font size=4 face='楷体'>

## sqlite3

### 去重插入

```sql
-- 如果不存在就插入，存在就更新
insert or replace into table_name( id,type) values (1,0);
-- 如果不存在就插入，存在就忽略
insert or ignore into table_name (id,type) values (2,0);
-- 先判断是否存在, 测试未成功
IF NOT EXISTS(SELECT * FROM table_name  WHERE ….) THEN INSERT INTO ... ELSE UPDATE SET ...
```

建立唯一索引, 重复则忽略

### Reference

[sqlite 如何避免插入重复数据](http://www.chenxm.cc/article/1109.html.html)
[sqlite3 去重复数据](https://zhuanlan.zhihu.com/p/339791429)

**2022.05.11**
