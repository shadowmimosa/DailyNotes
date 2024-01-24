<font size=4 face='楷体'>

## Docker + Mysql

[mysql on docker hub](https://hub.docker.com/_/mysql)

### 报错

> mysqld:Can’t read dir of '/etc/mysql/conf.d'

```bash
docker run -p 3306:3306 --name mysql -v /mydata/mysql/log:/var/log/mysql -v /mydata/mysql/data:/var/lib/mysql -v /mydata/mysql/conf:/etc/mysql -e MYSQL_ROOT_PASSWORD=root -d  mysql:5.7
```

原因
这个挂载目录出了问题，这个挂载方式已经不适用了，配置文件已经不在/etc/mysql 里了，里面只有两个空目录，分别是 conf.d 和 mysql.conf.d。真正的配置文件是/etc/my.cnf，因此需要修改。

```bash
docker run -p 3306:3307 --name mysql -v /mydata/mysql/log:/var/log/mysql -v /mydata/mysql/data:/var/lib/mysql -v /mydata/mysql/conf:/etc/mysql -e MYSQL_ROOT_PASSWORD=root -d  mysql:5.7
```

### Reference

[Can‘t read dir of /etc/mysql/conf.d/](https://blog.csdn.net/qq_45564783/article/details/126440171)

**2023.03.17**
