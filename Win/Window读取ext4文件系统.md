<font size=4 face='楷体'>

## Window 读取 Ext3/Ext4 文件系统数据

**Linux 支持多种文件系统类型，包括 ext3、vfat、jffs、romfs 和 nfs 等，Ext4/Ext3 为 Linux 系统的广泛格式；而 Window 系统的广泛格式是 NTFS，FAT32 等**。

NAS 服务器大都是 Linux 系统，自然在硬盘上保存的数据一般都是 Ext4，如下直接将 NAS 服务器的磁盘安装在 Window 系统是不能直接读取数据，本文笔者给大家介绍几个软件在 Window 读取 Ext3/Ext4 文件系统数据。

## 1 Linux Reader

Linux Reader 下载地址：[https://www.diskinternals.com/linux\-reader/](https://www.diskinternals.com/linux-reader/)

DiskInternals Linux Reader 是一款非常好用的免费软件，它可以直接在 Windows 系统下对 Linux 分区文件进行读取，不仅如此，还可以直接查看保存在 Ext4、Ext3、Ext2、ReiserFS 和 HFS 等 Linux 文件系统下的文件。

![](https://pic1.zhimg.com/v2-00cb39b5ed22b3ad025b900f39f40adc_b.jpg)

Linux Reader 使用起来很简单，我们只需要打开 Linux Reader，就可以在 Window 系统下读取 Ext3/Ext4 文件格式内容，在窗口中会列出所有的磁盘分区。不管是 Window 系统的文件格式还是 Linux 的文件格式都能显示并且都能操作。

![](https://pic4.zhimg.com/v2-83d6bd57757a7ea3ef4d2f5ebf60e1a7_b.jpg)

打开后就可以管理里面的文件了，像我这里根分区的一些文件。

如果想要将某个文件/文件夹保存到 Windows 系统中一些地方，只需要点击右键，选择‘Save’，然后根据提示保存到 Window 系统格式的某个磁盘下。

## 2 Ext2Read

Ext2Read 下载地址：[https://sourceforge.net/projects/ext2read/](https://sourceforge.net/projects/ext2read/) 或者 [这里](http://ext2read.blogspot.com/)

[https://github.com/finera/ext2read](https://link.zhihu.com/?target=https%3A//github.com/finera/ext2read)

Ext2Read 是一个 Windows 读取 Linux 分区工具，可以实现在 Windows 系统中访问读取 Linux 系统磁盘分区文件的功能，支持 ext2、ext3 或 ext4、LVM2 格式的文件系统，不仅本地磁盘，还支持 USB 可移动磁盘。值得注意的，使用该软件需要使用管理员身份，该软件只会扫描 Linux 的文件格式，不会扫描 Window 的系统的文件格式。

![](https://pic3.zhimg.com/v2-cd07ae4e10bf87eb1b0964d81b4b331a_b.jpg)

对于上述两款软件而言，可根据实际需求选择，Ext2Read 虽然小巧，但是功能相比 Linux Reader 就逊色多了。

### Reference

[Window 读取 Ext3/Ext4 文件系统数据](https://zhuanlan.zhihu.com/p/435004060)

**2023.09.19**
