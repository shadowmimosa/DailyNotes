<font size=4 face='楷体'>

## 反编译 webpack

- 安装 debundle

  > npm i -g debundle

- 语法

  ```bash
  debundle 用法：debundle [输入文件] {OPTIONS} 选项：
              --input，
              --i Bundle to debundle
              --output，
              -o将代码解压缩到的目录。    --config，-c配置文件

  #curl https://raw.githubusercontent.com/1egoman/debundle/master/test_bundles/browserify/bundle.js > bundle.js

  #curl https://raw.githubusercontent.com/1egoman/debundle/master/test_bundles/browserify/debundle.config.json > debundle.config.json

  #cat debundle.config.json

  {   "type": "browserify",   "knownPaths": {} }

  使用命令#debundle -i bundle.js -o dist/ -c debundle.config.json （
  bundle.js 是需要被反编译的js   dist反编译后输出的目录
  debundle.config.json 是反编译的配置文件 ）

  注意：如果找到debundle命令，需要使用ln  -s  root/data/debundle /usr/bin/debundle 建立软连接。

  注意：如果反编译的过程有错误，debundle.config.json使用如下配置文件

  #cat debundle.config.json
  {
  "type": "webpack",
  "knownPaths": {},
  "entryPoint": 1,
  "moduleAst": ["body", 0, "expression", "argument", "arguments", 0]
  }
  ```

实际使用还尚未成功
**待填坑**

### Reference

[使用 debundle 反编译（解压）webpack 打包的 javascript 代码](https://6iit.com/3147)

**2020.03.28**
