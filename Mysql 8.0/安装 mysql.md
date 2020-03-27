<font size=4 face='楷体'>

## Centos 安装 mysql

- 卸载默认安装的 mariadb

  > yum search mysql
  > yum remove mariadb.x86_64

- 去[官网](https://dev.mysql.com/downloads/repo/yum/)找到 mysql 的下载版本
  找到下面的 Linux7，即 CentOS7(CentOS 是 Red Hat 旗下的)
  在下面的链接上直接右键复制链接（或者可以先下载到本地然后再用 ftp 传到服务器）

- 安装

  > wget https://dev.mysql.com/get/mysql80-community-release-el8-1.noarch.rpm
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

  > cat /var/log/mysqld.log | grep password

- 登录

  > mysql -u root -p 密码

- 修改密码，权限等
  参考[这里](Mysql 8.0/添加用户和赋权.md)

- 开机启动
  > systemctl enable mysqld
  > systemctl daemon-reload

### Reference

[CentOS7 安装 mysql](https://cloud.tencent.com/developer/article/1393323)
[在 Centos 操作系统下安装 mysql8.0](https://blog.csdn.net/qq_43317529/article/details/83039252)

**2020.3.17**
