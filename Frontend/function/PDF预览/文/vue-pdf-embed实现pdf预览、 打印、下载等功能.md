---
created: 2024-09-24T16:45:56 (UTC +08:00)
tags: [vue-pdf-embed]
source: https://blog.csdn.net/weixin_51080551/article/details/140211314
author: 
---

# vue-pdf-embed实现pdf预览、 打印、下载等功能


## 一、前言        

在vue3中通过vue-pdf-embed实现pdf预览打印下载等功能，主要使用的第三方库**vue-pdf-embed** 该库同时也支持在vue2中使用，本文主要针对vue3项目中如何使用进行简单介绍。

ps:github地址：[Issue with long PDF + pagination · hrynko/vue-pdf-embed · Discussion #166 · GitHub](https://github.com/hrynko/vue-pdf-embed/discussions/166)

## 二、安装vue-pdf-embed

```bash
npm i vue-pdf-embed
yarn add vue-pdf-embed
```

### 1、全局引入

安装完成后在**main.js或main.ts**文件中 **引入vue-pdf-embed** 

```javascript
import { createApp } from 'vue'
import VuePdfEmbed from 'vue-pdf-embed'
 
import 'vue-pdf-embed/dist/style/index.css'
 
import 'vue-pdf-embed/dist/style/annotationLayer.css'
import 'vue-pdf-embed/dist/style/textLayer.css'
 
import App from './App.vue'
const app = createApp(App)
// 全局组件 由于我需要多次使用所有注册了全局组件方便使用
app.component('VuePdfEmbed', VuePdfEmbed)
app.mount('#app')
```

## 2.局部引入

```javascript
//在你要使用该功能的vue文件中直接引入
<script setup>
import VuePdfEmbed from 'vue-pdf-embed'
import 'vue-pdf-embed/dist/style/index.css'
import 'vue-pdf-embed/dist/style/annotationLayer.css'
import 'vue-pdf-embed/dist/style/textLayer.css'
</script>
```

## 三、使用vue-pdf-embed实现打印、下载等功能

### 示例demo1

```javascript
<template>
  <div class="pdf-content">
    <div class="pdf-button">
      <button @click="PDFPrint">打印</button>
      <button @click="PDFDownload">下载</button>
    </div>
    <div class="pdf">
      <VuePdfEmbed
        ref="vuePdfRef"
        height="800"
        annotation-layer
        text-layer
        :source="pdfSource"
      />
    </div>
  </div>
</template>
 
<script setup>
import { ref } from 'vue'
import VuePdfEmbed from 'vue-pdf-embed'
import 'vue-pdf-embed/dist/style/index.css'
import 'vue-pdf-embed/dist/style/annotationLayer.css'
import 'vue-pdf-embed/dist/style/textLayer.css'
//引入pdf
import pdfUrl from './240704.pdf'
const pdfSource = pdfUrl
 
const vuePdfRef = ref(null)
 
//打印
const PDFPrint = () => {
//打印分辨率默认 300  text1：文件名   allPages：是否打印所有页，默认值 false
  vuePdfRef.value?.print(200, 'text1', true)
}
//下载
const PDFDownload = () => {
  vuePdfRef.value?.download('text1')
}
</script>
 
<style lang="scss">
.pdf-content {
  width: 100%;
  height: calc(100vh - 20px);
  overflow: hidden;
  display: flex;
  .pdf-button {
    text-align: center;
    height: calc(100% - 10px);
    background-color: #999;
  }
  .pdf {
    width: 100%;
    height: calc(100% - 10px);
    overflow: auto;
    background-color: #ccc;
  }
}
//处理血染层cavers问题占位
.hiddenCanvasElement {
  display: none !important ;
}
</style>
```

###  示例demo2

分装成一个单独的组件放在components下使用

```javascript
// components/PdfPreviewer.vue文件
<template>
  <div class="pdf-content">
    <div v-if="showButtons" class="pdf-button">
      <button @click="PDFPrint">打印</button>
      <button @click="PDFDownload">下载</button>
    </div>
    <div class="pdf">
      <VuePdfEmbed
        ref="vuePdfRef"
        :height="height"
        :annotation-layer="annotationLayer"
        :text-layer="textLayer"
        :source="pdfSource"
      />
    </div>
  </div>
</template>
 
<script setup>
import { ref } from 'vue'
import VuePdfEmbed from 'vue-pdf-embed'
import 'vue-pdf-embed/dist/style/index.css'
import 'vue-pdf-embed/dist/style/annotationLayer.css'
import 'vue-pdf-embed/dist/style/textLayer.css'
 
const props = defineProps({
  pdfSource: {
    type: String,
    required: true
  },
  height: {
    type: Number,
    default: 800
  },
  annotationLayer: {
    type: Boolean,
    default: true
  },
  textLayer: {
    type: Boolean,
    default: true
  },
  showButtons: {
    type: Boolean,
    default: true
  }
})
 
const vuePdfRef = ref(null)
 
 
const PDFPrint = () => {
  console.log('打印pdf')
  vuePdfRef.value?.print(200, 'text1', true)
}
 
const PDFDownload = () => {
  vuePdfRef.value?.download('text1')
}
</script>
 
<style lang="scss">
//此处代码与上一个demo一样
</style>
```

如何引入组件使用如下：

```javascript
<template>
  <div>
    <PdfPreviewer :pdf-source="pdfSource" :height="800" show-buttons />
  </div>
</template>
 
<script setup>
import { onMounted, reactive, ref } from 'vue'
// 导入自己的文件
import pdfUrl from './240704.pdf'
import PdfPreviewer from './components/PdfPreviewer.vue'
const pdfSource = pdfUrl
</script>
 
<style lang="scss" scoped></style>
```


以上是一些pdf的基本的操作，后期将继续完善分装成一个完整的组件该组件还支持缩放、翻页等功能可以参考以下文档


[vue3中使用 vue-pdf-embed 实现pdf文件预览、翻页、下载等功能](https://blog.csdn.net/qq_45897239/article/details/136080318 "vue3中使用 vue-pdf-embed 实现pdf文件预览、翻页、下载等功能")
