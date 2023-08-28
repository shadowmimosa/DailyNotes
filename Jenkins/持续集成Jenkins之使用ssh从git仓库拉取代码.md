<font size=4 face='楷体'>

## 持续集成 Jenkins 之使用 ssh 从 git 仓库拉取代码

### 假设

（1）[Jenkins](https://so.csdn.net/so/search?q=Jenkins&spm=1001.2101.3001.7020)所在的服务器是 Server-1, 公钥是 Server-1-public-key, 私钥是 Server1-1-private-key

（2）git 本地仓库所在的服务器是 Server-2

### 分析

要在 Jenkins 管理界面上, 通过 ssh, 从本地[gitlab](https://so.csdn.net/so/search?q=gitlab&spm=1001.2101.3001.7020)上拉取代码, 则参照 ssh 登录流程, 需要将 Server-1 的公钥, 添加到 git 仓库, 可以对仓库进行管理, 比如 pull 或 push；另外由于是在 Jenkins 界面上进行执行, 则需要将 Server-1 的私钥, 添加到凭据, 用于 git 代码的拉取

### 具体执行步骤

- 将 Server-1, 公钥是 Server-1-public-key, 添加到需要管理的 git 仓库

  入口：首先进入到：某一仓库, 点击"Settings"

![](./持续集成Jenkins之使用ssh从git仓库拉取代码/ad9ee3f640fc36cbc83e6212a3d62ef8)

2、Jenkins 界面上, 将 Server-1 的[私钥](https://so.csdn.net/so/search?q=%E7%A7%81%E9%92%A5&spm=1001.2101.3001.7020), 添加到凭据类型：SSH Username with private key

入口：登录进入 Jenkins 管理界面, 点击“系统管理”-》“管理凭据”

![](./持续集成Jenkins之使用ssh从git仓库拉取代码/ca264367fc511939d19254512b7782ec)

![](./持续集成Jenkins之使用ssh从git仓库拉取代码/baa0f74f65d4d621a56becfeed51be71)

3、创建一个任务进行测试, 测试是否能拉取代码

![](./持续集成Jenkins之使用ssh从git仓库拉取代码/1a9d8391af1a3660fc53c6f5401d7935)

![](./持续集成Jenkins之使用ssh从git仓库拉取代码/6ab1be680d05fad8a107ef69474b3aa1)执行完毕后, 拉取成功, 拉取到工作空间下, 比如：/var/lib/jenkins/workspace/test_git

![](./持续集成Jenkins之使用ssh从git仓库拉取代码/715ea0130efa49905981b5f2a9f1f99b)

### 报错

> Jenkins 新建任务时，输入远程仓库地址设置，选择凭证后一直提示连不上
> jenkins stderr: No ECDSA host key is known for gitee.com and you have requested strict checking. Host key verification failed.

jenkins 是 docker 内部署的话
需要在 jenkins 的容器里 执行以下命令访问 git 上的仓库地址，把 git 的主机添加到/root/.ssh/known_hosts (执行命令前 known_hosts 这个文件是不存在的)

### Reference

[持续集成 Jenkins 之使用 ssh 从 git 仓库拉取代码](https://blog.csdn.net/jinli5621/article/details/121101980)
[Jenkins新建任务时，输入远程仓库地址设置，选择凭证后一直提示连不上](https://www.cnblogs.com/yitian395/p/16824436.html)

**2023.03.15**
