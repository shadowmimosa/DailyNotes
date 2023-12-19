---
created: 2023-12-06T17:23:07 (UTC +08:00)
tags: [Nginx,Docker,编程]
source: https://zhuanlan.zhihu.com/p/558474386
author: 
---

# 借助 Docker 来搭 Nginx 的积木：快速实现高性能二维码服务 - 知乎

> ## Excerpt
> 本篇文章，依旧是聊聊如何 “使用 Nginx 和 Docker 来偷懒”。以生成我们常见的二维码为例，聊聊 Nginx 在日常业务中，除了做接入层业务之外的应用。 本篇文章中，我们将侧重聊聊更通用的，在容器场景下借助 Docke…

---
本篇文章，依旧是聊聊如何 “使用 Nginx 和 Docker 来偷懒”。以生成我们常见的二维码为例，聊聊 Nginx 在日常业务中，除了做接入层业务之外的应用。

本篇文章中，我们将侧重聊聊更通用的，在容器场景下借助 Docker 的预构建、多阶段构建等能力，来帮助 Nginx 进行“搭积木”的玩法，快速实现某个传统业务。

## **写在前面**

触动我写下这篇内容的主要原因有三：

1.  我最近做的事情，需要大量的二维码，综合考虑，目前使用服务端生成会合适些，至于服务端生成有哪些好处，稍后我们聊。
2.  Nginx 最近曝出**[安全漏洞\[1\]](https://link.zhihu.com/?target=http%3A//nginx.org/en/security_advisories.html)**，会影响低版本（v1.20.1）之前的应用，以往的实践内容需要“更新”。
3.  受 CSDN 的一位老师邀请在一个小圈子里做一个简短的技术分享，这周事情比较多，这个原本积累素材就不少、最近又被激活了的话题，比较适合我在开始分享前一个小时“完成 PPT”，避免失言。

就二维码场景而言，我曾写过一些相关的内容和例子，如果你是我的老读者，或许会对下面这几篇内容有印象。

-   (2021.01) **[《使用 Docker 和 Nginx 打造高性能二维码服务（二）》\[2\]](https://link.zhihu.com/?target=https%3A//soulteary.com/2021/01/07/use-docker-and-nginx-to-build-high-performance-qr-code-services-2.html)**
-   (2018.12) **[《使用 Docker 和 Node 快速实现一个在线的 QRCode 解码服务》\[3\]](https://link.zhihu.com/?target=https%3A//soulteary.com/2018/12/09/use-docker-and-node-to-quickly-implement-an-online-qrcode-decoding-service.html)**
-   (2018.10) **[《使用 Docker 和 Nginx 打造高性能的二维码服务》\[4\]](https://link.zhihu.com/?target=https%3A//soulteary.com/2018/10/19/use-docker-and-nginx-to-build-high-performance-qr-code-services.html)**

以及，可能对下面这两篇聊 “Nginx 三方模块”的内容感兴趣：

-   (2021.03) **[《如何在容器时代高效使用 Nginx 三方模块》\[5\]](https://link.zhihu.com/?target=https%3A//soulteary.com/2021/03/22/how-to-use-nginx-third-party-modules-efficiently-in-the-container-era.html)**
-   (2021.03) **[《Nginx 模块系统：前篇》\[6\]](https://link.zhihu.com/?target=https%3A//soulteary.com/2021/03/05/nginx-module-system-part-1.html)**

本篇内容，将会更侧重“白盒化”、“容器和 Nginx 的模块组合”部分。完整的项目代码，我也已经上传至 GitHub：**[soulteary/nginx-qrcode-server\[7\]](https://link.zhihu.com/?target=https%3A//github.com/soulteary/nginx-qrcode-server)**，有需要可以自取。

相信耐心读完，你一定会有所收获。

## **二维码的业务场景**

二维码的出现比 JavaScript 创造出来还早一年（1994年被创造），这个有趣的小东西，在我们如今的日常生活中随处可见：每天掏出手机扫支付码、不时需要的扫码认证登录、下馆子想了解还需要排多久队的二维码、出入各种场合需要扫一下代表自己健康状况，包含了特别信息的“特别的”二维码等等。

![](https://pic3.zhimg.com/v2-9e48ee8e1c675d117bd6850c9489baba_b.jpg)

无处不在的二维码

它的工作原理并不复杂，陈皓大叔的**[一篇老文章\[8\]](https://link.zhihu.com/?target=https%3A//coolshell.cn/articles/10590.html)**中有提到过，我就不赘述了。

在聊怎么让“Docker 和 Nginx 结婚，生出二维码这个孩子”之前，先聊聊它的几种生成方式。

## **二维码的常见生成方式**

按照生成环境和方式来区分，二维码的生成场景主要有三种：服务端、客户端（含前端）、CLI 生成（常用于非实时场景）。

![](https://pic1.zhimg.com/v2-f17b110c11d16800eb1866addf989afc_b.jpg)

常见二维码生成方式

在多数场景下，我们会使用客户端生成的方式，因为这对于产品团队而言，是 **“最经济实惠”** 的方案：

-   不需要依赖网络带宽、不浪费网络流量，能够节约大量的成本
-   使用客户（用户）的 CPU，不占用服务器资源，能够节约不少计算成本
-   因为是本地生成，不需要网络传输，用户看到二维码普遍比“服务端生成+传输”快

但在一部分场景下，我们不方便使用“经济实惠”的客户端生成方案。就需要使用到服务端生成的方式啦，比如：

-   我们希望客户端（包括前端）的业务代码实现更简单一些，“引个图片就完事了”
-   或者，受到平台/环境场景限制，本地生成二维码的代码不好使了，不得不使用服务端在线生成的图片来替换本地生成的结果
-   再或者，在客户端部分场景，我们希望这个产品功能能够具备一定的灵活性，能够“动态化”起来。可以按照服务端的规则来玩，避免因为这类非核心逻辑的变化，带来不必要的“客户端升级版本”这类比较重的操作
-   还有，如果我们希望得到准确的二维码“访问日志”，进行一些额外的数据分析，最简单的方式就是借助服务端的力量啦

除了上面两类生成方案外，有些时候我们也会借助本地的工具来预先生成一些更复杂的二维码产物：带有特别设计风格的二维码、包含一段有趣动画效果的动图二维码、融合在视频里的二维码等等。

这个场景和上面两种场景的差别主要在于是否能够提供较高的**实时性**。当然，我们也可以借助前两种生成的方式，将结果存储下来以备后用。比如，借助 Puppeteer 或者客户端的 View 截图的方式，将前端生成的结果进行保存。总的来说，这类场景下的综合成本比较高，生成产物的时间较长，需要依赖较多的计算资源，不太适合进行日常业务，比较适合“离线”场景，比如一些广告、纸质印刷物等。试想一下，当你在家门口扫排队扫码“续保”、或者进入小区的时候，用这个方式生成的二维码转出来要转个大几十秒到一分钟，这个队伍得排到多长。

**每种方式都有各自的适用场景，需要结合自己的业务场景来玩。** 我们来继续来聊聊服务端生成。

## **服务端生成**

在服务端生成的场景下，因为使用的是自己的计算、存储、网络资源，所以我们一定是希望它是“多快好省”的。以生成二维码这个功能举例，我们可以拿 Java 和 Nginx 实现来做一个简单的比较（会存在一些不公平、比如网络请求处理、框架消耗、编译预热）

![](https://pic4.zhimg.com/v2-cd32e9dfd38ef00e7b8c0d8172107783_b.jpg)

一个不太严谨的比较

简单来说，Nginx 的性能表现会好过 Java 版本；站在资源利用的角度，Nginx 实现的简单应用，不论是 CPU 利用率、内存消耗、应用分发使用的容器镜像包体积也会远小于 Java 实现。

但是，从复杂性角度来说，一般情况下，两者其实是“差不多”的，因为前者公开的文档、参考资料非常多，实际业务里有固定组合，一般情况下，业务中也会有不少积累的“老代码”和“基础设施”可用，我们只需要完成“二维码生成”这部分功能，以及不断优化连接和缓存策略就能够解决 80% 的问题。

而 Nginx 目前的文档资料相对少不少，对于多数开发者存在“黑盒”，即使大概率我们只会用到它的一两个模块，同样是固定组合，这里面的“不确定性”依旧很高。但是，**当我们解决了这些问题之后，你会发现“用 Nginx 来偷懒”，真香。**

我们在曾经的业务中，用 Nginx 做过不少业务尝试，比如在短时间几十万人次使用的直播会议中，借助 Nginx 配合 embed runtime（PHP、JS）做基础业务逻辑、高频次的配置接口调用、生成二维码、进行身份验证、做一些带业务逻辑的打点统计、实现简易的 WAF 等...绝大多数场景只需要一两台机器，起几个容器就足够了。

让我们来看看，怎么才能够放心的、省心的用 Nginx 做简单业务呢？

## **容器时代的偷懒方式：寻找确定性**

使用 Nginx 进行业务开发，面临的最大的“黑盒场景”在于需要在不同的操作系统、不同的 Nginx 版本和软件依赖下进行“构建编译”，得到的产物即便是 DSO（ Nginx 动态模块），也不一定具备向前/向后兼容性。尤其是有一些模块的使用，还需要对 Nginx 打额外的代码补丁。

但是解决环境的不确定问题，不正是 Docker 的优势嘛！

![](https://pic4.zhimg.com/v2-918966c11eb0665b88cd7872def5741b_b.jpg)

寻找确定性

我们对 Nginx 官方镜像、不同版本、不同系统镜像的 Nginx 构建方式进行分析，然后搭配 Docker ，是完全可以将 “构建环境”、“运行环境” 都做到完全确定的：复用官方镜像进行构建、复用官方镜像进行应用运行。这部分包含了 80% 我们讨厌的不确定性：

•编译模块和 Nginx 的环境，不一定和运行环境完全一致，存在基础依赖不同的问题，可能会引发兼容性问题。•按照各自公开文档、历史资料来做的话，我们的编译命令，和官方版本可能存在一些差异，这也可能存在一些兼容或者性能问题。•运行环境和官方经过严密测试的容器环境，有比较大的差别，不确定我们的产物是否能够像官方镜像一样 “长命百岁”。

为了解决这个问题，我制作了一个基于 Nginx 官方镜像的快速开发环境，使用了官方镜像使用的构建命令，来帮助我们在一个和“Nginx 官方团队”一致的环境中构建我们自己的业务模块：**[nginx-with-docker/nginx-docker-playground\[9\]](https://link.zhihu.com/?target=https%3A//github.com/nginx-with-docker/nginx-docker-playground)**

这个项目自 Nginx 1.19.7 开始维护，目前已经支持到了最新的 Nginx 1.23.1，使用这个镜像来构建 Nginx 三方模块，通常只需要复制粘贴一些“模版代码”，然后执行 `docker build` 就能够得到包含模块产物的新的 Nginx 镜像啦。

在解决了不确定性的大头后，我们来处理剩下的小细节：如何解决“模块代码”、“Nginx不同版本”排列组合间的不确定性。

## **让容器构建的模块更“清晰透明”**

既然跨 Nginx 版本的模块使用，可能存在一些兼容问题，那么就别玩跨版本的软件排列组合了。我们就老老实实的一个 Nginx 版本，构建一套镜像模块就行了，兼容性妥妥的。尤其是在使用上面提到的 “nginx-docker-playground” 搞定构建都是分分钟内的事儿，生成 Nginx 应用镜像也都是秒级操作（下文详述）。

以最近更新的一个模块为例（**[nginx-with-docker/ngx\_http\_srcache\_filter\_module\[10\]](https://link.zhihu.com/?target=https%3A//github.com/nginx-with-docker/ngx_http_srcache_filter_module)**）：

```bash
├── LICENSE ├── README.md ├── docker │ ├── 0.32 │ │ ├── Dockerfile.alpine │ │ └── Dockerfile.debian │ └── master │ ├── Dockerfile.alpine │ └── Dockerfile.debian ├── make-image.sh └── push-image.sh
```

上面是这个 Nginx 模块的项目目录结构，在 `docker` 目录中的两个目录，分别是上游仓库最后的稳定版本号“0.32”以及包含了 0.32 版本之后的各种改动的分支（没有打版本号）。

在这两个子目录中，分别有一个 `.env` 文件，包含了类似下面的内容：

```bash
NGINX_VERSION=1.23.1 MODULE_CHECKSUM=8a841d5797a33b5676433bb85998d11a429caac3 MODULE_VERSION=master MODULE_NAME=srcache-nginx-module-src MODULE_SOURCE=https://github.com/nginx-with-docker/srcache-nginx-module-src
```

通过将 Nginx 版本、Nginx 代码的校验值等参数进行抽象，再配合一段简单的小脚本，我们就能够自动的完成不同 Nginx 版本、不同模块代码版本、甚至是不同依赖版本的容器产物构建啦：

```bash
#!/bin/bash PROJECT_NAME="srcache" RELEASE_DIR="./docker"; REPO_NAME="soulteary/prebuilt-nginx-modules" for subVer in $RELEASE_DIR/*; do set -a . "$subVer/.env" set +a REPO_TAG="ngx-$NGINX_VERSION-$PROJECT_NAME-$MODULE_VERSION"; BUILD_ARGS=$(tr '\n' ';' < "$subVer/.env" | sed 's/;$/\n/' | sed 's/^/ --build-arg /' | sed 's/;/ --build-arg /g') if [ -f "$subVer/Dockerfile.alpine" ]; then BUILD_NAME="$REPO_NAME:$REPO_TAG-alpine" if [[ "$(docker images -q $BUILD_NAME 2> /dev/null)" == "" ]]; then echo "Build: $BUILD_NAME"; docker build $BUILD_ARGS --tag $BUILD_NAME -f $subVer/Dockerfile.alpine . fi fi if [ -f "$subVer/Dockerfile.debian" ]; then BUILD_NAME="$REPO_NAME:$REPO_TAG" if [[ "$(docker images -q $BUILD_NAME 2> /dev/null)" == "" ]]; then echo "Build: $BUILD_NAME"; docker build $BUILD_ARGS --tag $BUILD_NAME -f $subVer/Dockerfile.debian . fi fi done
```

如果你想了解更多的内容，可以翻阅两年前的一篇博客：《**[如何在容器时代高效使用 Nginx 三方模块\[11\]](https://link.zhihu.com/?target=https%3A//soulteary.com/2021/03/22/how-to-use-nginx-third-party-modules-efficiently-in-the-container-era.html)**》。

编译是编译完了，那么要如何在容器中使用这类构建好的模块呢？

最复杂的模块构建搞定之后，想完成我们之前提到的“Nginx 应用镜像”，就只剩下 Nginx 应用镜像的组装了。

和前文中提到的折腾“Nginx 模块”复制粘贴模版代码类似，组装 Nginx 应用镜像，说白了也是一种“复制粘贴”，将我们已经在某个版本环境下的构建产物，复制粘贴到新的目标镜像里，这种多个 “FROM” 阶段的产物传递，在 Docker 操作术语中被称作“多阶段构建”。

![](https://pic2.zhimg.com/v2-5816e591318d00fbc20da6125f6f0ba9_b.jpg)

来！搭积木

前文中提到过，因为我们的构建环境、运行环境都是基于 Nginx 官方镜像来的，所以通过这么一通“多阶段构建”，得到的结果自然也会比我们使用 “Ubuntu、Centos” 等自己喜爱的基础镜像，从零到一构建 Nginx 和模块，要来的靠谱，因为除了模块产物之外，我们没有引入“任何额外的风险”。

## **体验基于 Nginx 的二维码服务**

为了我的读者，能够直接体验本文开头提到的二维码服务，我做了一个开箱即用的 Docker 镜像。

![](https://pic2.zhimg.com/v2-758d9dfaae0e426d9226e6d801054135_b.jpg)

开箱即用的二维码服务器

感兴趣的同学可以使用 `docker run --rm -it -p 8080:80 soulteary/nginx-qrcode-server` 跑跑看。

通过改变请求参数，就能够快速的生成不同的二维码，完成我们提到的基础业务场景中的功能了。如果你需要在生产环境中使用，项目中有搭配本地缓存使用的例子，在我的本地笔记本上，启用缓存，每秒的 QPS 能够超过 6 万。

## **最后**

虽然通过 Docker 预构建、多阶段构建这类方法，可以解决我们遇到的多数问题，但毕竟 Nginx 模块的开发、维护、调试成本都还是很高的，我们普遍需要和 C/C++ 打交道。

随着业务越来越复杂，交付时间的要求越来越高，我们一定是需要更快的、更轻量、更灵活的方案。

![](https://pic4.zhimg.com/v2-7231ad8a2bc409d81f6d7ddd5f621193_b.jpg)

或许，Nginx 模块化的未来

Nginx 推出 NJS 有一段时间了，因为各种原因，虽然目前发展没有想象中的快速，但是未来的想象力还是比较大的。我曾经写过一篇博客，感兴趣可以自行阅读**[《使用 Docker 和 Nginx NJS 实现 API 聚合服务（前篇）》\[12\]](https://link.zhihu.com/?target=https%3A//soulteary.com/2021/03/18/use-docker-and-nginx-njs-to-implement-api-aggregation-service-part-1.html)**，或者参考上面的图片中的链接进行更多的了解。

除此之外，近两年 WebAssembly（WASM）的热度也越来越高，尤其是在边缘计算场景中，有一些开源产品公司也推出一些相关的产品，各种语言相关的结合应用也层出不穷。或许这会是替代 Nginx + Embed Runtime（V8、PHP、Java、JS、Lua）的一个关键转折。

对 Nginx 的未来充满期待。

\-EOF

___

### **引用链接**

`[1]` 安全漏洞: _[http://nginx.org/en/security\_advisories.html](https://link.zhihu.com/?target=http%3A//nginx.org/en/security_advisories.html)_  
`[2]` 《使用 Docker 和 Nginx 打造高性能二维码服务（二）》: _[https://soulteary.com/2021/01/07/use-docker-and-nginx-to-build-high-performance-qr-code-services-2.html](https://link.zhihu.com/?target=https%3A//soulteary.com/2021/01/07/use-docker-and-nginx-to-build-high-performance-qr-code-services-2.html)_  
`[3]` 《使用 Docker 和 Node 快速实现一个在线的 QRCode 解码服务》: _[https://soulteary.com/2018/12/09/use-docker-and-node-to-quickly-implement-an-online-qrcode-decoding-service.html](https://link.zhihu.com/?target=https%3A//soulteary.com/2018/12/09/use-docker-and-node-to-quickly-implement-an-online-qrcode-decoding-service.html)_  
`[4]` 《使用 Docker 和 Nginx 打造高性能的二维码服务》: _[https://soulteary.com/2018/10/19/use-docker-and-nginx-to-build-high-performance-qr-code-services.html](https://link.zhihu.com/?target=https%3A//soulteary.com/2018/10/19/use-docker-and-nginx-to-build-high-performance-qr-code-services.html)_  
`[5]` 《如何在容器时代高效使用 Nginx 三方模块》: _[https://soulteary.com/2021/03/22/how-to-use-nginx-third-party-modules-efficiently-in-the-container-era.html](https://link.zhihu.com/?target=https%3A//soulteary.com/2021/03/22/how-to-use-nginx-third-party-modules-efficiently-in-the-container-era.html)_  
`[6]` 《Nginx 模块系统：前篇》: _[https://soulteary.com/2021/03/05/nginx-module-system-part-1.html](https://link.zhihu.com/?target=https%3A//soulteary.com/2021/03/05/nginx-module-system-part-1.html)_  
`[7]` soulteary/nginx-qrcode-server: _[https://github.com/soulteary/nginx-qrcode-server](https://link.zhihu.com/?target=https%3A//github.com/soulteary/nginx-qrcode-server)_  
`[8]` 一篇老文章: _[https://coolshell.cn/articles/10590.html](https://link.zhihu.com/?target=https%3A//coolshell.cn/articles/10590.html)_  
`[9]` nginx-with-docker/nginx-docker-playground: _[https://github.com/nginx-with-docker/nginx-docker-playground](https://link.zhihu.com/?target=https%3A//github.com/nginx-with-docker/nginx-docker-playground)_  
`[10]` nginx-with-docker/ngx\_http\_srcache\_filter\_module: _[https://github.com/nginx-with-docker/ngx\_http\_srcache\_filter\_module](https://link.zhihu.com/?target=https%3A//github.com/nginx-with-docker/ngx_http_srcache_filter_module)_  
`[11]` 如何在容器时代高效使用 Nginx 三方模块: _[https://soulteary.com/2021/03/22/how-to-use-nginx-third-party-modules-efficiently-in-the-container-era.html](https://link.zhihu.com/?target=https%3A//soulteary.com/2021/03/22/how-to-use-nginx-third-party-modules-efficiently-in-the-container-era.html)_  
`[12]` 《使用 Docker 和 Nginx NJS 实现 API 聚合服务（前篇）》: _[https://soulteary.com/2021/03/18/use-docker-and-nginx-njs-to-implement-api-aggregation-service-part-1.html](https://link.zhihu.com/?target=https%3A//soulteary.com/2021/03/18/use-docker-and-nginx-njs-to-implement-api-aggregation-service-part-1.html)_

___

如果你觉得内容还算实用，欢迎点赞分享给你的朋友，在此谢过。

如果你想更快的看到后续内容的更新，请戳 **“点赞”、“分享”、“喜欢”** ，这些免费的鼓励将会影响后续有关内容的更新速度。

___

此外，我们有一个小小的折腾群，里面聚集了一些喜欢折腾的小伙伴。

在不发广告的情况下，我们在里面会一起聊聊软硬件、HomeLab、编程上的一些问题，也会在群里不定期的分享一些技术沙龙的资料。

喜欢折腾的小伙伴，欢迎阅读下面的内容，扫码添加好友。

**添加好友，请备注实名和公司或学校、注明来源和目的，否则不会通过审核。**

___

本文使用「署名 4.0 国际 (CC BY 4.0)」许可协议，欢迎转载、或重新修改使用，但需要注明来源。 **[署名 4.0 国际 (CC BY 4.0)](https://link.zhihu.com/?target=https%3A//creativecommons.org/licenses/by/4.0/deed.zh)**

本文作者: 苏洋

创建时间: 2022年08月27日 统计字数: 7558字 阅读时间: 16分钟阅读 本文链接: [https://soulteary.com/2022/08/27/building-blocks-of-nginx-with-docker-quickly-implement-high-performance-qr-code-services.html](https://link.zhihu.com/?target=https%3A//soulteary.com/2022/08/27/building-blocks-of-nginx-with-docker-quickly-implement-high-performance-qr-code-services.html)
