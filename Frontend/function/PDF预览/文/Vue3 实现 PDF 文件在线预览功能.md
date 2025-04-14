---
created: 2024-09-24T16:35:25 (UTC +08:00)
tags: [Vue.js,JavaScript]
source: https://juejin.cn/post/7105933034771185701
author: 一颗Potato
---

# Vue3 实现 PDF 文件在线预览功能

## 概述

之前我们用 `Reactjs + React-PDF` 实现了 **React** 版的 **PDF** 文件预览，今天我们用 `Vue3 + vue3-pdfjs` 实现 **Vue** 版本的 **PDF** 文件在线预览功能。

我们先来看看完成后效果

![](ddea22205dd6441a86b5405275791899_tplv-k3u1fbpfcp-zoom-in-crop-mark_1512_0_0_0.gif)

## 正文

### 创建 Vue3 项目

我们先创建一个的 `Vue3` 项目, 在终端中输入命令

```bash
pnpm create vite vue-pdf-preview
```

选择 `vue-ts` 回车，cd 进入项目根目录，执行 `pnpm install`, 等待项目依赖包安装完成。

项目依赖包安装完成后，我们来启动项目, 执行命令 `pnpm run dev` ,可以看到控制台输入出了如下内容

```bash
vite v2.9.9 dev server running at:

> Local: http://localhost:3000/
> Network: use `--host` to expose

ready in 780ms.

```

按住 **control/command + 鼠标左键**，项目在浏览器中打开了

项目启动成功

### 添加 **PDF** 预览插件

项目启动成功后，我们安装 **PDF** 预览插件

```bash
pnpm install vue-pdf-embed
pnpm install vue3-pdfjs
```

我们在 `src` 下新建一个文件 `src/components/pdfPreview.vue`，添加一些代码，初始化 `vue-pdf` 预览，代码如下

```html
<template>
    <div class="pdf-preview">
    
    </div>
</template>
<script setup lang="ts">
import { reactive, onMounted, computed } from "vue";

const props = defineProps({
    pdfUrl: {
        type: String,
        required: true
    }
})

onMounted(() => {

});

</script>
<style lang="css" scoped>
.pdf-preview {
    position: relative;
    height: 100vh;
    padding: 20px 0;
    box-sizing: border-box;
    background: rgb(66, 66, 66);
}

.vue-pdf-embed {
    text-align: center;
    width: 515px;
    border: 1px solid #e5e5e5;
    margin: 0 auto;
    box-sizing: border-box;
}

</style>
```

添加完成后，我们将 **PDF** 预览组件引入到 `App.vue` 文件中，并将提前准备的 **PDF** 文件也引入，如下所示，这里 **PDF** 文件也可以是线上地址

```html
<template>
<div>
    <PDFView :pdfUrl="jsPdf" />
</div>
</template>
<script setup lang="ts">
import PDFView from "./components/pdfPreview.vue"
import jsPdf from "./Javascript.pdf"
</script>
```

接下来我们回到刚刚新建的 **PDF** 预览组件页面，来完善预览功能

我们先引入 **PDF** 预览插件

```javascript
import VuePdfEmbed from "vue-pdf-embed";
import { createLoadingTask } from "vue3-pdfjs";
```

使用 **Vue3** 的 `reactive` 定义一些页数，页码，**PDF** 文件预览地址变量

```javascript
const state = reactive({
    source: props.pdfUrl, 预览pdf文件地址
    pageNum: 1, 当前页面
    scale: 1, // 缩放比例
    numPages: 0, // 总页数
});
```

在 `OnMounted` 钩子函数中使用**createLoadingTask** 获取下预览文件的总页数

```javascript
const loadingTask = createLoadingTask(state.source);
  loadingTask.promise.then((pdf:{numPages: number}) => {
      state.numPages = pdf.numPages;
  });
```

在 **template** 中加入预览插件代码

```html
 <div class="pdf-wrap">
     <vue-pdf-embed :source="state.source" :style="scale" class="vue-pdf-embed" :page="state.pageNum" />
</div>
```

打开浏览器，可以看到 **PDF** 文件已经加载出来了，但是样式不是很好看，我们下一步将样式优化下，并将 **PDF** 文件的翻页功能，缩放功能，当前页面/总页数展示功能添加完善

添加如下代码到 **template** 中

```html
<div class="page-tool">
    <div class="page-tool-item" >上一页</div>
    <div class="page-tool-item">下一页</div>
    <div class="page-tool-item">{{state.pageNum}}/{{state.numPages}}</div>
    <div class="page-tool-item" >放大</div>
    <div class="page-tool-item">缩小</div>
</div>
```

美化样式

```css

.pdf-preview {
    position: relative;
    height: 100vh;
    padding: 20px 0;
    box-sizing: border-box;
    background-color: e9e9e9;
}
.pdf-wrap{
    overflow-y:auto ;
}
.vue-pdf-embed {
    text-align: center;
    width: 515px;
    border: 1px solid #e5e5e5;
    margin: 0 auto;
    box-sizing: border-box;
}

.page-tool {
    position: absolute;
    bottom: 35px;
    padding-left: 15px;
    padding-right: 15px;
    display: flex;
    align-items: center;
    background: rgb(66, 66, 66);
    color: white;
    border-radius: 19px;
    z-index: 100;
    cursor: pointer;
    margin-left: 50%;
    transform: translateX(-50%);
}
.page-tool-item {
    padding: 8px 15px;
    padding-left: 10px;
    cursor: pointer;
}
```

添加文件的翻页功能，缩放功能，当前页面/总页数展示功能添加完善

```js
const scale = computed(() => `transform:scale(${state.scale})`)
function lastPage() {
    if (state.pageNum > 1) {
        state.pageNum -= 1;
    }
}
function nextPage() {
    if (state.pageNum < state.numPages) {
        state.pageNum += 1;
    }
}
function pageZoomOut() {
    if (state.scale < 2) {
        state.scale += 0.1;
    }
}
function pageZoomIn() {
    if (state.scale > 1) {
        state.scale -= 0.1;
    }
}
```

**tempalte**

```html
<div class="page-tool-item" @click="lastPage">上一页</div>
<div class="page-tool-item" @click="nextPage">下一页</div>
<div class="page-tool-item">{{state.pageNum}}/{{state.numPages}}</div>
<div class="page-tool-item" @click="pageZoomOut">放大</div>
<div class="page-tool-item" @click="pageZoomIn">缩小</div>
```

到这里，**Vue3** **PDF** 文件预览功能我们已经做完了
