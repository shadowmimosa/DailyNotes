<font size=4 face='楷体'>

## electron 隐藏

### 隐藏最大化 最小化按钮

```js
mainWindow = new BrowserWindow({
    height: 563,
    useContentSize: true,
    width: 1000,
    frame: false /*去掉顶部导航 去掉关闭按钮 最大化最小化按钮*/,
});
```

### 隐藏顶部菜单

```js
mainWindow.setMenu(null);
```

### Reference

[Electron-Vue 隐藏顶部菜单 隐藏关闭按钮、自定义关闭 最大化 最小化按钮](https://blog.csdn.net/huangxiaoguo1/article/details/107768915)

**2020.12.30**
