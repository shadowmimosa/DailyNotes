<font size=4 face='楷体'>

## FFmpeg 安装

[FFmpeg](https://ffmpeg.org/) 是著名的开源视频处理工具

### 源码

- [Github](https://github.com/FFmpeg/FFmpeg)
- [官方源](https://git.ffmpeg.org/ffmpeg.git)

仓库好像并不提供编译好的版本

### 下载

- [官网](https://ffmpeg.org/download.html)
- [releases](https://ffmpeg.org/releases/)
- [CODEX FFMPEG](https://www.gyan.dev/ffmpeg/builds/)
- [old-releases](https://www.johnvansickle.com/ffmpeg/old-releases/)

### 安装

#### Windows

略

#### CentOS

1. yum 安装
2. 二进制安装
3. 编译安装

```bash
# 5.1 版本举例
wget http://www.ffmpeg.org/releases/ffmpeg-5.1.tar.gz
tar -zxvf ffmpeg-5.1.tar.gz

cd ffmpeg-5.1
./configure --prefix=/usr/local/ffmpeg --enable-openssl --disable-x86asm
make && make install

# 配置环境变量
vi /etc/profile
export PATH=$PATH:/usr/local/ffmpeg/bin
```

若安装过程中出现以下错误

> yasm/nasm not found or too old. Use –disable-yasm for a crippled build.

需要安装 yasm

```bash
wget http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
tar -zxvf yasm-1.3.0.tar.gz
cd yasm-1.3.0
./configure
make && make install

wget http://www.ffmpeg.org/releases/ffmpeg-5.1.tar.gz
tar -zxvf ffmpeg-5.1.tar.gz

cd ffmpeg-5.1
./configure --prefix=/usr/local/ffmpeg --enable-openssl --disable-x86asm

make && make install
```

#### GPU 加速编译安装

FFmpeg 使用 GPU 加速需要自行编译
[FFmpeg for Nvidia](https://developer.nvidia.com/ffmpeg)
[Nvidia Drivers](https://www.nvidia.com/drivers)
[CUDA](https://developer.nvidia.com/cuda-downloads)
[ffmpeg](http://www.ffmpeg.org/download.html)
[ffnvcodec](https://git.videolan.org/git/ffmpeg/nv-codec-headers.git)

```bash
# 安装ffnvcodec
git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git
cd nv-codec-headers && sudo make install && cd –

# 编译ffmpeg


tar -xvf ffmpeg-5.1.1-amd64-static.tar.xz
wget https://www.johnvansickle.com/ffmpeg/old-releases/ffmpeg-5.1.1-amd64-static.tar.xz
cd ffmpeg-5.1/
yum install libx264-devel # --enable-libx264 参数需要
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig # 很重要 不然老是提示h264_cuvid的错误
# cuda 硬编码需要
# cuvid 硬解码需要
./configure --prefix=/usr/local/ffmpeg --disable-x86asm --enable-shared --enable-cuda --enable-cuvid --enable-nvenc --enable-libx264 --enable-gpl

make && make install

ffmpeg -hwaccels # 当出现cuda时，标识当前的ffmpeg version 已支持gpu硬编码
```

### Reference

[如何在 CentOS 7 linux 上安装和使用 FFmpeg](https://cloud.tencent.com/developer/article/2285046)
[LINUX 下，ffmpeg 增加 NVIDIA 硬件编解码的步骤及解决办法](https://blog.csdn.net/quantum7/article/details/82713833)
[VideoProcessingFramework 编译安装使用终极教程](https://blog.csdn.net/cytheria43/article/details/106542756/)
[centos7 ffmpeg gpu 编译安装](https://blog.csdn.net/u010856284/article/details/120885968)

**2022.02.23**
