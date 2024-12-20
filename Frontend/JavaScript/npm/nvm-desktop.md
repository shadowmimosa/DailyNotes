<font size=4 face='楷体'>

## nvm 使用

作为一枚前端开发工程师，我们一般都是通过在 [官网](https://nodejs.org/) 下载二进制安装包来安装 `node`，但是实际开发难免会因为一些兼容性的问题需要安装切换不同版本的 `node`，如果还是通过这种方式，那么就必须先卸载现有版本再安装新的版本，无疑十分不便。

虽然社区已经有很成熟的工具（[nvm](https://github.com/nvm-sh/nvm)）来解决这个问题，但是 `nvm` 是基于 `shell` 的交互式命令的，用起来可能还是不是那么直观便捷：比如在 `macOS` 平台需要安装支持 `arm64` 架构的版本的 `node`，`nvm` 就没办法通过命令（`nvm ls -remote`）来查看；而在 Windows 平台则需要通过 [nvm-windows](https://github.com/coreybutler/nvm-windows) 来单独安装以获得支持。

今天就来介绍一个通过可视化界面操作来实现安装和管理多个 node 版本的工具：[nvm-desktop](https://github.com/1111mp/nvm-desktop)，全称：`Node Version Manager Desktop`，支持双平台，代码完全开源，可放心使用。

现在已经支持为不同项目单独设置和切换不同版本的 Node，开箱即用，不需要任何其他操作。

### Reference

[使用 nvm-desktop 轻松安装和管理多个 node 版本（支持为项目单独设置 Node 版本）](https://zhuanlan.zhihu.com/p/656404601)

**2023.12.18**
