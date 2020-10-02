<font size=4 face='楷体'>

## flask 实现 token 机制

### token 的生成

用 token 校验身份，是前后端交互的常用方式。
它有以下特性：

- 会失效
- 加密
- 可以根据它拿到用户的信息

> 生成方式: 内部配置的私钥 + 有效期 + user id

```python
# 导入依赖包
from flask import request,jsonify,current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

def create_token(api_user):
    '''
    生成token
    :param api_user:用户id
    :return: token
    '''

    # 第一个参数是内部的私钥，这里写在共用的配置信息里了，如果只是测试可以写死
    # 第二个参数是有效期(秒)
    s = Serializer(current_app.config["SECRET_KEY"],expires_in=3600)
    # 接收用户id转换与编码
    token = s.dumps({"id":api_user}).decode("ascii")
    return token
```

### token 的校验

> 校验接收到的 token，如果成功返回用户信息，否则返回 None

```python
# 基于上面的基础再导入用户的模型类
from app.model import User

def verify_token(token):
    '''
    校验token
    :param token:
    :return: 用户信息 or None
    '''

    # 参数为私有秘钥，跟上面方法的秘钥保持一致
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        # 转换为字典
        data = s.loads(token)
    except Exception:
        return None
    # 拿到转换后的数据，根据模型类去数据库查询用户信息
    user = User.query.get(data["id"])
    return user
```

### 用装饰器写一个必须携带 token 的校验

> 有很多接口是必须登录才能操作的，最好的方式就是在写一个装饰器，添加在需要的 api 上

```python
# 在上面的基础上导入
import functools

def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args,**kwargs):
        try:
            # 在请求头上拿到token
            token = request.headers["z-token"]
        except Exception:
            # 没接收的到token,给前端抛出错误
            # 这里的code推荐写一个文件统一管理。这里为了看着直观就先写死了。
            return jsonify(code = 4103, msg = '缺少参数token')

        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            s.loads(token)
        except Exception:
            return jsonify(code = 4101, msg = "登录已过期")

        return view_func(*args,**kwargs)

    return verify_token
```

### 使用案例

> 生成 token

```python
# 此处的api是蓝图的对象
from . import api
from app.model import User,db
from flask import request,jsonify
# 导入刚刚写的文件方法
from app.utils.common import create_token,login_required,verify_token

@api.route("/login",methods=["POST"])
def login():
    '''
    用户登录
    :return:token
    '''
    res_dir = request.get_json()
    if res_dir is None:
        # 这里的code，依然推荐用一个文件管理状态
        return jsonify(code = 4103, msg = "未接收到参数")

    # 获取前端传过来的参数
    phone = res_dir.get("phone")
    password = res_dir.get("password")

    # 校验参数
    if not all([phone,password]):
        return jsonify(code=4103, msg="请填写手机号或密码")

    if not re.match(r"1[23456789]\d{9}",phone):
        return jsonify(code=4103, msg="手机号有误")

    try:
        user = User.query.filter_by(phone=phone).first()
    except Exception:
        return jsonify(code=4004, msg="获取信息失败")

    if user is None or not user.check_password(password):
        return jsonify(code=4103, msg="手机号或密码错误")

    # 获取用户id，传入生成token的方法，并接收返回的token
    token = create_token(user.id)

    # 把token返回给前端
    return jsonify(code=0,msg="成功",data=token)
```

> 必须登录的校验与根据 token 拿到用户信息

```python
@api.route("/user/detail")
@login_required # 必须登录的装饰器校验
def userInfo():
    '''
    用户信息
    :return:data
    '''
    token = request.headers["z-token"]
    # 拿到token，去换取用户信息
    user = verify_token(token)

    data = {
        "phone":user.phone,
        "name":user.name,
        "head_portrait":user.head_portrait,
        "intro":user.intro,
        "level":user.level
    }

    return jsonify(code=0,msg="成功", data=data)
```

### Reference

[flask 实现 token 机制](https://juejin.im/post/6844903929289932808)

**Create on 2020.09.17**
