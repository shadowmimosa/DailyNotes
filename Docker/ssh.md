<font size=4 face='楷体'>

## Docker 远程连接

### 容器开启 sshd

- 安装 ssh

  ```bash
  yum install openssh-server
  ```

- 检查运行状态

  ```bash
  ps -e|grep ssh
  ```

- 配置 ssh

  ```bash
  vim /etc/ssh/sshd_config

  # 添加
  PermitRootLogin yes
  ```

- 修改或设置密码

  ```bash
  passwd root
  # 输入新密码 （两次）
  ```

- 启动
  用 systemctl 启动 `service sshd restart` 会报错 `Failed to get D-Bus connection: Operation not permitted`
  需重启容器, 加上权限 `--privileged=true` `docker run -d -name centos7 --privileged=true centos:7 /usr/sbin/init`(未尝试成功)

  用以下方式启动

  ```bash
  /usr/sbin/sshd -D &
  ```

  或报错, 设置公钥私钥对

  ```bash
  ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N ''
  ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''
  ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key -N ''
  ```

### Reference

[VScode 远程连接服务器中 docker 过程及遇到的问题](https://blog.csdn.net/weixin_45131923/article/details/112241194)
[CentOS 下开启 SSH Server 服务](https://www.cnblogs.com/DiDiao-Liang/articles/8283686.html)
[解决：Failed to get D-Bus connection: Operation not permitted](https://www.jianshu.com/p/175b59c2192f)
[docker 开启 ssh 服务](https://blog.csdn.net/nienelong3319/article/details/106796519)
[docker 容器内启动 sshd 启动报错](https://www.cnblogs.com/sharesdk/p/10102936.html)

**2021.11.18**
