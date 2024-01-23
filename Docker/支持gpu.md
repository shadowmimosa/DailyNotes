<font size=4 face='楷体'>

## Docker 容器中使用 GPU

> docker 版本在 19.03 及以上后，nvidia-container-toolkit 进行了进一步的封装，在参数里直接使用--gpus "device=0" 即可

意思是 docker 19.03 后不需要安装 `nvidia-docker` 实测 docker 20 版本最后还是安装了 nvidia-docker

```bash
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo
yum clean expire-cache
yum install -y nvidia-docker2
systemctl restart docker

# 测试运行
docker run -it --rm --gpus all centos nvidia-smi
```

## Reference

[Docker 使用 GPU](https://blog.csdn.net/weixin_38420154/article/details/123993221)
[centos 中 docker:Error response from daemon: could not select device driver ““ with capabilities: gpu](https://blog.csdn.net/shuolingzhou/article/details/120633329)
[CentOS 7.9 上安装 Nvidia 驱动和 docker](https://zhuanlan.zhihu.com/p/354842414)

**2022.07.20**
