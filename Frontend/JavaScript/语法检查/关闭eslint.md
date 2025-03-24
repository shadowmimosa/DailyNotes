<font size=4 face='楷体'>

## 关闭 ESLint 警告

默认情况下, ESLint 和 vscode 格式化工具有冲突, 需要添加配置文件解决冲突

- 在项目根目录添加配置文件
  webpack 项目生成 .eslintrc.js 规定需要单引号替换双引号并且文件末尾不能加分号
  需要在跟目录下创建 .prettierrc 文件 并且添加

  ```json
  // .prettierrc
  {
    "semi": false,
    "singleQuote": true
  }
  ```

```javascript
// .eslintrc.js
// 禁用对 space-before-function-paren 的检查
rules: {
'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
'space-before-function-paren' : 0
},
```

- 将以下三项设置为 false
  ```javascript
  // vue.config.js
    overlay: {
      warnings: false,
      errors: false,
    },
  lintOnSave: false,
  ```

### Reference

[关闭 ESLint 警告](https://www.cnblogs.com/huoshengmiao/p/14601566.html)
[vscode中ESLINT和Prettier插件搭配](https://www.cnblogs.com/Jimferen/p/14311304.html)

**2022.08.18**
