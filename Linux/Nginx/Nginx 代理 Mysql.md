<font size=4 face='楷体'>

## Nginx 代理 Mysql

- docker-compose.yml

  ```yaml
  version: '2.0'

  services:
    nginx:
      restart: always
      image: nginx:1.13.9-alpine
      ports:
        - 63307:63306
      volumes:
        - ./nginx.conf:/etc/nginx/nginx.conf
  ```

- nginx.conf

  ```ini
  user  nginx;
  worker_processes  1;

  error_log  /var/log/nginx/error.log warn;
  pid        /var/run/nginx.pid;


  events {
      worker_connections  1024;
  }


  http {
      include       /etc/nginx/mime.types;
      default_type  application/octet-stream;

      #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
      #                  '$status $body_bytes_sent "$http_referer" '
      #                  '"$http_user_agent" "$http_x_forwarded_for"';

      #access_log  /var/log/nginx/access.log  main;

      sendfile        on;
      #tcp_nopush     on;

      keepalive_timeout  65;

      #gzip  on;

      include /etc/nginx/conf.d/*.conf;
  }

  stream {

      log_format proxy '$remote_addr [$time_local] '
                   '$protocol $status $bytes_sent $bytes_received '
                   '$session_time "$upstream_addr" '
                   '"$upstream_bytes_sent" "$upstream_bytes_received" "$upstream_connect_time"';

      access_log  /var/log/nginx/access.log  proxy;

      upstream mysql_server {
          server 127.0.0.1:3306;
      }

      server {
          listen 63306;
          proxy_pass mysql_server;
      }
  }
  ```

### Docker + Nginx + Mysql

- 查看可用的 nginx 版本
  ```bash
  docker search nginx
  ```
- 取最新的 nginx 安装
  ```bash
  docker pull nginx:latest
  ```
- 查看 docker 镜像是都有 nginx

  ```bash
  docker images
  ```

- 运行 nginx

  ```bash
  $ docker run --name nginx -p 8080:80 -d nginx
  nginx: 容器名称
  8080: 本地端口
  80: 容器内部的80端口
  -d:nginx: 设置容器在后台一直运行
  ```

- 查看 nginx 是否启动
  ```bash
  docker ps 查看所有正在运行的容器
  docker ps -l 查看最近一次运行的容器
  docker ps | grep nginx 利用管道符查询
  ```
- 进入容器
  首先查看启动容器的 CONTAINER ID

  ```bash
  docker ps
  ```

  然后输入 `docker exec -it CONTAINER ID bash` 命令进入容器, 此处 CONTAINER ID 为上边查询出的。

- 修改 nginx 配置文件
  nginx.conf 配置文件在 /etc/nginx/ 下面

  ```bash
  # 可能需要先安装vim
  apt-get update
  apt-get install vim
  ```

- 容器重启

  ```bash
  docker restart nginx
  ```

- 端口开启
  防火墙开启端口, 安全组放开端口

- nginx 主机配置文件挂载

  ```bash
  docker run --name nginx -p **8089:80** -v **/home/inspur/docker-nginx/nginx.conf**:/etc/nginx/nginx.conf -v **/home/inspur/docker-nginx/log**:/var/log/nginx -v **/home/inspur/docker-nginx/conf.d/default.conf**:/etc/nginx/conf.d/default.conf -d nginx
  ```

  加粗的几个地方是需要注意的点

  --name 给你启动的容器起个名字，以后可以使用这个名字启动或者停止容器
  -p 映射端口，将 docker 宿主机的 8089 端口和容器的 80 端口进行绑定
  -v 挂载文件用的，第一个-v 表示将你本地的 nginx.conf 覆盖你要起启动的容器的 nginx.conf 文件，第二个表示将日志文件进行挂载，就是把 nginx 服务器的日志写到你 docker 宿主机的/home/docker-nginx/log/下面
  第三个-v 表示的和第一个-v 意思一样的。
  -d 表示启动的是哪个镜像

- 添加如下配置文件

```ini
# vim nginx.conf

stream {
  upstream cloudsocket {
    hash $remote_addr consistent;
    server 192.168.0.3:3306 weight=5 max_fails=3 fail_timeout=30s;
}
server {
  listen 3306;#数据库服务器监听端口
  proxy_connect_timeout 10s;
  proxy_timeout 300s;#设置客户端和代理服务之间的超时时间，如果 5 分钟内没操作将自动断开。
  proxy_pass cloudsocket;
}
}
```

注意 stream 与 http 同级 不要写在 http 里边

然后重启容器

```bash
docker stop nginx
docker rm nginx
docker run --name nginx -p 3306:3306 -v /home/inspur/docker-nginx/nginx.conf:/etc/nginx/nginx.conf -v /home/inspur/docker-nginx/log:/var/log/nginx -v /home/inspur/docker-nginx/conf.d/default.conf:/etc/nginx/conf.d/default.conf -d nginx
# 记得开启 3306 端口哦
```

### Reference

[Nginx 代理 MySQL](https://blog.csdn.net/jiankunking/article/details/124479507)
[docker 搭建 nginx 配置 mysql 反向代理](https://www.cnblogs.com/pengcool/p/15516433.html)

**2023.03.17**
