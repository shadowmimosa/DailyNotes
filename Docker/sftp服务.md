<font size=4 face='楷体'>

## Docker with SFTP

使用以下命令：

```bash
docker run -d \
  -v  /data/upload:/home/foo/upload \ # 挂载本地目录到容器内的指定路径
  -p 2222:22 \ # 将容器的22端口映射到本地的2222端口
  -e LANG=C.UTF-8 \ # 设置容器内的环境变量 LANG 为 C.UTF-8
  -e SFTP_USERS=foo:pass:::upload \ # 设置SFTP用户，包括用户名、密码、上传目录等信息
  --name sftp \ # 为容器指定一个名称为 sftp
  atmoz/sftp # 使用 atmoz/sftp 镜像运行容器
```

此时，容器已经启动，可以正常连接
上传时可能会报错 `permission is not allowed`，需要修改本来目录权限解决

```bash
chmod -R 777 /data/upload
```

### 文件乱码问题

- `atmoz/sftp` 容器默认是 `POSIX` 编码，需要 `-e LANG=C.UTF-8` 指定为 `UTF-8` 编码
- XShell 的 XFTP 默认编码可能不是`UTF-8`，需要设置一下

### Reference
[SFTP](https://github.com/atmoz/sftp)
[Sftp 中文件名乱码](https://blog.csdn.net/weixin_43441190/article/details/126084325)
[解决 docker 容器中文乱码，修改 docker 容器编码格式](https://article.itxueyuan.com/3ml64)
[Docker——搭建 SFTP](https://www.cnblogs.com/wangyang0210/p/14553135.html)

**2023.12.08**
