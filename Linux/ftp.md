<font size=4 face='楷体'>

## Linux 开启 ftp 服务

- 安装 ftp

  ```shell
  sudo apt install vsftpd
  ```

- 启动 ftp

  ```shell
  service vsftpd start
  service vsftpd status # 查看状态
  ```

- 注意
  1. 云服务器安全组要开启
  2. 阿里云 ftp 被动模式问题主动模式
     修改配置
  ```
  listen=NO            -> listen=YES
  listen_ipv6=YES    ->listen_ipv6=NO
  ```

### Reference

[Linux 开启 ftp 服务及基本使用方法](https://www.jianshu.com/p/2f4d6f71b4c8)
[记第一次阿里云安装 ftp（一定要配置对应的安全组规则）](https://blog.csdn.net/nidunlove/article/details/85165739?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)
[阿里云 centos 下搭建 vsftpd，被动模式出现的问题](https://blog.csdn.net/ridicuturing/article/details/80308053)

**2020.03.28**
