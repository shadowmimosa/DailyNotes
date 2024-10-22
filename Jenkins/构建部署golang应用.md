<font size=4 face='楷体'>

## Jenkins 构建部署 Golang 应用

### Go 环境

- 安装 [Go Plugin](https://plugins.jenkins.io/golang/)
- 新增 Go 环境并使用默认的 `Install from golang.org`
- 由于众所周知的网络原因可能需要重新手动安装 Go
  ```bash
  # 宿主机中下载到jenkins工作目录挂载的文件夹中
  $ wget https://dl.google.com/go/go1.18.6.linux-amd64.tar.gz
  ```

### Reference

[jenkins 手动安装Go 构建环境](https://segmentfault.com/a/1190000042635998?sort=votes)

**2023.10.07**
