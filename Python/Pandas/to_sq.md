<font size=4 face='楷体'>

## pandas 转存数据库中

一次懒得写 sql 了，正好项目中用了 pandas 存 Excel, 想着直接用 pandas 存数据库好了。没想到也不是那么方便、上手即用

首先需要安装 sqlalchemy 模块

```python
from sqlalchemy import create_engine

# 这里用的还是 pymysql,（所以打包什么的 pymysql 需要隐式导入
engine = create_engine(
    "mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}?charset={charset}"
    .format({
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "passwd": "password",
        "database": "mysql",
        "charset": "utf8mb4",
    }))

df.to_sql(name="my_table", con=engine, if_exists='append', index=False)
```

`to_sql` 的几个参数:

- name: 表名
- con: 连接
- if_exists: 表如果存在怎么处理
- - append: 追加
- - replace: 删除原表，建立新表再添加
- - fail: 什么都不干
- index=False: 不插入索引 index

### Reference

[利用 pandas 的 to_sql 将数据插入 MySQL 数据库和所踩过的坑](https://blog.csdn.net/lzw2016/article/details/84720433)
[python3 pandas to_sql 填坑](https://blog.csdn.net/qnloft/article/details/87979937)

**2019.11.12**
