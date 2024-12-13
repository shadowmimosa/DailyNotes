<font size=4 face='楷体'>

## 通过导入 ibd 文件快速复制数据表

### idb 文件详解

[简单学习一下 ibd 数据文件解析](https://zhuanlan.zhihu.com/p/476694806)

### 实现过程 1. 找到 idb 文件

```sql
-- 创建新的数据表结构
CREATE TABLE `table_name` (  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4
```

```sql
-- 删除表空间
ALTER TABLE table_name DISCARD TABLESPACE;
```

```bash
# 授权 idb 文件
chown mysql:mysql table_name.ibd
```

```sql
-- 导入表空间
ALTER TABLE table_name IMPORT TABLESPACE;
```

### 带 frm 格式

- 安装 mysqlfrm 以读取表结构

```bash
[root@ ~]#  wget https://downloads.mysql.com/archives/get/p/30/file/mysql-utilities-1.6.5.tar.gz
[root@ ~]#  tar -xvzf mysql-utilities-1.6.5.tar.gz
[root@ ~]#  cd mysql-utilities-1.6.5
[root@ ~]#  python ./setup.py build
[root@ ~]#  python ./setup.py install
```

- 导出故障实例表结构

```bash
[root@ ~]#  /usr/bin/mysqlfrm --diagnostic /data/database/mysql/testdb/user_info.frm
```

- 恢复数据
  新起一个 MySQL5.7 新实例，在新实例上建相同的表，并卸载表空间

```sql
(root@localhost) > alter table testdb.user_info discard tablespace;
```

将故障库 user_info 表的 ibd 文件(testdb/user_info.ibd)拷贝到新实例对应的路径

挂载表空间

```sql
(root@localhost) > alter table testdb.user_info import tablespace;
```

如果报错 Error Code: 1808. Schema mismatch (Table has ROW_TYPE_DYNAMIC row format, .ibd file has ROW_TYPE_COMPACT row format.)
则在建表语句后加上 ROW_FORMAT=COMPACT

至此，user_info 表就恢复了

另一种方法(mysql5.5)
新起一个 MySQL5.5 新实例，在新实例上建相同的表，关闭数据库。从新表的 ibd 文件(testdb/user_info.ibd)中获取新表的 tablespace id

```bash
[root@ ~]#  hexdump -C /data/database/mysql/testdb/user_info.ibd | head -3
00000000  55 e6 77 a3 00 00 00 00  00 00 00 00 00 00 00 00  |U.w.............|
00000010  00 00 00 00 00 00 35 69  00 08 00 00 00 00 00 00  |......5i........|
00000020  00 00 00 00 00 e2 00 00  00 e2 00 00 00 00 00 00  |................|
```

从上面可以知道，新表的 tablespace id 是 00e2(16 进制)。
这时用 vim -b 打开旧表的 idb 文件(testdb/user_info.ibd)，vim 打开后输入 :%!xxd 转换为 16 进制,大致如下：

```bash
0000000: 6372 4c23 0000 0000 0000 0000 0000 0000  crL#............
0000010: 0000 0000 0696 f666 0008 0000 0000 0000  .......f........
0000020: 0000 0000 00d6 0000 00d6 0000 0000 0000  ................
0000030: 0007 0000 0040 0000 0000 0000 0005 0000  .....@..........
0000040: 0000 ffff ffff 0000 ffff ffff 0000 0000  ................
0000050: 0001 0000 0000 009e 0000 0000 009e 0000  ................
```

可以看到旧表的 tablespace id 是 00d6(16 进制)。
修改为 00e2，再输入 :%!xxd -r 保存，最后 wq 退出 vim。

将故障库 user_info 表的 ibd 文件(testdb/user_info.ibd)拷贝到新实例对应的路径。

最后 MySQL 的配置 my.cnf 中配置以下两个选项：

```ini
innodb_force_recovery=6
innodb_purge_threads=0
```

启动数据库，user_info 表即恢复了。只要将 user_info 表重新导出导入到旧库即可。
如果不配置上面两个选项，数据库会认为 user_info 已被损坏。变更了新的 tablespace id 后的.ibd 表文件，启动数据库后只能认出数据，但不能写入，这是因为原 ibdata 文件不仅保存了 space id 索引，还同时保存了一些其它的元数据。为了使元数据补全，所以采取导出、再导入的操作。

### Reference

[Mysql 通过导入 ibd 文件快速复制数据表](https://www.jianshu.com/p/6cacaaceb0bc)
[MySQL 通过 ibd 恢复数据](https://www.cnblogs.com/wshenjin/p/14780723.html)

**2023.03.21**
