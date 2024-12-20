<font size=4 face='楷体'>

## [\#][link 1]全局 CLI 配置

有些针对 `@vue/cli` 的全局配置，例如你惯用的包管理器和你本地保存的 preset，都保存在 home 目录下一个名叫 `.vuerc` 的 JSON 文件。你可以用编辑器直接编辑这个文件来更改已保存的选项。

你也可以使用 `vue config` 命令来审查或修改全局的 CLI 配置。

## [\#][link 2]目标浏览器

请查阅指南中的[浏览器兼容性][link 3]章节。

## [\#][link 4]vue.config.js

`vue.config.js` 是一个可选的配置文件，如果项目的 (和 `package.json` 同级的) 根目录中存在这个文件，那么它会被 `@vue/cli-service` 自动加载。你也可以使用 `package.json` 中的 `vue` 字段，但是注意这种写法需要你严格遵照 JSON 的格式来写。

这个文件应该导出一个包含了选项的对象：

```java
// vue.config.js
module.exports = {
  // 选项...
}
```

## 参考配置

```java
// const path = require('path');
module.exports = {
  /** 区分打包环境与开发环境
   * process.env.NODE_ENV==='production'  (打包环境)
   * process.env.NODE_ENV==='development' (开发环境)
   * baseUrl: process.env.NODE_ENV==='production'?"https://xxx":'',
   */
  // 项目部署的基础路径
  // 我们默认假设你的应用将会部署在域名的根部,
  // 例如 https://www.my-app.com/
  // 如果你的应用部署在一个子路径下，那么你需要在这里
  // 指定子路径。比如将你的应用部署在
  // https://www.foobar.com/my-app/
  // 那么将这个值改为 '/my-app/'

  //baseUrl: '/',//vue-cli3.3以下版本使用
  publicPath: '/',//vue-cli3.3+新版本使用

  // 构建好的文件输出到哪里
  outputDir: "dist",

  // assetsDir: "base" //静态资源打包地址

  //以多页模式构建应用程序。
  pages: undefined,

  // 是否在保存时使用‘eslint-loader’进行检查 // 有效值: true | false | 'error'
  // 当设置为‘error’时，检查出的错误会触发编译失败
  lintOnSave: true,

  // 使用带有浏览器内编译器的完整构建版本,是否使用包含运行时编译器的 Vue 构建版本
  runtimeCompiler: false,

  // babel-loader默认会跳过`node_modules`依赖. // 通过这个选项可以显示转译一个依赖
  // 默认babel-loader忽略mode_modules，这里可增加例外的依赖包名
  transpileDependencies: [],

  // 是否在构建生产包时生成 sourceMap 文件，false将提高构建速度  映射文件 打包时使用
  productionSourceMap: false,

  // 调整内部的webpack配置.
  // see https://github.com/vuejs/vue-cli/blob/dev/docs/webpack.md
  chainWebpack: () => { },
  // chainWebpack: () => {
  //   // 删除懒加载模块的prefetch，降低带宽压力
  //   // 而且预渲染时生成的prefetch标签是modern版本的，低版本浏览器是不需要的
  //   //config.plugins.delete('prefetch');
  //   //if(process.env.NODE_ENV === 'production') {
  //   // 为生产环境修改配置...process.env.NODE_ENV !== 'development'
  //   //} else {
  //   // 为开发环境修改配置...
  //   //}
  // },
  configureWebpack: () => { },
  // configureWebpack: () => {
  // // 生产and测试环境
  // let pluginsPro = [
  //   new CompressionPlugin({ //文件开启Gzip，也可以通过服务端(如：nginx)
  //     filename: '[path].gz[query]',
  //     algorithm: 'gzip',
  //     test: new RegExp('\\.(' + ['js', 'css'].join('|') + ')$'),
  //     threshold: 8192,
  //     minRatio: 0.8,
  //   }),
  //   new BundleAnalyzerPlugin(),
  // ];
  // //开发环境
  // let pluginsDev = [
  //   new vConsolePlugin({
  //     filter: [], // 需要过滤的入口文件
  //     enable: true // 发布代码前记得改回 false
  //   }),
  // ];
  // if (process.env.NODE_ENV === 'production') { // 为生产环境修改配置...process.env.NODE_ENV !== 'development'
  //   config.plugins = [...config.plugins, ...pluginsPro];
  // } else {
  //   // 为开发环境修改配置...
  //   config.plugins = [...config.plugins, ...pluginsDev];
  // }
  // },

  // CSS 相关选项
  css: {
    // 将组件内部的css提取到一个单独的css文件（只用在生产环境）
    // 也可以是传递给 extract-text-webpack-plugin 的选项对象
    // 是否使用css分离插件 ExtractTextPlugin，采用独立样式文件载入，不采用<style>方式内联至html文件中
    extract: true,

    // 是否在构建css样式映射，false将提高构建速度
    sourceMap: false,

    // css预设器配置项
    loaderOptions: {
      //   sass: {
      //     data: ''//`@import "@/assets/scss/mixin.scss";`
      //   }
    },

    // 启用 CSS modules for all css / pre-processor files.
    modules: false
  },

  // 构建时开启多进程处理 babel 编译
  //是否为 Babel 或 TypeScript 使用 thread-loader。
  //该选项在系统的 CPU 有多于一个内核时自动启用，仅作用于生产构建，在适当的时候开启几个子进程去并发的执行压缩
  parallel: require("os").cpus().length > 1,

  // PWA 插件相关配置
  // 单页插件相关配置 https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-pwa
  pwa: {},

  //vue3.0+
  devServer: {//跨域
    open: process.platform === "darwin",
    //open: true, //配置自动启动浏览器
    disableHostCheck: false,
    host: "0.0.0.0",
    // host: "0.0.0.0" =>
    //   App running at:
    // - Local:   http://localhost:8080/
    // - Network: http://192.168.1.102:8080/
    // host: "127.0.0.1"=>
    //   App running at:
    // - Local:   http://127.0.0.1:8080/
    // - Network: http://127.0.0.1:8080/
    port: 8080,// 端口号
    https: false,// true 配置之后可使用生成 https://localhost:8080/
    hotOnly: false,// 热更新（webpack已实现了，这里false即可）
    // proxy: null // 设置代理
    proxy: 'http://localhost:8080'   // 配置跨域处理,只设一个代理
    //   proxy: { //多个
    //     // 配置跨域处理 可以设置多个
    //     '/api': {
    //       target: 'https://www.baidu.com/api',
    //       ws: true,
    //       changeOrigin: true
    //     }
    //   }
    // before: app => {}
  },

  // vue 2.0 设置跨域
  // dev: {
  //   // proxyTable: {
  //   //     '/api': {
  //   //         target: 'http://127.0.0.1:8080', // 目标地址
  //   //         changeOrigin: true,
  //   //         pathRewrite: {
  //   //             '^/api': '' // 将目标地址变成这个
  //   //         }
  //   //     }
  //   // },
  // },

  // 是否启用dll webpack dll
  // 关于dll只做简单解释 未附详细代码
  // webpack.dll.conf.js
  // 1、entry配置需要dll打包的库
  // 2、module配置处理对应文件类型的loader
  // 3、增加 webpack.DllPlugin插件
  //    (1)、path:生成mainfest.json文件的绝对路径。mainfest.json里面的内容为所有被打包到dll.js文件模块id的映射。
  //    (2)、name：webpack打包时mainfest.json包含的库的暴露出来的函数名名
  //    (3)、contenxt(可选):引入manifest文件的context，默认为webpack的context
  // dll: false,//配置好dll库，设置dll：true；可优化打包效率。减少打包时间，增加库缓存

  // 第三方插件配置
  pluginOptions: {},
  // pluginOptions: {
  //   'style-resources-loader': {//https://github.com/yenshih/style-resources-loader
  //     preProcessor: 'scss',//声明类型
  //     'patterns': [
  //       //path.resolve(__dirname, './src/assets/scss/_common.scss'),
  //     ],
  //     //injector: 'append'
  //   }
  // }
};
```

## 具体属性含义

### [\#][link 5]baseUrl

从 Vue CLI 3.3 起已弃用，请使用[`publicPath`][publicpath]。

### [\#][link 6]publicPath

- Type: `string`
- Default: `'/'`

  部署应用包时的基本 URL。用法和 webpack 本身的 `output.publicPath` 一致，但是 Vue CLI 在一些其他地方也需要用到这个值，所以请始终使用 `publicPath` 而不要直接修改 webpack 的 `output.publicPath`。

  默认情况下，Vue CLI 会假设你的应用是被部署在一个域名的根路径上，例如 `https://www.my-app.com/`。如果应用被部署在一个子路径上，你就需要用这个选项指定这个子路径。例如，如果你的应用被部署在 `https://www.my-app.com/my-app/`，则设置 `publicPath` 为 `/my-app/`。

  这个值也可以被设置为空字符串 (`''`) 或是相对路径 (`'./'`)，这样所有的资源都会被链接为相对路径，这样打出来的包可以被部署在任意路径，也可以用在类似 Cordova hybrid 应用的文件系统中。

  相对 publicPath 的限制

  相对路径的 `publicPath` 有一些使用上的限制。在以下情况下，应当避免使用相对 `publicPath`:

  - 当使用基于 HTML5 `history.pushState` 的路由时；
  - 当使用 `pages` 选项构建多页面应用时。

  这个值在开发环境下同样生效。如果你想把开发服务器架设在根路径，你可以使用一个条件式的值：

  ```java
  module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
      ? '/production-sub-path/'
      : '/'
  }
  ```

### [\#][link 7]outputDir

- Type: `string`
- Default: `'dist'`

  当运行 `vue-cli-service build` 时生成的生产环境构建文件的目录。注意目标目录在构建之前会被清除 (构建时传入 `--no-clean` 可关闭该行为)。

  提示

  请始终使用 `outputDir` 而不要修改 webpack 的 `output.path`。

### [\#][link 8]assetsDir

- Type: `string`
- Default: `''`

  放置生成的静态资源 (js、css、img、fonts) 的 (相对于 `outputDir` 的) 目录。

  提示

  从生成的资源覆写 filename 或 chunkFilename 时，`assetsDir` 会被忽略。

### [\#][link 9]indexPath

- Type: `string`
- Default: `'index.html'`

  指定生成的 `index.html` 的输出路径 (相对于 `outputDir`)。也可以是一个绝对路径。

### [\#][link 10]filenameHashing

- Type: `boolean`
- Default: `true`

  默认情况下，生成的静态资源在它们的文件名中包含了 hash 以便更好的控制缓存。然而，这也要求 index 的 HTML 是被 Vue CLI 自动生成的。如果你无法使用 Vue CLI 生成的 index HTML，你可以通过将这个选项设为 `false` 来关闭文件名哈希。

### [\#][link 11]pages

- Type: `Object`
- Default: `undefined`

  在 multi-page 模式下构建应用。每个“page”应该有一个对应的 JavaScript 入口文件。其值应该是一个对象，对象的 key 是入口的名字，value 是：

  - 一个指定了 `entry`, `template`, `filename`, `title` 和 `chunks` 的对象 (除了 `entry` 之外都是可选的)；
  - 或一个指定其 `entry` 的字符串。

  ```java
  module.exports = {
    pages: {
      index: {
        // page 的入口
        entry: 'src/index/main.js',
        // 模板来源
        template: 'public/index.html',
        // 在 dist/index.html 的输出
        filename: 'index.html',
        // 当使用 title 选项时，
        // template 中的 title 标签需要是 <title><%= htmlWebpackPlugin.options.title %></title>
        title: 'Index Page',
        // 在这个页面中包含的块，默认情况下会包含
        // 提取出来的通用 chunk 和 vendor chunk。
        chunks: ['chunk-vendors', 'chunk-common', 'index']
      },
      // 当使用只有入口的字符串格式时，
      // 模板会被推导为 `public/subpage.html`
      // 并且如果找不到的话，就回退到 `public/index.html`。
      // 输出文件名会被推导为 `subpage.html`。
      subpage: 'src/subpage/main.js'
    }
  }
  ```

  提示

  当在 multi-page 模式下构建时，webpack 配置会包含不一样的插件 (这时会存在多个 `html-webpack-plugin` 和 `preload-webpack-plugin` 的实例)。如果你试图修改这些插件的选项，请确认运行 `vue inspect`。

### [\#][link 12]lintOnSave

- Type: `boolean` | `'warning'` | `'default'` | `'error'`
- Default: `'default'`

  是否在开发环境下通过 [eslint-loader][] 在每次保存时 lint 代码。这个值会在 [`@vue/cli-plugin-eslint`][vue_cli-plugin-eslint] 被安装之后生效。

  设置为 `true` 或 `'warning'` 时，`eslint-loader` 会将 lint 错误输出为编译警告。默认情况下，警告仅仅会被输出到命令行，且不会使得编译失败。

  如果你希望让 lint 错误在开发时直接显示在浏览器中，你可以使用 `lintOnSave: 'default'`。这会强制 `eslint-loader` 将 lint 错误输出为编译错误，同时也意味着 lint 错误将会导致编译失败。

  设置为 `error` 将会使得 `eslint-loader` 把 lint 警告也输出为编译错误，这意味着 lint 警告将会导致编译失败。

  或者，你也可以通过设置让浏览器 overlay 同时显示警告和错误：

  ```java
  // vue.config.js
  module.exports = {
    devServer: {
      overlay: {
        warnings: true,
        errors: true
      }
    }
  }
  ```

  当 `lintOnSave` 是一个 truthy 的值时，`eslint-loader` 在开发和生产构建下都会被启用。如果你想要在生产构建时禁用 `eslint-loader`，你可以用如下配置：

  ```java
  // vue.config.js
  module.exports = {
    lintOnSave: process.env.NODE_ENV !== 'production'
  }
  ```

### [\#][link 13]runtimeCompiler

- Type: `boolean`
- Default: `false`

  是否使用包含运行时编译器的 Vue 构建版本。设置为 `true` 后你就可以在 Vue 组件中使用 `template` 选项了，但是这会让你的应用额外增加 10kb 左右。

  更多细节可查阅：[Runtime + Compiler vs. Runtime only][runtime _ compiler vs. runtime only]。

### [\#][link 14]transpileDependencies

- Type: `Array<string | RegExp>`
- Default: `[]`

  默认情况下 `babel-loader` 会忽略所有 `node_modules` 中的文件。如果你想要通过 Babel 显式转译一个依赖，可以在这个选项中列出来。

### [\#][link 15]productionSourceMap

- Type: `boolean`
- Default: `true`

  如果你不需要生产环境的 source map，可以将其设置为 `false` 以加速生产环境构建。

### [\#][link 16]crossorigin

- Type: `string`
- Default: `undefined`

  设置生成的 HTML 中 `<link rel="stylesheet">` 和 `<script>` 标签的 `crossorigin` 属性。

  需要注意的是该选项仅影响由 `html-webpack-plugin` 在构建时注入的标签 - 直接写在模版 (`public/index.html`) 中的标签不受影响。

  更多细节可查阅: [CORS settings attributes][]

### [\#][link 17]integrity

- Type: `boolean`
- Default: `false`

  在生成的 HTML 中的 `<link rel="stylesheet">` 和 `<script>` 标签上启用 [Subresource Integrity][] (SRI)。如果你构建后的文件是部署在 CDN 上的，启用该选项可以提供额外的安全性。

  需要注意的是该选项仅影响由 `html-webpack-plugin` 在构建时注入的标签 - 直接写在模版 (`public/index.html`) 中的标签不受影响。

  另外，当启用 SRI 时，preload resource hints 会被禁用，因为 [Chrome 的一个 bug][chrome _ bug] 会导致文件被下载两次。

### [\#][link 18]configureWebpack

- Type: `Object | Function`

  如果这个值是一个对象，则会通过 [webpack-merge][] 合并到最终的配置中。

  如果这个值是一个函数，则会接收被解析的配置作为参数。该函数既可以修改配置并不返回任何东西，也可以返回一个被克隆或合并过的配置版本。

  更多细节可查阅：[配合 webpack > 简单的配置方式][webpack _]

### [\#][link 19]chainWebpack

- Type: `Function`

  是一个函数，会接收一个基于 [webpack-chain][] 的 `ChainableConfig` 实例。允许对内部的 webpack 配置进行更细粒度的修改。

  更多细节可查阅：[配合 webpack > 链式操作][webpack _ 1]

### [\#][link 20]css.modules

从 v4 起已弃用，请使用[`css.requireModuleExtension`][css.requiremoduleextension]。 在 v3 中，这个选项含义与 `css.requireModuleExtension` 相反。

### [\#][link 21]css.requireModuleExtension

- Type: `boolean`
- Default: `true`

  默认情况下，只有 `*.module.[ext]` 结尾的文件才会被视作 CSS Modules 模块。设置为 `false` 后你就可以去掉文件名中的 `.module` 并将所有的 `*.(css|scss|sass|less|styl(us)?)` 文件视为 CSS Modules 模块。

  提示

  如果你在 `css.loaderOptions.css` 里配置了自定义的 CSS Module 选项，则 `css.requireModuleExtension` 必须被显式地指定为 `true` 或者 `false`，否则我们无法确定你是否希望将这些自定义配置应用到所有 CSS 文件中。

  更多细节可查阅：[配合 CSS > CSS Modules][css _ css modules]

### [\#][link 22]css.extract

- Type: `boolean | Object`
- Default: 生产环境下是 `true`，开发环境下是 `false`

  是否将组件中的 CSS 提取至一个独立的 CSS 文件中 (而不是动态注入到 JavaScript 中的 inline 代码)。

  同样当构建 Web Components 组件时它总是会被禁用 (样式是 inline 的并注入到了 shadowRoot 中)。

  当作为一个库构建时，你也可以将其设置为 `false` 免得用户自己导入 CSS。

  提取 CSS 在开发环境模式下是默认不开启的，因为它和 CSS 热重载不兼容。然而，你仍然可以将这个值显性地设置为 `true` 在所有情况下都强制提取。

### [\#][link 23]css.sourceMap

- Type: `boolean`
- Default: `false`

  是否为 CSS 开启 source map。设置为 `true` 之后可能会影响构建的性能。

### [\#][link 24]css.loaderOptions

- Type: `Object`
- Default: `{}`

  向 CSS 相关的 loader 传递选项。例如：

  ```java
  module.exports = {
    css: {
      loaderOptions: {
        css: {
          // 这里的选项会传递给 css-loader
        },
        postcss: {
          // 这里的选项会传递给 postcss-loader
        }
      }
    }
  }
  ```

  支持的 loader 有：

  - [css-loader][]
  - [postcss-loader][]
  - [sass-loader][]
  - [less-loader][]
  - [stylus-loader][]

  另外，也可以使用 `scss` 选项，针对 `scss` 语法进行单独配置（区别于 `sass` 语法）。

  更多细节可查阅：[向预处理器 Loader 传递选项][loader]

  提示

  相比于使用 `chainWebpack` 手动指定 loader 更推荐上面这样做，因为这些选项需要应用在使用了相应 loader 的多个地方。

### [\#][link 25]devServer

- Type: `Object`

  [所有 `webpack-dev-server` 的选项][_webpack-dev-server_]都支持。注意：

  - 有些值像 `host`、`port` 和 `https` 可能会被命令行参数覆写。
  - 有些值像 `publicPath` 和 `historyApiFallback` 不应该被修改，因为它们需要和开发服务器的 [publicPath][link 6] 同步以保障正常的工作。

### [\#][link 26]devServer.proxy

- Type: `string | Object`

  如果你的前端应用和后端 API 服务器没有运行在同一个主机上，你需要在开发环境下将 API 请求代理到 API 服务器。这个问题可以通过 `vue.config.js` 中的 `devServer.proxy` 选项来配置。

  `devServer.proxy` 可以是一个指向开发环境 API 服务器的字符串：

  ```java
  module.exports = {
    devServer: {
      proxy: 'http://localhost:4000'
    }
  }
  ```

  这会告诉开发服务器将任何未知请求 (没有匹配到静态文件的请求) 代理到`http://localhost:4000`。

  如果你想要更多的代理控制行为，也可以使用一个 `path: options` 成对的对象。完整的选项可以查阅 [http-proxy-middleware][] 。

  ```java
  module.exports = {
    devServer: {
      proxy: {
        '/api': {
          target: '<url>',
          ws: true,
          changeOrigin: true
        },
        '/foo': {
          target: '<other_url>'
        }
      }
    }
  }
  ```

### [\#][link 27]parallel

- Type: `boolean`
- Default: `require('os').cpus().length > 1`

  是否为 Babel 或 TypeScript 使用 `thread-loader`。该选项在系统的 CPU 有多于一个内核时自动启用，仅作用于生产构建。

### [\#][link 28]pwa

- Type: `Object`

  向 [PWA 插件][pwa]传递选项。

### [\#][link 29]pluginOptions

- Type: `Object`

  这是一个不进行任何 schema 验证的对象，因此它可以用来传递任何第三方插件选项。例如：

  ```java
  module.exports = {
    pluginOptions: {
      foo: {
        // 插件可以作为 `options.pluginOptions.foo` 访问这些选项。
      }
    }
  }
  ```

## [\#][link 30]Babel

Babel 可以通过 `babel.config.js` 进行配置。

提示

Vue CLI 使用了 Babel 7 中的新配置格式 `babel.config.js`。和 `.babelrc` 或 `package.json` 中的 `babel` 字段不同，这个配置文件不会使用基于文件位置的方案，而是会一致地运用到项目根目录以下的所有文件，包括 `node_modules` 内部的依赖。我们推荐在 Vue CLI 项目中始终使用 `babel.config.js` 取代其它格式。

所有的 Vue CLI 应用都使用 `@vue/babel-preset-app`，它包含了 `babel-preset-env`、JSX 支持以及为最小化包体积优化过的配置。通过[它的文档][link 31]可以查阅到更多细节和 preset 选项。

同时查阅指南中的 [Polyfill][] 章节。

## [\#][link 32]ESLint

ESLint 可以通过 `.eslintrc` 或 `package.json` 中的 `eslintConfig` 字段来配置。

更多细节可查阅 [@vue/cli-plugin-eslint][vue_cli-plugin-eslint]。

## [\#][link 33]TypeScript

TypeScript 可以通过 `tsconfig.json` 来配置。

更多细节可查阅 [@vue/cli-plugin-typescript][vue_cli-plugin-typescript]。

## [\#][link 34]单元测试

### [\#][link 35]Jest

更多细节可查阅 [@vue/cli-plugin-unit-jest][vue_cli-plugin-unit-jest]。

### [\#][link 36]Mocha (配合 `mocha-webpack`)

更多细节可查阅 [@vue/cli-plugin-unit-mocha][vue_cli-plugin-unit-mocha]。

## [\#][link 37]E2E 测试

### [\#][link 38]Cypress

更多细节可查阅 [@vue/cli-plugin-e2e-cypress][vue_cli-plugin-e2e-cypress]。

### [\#][link 39]Nightwatch

更多细节可查阅 [@vue/cli-plugin-e2e-nightwatch][vue_cli-plugin-e2e-nightwatch]。

参考:

[https://cli.vuejs.org/zh/config/][https_cli.vuejs.org_zh_config]

[https://www.cnblogs.com/xzychoose/p/11505113.html][https_www.cnblogs.com_xzychoose_p_11505113.html]

[link 1]: https://cli.vuejs.org/zh/config/#%E5%85%A8%E5%B1%80-cli-%E9%85%8D%E7%BD%AE
[link 2]: https://cli.vuejs.org/zh/config/#%E7%9B%AE%E6%A0%87%E6%B5%8F%E8%A7%88%E5%99%A8
[link 3]: https://cli.vuejs.org/zh/guide/browser-compatibility.html#browserslist
[link 4]: https://cli.vuejs.org/zh/config/#vue-config-js
[link 5]: https://cli.vuejs.org/zh/config/#baseurl
[publicpath]: https://cli.vuejs.org/zh/config/#publicPath
[link 6]: https://cli.vuejs.org/zh/config/#publicpath
[link 7]: https://cli.vuejs.org/zh/config/#outputdir
[link 8]: https://cli.vuejs.org/zh/config/#assetsdir
[link 9]: https://cli.vuejs.org/zh/config/#indexpath
[link 10]: https://cli.vuejs.org/zh/config/#filenamehashing
[link 11]: https://cli.vuejs.org/zh/config/#pages
[link 12]: https://cli.vuejs.org/zh/config/#lintonsave
[eslint-loader]: https://github.com/webpack-contrib/eslint-loader
[vue_cli-plugin-eslint]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint
[link 13]: https://cli.vuejs.org/zh/config/#runtimecompiler
[runtime _ compiler vs. runtime only]: https://cn.vuejs.org/v2/guide/installation.html#%E8%BF%90%E8%A1%8C%E6%97%B6-%E7%BC%96%E8%AF%91%E5%99%A8-vs-%E5%8F%AA%E5%8C%85%E5%90%AB%E8%BF%90%E8%A1%8C%E6%97%B6
[link 14]: https://cli.vuejs.org/zh/config/#transpiledependencies
[link 15]: https://cli.vuejs.org/zh/config/#productionsourcemap
[link 16]: https://cli.vuejs.org/zh/config/#crossorigin
[cors settings attributes]: https://developer.mozilla.org/zh-CN/docs/Web/HTML/CORS_settings_attributes
[link 17]: https://cli.vuejs.org/zh/config/#integrity
[subresource integrity]: https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity
[chrome _ bug]: https://bugs.chromium.org/p/chromium/issues/detail?id=677022
[link 18]: https://cli.vuejs.org/zh/config/#configurewebpack
[webpack-merge]: https://github.com/survivejs/webpack-merge
[webpack _]: https://cli.vuejs.org/zh/guide/webpack.html#%E7%AE%80%E5%8D%95%E7%9A%84%E9%85%8D%E7%BD%AE%E6%96%B9%E5%BC%8F
[link 19]: https://cli.vuejs.org/zh/config/#chainwebpack
[webpack-chain]: https://github.com/mozilla-neutrino/webpack-chain
[webpack _ 1]: https://cli.vuejs.org/zh/guide/webpack.html#%E9%93%BE%E5%BC%8F%E6%93%8D%E4%BD%9C-%E9%AB%98%E7%BA%A7
[link 20]: https://cli.vuejs.org/zh/config/#css-modules
[css.requiremoduleextension]: https://cli.vuejs.org/zh/config/#css-requireModuleExtension
[link 21]: https://cli.vuejs.org/zh/config/#css-requiremoduleextension
[css _ css modules]: https://cli.vuejs.org/zh/guide/css.html#css-modules
[link 22]: https://cli.vuejs.org/zh/config/#css-extract
[link 23]: https://cli.vuejs.org/zh/config/#css-sourcemap
[link 24]: https://cli.vuejs.org/zh/config/#css-loaderoptions
[css-loader]: https://github.com/webpack-contrib/css-loader
[postcss-loader]: https://github.com/postcss/postcss-loader
[sass-loader]: https://github.com/webpack-contrib/sass-loader
[less-loader]: https://github.com/webpack-contrib/less-loader
[stylus-loader]: https://github.com/shama/stylus-loader
[loader]: https://cli.vuejs.org/zh/guide/css.html#%E5%90%91%E9%A2%84%E5%A4%84%E7%90%86%E5%99%A8-loader-%E4%BC%A0%E9%80%92%E9%80%89%E9%A1%B9
[link 25]: https://cli.vuejs.org/zh/config/#devserver
[_webpack-dev-server_]: https://webpack.js.org/configuration/dev-server/
[link 26]: https://cli.vuejs.org/zh/config/#devserver-proxy
[http-proxy-middleware]: https://github.com/chimurai/http-proxy-middleware#proxycontext-config
[link 27]: https://cli.vuejs.org/zh/config/#parallel
[link 28]: https://cli.vuejs.org/zh/config/#pwa
[pwa]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-pwa
[link 29]: https://cli.vuejs.org/zh/config/#pluginoptions
[link 30]: https://cli.vuejs.org/zh/config/#babel
[link 31]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/babel-preset-app
[polyfill]: https://cli.vuejs.org/zh/guide/browser-compatibility.html#polyfill
[link 32]: https://cli.vuejs.org/zh/config/#eslint
[link 33]: https://cli.vuejs.org/zh/config/#typescript
[vue_cli-plugin-typescript]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-typescript
[link 34]: https://cli.vuejs.org/zh/config/#%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95
[link 35]: https://cli.vuejs.org/zh/config/#jest
[vue_cli-plugin-unit-jest]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-unit-jest
[link 36]: https://cli.vuejs.org/zh/config/#mocha-%E9%85%8D%E5%90%88-mocha-webpack
[vue_cli-plugin-unit-mocha]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-unit-mocha
[link 37]: https://cli.vuejs.org/zh/config/#e2e-%E6%B5%8B%E8%AF%95
[link 38]: https://cli.vuejs.org/zh/config/#cypress
[vue_cli-plugin-e2e-cypress]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-e2e-cypress
[link 39]: https://cli.vuejs.org/zh/config/#nightwatch
[vue_cli-plugin-e2e-nightwatch]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-e2e-nightwatch
[https_cli.vuejs.org_zh_config]: https://cli.vuejs.org/zh/config/
[https_www.cnblogs.com_xzychoose_p_11505113.html]: https://www.cnblogs.com/xzychoose/p/11505113.html

### Reference

[关于 Vue 配置 config 文件详解](https://www.cnblogs.com/makalochen/p/13984699.html)

**2022.08.18**
