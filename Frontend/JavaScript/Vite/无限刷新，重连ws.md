<font size=4 face='楷体'>

## Vite 无限刷新 重连 ws

vite 开发微信应用，因为微信无法在本地调试，所以用了内网穿透工具穿透到本地的开发环境
连了之后在首页获取 code 的时候，一直在重启项目

```js
# vite.config.js
server: {
  hmr: {
    protocol: "ws",
    host: "127.0.0.1",
  },}
```

### Reference

[vite 项目一直在无限刷新，重连 ws](https://blog.csdn.net/kabudada/article/details/127747316)

**2023.11.20**
