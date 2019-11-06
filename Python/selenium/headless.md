<font size=4 face='楷体'>

## 无头浏览器（Headless Chrome）

曾经的 PhantomJS 逐渐的被 selenium 放弃支持

> 在使用 PhantomJS 时候，出现提示：

    UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead

> 意思是说：新版本的 Selenium 不再支持 PhantomJS 了，请使用 Chrome 或 Firefox 的无头版本来替代。


### Headless Chrome 基本配置  

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.baidu.com/")
```

### Reference

[PhantomJS的替代品--无头浏览器（Headless Chrome）](https://www.cnblogs.com/liangmingshen/p/9989049.html)
[官方文档](https://developers.google.com/web/updates/2017/04/headless-chrome)

**2019.10.6**
