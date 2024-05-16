<font size=4 face='楷体'>

## electron-store 使用

### 介绍

[Github](https://github.com/sindresorhus/electron-store)

- 以文件形式缓存数据，保存 Electron 应用程序或模块的简单数据持久性-保存和加载用户首选项，应用程序状态，缓存等
- 数据保存在 `app.getPath('userData')` 中的 JSON 文件中。您可以在主进程和渲染器进程中直接使用此模块。

> app.getPath(name)-储存你应用程序设置文件的文件夹，默认是 appData 文件夹附加应用的名称。
> appData: 当前用户的应用数据文件夹，默认对应：
> %APPDATA% Windows 中  
> $XDG_CONFIG_HOME or ~/.config Linux 中  
> ~/Library/Application Support macOS 中

## 安装

```bash
npm install electron-store
```

## 使用

```javascript
const Store = require('electron-store')

let option = {
  name: 'config', //文件名称, 默认 config
  fileExtension: 'json', // 文件后缀, 默认json
  cwd: app.getPath('userData'), // 文件位置, 尽量不要动， 默认情况下，它将通过遵循系统约定来选择最佳位置C:\Users\xxx\AppData\Roaming\test\config.json
  encryptionKey: 'aes-256-cbc', // 对配置文件进行加密
  clearInvalidConfig: true, // 发生 SyntaxError  则清空配置
}
const store = new Store(option)

// 一般直接简化为
const Store = require('electron-store')

const store = new Store()
```

### 方法

```javascript
store.set(key, value)
store.set(object)
store.get(key, [defaultValue]) // 获取一个数据或 defaultValue（如果该数据不存在）
store.reset(keys) // 将项目重置为其默认值
store.has(key)
store.delete(key)
store.clear()
store.size
store.path // 获取存储文件的路径
```

### 示例：

```javascript
store.set('unicorn', '这是需要存储的内容')
console.log(store.get('unicorn')) //=> '这是需要存储的内容'

// 使用点表示法访问嵌套属性
store.set('foo.bar', true)
console.log(store.get('foo')) //=> {bar: true}

// 嵌套存储
store.set({
  foo: {
    bar: {
      foobar: 'hahaha',
    },
  },
})
console.log(store.get('foo.bar.foobar'))

store.delete('unicorn')
console.log(store.get('unicorn')) //=> undefined
```

### 为什么不使用 window.localStorage

- localStorage 仅在浏览器进程（渲染进程）中起作用
- localStorage 的容错性不是很高，因此，如果您的应用遇到错误并意外退出，则可能会丢失数据
- localStorage 仅支持持久字符串。 此模块支持任何 JSON 支持的类型
- localStorage 不是很安全，可能是由于 xss 攻击而泄漏信息
- electron-store 模块的 API 更好。 您可以设置并获取嵌套属性。 您可以设置默认的初始配置

### 各存储区别

- vuex 存储在内存
- localstorage 则以文件的方式存储在本地
- electron-store 数据存储卸载应用之后依然存在

## Reference

[electron-store 的了解使用](https://blog.csdn.net/qq_44041514/article/details/119570453)
[Electron 存储简单数据和用户首选项推荐用 electron-store](https://xushanxiang.com/2019/12/electron-store.html)

**2022.07.06**
