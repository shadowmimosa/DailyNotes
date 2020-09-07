<font size=4 face='楷体'>

## Nginx 配置反向代理

### 安装

- 安装相关组件
  ```bash
  yum -y install gcc gcc-c++ zlib zlib-devel openssl openssl-devel pcre pcre-devel
  ```
- 编译安装
  [官方网站](https://nginx.org/en/download.html)获取下载链接，这里直接下载最新版
  默认安装路径为: `/usr/local/nginx`

  ```bash
    #获取nginx。如果未安装 wget，使用 yum -y install wget
    wget https://nginx.org/download/nginx-1.19.0.tar.gz

    #解压，zxvf显示解压文件
    tar zxf nginx-1.19.0.tar.gz

    #进入nginx源文件目录
    cd nginx-1.19.0

    #编译
    #默认 https 没有打开，需要添加 --with-http_ssl_module
    # 默认不安装 stream 模块，需要代理 TCP 要打开
    ./configure --with-http_ssl_module --with-stream

    #安装Nginx
    make && make install

    #启动Nginx
    /usr/local/nginx/sbin/nginx
  ```

### 代理 Http 配置文件示例

```bash
{
worker_processes 1;

events {
  use epoll;
  worker_connections 65535;
}

http {
  server {
    listen 80;

    server_name baidu.com;

    return 301 http://www.baidu.com;
  }

  server {
    listen 80;

    server_name www.baidu.com;

    location / {
      proxy_pass http://127.0.0.1:8000/;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
    }
  }
}
```

### 代理 Https 配置文件示例
{
worker_processes 1;

events {
  use epoll;
  worker_connections 65535;
}

http {
  server { 
    listen 443 ssl;
    server_name www.baidu.com;
    charset utf-8;

    ssl_certificate /root/cert/baidu.com_chain.crt;
    ssl_certificate_key /home/xuan/cert/baidu.com_key.key;
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;

    location / {
      proxy_pass http://127.0.0.1:8000/;
    }
}
}
}

### 代理 TCP 配置文件示例

这里以代理 Mongo 的配置文件示例
代理 TCP 需要 Nginx 版本大于等于 1.9.0

配置 TCP 代理

```bash
# /etc/nginx/tcp.d/mongo.conf

stream {
  server {
    listen       27017;
    proxy_pass   stream_mongo;
  }
  upstream stream_mongo {
    server host:27017;
  }
}
```

在 http 配置中导入以上配置

```bash
# /usr/local/nginx/conf/nginx.conf

worker_processes  1;

# 此处导入 TCP 配置
include /etc/nginx/tcp.d/*.conf;

events {
    worker_connections  1024;
}
```

重启 Nginx

```bash
nginx -s reload
```

### Reference

[Nginx（三）------nginx 反向代理](https://www.cnblogs.com/ysocean/p/9392908.html)
[Nginx 配置反向代理](https://www.jianshu.com/p/bcfb5a3a5903)

[Nginx stream 模块初探](https://blog.csdn.net/Aria_Miazzy/article/details/100055748)
[Nginx 安装与配置-Centos7](https://www.cnblogs.com/docsxyz/p/11133175.html)
[mongodb nginx 代理问题](https://blog.csdn.net/zhao4471437/article/details/53261276)
[nginx 转发 tcp 连接](https://www.cnblogs.com/imcati/p/11717802.html)

**2019.10.31**
