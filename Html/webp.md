<font size=4 face='楷体'>

## WebP

WebP 是 Google 推出的一种图片格式，它基于 VP8 编码，可对图像大幅压缩。与 JPEG 相同，WebP 也是一种有损压缩，但在画质相同的情况下，WebP 格式比 JPEG 图像小 40%

### webp 与 png, jpg 相互转换

使用 webp-tools

- Ubuntu
  ```bash
  apt-get install webp
  ```
- CentOS

  ```bash
  yum -y install libwebp-devel libwebp-tools
  ```

- 会安装几个工具
  ```
  cwebp → WebP encoder tool
  dwebp → WebP decoder tool
  vwebp → WebP file viewer
  webpmux → WebP muxing tool
  gif2webp → Tool for converting GIF images to WebP
  ```
- Convert from WebP to PNG
  ```bash
  dwebp img.webp -o img.png
  ```
- Convert from JPG to WebP
  ```bash
  cwebp img.jpg -o img.webp
  ```

### WebP 兼容

WebP 的优势显而易见，但尚有部分浏览器不支持，而且也要保持对旧版本的兼容
使用 [WebJS](http://webpjs.appspot.com/js/webpjs-0.0.2.min.js) 插件，对不支持的浏览器使用 JS 解码

```html
<script type="text/javascript" src="js/webpjs-0.0.2.min.js"></script>
<img src="/images/img.webp" />
```

### Reference

[WordPress 使用 webP 格式减少图片体积](https://tlanyan.me/wordpress-use-webp-format-accelerate-image-downloads/)
[webp 与 png、jpg 相互转换](https://www.cnblogs.com/gentlemanwuyu/p/10594862.html)
[让浏览器全面兼容 WebP 图片格式](https://www.cnblogs.com/yjken/p/3922299.html)
[WebPJS](http://webpjs.appspot.com/)

**2020.11.05**
