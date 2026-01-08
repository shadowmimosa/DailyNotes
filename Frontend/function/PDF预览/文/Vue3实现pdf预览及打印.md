---
created: 2024-09-24T16:55:13 (UTC +08:00)
tags: [Vue.js, 前端]
source: https://juejin.cn/post/7340107906405613618
author: 南玖
---

# Vue3 实现 pdf 预览及打印

## Vue3 实现 pdf 预览及打印

在一些后台管理中,  经常会看到 pdf 的打印预览, 比如流程的审批, 规章制度或者财务系统的发票等等, 都要涉及到 pdf 的打印及其预览

现在基本搭建的项目都是基于 Vue3, 所以, 我们今天就使用 Vue3 来实现一下我们 pdf 的预览及其打印, 也将最终的代码上传到 gitee 仓库了, 放在文章的最下面了

在之前, 我写过一篇 Vue2 对于文件的打印预览, 借助的是 vue-office 插件, 大家可以点击以下链接进行阅读

[借助 vue-office 实现 word 文件预览](https://mp.weixin.qq.com/s?__biz=Mzg5MTU1NDg1OQ==&mid=2247487486&idx=1&sn=8bbb595d4ea7ea48a56877497fa49ade)

我们先来创建一个 Vue3 的项目

现在, 我们的 pdf 预览及其打印, 将其封装出来, 在 App.vue 文件进行引入

大家可以搜索下方链接查看该插件

> [vue-pdf-embed](https://github.com/hrynko/vue-pdf-embed)

项目创建完毕, 我们需要安装一下依赖

```bash
npm install vue-pdf-embed
```

我们创建一个组件
在 index.vue 组件中我们接收一个 pdf
现在, 我们对功能进行分析, 我们需要将 pdf 在页面中显示,  而且如果页数过多, 我们还需要点击翻页,  甚至可以放大缩小,  打印或者下载
确认功能之后, 我们先将最基本的 HTML 页面写出来,  现在先将 pdf 预览出来, 我们再对其功能一步一步实现
将准备好的 pdf 传递过去, 现在, 我们只需要在组件中进行编写就 OK 了

```javascript
import VuePdfEmbed from 'vue-pdf-embed'
```

将预览插件引入进来之后, 我们在页面中进行使用, 使用之前, 我们需要定义几个数据

```javascript
import { reactive } from 'vue'
const state = reactive({
  source: props.pdfUrl, // 预览pdf文件地址
  pageNum: 1, // 当前页面
  scale: 1, // 缩放比例
  numPages: 0, // 总页数
})
```

这里, 我添加了 loading 效果, 因为 pdf 的加载, 需要一定的时间
这个 loading 效果, 我是这么做的, 如果加上 element-plus 的 loading 效果会好看一些, 我只是添加了文字展示

```javascript
import { ref, watchEffect } from 'vue'
const loading = ref(true)
watchEffect(() => {
  if (state.numPages > 0) {
    loading.value = true
  }
})
```

因为, 我们的总页面肯定不会是 0, 所以, 我才这么显示, 大家也可以在加载完 pdf 之后, 再将其值改为 true, 这也是可以的

接下来需要做的就是获取 pdf 的总页码
就是在预览组件中, 绑定 loaded 方法

在该方法中, 可以接收一个值, 我们在其值中就可以获取页码了

现在,  我们的页面就可以正常显示了

我们先实现一下上一页和下一页这个功能

```html
# html
<div class="page-tool-item" @click="lastPage">上一页</div>
<div class="page-tool-item" @click="nextPage">下一页</div>
```

```javascript
# js
function lastPage() {
if (state.pageNum > 1) {
    state.pageNum -= 1;
}}
function nextPage() {
if (state.pageNum < state.numPages) {
    state.pageNum += 1;
}}
```

我们发现上一页下一页没有问题, 接下来, 我们实现一下方法和缩小

```html
# html
<div class="page-tool-item" @click="pageZoomOut">放大</div>
<div class="page-tool-item" @click="pageZoomIn">缩小</div>
```

```javascript
# js
function pageZoomOut() {
if (state.scale < 2) {
    state.scale += 0.1;
}}
function pageZoomIn() {
if (state.scale > 1) {
    state.scale -= 0.1;
}}

```

我们自定义样式, 传递给预览组件,  这里使用计算属性最好不过, 因为需要依赖数据进行计算

```javascript
import { computed } from 'vue'
const scale = computed(() => `transform:scale(${state.scale})`)
```

现在, 我们的放大缩小也没有问题了
我们来实现一下打印功能, 需要创建一个模版 ref

```html
# html
<div class="page-tool-item" @click="printPdf">打印</div>
```

```javascript
# js
// 打印
const pdfRef = ref();
const printPdf = () => {  pdfRef.value.print(100, "test", true)}

```

我们发现,  打印功能也可以正常实现

就差最后的下载了, 文档也提供了下载方法

```html
# html
<div class="page-tool-item" @click="downloadPdf">下载</div>
```

```javascript
# js
const downloadPdf = () => {  pdfRef.value.download("test.pdf");}

```

我们发现下载功能也可以正常下载

这样我们的整体功能就实现啦
