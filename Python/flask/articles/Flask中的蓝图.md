---
title: Flask中的蓝图
date: 2022-07-05 14:08:04
copyright: false
author: 充值查看昵称
home: https://www.jianshu.com/u/358db66b5a0c
origin: jianshu
url: https://www.jianshu.com/p/d6ce0a148190
tag:
categories:
description: 引入 正常情况下，我们简单的Flask程序都是单文件，把所有的视图函数写在一个文件里，比如说我有一个...
---

# 引入

正常情况下，我们简单的 Flask 程序都是单文件，把所有的视图函数写在一个文件里，比如说我有一个博客程序，前台需要首页、列表、详情等等。比如说我们创建一个 app.py 来实现这个功能。

```python
#app.py 文件
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/list')
def list():
    pass

@app.route('/detail')
def detail():
    pass

if __name__=='__main__':
    app.run()
```

假设内部逻辑完全实现，一个简单的博客系统就完成了，是不是很简洁。但是我们的博客可不是只有前台页面啊，我们的博主想要编辑博客,要进入后台进行处理:后台主页,编辑,创建,发布博客等等。行，既然有新需求了，那么我们就往 app 文件中加呗。如下:

```python
#app.py 文件
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/list')
def list():
    pass

@app.route('/detail')
def detail():
    pass
# ---------------新加入的代码
@app.route('/')
def admin_home():
    pass

@app.route('/new')
def new():
    pass

@app.route('/edit')
def edit():
     pass

@app.route('/publish')
def publish():
    pass

if __name__=='__main__':
    app.run()
```

假设新加入的代码逻辑也全部实现了，我们的博客系统就完成了。但是这只是理想化的情况，真正线上的博客可不是这么简单，业务都很复杂。  
按照我们的设计，一个 py 文件中写入大量的路由，这样既不简洁，也不良好，将来维护代码会非常麻烦，所以有人就会想到了模块化的方法，把 admin 相关的代码移到一个 admin.py 中，那么就这么做一下。

```python
# admin.py 文件
from app import app
@app.route('/')
def admin_home():
    pass

@app.route('/new')
def new():
    pass

@app.route('/edit')
def edit():
     pass

@app.route('/publish')
def publish():
    pass
```

这样写完后，发现启动程序，路由找不到，也就是说，使用 python 传统的模块化方式是行不通的，这时候就需要使用 Flask 内置的一个模块化处理的类,即蓝图(Blueprint)，完美解决以上问题。那么蓝图究竟是什么？

# 什么是蓝图

简单来说，Blueprint 是一个存储操作方法的容器，这些操作在这个 Blueprint 被注册到一个应用之后就可以被调用，Flask 可以通过 Blueprint 来组织 URL 以及处理请求。

Flask 使用 Blueprint 让应用实现模块化，在 Flask 中，Blueprint 具有如下属性：

- 一个应用可以具有多个 Blueprint
- 可以将一个 Blueprint 注册到任何一个未使用的 URL 下比如 “/”、“/sample”或者子域名
- 在一个应用中，一个模块可以注册多次
- Blueprint 可以单独具有自己的模板、静态文件或者其它的通用操作方法，它并不是必须要实现应用的视图和函数的
- 在一个应用初始化时，就应该要注册需要使用的 Blueprint

但是一个 Blueprint 并不是一个完整的应用，它不能独立于应用运行，而必须要注册到某一个应用中。

# 蓝图的使用

使用蓝图大概需要三个步骤

- 创建蓝图对象

```python
# 这里的两个参数为必选，至于为什么，稍后解释
admin = Blueprint('admin',__name__)
```

- 使用蓝图对象注册路由

```python
@admin.route('/')
def admin_home():
    pass
```

- 将蓝图注册到 app 上。注意：**蓝图对象没有办法独立运行，必须将它注册到一个应用对象上才能生效**

```css
app.register_blueprint(admin)
```

完整 demo

```python
from flask import Flask,Blueprint

admin = Blueprint('admin',__name__)

app = Flask(__name__)

app.register_blueprint(admin)

@admin.route('/')
def admin_home():
    pass

if __name__ == '__main__':
    app.run()`
```

# 蓝图对象的初始化

首先来看一下蓝图对象的构造方法

```python
def __init__(self, name, import_name, static_folder=None,
                 static_url_path=None, template_folder=None,
                 url_prefix=None, subdomain=None, url_defaults=None,
                 root_path=None):
    pass
# name 蓝图对象的名字（标识）
# import_name 蓝图的资源文件夹，也就是蓝图的位置，该参数是一般是模块的名字
# static_folder 静态资源文件夹路径，相对路径
# static_url_path 静态文件url
# template_folder 模板文件路径
# url_prefix url前缀
# subdomain 子域名
# url_defaults 默认的路径参数和其对应的值的键值对，当其被设置后，本蓝图的所有视图函数便拥有该参数
# root_path 蓝图的资源文件夹的绝对路径，如果这个不是None，import_name的设置失效
```

由构造参数可知，为什么只有 name 和 import_name 是必传入的。

- url_prefix 这个参数是干什么用的呢？  
  这个参数可以动态帮助我们构造 url 前缀。比如我们有下面的路由。

```python
@app.route('/blog')
def index():
    pass

@app.route('/blog/list')
def list():
    pass

@app.route('/blog/detail')
def detail():
    pass
```

从上面我们可以看出，所有的路由都是以 blog 开头的，若这样写代码的话，会增加代码的复杂性、降低可维护性。为了解决这个问题，我们可以在蓝图中定义动态的 URL 前缀。

```
blog=Blueprint('blog', __name__, url_prefix='/blog')
```

这样一来我们的路由可以写为

```python
@app.route('/')
def index():
    pass

@app.route('/list')
def list():
    pass

@app.route('/detail')
def detail():
    pass
```

- static_folder 注册静态路由  
  和应用对象不同，蓝图对象创建时不会默认注册静态目录的路由。需要我们在 创建时指定 static_folder 参数。

```
blog = Blueprint("blog",__name__,static_folder='static_blog', url_prefix='/blog')
```

现在就可以使用/blog/static_blog/ 访问 static_blog 目录下的静态文件了。我们可以在创建蓝图对象时使用 static_url_path 来改变静态目录的路由。下面的示例将为 static_blog 文件夹的路由设置为 /lib

```
blog = Blueprint("blog",__name__,static_folder='static_blog', static_url_path='/lib',url_prefix='/blog')
```

- template_folder 注册模板目录  
  蓝图对象默认的模板目录为系统的模版目录，可以在创建蓝图对象时使用 template_folder 关键字参数设置模板目录

```
blog = Blueprint('blog',__name__,template_folder='my_templates')
```

# 蓝图的运行机制-源码分析

我们已经知道蓝图怎么使用了，但是仅仅知道怎么使用是不够的，还是要了解下其背后的运行机制，才能更好的掌握蓝图，更好的使用它。  
我们看一下 app 的 register_blueprint 方法，实际是调用了蓝图的 register 方法。

```
@setupmethod
    def register_blueprint(self, blueprint, **options)
        ...
        blueprint.register(self, options, first_registration)
```

继续看一下蓝图的 register 方法

```
    def register(self, app, options, first_registration=False):
        self._got_registered_once = True
        state = self.make_setup_state(app, options, first_registration)
        if self.has_static_folder:
            state.add_url_rule(self.static_url_path + '/<path:filename>',
                               view_func=self.send_static_file,
                               endpoint='static')

        for deferred in self.deferred_functions:
            deferred(state)
```

这里有两个重要的地方，一个是 state，一个是 deferred_functions。  
先看一下 state 是什么。

```
def make_setup_state(self, app, options, first_registration=False):
    ...
    return BlueprintSetupState(self, app, options, first_registration)
```

通过 make_setup_state 这个方法我们发现 state 实际上是 BlueprintSetupState 的一个实例。

```
class BlueprintSetupState(object):

    def __init__(self, blueprint, app, options, first_registration):
        ...

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        ...
        self.app.add_url_rule(rule, '%s.%s' % (self.blueprint.name, endpoint),
                              view_func, defaults=defaults, **options)
```

发现 BlueprintSetupState 类中有一个 add_url_rule 方法，实际上是在调用 flask app 的路由操作，这个类个人理解是蓝图和 flask 连接的桥梁。  
我们在看一下 deferred_functions，通过源码发现 recode 和 record_once 在向 deferred_functions 里面添加函数。

```
def record(self, func):
    ...
    self.deferred_functions.append(func)

def record_once(self, func):
    ...
    return self.record(update_wrapper(wrapper, func))
```

record_once 作用是这种添加只进行一次。通过源码分析我们找到 record 调用，发现是 deferred_functions 里面添加的是 lambda 函数，可以理解为视图函数和路由信息。

```
def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
     ...
    self.record(lambda s: s.add_url_rule(rule, endpoint, view_func, **options))
```

我们理清了 deferred_functions 和 state，回过头来在看 register。  
发现 deferred_functions 里的函数以 BlueprintSetupState 实例为参数，调用 flask app 的 add_rule_url 方法，实现路由的操作。  
为什么 deferred_functions 叫延迟函数呢，我们通过源码看不难发现因为只有在 register 注册的时候才会真正调用 flask app 的 add_rule_url 方法，添加到 url_map 中。  
总结一下整体流程:

- 当在应用对象上调用 route 装饰器注册路由时,这个操作将修改对象的 url_map 路由表
- 然而，蓝图对象根本没有路由表，当我们在蓝图对象上调用 route 装饰器注册路由时,它只是在内部的一个延迟操作记录列表 defered_functions 中添加了一个项
- 当执行应用对象的 register_blueprint() 方法时，应用对象调用蓝图的 register 方法，从蓝图对象的 defered_functions 列表中取出每一项，并以自身作为参数执行该匿名函数，即调用应用对象的 add_url_rule() 方法，这将真正的修改应用对象的路由表。

> 当前文档由 [markdown 文档下载插件](https://github.com/kscript/markdown-download) 下载, 原文链接: [Flask 中的蓝图](https://www.jianshu.com/p/d6ce0a148190)
