<font size=4 face='楷体'>

## Vue 把 html 导出为 Word

### html 转 word 使用 html-docx-js

- 安装
  ```bash
  npm install html-docx-js --save
  ```
- 引用
  ```js
  import htmlDocx from 'html-docx-js/dist/html-docx'
  ```
  注意引用路径
- html 转为 word
  ```js
  let arr = document.querySelector('#question_doc') //获取dom
  let html = arr.innerHTML //获取html的内容
  let htmlStr = `
        <!DOCTYPE html>
        <html lang="en">
          <body style="font-family:方正仿宋_GBK;mso-ascii-font-family:'Times New Roman';">
            ${html}
          </body>
        </html>` //把获取到的html放入到原生的html中
  let word = htmlDocx.asBlob(htmlStr, { orientation: 'landscape' })
  ```
- **坑**
  这里有坑, 直接这么运行会报错

  ```bash
  Module not found: Error: Can't resolve 'fs' in 'node_modules\html-docx-js\build
  ```

  官方建议设置 webpack config, 详见[issues 48](https://github.com/evidenceprime/html-docx-js/issues/48)

  ```js
  // vue.config.js
  node: {
    fs: 'empty'
  }
  ```

  运行正常, 但是打包又会报错

  ```bash
  Webpack Error - configuration.node has an unknown property 'fs'
  ```

  原因是

  > [Using the following webpack configuration as recommended by the antlr4 documentation is no longer supported](https://stackoverflow.com/questions/64361940)

  **Does not work**

  ```js
  {
    node: {
      fs: 'empty',
      module: 'empty',
      net: 'empty'
    }
  }
  ```

  **Working configuration**

  ```js
  {
    resolve: {
      fallback: {
        fs: false
      }
    }
  }
  ```

  如此可以正常运行, 打包

### 导出 word

- 使用 file-saver

  ```bash
  # 安装 file-saver
  npm install file-saver --save
  ```

  ```js
  import { saveAs } from 'file-saver'

  let word = htmlDocx.asBlob(htmlContent)
  let filename = 'file.docx'

  saveAs(word, filename) // 导出为word
  ```

- 使用原生 a 标签

  ```js
  let word = htmlDocx.asBlob(htmlContent)
  let downloadLink = document.createElement('a')

  downloadLink.href = URL.createObjectURL(word)
  downloadLink.download = 'file.docx'

  downloadLink.click()
  ```

## Reference

[vue 把 html 导出为 word](https://blog.csdn.net/m0_47408822/article/details/121099257)

**2023.06.14**
