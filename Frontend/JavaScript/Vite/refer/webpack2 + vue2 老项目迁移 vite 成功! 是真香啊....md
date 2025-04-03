---
created: 2023-11-20T15:57:46 (UTC +08:00)
tags: [vite]
source: https://zhuanlan.zhihu.com/p/471966642
author: 
---

# webpack2 + vue2 老项目迁移 vite 成功! 是真香啊... - 知乎

> ## Excerpt
> 起因是公司有个核心项目, 几乎贯穿了全部业务. 所以就算另起一个项目, 也有非常多的业务需要在此之上迭代. 这一个 近千页面的项目又是这么老的技术栈, 而且还是个多页面项目. 启动速度可想而知...每次开发. 光是项…

---
起因是公司有个核心项目, 几乎贯穿了全部业务. 所以就算另起一个项目, 也有非常多的业务需要在此之上迭代. 这一个**近千页面的项目又是这么老的技术栈**, 而且还是个多页面项目. 启动速度可想而知...每次开发. 光是项目启动都要等傻了, 无法忍受这种开发效率的我, 决定将其迁移至`Vite`

先跟大家说一下迁移成功后的效率变化:

原先, 单项目启动时长从 `265s` 降到了 `56s`. 热更新时长从 `38s` 降到了`几乎瞬时`.并且原先的`多页面开发模式`是通过启动多个`http-server`来实现的, 如果同时启动两个比较大的项目, 那基本会卡死. 但是在`vite`中就不再需要这种模式了. 因为我们完全可以配置多个入口, 也不怕会卡顿了.

## **介绍**

> 基于项目背景, 我本次重构的仅是开发环境构建逻辑. 也就是说生产环境打包, 仍采用的是`webpack`. 这么做主要原因: **是这个项目非常庞大, 对生产环境的逻辑进行重构的代价实在过大了.** 假设你希望整体大升级, 那最好要好好评估下风险.  

**为什么采用vite?**

-   性能上的原理就不详解了, 网上也有大把文章, 简单地概括就是"**按需加载**".  
    
-   开箱即用, 是的, 你甚至不用看文档就可以开造(我就是这样的)  
    
-   生态上, 主要是因为`Vite`会为`Vue`的技术栈提供**第一优先级**的更新, 我们在生态上会有很好的保障  
    
-   `vite`与`rollup`的插件开发更加友好, 遇到生态没法解决的问题, 你可以自己动手写一个插件去resolve  
    

**一定是Vite吗?**

-   当然不是的, 最近随着 `WebAssembly` 这个概念的兴起, 其实`Webpack5`在性能上也有一些质的飞跃, 推荐你也去了解一下这个概念.

## **迁移过程**

> 如果你的项目足够庞大, 我相信你会在这一路踩坑中抓耳挠腮. 不过当看到项目正常启动的时候, 还是成就感满满的.  

直接对着项目:

然后配置`vite.config.js`文件

```
import { defineConfig } from 'vite'
import { createVuePlugin } from 'vite-plugin-vue2'

export default defineConfig({
        plugins: [
            createVuePlugin({
                jsx: true, // jsx语法兼容处理, 实际上并没有用...后面我会说的
            })
        ]
})
```

`package.json`文件

```
{
    "scripts": {
        "vite": "vite"
    }
}
```

直接跑起来, **恭喜你会收获一大堆抛错.**

## **错误记录**

> 这里我只贴出了几个比较坑的错, 一些很容易解决的我就不贴出啦, 网上也有很多解决方案  

### **导入模块的无法解析文件夹下的index.js**

不仅如这个标题, 我转到vite的时候, 会有以下三种情况无法识别

```
case1: src/demo1/index.vue
case2: src/demo2/index.js
case3: src/demo3.vue

// ❌ in vite ,  in webpack
import demo1 from 'src/demo1'
import demo2 from 'src/demo2'
import demo3 from 'src/demo3'
```

也就是说, vite会找不到文件夹内的`index.js`, `index.vue`以及你在webpack默认省略拓展名`.vue`, 也会导致找不到文件. 如果你涉及的文件特别少, 也可以手动自己加上, 但是多的话就很难解决了

在这里我自己写了一个插件解决这几种情况. 你也可以直接使用我的插件**[vite-plugin-path-resolve](https://link.zhihu.com/?target=https%3A//www.npmjs.com/package/vite-plugin-path-resolve)**

```
// vite.config.js
import pathResolve from 'vite-plugin-path-resolve'
function getPath(dir) {
    return path.resolve(path.dirname(fileURLToPath(import.meta.url)), dir)
}

export default defineConfig({
    plugins: [
        pathResolve({ src: getPath('src') }),
    ]
})
```

### **Vue2中使用了 JSX的问题**

> The JSX syntax extension is not currently enabled

![](https://pic1.zhimg.com/v2-fa753b990e3bd06539fb6ef028c43e38_b.jpg)

vue2组件的script模块中, 如果你使用了jsx语法, vite是无法辨别出来的. 目前我查到的有以下几种解决办法:

目前该抛错以下的解决办法:

-   vite配置文件加上该plugin(对我无用)

```
vite.config.js => plugins: [createVuePlugin({ jsx: true })]
```

-   如果是在`js`文件中带有`jsx`语法, 则将改为`.jsx`扩展名文件

-   如果是在`.vue`文件中带有jsx语法, 则在`script`标签下增加该标识

```
.vue(has jsx) => <script lang="jsx">
```

以上几种解决办法对我来说都有用, **但是我有成百上千个文件呢...**, 总不能可能一个一个改吧. 我个人去搜索了网上是有开发好的插件, 但是在我的项目都不适用. 为此我自己写了个脚本, 实际的去帮我给这些带有`jsx`语法的 `.vue`文件, 自动加上标签.**npm搜索:** **[vite-vue2-script-jsx](https://link.zhihu.com/?target=https%3A//www.npmjs.com/package/vite-vue2-script-jsx)**

### **element找不到依赖模块: `async-validator`**

> ERROR: \[plugin: vite:dep-pre-bundle\] Failed to resolve entry for package "async-validator". The package may have incorrect main/module/exports specified in its package.json: Failed to resolve entry for package "async-validator". The package may have incorrect main/module/exports specified in its package.json. 遇到这种模块内, 找不到引用模块的, 都可以用路径别名来解决.  

```
// vite.config.js
alias: [
  { find: 'async-validator', replacement: 'node_modules/async-validator/dist-web/index.js' },
],
```

### **less的问题**

![](https://pic2.zhimg.com/v2-36ba664183a2fd1b8a5525757cd9b0c5_b.jpg)

这个问题主要是因为一些`less`的全局模块无法找到.在`vite.config.js`下配置:

```
css: {
        preprocessorOptions: {
            less: { additionalData: `@import "${getPath('src')}/assets/less/theme.less";` },
        }
    }
```

___

> **\[vite\]** Internal server error: '~@/assets/less/global.less' wasn't found. Tried - /Users/xxxx/xx-project/boss-admin/src/project/system/~@/assets/less/global.less,node\_modules/~@/assets/less/global.less,~@/assets/less/global.less

这个问题简单, 把~@改成@就可以了

### **commonjs导入报错**

> **\[vite\]** Internal server error: Failed to resolve import "vertx" from "node\_modules/.vite/es6-promise.js?v=7253cf1d". Does the file exist? 使用插件的时候抛的错,  

```
import { viteCommonjs } from '@originjs/vite-plugin-commonjs'
```

-   顺便提一下这个插件使用来解决代码中使用了`commonJs`, 但`vite`不支持的问题. 这个很好解决, 我就不提了

在该插件的配置加入一个`skipPreBuild`即可

```
plugins: [
    // 这个 plugin 是自定义的, 解决路径问题
    viteCommonjs({ skipPreBuild: true }),
],
```

### **最坑的错误**

> **\[vite\]** Internal server error: CssSyntaxError: /Users/xxxx/xxxx-project/xxxx-admin/src/project/system/components/channel-select/index.vue?vue&type=style&index=0&rel=stylesheet%2Fless&lang.less:1:0: Unknown word  

![](https://pic1.zhimg.com/v2-01659c2c01b7a6b111c5a525d4e6671c_b.png)

这个bug是我最匪夷所思的, 因为他的报错非常的诡异, 我调试源码, 甚至去官方提了 `issue`,都没解决问题, 最后发现是因为我延后了`vite-plugin-vue2`的执行, 当时是因为想解决jsx语法的问题, 最终抛弃了那个方案

```
plugins: [
    {
        enforce: 'pre', // dont do that
        ...createVuePlugin({
            jsx: true,
        }),
    }
],
```

### **全局注册的UI组件库失效**

> 这个报错就是原本项目全局导入的ElementUI组件库, 在组件文件内却提示组件未注册? 后面我是用了一个大佬的插件解决的, 让ElementUI自动按需导入  

```
import OptimizationPersist from 'vite-plugin-optimize-persist'
import PkgConfig from 'vite-plugin-package-config'

Components({
  resolvers: [ElementUiResolver()],
  include: [/\.vue$/, /\.vue\?vue/, /\.md$/],
}),
```

### **Failed to load source map for /node\_modules/.vite/vite.js**

![](https://pic4.zhimg.com/v2-c522d558141bcd90be7517c7eb409b17_b.jpg)

项目启动后一直放这个警告, 导致卡顿. 这个问题我还没有搞清楚是为什么, 但是找到了解决办法, 告诉`Vite`哪些包应该被预先加载.这里可以使用这个插件解决这个问题.

```
import OptimizationPersist from 'vite-plugin-optimize-persist'

plugins: [
    OptimizationPersist(),
],
```

### **Uncaught ReferenceError: parcelRequire is not defined**

![](https://pic2.zhimg.com/v2-b66b1e449b7aca68cfacbcc137b15ca9_b.png)

我的办法是直接在 `window` 对象下添加一个`parcelRequire` 属性

## **vite.config.js**

> 最后贴一个我的全部配置图, 方便你参考  

```
import path from 'path'
import { fileURLToPath } from 'url'
import { defineConfig } from 'vite'
import { viteCommonjs } from '@originjs/vite-plugin-commonjs'
import { createVuePlugin } from 'vite-plugin-vue2'
import Inspect from 'vite-plugin-inspect'
import aliasDefualt from './vite-script/plugins/vite-plugin-alias-defualt.js'
import Components from 'unplugin-vue-components/vite'
import { ElementUiResolver } from 'unplugin-vue-components/resolvers'
import OptimizationPersist from 'vite-plugin-optimize-persist'
import PkgConfig from 'vite-plugin-package-config'
// 多页面入口
import projects from './vite-script/options/project-input'
// 项目的代理文件
import proxies from './vite-script/options/proxy'

function getPath(dir) {
    return path.resolve(path.dirname(fileURLToPath(import.meta.url)), dir)
}

const projectPath = (projectName) => getPath(`src/project/${projectName}`)

export default defineConfig({
    build: {
        rollupOptions: {
            input: projects,
        },
    },
    plugins: [
        // 这两个包主要是解决 依赖按需加载的问题.
        PkgConfig(),
        OptimizationPersist(),
        // 这个 plugin 是自定义的, 解决路径问题
        aliasDefualt({ src: getPath('src') }),
        createVuePlugin({
            jsx: true,
        }),
        // UI框架的自动按需导入
        Components({
            resolvers: [ElementUiResolver()],
            include: [/\.vue$/, /\.vue\?vue/, /\.md$/],
        }),
        // common transform to ES6 Module
        viteCommonjs({ skipPreBuild: true }),
        Inspect(),
    ],
    resolve: {
        alias: [
            { find: '@', replacement: getPath('src') },
            /** 解决element-ui 内部找不到 async-validator 模块的问题*/
            { find: 'async-validator', replacement: 'node_modules/async-validator/dist-web/index.js' },
            { find: 'v-viewer', replacement: 'node_modules/v-viewer' },
        ],
    },
    server: {
        open: '/index.html',
        proxy: {
            ...proxies,
            '/web-socket': {
                target: 'https://dev.www.xxx.com.cn',
                secure: false,
                changeOrigin: true,
                ws: true,
            },
        },
    },
    css: {
        preprocessorOptions: {
            less: { additionalData: `@import "${getPath('src')}/assets/less/theme.less";` },
        },
    },
    define: {
        global: {},
    },
})

```

## **感谢**

___

如果觉得文章内容对你有帮助:

-   ❤️欢迎关注点赞哦! 我会尽最大努力产出高质量的文章
