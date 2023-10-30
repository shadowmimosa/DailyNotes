<font size=4 face='楷体'>

## electron 打包 puppeteer

### 打包后报错

默认打包情况, 找不到 chromium 路径

打包设置

```json
"build": {
   "asar": true,
   "asarUnpack": "node_modules/puppeteer/.local-chromium/**/*"
 }
```

设置打包后运行路径

```javascript
function getChromiumExecPath() {
  return puppeteer.executablePath().replace('app.asar', 'app.asar.unpacked')
}

export function createBrowser(options = {}) {
  return puppeteer.launch({
    ...options,
    executablePath: getChromiumExecPath(),
  })
}
```

搭配判断运行环境

```javascript
async function openBrowser() {
  if (isDev) {
    var executablePath = puppeteer.executablePath()
  } else {
    var executablePath = puppeteer
      .executablePath()
      .replace('app.asar', 'app.asar.unpacked')
  }
  const browser = await puppeteer.launch({ executablePath: executablePath })

  return browser
}
```

### Reference

[puppeteer-fails-in-react-app-after-running-electron-builder](https://stackoverflow.com/questions/62602604)
[Error: Failed to launch the browser process! spawn /app/node_modules/puppeteer/.local-chromium/linux-756035/chrome-linux/chrome ENOENT](https://github.com/puppeteer/puppeteer/issues/5992)

**2022.08.22**
