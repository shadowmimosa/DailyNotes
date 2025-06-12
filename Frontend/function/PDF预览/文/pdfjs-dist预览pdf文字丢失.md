---
created: 2024-09-24T17:02:31 (UTC +08:00)
tags: [warning: error during font loading: the cmap "baseurl" parameter must be spe]
source: https://blog.csdn.net/gentleman_hua/article/details/126579762
author: 
---

# pdfjs-dist 预览 pdf 文字丢失

> Vue3 环境不支持 vue-pdf 插件使用，使用 pdfjs-dist

> pdf-dist 版本 `npm install pdfjs-dist@2.5.207 -S`

## 控制台报错 缺少字体包

`Warning: Error during font loading: The CMap "baseUrl" parameter must be specified, ensure that the "cMapUrl" and "cMapPacked" API parameters are provided.`

## 页面丢失效果

![Alt text](image-1.png)

## 寻找报错路径

控制台报错 CMap 的 baseUrl 参数地址和 cMapPacked 压缩未被指定  
![Alt text](image-2.png)

## 找到 pdfjs 源码

## 解决方法 `加载线上地址文件字体`

## 找到 pdfjs 依赖路径

`node_modules > pdfjs-dist>build>pdf.js`

## 在 1834 行指定 cMapUrl 添加两行

```javascript
params.rangeChunkSize = params.rangeChunkSize || DEFAULT_RANGE_CHUNK_SIZE
params.CMapReaderFactory =
  params.CMapReaderFactory || _display_utils.DOMCMapReaderFactory
params.ignoreErrors = params.stopAtErrors !== true
params.fontExtraProperties = params.fontExtraProperties === true
params.pdfBug = params.pdfBug === true

//解决文字缺少问题
params.cMapPacked = true
params.cMapUrl = 'https://cdn.jsdelivr.net/npm/pdfjs-dist@2.2.228/cmaps/'
```

###### 重新加载项目 问题解决

![Alt text](image-3.png)
