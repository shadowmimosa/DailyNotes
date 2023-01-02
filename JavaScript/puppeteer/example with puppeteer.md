```javascript
// example 1: directly open

const puppeteer = require('puppeteer')

;(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    executablePath:
      'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
    devtools: false,
    ignoreHTTPSErrors: true,
    defaultViewport: null,
    timeout: 0,
    args: [],
    ignoreDefaultArgs: ['--enable-automation', '--enable-blink-features'],
  })
  const page = await browser.newPage()
  await page.goto('https://bot.sannysoft.com/')
  await browser.close()
})()

// example 2: open with puppeteer-extra-plugin-stealth

// puppeteer-extra is a drop-in replacement for puppeteer,
// it augments the installed puppeteer with plugin functionality
const puppeteer = require('puppeteer-extra')

// add stealth plugin and use defaults (all evasion techniques)
const StealthPlugin = require('puppeteer-extra-plugin-stealth')
puppeteer.use(StealthPlugin())

// puppeteer usage as normal
puppeteer
  .launch({
    headless: true,
  })
  .then(async (browser) => {
    console.log('Running tests..')
    const page = await browser.newPage()
    await page.goto('https://bot.sannysoft.com')
    await page.waitForTimeout(5000)
    await page.screenshot({
      path: 'testresult.png',
      fullPage: true,
    })
    await browser.close()
    console.log(`All done, check the screenshot. ✨`)
  })

// example 3: open with puppeteer-extra-plugin-portal

// puppeteer-extra is a drop-in replacement for puppeteer,
// it augments the installed puppeteer with plugin functionality
import puppeteer from 'puppeteer-extra'

// add portal plugin
import PortalPlugin from 'puppeteer-extra-plugin-portal'
puppeteer.use(
  PortalPlugin({
    // This is a typical configuration when hosting behind a secured reverse proxy
    webPortalConfig: {
      listenOpts: {
        port: 3000,
      },
      baseUrl: 'https://portal.example.com',
    },
  })
)

// puppeteer usage as normal
puppeteer
  .launch({
    headless: true,
  })
  .then(async (browser) => {
    const page = await browser.newPage()
    await page.goto('https://www.google.com/recaptcha/api2/demo')

    // Open a portal to get a link to it.
    const portalUrl = await page.openPortal()
    console.log('Portal URL:', portalUrl)

    // Wait a long time for the success condition to be met
    const successDiv = await page.waitForSelector('.recaptcha-success', {
      timeout: 86400 * 1000, // 24 hours
    })

    await page.closePortal() // You can manually close a portal with
    await page.close() // Closing the page will automatically close its portal.
    await browser.close() // Closing the browser will automatically close the portals opened on it.
    // When all portals are closed, the web server will automatically shut down
  })
```

```python
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome()
with open('stealth.min.js') as f:
    js = f.read()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": js})
driver.get('https://bot.sannysoft.com/')
driver.save_screenshot('test_by_py.png')

```
