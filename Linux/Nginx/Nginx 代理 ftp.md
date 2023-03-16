<font size=4 face='楷体'>

## nginx 代理 ftp

```ini
stream {
    upstream ftp {
        hash $remote_addr consistent;
        server 10.0.2.2:21 weight=5;
    }
    server {
        listen 24389;
        proxy_connect_timeout 5s;
        proxy_timeout 30s;
        proxy_pass ftp;
   }
}
```

- 使用 stream 需要安装 stream 模块
- 可以代理成功, 但 ftp 需要开启被动模式, 否则连接只控制在 nginx 服务器 ip

> 在 port 模式, 与 server 建立控制链路的是中转 ip2.2.2.2, 而控制链路信息告诉 server, 要去连接 client1.1.1.1, server 认为不合法(只有连接 2.2.2.2 才合法), 于是返回控制链路 500 信息

### Reference

[nginx 代理 ftp 服务器](https://blog.csdn.net/yangyi139926/article/details/123713698)

**2023.03.14**
