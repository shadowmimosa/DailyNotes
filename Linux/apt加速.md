<font size=4 face='楷体'>

## Ubuntu apt 加速

### apt-fast

- 安装软件
  ```bash
  sudo apt-get install axel
  sudo axel -o /usr/bin/apt-fast http://www.mattparnell.com/linux/apt-fast/apt-fast.sh
  sudo chmod +x /usr/bin/apt-fast
  ```
- 使用
  之前的 apt 直接换成 apt-fast 即可
  ```bash
  sudo apt-get install xxx
  # 替换为
  sudo apt-fast install xxx
  ```

### 换源

[阿里云镜像开源社区镜像站](https://developer.aliyun.com/mirror/)
[网易开源镜像站](http://mirrors.163.com/.help/ubuntu.html)
[阿里云镜像开源社区镜像站](https://www.jianshu.com/p/24192990a891)
[清华大学开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)
[中科大开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)

```bash
/etc/apt/sources.list
```

替换默认的

```bash
archive.ubuntu.com
```

为

```bash
mirrors.aliyun.com
```

### Reference

[apt 加速神器 apt-fast](https://www.jianshu.com/p/24192990a891)
[Ubuntu apt-get 国内镜像源替换](https://blog.csdn.net/qq_21095573/article/details/99736630)
[Ubuntu 镜像](https://developer.aliyun.com/mirror/ubuntu)

**2020.10.29**
