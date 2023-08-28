---
title: flask web整合jwt认证
date: 2022-07-05 14:43:27
copyright: false
author: 我叫zhengxianjun
home: https://www.jianshu.com/u/9b9d3c6fdcdf
origin: jianshu
url: https://www.jianshu.com/p/7afbffaf08bf
tag: 
categories: 
description: 今天继续来弄flask的东东，jwt。用来做登录认证。项目整合模块：代码在后文附上flask_jwt...
---

今天继续来弄flask的东东，jwt。用来做登录认证。

---

项目整合模块：代码在后文附上

flask\_jwt\_extended 附上官方文档地址：[地址](https://links.jianshu.com/go?to=https%3A%2F%2Fflask-jwt-extended.readthedocs.io%2Fen%2Flatest%2F)

一基本使用：

安装：

> pip install flask-jwt-extended

安装好后，导入模块

![](./flask web整合jwt认证/83d130ceb28125113cb8577a119b56b4)

导入

注册到flask app实例中

![](./flask web整合jwt认证/8ef2ba4846f642c6b1fa53d6c7f6d9cc)

注册实例

只需要在视图函数，即接口处加上@fresh\_jwt\_required，或者@jwt\_required装饰器，jwt 就可以使用了。接下来分析下，工作流程。

二.工作流程

先来分析下源码，

![](./flask web整合jwt认证/24e3f5108aba9dc813f706381ecc0419)

源码

flask\_jwt\_extended 创建好JWTManager实例后，会默认加载好自身的回调函数，回调函数也就是当触发我们要访问的条件时，即满足触发条件，就会调用这个函数。比如我们用了，@fresh\_jwt\_required 来装饰我们的接口，当我们访问这个接口时，就会执行这个回调函数。有各种回调函数进行来验证和解析我们的token，所以使用的时候很方便。从源码中可以看出，有两个回调函数没有进行调用。黑名单验证，这个可以自己重写，重写就是再写一个装饰器覆盖而已，进行黑名单的token限制访问，具体可以看本文代码。

> @main\_bp.route('/user', methods=(\['POST'\]))
>
> @fresh\_jwt\_required
>
> def get\_user():
>
> \# 通过flask 的request 获取前端传过来的json数据
>
> json = request.json username = json.get('username')
>
> user = User(username=username)
>
> return jsonify(user.username),200

所以简单来说，flask\_jwt\_extended这个的工作流程就是 实例化JWTManager——>注册到app实例中——>对接口进行装饰器保护——>回调函数进行验证解析，保护接口安全，如有必要进行回调函数重写

web程序完整的流程：

1.HTTP访问登录，生成token（通过flask\_jwt\_extended的现有相关方法生成），返回。

2.访问其它接口，携带1中生成的token，flask\_jwt\_extended对保护的接口（视图函数）通过回调函数进行token验证解析。

3.通过2的token验证，访问视图函数，返回数据。

三.补充jwt原理

一个JWT实际上就是一个字符串，它由三部分组成，**头部**、**载荷**与**签名**。

头部进行BASE64编码，头部用于描述关于该JWT的最基本的信息，例如其类型以及签名所用的算法等。这也可以被表示成一个JSON对象。

载荷就是存放有效信息的地方,有效信息包含三个部分:

jwt的第三部分是一个签证信息，这个签证信息由三部分组成：

header (base64后的)

payload(base64后的)

secret

这个部分需要(1)base64加密后的header(2)base64加密后的payload

最后使用.连接两者组成的最终字符串，进行header中声明的加密方式进行加盐secret组合加密，然后就构成了jwt的第 三部分。所以要保护好secret。flask\_jwt\_extended里也提供了动态的加密方法，用不同的secret进行加密的回调方法，只要重写就会了。重写就是再写一个装饰器覆盖而已。具体可以看源码和文档。

flask\_jwt\_extended已经给flask app实例添加了默认配置。通过app.config可以修改

![](./flask web整合jwt认证/ee3e4aa1aef3038e4b23c27c4102a8d7)

jwt的默认配置

\# Secret key to sign JWTs with. Only used if a symmetric algorithm is

\# used (such as the HS\* algorithms). We will use the app secret key

\# if this is not set.

app.config.setdefault('JWT\_SECRET\_KEY', None)

以上就是flask\_jwt\_extended的运行原理了。

#### 代码：https://github.com/JUN-ZZ/flask-app。[代码](https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FJUN-ZZ%2Fflask-app)

> 当前文档由 [markdown文档下载插件](https://github.com/kscript/markdown-download) 下载, 原文链接: [flask web整合jwt认证](https://www.jianshu.com/p/7afbffaf08bf)  