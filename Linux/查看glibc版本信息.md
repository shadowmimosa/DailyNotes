<font size=4 face='楷体'>

## 查看 glibc 版本信息

-   CentOS
    简单信息

    > rpm -qa | grep glibc

    详细信息

    > rpm -qi glibc

    其它

    > ls -l /lib/libc.so.6

-   Ubuntu

    > ls -l /lib/i386-linux-gnu/libc.so.6
    > apt-cache show libc6

-   发行版无关方法
    > ldd –version

### Reference

[Linux 查看 glibc 版本信息](https://blog.csdn.net/xiaoxinyu316/article/details/44834255)

**2021.03.08**
