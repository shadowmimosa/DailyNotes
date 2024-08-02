<font size=4 face='楷体'>

## Nginx with Docker

```bash
# 启动docker服务
systemctl start docker
# 下载Nginx镜像
docker pull nginx
# Nginx 镜像测试运行
docker run -d --name nginx -p 8080:80 nginx
```
配置文件参考
```yaml
server {
        listen 80;
        server_name www.haha.com
        root  /usr/share/nginx/html/www.haha.com;
 
        location / {
            root  /usr/share/nginx/html/www.haha.com;
            index index.html index.htm index.php;
            proxy_pass https://www.baidu.com;
        }
    }
```

### 无法查看日志问题

查看日志文件

```bash
ls -la /var/log/nginx/
```

文件被重定向到标准输出和标准错误

```bash
lrwxrwxrwx    1 root     root            11 Sep  9 18:26 access.log -> /dev/stdout
lrwxrwxrwx    1 root     root            11 Sep  9 18:26 error.log -> /dev/stderr
```

所以正确的查看方式是

```bash
docker logs <container-id>
```

### Reference

[利用docker来配置Nginx反向代理](https://blog.csdn.net/weixin_59128094/article/details/126980975)
[解决docker nginx无法查看日志的问题](https://blog.csdn.net/MacwinWin/article/details/120284472)

**2023.08.17**
