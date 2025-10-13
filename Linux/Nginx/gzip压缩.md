<font size=4 face='楷体'>

## Nginx 配置 gzip 压缩

nginx 有两种压缩方式，动态压缩和静态压缩

### 动态压缩

在 nginx 中实时用 gzip 压缩文件输出，利用 nginx 中的模块 `ngx_http_gzip_module`
消耗 CPU 来做压缩，配置如下：

```nginx
http {
  gzip on;
  gzip_min_length 1k;
  gzip_buffers 4 16k;
  gzip_comp_level 8;
  gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript;
  gzip_vary on;
  gzip_disable "MSIE [1-6]\.";
}
```

### 静态压缩

事先用 gzip 压缩好文件 `.gz`，让 nginx 根据请求来自己选择 `.gz` 文件输出，利用 nginx 中的模块 `http_gzip_static_module`
不消耗 CPU 资源，配置如下

```nginx
http {
  gzip on;
  gzip_min_length 1k;
  gzip_buffers 4 16k;
  gzip_comp_level 8;
  gzip_types text/plain application/javascript application/x-javascript text/css application/xml text/javascript;
  gzip_vary on;
  gzip_disable "MSIE [1-6]\.";
  gzip_static on; # 动态压缩 比动态压缩多了这行
}
```

### 完整的 Nginx 配置 Gzip 压缩

在 `nginx.conf` 的 `http` 部分添加以下配置以启用 gzip 压缩

```nginx
# 开启 gzip 功能
gzip on;
# 开启 gzip 静态压缩功能
gzip_static on;
# gzip 缓存大小
gzip_buffers 4 16k;
# gzip http 版本
gzip_http_version 1.1;
# gzip 压缩级别（1-10）
gzip_comp_level 5;
# gzip 压缩类型
gzip_types text/plain application/javascript text/css application/xml text/javascript application/x-httpd-php image/jpeg image/gif image/png;
# 是否在 http header 中添加 Vary: Accept-Encoding，一定要开启，否则读取不到以 .gz 结尾的压缩文件
gzip_vary on;
```

**注意**： 一定要设置 `gzip_vary on;`，否则打包后的 HTML 引入的文件以 `.js` 或 `.css` 结尾，而压缩文件却以 `.js.gz` 或 `.css.gz` 结尾，可能导致引入报错。

### Reference

[前端压缩打包 Vue+vite 配合 nginx 实现 gzip 压缩](https://blog.csdn.net/weixin_39559449/article/details/121675705)
[文档 - HttpGzip 模块](https://blog.redis.com.cn/doc/standard/httpgzip.html)
[文档 - HttpGzipStatic 模块](https://blog.redis.com.cn/doc/optional/gzipstatic.html)

**2023.12.07**
