<font size=4 face='楷体'>

## NEXTCLOUD + ONLYOFFICE 打造在线协同编辑平台

### ONLYOFFICE DOC 对服务器的基本需求

|            |                    |
| ---------- | ------------------ |
| CPU        | 双核, 主频 2G 以上 |
| RAM        | 2G 及以上          |
| HDD        | 40G 以上           |
| OS         | Centos7            |
| 附加要求   | SWAP 空间 4G 以上  |
| PostgreSQL | 9.1 以上           |
| Nginx      | 1.3.13 以上        |
| RabbitMQ   |                    |

### Nextcloud 环境

网页服务：Apache
Linux 版本：RockyLinux 8.4
PHP 版本：7.4
数据库版本：Mariadb 10.3.28

### ONLYOFFICE 环境

网页服务：Nginx 1.20
Linux 版本：CentOS 7.6
RabbitMQ：3.3.5
数据库：Postgresql 12

### 安装 Nginx

```bash
yum -y install epel-release
yum -y install nginx
```

### 安装 Postgresql-12

```bash
yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
yum install -y postgresql12-server
```

### 初始化数据库

```bash
/usr/pgsql-12/bin/postgresql-12-setup initdb
systemctl enable postgresql-12 && systemctl start postgresql-12
```

### 修改数据库认证配置文件

```bash
vi /var/lib/pgsql/12/data/pg_hba.conf
systemctl reload postgresql-12
```

### 创建数据库

```bash
cd /tmp
sudo -u postgres psql -c "CREATE DATABASE onlyoffice;"
sudo -u postgres psql -c "CREATE USER onlyoffice WITH password 'xiaoyu123';"
sudo -u postgres psql -c "GRANT ALL privileges ON DATABASE onlyoffice TO onlyoffice;"
```

### 安装 RabbitMQ

```bash
yum -y install rabbitmq-server
systemctl enable rabbitmq-server && systemctl start rabbitmq-server
```

### 安装微软字体

```bash
yum -y install cabextract
yum -y xorg-x11-font-utils
yum -y fontconfig
rpm -i https://deac-ams.dl.sourceforge.net/project/mscorefonts2/rpms/msttcore-fonts-installer-2.6-1.noarch.rpm
```

### 安装 onlyoffice doc 源

```bash
yum -y install https://download.onlyoffice.com/repo/centos/main/noarch/onlyoffice-repo.noarch.rpm
```

### 安装 onlyoffice doc

```bash
yum -y install onlyoffice-documentserver
systemctl enable supervisord &&systemctl start supervisord
systemctl enable nginx &&systemctl start nginx
```

### 修改 onlyoffice doc 端口号(可选)

```bash
export DS_PORT=6100
```

### 配置 onlyoffice 服务

```bash
bash documentserver-configure.sh
```

### Reference

[NEXTCLOUD 与 ONLYOFFICE：打造在线协同编辑平台](https://www.51cto.com/article/668736.html)

**2023.08.18**
