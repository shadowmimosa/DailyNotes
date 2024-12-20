<font size=4 face='楷体'>

## PDF 相关

- [vue-pdf](https://github.com/FranckFreiburger/vue-pdf)
  很久没更新了
- [vue-pdf-embed](https://github.com/hrynko/vue-pdf-embed)
- [pdf.js](https://github.com/mozilla/pdf.js)
  PDF Reader in JavaScript
  其它的基本都是这个库的第三方实现

- [pdfjs-dist 加载不全的解决方案 cmaps 本地路径](https://blog.csdn.net/Li_Ning21/article/details/133890431)

  ```js
  // vue.config.js
  const CopyPlugin = require('copy-webpack-plugin')

  module.exports = defineConfig({
    configureWebpack: {
      plugins: [
        new CopyPlugin({
          patterns: [
            // 将 pdfjs-dist/cmaps/ 目录复制到输出目录的 cmaps/ 目录
            { from: 'node_modules/pdfjs-dist/cmaps/', to: 'cmaps/' },
          ],
        }),
      ],
    },
  })

  // 使用

  import { getDocument } from 'pdfjs-dist/build/pdf'
  const loadingTask = getDocument({
    data: pdfData,
    cMapUrl: '/cmaps/',
  })
  ```

  这样打包之后就会带着字体文件

### Reference

- [移动端使用 pdfjs-dist 来预览 pdf 文件的一些坑](https://segmentfault.com/a/1190000042089590)

**2024.04.22**
