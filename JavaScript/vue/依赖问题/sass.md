<font size=4 face='楷体'>

## SASS 依赖问题

今天在写 Vue 页面的时候，根据教程，我要安装 sass-loader 与 node-sass，但是在安装完成后运行项目的时候，报出如下错误：

> Node Sass version 7.0.0 is incompatible with ^4.0.0 || ^5.0.0 || ^6.0.0

### 替代方案

不要再使用`node-sass`了，要用`sass`替代它。

如果你想在你的应用中使用 scss 或者 sass，需要这样做：

- 首先卸载原来安装的`node-sass`

```bash
yarn remove node-sass
```

如果使用的是 npm，则

```bash
npm uninstall node-sass
```

- 然后安装`sass`，而不要安装`node-sass`

```bash
yarn add -D sass
```

或者

```bash
npm i -D sass
```

然后你的 scss/sass 的文件就会被正确地 compiled 了

> Syntax Error: TypeError: this.getOptions is not a function

### 降低版本

vue3 使用 scss 只用安装两个包就行

```bash
npm install sass --save
```

这个问题是 sass-loader 版本太高
修改配置

```json
// package.json
sass-loader: "^10.1.0",
```

然后执行 `npm install`
和 `npm install sass-loader@^10.1.0 --save` 效果一样

> TypeError: this.getOptions is not a function

[这里](https://github.com/webpack-contrib/sass-loader/releases/tag/v11.0.0)指出 `sass-loader@11.0.0` 版本需要 `webpack@5.0.0`
而 `@vue/cli@4.5.0` 所用的是 `webpack@4` 所以需要将 sass-loader 的版本降到 11 以下

```bash
yarn remove sass-loader
yarn add sass-loader@10.1.1
```

### Reference

[Node Sass version 7.0.0 is incompatible with ^4.0.0 || ^5.0.0 || ^6.0.0 报错解决方案](https://blog.csdn.net/weixin_44421143/article/details/122243061)
[关于 vue3 使用 scss 出现 Syntax Error: TypeError: this.getOptions is not a function](https://blog.csdn.net/nithumahel/article/details/120734891)
[解决TypeError: this.getOptions is not a function](https://www.jianshu.com/p/ed3d7409e974)

**2022.08.18**
