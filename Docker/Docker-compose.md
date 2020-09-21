<font size=4 face='楷体'>

## Docker-compose

### 简介

Docker-Compose 项目是 Docker 官方的开源项目，负责实现对 Docker 容器集群的快速编排。

### 安装

```bash
apt install python-pip
# centOS
yum -y install python-pip
pip install docker-compose
```

检查版本

```bash
docker-compose --version
```

卸载

```bash
pip uninstall docker-compose
```

### 常用命令

> docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]

    -f --file FILE指定Compose模板文件，默认为docker-compose.yml
    -p --project-name NAME 指定项目名称，默认使用当前所在目录为项目名
    --verbose  输出更多调试信息
    -v，-version 打印版本并退出
    --log-level LEVEL 定义日志等级(DEBUG, INFO, WARNING, ERROR, CRITICAL)

> docker-compose up [options] [--scale SERVICE=NUM...] [SERVICE...]

    -d 在后台运行服务容器
    -no-color 不是有颜色来区分不同的服务的控制输出
    -no-deps 不启动服务所链接的容器
    --force-recreate 强制重新创建容器，不能与-no-recreate同时使用
    –no-recreate 如果容器已经存在，则不重新创建，不能与–force-recreate同时使用
    –no-build 不自动构建缺失的服务镜像
    –build 在启动容器前构建服务镜像
    –abort-on-container-exit 停止所有容器，如果任何一个容器被停止，不能与-d同时使用
    -t, –timeout TIMEOUT 停止容器时候的超时（默认为10秒）
    –remove-orphans 删除服务中没有在compose文件中定义的容器

> docker-compose ps [options] [SERVICE...] 列出项目中所有的容器

> docker-compose stop [options] [SERVICE...]

    -t, –timeout TIMEOUT 停止容器时候的超时（默认为10秒）

> docker-compose -h

> docker-compose down [options]

    –rmi type，删除镜像，类型必须是：all，删除compose文件中定义的所有镜像；local，删除镜像名为空的镜像
    -v, –volumes，删除已经在compose文件中定义的和匿名的附在容器上的数据卷
    –remove-orphans，删除服务中没有在compose中定义的容器
    docker-compose down
    停用移除所有容器以及网络相关

> docker-compose logs [options] [SERVICE...]

    查看服务容器的输出。默认情况下，docker-compose将对不同的服务输出使用不同的颜色来区分。可以通过–no-color来关闭颜色。
    docker-compose logs
    查看服务容器的输出
    -f 跟踪日志输出

> docker-compose build [options] [--build-arg key=val...] [SERVICE...]

    –compress 通过gzip压缩构建上下环境
    –force-rm 删除构建过程中的临时容器
    –no-cache 构建镜像过程中不使用缓存
    –pull 始终尝试通过拉取操作来获取更新版本的镜像
    -m, –memory MEM为构建的容器设置内存大小
    –build-arg key=val为服务设置build-time变量
    服务容器一旦构建后，将会带上一个标记名。可以随时在项目目录下运行docker-compose build来重新构建服务

### Reference

[Docker 入门之 docker-compose](https://www.cnblogs.com/minseo/p/11548177.html)

**2020.09.17**
