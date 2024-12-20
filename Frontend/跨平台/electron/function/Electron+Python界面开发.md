<font size=4 face='楷体'>

Python 开发 GUI 要么太繁琐要么太丑，而前端技术恰巧是最适合做漂亮 UI 的。所以考虑将 Python 和前端技术结合，通过进程通信和前端框架交流，打包成一个完整的桌面 APP。教程分成两种实现方式，一个是 zerorpc 进程通信一个是 http 通信。

这篇教程介绍 zerorpc 的方式，流程如下：

```java
start
 |
 V
+--------------------+
|                    | start
|  electron          +-------------> +------------------+
|                    | sub process   |                  |
| (browser)          |               | python server    |
|                    |               |                  |
| (all html/css/js)  |               | (business logic) |
|                    |   zerorpc     |                  |
| (node.js runtime,  | <-----------> | (zeromq server)  |
|  zeromq client)    | communication |                  |
|                    |               |                  |
+--------------------+               +------------------+
```

## Electron 基础

> 详情见官方文档： [https://electronjs.org/docs][https_electronjs.org_docs]

如果你可以建一个网站，你就可以建一个桌面应用程序。 Electron 是一个使用 JavaScript, HTML 和 CSS 等 Web 技术创建原生程序的框架，它负责比较难搞的部分，你只需把精力放在你的应用的核心上即可。

![](https://pic2.zhimg.com/v2-20ea5503f18da0e598d5f765e3b3b0d1_b.jpg)

有很多有名的 App 是用 Electeon 开发的，如：Skype 和 GitHub 以及著名编辑器 Atom，所以这个框架在水平上是被认可的。

![](https://pic1.zhimg.com/v2-d60303e945e27107a637a580e2e8366c_b.jpg)

Electron 可以让你使用纯 JavaScript 调用丰富的原生(操作系统) APIs 来创造桌面应用。 你可以把它看作一个专注于桌面应用的 Node. js 的变体，而不是 Web 服务器。

这不意味着 Electron 是某个图形用户界面（GUI）库的 JavaScript 版本。 相反，Electron 使用 web 页面作为它的 GUI，所以你能把它看作成一个被 JavaScript 控制的，精简版的 Chromium 浏览器。

## 安装

为你的新 Electron 应用创建一个新的空文件夹。 打开你的命令行工具，然后从该文件夹运行`npm init`。将`package.json`修改一下。

```java
{
    "name": "your-app",
    "version": "0.1.0",
    "main": "main.js",
    "scripts": {
      "start": "electron ."
    }
 }
```

现在，您需要安装`electron`。 我们推荐的安装方法是把它作为您 app 中的开发依赖项，这使您可以在不同的 app 中使用不同的 Electron 版本。 在您的 app 所在文件夹中运行下面的命令：

```java
npm install --save-dev electron
```

## 使用

`electron`模块包含了 Electron 提供的所有 API 和功能，引入方法和普通 Node.js 模块一样：

```java
const electron = require('electron')
```

`electron` 模块所提供的功能都是通过命名空间暴露出来的。 比如说： `electron.app`负责管理 Electron 应用程序的生命周期， `electron.BrowserWindow`类负责创建窗口。 下面是一个简单的`main.js`文件，它将在应用程序准备就绪后打开一个窗口：

```java
const {app, BrowserWindow} = require('electron')

  function createWindow () {
    // 创建浏览器窗口
    win = new BrowserWindow({width: 800, height: 600})

    // 然后加载应用的 index.html。
    win.loadFile('index.html')
  }

  app.on('ready', createWindow)
```

您应当在 `main.js` 中创建窗口，并处理程序中可能遇到的所有系统事件。 下面我们将完善上述例子，添加以下功能：打开开发者工具、处理窗口关闭事件、在 macOS 用户点击 dock 上图标时重建窗口，添加后，main. js 就像下面这样：

```java
const {app, BrowserWindow} = require('electron')

  // Keep a global reference of the window object, if you don't, the window will
  // be closed automatically when the JavaScript object is garbage collected.
  let win

  function createWindow () {
    // 创建浏览器窗口。
    win = new BrowserWindow({width: 800, height: 600})

    // 然后加载应用的 index.html。
    win.loadFile('index.html')

    // 打开开发者工具
    win.webContents.openDevTools()

    // 当 window 被关闭，这个事件会被触发。
    win.on('closed', () => {
      // 取消引用 window 对象，如果你的应用支持多窗口的话，
      // 通常会把多个 window 对象存放在一个数组里面，
      // 与此同时，你应该删除相应的元素。
      win = null
    })
  }

  // Electron 会在初始化后并准备
  // 创建浏览器窗口时，调用这个函数。
  // 部分 API 在 ready 事件触发后才能使用。
  app.on('ready', createWindow)

  // 当全部窗口关闭时退出。
  app.on('window-all-closed', () => {
    // 在 macOS 上，除非用户用 Cmd + Q 确定地退出，
    // 否则绝大部分应用及其菜单栏会保持激活。
    if (process.platform !== 'darwin') {
      app.quit()
    }
  })

  app.on('activate', () => {
    // 在macOS上，当单击dock图标并且没有其他窗口打开时，
    // 通常在应用程序中重新创建一个窗口。
    if (win === null) {
      createWindow()
    }
  })

  // 在这个文件中，你可以续写应用剩下主进程代码。
  // 也可以拆分成几个文件，然后用 require 导入。
```

最后，创建你想展示的 `index.html`：

```java
<!DOCTYPE html>
  <html>
    <head>
      <meta charset="UTF-8">
      <title>Hello World!</title>
    </head>
    <body>
      <h1>Hello World!</h1>
      We are using node <script>document.write(process.versions.node)</script>,
      Chrome <script>document.write(process.versions.chrome)</script>,
      and Electron <script>document.write(process.versions.electron)</script>.
    </body>
  </html>
```

## 启动

在创建并初始化完成 `main.js`、 `index.html`和`package.json`之后，您就可以在当前工程的根目录执行 `npm start` 命令来启动刚刚编写好的 Electron 程序了。

![](https://pic3.zhimg.com/v2-a2b0d7a35482162dd5a63bfb1053ca36_b.jpg)

## Python 部分

安装`pip install zerorpc`。在项目根目录创建文件夹`py`，用于存放 Python 相关代码。新建一个 python 文件，命名为 api.py。敲入如下 demo。

```java
import zerorpc

class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
```

然后命令行里运行`python api.py`。再另一个终端输入`zerorpc tcp://localhost:4242 hello NXB`,如果得到`Hello,NXB`则没有问题。

## Electron 部分

接着之前的`main.js`后面写。我们首先需要 node.js 能够调用 Python 进程。

```java
const path=require('path')

let pyProc = null
let pyPort = null

const createPyProc = () => {
  let port = '4242'
  let script = path.join(__dirname, 'py', 'api.py')
  pyProc = require('child_process').spawn('python', [script, port])
  if (pyProc != null) {
    console.log('child process success')
  }
}

const exitPyProc = () => {
  pyProc.kill()
  pyProc = null
  pyPort = null
}

app.on('ready', createPyProc)
app.on('will-quit', exitPyProc)
```

写完后运行`npm start`看看能不能启动 python 子程序按照之前的方式测试一下能不能通信。没问题的话继续。

修改我们的主页`index.html`，构建一个输入框。我们希望在输入框里输入字符，下方可以动态显示 Hello,XX。

```java
<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Hello XX</title>
  </head>
  <body>
    <input id="name" ></input>
    <p id="result" color='black'></p>
  </body>
  <script>
    require('./render.js')
  </script>
</html>
```

在根目录下创建`render.js`用于监听输入框，将输入框的内容动态发送给 python 进程，并接收反回来的消息。

```java
// renderer.js
var zerorpc = require("zerorpc");
var client = new zerorpc.Client();
client.connect("tcp://127.0.0.1:4242");

let name = document.querySelector('#name')
let result = document.querySelector('#result')
name.addEventListener('input', () => {
  client.invoke("hello", name.value, (error, res) => {
    if(error) {
      console.error(error)
    } else {
      result.textContent = res
    }
  })
})
name.dispatchEvent(new Event('input'))
```

如果没问题的话应该是这样的效果：

![](https://pic2.zhimg.com/v2-ed8a96d3cd4ae44c06425d888aaee21d_b.gif)

## 打包

测试没问题之后我们需要将应用打包，因为别人电脑上不一定装了 node.js 或是 python。首先要装个打包工具`pip install pyinstaller`。

在`package.json`的`script`中加入`"build-python":"pyinstaller ./py/api.py --clean --distpath ./pydist"`。然后运行`npm run build-python编译一下`。编译完了可以把根目录下生成的`build`文件夹和`api.spec`删了。如果中间报错 `AttributeError: module 'enum' has no attribute 'IntFlag'`，就运行`pip uninstall enum34`把 enum34 删了。

> This is likely caused by the package `enum34`. Since python 3.4 there's a standard library `enum`module, so you should uninstall `enum34`, which is no longer compatible with the enum in the standard library since `enum.IntFlag` was added in python 3.6

之前子进程是通过调用 python 命令运行的，现在我们要换成生成的可执行程序。修改`main.js`：

```java
// let script = path.join(__dirname, 'py', 'api.py')
  // pyProc = require('child_process').spawn('python', [script, port])
  let script = path.join(__dirname, 'pydist', 'api','api')
  pyProc = require('child_process').execFile(script, [port])
```

运行`npm start`可以查看效果。

在根目录运行`npm install electron-packager --save-dev`安装 Electron 打包模块。然后将`"pack-app": "./node_modules/.bin/electron-packager . --overwrite --ignore=py$"`写入`package.json`的 script 中。

运行`npm run pack-app`打包程序。最后会生成可执行文件，复制到别的电脑也可以运行。

![](https://pic1.zhimg.com/v2-3bd7a63aeb9d92d9f9a29c1c40c73148_b.jpg)

[https_electronjs.org_docs]: https://link.zhihu.com/?target=https%3A//electronjs.org/docs

### Reference

[【linux】CentOS 查看系统时间，修改时区](https://www.cnblogs.com/sxdcgaq8080/p/11155232.html)

**2022.08.17**
