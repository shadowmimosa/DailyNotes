<font size=4 face='楷体'>

## nginx 通过域名代理 tcp 端口

示例有误，还未成功，具体参考[stackoverflow](https://stackoverflow.com/questions/34741571/nginx-tcp-forwarding-based-on-hostname/40135151#40135151)

```bash
stream {
    map $ssl_preread_server_name $name {
        mysql.test.com mysql;
        redis.test.com redis;
        default https_default_backend;
    }
    upstream mysql{
        server 10.0.0.3:3306;
    }
    upstream redis{
        server 10.0.0.4:6379;
    }
    upstream https_default_backend {
        server 127.0.0.1:443;
    }
    server {
        listen 10.0.0.1:443;
        proxy_pass $name;
        ssl_preread on;
    }
}
```

或者

```bash
stream {
    upstream mysql{
        server 10.1.5.3:3306;
    }
    upstream redis{
        server 10.1.5.4:6379;
    }
    map $server_addr $name {
        192.168.168.238 mysql;
        192.168.168.239 redis;
    }
    server {
        listen 80;
        proxy_pass $name;
    }
}
```

### Reference

[nginx 通过域名代理 tcp 端口](https://www.it610.com/article/1281701766869565440.htm)

**2020.12.01**
