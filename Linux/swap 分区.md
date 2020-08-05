<font size=4 face='楷体'>

## 开启 swap 分区

- 创建交换文件

  ```bash
  dd if=/dev/zero of=/data/swap bs=1024 count=8388616
  ```

  此文件的大小是 count 的大小乘以 bs 大小，上面命令的大小是 8GB

- 制作分区格式文件

  ```bash
  mkswap /data/swap
  ```

- 修改内核参数

  ```bash
  cat /proc/sys/vm/swappiness
  sysctl -a | grep swappiness
  sysctl -w vm.swappiness=60
  ```

  vm.swappiness 设定为 0，即永不使用 swap 分区
  若 vm.swappiness 为 0 则根据实际需要调整成 30 或者 60
  若想永久修改，则编辑/etc/sysctl.conf 文件

- 挂载分区

  ```bash
  swapon /data/swap
  echo "/data/swap swap swap defaults    0  0" >> /etc/fstab
  ```

- 关闭 swap 分区
  ```bash
  swapoff /data/swap
  swapoff -a >/dev/null
  ```

### Reference

[Centos7 开启 swap 分区](http://www.mamicode.com/info-detail-2688008.html)
[SWAP虚拟内存配置](https://blog.csdn.net/wo18237095579/article/details/80363397)  

**2020.08.05**
