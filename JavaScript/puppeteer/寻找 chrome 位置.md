<font size=4 face='楷体'>

## Chrome 浏览器安装位置

### 使用 [carlo](https://github.com/GoogleChromeLabs/carlo) 查找

_2022.04 尝试无效_

```bash
// 安装对应 chrome@71 对应的 puppeteer
npm install puppeteer-core@chrome-71
// 安装 Carlo
npm i carlo
// 或 yarn add carlo
```

```javascript
const puppeteer = require('puppeteer-core')
//find_chrome模块来源于GoogleChromeLabs的Carlo,可以查看本机安装Chrome目录，详细请查看底部博客,

const findChrome = require('./node_modules/carlo/lib/find_chrome')

;(async () => {
  let findChromePath = await findChrome({})
  let executablePath = findChromePath.executablePath
  console.log(executablePath)
  const browser = await puppeteer.launch({
    executablePath,
    headless: false,
  })

  const page = await browser.newPage()
  await page.goto('http://www.woleigequ.net/')
  /*
  	dosomeThing
  */

  await browser.close()
})()
```

或者

```javascript
const puppeteer = require('puppeteer-core')
const findChrome = require('./find_chrome')

;(async () => {
  const browser = await puppeteer.launch({
    executablePath: findChrome().pop(),
    pipe: true,
    defaultViewport: null,
    headless: false,
    userDataDir: '.profile',
    // args,
  })

  const page = await browser.newPage()
  await page.goto('https://www.bilibili.com/')
  await page.screenshot({ path: 'example.png', fullPage: true })

  await browser.close()
})()
```

### Windows 10

- %ProgramFiles%\Google\Chrome\Application\chrome.exe
- %ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe
- %LocalAppData%\Google\Chrome\Application\chrome.exe

### Windows 7

- C:\Program Files (x86)\Google\Application\chrome.exe

### Vista

- C:\Users\UserName\AppDataLocal\Google\Chrome

### XP

- C:\Documents and Settings\UserName\Local Settings\Application Data\Google\Chrome

### Reference

[Google Chrome Path in Windows 10](https://stackoverflow.com/a/40674915)
[如何使用 puppeteer-core,puppeteer 使用本地 Chrome，puppeteer 下载失败问题](https://blog.csdn.net/w20101310/article/details/95491180)
[chrome + puppeteer](https://www.52cik.com/2018/12/31/chrome-puppeteer.html)

**2022.05.10**
