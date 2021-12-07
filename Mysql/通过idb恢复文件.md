<font size=4 face='楷体'>

## 通过 idb 恢复文件

- 建立一张和需要还原的空表, 表结构要一致
- 找到当前 mysql 目录下的 data 文件夹下对应的数据库, 里面有当前创建的表, 例如 user.idb, 不要删除
- 执行 sql 语句命令：ALTER TABLE 表名 DISCARD TABLESPACE
- 此时把需要还原的数据替换到刚才的目录下
- 再次执行 sql 命令：ALTER TABLE 表名 IMPORT TABLESPACE

### Reference

[mysql 通过 idb 文件恢复数据](https://www.cnblogs.com/mybk/p/15438596.html)
[MySQL 根据 idb 文件恢复数据](https://blog.csdn.net/weixin_45121446/article/details/117409931)

**2021.12.07**
