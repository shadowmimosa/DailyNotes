<font size=4 face='楷体'>

## mysql 一个字段多个值

某次比较懒，想了个骚操作：想在一个字段里存多个值，想来想去没想好咋弄，然后发现万能的百度竟然还有这种骚操作

- 在一个字段中添加一个值 使用 "," 隔开

```sql
update table set username=CONCAT(username, ',添加的值') where id=1
```

- 一个字段多个值，修改其中的一个

```sql
update table set username=replace(username, '原来的值', '新值')
```

- 一个列有多个值，查询字段中是否包含某个值

```sql
select *  from table where find_in_set('admin', username)
```

- 删除指定字段

```sql
-- 删除
UPDATE sys_user SET username= REPLACE(username, ',1', '') where id = '123'
UPDATE sys_user SET username= REPLACE(username, '1,', '') where id = '123'
```

### Reference

[mysql 一个字段多个值](https://blog.csdn.net/qq_36609501/article/details/88362841)

**2019.11.6**
