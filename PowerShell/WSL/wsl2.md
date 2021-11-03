<font size=4 face='楷体'>

## WSL2 安装

### 升级到 WSL2

-   安装 WSL2 功能模块

    ```powershell
    # 安装 Windows 10 的 WSL 功能
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

    #  安装 WSL2 功能模块
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```

    需重启电脑生效

-   安装 Linux 内核
    按[官方教程](https://docs.microsoft.com/zh-cn/windows/wsl/wsl2-kernel)中，下载安装驱动

    ```powershell
    # 设置 wsl 默认版本
    wsl --set-default-version 2
    ```

-   安装 Linux 发行版
    Microsoft Store 中安装相应发行版

### wsl1 wsl2 共存

-   安装多个发行版
    可以同时装两个发行版，一个用 WSL1 一个用 WSL2，这样就互不影响
-   切换版本
    转换时间较长

    ```powershell
    wsl --set-version <distribution name> <versionNumber>

    # eg
    wsl --set-version Ubuntu 2
    ```

### Reference

[WSL2 来了！但是能正常使用并不简单](https://zhuanlan.zhihu.com/p/144583887)
[适用于 Linux 的 Windows 子系统的命令参考](https://docs.microsoft.com/zh-cn/windows/wsl/reference)

**2020.11.18**
