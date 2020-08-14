<font size=4 face='楷体'>

## docker 安装 redis 并启用认证

启动容器带认证

```bash
docker run --name myredis -p 6379:6379 -d --restart=always redis:latest redis-server --appendonly yes --requirepass "root123456"
```

```
-p 6379:6379 :将容器内端口映射到宿主机端口(右边映射到左边)
redis-server –appendonly yes : 在容器执行redis-server启动命令，并打开redis持久化配置
requirepass "your passwd" :设置认证密码
–restart=always: 随docker启动而启动
```

### Reference

[docker 安装官方 Redis 镜像并启用密码认证](https://www.cnblogs.com/Samuel-Leung/p/12316079.html)

**2020.08.13**
