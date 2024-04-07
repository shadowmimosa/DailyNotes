<font size=4 face='楷体'>

## Electron 中使用 Vue-devtools

### 使用 [electron-devtools-installer](https://github.com/MarshallOfSound/electron-devtools-installer) 工具

- 声明

```javascript
const {
  default: installExtension,
  VUEJS_DEVTOOLS,
} = require('electron-devtools-installer')
```

- 安装

```javascript
// 在ready事件发出之后调用
installExtension(VUEJS_DEVTOOLS)
  .then((name) => console.log(`Added Extension:  ${name}`))
  .catch((err) => console.log('An error occurred: ', err))
```

### Reference

[在 electron 中使用 vue-devtools](https://www.jianshu.com/p/cfcfca4d8556)

**2022.08.17**
