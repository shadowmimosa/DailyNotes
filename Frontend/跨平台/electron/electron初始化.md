<font size=4 face='楷体'>

## electron 初始化功能

### 隐藏最大化 最小化按钮

```js
mainWindow = new BrowserWindow({
  height: 563,
  useContentSize: true,
  width: 1000,
  frame: false /*去掉顶部导航 去掉关闭按钮 最大化最小化按钮*/,
})
```

### 在任务栏隐藏

```javascript
mainWindow = new BrowserWindow({
  //...
  skipTaskbar: true,
})
```

### 隐藏顶部菜单

```js
mainWindow.setMenu(null)
```

或者

```javascript
const electron = require('electron')

const Menu = electron.Menu
Menu.setApplicationMenu(null) // 隐藏菜单栏
```

### 禁止调整窗口大小

```javascript
win = new BrowserWindow({
  width: 800,
  height: 600,
  frame: false, // 为了兼容 可选则加上无边框
  resizable: false, // 禁止调整大小
})
```

### 可显示内容区域

```javascript
win = new BrowserWindow({
  useContentSize: false,
})
```

- useContentSize 为 false 时, 整个 window 窗体宽度是参数 width 和 height 的值
- useContentSize 为 true 时, window 窗体可显示内容区域(排除边框 title，因为不能显示内容) 的宽高是参数 width 和 height 值

### Reference

[Electron-Vue 隐藏顶部菜单 隐藏关闭按钮、自定义关闭 最大化 最小化按钮](https://blog.csdn.net/huangxiaoguo1/article/details/107768915)
[如何隐藏 electron 窗体的菜单栏](https://www.jianshu.com/p/3f19a70ed49d)
[electron-builder 踩坑系列---禁止用户调整窗口大小](https://zhuanlan.zhihu.com/p/263005409)
[electron useContentSize 的详解](https://www.cnblogs.com/del88/p/13744399.html)

**2022.08.17**
