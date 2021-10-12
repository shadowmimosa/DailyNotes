<font size=4 face='楷体'>

## wsl 连接远程 docker

在 wsl 中尝试挣扎之后发现，还是没办法脱离 docker for Windows 单纯的在 wsl 中运行 docker  
所以退而求其次，连接远程 docker, 作为 docker client 使用

- 修改远程 docker 设置，开启 tcp 连接  
   在 /lib/systemd/system/docker.service 中增加 tcp 连接
  ```shell
  # 原始
  ExecStart=/usr/bin/dockerd -H unix:///var/run/docker.sock -H fd:// --containerd=/run/containerd/containerd.sock
  # 修改后 注意 `port` 为要开启的端口
  ExecStart=/usr/bin/dockerd -H unix:///var/run/docker.sock -H tcp://0.0.0.0:port -H fd:// --containerd=/run/containerd/containerd.sock
  ```
- 本地 wsl 连接远程 docker

  ```shell
  # 导入环境变量
  export DOCKER_HOST=tcp://<your docker server ip>:port
  ```

至此，本地 wsl 就是作为 docker client 使用

### Reference

[windows 子系统 \* Docker is not running 问题](https://www.jianshu.com/p/95742c89a3ba)

**2019.10.31**
