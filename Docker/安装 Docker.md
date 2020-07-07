<font size=4 face='楷体'>

## Linux 下 docker 安装

- 安装依赖包

  ```bash
  sudo yum install -y yum-utils device-mapper-persistent-data lvm2
  ```

- 设置阿里云镜像源

  ```bash
  sudo yum-config-manager --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
  ```

- 安装 Docker-CE

  ```bash
  sudo yum install docker-ce
  ```

  如果出现报错

  ```bash
  Problem: package docker-ce-3:19.03.12-3.el7.x86_64 requires containerd.io >= 1.2.2-3, but none of the providers can be installed
  ```

  此时需要安装新版 containerd.io

  ```bash
  dnf install https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm
  ```

  再次执行安装

  ```bash
  sudo yum install docker-ce
  ```

- 启动 docker

  ```bash
  # 开机自启
  sudo systemctl enable docker
  # 启动docker服务
  sudo systemctl start docker
  ```

- 添加 docker 用户组（可选）

  ```bash
  # 1. 建立 Docker 用户组
  sudo groupadd docker
  # 2.添加当前用户到 docker 组
  sudo usermod -aG docker $USER
  ```

  如果运行 docker 出现报错

  ```bash
  Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.40/containers/json: dial unix /var/run/docker.sock: connect: permission denied
  ```

  执行

  ```bash
  sudo chmod a+rw /var/run/docker.sock
  ```

  修改权限

## 基本使用

- 官方镜像[地址](https://hub.docker.com/)

- 阿里云镜像[地址](https://cr.console.aliyun.com/)

- 基本语法

  ```bash
  # 下载镜像：docker pull <镜像名:tag>    如：下载centos镜像
  docker pull centos
  docker pull sameersbn/redmine:latest
  # 查看已下载镜像
  docker images
  # 删除容器
  docker rm <容器名 or ID>
  # 查看容器日志
  docker logs -f <容器名 or ID>
  # 查看正在运行的容器b
  docker ps
  # 查看所有的容器，包括已经停止的。
  docker ps -a
  # 删除所有容器
  docker rm $(docker ps -a -q)
  # 停止、启动、杀死指定容器
  docker start <容器名 or ID> # 启动容器
  docker stop <容器名 or ID> # 启动容器
  docker kill <容器名 or ID> # 杀死容器
  # 后台运行 docker run -d <Other Parameters>
  docker run -d -p 127.0.0.1:33301:22 centos6-ssh
  # 暴露端口： 一共有三种形式进行端口映射
  docker -p ip:hostPort:containerPort # 映射指定地址的主机端口到容器端口
  # 例如：docker -p 127.0.0.1:3306:3306 映射本机3306端口到容器的3306端口
  docker -p ip::containerPort # 映射指定地址的任意可用端口到容器端口
  # 例如：docker -p 127.0.0.1::3306 映射本机的随机可用端口到容器3306端口
  docer -p hostPort:containerPort # 映射本机的指定端口到容器的指定端口
  # 例如：docker -p 3306:3306 # 映射本机的3306端口到容器的3306端口
  # 映射数据卷
  docker -v /home/data:/opt/data # 这里/home/data 指的是宿主机的目录地址，后者则是容器的目录地址
  ```

## GUI 管理

这里推荐使用 Portainer 作为容器的 GUI 管理方案。
官方[地址](https://portainer.io/install.html)

安装：

```bash
docker volume create portainer_data
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```

访问你的 IP:9000 即可进入容器管理页面

## 镜像加速

鉴于国内网络问题，后续拉取镜像十分缓慢，可以需要配置加速器来解决

- 镜像站
  [Docker 官方中国区](https://registry.docker-cn.com)
  [网易](http://hub-mirror.c.163.com)
  [ustc](https://docker.mirrors.ustc.edu.cn)

  [腾讯云](https://mirror.ccs.tencentyun.com)

这里使用阿里云的镜像加速，在开发者平台找到自己的唯一加速地址后编辑

```bash
# 阿里云控制台搜索容器镜像服务
# 进入容器镜像服务， 左侧最下方容器镜像服务中复制加速器地址
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'

{
  "registry-mirrors": ["你的加速器地址"]
}

EOF
# 重启docker
sudo systemctl daemon-reload
sudo systemctl restart docker
```

### Reference

[linux 安装 docker](https://www.jianshu.com/p/2dae7b13ce2f)
[Docker（二）使用阿里云 docker 镜像加速](https://blog.csdn.net/qq_37495786/article/details/83246421)
[CentOS 8 安装 Docker 报错](https://blog.csdn.net/shana_8/article/details/105190368)

**2020.6.8**
