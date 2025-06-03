没想到在我上篇关于 WSL 2的文章发布后的 5 天，微软就正式发布了 WSL 1.0，上篇文章发布 5 天就过时了。另外，微软曾在 9 月更新了一波 WSL 2 官宣了对 systemd 的支持，但只对 Windows 11 可用。这次正式发布的 WSL 1.0 在 Windows 10 上也是可用的，这就意味着 Windows 10 上的 WSL 2 也可以使用 systemd 了，太开心了，我决定再写（水）一篇 WSL 的安装教程，毕竟上篇已经过时了。

> 注意，本次发布的 WSL 1.0 是指 WSL 2 的 1.0 版本。WSL 分为 WSL 1 和 WSL 2，后者是前者的替代，两者技术完全不同。WSL 1 已经不更新了。

### 安装

### Step 0：升级 Windwos 10 到最新版

打开设置——更新和安全——检查更新，安装更新。然后打开文件资源管理器，在左侧“此电脑”上右击--属性，在弹出的窗口中查看系统信息，确保 Windows 10 版本号为 22H2 或更高，操作系统内部版本为 19045.2311 或更高。

![](https://pic4.zhimg.com/v2-3487c8777d91bbd9a79c2951da1c757f_b.jpg)

### Step 1：打开相关功能

在任务栏的搜索框中搜索”启用或关闭 Windows 功能“。

![](https://pic1.zhimg.com/v2-9a319dd5aa9cc84eb0ca3240a3b3c4a4_b.jpg)

在打开的”Windows 功能“窗口中勾选 ”Hyper-V“、"适用于 Linux 的 Windows 子系统"、”虚拟机平台“，然后点确定。

![](https://pic4.zhimg.com/v2-d4f7e2fdd18e9c9b2b90e322f174bf63_b.jpg)

如果点确定后系统提示你重启，那你就重启。我这边因为默认是开启状态，所以没有提示重启。

### Step 2：在命令行中确认并更改 WSL 默认版本

走完前面两步，WSL 应该已经可用了。以管理员权限打开系统自带的 PowerShell 或你自己安装其他终端（比如 Git-Bash）。

![](https://pic3.zhimg.com/v2-eb26731bc04c586c89f691daccf5379e_b.jpg)

执行命令:

正常情况下会输出当前系统上安装的 Linux 系统发行版和对应 的 WSL 版本。因为我之前安装过了，所以输出如下：

```
wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-22.04    Stopped         2
```

然后，继续在命令行中执行如下命令，更新 wsl。

这行命令会将 wsl 更新到最新的内核版本。

检查更新后的版本：

```
wsl --version
WSL 版本： 1.0.0.0
内核版本： 5.15.74.2
WSLg 版本： 1.0.47
MSRDC 版本： 1.2.3575
Direct3D 版本： 1.606.4
DXCore 版本： 10.0.25131.1002-220531-1700.rs-onecore-base2-hyp
Windows版本： 10.0.19045.2311
```

看到 WSL 版本号大于等于 1.0.0.0 就是对的。

然后，再执行如下命令，将默认的 WSL 默认的 Linux 分发版本设为 2。

```
wsl --set-default-version 2
```

### Step 3：安装一个 WSL Linux 发行版

接下来执行：

看看微软为我们提供了哪些可用 Linux 发行版。输出如下图。

![](https://pic2.zhimg.com/v2-540e00203275a0247c9c95e680b6c08d_b.jpg)

输出的 8 个发行版中，排在第一的是没有注明版本号的 Ubuntu，这也是目前 WSL 默认的发行版，如果你在获取 Linux 发行版时没有指定发行版信息，就会给你安装这个。当前默认的 Ubuntu 版本为最新的 LTS 版本，即 22.04.1（jammy），估计再过两年会变成 24.04。

第二个没有注明版本信息的是 Debian，当前版本为 11.5（bullseye）。

现在就可以通过执行：

来安装一个 Linux 发行版了。

如果你执行 `wsl -l --online` 命令时就遇到如下网络问题。

```
wsl -l --online
无法从'https://raw.githubusercontent.com/microsoft/WSL/master/distributions/Dist
ributionInfo.json'提取列表分发。无法解析服务器的名称或地址
Error code: Wsl/WININET_E_NAME_NOT_RESOLVED
```

或者 `wsl --insall -d <发行版本>` 执行太慢。不慌，这都是网络问题，我们可以直接从 Windows 应用商店安装想要的发行版。

打开 Windows 应用商店，搜索想装的发行版。我本次想装的是 Debian。

![](https://pic1.zhimg.com/v2-90306f1a1daaa1b72fb26488d1b60064_b.jpg)

点击获取就可以下载了。下载安装完成后点击“打开”即可开启发行版。第一次打开会弹出窗口进行初始化操作，并让你设置账户的密码。

![](https://pic4.zhimg.com/v2-0ebe9a468ee922214952d6670aa84eaf_b.jpg)

账户密码设置完后就会进入发行版系统。现在就可以探索 WSL Linux 了。

输入 `logout` 可关闭当前窗口。

### 使用

### 1\. 进入发行版

到了这一步，所安装发行版的图标就会出现在 Windows 启动菜单中，点击对应图标或在终端命令行中输入 :

就可以进入发行版系统了。`-d` 选项用于指定要进入的目标发行版。

如果你安装的是 Ubuntu-22.04，直接输入：

不用 `-d` 选项，也可以进入，因为 Ubuntu-22.04 是目前 WSL 默认的发行版。

### 2\. 退出发行版

在发行版的命令行中执行 `exit` 或 `logout` 即可退出当前发行版。

### 3\. 查询发行版的状态

退出发行版命令行后或者另外打开一个命令行终端，执行：

```
wsl -l -v
  NAME            STATE           VERSION
* Ubuntu-22.04    Stopped         2
  Debian          Stopped         2
```

即可查看当前有发行版的运行状态。我这里显示 Ubuntu-22.04 和 Debian 都没在运行。

### 4\. 关闭发行版

前面用 `exit` 或 `logout` 只能推出 wsl 发行版的交互式 shell，并不一定会关闭发行版。虽然 WSL 现在支持 systemd 了，但新安装的发行版默认使用的还不是 systemd，所以也不能在 wsl 发行版中执行 `sudo poweroff` 或 `sudo shutdown` 命令来关闭发行版系统。

尝试执行`poweroff` 或 `shutdown` 会报错：

```
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```

在使用 `exit` 或 `logout` 后，我们可以在 Windows 终端中执行 `wsl --shutdown` 或 `wsl -t` 来关闭后台正在运行的发行版。

-   关闭指定的单个发行版：`wsl -t 发行版名称`。
-   关闭所有正在运行的发行版：`wsl --shutdown`。

### 5\. 移除发行版

对于不再需要的 wsl 发行版，我们可以将其移除，以节省磁盘空间。执行：

即可移除指定的发行版。

### 6\. 为发行版开启 systemd

先进入发行版。

执行如下命令：

```
sudo sh -c 'echo "[boot]\nsystemd=true" >> /etc/wsl.conf'
```

即在发行版的 `/etc` 目录下创建一个 `wsl.conf` 文件，并输入了如下配置：

然后退出发行版，关闭发行版，再进入。执行如下命令：

```
ps --no-headers -o comm 1
```

如果输出的是 “systemd”，说明 systemd 已开启成功。

### 后记

使用 WSL 2 差不多两周了，感觉 WSL 才是最好用的 Linux 发行版。如果阅读量超过 1000，我会继续更新一篇关于 WSL 使用的小技巧。

[喜迎 WSL 1.0 发布，Windows 10 的 WSL 2 也可以用 systemd 了，再水一篇安装教程](https://zhuanlan.zhihu.com/p/586126933)