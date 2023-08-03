<font size=4 face='楷体'>

## python 执行 js

### [PyExecJS](https://github.com/doloopwhile/PyExecJS)

_依赖本地 js 环境, 多数情况下不适用_

PyExecJS 是使用最多的一种方式, 底层实现方式是：在**本地 JS 环境**下运行 JS 代码
支持的 JS 环境包含：Node.js, PyV8, PhantomJS, Nashorn 等
首先, 我们需要安装依赖包 PyExecJS

```bash
//py_exec_js_demo.py

//安装依赖
pip3 install PyExecJS
```

然后, 从 JS 文件中读取源码

```python
def js_from_file(file_name):
    """
    读取js文件
    :return:
    """
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()

    return result
```

最后, 使用 `execjs` 类的`compile()`方法编译加载上面的 JS 字符串, 返回一个上下文对象

```python
import execjs

from js_code import *

# 编译加载js字符串
context1 = execjs.compile(js_from_file('./norm.js'))
```

最后, 调用上下文对象的`call()` 方法执行 JS 方法
其中, 参数包含：JS 代码被调的方法名, 对应方法的传入参数

```python
# 调用js代码中的add()方法, 参数为2和3
# 方法名：add
# 参数：2和3
result1 = context1.call("add", 2, 3)

print(result1)
```

需要注意的, 由于 PyExecJS 运行在本地 JS 环境下, 使用之前会启动 JS 环境, 最终导致运行速度会偏慢

#### 执行含有 document、window 等对象的 js 代码

- 安装 jsdom

全局安装会报错 `execjs._exceptions.ProgramError: Error: Cannot find module 'jsdom'`
需要再项目路径或 python 执行文件路径下安装 jsdom

```bash
npm i jsdom -g
```

或者指定模块的所在目录

```python
import execjs

ct = execjs.compile(js,cwd='node_modules')
```

最后在对应 js 代码里最前面替换

```js
const jsdom = require('jsdom')
const { JSDOM } = jsdom
const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`)
window = dom.window
document = window.document
XMLHttpRequest = window.XMLHttpRequest
navigator = window.navigator
```

### [js2py](https://github.com/PiotrDabkowski/Js2Py)

_默认有 crypto-js 包, 好评; 但没有 crypto 包_

js2py 作为一个纯 Python 实现的 JS 解释器, 可以完全脱离 JS 环境, 直接将 JS 代码转换为 Python 代码

首先, 安装依赖库

```bash
# 安装依赖库
pip3 install js2py
```

然后使用 js2py 中的`EvalJs()`方法生成一个上下文对象

```python
# 使用获取上下js2py生成一个上下文环境
context = js2py.EvalJs()
```

接着利用上下文对象执行 JS 脚本, 转换为 Python 代码

```python
# 执行整段JS代码
context.execute(js_content)
```

最后, 利用上下文调用 JS 中的方法, 并制定输入参数即可

```python
# 使用上下文context调用具体的函数
# 函数名：add
# 参数：1, 2
result = context.add(1, 2)
print(result)
```

需要注意是, 如果 JS 是很长的混淆代码, 转换为 Python 的过程可能会报错

### Node.js

_依赖本地 js 的环境, 同 PyExecJS_

实际上是使用 Python 的 os.popen 执行 node 命令, 执行 JS 脚本
首先, 确保本地已经安装了 Node.js 环境
修改 JS 脚本, 新增一个导出函数 init , 方便内部函数被调用

```javascript
//计算两个数的和
function add(num1, num2) {
  return num1 + num2
}

//新增一个导出函数（node方式）
module.exports.init = function (arg1, arg2) {
  //调用函数, 并返回
  console.log(add(arg1, arg2))
}
```

然后, 将调用 JS 方法的命令组成一个字符串

```python
# 组成调用js的命令
# node命令：node -e
cmd = 'node -e "require(\\"%s\\").init(%s,%s)"' % ('./norm', 3, 5)
```

最后, 通过 os.popen 执行命令即可

```python
pipeline = os.popen(cmd)
# 读取结果
result = pipeline.read()
print('结果是:', result)
```

### [PyV8](https://github.com/emmetio/pyv8-binaries)

_未尝试, 安装方式看着就 移植成本高_

PyV8 是 Google 将 Chrome V8 引擎用 Python 封装的依赖库

它不依赖本地 JS 环境, 运行速度很快

```python
import PyV8
from js_code import js_from_file

with PyV8.JSContext() as ctx:
    ctx.eval(js_from_file('./norm.js'))

# 调用js函数, 指定参数
ctx.locals.add(1, 2)
```

### Reference

[python 调用 js 的四种方式](https://www.jb51.net/article/209279.htm)
[python 使用 execjs 执行含有 document、window 等对象的 js 代码，使用 jsdom 解决](https://www.cnblogs.com/huchong/p/11044238.html)

**Create On 2022.07.27, Update On 2023.06.14**
