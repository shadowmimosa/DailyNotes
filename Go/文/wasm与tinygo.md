---
created: 2024-08-05T17:29:19 (UTC +08:00)
tags: [Go, Go每日一库]
source: https://www.cnblogs.com/luckzack/p/17737341.html
author: luckzack
---

# wasm 与 tinygo

---

WASM 的概念，这几年还是挺火的，新的语言，比如 Rust、Go、Swift 等，都对 WASM 提供支持。相比之下，Go 语言的简单性，使得对 WASM 的支持，使用起来也较简单。本文是目前公开资料中为数不多较完整的教程，希望能对你有帮助。

标题说：“Golang 中的 Wasm 太棒了。”，但请用几句话来说“Wasm”是什么？  
WebAssembly 主页说： WebAssembly（缩写为 Wasm）是一种基于堆栈的虚拟机的二进制指令格式。Wasm 被设计为编程语言的可移植编译目标，支持在 Web 上部署客户端和服务器应用程序。
总结就是：

- Wasm 是一种可移植的格式（如 Java 或 .Net），你可以在任何有支持它的主机的地方执行它。最初，主要的主机是带有浏览器的 JavaScript”。

现在，你可以用 JavaScript 和 NodeJS 运行 Wasm，我们最近看到了像 Wasmer 项目这样的 Wasm 运行时的诞生，允许在任何地方运行 Wasm。  
我喜欢说 一个 wasm 文件就像一个容器镜像，但更小，没有操作系统。

你可以用多种语言编译一个 Wasm 文件：C/C++、Rust、Golang、Swift ……我们甚至看到了专门用于构建 Wasm 的语言的出现，比如 **AssemblyScript** 或有前途的 **Grain**（可以密切关注它，语法很可爱）。  
今年夏天，我决定开始使用 Wasm。这种趋势似乎是使用 Rust，但我很快就明白我的小步骤会很复杂。困难不一定来自语言本身。最乏味和困难的部分是我在浏览器中运行一个简单的“Hello World”所需的所有工具。经过一番搜索，我发现 **Golang** 为 **Wasm** 提供了非常简单的支持（比 Rust 简单得多）。所以，我的假期作业是用 Golang 完成的。  
Golang 对 Wasm 的支持非常棒。通常，WebAssembly 有四种数据类型（32 和 64 位整数，32 和 64 位浮点数），使用带有字符串参数（甚至 JSON 对象）的函数可能会很混乱。幸运的是，Go 提供了 wasm_exec.js 与 JavaScript API 交互的文件。

## WASM 在 Go 中的简单示例

创建项目：

```bash
 go-wasm/
 |__ out/
 |__ go/
     |__ main.go
```

**main.go:**

```go
package main

func main() {
   println("Hello World!!!")
}

```

运行 go 文件 go run go/main.go。这将打印 Hello World。

现在我们可以将它编译成 WebAssembly 模块并作为 WebAssembly 运行：

```bash
GOOS=js GOARCH=wasm go build -o out/main.wasm go/main.go
```

这将在 out 文件夹里生成 main.wasm。与 Rust 不同，Golang 不会生成任何绑定文件。

拷贝 wasm 绑定文件`wasm_exec.js`到 out 目录中。

```bash
# go原生版本
cp "$(go env GOROOT)/misc/wasm/wasm_exec.js" ./out

```

在 out 目录中创建一个`index.html`文件并添加以下内容：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Go wasm</title>
  </head>

  <body>
    <script src="wasm_exec.js"></script>
    <script>
      const go = new Go()
      WebAssembly.instantiateStreaming(
        fetch('main.wasm'),
        go.importObject
      ).then((res) => {
        go.run(res.instance)
      })
    </script>
  </body>
</html>
```

也可以用这种更健壮的版本：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Go wasm</title>
  </head>

  <body>
    <script src="wasm_exec.js"></script>
    <script>
      // This is a polyfill for FireFox and Safari
      if (!WebAssembly.instantiateStreaming) {
        WebAssembly.instantiateStreaming = async (resp, importObject) => {
          const source = await (await resp).arrayBuffer()
          return await WebAssembly.instantiate(source, importObject)
        }
      }

      // Promise to load the wasm file
      function loadWasm(path) {
        const go = new Go()

        return new Promise((resolve, reject) => {
          WebAssembly.instantiateStreaming(fetch(path), go.importObject)
            .then((result) => {
              go.run(result.instance)
              resolve(result.instance)
            })
            .catch((error) => {
              reject(error)
            })
        })
      }

      // Load the wasm file
      loadWasm('main.wasm')
        .then((wasm) => {
          console.log('main.wasm is loaded ')
        })
        .catch((error) => {
          console.error(error)
        })
    </script>
  </body>
</html>
```

> 最重要的部分是：  
> 这行代码  
> 和这一行 WebAssembly.instantiateStreaming，它是允许加载 wasm 文件的 JavaScript API。

index.html 加载 wasm_exec.js 文件。请注意，此文件适用于 Browser 和 NodeJS 环境，它导出一个 Go 对象。

然后我们添加一个本地脚本。在脚本中，我们执行以下操作：

- Instantiate Go from the wasm_exec.js.
- Fetch the WebAssembly Module using instantiateStreaming

接下来启动一个 Web server 尝试一下 go wasm。

`./webserver.go:`

```go
package main

import (
        "log"
        "net/http"
        "strings"
)

const dir = "./out"

func main() {
        fs := http.FileServer(http.Dir(dir))
        log.Print("Serving " + dir + " on http://localhost:8080")
        http.ListenAndServe(":8080", http.HandlerFunc(func(resp http.ResponseWriter, req *http.Request) {
                resp.Header().Add("Cache-Control", "no-cache")
                if strings.HasSuffix(req.URL.Path, ".wasm") {
                        resp.Header().Set("content-type", "application/wasm")
                }
                fs.ServeHTTP(resp, req)
        }))
}

```

项目结构：

```bash
├── go
│   └── main.go
└── out
    ├── index.html
    ├── wasm_exec.js
    └── main.wasm
├── webserver.go
```

运行：

```bash
go run webServer.go
```

打开 `http://localhost:8080` ,可以在 console 上显示 Hello World!!!：

注意：  
由于 wasm 是在网页上实时加载，所以生成的 WebAssembly 模块的文件大小非常重要。上例中仅仅一个 Hello World 就高达 1.3MB，对于现代网页来说是完全不能接受的。

```bash
-rw-r--r--  1 sendilkumar  staff   482B Jul  5 23:20 index.html
-rwxr-xr-x  1 sendilkumar  staff   1.3M Jul  5 23:19 main.wasm
-rw-r--r--  1 sendilkumar  staff    13K Jul  5 23:18 wasm_exec.js

```

> 或许 WebAssembly 能提供更优秀的性能，但如果引入的模块过大的话就不应当考虑它。

别当心，我们有 Tiny GO!

## TinyGO 使用

TinyGo 是一个将 Golang 带入微控制器和现代网络浏览器的项目。他们有一个基于 LLVM 编译的全新编译器。使用 TinyGo，我们可以生成经过优化以在芯片中执行的微小库。

TinyGo 允许为微控制器编译 Golang 源代码，它也可以将 Go 代码编译为 Wasm。TinyGo 是一个用于“小地方”的编译器，因此生成的文件要小得多。

查看如何安装 tinygo：[https://tinygo.org/getting-started/](https://tinygo.org/getting-started/)

安装后，您可以使用 TinyGo 编译任何 Golang 代码。我们可以使用以下命令将 Golang 编译成 WebAssembly 模块。

```bash
tinygo build -o out/main.wasm -target wasm ./go/main.go
```

使用 tinygo 编译后，wasm 模块减小到 3.8K：

```bash
-rw-r--r--  1 sendilkumar  staff   482B Jul  5 23:20 index.html
-rwxr-xr-x  1 sendilkumar  staff   3.8K Jul  5 23:29 main.wasm
-rw-r--r--  1 sendilkumar  staff    13K Jul  5 23:18 wasm_exec.js
```

使用 tinygo 编译的 wasm 模块，在加载的时候也要搭配 tinygo 版本的 wasm_exec.js:

```bash
cp "$(tinygo env TINYGOROOT)/targets/wasm_exec.js" ./out/wasm_exec.js

# 或者从这里下载
https://github.com/tinygo-org/tinygo/blob/master/targets/wasm_exec.js
```

再重新启动 webserver 尝试下吧！

## References

[Go 中的 WASM 很棒：全网最全示例教程](https://mp.weixin.qq.com/s/HNaH775qMLqY0-Oq7BQEsQ)  
[tinygo 快速入门](https://mp.weixin.qq.com/s/HNaH775qMLqY0-Oq7BQEsQ)  
[如何使用 WebAssembly 提升性能？](https://blog.51cto.com/u_15057848/2567467)  
[从首届 WebAssembly Summit 看 Wasm 未来发展方向](https://cloud.tencent.com/developer/news/606869)  
\[

\]([https://blog.51cto.com/u_15057848/2567467](https://blog.51cto.com/u_15057848/2567467))

- [WASM 是什么](https://www.cnblogs.com/luckzack/p/17737341.html#wasm-%E6%98%AF%E4%BB%80%E4%B9%88)
- [WASM 在 Go 中的简单示例](https://www.cnblogs.com/luckzack/p/17737341.html#wasm-%E5%9C%A8go%E4%B8%AD%E7%9A%84%E7%AE%80%E5%8D%95%E7%A4%BA%E4%BE%8B)
- [TinyGO 使用](https://www.cnblogs.com/luckzack/p/17737341.html#tinygo-%E4%BD%BF%E7%94%A8)
- [References](https://www.cnblogs.com/luckzack/p/17737341.html#references)
