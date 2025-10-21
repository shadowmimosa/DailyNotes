# OpenWrt 使用终端挂载共享硬盘

在本篇文章中，我们介绍了如何在 OpenWrt 上使用终端挂载共享硬盘。本例中使用了 R2S 软路由连接外部 SATA 硬盘，通过 USB 2.0 接口进行挂载，速度大约为 30MB/s。由于 R2S 路由器没有提供图形界面配置共享硬盘的选项，因此需要通过终端来进行配置。

---

## 查看挂载信息

首先，可以通过以下命令查看当前系统的磁盘挂载情况：

```bash
root@ImmortalWrt:/etc/samba# df -h
Filesystem                Size      Used Available Use% Mounted on
/dev/root                29.1G    508.4M     28.6G   2% /
tmpfs                   493.7M     22.5M    471.3M   5% /tmp
tmpfs                   512.0K         0    512.0K   0% /dev
/dev/mmcblk0p1           63.0M     15.3M     46.3M  25% /mnt/mmcblk0p1
/dev/sda1                 1.7T    331.1G      1.4T  19% /pm863
```

可以看到，硬盘 `/dev/sda1` 已经挂载在 `/pm863` 目录下。接下来查看系统检查到的硬盘信息，包括未挂载的硬盘。安装 `lsblk` 命令：

```bash
root@ImmortalWrt:/dev# opkg install lsblk
```

安装完成后，使用以下命令查看磁盘信息：

```bash
root@ImmortalWrt:/dev# lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda           8:0    0  1.7T  0 disk
└─sda1        8:1    0  1.7T  0 part /pm863
mmcblk0     179:0    0 29.7G  0 disk
├─mmcblk0p1 179:1    0   64M  0 part /mnt/mmcblk0p1
└─mmcblk0p2 179:2    0 29.6G  0 part /
```

通过 `lsblk` 命令可以查看磁盘分区和挂载点。

---

## Samba4 注册用户

为了使共享文件夹对特定用户可访问，我们需要在 OpenWrt 中创建一个 Samba 用户。首先安装 `shadow-common` 和 `shadow-useradd`：

```bash
root@ImmortalWrt:/etc/samba# opkg install shadow-common
root@ImmortalWrt:/etc/samba# opkg install shadow-useradd
```

安装完成后，添加新用户 `hongda`：

```bash
root@ImmortalWrt:/etc/samba# useradd hongda
root@ImmortalWrt:/etc/samba# passwd hongda
Changing password for hongda
New password:
Bad password: similar to username
Retype password:
passwd: password for hongda changed by root
```

然后注册 Samba 用户 `hongda`，并设置 SMB 密码：

```bash
root@ImmortalWrt:/etc/samba# smbpasswd -a hongda
New SMB password:
Retype new SMB password:
Added user hongda.
```

如果需要删除该用户，可以使用以下命令：

```bash
root@ImmortalWrt:/mnt/883dct# smbpasswd -x hongda
Deleted user hongda.
```

---

## Samba4 配置

接下来，我们需要配置 Samba 的共享目录。配置文件路径为 `/etc/samba/smb.conf.template`。在该文件中添加以下共享配置：

```ini
[883-DCT]
    path = /mnt/883dct
    valid users = hongda,@root
    admin users = hongda,@root
    writable = yes
    read only = no
    create mask = 0666
    directory mask = 0755
    browseable = yes
    inherit owner = yes
```

配置完成后，可以通过以下命令校验配置文件的正确性：

```bash
root@ImmortalWrt:/etc/samba# testparm -v
```

如果配置文件无误，重启 Samba 服务：

```bash
root@ImmortalWrt:/etc/samba# service samba4 restart
root@ImmortalWrt:/etc/samba# service samba4 status
running
```

---

## 参考

- [Openwrt 使用终端挂载共享硬盘](https://www.cnblogs.com/hongdada/p/17245528.html)

- [openwrt 上设置 SAMBA4 共享，并且指定用户密码](https://blog.csdn.net/selar888/article/details/116382598)

- [Openwrt 下折腾 Samba4 配置](https://blog.csdn.net/kk380446/article/details/114213014)

- [OpenWrt 使用终端挂载共享硬盘](https://www.cnblogs.com/hongdada/p/17245528.html#openwrt-%E4%BD%BF%E7%94%A8%E7%BB%88%E7%AB%AF%E6%8C%82%E8%BD%BD%E5%85%B1%E4%BA%AB%E7%A1%AC%E7%9B%98)

- [查看挂载信息](https://www.cnblogs.com/hongdada/p/17245528.html#%E6%9F%A5%E7%9C%8B%E6%8C%82%E8%BD%BD%E4%BF%A1%E6%81%AF)

- [samba4 注册用户](https://www.cnblogs.com/hongdada/p/17245528.html#samba4%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7)

- [samba4 配置](https://www.cnblogs.com/hongdada/p/17245528.html#samba4-%E9%85%8D%E7%BD%AE)
