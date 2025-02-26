---
created: 2024-01-04T17:36:25 (UTC +08:00)
tags: [nginx 压缩]
source: https://blog.csdn.net/weixin_52834606/article/details/129100959
author:
---

# Nginx 请求压缩详解\_nginx 压缩-CSDN 博客

> ## Excerpt
>
> 文章浏览阅读 3.1k 次。nginx 高并发优化 ，压缩请求\_nginx 压缩

---

## 一、介绍

请求压缩，是将服务器的结果通过 Nginx 将内容进行压缩后，在发送给客户端，降低网络传输压力，提升传输效率。

常见的两种请求方式是： gzip 、brotli（Google），相当于 brotli 的效率会高，后续内容详解。

请求压缩的话分为：动态压缩，静态压缩，动态压缩会导致 Nginx 内部的 sendfile 失效。对于一些不变的内容可以使用静态压缩，提升请求效率 。

用于请求结果的压缩，需要客户端和服务器双方支持压缩协议，在服务器进行结果的压缩，客户端进行数据解压缩，在压缩会占用服务器端一些性能效率，这个损耗根据压缩的等级来定，等级越高，耗损越大。可以减少网络传输压力。

压缩只针对于 代理方式请求才生效。

## 二、请求压缩的流程

![Alt text](image.png)

执行的流程是：客户端向服务器端发送请求，nginx 接收请求之后，会向上游服务器服务器发送请求，Nginx 和上游服务器之间会创建网络通道，之间会进行数据的传输，在这里如果是开启了压缩操作，那么 Nginx 会将结果数据进行压后，在将数据返回给客户端，在浏览器接收到 nginx 的请求，会先处理请求头，发现有 压缩协议，那么就会判断当前浏览器是否支持该协议，如果支持则会将数进行解压的操作并数据展示给用户。

开启压缩之后用户是无感的，可以降低传输压力，但是图片和视频就不建议压缩了，因为后的大小变化不大，gzip 是网络传输的压缩的，需要客户端支持，服务器端也需要支持，将传输的数据进行压缩，将传输数据变小，我们可以设置下，当然压缩必越高，解压缩和压缩的时间更长，服务器端压力会大些。

## 三、[Gzip 压缩](https://so.csdn.net/so/search?q=Gzip%E5%8E%8B%E7%BC%A9&spm=1001.2101.3001.7020)

### 3.1 gzip 介绍

Gzip 是 GNUzip 的缩写，最早用于 UNIX 系统的文件压缩。[HTTP 协议](https://so.csdn.net/so/search?q=HTTP%E5%8D%8F%E8%AE%AE&spm=1001.2101.3001.7020)上的 Gzip 编码是一种用来改进 Web 应用程序性能的技术，Web 服务器和客户端（浏览器）必须共同支持 Gzip。目前主流浏览器：Chrome、Firefox 等都支持该协议，常见的服务器：Apache、Nginx、IIS 同样支持 Gzip。

Gzip 的压缩比率在 3-10 倍左右（纯文本），可以大大节省服务器的网络带宽。在实际应用中，并不是对所有文件进行压缩，通常只压缩静态文件（js\\css\\html）。JPEG 这类文件用 Gzip 压缩的不够好，而且压缩也是耗费 CPU 资源的。

那么 Gzip 是如何进行压缩的呢？简单来说，Gzip 压缩是在一个文本文件中找出类似的字符串，并临时替换他们，使整个文件变小。这种形式的压缩对 Web 来说非常合适，因为 HTML 和 CSS 文件通常包含大量的重复字符串，例如空格、标签等。

![Alt text](image-1.png)

### 3.2 gzip 的使用

gzip 模块是 Nginx 中内置的，所以不需要添加其他的默认，只要配置安装好 Nginx 既可。

使用作用域： http , server , location

Nginx 如下配置

- gzip on ;

- 是否开启压缩。

- 默认值：gzip off 默认关闭

- gzip_buffers 32 4k | 16 8k

- 压缩缓冲区大小。

- 默认值 ： gzip_buffers 32 4k | 16 8k

- gzip_comp_level 1 ;

- 压缩等级 1-9 ，数字越大压缩比越高。

- 越小压缩速度和解压缩速度越快，压缩占比越小

- 默认值 ：gzip_comp_leve 1

- gzip_http_version 1.1

- 使用 gzip 的最小的 http 版本。

- gzip_min_length

- 设置将被 gzip 压缩的响应的最小长度。长度仅由 "Content-Length" 响应报头字段确定。

- gzip_proxied 多选

- 对于上游服务器返回不同的 head 来决定是不是要进行压缩，两种常见的一种 off 一种 any

- 一般启用 cache 的话都是已经进行过压缩的所有可以规避一些细节

- off 为不做限制。

- 作为反向代理时，针对于上游服务器返回的头信息进行压缩。

- expired - 启用压缩，如果 header 头中包含 "Expires" 头信息

- no-cache - 启用压缩，如果 header 头中包含 "Cache-Control:no-cache" 头信息

- no-store - 启用压缩，如果 header 头中包含 "Cache-Control:no-store" 头信息

- private - 启用压缩，如果 header 头中包含 "Cache-Control:private" 头信息

- no_last_modified - 启用压缩,如果 header 头中不包含 "Last-Modified" 头信息

- no_etag - 启用压缩 ,如果 header 头中不包含 "ETag" 头信息

- auth - 启用压缩 , 如果 header 头中包含 "Authorization" 头信息

- any - 无条件启用压缩。

- gzip_vary on ;

- 增加一个 header ，适配老的浏览器 Vary : Accept-Encoding

- gzip_types :

- 哪些 mime 类型的文件进行压缩。

- gzip_disable ：

- 禁止哪些浏览器使用 gzip。

- 建议不要配置

- 默认值 ： gzip_disable 'msie6MSIE \[4-6\]\\.MSIE 6.0'

```markdown
location / {

gzip off ; # 开启 gzip 压缩

gzip_buffers 32 4k ; # 设置缓冲区大小

gzip_comp_level 5; # 设置压缩等级 1-9

gzip_disable 'msie6MSIE [4-6]\.MSIE 6.0'; # 禁止哪些浏览器不使用压缩

gzip_http_version 1.1; # 设置压缩所需要的最低的 http 版本。

gzip_min_length 20 ; # 设置响应的数据最小限制，在这个限制之后再回进行压缩

gzip_vary on ; # 增加一个 header ，适用于老的浏览器 Vary:Accept-Encoding

gzip_proxied any; # 无条件启动压缩

# 哪些 mime 类型的文件进行压缩

#gzip_types text/plain application/x-javascript text/css application/xml;

gzip_types

text/xml application/xml application/atom+xml application/rss+xml application/xhtml+xml image/svg+xml

text/javascript application/javascript application/x-javascript

text/x-json application/json application/x-web-app-manifest+json

text/css text/plain text/x-component

font/opentype application/x-font-ttf application/vnd.ms-fontobject

image/x-icon;

}
```

### 3.3 gzip 的请求

![Alt text](image-2.png)

- 当启动了 gzip，我们的请求到 nginx 服务器上，nginx 就已经给我们生产了 response heard 但是数据还没有生成，他也不知道具体数据有多大，因为 nginx 是异步响应式请求，他一步一步来的，他先把 header 准备好然后请求内容去压缩，最后将两块内容合并去压缩，最后发过来，也就是因为异步导致他不知道具体大小。

- 他是先将请求头返回然后数据在慢慢读。

```markdown
----------------------------------响应体-------------------------------------------------

Connection: keep-alive

Content-Encoding: gzip # 结果启动了 gzip 压缩

Content-Type: application/json # 响应结果

Date: Mon, 13 Feb 2023 09:13:19 GMT

Keep-Alive: timeout=65

Server: nginx/1.20.2

Transfer-Encoding: chunked # 传输的格式这个对应的就是 length，这个是他会发送一个一个的包，当最后一个包是 0 表示传输结束

Vary: Accept-Encoding

------------------------------------请求头-----------------------------------------------

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,_/_;q=0.8,application/signed-exchange;v=b3;q=0.9

Accept-Encoding: gzip, deflate

Accept-Language: zh-CN,zh;q=0.9,en;q=0.8

Cache-Control: max-age=0

Connection: keep-alive

Host: 192.168.101.128

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
```

注意：以上是动态压缩就是所有的请求都会经历一次压缩，这个有一个致命的缺点就是不支持 sendfile，sendfile 是数据零拷贝，不会将数据加载到 nginx，而是通过网络接口传递数据，但是一旦开启了 gzip 动态压缩会导致 sendfile 失效，可以使用静态压缩。

在多层 Nginx 时，建议和服务器创建连接的 Nginx 进行开启 Gzip 就可以了，这样就会支持 gzip，在任意一台开启都是会开启的 gzip 的 。

### 3.4 静态压缩

![Alt text](image-3.png)

1.  #### 为什么要使用静态压缩呢？

首先动态压缩无法使用 sendfile 而静态压缩则完美的解决了这个问题。

静态压缩是一个互补或者说是一个扩展的功能，他可以把请求的这些资源文件，我们可以预先的将内容进行压缩成一个压缩包。

首先静态的资源一定是要比动态的资源要效率高，通过压缩之后可以减少磁盘的大小，并且还可以节约网络的通道资源。

2.  #### 什么是静态压缩

静态压缩不适合反向代理只适合资源服务器，他可以把压缩的文件传递给客户端，静态压缩就是在资源路径下会有一个资源文件还会有一个对应名称的压缩包。 并且 Nginx 会优先找压缩包，直接通过 sendfile 将数据传递过去。

Nginx 将压缩的文件通过网络发送过去，然后当浏览器接收到 Nginx 发送的压缩包文件，并进行解压缩的操作。他会在发送给客户端之前将压缩包接口在发送给客户端。

#### 3\. 配置

该 http_gzip_static_module 模块允许发送带有“”文件扩展名的预压缩文件，.gz 而不是常规文件。默认情况下不构建此模块，应使用 --with-http_gzip_static_module 配置参数启用它。这个模块没有在预编译的包里，需要手动添加，这个模块的作用就是把压缩包解压开

with 是内部模块，add 是外部的模块。

- 首次安装 nginx 时使用

> ./configure --prefix==/usr/local/nginx --with-hhtp_gzip_static_module  
> make && make install

- 已经安装过 nginx，对 nginx 客户端升级时使用命令

> ./configure --prefinx==/usr/local/nginx --with-http_gzip_static_module

make 不要 make install 否则会覆盖之前的文件

在将 objs 的 nginx 程序拷贝到 /usr/local/nginx/sbin 下·，注意需要做好原 nginx 程序备份 。

- 语法 ： gzip_static on | off | always;

- 作用：是否开启静态压缩功能。

- 参数值：

- on ：开启静态压缩，并会检测浏览器是否支持，如果不支持则不会走静态压缩，

- off ：关闭静态压缩

- always：是否使用静态压缩，无论浏览器是否支持静态压缩功能。

- 这样就会引发一个问题，如果客户端不支持，就解不开 ，如果磁盘上没有未压缩的文件默认会报 404，可以配合 [ngx_http_gunzip_module ，](http://nginx.org/en/docs/http/ngx_http_gunzip_module.html)模块使用。

- 默认值：gzip_static on

- 适用于 ：http、server、location

使用的需要将本地的资源文件进行压缩 ，压缩成 xxx.gz 的文件

```markdown
cd /usr/local/nginx/html

gzip \*
```

注意：开启之后默认就会先访问 .gz 的文件了，如果不支持 静态压缩则会访问 正常文件，如果没有正常的文件只有 .gz 那么就会报错 。

#### 4\. nginx_http_gunzip_module 模块

![Alt text](image-4.png)
这个模块是配合 gzip_static always 时使用的 ，因为 当配置程 always 时，所有的请求会都进行找压缩文件，在文件存不存在或者说浏览器支不支持 静态压缩，nginx 都会将静态压缩文件返回给浏览器，如果浏览器不支持的话会导致文件解不开，也就是 404 。

这个模块它没有在预编译的包里，需要手动添加，这个模块的作用就是把静态的压缩包解压开，他会在发送给客户端之前将压缩包接口在发送给客户端，它相当于是一层拦截器，它的作用就是可以把源文件进行压缩，我们可以把源文件进行删除了，节省磁盘空间，但是一般会用到。

注意 ： with 是内部 、 add 是外部的

安装命令 ：

> ./configure --prefix=/usr/local/nginx --add-module=/tools/nginx-sticky --with-http_gzip_static_module --with-http_gunzip_module
>
> make

如果是替换的话，则将这个文件中的这个文件 cp 到 nginx 的安装目录下的 sbin

![Alt text](image-5.png)
移动命令：

```markdown
cp /usr/local/nginx/sbin/nginx /usr/local/nginx/sbin/nginx.old2

cd /tools/nginx/objs

mv nginx /usr/local/nginx/sbin/
```

这里没有 gzip，但也没有 context-length 因为 nginx 需要把文件解压缩，他也不知道具体文件有多大，这个 gzip_static 适用场景 ：在作为 cdn 服务器或者 cdn 上游服务器文件存储服务器时，我们就可以把本地原始文件删了，只展示 zip 包，把解压缩的压力丢弃给客户端 ， 同时可以把本地压缩等级，提高不是 gzip 的压缩等级 ，经常高配访问的一些页面 css js ，也可以通过 static 压缩。

![Alt text](image-6.png)
静态压缩 响应结果会有 Context-Encoding : gzip 、Conten-Length：392 有展示 context-length 表示他开启了静态压缩，预压缩直接返回 zip 包 没有源文件 ，1.速度快，2 节省服务器资源。

## 四、Brotli

Brotli 是 Google 推出的开源压缩算法，通过变种的 LZ77 算法、Huffman 编码以及二阶文本建模等方式进行数据压缩，与其他压缩算法相比，它有着更高的压缩效率，性能也比我们目前常见的 Gzip 高 17-25%，可以帮我们更高效的压缩网页中的各类文件大小及脚本，从而提高加载速度，提升网页浏览体验。需要说明的是 Brotli 压缩只在 https 下生效，因为 在 http 请求中 request header 里的 Accept-Encoding: gzip, deflate 是没有 br 的。

Brotli 如此高的压缩比率，得益于其使用一个预定义的字典，该字典包含超过 13000 个来自文本和 HTML 文档的大型语料库的常用字符串，预定义的算法可以提升较小文件的压缩密度，而压缩与解压缩速度则大致不变。

Brotli 凭借它优异的压缩性能迅速占领了市场，从下图可以看到，除了 IE 和 Opera Mini 之外，几乎所有的主流浏览器都已支持 Brotli 算法，因此处于资源占用的考虑，比如说流量，建议启用：

Brotil 规范由 Google 员工 Jyrki Alakuijala 和 Zoltan Szabadka 于 2013-2016 开发，并伴随着规范的俩个作者 Evgenii Kuliuchniko 和 Lode Vandevenne 共同开发的参考实现，后者之前开发了谷歌的 zopfli 在 2013 年重新实现了收缩 /gzip 压缩格式。与 zopfli 不同，后者是对现有数据格式规范的重新实现，Brotli 是一种新的数据格式，并允许作者进一步提高压缩比。

### 4.1 Brotli 概述

- Brotli 的编码器提供了 12 个质量级别 （从 0 到 11）。它们是压缩速度换取压缩效率的压缩模式：更高质量的几倍速度较慢，但会产生更好的压缩比。

- 一个 Brotli 压缩文件由 元块（meta-blocks）集合组成。每个元块最多可容纳 16 MiB，由俩部分组成：一个 数据部分（data part），它存储 LZ77 压缩的放入快，以及一个 标题（header），每个块的压缩遵循经典的 ①LZ77 压缩方案并由 ② 计算具有良好的 LZ77 解析和计算 LZ 短语的简洁编码这俩个主要阶段组成。

- 它效率高是因为内置了 n 多个字典，包含都是一些常见的文件文件 css 、js 等等一些标签，如果我们将这些标签归类生成一个字典之后，我们就可以按照序号去解压这个文件了。

- 并且它在 Nginx 中话是可以和 Gzip 共存，开启了 Brotli 不会导致 Gzip 失效，如果浏览器支持 brotli 那么优先使用 Brotli ，不支持在使用 Gzip。

### 4.2 Brotli 的安装

\--add-dynamic-module 表示动态的引入模块在配置文件中还需要单独加入 load_module path/xxx

- 官网

- [https://github.com/google/ngx_brotli](https://github.com/google/ngx_brotli)

- [https://codeload.github.com/google/brotli/tar.gz/refs/tags/v1.0.9](https://codeload.github.com/google/brotli/tar.gz/refs/tags/v1.0.9)

- 下载 俩个项目

- 解压缩

- brotli-1.0.9 是 brotli 算法模块，需要先解压。

- tar -zxvf brotli-1.0.9.tar.gz

- ngx_brotli-1.0.0rc 是 nginx 的 brotli 的模块。这模块里需要引入 brotli 算法模块

- tar -zxvf ngx_brotli-1.0.0rc.tar.gz

- 接下来讲 brotli 的内容全部 复制到 ngx_brotli 的 deps/brotli/目录

- cd /tools/brotli-1.0.9

- cp -r \* /tools/ngx_brotli-1.0.0rc/deps/brotli/

模块化编译 ：

```markdown
./configure --with-compat --add-dynamic-module=/tools/ngx_brotli-1.0.0rc --prefix=/usr/local/nginx/
```

或

\--add-dynamic-module=brotli 目录

加载所有的压缩模块

```markdown
./configure --with-compat --add-dynamic-module=/tools/ngx_brotli-1.0.0rc --prefix=/usr/local/nginx/ --add-module=/tools/nginx-sticky --with-http_gzip_static_module --with-http_gunzip_module
```

- make && make install

- 下载的两个模块 拷贝到 /usr/local/nginx/modules/

![Alt text](image-7.png)

- 首先在 /usr/local/nginx 创建一个 modules 文件夹 mkdir modules

- mv ngx_http_brotli_filter_module.so ngx_http_brotli_static_module.so /usr/local/nginx/modules/

- 最后将新编译的 nginx 启动程序复制到 /usr/local/nginx/sbin 下 做好之前程序复制。

- cp /usr/local/nginx/sbin/nginx /usr/local/nginx/sbin/nginx.oid3

- mv /tools/nginx-12.0/objs/nginx /usr/local/nginx/sbin/

- 在配置文件中动态加载模块

```markdown
load_module "/usr/local/nginx/modules/ngx_http_brotli_filter_module.so";

load_module "/usr/local/nginx/modules/ngx_http_brotli_static_module.so";
```

### 4.3 配置选项

具体的配置选项可以查看 GitHub： [https://github.com/google/ngx_brotli](https://github.com/google/ngx_brotli)

brotli 的配置可以参考 Gzip 的配置，几乎一致。

- brotli

- 语法：brotli on | off

- 默认值 ：brotli off

- 适用于： http、server、location、if

- 作用：开启或者禁用 brotli 压缩功能。

- brotli_static

- 语法：brotli_static on | off | always

- 默认值：brotli_static off

- 适用于：http、server、location

- 作用：brotli 也是支持预先压缩文件，启用或禁用检查是否存在带扩展名的预压缩文件.br 。使用该 always 值，在所有情况下都使用预压缩文件，而不检查客户端是否支持它。

- brotli_types

- 语法：brotli_types <mime_type> \[...\]

- 默认值：brotli_types text/html

- 适用于： http、server、location

- 作用：指定哪些资源类型需要进行压缩操作，特殊值\*匹配任何 MIME 类型。

- brotli_buffers

- 语法：brotli_buffers <number> <size>

- 默认值： 32 4k | 16 8 k

- 适用于： http、server、location

- 作用：设置压缩缓冲区大小，最新版本以及弃用了 。

- brotli_comp_level

- 语法：brotli_comp_level <level>

- 默认值 ：6'

- 适用于 ： http、server、location

- 作用 ： 设置即时压缩 Brotli 质量（压缩）level。0 可接受的值在从到 的范围内 11。

- brotli_window

- 语法：brotli_window <size>

- 默认值 ： 512k

- 适用于 ：http、server、 location

- 作用：设置 Brotli 窗口 size。可以比作是一个桌子，将要压缩的文件同时放在这个桌子上，这个桌子上可以放多少文件的大小，这个值也不越大越好，他比较占内存，值增加建议是 2 的倍数，可接受的值为 1k, 2k, 4k, 8k, 16k, 32k, 64k, 128k, 256k, 512k, 1m, 2m,和 4m。8m 16m

- brotli_min_length

- 语法：brotli_min_length <length>

- 默认值：20

- 适用于： http、server、location

- 作用：指定进行压缩的文件最小的长度，如果小于这个值则不压缩。

```markdown
#加载动态模块

load_module "/usr/local/nginx/modules/ngx_http_brotli_filter_module.so";

load_module "/usr/local/nginx/modules/ngx_http_brotli_static_module.so";

worker_processes 1;

events {

worker_connections 1024;

}

http {

server {

listen 80;

server_name localhost;

location / {

#brotli 配置

brotli on; # 开启 压缩

brotli_static on; # 是否开启预先压缩，开启之后就会 .br 的压缩包

brotli_comp_level 6; # 压缩等级

brotli_buffers 16 8k; # 缓冲区大小 ，已经启用

brotli_min_length 20; # 压缩时文件最小限制

# 对哪些 mime.types 类型进行压缩

brotli_types text/plain text/css text/javascript application/javascript text/xml application/xml application/xml+rss application/json image/jpeg image/gif image/png;

}

}

}
```

### 4.4 brotli 测试

因为默认 brotli 是必现 https 请求才能使用的，因为 http 的请求 请求头的 Accept-Encoding 是没有 br 的，所以服务器是无法知道客户端可以使用的。

测试方案：

使用 linux 的 curl 命令 ：

```markdown
curl -H 'Accept-Encding : br' -I 192.168.101.128/index.html
```

```markdown
[root@localhost sbin]# curl -H Accept-Encoding:br -I http://192.168.101.128/static_page.html

HTTP/1.1 200 OK

Server: nginx/1.20.2

Date: Fri, 17 Feb 2023 08:11:05 GMT

Content-Type: text/html

Last-Modified: Fri, 17 Feb 2023 03:28:14 GMT

Connection: keep-alive

Keep-Alive: timeout=65

Vary: Accept-Encoding

ETag: W/"63eef44e-31"

Content-Encoding: br

[root@localhost sbin]# curl -I http://192.168.101.128/static_page.html

HTTP/1.1 200 OK

Server: nginx/1.20.2

Date: Fri, 17 Feb 2023 08:11:54 GMT

Content-Type: text/html

Last-Modified: Fri, 17 Feb 2023 03:28:14 GMT

Connection: keep-alive

Keep-Alive: timeout=65

Vary: Accept-Encoding

ETag: W/"63eef44e-31"
```
