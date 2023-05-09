<font size=4 face='楷体'>

## Nginx 验证微信文件

### 固定文件名

```nginx
location /OiHVjAiPc2.txt { alias /home/wwwroot/xxx/OiH123iPc2.txt; }
```

重启生效

```bash
/usr/sbin/nginx -s reload
```

### 动态文件名

首先在 ngxin.conf 中, 加入一个变量, 这个变量是解惑 uri 中的文件名
例如/a/b.txt 则能获取到 b.txt, 然后把这个变量 传递给某个 controller, controller 获取这个变量的名字, 去数据库搜索, 输出内容

```nginx
map $uri $basename {
      ~/(?<captured_basename>[^/]*)$ $captured_basename;
}
```

注意, 这个 map 需要 nginx 开启 mapmodule, 这个一般最新的 nginx 都有
这个代码需要些在全局中的 http 块中, 也就是 nginx.conf 中

到了具体的 server 时, 想要获取这个变量

```ngin
location ~ \.txt$ {
        if ( $basename ~ (([\S\s]*).txt) ){
              set  $file_name $2;
            #proxy_pass http://127.0.0.1:8090/yun/weChatTicket/verify?ticket_file=$file_name;
            proxy_pass http://127.0.0.1:9290/yun/weChatTicket/verify?ticket_file=$basename;
                break;
        }

        return 502 '{"status":502,"msg":$uri $basename $file_name}';
    }
```

这里 `$file_name` 是不带后缀结尾的, `$basename` 是带后缀结尾的

## Reference

[nginx 验证微信文件(linux 服务器添加校验文件)](https://www.cnblogs.com/fanbi/p/14372789.html)
[nginx 验证微信文件](https://blog.csdn.net/m0_37581001/article/details/105414308)

**2022.10.27**
