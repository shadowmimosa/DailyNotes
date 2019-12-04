<font size=4 face='楷体'>

## Fiddler 部分出现 tunnel to 443

首先排除是不是全部 HTTPS 都抓不到，如果全部都抓不到那应该是没有设置好，参考[这里]()

如果设置好，能抓到 HTTPS 了，仍然出现 tunnel to 443，才是本文讨论的问题

### connect 方法

出现 tunnel to, 即使用的是 http connect 方法

> connect 是为了建立 http tunnel，connect 是 http 众多方法中的其中一种，它跟 post、get、put、options 方法是并列的。但是它的使用场景很特殊。

> 只有在受限制的网络环境中（防火墙、NAT、代理器）并且是 https 通信时，客户端使用 http connect 请求代理服务器，代理服务器使用 connect 方法与目标服务器建立 http tunnel，通道建立后，客户端与服务器进行通信，代理服务器就像透明一样，只是接收、转发 tcp stream。

<!-- > 锁表示是使用 HLS 协议访问（就是 HTTP 变成 HTTPS），HTTP 的默认端口是 80，HTTPS 的默认端口是 443。
> 火狐浏览器抓不到 443，说明火狐浏览器没有自动使用 HTTPS 协议访问服务器（同时说明服务器即支持 HTTP 也支持 HTTPS）
> HLS 是一种安全的 HTTP 协议（可以简单这样理解），HTTP 在网络上传输的都是明文（甚至会包括你登录某个网站的密码），而 HLS 是经过加密的。 -->

> 为什么要建立 http tunnel 呢？
> 这是因为，网络环境受限，客户端无法直接访问某些网络，所以只能通过代理服务器访问网络，然后，将内容转发给客户端，从宏观上看，客户端与服务器端就像建立了一条隧道一样。
> 但是由于 http tunnnel 可控性不强，所以，服务器通常会限制”可 connect 的端口”(一般只开放 SSL 的 443 端口)

> connect：要求用隧道协议连接代理
> connect 方法要求在与代理服务器通信时建立隧道，实现用隧道协议进行 tcp 通信。主要使用 SSL 和 TLS 协议把通信内容加密后经网络隧道传输。

### fiddler 出现 connect tunnel 连接

如果理解了上边的话，那么也就明白了为什么 fiddler 抓包时，出现大量 connect 连接

> 因为 fiddler 是代理，访问百度网页（使用了 https 协议），满足了使用 connect 条件，所以客户端会使用 connect 方法与目标服务器建立 http tunnel，一旦 connection 建立完成，后续 fiddler 会转发、接收所有的 tcp stream。

> 当然，并不是所有的受限网络(restricted network)，https 通信时，都会使用 connect 建立 http tunnel，如果目标服务器限制 connect 方法，那么就会使用其它方法来建立通道（post/get）；如果服务器不支持 http tunnel,那么就需要安装 http tunnel server 端的程序，客户端不支持 http tunnel，那么客户端就需要安装 http tunnel client 程序；http tunnel 程序包含两部分，server 端程序和 client 端程序；

### 解决

解决是解决不了了，网上好多插入脚本的方法屏蔽，这里想说一句

> 如果不想显示 Connect，你也可以设置 rules----->hide connects 隐藏 connect

完美

### Reference

[http tunnel && http connect method](https://blog.csdn.net/wangjun5159/article/details/54142016)
[fiddler pc https 抓包](https://blog.csdn.net/wangjun5159/article/details/52198842)

**2019.12.04**
