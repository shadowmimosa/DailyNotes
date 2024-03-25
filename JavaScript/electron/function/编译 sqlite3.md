<font size=4 face='楷体'>

## electron 编译 sqlite3

直接通过 `npm install sqlite3` 安装 [sqlite3](https://github.com/TryGhost/node-sqlite3), 无法在 electron 内使用
需要进行编译

### 版本

> sqlite3 在升级到 5.0.2 之后, 可以支持 electron 8.X 之后的版本了
> 如果 electron 在 8 之前可以安装 sqlite3 之前的版本 4.2.0

另外还要注意 32 位 64 位的问题

### 配置安装

配置 [node-pre-gyp](https://github.com/nodejs/node-gyp#on-windows) 手动安装

- VisualStudio 2019 安装 (带有 C++桌面开发 或者安装 windows-build-tools
  ```bash
  npm install --global --production windows-build-tools
  ```
- 安装 node-pre-gyp
  ```bash
  npm install -g node-gyp
  npm install -g node-pre-gyp
  ```
- msvs 版本配置设置 (手动输入路径, 因为 npm 查找路径时出错
  ```bash
  npm config set msvs_version "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community"
  ```
- 安装 sqlite3
  ```bash
  npm install sqlite3
  ```
- electron 适配编译
  ```bash
  node-gyp rebuild --target=7.1.4 --arch=x64 --target_platform=win32  --dist-url=https://atom.io/download/electron/ --module_name=node_sqlite3 --module_path=../lib/binding/electron-v7.1-win32-x64
  ```
  target electron 版本号

### 使用 electron-builder

首先 python2.7, vs2015 这些环境, 很多 nodejs 使用的 c++包都需要
可以安装 windows-build-tools

在 package.json 内配置 `"postinstall": "install-app-deps"`

- postinstall 是 npm 的一个钩子, 它会在你执行 npm install 安装完成后执行
- install-app-deps 是 electron 的命令, 会利用 electron-builder 重新构建绑定了当下 sqlite3 版本的 electron

```json
// package.json

"scripts": {
  "postinstall": "install-app-deps",
  // 或者
  "postinstall": "electron-builder install-app-deps",
}
```

安装 sqlite3

```bash
npm i sqlite3 -S
```

- 安装之后他会自动进行编译 `node-pre-gyp install –fallback-to-build`

- 先编译出对应 nodejs 版本的 sqlite3 版本 类似 \node_modules\sqlite3\lib\binding\node-v57-win32-x64\node_sqlite3.node

- 再自动执行 install-app-deps, 编译出对应 electron 版本的 sqlite3 版本, 类似 \node_modules\sqlite3\lib\binding\electron-v1.8-win32-x64\node_sqlite3.node
  如果因为某个原因没有执行 install-app-deps, 那么在这个时候手动执行也是可以的

- 最后一步操作如果失败, 很大原因是因为被墙了, 挂代理或者用 cnpm 装 sqlite3 也是可行的

### electron-rebuild

- 安装 electron-rebuild
  ```bash
  npm install --save-dev electron-rebuild
  ```
- 安装 node-gyp
  ```bash
  npm install node-gyp -g
  ```
- 安装 sqlite3
  ```bash
  npm install --save sqlite3
  ```
- 修改 package.json

  ```json
  // package.json

  "scripts": {
    "rebuild": "electron-rebuild -f -w sqlite3"
  }
  ```

- 编译
  ```bash
  npm run rebuild
  ```
- 报错的话, 通过 cnpm 试试
  ```bash
  # 安装
  npm install -g cnpm --registry=https://registry.npm.taobao.org
  # 测试
  cnpm -v
  # 清理缓存
  npm cache clean -f
  # 安装  target 为 electron 版本号
  cnpm install sqlite3@latest --build-from-source --runtime=electron --target=8.3.0 --dist-url=https://atom.io/download/electron --save
  # 编译
  cnpm run rebuild
  ```

### 替代

也可以使用 [sql.js](https://github.com/sql-js/sql.js) 代替
[Electron 中使用 sql.js 操作 SQLite 数据库](https://xushanxiang.com/electron-sql-js-sqlite.html)
[Online SQL interpreter](https://sql.js.org/examples/GUI/index.html)

### 官方说明

原生 Node.js 模块由 Electron 支持，但由于 Electron 具有与给定 Node.js 不同的 应用二进制接口 (ABI)(由于使用 Chromium 的 BoringSL 而不是 OpenSSL 等 差异)，您使用的原生 模块需要为 Electron 重新编译。 否则，当您尝试运行您的应用程序时， 将会遇到以下的错误：

```bash
Error: The module '/path/to/native/module.node'
was compiled against a different Node.js version using
NODE_MODULE_VERSION $XYZ. This version of Node.js requires
NODE_MODULE_VERSION $ABC. Please try re-compiling or re-installing
the module (for instance, using `npm rebuild` or `npm install`).
```

[如何安装原生模块](https://www.electronjs.org/zh/docs/latest/tutorial/using-native-node-modules#installing-modules-and-rebuilding-for-electron)

### 概述

- 首先查看是否安装了 sqlite3 依赖 (`npm i sqlite3`)
  或者指定版本安装 `npm i sqlite3@5.0.1`

- 然后查看是否安装了 sqlite3 的编译依赖 node-gyp (`npm i node-gyp`)
  或者 node-pre-gyp (`npm i node-pre-gyp`)
  - 安装 python2.7, 如果之前安装过多个版本则必须 `npm config set python "/path/python.exe"`, 必须为 2.7 版本
  - 安装 Visual Studio 2015, 安装过程中需要安装 c++相关, 必须安装
  - 安装 windows-build-tools `npm install windows-build-tools -g`, 如果 npm 不行 尝试 `cnpm install windows-build-tools -g`, windows build 错误时, 需要重新安装 vs2015
    - 安装 node-pre-gyp 和 node-gyp `npm install node-pre-gyp -g npm install node-gyp -g`
- 安装完成后，查看 package.json 文件中的 scripts 属性中是否有 postinstall 键值
  - 如果有, 将其值设置为 `"install-app-deps"`
    如果没有, 添加 `"postinstall" : "install-app-deps"`
- 然后在 npm install 一下
  执行完后，查看 `node_modules\sqlite3\lib\binding` 目录下是否已经存在 `electron-v2.0-win32-x64\node_sqlite3.node` 文件
  如果已经存在，就可以启动项目了

或者尝试手动编译

```bash
cnpm install sqlite3@latest --build-from-source --runtime=electron --target=1.7.9 --dist-url=https://atom.io/download/electron --save
```

`--target` 后为 electron 版本

```bash
electron --version
```

### Reference

[electron 项目中使用 sqlite3 的编译问题（windows）](https://blog.csdn.net/CaanDoll/article/details/81429171)
[关于 electron 使用 sqlite3 的一些问题](https://blog.csdn.net/baidu_40294156/article/details/121613357)
[在成功安装 sqlite3 后尝试运行代码时，如何修复此“模块未找到错误”？](https://www.5axxw.com/questions/content/i4b6or)
[Electron(Windows) sqlite3 使用](https://blog.csdn.net/cs_1307725524/article/details/103601718)
[electron 集成 sqlite3](https://www.cnblogs.com/yuNotes/p/12957072.html)
[node-webkit 中使用 sqlite3(含编译教程)](https://blog.csdn.net/carfge/article/details/115230594)
[electron 项目中使用 sqlite3 数据库，获取不到 node_sqlite3.node 文件的问题](https://blog.csdn.net/qq_37237495/article/details/99438874)
[Electron & sqlite3 新手入门](https://www.jianshu.com/p/5ac9ffc904fa)
[electron 搭配 sqlite3 数据库之环境安装](https://newsn.net/say/electron-sqlite3.html)

**2022.07.28**
