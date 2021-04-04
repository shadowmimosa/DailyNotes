<font size=4 face='楷体'>

## yum $ dnf 换源

### 配置方法

这里拿阿里云镜像源举例

-   备份
    ```bash
    mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
    ```
-   下载新的 CentOS-Base.repo 到 /etc/yum.repos.d/
    ```bash
    # CentOS 8
    wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-8.repo
    ```
-   运行 `yum makecache` 生成缓存

### Reference

[阿里源](https://developer.aliyun.com/mirror/centos)
[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/centos/)

**2020.11.27**
