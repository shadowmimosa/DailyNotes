---
created: 2024-09-24T17:09:22 (UTC +08:00)
tags: [vue, 工具方法]
source: https://www.cnblogs.com/shyhuahua/p/18331635
author: 行走的蒲公英

  粉丝 - 5
  关注 - 1
---

# vue-pdf-embed 预览和下载、解决文字丢失问题

## 1\. 实现效果：

文件列表点击 pdf 文档可预览，含多页，带下载按钮

##  2.  用的 vue3 + vue-pdf-embed

版本号可用 1.x 或 2.x : 这里我用的 1.2.1 版本：

```
// 安装：
npm i vue-pdf-embed@1.2.1
```

**vue-pdf-embed 官方文档：**

- 2.0.0 版本 ： https://www.npmjs.com/package/vue-pdf-embed/v/2.0.0

- 1.2.1 版本 : https://www.npmjs.com/package/vue-pdf-embed/v/1.2.1?activeTab=readme

## 3\. 具体代码

- hmtl 部分

```html
<div @click="handleViewPdf">
  <div class="pdfNameBox" title="点击预览">点击文件名</div>
</div>

<!-- pdf预览 -->
<el-dialog v-model="pdfOpen" title="'pdf预览'" width="80%" append-to-body>
  <div
    v-loading="isLoading"
    style="min-height: 439px"
    element-loading-text="加载中..."
  >
    <vue-pdf-embed
      ref="pdfRef"
      v-if="!pdfFail"
      :source="pdfSrc"
      @rendered="handleDocumentRender"
      @loading-failed="handlePdfFaid"
    />
  </div>

  <a :href="pdfSource" :download="下载文件名" class="loadPdf" target="_blank">
    <el-button type="primary" icon="Download" plain>下载</el-button>
  </a>

  <template #footer>
    <el-button @click="pdfOpen = false" type="primary">关 闭</el-button>
  </template>
</el-dialog>
```

- 方法：

```javascript
const pdfOpen = ref(false)
const isLoading = ref(true)
const pdfSrc = ref('')
const pdfFail = ref(false)

// 调试文档用
const pdfSource = ref(
  'https://raw.githubusercontent.com/mozilla/pdf.js/ba2edeae/web/compressed.tracemonkey-pldi-09.pdf'
)
// pdf加载
function handleDocumentRender(val) {
  isLoading.value = false
  pdfFail.value = false
}
// pdf加载失败，或者404
function handlePdfFaid(val) {
  isLoading.value = false
  pdfFail.value = true
  console.log('文档加载失败')
}
// 点击 预览
function handleViewPdf(file) {
  isLoading.value = true
  pdfOpen.value = true
  pdfSrc.value = pdfSource.value
  pdfFail.value = false
}
```

- 样式：

```html
// 下载按钮 .loadPdf { position: absolute; top: 6px; right: 50px; }
```

##  4. 文字丢失的问题

偶然上传了发票 pdf，预览发现文字丢失。如图

![Alt text](image-4.png)

确认是找不到对应字体了。修改如下：需要加上 cMapUrl  和 cMapPacked: true，

```html
<vue-pdf-embed
  v-if="!pdfFail"
  :source="{ url: getBowserUrl(props.pdfRowData.filePath), cMapUrl: 'https://cdn.jsdelivr.net/npm/pdfjs-dist@2.9.359/cmaps/', cMapPacked: true }"
  @rendered="handleDocumentRender"
  @loading-failed="handlePdfFaid"
/>
```

其中 cMapUrl: 'https://cdn.jsdelivr.net/npm/pdfjs-dist@2.9.359/cmaps/' 需要找到"vue-pdf-embed": "1.2.1" 依赖包 pdfjs-dist 的版本号，如 2.9.359 版本。

附上官方解释：https://github.com/hrynko/vue-pdf-embed/tree/v1

![Alt text](image-5.png)

验证后已解决文字不显示的问题。
