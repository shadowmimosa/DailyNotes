<font size=4 face='楷体'>

## Windows 下 GCC 编译环境配置

Windows 下很多地方也有需要使用 GCC 编译环境，如 python 安装某些包

在 Windows 下可以通过 MinGW-w64 安装 GCC 环境，但 MinGW-w64 是有很多发行版的, 如 `MingW-W64-builds`, `MSYS2`, `WinLibs.com` 等，可以在[这里](https://www.mingw-w64.org/downloads/)查看

### MSYS2

安装参考[官网文档](https://www.msys2.org/)即可，大致步骤如下

- 下载软件
- 安装启动
- 配置 GCC
  在 MSYS2 提供的终端(MSYS2 MSY)中执行
  ```bash
  pacman -S mingw-w64-ucrt-x86_64-gcc
  ```
- 检查版本
  ```bash
  gcc --version
  ```
  出现 GCC 版本号即代表成功

### Reference

[MSYS2 官网文档](https://www.msys2.org/)
[windows 安装 MSYS2（mingw && gcc）](https://blog.csdn.net/xuxu_123_/article/details/130516711)

**2024.01.04**
