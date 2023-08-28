---
title: 插件flask_jwt_extended
date: 2022-07-05 14:56:38
copyright: false
author: 浪尖的游鱼
home: https://www.jianshu.com/u/9fd2055a348f
origin: jianshu
url: https://www.jianshu.com/p/10d0da01244c
tag: 
categories: 
description: 书接上文flask配置生产环境，我们了解到了： 如何配置flask+uWSGI+nginx的生产环境...
---

书接上文[flask配置生产环境](https://www.jianshu.com/p/dd1ada65f8f1)，我们了解到了：  
如何配置flask+uWSGI+nginx的生产环境

接下来我们来看拓展性更强的jwt插件flask\_jwt\_extended

# flask\_jwt\_extended

安装

```
> pip3 install Flask-JWT-Extended
```

什么是Flask-JWT-Extended  
之前已经说过jwt是序列化并加密过的json串，那很明显extend则是对之前功能的拓展。那下面我们就该看看拓展的强大之处。  
app.py

```python
from flask_jwt_extended import JWTManager

app.config['JWT_SECRET_KEY'] = 'jose'  # token密钥
app.config['JWT_BLACKLIST_ENABLED'] = True  # 黑名单管理
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']  # 允许将access and refresh tokens加入黑名单
#注册jwt
jwt = JWTManager(app)
```

接下来，因为此插件剔除了自动生成/auth，我们需要拓展user的功能，生成用户有关的：注册、登录、登出等功能，以及用户令牌认证以及刷新、失效等功能。  
user.py

```python
#关联包介绍

#request约束
_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
#用户登录
class UserLogin(Resource):
    def post(self):
#从parser获取request资料
        data = _user_parser.parse_args()
#找到用户资料
        user = UserModel.find_by_username(data['username'])
#进行用户认证
        if user and safe_str_cmp(user.password, data['password']):
#生成token，认证令牌和刷新令牌
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                       'access_token': access_token,
                       'refresh_token': refresh_token
                   }, 200
#认证失败
        return {"message": "Invalid Credentials!"}, 401
```

claims  
这是jwt的数据存储机制

```python
jwt = JWTManager(app)
#user_claims_loader定义我们附加到jwt的有效数据
#在每一个收到jwt保护的端口，我们都可以使用get_jwt_claims检索这些数据
#如下所示
@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:   # instead of hard-coding, we should read from a config file to get a list of admins instead
        return {'is_admin': True}
    return {'is_admin': False}
```

通过这个示例我们可以模拟用户管理机制，如下对item.py的修改，非管理员用户不可以删除item：  
注意下get\_jwt\_claims，说明在上文。

```
    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404
```

接下来就是一个个介绍特色的时候了：  
jwt\_optional  
官网介绍是，可以可选的保护节点，无论是否发送token，都可以进入节点，然后交给逻辑判断如何处理。比较常见的判定如下：  
如果请求中存在访问令牌，则将调用[`get_jwt_identity()`](https://links.jianshu.com/go?to=https%3A%2F%2Fflask-jwt-extended.readthedocs.io%2Fen%2Flatest%2Fapi.html%23flask_jwt_extended.get_jwt_identity)具有访问令牌标识的端点。如果请求中不存在访问令牌，则仍将调用此端点，但 [`get_jwt_identity()`](https://links.jianshu.com/go?to=https%3A%2F%2Fflask-jwt-extended.readthedocs.io%2Fen%2Flatest%2Fapi.html%23flask_jwt_extended.get_jwt_identity)将返回None  
示例

```python
class ItemList(Resource):
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        items = [item.json() for item in ItemModel.find_all()]
        if user_id:
            return {'items': items}, 200
        return {
            'items': [item['name'] for item in items],
            'message': 'More data available if you log in.'
        }, 200
```

create\_refresh\_token  
这个要追溯到create\_access\_token。一般来说，我们都是将用户权限和用户基本资料存放在这个TOKEN中，但是当用户权限？或者资料变更时，我们就要去刷新用户的资料，或者说当access\_token过期了，我们也要去更新access\_token。这一部分可以细看[Web API与OAuth：既生access token，何生refresh token](https://links.jianshu.com/go?to=https%3A%2F%2Fwww.cnblogs.com%2Fdudu%2Fp%2Foauth-refresh-token.html)  
其实这只是定义的问题（不过如果不是自己写TOKEN规则，我们要遵守这个定义）。我们在书写create\_refresh\_token的逻辑时，不在需要验证用户名和密码即达到了这种效果，如果说个人不这么写逻辑，你也看不出来效果，毕竟两种TOKEN其实是一样的。

```python
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {'access_token': new_token}, 200
```

这里有另一个概念，令牌的新鲜度fresh=False/True。我们可以根据此处的变更灵活处理一些敏感数据。比如说有些数据只有刚输入用户名和密码时的那段有效认证期才可以使用，当令牌刷新时即判定无效。此处匹配装饰器[`fresh_jwt_required()`](https://links.jianshu.com/go?to=https%3A%2F%2Fflask-jwt-extended.readthedocs.io%2Fen%2Flatest%2Fapi.html%23flask_jwt_extended.fresh_jwt_required)  
item.py，POST /item/<name>的逻辑变更。

```
    @fresh_jwt_required
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = self.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred while inserting the item."}, 500

        return item.json(), 201
```

expired\_token\_loader  
invalid\_token\_loader  
重新定义TOKEN回调错误内容，还有更多的请参考[Changing Default Behaviors](https://links.jianshu.com/go?to=https%3A%2F%2Fflask-jwt-extended.readthedocs.io%2Fen%2Flatest%2Fchanging_default_behavior.html%3Fhighlight%3Dinvalid_token_loader)

```python
#过期令牌
@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'message': 'The token has expired.',
        'error': 'token_expired'
    }), 401
#无效令牌
@jwt.invalid_token_loader
def invalid_token_callback(error):  # we have to keep the argument here, since it's passed in by the caller internally
    return jsonify({
        'message': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401
```

最后我们来介绍黑名单系统  
token\_in\_blacklist\_loader by app.py

```python
app.config['JWT_BLACKLIST_ENABLED'] = True  # enable blacklist feature
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']  # allow blacklisting for access and refresh tokens
# 检查此令牌是否属于黑名单，并在启用黑名单时调用
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST
```

可以看到此拓展插件给我们的用户管理提供了更多的可能

[回到目录](https://www.jianshu.com/p/757f31ec6eb1)

> 当前文档由 [markdown文档下载插件](https://github.com/kscript/markdown-download) 下载, 原文链接: [插件flask_jwt_extended](https://www.jianshu.com/p/10d0da01244c)  