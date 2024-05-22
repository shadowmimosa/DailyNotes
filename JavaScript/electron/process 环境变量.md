<font size=4 face='楷体'>

## Electron 中 process 读取系统环境变量的问题

若在渲染进程中直接使用

```javascript
process.env.[SystemVariableName]
```

eg.

```javascript
console.log(process.env.Path)
```

其返回值为

```javascript
undefined
```

上述代码中的 process 来自于 electron 当中预定义的 process, 其导出内容仅为在程序中预定的内容
因此需要在渲染进程中显示引入 process 后进行调用, 即可获取包含 `VUE_APP_` 开头的自定义环境变量以及系统环境变量

正确调用方式应当先显示引入后再进行系统环境变量的调用:

```javascript
import * as process from 'process'
// import process from 'process'
console.log(process.env.Path)
```

### Reference

[Electron13 + Vue3 中 process 读取系统环境变量的问题](https://zhuanlan.zhihu.com/p/418035549)

**2022.05.10**
