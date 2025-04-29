<font size=4 face='楷体'>

## Prettier 针对不同语言配置

### 项目配置

prettier 官方给出了针对不同项目配置 prettier 的方法
在项目根目录建立`.prettierrc`文件

```json
{
  "semi": false,
  "overrides": [
    {
      "files": "*.test.js",
      "options": {
        "semi": true
      }
    },
    {
      "files": ["*.html", "legacy/**/*.js"],
      "options": {
        "tabWidth": 4
      }
    },
    {
      "files": ["*.css"],
      "options": {
        "tabWidth": 2
      }
    }
  ]
}
```

### 全局配置

官方文档在扩展设置一栏中给了一个 `prettier.configPath`

> prettier.configPath
> 提供更漂亮的配置文件的自定义路径。

> 注意，如果设置了该值，将始终使用该值，并且本地配置文件将被忽略。全局默认值的一个更好的选择是将~/.prettierrc 文件放在主目录中。

在 setting.json 中设置

```json
"prettier.configPath": "**/.prettierrc",
```

需要注意的是, 如果设置了这个选项, 那你项目目录的 `.prettierrc` 文件就会失效

### prettier 设置详解

```json
{
  "//": "https://prettier.io/docs/en/options.html#prose-wrap",
  "_comment0": "trailingComma:在多行逗号分隔的句法结构中尽可能打印尾随逗号,默认es5,'es5'- 在 ES5 中有效的尾随逗号(对象、数组等)。TypeScript 中的类型参数中没有尾随逗号。'none'- 没有尾随逗号。'all'- 尽可能使用尾随逗号",
  "trailingComma": "none",
  "_comment1": "printWidth:一行长度,默认80",
  "printWidth": 120,
  "_comment2": "tabWidth:缩进级别的空格数,默认2",
  "tabWidth": 2,
  "_comment3": "semi:在语句的末尾打印分号,默认true",
  "semi": false,
  "_comment4": "singleQuote:使用单引号而不是双引号,默认false",
  "singleQuote": true,
  "_comment5": "bracketSameLine:将>多行 HTML(HTML、JSX、Vue、Angular)元素放在最后一行的末尾,而不是单独放在下一行,默认false",
  "bracketSameLine": true,
  "_comment6": "useTabs:使用制表符而不是空格缩进行,默认false",
  "useTabs": false,
  "_comment7": "quoteProps:引用对象中的属性时更改,默认'as-needed'",
  "quoteProps": "as-needed",
  "_comment8": "jsxSingleQuote:在 JSX 中使用单引号而不是双引号,默认false",
  "jsxSingleQuote": true,
  "_comment9": "bracketSpacing:在语句的末尾打印分号,默认true",
  "bracketSpacing": true,
  "_comment10": "arrowParens:引用对象中的属性时更改,默认'always','always'- 始终包括括号。例子:(x) => x'avoid'- 尽可能省略括号。例子:x => x",
  "arrowParens": "always",
  "_comment11": "endOfLine:文本文件中的行尾风格,默认'lf','lf'– 仅换行 ( \n),常见于 Linux 和 macOS 以及 git repos 内部'crlf'- 回车 + 换行字符 ( \r\n),常见于 Windows",
  "endOfLine": "lf",
  "_comment12": "html 存在空格是不敏感的",
  "htmlWhitespaceSensitivity": "ignore",
  "_comment13": "vue 的 script 和 style 的内容是否缩进",
  "vueIndentScriptAndStyle": false,
  "_comment14": "组件或者标签的属性是否控制一行只显示一个属性",
  "singleAttributePerLine": false,
  "_comment15": "是否需要在文件顶部添加特殊的注释才能进行格式化，默认为 false",
  "requirePragma": false,
  "_comment16": "是否保留 markdown 文件中的换行符，默认为 preserve",
  "proseWrap": "preserve",
  "_comment17": "是否在格式化后的文件顶部插入特殊的注释，默认为 false",
  "insertPragma": false
}
```

## Reference

[prettier 官方文档](https://prettier.io/docs/en/configuration)
[插件官方文档](https://github.com/prettier/prettier-vscode)
[vscode 之 prettier 插件配置](https://www.dazhuanlan.com/2020/04/02/5e84fd72d7551/)
[vscode 配置 prettier](https://www.jianshu.com/p/162db0ff0b47)
[vscode Prettier 安装及配置](https://blog.csdn.net/weixin_62992614/article/details/131991716)

**Create On 2021.05.13, Modify On 2023.11.20**
