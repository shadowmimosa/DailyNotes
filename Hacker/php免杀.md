<font size=4 face='楷体'>

## PHP 免杀木马

### 一句话木马

[一句话木马](一句话木马.md)

### 渗透测试

[渗透测试-一些 webshell 免杀的技巧](https://blog.csdn.net/lza20001103/article/details/127907054)

### 文件上传漏洞

[文件上传漏洞初探](https://www.jianshu.com/p/f53d6b8c575f)

### Webshell

[一句话木马上传（webshell）](https://www.cnblogs.com/xiaoxiaoxiaoz/p/16096397.html)
[一句话木马及文件上传](https://www.ngui.cc/article/show-113681.html?action=onClick)

### Webshell 管理工具

目前国内安全人员常用的有：中国菜刀、中国蚁剑、冰蝎、哥斯拉、Metasploit、SharPyShell 等，也有一些内部团队开发的类似工具，但是并没有对外公开。

**(1) 中国菜刀（Chopper）**

中国菜刀是一款专业的网站管理软件，用途广泛，使用方便，小巧实用。只要支持动态脚本的网站都可用它来进行管理！在非简体中文环境下使用自动切换到英文界面。UNICODE 方式编译，支持多国语言输入。已被各大安全厂商提取其特征。

![](https://pic3.zhimg.com/v2-9660d7ee1af14395326f9a0c543eedb2_b.jpg)

**(2) 中国蚁剑（AntSword）**

中国蚁剑是一款开源的跨平台网站管理工具，它主要面向于合法授权的渗透测试安全人员以及进行常规操作的网站管理员。任何人不得将其用于非法用途以及盈利等目的，否则后果自行承担！使用编/解码器进行流量混淆可绕过 WAF，并且有多款实用插件。

**项目地址：**

[https://github.com/AntSwordProject/antSword](https://link.zhihu.com/?target=https%3A//github.com/AntSwordProject/antSword)

![](https://pic4.zhimg.com/v2-4d17575e6f346c3af8db791f28236e87_b.jpg)

**(3) 冰蝎（Behinder）**

冰蝎是一款基于 Java 开发的动态二进制加密通信流量的新型 Webshell 客户端，由于它的通信流量被加密，使用传统的 WAF、IDS 等设备难以检测，目前在 HVV 中使用较多的一款工具。

**项目地址：**

[https://github.com/rebeyond/Behinder](https://link.zhihu.com/?target=https%3A//github.com/rebeyond/Behinder)

![](https://pic1.zhimg.com/v2-f095640b3bca56da9a6c6ce25b40f3c0_b.jpg)

**(4) 哥斯拉（Godzilla）**

哥斯拉是一款继冰蝎之后又一款于 Java 开发的加密通信流量的新型 Webshell 客户端，内置了 3 种有效载荷以及 6 种加密器，6 种支持脚本后缀，20 个内置插件，也是目前在 HVV 中使用较多的一款工具。

**项目地址：**

[https://github.com/BeichenDream/Godzilla](https://link.zhihu.com/?target=https%3A//github.com/BeichenDream/Godzilla)

![](https://pic2.zhimg.com/v2-95135aa8879417cc82020e86c9f7e641_b.jpg)

**(5) Web 版菜刀（w8ay）**

w8ay 是 Hacking8 安全信息流站长早些年用 PHP+MySQL 写的一款半成品一句话 WEB 端管理工具，目前完成的功能有：文件管理、自定义命令、多用户系统注册登陆，且仅支持对 PHP 的一句话进行操作。

**项目地址：**

[https://github.com/boy-hack/WebshellManager](https://link.zhihu.com/?target=https%3A//github.com/boy-hack/WebshellManager)

![](https://pic1.zhimg.com/v2-1d741975c898f122a93d21e2349b8fc0_b.jpg)

**(6) Web 版菜刀（WebKnife）**

WebKnife 是陌小离练习 ajax 时候写的一款半成品 Web 版菜刀，目前完成的功能有：文件管理，虚拟终端，文件查看，图片查看，一键挂黑，作者居然还是个 00 后，tql！

**项目地址：**

[https://github.com/MoLeft/WebKnife](https://link.zhihu.com/?target=https%3A//github.com/MoLeft/WebKnife)

![](https://pic2.zhimg.com/v2-12b53e6ed88195a82a12ecf71fb89dc9_b.jpg)

**(7) 一句话木马连接客户端**

ASP/PHP/JSP 一句话木马连接客户端，在中国菜刀还没出来之前用的都是这个，不知还有多少人记得、默认为 POST，在遇到一些特殊场景时也可以将其改为 GET。

![](https://pic4.zhimg.com/v2-71db414e3b96a2fa691e29754963b7fb_b.jpg)

**(8) XISE**

XISE 是小骏用易语言开发的一款类似于中国菜刀的 Webshell 网站管理工具，早些年做黑帽 SEO 的基本人手一份，现在已经停止更新，至于什么原因，大家都懂的！！！

![](https://pic1.zhimg.com/v2-708ae3daa2c319c6c36d9e333b881b04_b.jpg)

**(9) 开山斧**

开山斧是一款基于 Python 2.7X + QT4 开发的一款跨平台菜刀 (Win/Linux/Mac)，体积比较大，刚出来时只用过一次，现在用的人应该不多，也已经停止更新了。

项目地址：

[GitHub - pyqteval/evlal_win](https://link.zhihu.com/?target=https%3A//github.com/pyqteval/evlal_win)

![](https://pic3.zhimg.com/v2-8ecf0f9b0fae84e4254ce5e44e027c9e_b.jpg)

**(10) K8 飞刀**

K8 飞刀是 K8 哥哥开发的一款 Webshell 网站管理工具，不得不说他开发的安全工具都很强大且实用，只不过个人感觉略显臃肿，对新人来说可能不是很友好，有兴趣的可以自己去看一下。

**项目地址：**

[https://github.com/k8gege/K8tools](https://link.zhihu.com/?target=https%3A//github.com/k8gege/K8tools)

![](https://pic3.zhimg.com/v2-9e2d0d2dc34cf0d53837e0b1fd71560a_b.jpg)

**(11) Altman**

Altman 基于.Net4.0 开发，整个程序采用 mef 插件架构。目前完成的功能有：Shell 管理、命令执行、文件管理、数据库管理、编码器等，脚本类型支持 asp、aspx、php、jsp、python。

项目地址：

[https://github.com/keepwn/Altman](https://link.zhihu.com/?target=https%3A//github.com/keepwn/Altman)

![](https://pic1.zhimg.com/v2-32148e1991f6ebcd69f0f6345885575c_b.jpg)

**(12) Hatchet**

hatchet 基于 C++开发，是继中国菜刀后比较早放出来的一款 Webshell 网站管理工具，目前完成的功能有：文件管理、命令执行、数据库管理以及注册表读取等等，而且能够自定义部分 POST 数据，还支持同时剪切、删除和下载多个文件/文件夹。

**项目地址：**

[https://github.com/euphrat1ca/hatchet](https://link.zhihu.com/?target=https%3A//github.com/euphrat1ca/hatchet)

![](https://pic4.zhimg.com/v2-561bea2d2aebf1c1af2c7af2787754c3_b.jpg)

**(13) 小李飞刀**

小李飞刀基于 C#开发，一个还没开始就已经结束了的项目，只实现了简单的 Webshell 连接和文件管理功能，忘了当时是在哪找到的这套源码了，具体作者不详！

![](https://pic4.zhimg.com/v2-f8d0345fb943e8b3dea81db3a838721f_b.jpg)

**(14) AspxClient**

AspxClient 是一款基于反射的.NET 一句话木马连接客户端，仅支持 ASPX 脚本，算是比较老的一个工具了，在高版本 IIS 中连接时可能会出现一些问题。

![](https://pic1.zhimg.com/v2-e67da00822be5ce4d3b8d20bc4b2af48_b.jpg)

(15) C 刀（Cknife）

C 刀是一款基于 Java 开发的完全基于配置文件的中国菜刀，脚本类型支持 ASP、ASPX、PHP、JSP、JSPX、Customize，目前完成的功能有：文件管理、数据库管理、模拟终端以及代理设置等。

**项目地址：**

[https://github.com/Chora10/Cknife](https://link.zhihu.com/?target=https%3A//github.com/Chora10/Cknife)

![](https://pic2.zhimg.com/v2-fc9ffda664d8493b9831cea672d5f00d_b.jpg)

**(16) QuasiBot**

QuasiBot 是一款 php 编写的 webshell 管理工具，可以对 webshell 进行远程批量管理。这个工具超越于普通的 webshell 管理是因为其还拥有安全扫描、漏洞利用测试等功能，可以帮助渗透测试人员进行高效的测试工作。

项目地址：

[https://github.com/Smaash/quasibot](https://link.zhihu.com/?target=https%3A//github.com/Smaash/quasibot)

![](https://pic1.zhimg.com/v2-51a67039f6263498e7deb7f3c6cb5f38_b.jpg)

**(17) Weevely**

Weevely 是一款 python 编写的生成和管理 php webshell 的安全测试工具，目前拥有 30 多个模块：文件管理、命令执行、数据库管理、端口扫描等功能，部分模块不支持在 Windows 环境下使用。

**项目地址：**

[https://github.com/epinna/weevely3](https://link.zhihu.com/?target=https%3A//github.com/epinna/weevely3)

![](https://pic4.zhimg.com/v2-7f41331a82fe29db37e52b310449fd73_b.jpg)

**(18) WeBaCoo**

WeBaCoo 是一款 Perl 语言编写的 Web 后门工具，它的特别之处在于 Web 服务器和客户端之间的通信载体是 Cookie，这就意味着多数的杀毒软件、网络入侵检测/防御系统、网络防火墙和应用程序防火墙都无法检测到该后门的存在。当然，这只是以前的介绍，现在基本都会被检测了。

**项目地址：**

[https://github.com/anestisb/WeBaCoo](https://link.zhihu.com/?target=https%3A//github.com/anestisb/WeBaCoo)

![](https://pic2.zhimg.com/v2-f167f53ee88eebf84f235965a8311a09_b.jpg)

**(19) Webhandler**

Webhandler 是一款 Python 语言编写的 php webshell 安全测试工具，主要以 system、passthru、exec 等函数执行命令，但它不仅支持系统命令，还提供了以@开始的专有命令用于渗透测试，如：获取系统信息、端口扫描、上传下载、FTP/MYSQL 爆破、创建后门（反弹 shell）等。

**项目地址：**

[https://github.com/lnxg33k/webhandler](https://link.zhihu.com/?target=https%3A//github.com/lnxg33k/webhandler)

![](https://pic1.zhimg.com/v2-d247d6bb935b3c98fb127e7025180ae4_b.jpg)

**(20) Webshell-Sniper**

Webshell-Sniper 是一款 Python 语言编写的 webshell 管理器，支持的功能有：文件管理、命令执行、数据库管理、端口扫描、反弹 Shell 等，该项目作者是王一航，但是已经停止更新了。

**项目地址：**

[https://github.com/WangYihang/Webshell-Sniper](https://link.zhihu.com/?target=https%3A//github.com/WangYihang/Webshell-Sniper)

![](https://pic4.zhimg.com/v2-3be2776ecd4519809cb8d8197c825427_b.jpg)

**(21) Metasploit**

Metasploit 虽说不是一款 Webshell 网站管理工具，但是已经具备了该有的功能，甚至更加强大，如：文件管理、命令执行等，脚本类型支持 ASPX、PHP、JSP 等。

**项目地址：**

[https://github.com/rapid7/metasploit-framework](https://link.zhihu.com/?target=https%3A//github.com/rapid7/metasploit-framework)

![](https://pic4.zhimg.com/v2-ccfbbf77b34e4fb4a7a6cc4dbdfed8b7_b.jpg)

**(22) PhpSploit**

PhpSploit 是一个由 Python 编写的后渗透利用框架，支持在 Win/Linux/Mac 等平台执行，该工具会对标准客户端请求以及 Web 服务器相关请求的 HTTP 头数据进行混淆处理，并利用一个小型后门来实现隐蔽通信，<?php @eval($\_SERVER\['HTTP\_PHPSPL01T'\]); ?>。

**项目地址：**

[https://github.com/nil0x42/phpsploit](https://link.zhihu.com/?target=https%3A//github.com/nil0x42/phpsploit)

![](https://pic3.zhimg.com/v2-88b37becfa32db4b34f3dd18f43d15fe_b.jpg)

**(23) SharPyShell**

SharPyShell 是一个由 Python 编写的后渗透框架，用于 C＃[Web 应用程序的小型混淆版 ASP.NET](https://link.zhihu.com/?target=http%3A//Web%25E5%25BA%2594%25E7%2594%25A8%25E7%25A8%258B%25E5%25BA%258F%25E7%259A%2584%25E5%25B0%258F%25E5%259E%258B%25E6%25B7%25B7%25E6%25B7%2586%25E7%2589%2588ASP.NET) WebShell，[但仅支持在.NET](https://link.zhihu.com/?target=http%3A//%25E4%25BD%2586%25E4%25BB%2585%25E6%2594%25AF%25E6%258C%2581%25E5%259C%25A8.NET) Framework >= 2.0 上运行，执行由加密信道接收的命令，并在运行时将它们编译到内存中。

**项目地址：**

[https://github.com/antonioCoco/SharPyShell](https://link.zhihu.com/?target=https%3A//github.com/antonioCoco/SharPyShell)

![](https://pic4.zhimg.com/v2-6df87dfa09878a558b2790fa4db159b7_b.jpg)

### Reference

[PHP 过安全狗、过 waf、免杀 PHP 大马 - 2021.1.19 更新](https://www.vvhan.com/phpmiansha-1.html)
[谈谈 php 一句话木马的免杀](https://cloud.tencent.com/developer/article/2101661)
[谈谈 php 一句话木马的免杀](https://saucer-man.com/information_security/248.html)
[23 个常见 Webshell 网站管理工具](https://zhuanlan.zhihu.com/p/440563201)

**2023.08.17**
