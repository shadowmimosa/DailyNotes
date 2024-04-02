<font size=4 face='楷体'>

## Electron 与 python 交互

### IPC 通讯

> 在计算机科学中，进程间通信（IPC）特指操作系统提供的机制，允许进程管理共享数据。通常，应用程序可以使用 IPC，分类为客户机和服务器，其中客户机请求数据，服务器响应客户机请求。

### 子进程

创建 python 脚本文件 `calc.py`

```python
from sys import argv
from calculator.simple import SimpleCalculator

def calc(text):
	"""based on the input text, return the operation result"""
	try:
		c = SimpleCalculator()
		c.run(text)
		return c.log[-1]
	except Exception as e:
		print(e)
		return 0.0

if __name__ == '__main__':
    print(calc(argv[1]))
```

使用 [child_process](https://nodejs.org/api/child_process.html) 生成 Python 进程

```javascript
function sendToPython() {
  var python = require('child_process').spawn('python', [
    'calc.py',
    input.value,
  ])
  python.stdout.on('data', function (data) {
    console.log('Python response: ', data.toString('utf8'))
    result.textContent = data.toString('utf8')
  })

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`)
  })

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`)
  })
}

btn.addEventListener('click', () => {
  sendToPython()
})

btn.dispatchEvent(new Event('click'))
```

### [python-shell](https://www.npmjs.com/package/python-shell)

python-shell 可用于

- 生成 Python 脚本
- 在文本、JSON 和二进制模式之间切换
- 通过 stdin 和 stdout 流进行数据传输
- 在发生错误的情况下获取堆栈跟踪

```javascript
function sendToPython() {
  var { PythonShell } = require('python-shell')

  let options = {
    mode: 'text',
    args: [input.value],
  }

  PythonShell.run('./py/calc.py', options, function (err, results) {
    if (err) throw err
    // results is an array consisting of messages collected during execution
    console.log('results: ', results)
    result.textContent = results[0]
  })
}
```

### 客户端-服务器通信

python 中运行 flask 服务

```python
import sys
from flask import Flask
from flask_cors import cross_origin
from calculator.simple import SimpleCalculator

def calcOp(text):
	"""based on the input text, return the operation result"""
	try:
		c = SimpleCalculator()
		c.run(text)
		return c.log[-1]
	except Exception as e:
		print(e)
		return 0.0

app = Flask(__name__)

@app.route("/<input>")
@cross_origin()
def calc(input):
    return calcOp(input)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)
```

js 中访问

```javascript
let input = document.querySelector('#input')
let result = document.querySelector('#result')
let btn = document.querySelector('#btn')

function onclick() {
  fetch(`http://127.0.0.1:5001/${input.value}`)
    .then((data) => {
      return data.text()
    })
    .then((text) => {
      console.log('data: ', text)
      result.textContent = text
    })
    .catch((e) => {
      console.log(e)
    })
}
sendToPython()

btn.addEventListener('click', () => {
  onclick()
})

btn.dispatchEvent(new Event('click'))
```

### 交互项目参考

[Electron as GUI of Python Applications](https://github.com/fyears/electron-python-example)
[A better way to make GUIs for your python apps](https://github.com/SouravJohar/python-app-with-electron-gui)
[This project is just a sample to show how the integration between Python and Electron works.](https://github.com/Augustomesquita/PythonElectron)

### Reference

[连接 Python 3 和 Electron/Node.JS：构建现代桌面应用程序](https://blog.csdn.net/mzl87/article/details/106202144/)

**2022.08.22**
