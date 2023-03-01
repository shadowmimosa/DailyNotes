<font size=4 face='楷体'>

## CentOs 7 安装配置 Mongo

### yum 安装

- 配置官方 yum 源  
  编辑 /etc/yum.repos.d/mongodb-org-4.2.repo 文件

  ```bash
  >>> vim /etc/yum.repos.d/mongodb-org-4.2.repo
  [mongodb-org-4.2]
  name=MongoDB Repository
  baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.2/x86_64/
  gpgcheck=1
  enabled=1
  gpgkey=https://www.mongodb.org/static/pgp/server-4.2.asc
  ```

- 安装 MongoDB

  ```bash
  > sudo yum install -y mongodb-org
  ```

- 启动 MongoDB

  ```bash
  > sudo service mongod start
  ```

- 进入 MongoDB 交互

  ```bash
  > mongo
  ```

### 安装 MongoDB Shell

新版本 mongo 默认不提供 shell, 需要自行安装

- 配置源

```bash
# /etc/yum.repos.d/mongodb-org-6.0.repo
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/6.0/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
```

- yum 安装

```bash
yum install -y mongodb-mongosh
```

- 启动

```bash
mongosh
```

[参考](https://www.mongodb.com/docs/mongodb-shell/install/#std-label-mdb-shell-install)

### 安装包

```bash
# 下载
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel80-4.4.1.tgz
# 解压
tar -zxvf mongodb-linux-x86_64-rhel80-4.4.1.tgz
# 移动文件
mv mongodb-linux-x86_64-rhel80-4.4.1  /opt/mongodb4
# 添加环境变量
export PATH=/opt/mongodb4/bin:$PATH

#创建数据文件夹和日志文件夹
sudo mkdir -p /usr/mongodb/data
sudo mkdir -p /usr/mongodb/log
# 设置权限
sudo chown `whoami` /usr/mongodb/data
sudo chown `whoami` /usr/mongodb/log

# 进入 mongodb 安装文件夹内写配置文件
vim mongodb.conf

# 写入以下内容
dbpath=/usr/mongodb/data # 数据文件存放目录
logpath=/usr/mongodb/log/mongod.log # 日志文件存放地址
port=27017 # 端口
fork=true # 以守护程序的方式启用，即在后台运行
auth=true # 需要认证。如果放开注释，就必须创建MongoDB的账号，使用账号与密码才可远程访问，第一次安装建议注释
bind_ip=0.0.0.0 # 允许远程访问，或者直接注释，127.0.0.1是只允许本地访问

# 启动 mongodb
mongod  -f  /opt/mongodb4/mongodb.conf
# 停止 mongodb
mongod --dbpath /usr/mongodb/data --logpath /usr/mongodb/log/mongod.log --shutdown
```

更多设置参考[官方文档](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)，这里使用的都是默认设置

### 开始远程连接

- 修改配置文件
  编辑 /etc/mongod.conf 文件

  ```bash
  # bind_ip=127.0.0.1
  bind_ip=0.0.0.0 # 修改为所有 ip 都可以访问
  ```

- 防火墙、安全组开放 27017 端口
  安全组是在阿里云控制台操作的
  关闭防火墙

  ```bash
  # 停止firewall
  systemctl stop firewalld.service
  # 禁止firewall开机启动
  systemctl disable firewalld.service
  ```

- 重启 mongo

  ```bash
  sudo service mongod restart
  ```

  至此远程可以直接连接，无需要验证

### 添加用户认证

- 进入 mongo 交互

  ```bash
  > mongo
  ```

- 创建用户、设置密码

  ```bash
  > use admin
  > db.createUser({user: "username", pwd: "password", roles: ["root"]})
  ```

  这里注意一下，新版本不支持 db.addUser() 创建用户，改为了 db.createUser()

- 修改密码

  ```bash
  > db.changeUserPassword("usertest","changepass");
  > db.updateUser("usertest",{pwd:"changepass1"});
  ```

- 创建不同权限用户

  ```bash
  > db.createUser({
          user: "mma",
          pwd: "mma@115",
          roles: [{
                  role: "readWrite", # 读写
                  db: "test1"
          }, {
                  role: "read", # 只读
                  db: "test2"
          }]
          })
  ```

- 修改配置文件
  再次编辑 /etc/mongod.conf 文件

  ```bash
  security:
    authorization: enabled # 开启认证
  ```

- 重启 mongo

  ```bash
  > sudo service mongod restart
  ```

  至此刚才的远程连接应该已经连不上了，添加用户认证后重新连接即可

### 命令

```bash
# 查看 mongo 安装位置
> whereis mongod

# 查看修改配置文件
> vim /etc/mongod.conf

# 启动 mongodb
> systemctl start mongod.service

# 停止 mongodb
> systemctl stop mongod.service

# 重启 mongodb
> systemctl restart mongod.service

# 查看 mongodb 的状态
> systemctl status mongod.service

# mongo shell
> mongo

# 查看数据库
> show dbs
```

### Reference

[Install MongoDB Community Edition on Red Hat or CentOS](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)
[mongodb 安装和配置 auth 验证](https://cloud.tencent.com/developer/article/1469172)
[20.MongoDB 远程连接](https://www.jianshu.com/p/90f0b638094d)
[mongodb 远程连接配置](https://www.cnblogs.com/jinxiao-pu/p/7121307.html)
[mongodb 远程连接配置](https://www.cnblogs.com/jinxiao-pu/p/7121307.html)
[Centos7 下 yum 安装 mongodb](https://www.cnblogs.com/xzlive/p/12855437.html)
[Centos8.0 安装 Mongodb 命令步骤](https://www.cnblogs.com/yuchenghao/p/13730675.html)

**Update On 2023.03.01, Create On 2020.06.26**
