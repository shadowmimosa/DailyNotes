<font size=4 face='楷体'>

## 解决 vite 首次启动时，页面加载慢的问题

### 问题描述

当你首次启动 `vite` 时，Vite 会执行的所谓的[依赖预构建](https://vitejs.cn/guide/dep-pre-bundling.html)，每当打开新的页面，如果该页面使用到了新的依赖，界面就会被强制刷新一次，终端显示如下：

![image (18).png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28b979e314cd4e1fad74e9297afceaa5~tplv-k3u1fbpfcp-watermark.image?) 如果依赖越来越多，或者在特殊情况下，需要删除 node_modules 重新安装依赖启动页面时，这个情况会更明显，所谓的 vite 快，也就不以为然了，其实真是情况是：vite 启动项目要比 webpack 快，但是首次加载页面，并且依赖较多时，没有进行预构建就会比较慢。

> 页面的渲染时间和 webpack 项目的渲染时间差不多，esm 的形式被浏览器加载和请求数量对页面的渲染时间的影响不是主要的，也证实项目启动后浏览器第一次加载多出的时间主要是在编译上。

相关链接：[https://github.com/vitejs/vite/issues/1309](https://github.com/vitejs/vite/issues/1309)

打开新的页面时：加载新的模块会报 408，并触发页面刷新，element 相关依赖需要重新获取:

![image (19).png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c781b12a1e0461dad8c1298bf7db741~tplv-k3u1fbpfcp-watermark.image?)

![image (20).png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a571c5be53724bf3982c3da7aca05ec3~tplv-k3u1fbpfcp-watermark.image?)

vite 的快：命令行启动快，官网的说法是，vite 通过在一开始将应用中的模块区分为 依赖 和 源码 两类，改进了开发服务器启动时间，以 原生 ESM 方式提供源码，让浏览器接管了打包程序的部分工作，只需要在浏览器请求源码时进行转换并按需提供源码。而 webpack 需要在内存中编译、打包、压缩。

vite 的慢：需要一次性请求太多的资源，而且这些资源有些并不是浏览器可以直接运行的，vite 还需要动态的解析，然后一些需要打包再返回给浏览器。

vite 也提供了解决的方法，依赖预构建，使用自定义行为的配置项 optimizeDeps，

里面也提到了缓慢的[原因](https://vitejs.cn/guide/dep-pre-bundling.html)

### 解决方案 1：

配置 `vite`的`optimizeDeps`，将需要预构建的依赖配置进去

缺点：每次添加新的依赖都需要手动更新该配置

#### 最终解决方案：

使用`vite-plugin-optimize-persist` 插件自动配置，[https://www.npmjs.com/package/vite-plugin-optimize-persist](https://www.npmjs.com/package/vite-plugin-optimize-persist)

安装之后，`package.json`就会自动添加进预构建的依赖，如图：

![image (21).png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b64219dabe64937889fdc24c20a5a6a~tplv-k3u1fbpfcp-watermark.image?)

使用方法

```bash
npm i -D vite-plugin-optimize-persist vite-plugin-package-config
```

```js
// vite.config.tsimport OptimizationPersist from 'vite-plugin-optimize-persist'import PkgConfig from 'vite-plugin-package-config'
export default {
  plugins: [PkgConfig(), OptimizationPersist()],
}
```

配置完成之后，首次加载页面会快很多，因为已经预先构建了相关依赖，并且是存储在硬盘中的缓存

![image (22).png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13e8e95160c6476a8b0442a82b1e9120~tplv-k3u1fbpfcp-watermark.image?)

如果打开新的页面中，相关依赖已经加载过之后，只需请求页面中新的组件即可

![image (23).png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1b6d37cce804c8794474868aa4151b9~tplv-k3u1fbpfcp-watermark.image?)

### Reference

[解决 vite 首次启动时，页面加载慢的问题](https://frontend.devrank.cn/traffic-information/7259709767592118333)
[快速创建 vite+vue3+ts 项目及首次缓慢问题](https://zhuanlan.zhihu.com/p/475277841)

**2023.11.20**
