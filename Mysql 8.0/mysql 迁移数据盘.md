<font size=4 face='楷体'>

## Mysql 迁移数据目录到数据盘

- 停止 mysql 服务

  ```bash
  service mysqld stop
  ```

- 复制数据目录

  ```bash
  cp -a /var/lib/mysql/* /data/mysql/
  ```

- 赋权

  ```bash
  chown -R mysql.mysql /data/mysql/
  ```

- 配置文件里修改数据目录

  ```bash
  vim /etc/my.cnf

  datadir=/data/mysql
  socket=/data/mysql/mysql.sock
  ```

- 启动 mysql 服务

  ```bash
  service mysqld start
  ```

### Referenc

[mysql 迁移数据目录](https://cloud.tencent.com/developer/article/1671532)

**2020.8.21**
