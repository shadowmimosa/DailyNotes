<font size=4 face='楷体'>

## vue 携带 cookie

```javascript
 document.cookie = “ioiopipoadiasdasdbasdbas”
 let data2 = await this.$axios.get("http://localhost:9000/select", {
        withCredentials: true,   //设置跨域的时候传递cookie，需要服务端的配合
      });
      console.log(data2, "data2");
```

后端响应需要携带跨域字段

```java
res.header('Access-Control-Allow-Credentials', 'true') //当客户端跨域并需要传递cookie时，需要设置Access-Control-Allow-Credentials，并且值为“true”  代表是否向页面暴露cookie
    // 指定允许的跨域请求字段。
res.header(
        'Access-Control-Allow-Headers',
        'token,Content-Type,Content-Length, Authorization, Accept,X-Requested-With,domain,zdy' //当客户端跨域并需要传递cookie时，需要设置Access-Control-Allow-Headers，并且值为不能为“*”，需要具体配置  代表允许上传的请求头字段
    )
    // 指定允许的跨域请求的来源。填写星号（*）表示全部域名；您也可以填写完整域名，例如http://www.aliyun.com。
res.header('Access-Control-Allow-Origin', 'http://localhost:8082') //当客户端跨域并需要传递cookie时，需要设置Access-Control-Allow-Origin，并且值为不能为“*”，需要具体配置
    // 指定允许的跨域请求方法。可同时设置多个方法，多个方法用英文逗号（,）分隔。
res.header('Access-Control-Allow-Methods', 'PUT,POST,GET,DELETE,OPTIONS')
```

### Reference

[axios+vue 请求时如何携带 cookie](https://blog.csdn.net/qq_46634851/article/details/125171043)

**2022.08.15**
