---
title: python之Marshmallow使用
date: 2022-07-05 14:20:38
copyright: false
author: 指尖听戏
home: https://www.zhihu.com/people/liuhuanhuan963019
origin: zhihu
url: https://zhuanlan.zhihu.com/p/376211409
tag: 
categories: 
description: python之Marshmallow marshmallow是一个用来将复杂的orm对象与pytho...
---

## python之Marshmallow

> marshmallow是一个用来将复杂的orm对象与python原生数据类型之间相互转换的库，简而言之，就是实现object -> dict， objects -> list, string -> dict 和 string -> list。  
> 序列化：序列化的意思是将数据对象转化为可存储或可传输的数据类型 反序列化：将可存储或可传输的数据类型转化为数据对象  
> 要进行序列化或反序列化，首先我们需要一个用来操作的object，这里我们先定义一个类：

```python
import datetime as dt


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_time = dt.datetime.now()
```

## 1、Scheme
要对一个类或者一个json数据实现相互转换(即序列化和反序列化), 需要一个中间载体, 这个载体就是Schema，另外Schema还可以用来做数据验证。
  

```java
# 这是一个简单的Scheme
from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_time = fields.DateTime()
```

## 2、Serializing(序列化)
使用scheme的dump()方法来序列化对象，返回的是dict格式的数据
  
另外schema的dumps()方法序列化对象，返回的是json编码格式的字符串。
  

```java
user = User("lhh","2432783449@qq.com")
schema = UserSchema()
res = schema.dump(user)
print(res)
# {'email': '2432783449@qq.com', 'created_time': '2021-05-28 20:43:08.946112', 'name': 'lhh'}  dict

res2 = schema.dumps(user)
print(res2)
# {"name": "lhh", "email": "2432783449@qq.com", "created_time": "2021-05-28 20:45:17.418739"}  json
```

## 3、过滤输出
当不需要输出所有的字段时，可以在实例化Scheme时，声明only参数，来指定输出：
  

```java
summary_schema = UserSchema(only={"name","email"})
res = summary_schema.dump(user)
print(res)
```

## 4、Deserializing（反序列化）
schema的load()方法与dump()方法相反，用于dict类型的反序列化。他将输入的字典格式数据转换成应用层数据结构。他也能起到验证输入的字典格式数据的作用。 同样，也有对json解码的loads()方法。用于string类型的反序列化。 默认情况下，load()方法返回一个字典，当输入的数据的值不匹配字段类型时，抛出 ValidationError 异常。
  

```java
user_data = {
    "name": "lhh",
    "email": "2432783449@qq.com",
    "created_time": "2021-05-28 20:45:17.418739"
}
schema = UserSchema()
res = schema.load(user_data)
print(res)
# {'created_time': '2021-05-28 20:45:17.418739', 'email': '2432783449@qq.com', 'name': 'lhh'}
```
对反序列化而言, 将传入的dict变成object更加有意义. 在Marshmallow中, dict -> object的方法需要自己实现, 然后在该方法前面加上一个装饰器post\_load即可
  

```java
class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_time = fields.DateTime()

    @post_load
    def make_user(self, data):
        return User(**data)
```
这样每次调用load()方法时, 会按照make\_user的逻辑, 返回一个User类对象。
  

```java
user_data = {
    "name": "lhh",
    "email": "2432783449@qq.com"
}

schema = UserSchema()
res = schema.load(user_data)
print(res)
# <__main__.User object at 0x0000027BE9678128>
user = res
print("name: {}    email: {}".format(user.name, user.email))
# name: lhh    email: 2432783449@qq.com
```

## 5、处理多个对象的集合
多个对象的集合如果是可迭代的，那么也可以直接对这个集合进行序列化或者反序列化。在实例化Scheme类时设置参数many=True
  
也可以不在实例化类的时候设置，而在调用dump()方法的时候传入这个参数。
  

```java
user1 = User(name="lhh1", email="2432783449@qq.com")
user2 = User(name="lhh2", email="2432783449@qq.com")
users = [user1, user2]

# 第一种方法
schema = UserSchema(many=True)
res = schema.dump(users)
print(res)

# 第二种方法
schema = UserSchema()
res = schema.dump(users,many=True)
print(res)
```

## 6、Validation(验证)
当不合法的数据通过Schema.load()或者Schema.loads()时，会抛出一个 ValidationError 异常。ValidationError.messages属性有验证错误信息，验证通过的数据在 ValidationError.valid\_data 属性中 我们捕获这个异常，然后做异常处理。首先需要导入ValidationError这个异常
  

```java
from marshmallow import Schema,fields,ValidationError


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email()
    created_time = fields.DateTime()

try:
    res = UserSchema().load({"name":"lhh","email":"lhh"})

except ValidationError as e:
    print(f"错误信息：{e.messages}  合法数据:{e.valid_data}")

'''
    当验证一个数据集合的时候，返回的错误信息会以 错误序号-错误信息 的键值对形式保存在errors中
'''
user_data = [
    {'email': '2432783449@qq.com', 'name': 'lhh'},
    {'email': 'invalid', 'name': 'Invalid'},
    {'name': 'wcy'},
    {'email': '2432783449@qq.com'},
]


try:
    schema = UserSchema(many=True)
    res = schema.load(user_data)
    print(res)
except ValidationError as e:
    print("错误信息：{}   合法数据：{}".format(e.messages, e.valid_data))
```
可以看到上面，有错误信息，但是对于没有传入的属性则没有检查，也就是说没有规定属性必须传入。
  
在Schema里规定不可缺省字段：设置参数required=True
  

> `可以看到上面，有错误信息，但是对于没有传入的属性则没有检查，也就是说没有规定属性必须传入。 在Schema里规定不可缺省字段：设置参数required=True`

### 6.1 自定义验证信息
在编写Schema类的时候，可以向内建的fields中设置validate参数的值来定制验证的逻辑, validate的值可以是函数, 匿名函数lambda, 或者是定义了**call**的对象。
  

```java
from marshmallow import Schema,fields,ValidationError


class UserSchema(Schema):
    name = fields.String(required=True, validate=lambda s:len(s) < 6)
    email = fields.Email()
    created_time = fields.DateTime()

user_data = {"name":"InvalidName","email":"2432783449@qq.com"}
try:
    res = UserSchema().load(user_data)
except ValidationError as e:
    print(e.messages)
```
**在验证函数中自定义异常信息：**
  

```python
#encoding=utf-8
from marshmallow import Schema,fields,ValidationError

def validate_name(name):
    if len(name) <=2:
        raise ValidationError("name长度必须大于2位")
    if len(name) >= 6:
        raise ValidationError("name长度不能大于6位")




class UserSchema(Schema):
    name = fields.String(required=True, validate=validate_name)
    email = fields.Email()
    created_time = fields.DateTime()

user_data = {"name":"InvalidName","email":"2432783449@qq.com"}
try:
    res = UserSchema().load(user_data)
except ValidationError as e:
    print(e.messages)
```
`注意`：只会在反序列化的时候发生验证！序列化的时候不会验证！
  

### 6.2 将验证函数写在Schema中变成验证方法
在Schema中，使用validates装饰器就可以注册验证方法。
  

```python
#encoding=utf-8
from marshmallow import Schema, fields, ValidationError, validates


class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email()
    created_time = fields.DateTime()

    @validates("name")
    def validate_name(self, value):
        if len(value) <= 2:
            raise ValidationError("name长度必须大于2位")
        if len(value) >= 6:
            raise ValidationError("name长度不能大于6位")


user_data = {"name":"InvalidName","email":"2432783449@qq.com"}
try:
    res = UserSchema().load(user_data)
except ValidationError as e:
    print(e.messages)
```

### 6.3 Required Fields(必填选项)
上面已经简单使用过required参数了。这里再简单介绍一下。
  
**自定义required异常信息：**
  
首先我们可以自定义在requird=True时缺失字段时抛出的异常信息：设置参数error\_messages的值
  

```python
#encoding=utf-8
from marshmallow import Schema, fields, ValidationError, validates


class UserSchema(Schema):
    name = fields.String(required=True, error_messages={"required":"name字段必须的"})
    email = fields.Email()
    created_time = fields.DateTime()

    @validates("name")
    def validate_name(self, value):
        if len(value) <= 2:
            raise ValidationError("name长度必须大于2位")
        if len(value) >= 6:
            raise ValidationError("name长度不能大于6位")


user_data = {"email":"2432783449@qq.com"}
try:
    res = UserSchema().load(user_data)
except ValidationError as e:
    print(e.messages)
```
**忽略部分字段：**
  
使用required之后我们还是可以在传入数据的时候忽略这个必填字段。
  

```java
#encoding=utf-8
from marshmallow import Schema, fields, ValidationError, validates


class UserSchema(Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)

# 方法一：在load()方法设置partial参数的值（元组），表时忽略那些字段。
schema = UserSchema()
res = schema.load({"age": 42}, partial=("name",))
print(res)
# {'age': 42}

# 方法二：直接设置partial=True
schema = UserSchema()
res = schema.load({"age": 42}, partial=True)
print(res)
# {'age': 42}
```
看起来两种方法是一样的，但是方法一和方法二有区别：方法一只忽略传入partial的字段，方法二会忽略除前面传入的数据里已有的字段之外的所有字段
  

### 6.4 对未知字段的处理
默认情况下，如果传入了未知的字段（Schema里没有的字段），执行load()方法会抛出一个 ValidationError 异常。这种行为可以通过更改 unknown 选项来修改。
  
unknown 有三个值：
  

* EXCLUDE: exclude unknown fields(直接扔掉未知字段)
* INCLUDE: accept and include the unknown fields（接受未知字段）
* RAISE: raise a ValidationError if there are any unknown fields（抛出异常）
我们可以看到，默认的行为就是RAISE。有两种方法去更改：
  
方法一：在编写Schema类的时候在class Meta里修改
  

```python
from marshmallow import EXCLUDE,Schema,fields

class UserSchema(Schema):
    name = fields.String(required=True,error_messages={"required": "name字段必须填写"})
    email = fields.Email()
    created_time = fields.DateTime()


    class Meta:
        unknown  = EXCLUDE
```
方法二：在实例化Schema类的时候设置参数unknown的值
  

```python
class UserSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "name字段必须填写"})
    email = fields.Email()
    created_time = fields.DateTime()

shema = UserSchema(unknown=EXCLUDE)
```

## 7、Schema.validate(校验数据)
如果只是想用Schema去验证数据, 而不进行反序列化生成对象, 可以使用Schema.validate() 可以看到, 通过schema.validate()会自动对数据进行校验, 如果有错误, 则会返回错误信息的dict,没有错误则返回空的dict，通过返回的数据, 我们就可以确认验证是否通过.
  

```python
#encoding=utf-8
from marshmallow import Schema,fields,ValidationError

class UserSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "name字段必须填写"})
    email = fields.Email()
    created_time = fields.DateTime()

user = {"name":"lhh","email":"2432783449"}
schema = UserSchema()
res = schema.validate(user)
print(res)  # {'email': ['Not a valid email address.']}

user = {"name":"lhh","email":"2432783449@qq.com"}
schema = UserSchema()
res = schema.validate(user)
print(res)  # {}
```

## 8\. Specifying Serialization/Deserialization Keys（指定序列化/反序列化键）

### 8.1 Specifying Attribute Names（序列化时指定object属性对应fields字段）
Schema默认会序列化传入对象和自身定义的fields相同的属性, 然而你也会有需求使用不同的fields和属性名. 在这种情况下, 你需要明确定义这个fields将从什么属性名取值
  

```python
from marshmallow import fields,Schema,ValidationError
import datetime as dt

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_time = dt.datetime.now()


class UserSchema(Schema):
    full_name = fields.String(attribute="name")
    email_address = fields.Email(attribute="email")
    created_at = fields.DateTime(attribute="created_time")


user = User("lhh",email="2432783449@qq.com")
schema = UserSchema()
res = schema.dump(user)
print(res)
# {'email_address': '2432783449@qq.com', 'full_name': 'lhh', 'created_at': '2021-05-29T09:24:38.186191'}
```
如上所示：UserSchema中的full\_name，email\_address，created\_at分别从User对象的name，email，created\_time属性取值。
  

### 8.2 反序列化时指定fields字段对应object属性
这个与上面相反，Schema默认反序列化传入字典和输出字典中相同的字段名. 如果你觉得数据不匹配你的schema, 可以传入load\_from参数指定需要增加load的字段名(原字段名也能load, 且优先load原字段名)
  

```python
from marshmallow import fields,Schema,ValidationError
import datetime as dt

class UserSchema(Schema):
    full_name = fields.String(load_from="name")
    email_address = fields.Email(load_from="email")
    created_at = fields.DateTime(load_from="created_time")

user = {"full_name":"lhh","email_address":"2432783449@qq.com"}
schema = UserSchema()
res = schema.load(user)
print(res)
# {'full_name': 'lhh', 'email_address': '2432783449@qq.com'}
```

### 8.3 让key同时满足序列化与反序列化的方法

```python
#encoding=utf-8
from marshmallow import fields,ValidationError,Schema

class UserSchema(Schema):
    full_name = fields.String(data_key="name")
    email_address = fields.Email(data_key="email")
    created_at = fields.DateTime(data_key="created_time")

# 序列化
user = {"full_name": "lhh", "email_address": "2432783449@qq.com"}
schema = UserSchema()
res = schema.dump(user)
print(res)
# {'name': 'lhh', 'email': '2432783449@qq.com'}


# 反序列化
user = {'name': 'lhh', 'email': '2432783449@qq.com'}
schema = UserSchema()
res = schema.load(user)
print(res)
# {'full_name': 'lhh', 'email_address': '2432783449@qq.com'}
```

## 9\. 重构：创建隐式字段
当Schema具有许多属性时，为每个属性指定字段类型可能会重复，特别是当许多属性已经是本地python的数据类型时。class Meta允许指定要序列化的属性，marshmallow将根据属性的类型选择适当的字段类型。
  

```python
# 重构Schema
class UserSchema(Schema):
    uppername = fields.Function(lambda obj: obj.name.upper())

    class Meta:
        fields = ("name", "email", "created_at", "uppername")
```
以上代码中， name将自动被格式化为String类型，created\_at将被格式化为DateTime类型。
  
如果您希望指定除了显式声明的字段之外还包括哪些字段名，则可以使用附加选项。如下：
  

```python
class UserSchema(Schema):
    uppername = fields.Function(lambda obj: obj.name.upper())

    class Meta:
        # No need to include 'uppername'
        additional = ("name", "email", "created_at")
```

## 10\. 排序
对于某些用例，维护序列化输出的字段顺序可能很有用。要启用排序，请将ordered选项设置为true。这将指示marshmallow将数据序列化到`collections.OrderedDict`
  

```python
from collections import OrderedDict
import datetime as dt
from marshmallow import fields,ValidationError,Schema

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_time = dt.datetime.now()

class UserSchema(Schema):
    uppername = fields.Function(lambda obj: obj.name.upper())

    class Meta:
        fields = ("name", "email", "created_time", "uppername")
        ordered = True


user = User("lhh", "2432783449@qq.com")
schema = UserSchema()
res = schema.dump(user)
print(isinstance(res,OrderedDict))  # 判断变量类型
# True
print(res)
# OrderedDict([('name', 'lhh'), ('email', '2432783449@qq.com'), ('created_time', '2021-05-29T09:40:46.351382'), ('uppername', 'LHH')])
```

## 11\. “只读”与“只写”字段
在Web API的上下文中，序列化参数dump\_only和反序列化参数load\_only在概念上分别等同于只读和只写字段。
  

```python
from marshmallow import Schema,fields


class UserSchema(Schema):
    name = fields.Str()
    password = fields.Str(load_only=True)  # 等于只写
    created_at = fields.DateTime(dump_only=True)  # 等于只读
```
load时，dump\_only字段被视为未知字段。如果unknown选项设置为include，则与这些字段对应的键的值将因此loaded而不进行验证。
  

## 12\. 序列化/反序列化时指定字段的默认值
序列化时输入值缺失用default指定默认值。反序列化时输入值缺失用missing指定默认值。
  

```python
#encoding=utf-8
import uuid
import datetime as dt
from marshmallow import fields,ValidationError,Schema


class UserSchema(Schema):
    id = fields.UUID(missing=uuid.uuid1)
    birthday = fields.DateTime(default=dt.datetime(1996,11,17))

# 序列化
res = UserSchema().dump({})
print(res)
# {'birthday': '1996-11-17T00:00:00'}

# 反序列化
res = UserSchema().load({'birthday': '1996-11-17T00:00:00'})
print(res)
# {'id': UUID('751d95db-c020-11eb-83eb-001a7dda7115'), 'birthday': datetime.datetime(1996, 11, 17, 0, 0)}
```

## 13\. 后续扩展

```python
from marshmallow import Schema, fields


class String128(fields.String):
    """
    长度为128的字符串类型
    """

    default_error_messages = {
        "type": "该字段只能是字符串类型",
        "invalid": "该字符串长度必须大于6",
    }

    def _deserialize(self, value, attr, data, **kwargs):
        if not isinstance(value, str):
            self.fail("type")
        if len(value) < 6:
            self.fail("invalid")


class AppSchema(Schema):
    name = String128(required=True)
    priority = fields.Integer()
    obj_type = String128()
    link = String128()
    deploy = fields.Dict()
    description = fields.String()
    projects = fields.List(cls_or_instance=fields.Dict)


app = {
    "name": "app11",
    "priority": 2,
    "obj_type": "web",
    "link": "123.123.00.2",
    "deploy": {"deploy1": "deploy1", "deploy2": "deploy2"},
    "description": "app111 test111",
    "projects": [{"id": 2}]
}

schema = AppSchema()
res = schema.validate(app)
print(res)
# {'obj_type': ['该字符串长度必须大于6'], 'name': ['该字符串长度必须大于6']}
```
参考文章：[python之Marshmallow - X-Wolf - 博客园 (cnblogs.com)](https://link.zhihu.com/?target=https%3A//www.cnblogs.com/xingxia/p/python_Marshmallow.html)

> 当前文档由 [markdown文档下载插件](https://github.com/kscript/markdown-download) 下载, 原文链接: [python之Marshmallow使用](https://zhuanlan.zhihu.com/p/376211409)  