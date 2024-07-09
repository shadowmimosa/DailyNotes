<font size=4 face='楷体'>

## NextJS18+React 中 useEffect 执行两次的原因及解决方法

### 什么是 useEffect

useEffect 是 React Hooks 中的一个方法，它用于在函数式组件中执行 ui 以外的附加操作，例如从接口获取数据等，useEffect 可以在组件挂载、更新或卸载时执行。

### useEffect 触发两次的原因

```js
import { useEffect, useState } from 'react'
const Upload = (prop: { children: any }) => {
  useEffect(() => {
    console.log('test')
    return () => {}
  }, [])

  return <></>
}
```

测试发现创建默认工程上面代码会输出两次 test，究其原因是为了模拟立即卸载组件和重新挂载组件。帮助开发者提前发现重复挂载造成的 Bug，提供的调试机制。

简单说，development mode + strict mode，开发环境帮你对每个组件模拟执行了如下操作，挂载->卸载->挂载的操作，为了帮你测试卸载时是否清理了需要释放的资源，例如挂载时开启了一个定时器，卸载时候记得释放掉，否则会无限循环执行。

```js
useEffect(() => {
  const timer = setInterval(function () {
    console.log('test')
  }, 2000)
  return () => {
    clearInterval(timer)
  }
}, [])
```

### 暴力解决方法

如果是 React 项目，修改 index.tsx，去掉标签

```js
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)

// 改为

root.render(<App />)
```

如果 Nextjs 18 工程，修改 next.config.js 增加 reactStrictMode: false 配置项

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: false,
}

module.exports = nextConfig
```

### 更好的解决方法

更好的解决方法还是兼顾，挂载->卸载->挂载，useEffect 执行两次的方式去合理的初始化和释放资源，让一套代码兼容开发阶段的模拟模式和上线后的正式发布两种模式，适应 react 提供给你的这种完善的模拟调试模式。

## Reference

[NextJS18+React 中 useEffect 执行两次的原因及解决方法](https://zhuanlan.zhihu.com/p/663788000)

**2023.12.18**
