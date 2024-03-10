<font size=4 face='楷体'>

## iftop 使用

### 安装

```bash
yum install iftop
```

如果 yum 报错找不到源, 先执行

```bash
yum install epel-release
```

如果 yum 报错找不到 epel 源, 先执行

```bash
wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -ivh epel-release-latest-7.noarch.rpm
# 检查是否安装成功
yum repolist
```

### Reference

[centos8 平台基于 iftop 监控网络流量](http://t.zoukankan.com/architectforest-p-12536971.html)
[No package epel-release available](https://blog.csdn.net/qq_32828933/article/details/88656414)

**2022.06.06**
