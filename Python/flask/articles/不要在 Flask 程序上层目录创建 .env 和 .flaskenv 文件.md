---
title: 不要在 Flask 程序上层目录创建 .env 和 .flaskenv 文件
date: 2022-07-05 14:15:09
copyright: false
author: 李辉
home: https://www.zhihu.com/people/im-greyli
origin: zhihu
url: https://zhuanlan.zhihu.com/p/128977263
tag: 
categories: 
description: TL;DR 版本：如果你的程序存储在单脚本里，比如 app.py，那么 .flaskenv 和 .e...
---
TL;DR 版本：
  
如果你的程序存储在单脚本里，比如 app.py，那么 .flaskenv 和 .env 应该放在程序脚本的同级目录：
  

```
myproject/
    - app.py
    - templates
    - static
    - .flaskenv
    - .env
```
如果你的程序存储在程序包里，那么 .flaskenv 和 .env 应该放在程序包的同级目录：
  

```
myproject/
    - app/
        - templates
        - static
        - __init__.py
        - views.py
    - .flaskenv
    - .env
```
如果你把 .flaskenv 和 .env 放到了再往上一层（myproject 再往上），或是把你的程序包或程序脚本放到了一个子目录（比如 /myproject/myapp），那么执行 flask run 就会出错。
  

---
如果你安装了 python-dotenv，同时在 Flask 程序的上层目录创建了 .env 或 .flaskenv 文件，那么你将没法成功执行 flask run 等命令，因为这会导致 Flask 没法正确找到对应的 Flask 程序实例。
  
这个问题从 Flask 开始引入 CLI 机制开始就存在了，困扰了我两年。18 年偶然在用户根目录创建了一个 .env 文件，发现 Flask 程序没法运行了，当时遇到的各种 bug 太多，没仔细考虑这两者之间的关联。后来经过几次测试，才确定下来是上层目录的 .env 和 .flaskenv 文件导致，但是一时找不到原因，就暂时放下了。直到 19 年 11 月，花了几个小时排查，还是没找到原因。
  
中间花了很长时间来追踪 Windows 特定的 Flask 程序无法启动的 bug（TypeError: environment can only contain strings），实在是怕了。因为 Flask 的 CLI 涉及太多东西，有时你要钻进 python-dotenv（[#101](https://link.zhihu.com/?target=https%3A//github.com/theskumar/python-dotenv/pull/101)） 和 Werkzeug（[#1320](https://link.zhihu.com/?target=https%3A//github.com/pallets/werkzeug/pull/1320)） 才能找到问题的原因。
  
但是问题不解决的话，你永远睡不好觉。《[Flask Web 开发实战](https://link.zhihu.com/?target=http%3A//helloflask.com/book)》第一部分的[示例程序](https://link.zhihu.com/?target=https%3A//github.com/greyli/helloflask)都放在了一个程序仓库，而且都放在了子目录，这意味着如果读者错误的在仓库根目录创建 .env 和 .flaskenv 文件的话，就会导致子目录下的六个示例程序没法运行。前后大概收到 6 个相关的读者反馈，虽然后续在网站上添加了提醒，在重印的书里介绍创建 .env/.flaskenv 文件的地方追加提醒，但这终究没有真正解决问题，而且总会有人可以完美的错过所有提示。
  
如果每个人都可以在书上标记出错位置并共享，那么这一页应该会有很多红色小叉号（参考《超级马里奥制造》，也许未来某个电子书平台会做出来这个功能 :P）。
  
前几天在[这个 Issue](https://link.zhihu.com/?target=https%3A//github.com/greyli/helloflask/issues/200) 的提醒下，又花了两个小时排查，这次终于找到原因。加上写 PR（[#3560](https://link.zhihu.com/?target=https%3A//github.com/pallets/flask/pull/3560)）和 Issue（[#3561](https://link.zhihu.com/?target=https%3A//github.com/pallets/flask/issues/3561)），前后两年一共花了 8 个小时，这个问题终于有了着落。没意外的话，预计会在下一个版本的 Flask 中更新。下面是具体原因。
  
本来以为这个问题和 python-dotenv 或 Werkzeug 相关，没想到只是 Flask 本身代码的问题，我太笨了，这个问题本可以早一点解决。
  
按照预定的行为，当安装了 python-dotenv，Flask 会自动加载 .env 和 .flaskenv 里的环境变量。python-dotenv 在搜索存储环境变量的文件时，会从当前目录开始向上搜索，如果找到就返回对应的文件路径。但是这时 Flask 如果发现 .env 或 .flaskenv 的所在目录不是当前目录，就会把当前工作目录切换到 .env 和 .flaskenv 所在的目录（[相关源码](https://link.zhihu.com/?target=https%3A//github.com/pallets/flask/blob/master/src/flask/cli.py%23L658)）。而如果你的程序模块或程序包不是和 .env/.flaskenv 同级目录的话，就会导致找不到程序实例。
  
使用下面的步骤可以重现：
  

```
$ git clone https://github.com/greyli/flask-env-test
$ cd flask-env-test
$ pip install -r requirements.txt  # or just pip install flask[dotenv]
$ cd hello
$ flask run
```
示例项目的文件结构如下：
  

```
- flask-env-test
    - .env
    - hello
        - app.py
```
像示例程序这样把程序存储在 app.py 文件中时，运行 flask run 你会看到下面的报错：
  

```
$ flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not locate a Flask application. You did not provide the "FLASK_APP" environment variable, and a "wsgi.py" or "app.py" module was not found in the current directory.
```
如果你使用 FLASK\_APP 指定了程序的导入路径，那么错误大概会是这样：
  

```
$ flask run
 * Serving Flask app "myapp"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
Usage: flask run [OPTIONS]

Error: Could not import "myapp".
```
相关链接
  

* [https://github.com/greyli/helloflask/issues/200](https://link.zhihu.com/?target=https%3A//github.com/greyli/helloflask/issues/200)
* [https://github.com/pallets/flask/issues/3561](https://link.zhihu.com/?target=https%3A//github.com/pallets/flask/issues/3561)
* [https://github.com/pallets/flask/pull/3560](https://link.zhihu.com/?target=https%3A//github.com/pallets/flask/pull/3560)
原文链接：[一个困扰我两年的 Flask bug](https://link.zhihu.com/?target=http%3A//greyli.com/a-flask-bug-that-bother-me-two-years/)

> 当前文档由 [markdown文档下载插件](https://github.com/kscript/markdown-download) 下载, 原文链接: [不要在 Flask 程序上层目录创建 .env 和 .flaskenv 文件](https://zhuanlan.zhihu.com/p/128977263)  