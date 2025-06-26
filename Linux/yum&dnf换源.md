<font size=4 face='楷体'>

## yum $ dnf 换源

### 配置方法

这里拿阿里云镜像源举例

- 备份
  ```bash
  mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
  ```
- 下载新的 CentOS-Base.repo 到 /etc/yum.repos.d/
  ```bash
  # CentOS 8
  wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-8.repo
  # CentOS 7
  wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
  # CentOS 6
  wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-6.repo
  ```
- 清理生成缓存
  较为耗时, 可不执行
  ```bash
  yum clean all
  yum makecache
  ```

### Reference

[阿里源](https://developer.aliyun.com/mirror/centos)
[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/centos/)
[将 CentOS 的 yum 源更换为国内镜像源](https://blog.csdn.net/wudinaniya/article/details/105758739)

**2020.11.27**
