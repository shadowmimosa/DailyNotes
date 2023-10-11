<font size=4 face='楷体'>

## Centos 安装 mysql

可以直接参考官网最新的[文档](https://dev.mysql.com/doc/refman/8.0/en/linux-installation-yum-repo.html)

- 卸载默认安装的 mariadb

  > yum search mysql
  > yum remove mariadb\*
  > yum remove mariadb.x86_64

- 去[官网](https://dev.mysql.com/downloads/repo/yum/)找到 mysql 的下载版本
  <!-- 找到下面的 Linux7, 即 CentOS7(CentOS 是 Red Hat 旗下的) -->

  在下面的链接上直接右键复制链接（或者可以先下载到本地然后再用 ftp 传到服务器）

- 安装

  > wget <https://dev.mysql.com/get/mysql80-community-release-el8-1.noarch.rpm>
  > yum localinstall mysql # 本地安装 yum 源
  > yum search mysql # 检测是否已经安装

  找到对应的软件包, 复制名称, 使用 yum 安装

  > yum install mysql-community-server.x86_64

- 查看是否安装成功

  > ps -ef | grep mysql

- 启动 mysql

  > service mysqld start
  > service mysqld restart
  > service mysqld stop

- 查找默认登录密码

  > cat /var/log/mysql/mysqld.log | grep password
  > cat /var/log/mysqld.log | grep password

- 登录

  > mysql -u root -p 密码

<!-- - 修改密码, 权限等 -->

参考[这里](Mysql/添加用户和赋权.md)

- 开机启动
  > systemctl enable mysqld
  > systemctl daemon-reload

### Centos8 重装 MySQL8

- 卸载

  ```bash
  yum remove -y mysql
  ```

- 清理残留

  ```bash
  find / -name mysql
  ```

- 安装 mysql

  ```bash
  yum localinstall mysql80-community-release-el8-1.noarch.rpm
  yum update
  yum install mysql-server
  ```

- 查看 mysql

  ```bash
  ps -ef | grep mysql
  ```

- 启动

  ```bash
  systemctl start mysqld # 启动
  systemctl enable mysqld # 添加开机启动
  systemctl status mysqld # 查看mysqld状态
  ```

- 修改 root 密码
  默认启动是无密码

  ```sql
  Alter user 'root'@'localhost' identified by 'password';
  flush privileges; -- 刷新权限
  ```

- 创建用户

  ```sql
  -- 创建用户名为 user 密码为 password 的用户
  Create user 'user'@'%' identified by 'password';
  ```

  新用户赋权

  ```sql
  -- 这里赋予所有权限
  Grant all privileges on *.* to 'user'@'%';
  ```

  ```sql
  -- 刷新权限
  flush privileges;
  ```

- 修改端口
  配置文件中添加端口配置

  ```bash
  vim /etc/my.cnf

  # 指定配置文件启动, 指定用户
  mysqld --defaults-file=/etc/my.cnf --user=root
  ```

  ```bash
  [mysqld]
  port=12345
  ```

  重启服务

  ```bash
  systemctl restart mysqld.service
  ```

  检查端口

  ```bash
  netstat -nltp
  ```

### 卸载

```bash
# 查看安装的mysql
mysql --version
rpm -qa|grep -i mysql

# 查看mysql服务启用状态
systemctl status mysqld.service

# 停止mysql服务
systemctl stop mysqld
systemctl status mysqld.service

# # # # 开始卸载, 一共5个包, 先卸载谁都可以, 逐个卸载, 直到5个全部卸载
yum remove mysql-community-server.x86_64

# 或者 --nodeps 忽略组件的依赖关系, 强制卸载
rpm -qa|grep -i mysql
rpm -ev --nodeps mysql-community-release-el7-5.noarch
rpm -ev --nodeps mysql-community-common-5.1.73-7.el6.x86_64
rpm -ev --nodeps mysql-community-client-5.1.73-7.el6.x86_64
rpm -ev --nodeps mysql-community-libs-5.1.73-7.el6.x86_64
rpm -ev --nodeps community-server-5.1.73-7.el6.x86_64

# 查询没有了, 说明全部卸载完了
rpm -qa|grep -i mysql

# 删除 mysql 相关的文件
rm -rf /usr/lib64/mysql

# 删除 my.cnf
rm -rf /etc/my.cnf
```

### Reference

[CentOS7 安装 mysql](https://cloud.tencent.com/developer/article/1393323)
[在 Centos 操作系统下安装 mysql8.0](https://blog.csdn.net/qq_43317529/article/details/83039252)
[centos8 重装 MySQL8](https://blog.csdn.net/weixin_40251892/article/details/108899826)
[[MySQL]如何修改 MySQL8.0 端口(centos 7)
](https://blog.csdn.net/jameskaron/article/details/104561098)

**Created On 2020.3.17, Update On 2020.10.10**
