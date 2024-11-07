<font size=4 face='楷体'>

## Vant 监听物理返回退出功能

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>NanChen_web</title>
    <link
      rel="stylesheet"
      href="https://fastly.jsdelivr.net/npm/vant@3/lib/index.css"
    />
  </head>

  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.ts"></script>
    <script src="https://fastly.jsdelivr.net/npm/vant@3/lib/vant.min.js"></script>
  </body>
  <style></style>
  <script>
    var time = '' // 用来存上一次按键时间；
    setTimeout(() => {
      // 监听返回按钮
      document.addEventListener('plusready', function () {
        plus.key.addEventListener(
          'backbutton',
          function (evt) {
            var webview = plus.webview.currentWebview()
            var url = location.hash.split('/')[1]
            if (url === 'index') {
              // 处于首页时,实现退出app操作
              // vant.Toast('提示');
              if (new Date() - time < 2000) {
                // 小于2s,退出程序
                webview.close()
              } else {
                // 重置时间，
                time = new Date()
                vant.Toast('再次点击退出', 2000)
              }
              return
            } else {
              vant.Toast('不满足条件')
              history.go(-1) // 不满足退出操作，，返回上一页
            }
          },
          false
        )
      })
    }, 10)
  </script>
</html>
```

### Reference

[Vue3+Vant3——监听物理返回退出功能](https://blog.csdn.net/nanchen_J/article/details/127844658)

**2023.11.17**
