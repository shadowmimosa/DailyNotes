<font size=4 face='楷体'>

## VNC Server 部署

### 安装和配置

- 安装
  ```bash
  yum install tigervnc tigervnc-server
  ```
- 设置密码
  ```bash
  vncpasswd
  ```
  也可修改密码
- 启动
  ```bash
  vncserver
  ```
  默认配置启动
- 停止
  ```bash
  vncserver -kill :1
  vncserver -kill :1
  ```
  vncserver 只能由启动它的用户来关闭，即时是 root 也不能关闭其它用户开启的 vncserver，只能用 kill 命令暴力杀死进程
- 重启
  ```bash
  service vncserver restart
  ```
- 允许多个客户端同时连接
  ```bash
  vncserver -alwaysshared
  ```

### 无法连接

> 服务器安全组 放通对应 ip 端口

> 检查防火墙状态

- 查看防火墙状态命令
  ```bash
  systemctl status firewalld
  ```
- 开启防火墙命令
  ```bash
  systemctl start firewalld
  ```
- 关闭防火墙命令
  ```bash
  systemctl stop firewalld
  ```

### Reference

[vnc server 配置、启动、重启与连接](https://www.cnblogs.com/wangyuehan/p/9807628.html)
[用 vnc 实现 Windows 远程连接 linux 桌面](http://www.wuwenhui.cn/3914.html)

**2020.09.18**
