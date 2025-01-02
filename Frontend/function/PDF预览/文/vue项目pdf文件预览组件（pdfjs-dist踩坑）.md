---
created: 2024-09-24T16:22:44 (UTC +08:00)
tags: [前端]
source: https://juejin.cn/post/7244722310204014649
author: 自学前端第一天
---

# vue 项目 pdf 文件预览组件（pdfjs-dist 踩坑）

最近项目中需要使用 pdf 的预览功能，最初选用的 vue-pdf，vue-pdf 中有一些问题，改用 vue-pdf-signature，该插件解决了 vue-pdf 的签章显示问题&反复预览 pdf 无法重载。但是最近有了新的问题，最新 iphone14 手机会出现大文件加载不全的问题，小文件正常显示（iphone14 的适配真的头疼）。于是重新封装了 pdf 预览的组件。

之前封装过 word，pdf 和图片的预览组件，分别使用 mammoth，vue-pdf-signature 和 vant 自带的图片预览，先看下 vue-pdf-signature 实现的代码

```html
<template>
  <div>
    <div class="viewBox">
      <div class="word-box" ref="docPreview" v-if="type === 'docx'"></div>
      <div class="txt-box" v-if="type === 'txt'" ref="txtPreview"></div>
      <!-- pdf组件 -->
      <div class="pdf-box" v-if="type === 'pdf'">
        <pdf
          :src="newSrc"
          v-for="i in numPages"
          :key="i"
          :page="i"
          style="display: inline-block; width: 100%"
        >
        </pdf>
      </div>
    </div>
  </div>
</template>

<script>
  import pdf from 'vue-pdf-signature'
  import CMapReaderFactory from 'vue-pdf-signature/src/CMapReaderFactory'
  import mammoth from 'mammoth'
  import { ImagePreview, Toast } from 'vant'
  export default {
    name: 'ComPre',
    components: { pdf, CMapReaderFactory },
    data() {
      return {
        type: '',
        isShow: false,
        fileIdList: [],
        fileList: [],
        newSrc: '',
        sheetNames: [],
        wsObj: {},
        isAllowed: true,
        numPages: 1,
        pdfURL: null, //pdf预览url
      }
    },
    created() {
      //获取预览文件preData，type为文件类型，file为二进制流
      this.preData = this.$route.params.preData
      this.type = this.preData.type
      this.showFile(this.preData.type)
    },
    methods: {
      onLoading() {
        Toast.loading({
          duration: 500,
          forbidClick: true,
          message: '加载中...',
          className: 'loading',
        })
      },
      showFile(type) {
        const typeObj = {
          docx: 'word',
          pdf: 'pdf',
          txt: 'txt',
          jpg: 'img',
          jpeg: 'img',
          png: 'img',
          gif: 'img',
        }
        const fileType = typeObj[type] || ''
        const file = this.preData.file
        if (fileType == 'word') {
          const val = new Blob([file], { type: 'application/msword' })
          mammoth
            .convertToHtml({ arrayBuffer: val })
            .then((result) => {
              this.$refs.docPreview.innerHTML = result.value || ''
            })
            .done()
        }
        if (fileType == 'txt') {
          const val = new Blob([file], { type: 'text/plain' })
          const reader = new FileReader()
          const that = this
          reader.readAsText(val)
          reader.onload = function () {
            that.$refs.txtPreview.innerHTML = reader.result || ''
          }
        }
        if (fileType == 'pdf') {
          const val = new Blob([file], { type: 'application/pdf' })
          const url = window.URL.createObjectURL(val)
          this.pdfURL = url
        }
        if (fileType == 'img') {
          const val = new Blob([file], { type: 'image/jpeg' })
          this.newSrc = window.URL.createObjectURL(val)
          const that = this
          ImagePreview({
            // vant自带图片预览组件
            images: [that.newSrc],
            showIndex: false,
            onClose() {
              that.$router.go(-1)
            },
          })
        }
      },
      download() {
        // 下载文件
        const data = this.preData.file
        const url = window.URL.createObjectURL(data)
        const link = document.createElement('a')
        link.style.display = 'none'
        link.href = url
        link.setAttribute('download', this.preData.name)
        document.body.appendChild(link)
        link.click()
        document.body.removeChild(link)
      },
      blobToDataURI(blob, callback) {
        var reader = new FileReader()
        reader.readAsDataURL(blob)
        reader.onload = function (e) {
          callback(e.target.result)
        }
      },
    },
  }
</script>

<style lang="scss" scoped>
  .viewBox {
    margin-bottom: 1.34rem;
  }
  .txt-box {
    width: 100vw;
    height: 100vh;
  }
  .word-box {
    padding: 15px 15px 10px 15px;
    box-sizing: border-box;
    overflow: auto;
  }
</style>
```

## 更改 PDF 预览组件

重新封装 pdf 相关预览部分，改用 pdfjs-dist

### 安装 pfdjs

```bash
npm install pdfjs@2.2.228 --save
```

最好安装 2.2.228 版本，稍后在解释这个版本问题

### 组件编写

这里可以参考 pdfjs 的示例 [pdfjs 示例](https://gitcode.gitcode.host/docs-cn/pdf.js-docs-cn/examples/index.html)，下面是完整组件代码(Loading 组件可自己封装，不用可去除)

```html
<<template>
  <div>
    <Loading v-model="loading">加载中...</Loading>
    <div ref="pdfViewerContainer" class="pdfViewerContainer"></div>
  </div>
</template>

<script>
  import Loading from '@/components/common/Loading.vue'
  import * as PDFJS from 'pdfjs-dist'
  import pdfjsWorker from 'pdfjs-dist/build/pdf.worker.entry'

  PDFJS.GlobalWorkerOptions.workerSrc = pdfjsWorker
  export default {
    name: 'PdfViewer',
    components: { Loading },
    props: {
      /**
       * pdf地址
       */
      pdfUrl: {
        type: String,
        default: '',
      },
      /**
       * cMap的url地址(用于解决中文乱码或中文显示为空白的问题). 该资源的物理路径在: node_modules/pdfjs-dist/cmaps
       * 2.2.228版本可解决iphone14大文件显示不全问题
       */
      cMapUrl: {
        type: String,
        default: 'https://cdn.jsdelivr.net/npm/pdfjs-dist@2.2.228/cmaps/',
      },
      /**
       * pdf缩放比例
       */
      scale: {
        type: Number,
        default: 1,
      },
      /**
       * 携带的特定http请求头
       */
      httpHeaders: {
        type: Object,
        default: () => ({}),
      },
    },
    data() {
      return {
        pdfDocRef: null,
        loading: false,
      }
    },
    computed: {
      urlObj() {
        return { pdfUrl: this.pdfUrl, cMapUrl: this.cMapUrl }
      },
    },
    watch: {
      urlObj() {
        this.renderPdf()
      },
      scale() {
        this.renderPdf()
      },
    },
    mounted() {
      this.loading = true
      // 创建画布
      this.renderPdf()
      setTimeout(() => {
        console.log(document.querySelector('.pdfViewerContainer'), 'dom done')
        this.loading = false //渲染pdf时会影响这里异步代码执行，在这设置loading结束
      }, 200)
    },
    methods: {
      /**
       * 渲染pdf文件的指定页到画板
       * @param pdfViewerDom 承载pdf画板的dom容器
       * @param pdfDoc pdf文件
       * @param pageNum 需要渲染的页码
       * @param scale 缩放比例
       */
      renderPdfOnePage(pdfViewerDom, pdfDoc, pageNum, scale) {
        // 创建画布
        const canvas = document.createElement('canvas')
        pdfViewerDom.appendChild(canvas)
        // 获取2d上下文
        const context = canvas.getContext('2d')
        pdfDoc.getPage(pageNum).then((page) => {
          let viewport = page.getViewport({ scale: scale })
          let newScale = 375 / viewport.width //这里根据实际情况来，设计稿为宽375的iphone
          viewport = page.getViewport({ scale: newScale }) //按设备宽等比例缩放pdf文件
          const realCanvas = context.canvas
          let outputScale = window.devicePixelRatio || 1 //按像素缩放调节清晰度
          realCanvas.width = Math.floor(viewport.width * outputScale) //将pdf缩放到对应屏幕大小
          realCanvas.height = Math.floor(viewport.height * outputScale)
          realCanvas.style.width = '100%' //显示区域宽度撑满
          realCanvas.style.height = '100%' //显示区域高度撑满
          let transform =
            outputScale !== 1 ? [outputScale, 0, 0, outputScale, 0, 0] : null
          page.render({ canvasContext: context, viewport, transform })
        })
      },
      /**
       * 渲染pdf的画布
       * @param pdfViewerDom 承载pdf画布的dom容器
       * @param pdfDoc pdf文档
       * @param scale 缩放比例
       */
      renderPdfCanvas(pdfViewerDom, pdfDoc, scale) {
        // 清除原来的pdf画布
        pdfViewerDom.innerHTML = ''
        // 获取总页数
        const totalPage = pdfDoc.numPages
        // 获取显示容器
        for (let i = 1; i <= totalPage; i++) {
          // 循环处理pdf的每页
          this.renderPdfOnePage(pdfViewerDom, pdfDoc, i, scale)
        }
      },
      renderPdf() {
        const pdfViewerDom = this.$refs.pdfViewerContainer
        if (this.pdfUrl) {
          // 获取pdf文件
          const pdfLoadingTask = PDFJS.getDocument({
            url: this.pdfUrl,
            withCredentials: true, // 携带凭证
            httpHeaders: this.httpHeaders,
            cMapUrl: this.cMapUrl,
            cMapPacked: true,
          })
          pdfLoadingTask.promise.then((pdfDoc) => {
            if (pdfDoc && pdfViewerDom) {
              // 缓存pdf内容
              this.pdfDocRef = pdfDoc
              this.renderPdfCanvas(pdfViewerDom, pdfDoc, this.scale)
            }
          })
        }
      },
    },
  }
</script>

<style scoped></style>
```

> 开始使用的时候没有问题，但是 iphone14 会出现大文件显示不全问题，后来发现是 pdfjs 新版本对 iphone 兼容性不太好，这里需要使用 pdfjs@2.2.228 版本，这个版本相对比较稳定，目前多个机型暂未发现问题。

## 总结

iphone14 无法加载大文件需要更改 pdfjs 的 cmap 文件，这里采用的[cdn 引入](https://cdn.jsdelivr.net/npm/pdfjs-dist@2.2.228/cmaps/)的方式 ，或者直接使用 2.2.228 版本，可以解决乱码及空白页问题。这里还有个难点是根据 pdfjs 的实例，发现 pdf 文件很模糊，需要更改 canvas 的缩放，这里用到了 transform 属性，在组件中已经设置为根据设备实际像素调整，可以自行摸索。
