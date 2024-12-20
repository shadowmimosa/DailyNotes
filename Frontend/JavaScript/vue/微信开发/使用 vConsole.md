<font size=4 face='楷体'>

## Vue 微信调试

vConsole 是帮助在手机查看执行情况的微信调试插件
现在已经无法通过 x5 debug 打开
需要自行安装使用 [Github](https://github.com/Tencent/vConsole)

### 官方示例

- 安装
  ```bash
  $ npm install vconsole
  ```
- 使用

  ```javascript
  import VConsole from 'vconsole'

  const vConsole = new VConsole()
  // or init with options
  const vConsole = new VConsole({ theme: 'dark' })

  // call `console` methods as usual
  console.log('Hello world')

  // remove it when you finish debugging
  vConsole.destroy()
  ```

### Vue 使用

```javascript
import Vconsole from 'vconsole'

let vConsole = new Vconsole()

Vue.use(vConsole)
```

### Reference

[vue 使用 vConsole](https://blog.csdn.net/qq_41227106/article/details/125427283)
[Vue 项目中使用 vConsole 调试](https://www.cnblogs.com/sener/p/16525686.html)
[vue 中使用 vconsole(移动端调试)](https://zhuanlan.zhihu.com/p/358373930)

**2022.10.12**
