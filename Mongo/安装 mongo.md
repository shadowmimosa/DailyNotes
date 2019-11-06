<font size=4 face='楷体'>

## CentOs 7 安装配置 mongo

### 安装 MongoDB

- 配置官方 yum 源  
   编辑 /etc/yum.repos.d/mongodb-org-4.2.repo 文件

        [mongodb-org-4.2]
        name=MongoDB Repository
        baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.2/x86_64/
        gpgcheck=1
        enabled=1
        gpgkey=https://www.mongodb.org/static/pgp/server-4.2.asc

- 安装 MongoDB

        > sudo yum install -y mongodb-org

- 启动 MongoDB

        sudo service mongod start

- 进入 MongoDB 交互

        > mongo

更多设置参考[官方文档](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)，这里使用的都是默认设置

### 开始远程连接

- 修改配置文件
  编辑 /etc/mongod.conf 文件

        # bind_ip=127.0.0.1
        bind_ip=0.0.0.0 # 修改为所有 ip 都可以访问

- 防火墙开放 27017 端口  
   这里是在阿里云控制台操作的

- 重启 mongo

          sudo service mongod restart

  至此远程可以直接连接，无需要验证

### 添加用户认证

- 进入 mongo 交互

  > mongo

- 创建用户、设置密码

        > use admin
        > db.createUser({user: "username", pwd: "password", roles: ["root"]})

  这里注意一下，新版本不支持 db.addUser() 创建用户，改为了 db.createUser()

- 创建不同权限用户

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

- 修改配置文件
  再次编辑 /etc/mongod.conf 文件

        security:
          authorization: enabled # 开启认证

- 重启 mongo

        sudo service mongod restart

至此刚才的远程连接应该已经连不上了，添加用户认证后重新连接即可

### Reference

[Install MongoDB Community Edition on Red Hat or CentOS](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/)
[mongodb 安装和配置 auth 验证](https://cloud.tencent.com/developer/article/1469172)
[20.MongoDB 远程连接](https://www.jianshu.com/p/90f0b638094d)
[mongodb 远程连接配置](https://www.cnblogs.com/jinxiao-pu/p/7121307.html)

**2019.11.1**
_新的一个月 加油_
