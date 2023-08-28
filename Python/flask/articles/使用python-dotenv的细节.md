---
title: 使用python-dotenv的细节
date: 2022-07-05 14:11:01
copyright: false
author: 竹风抚荷塘
home: https://www.zhihu.com/people/pythonmonk
origin: zhihu
url: https://zhuanlan.zhihu.com/p/101517745
tag: 
categories: 
description: 前言日常项目中，敏感信息（如数据库密码）比较推荐使用.env文件来单独管理，且不纳入git管理中。而...
---

### 前言
日常项目中，敏感信息（如数据库密码）比较推荐使用`.env`文件来单独管理，且不纳入git管理中。而目前比较流行的解析`.env`则是`python-dotenv`。
  

### 坑一：默认不会更新的配置项
官方文档的例子简单易懂。
  

```
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
```
然而这个例子里面缺隐藏了一个大坑。此时当用户在`.env`中更新配置项的值时，是不会生效的。原因是`load_dotenv`默认不会更新已经存在的配置项。推荐使用`override`参数，推荐代码如下:
  

```
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
```

### 坑二：`#`的处理
考虑`.env`中的如下写法:
  

```
BASEURL=http://codehub.com/#/python
```
暂且不讨论在url中带`#`是否优雅。`#`在url中表示锚点，的确是会经常用到的；然而在`Python`中却是表示注释开始。此时`BASEURL`的值会是`http://codehub.com/`。以下写法均符合预期。
  

```
BASEURL="http://codehub.com/#/python"
BASEURL='http://codehub.com/#/python'
```
需要使用双引号/单引号括起来。

> 当前文档由 [markdown文档下载插件](https://github.com/kscript/markdown-download) 下载, 原文链接: [使用python-dotenv的细节](https://zhuanlan.zhihu.com/p/101517745)  