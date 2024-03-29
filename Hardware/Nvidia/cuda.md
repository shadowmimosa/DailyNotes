<font size=4 face='楷体'>

## CentOS 8 安装 CUDA

### 安装显卡驱动

在[这里](https://www.nvidia.cn/Download/index.aspx?lang=cn)搜索合适的驱动, 复制下载链接, 形如 `https://us.download.nvidia.com/XFree86/Linux-x86_64/470.74/NVIDIA-Linux-x86_64-470.74.run`

下载安装

```bash
wget https://us.download.nvidia.com/XFree86/Linux-x86_64/470.74/NVIDIA-Linux-x86_64-470.74.run

# 确保安装内核版本一致
yum list | grep kernel-devel
yum -y install kernel-devel
yum -y install gcc dkms
yum -y install gcc
 
chmod u+x NVIDIA-Linux-x86_64-470.74.run

# 安装报错会自动生成禁用 nouveau 的配置文件
# /etc/modprobe.d/nvidia-installer-disable-nouveau.conf
# # generated by nvidia-installer
# blacklist nouveau
# options nouveau modeset=0
./NVIDIA-Linux-x86_64-470.74.run --kernel-source-path=/usr/src/kernels/4.18.0-338.el8.x86_64/

# 重新建立 initramfs image 文件
mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).img.bak
dracut /boot/initramfs-$(uname -r).img $(uname -r)

# 重启生效
reboot

# 再次安装
./NVIDIA-Linux-x86_64-470.74.run --kernel-source-path=/usr/src/kernels/4.18.0-338.el8.x86_64/
```

如报错 `The CC version check failed`

```bash
# 查看 GCC 版本
/usr/bin/gcc*

# 指定报错中 kernel 的构建 GCC 版本
export CC=gcc-7

# 再次安装
./NVIDIA-Linux-x86_64-470.74.run --kernel-source-path=/usr/src/kernels/4.18.0-338.el8.x86_64/
```

验证是否安装

```bash
nvidia-smi
```

### 安装 CUDA

[CUDA Toolkit 11.4 Update 2 Downloads](https://developer.nvidia.cn/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=CentOS&target_version=8&target_type=rpm_network)

```bash
dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo
dnf clean all
dnf -y module install nvidia-driver:latest-dkms
dnf -y install cuda
```

如报错形如

```text
 Problem 8: package nvidia-driver-3:470.57.02-1.el8.x86_64 requires nvidia-kmod-common = 3:470.57.02, but none of the providers can be installed
  - package nvidia-xconfig-3:470.57.02-1.el8.x86_64 requires nvidia-driver(x86-64) = 3:470.57.02, but none of the providers can be installed
  - package nvidia-kmod-common-3:470.57.02-1.el8.noarch requires nvidia-kmod = 3:470.57.02, but none of the providers can be installed
  - cannot install the best candidate for the job
  - package kmod-nvidia-470.57.02-4.18.0-305.10.2-3:470.57.02-3.el8_4.x86_64 is filtered out by modular filtering
  - package kmod-nvidia-470.57.02-4.18.0-305.12.1-3:470.57.02-3.el8_4.x86_64 is filtered out by modular filtering
  - package kmod-nvidia-470.57.02-4.18.0-305.17.1-3:470.57.02-3.el8_4.x86_64 is filtered out by modular filtering
  - package kmod-nvidia-470.57.02-4.18.0-305.19.1-3:470.57.02-3.el8_4.x86_64 is filtered out by modular filtering
  - package kmod-nvidia-470.57.02-4.18.0-305.7.1-3:470.57.02-3.el8_4.x86_64 is filtered out by modular filtering
  - nothing provides dkms needed by kmod-nvidia-latest-dkms-3:470.57.02-1.el8.x86_6
```

则安装 dkms

```
yum -y install epel-release
yum -y install --enablerepo=epel dkms
```

验证是否安装

```bash
nvcc -V
```

### 安装 cuDNN

在[cuDNN](https://developer.nvidia.com/cudnn)下载合适的版本
cuDNN 不需要选择平台

```bash
sudo cp cuda/include/cudnn*.h /usr/local/cuda/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
```

[NVIDIA cuDNN](https://developer.nvidia.cn/zh-cn/cudnn)

### Reference

[Centos8.1 安装 NVIDIA 显卡驱动及基于 docker 搭建 tensorflow 开发环境](https://blog.csdn.net/zhangsh87/article/details/106  178825/)
[Centos 8 GPU 驱动配置](https://zhuanlan.zhihu.com/p/354307973)
[安装显卡驱动报错：”THE CC VERSION CHECK FAILED”](https://www.freesion.com/article/4977946340/)
[centos8.2 安装 nvidia 1660s 驱动及 cuda10.2](https://www.cnblogs.com/wq242424/p/13851430.html)
[NVIDIA cuDNN Documentation](https://docs.nvidia.com/deeplearning/cudnn/install-guide/)

**2021.09.25**
