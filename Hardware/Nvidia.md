<font size=4 face='楷体'>

## Nvidia

[List of Nvidia graphics processing units](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units)
[CUDA](https://en.wikipedia.org/wiki/CUDA)

[科普帖：深度学习中 GPU 和显存分析](https://zhuanlan.zhihu.com/p/31558973)
[深度学习·炼丹入门](https://zhuanlan.zhihu.com/p/23781756)

### 问题解决

#### CentOS 意外断电重启后驱动没有了

```bash
nvidia-smi
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.
```

可能是由于重启服务器, linux 内核升级导致的, 由于 linux 内核升级, 之前的 Nvidia 驱动就不匹配连接了, 但是此时 Nvidia 驱动还在

- 安装 `dkms`

  ```bash
  yum install dkms -y
  ```

- 查看本机连接不上的驱动版本

  ```bash
  ls -l /usr/src/
  ```

  可以看到 `nvidia-470.103.01` 类似的文件, 这其中 `470` 即为 Nvidia 驱动的版本
  如果没有则需要重新安装对应版本的 Nvidia 驱动

- 使用 dkms 重新安装适合驱动

  ```bash
  dkms install -m nvidia -v 470.103.01
  ```

  到了这里, 如果安装成功, 那么此时输入 `nvidia-smi` 就会成功连接了

### Reference

[nvidia-smi 报错：NVIDIA-SMI has failed because it couldn‘t communicate with the NVIDIA driver 原因及避坑解决方案](https://blog.csdn.net/baidu_41617231/article/details/135858658)

**Created On 2021.09.09, Modified on 2024.05.10**
