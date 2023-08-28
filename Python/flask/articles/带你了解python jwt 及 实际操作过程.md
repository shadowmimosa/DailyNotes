---
title: 带你了解python jwt 及 实际操作过程
date: 2022-07-05 14:54:16
copyright: false
author: 橘子不橙
home: https://blog.csdn.net/weixin_43939159
origin: csdn
url: https://blog.csdn.net/weixin_43939159/article/details/109148815
tag: 
categories: 
description: 文章目录  什么是jwt？jwt 认证流程jwt 与传统token的区别传统token的方式jwt ...
---
<link />

### 文章目录

* * * [什么是jwt？](#jwt_1)
    * [jwt 认证流程](#jwt__4)
    * [jwt 与传统token的区别](#jwt_token_9)
    * * [传统token的方式](#token_10)
      * [jwt 方式](#jwt__13)
    * [jwt 的构成](#jwt__16)
    * * [构成规则如下：](#_21)
      * * [header](#header_24)
        * [playload](#playload_43)
        * [signature](#signature_60)
    * [代码实行](#_83)
    * [jwt 校验token](#jwt_token_184)
    * * [获取token之后，会按照以下步骤进行校验：](#token_187)
    * [总结](#_210)
    * * [优点](#_211)
      * [安全相关](#_217)

### 什么是jwt？

> Json web token (JWT), 是为了在网络应用环境间传递声明而执行的一种基于JSON的开放标准（(RFC 7519).该token被设计为紧凑且安全的，特别适用于分布式站点的单点登录（SSO）场景。JWT的声明一般被用来在身份提供者和服务提供者间传递被认证的用户身份信息，以便于从资源服务器获取资源，也可以增加一些额外的其它业务逻辑所必须的声明信息，该token也可直接被用于认证，也可被加密。

### jwt 认证流程

![在这里插入图片描述](./带你了解python jwt 及 实际操作过程/9d6d5031a31f282f6fb2601843955e73)  
在项目开发中，一般会按照上图所示的过程进行认证，即：用户登录成功之后，服务端给用户浏览器返回一个token，以后用户浏览器要携带token再去向服务端发送请求，服务端校验token的合法性，合法则给用户看数据，否则，返回一些错误信息。

### jwt 与传统token的区别

#### 传统token的方式

> 用户登录成功后，服务端生成一个随机token给用户，并且在服务端(数据库或缓存)中保存一份token，以后用户再来访问时需携带token，服务端接收到token之后，去数据库或缓存中进行校验token的是否超时、是否合法。

#### jwt 方式

> 用户登录成功后，服务端通过jwt生成一个随机token给用户（服务端无需保留token），以后用户再来访问时需携带token，服务端接收到token之后，通过jwt对token进行校验是否超时、是否合法。

### jwt 的构成

![在这里插入图片描述](./带你了解python jwt 及 实际操作过程/b85b7303b56db68311626731626d37ff)  
jwt的生成token格式如下，即：由 . 连接的三段字符串组成。

> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV\_adQssw5c

#### 构成规则如下：

第一部分我们称它为头部（header),第二部分我们称其为载荷（payload, 类似于飞机上承载的物品)，第三部分是签证（signature).

##### header

jwt的头部承载两部分信息：

* 声明类型，这里是jwt
* 声明加密的算法 通常直接使用 HMAC SHA256
* 完整的头部就像下面这样的JSON：

```
{
  'typ': 'JWT',
  'alg': 'HS256'
}

1234
```

然后将头部进行base64加密（该加密是可以对称解密的),构成了第一部分.

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9


12
```

##### playload

第二段PAYLOAD部分，包含一些数据，对此json进行base64url加密，这就是token的第二段。

```
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}

12345
```

然后将其进行base64加密，得到Jwt的第二部分。

```
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9

1
```

##### signature

jwt的第三部分是一个签证信息，这个签证信息由三部分组成：

* header (base64后的)
* payload (base64后的)
* secret

```
// javascript
var encodedString = base64UrlEncode(header) + '.' + base64UrlEncode(payload);

var signature = HMACSHA256(encodedString, 'secret'); // TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ

1234
```

这个部分需要base64加密后的header和base64加密后的payload使用 . 连接组成的字符串，然后通过header中声明的加密方式进行加盐secret组合加密，然后就构成了jwt的第三部分。

将这三部分用.连接成一个完整的字符串,构成了最终的jwt:

```
 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ

1
```

> **注意**：secret是保存在服务器端的，jwt的签发生成也是在服务器端的，secret就是用来进行jwt的签发和jwt的验证，所以，它就是你服务端的私钥，在任何场景都不应该流露出去。一旦客户端得知这个secret, 那就意味着客户端是可以自我签发jwt了。

### 代码实行

urls.py

```
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from api import views

urlpatterns = [
    url('^pro/login/$', views.ProLoginView.as_view()),
    url('^pro/order/$', views.ProOrderView.as_view()),
]

123456789
```

views.py

```
class ProLoginView(APIView):
    """基于JWT 用户登录"""
    authentication_classes = []  # 登录不需要认证

    def post(self, request, *args, **kwargs):
        user = request.data.get('username')
        pwd = request.data.get('password')

        user_object = models.UserInfo.objects.filter(user=user, password=pwd).first()
        if not user_object:
            return Response({'code': 1000, 'error': '用户名或密码错误'})
		
		# 生成token
		salt = settings.SECRET_KEY
    	headers = {
        	'typ': 'jwt',
        	'alg': 'HS256'
   		}
    	# 构造payload
    	payload = {
            'user_id': user_object.id,  # 自定义用户ID
            'username': user_object.username,  # 自定义用户名
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)  # 超时时间
        }  # 超时时间为1分钟
    	token = jwt.encode(payload=payload, key=salt, algorithm="HS256", headers=headers).decode('utf-8')
        return Response({'code': 1001, 'data': token})


class ProOrderView(APIView):

    def get(self, request, *args, **kwargs):
        print(request.user)
        return Response({'data': '订单列表'})

    def post(self, request, *args, **kwargs):
        print(request.user)
        return Response({'data': '添加订单'})

    def put(self, request, *args, **kwargs):
        print(request.user)
        return Response({'data': '修改订单'})

    def delete(self, request, *args, **kwargs):
        print(request.user)
        return Response({'data': '删除订单'})

123456789101112131415161718192021222324252627282930313233343536373839404142434445
```

auth.py

```
import jwt
from django.conf import settings
from jwt import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class JwtQueryParamAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        salt = settings.SECRET_KEY

        try:
            # 从token中获取payload【不校验合法性】
            # unverified_payload = jwt.decode(token, None, False)
            # print(unverified_payload)
            # 从token中获取payload【校验合法性】
            payload = jwt.decode(token, salt, True)
        except exceptions.ExpiredSignatureError:
            raise AuthenticationFailed({'code': 1003, 'error': 'token已失效'})
        except jwt.DecodeError:
            raise AuthenticationFailed({'code': 1003, 'error': 'token认证失败'})
        except jwt.InvalidTokenError:
            raise AuthenticationFailed({'code': 1003, 'error': '非法的token'})

        # 三种操作
        # 1.跑出异常, 后序不在执行.
        # 2.returr一个元组(1, 2), 认证通过;在视图中如果调用request.user就是元组的第一个值;request.auth
        # 3.None
        return (payload, token)

123456789101112131415161718192021222324252627282930
```

### jwt 校验token

一般在认证成功后，把jwt生成的token返回给用户，以后用户再次访问时候需要携带token，此时jwt需要对token进行超时及合法性校验。

#### 获取token之后，会按照以下步骤进行校验：

将token分割成 header\_segment、payload\_segment、crypto\_segment 三部分

```
jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
signing_input, crypto_segment = jwt_token.rsplit(b'.', 1)
header_segment, payload_segment = signing_input.split(b'.', 1)

123
```

对第一部分 `header_segment` 进行base64url解密，得到`header`

对第二部分 `payload_segment` 进行base64url解密，得到 `payload`

对第三部分`crypto_segment`进行base64url解密，得到`signature`

对第三部分`signature`部分数据进行合法性校验

拼接前两段密文，即：signing\_input  
从第一段明文中获取加密算法，默认：HS256  
使用 算法+盐 对signing\_input 进行加密，将得到的结果和signature密文进行比较。

### 总结

#### 优点

因为json的通用性，所以JWT是可以进行跨语言支持的，像python，JAVA,JavaScript,NodeJS,PHP等很多语言都可以使用。  
因为有了payload部分，所以JWT可以在自身存储一些其他业务逻辑所必要的非敏感信息。  
便于传输，jwt的构成非常简单，字节占用很小，所以它是非常便于传输的。  
它不需要在服务端保存会话信息, 所以它易于应用的扩展

#### 安全相关

* 不应该在jwt的payload部分存放敏感信息，因为该部分是客户端可解密的部分。
* 保护好secret私钥，该私钥非常重要。
* 如果可以，请使用https协议

部分内容来源于此篇文章：[https://www.jianshu.com/p/576dbf44b2ae](https://www.jianshu.com/p/576dbf44b2ae)
<link />
<link />

> 当前文档由 [markdown文档下载插件](https://github.com/kscript/markdown-download) 下载, 原文链接: [带你了解python jwt 及 实际操作过程](https://blog.csdn.net/weixin_43939159/article/details/109148815)  