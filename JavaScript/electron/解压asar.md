<font size=4 face='楷体'>

## 解压 electron 的 app.asar

app.asar 文件是 Electron 程序的主业务文件, 是一种压缩格式的文件

### 解压步骤

- 全局安装 npm
- 确定已正确安装 npm
  `npm -v` 指令是否可以返回版本号来确定是否已经正确安装了 npm

- 全局环境安装 asar
  `npm install -g asar` 或者 `cnpm install -g asar`

- 确定已经正确安装 asar

  `asar -V`

- 解压缩 asar 文件

  在 asar 文件所在的根目录执行`asar extract app.asar ./`

  第一个是需要解压缩的 asar 文件
  第二个参数是解压缩之后文件存放的路径

## Reference

[如何解压 electron 的 app.asar](https://blog.csdn.net/qq_35432904/article/details/107381278)

**2022.07.20**
