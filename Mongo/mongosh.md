<font size=4 face='楷体'>

## mongosh

服务端安装 mongodb 后可能没有 mongosh

报错如下

```bash
-bash: mongo: 未找到命令
```

### 安装

编辑源

```bash
# /etc/yum.repos.d/mongodb-org-6.0.repo
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/6.0/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
```

```bash
yum install -y mongodb-mongosh
```

### Reference

[Mongodb -bash: mongo: 未找到命令](https://blog.csdn.net/qq_27566167/article/details/126432672)
[Install mongosh](https://www.mongodb.com/docs/mongodb-shell/install/#std-label-mdb-shell-install)

**2023.08.17**
