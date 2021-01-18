<font size=4 face='楷体'>

## nginx 多配置文件配置

当 nginx 配置文件 nginx.conf 项目或业务越来越多的时候，nginx 配置文件会越来越大和复杂，不便于管理，所以需要分到多个子配置文件中

-   建立子配置文件目录

    ```bash
    mkdir /usr/local/nginx/conf/conf.d
    touch web.conf api.conf
    ```

-   nginx.conf include 引入文件

    ```bash
    http{
        ...
        include conf/conf.d/*.conf; # *.conf代表所有配置文件
    }
    ```

-   把 server 模块移入子配置文件中
    ```bash
    #web.conf
    server{
        listen 80;
        server_name localhost;
        ...
    }
    #api.conf
    server{
        listen 81;
        server_name localhost;
        ...
    }
    ```

通过 /usr/local/nginx/sbin/nginx -t 检测 nginx 配置文件有没有语法错误，nginx -s reload 重启 nginx 生效

### Reference

[nginx多配置文件配置](https://zixuephp.net/article-500.html)

**2020.12.01**
