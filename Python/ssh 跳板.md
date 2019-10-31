<font size=4 face='楷体'>

## python 启用 ssh 隧道

在 python 中启用 ssh 隧道有两个包可以用，可以看[这里](https://www.cnblogs.com/sch01ar/p/8024380.html)。这里只用了 `sshtunnel`

### 通过 sshtunnel 启用 ssh 隧道

- 首先，安装 sshtunnel

  > pip install sshtunnel

- 连接远程服务器

  ```python
  from sshtunnel import SSHTunnelForwarder

  server = SSHTunnelForwarder(
      ssh_address_or_host=("host", 22), # 远程地址
      ssh_username="root", # ssh 连接的用户名
      ssh_password="password",  # ssh 连接的密码
      remote_bind_address=("127.0.0.1", 6379)) # 这里是连接远程 redis
  server.start()
  # do someting
  server.close() # 关闭连接
  ```

### 通过 ssh 跳板连接远程 redis

这里拿连接远程 redis 举个栗子

```python
import redis
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    ssh_address_or_host=("host", 22), # 远程地址
    ssh_username="root", # ssh 连接的用户名
    ssh_password="password",  # ssh 连接的密码
    remote_bind_address=("127.0.0.1", 6379)) # 这里是连接远程 redis
server.start()
r = redis.Redis(
    host='127.0.0.1',
    port=server.local_bind_port, # 主要是这里，这里的端口是刚才 server 提供的
    db=0,
    decode_responses=True)
server.close() # 关闭连接
```

### Reference

[python 通过 SSHTunnelForwarder 隧道连接 redis](https://blog.csdn.net/sinat_34209942/article/details/89880363)
[python 利用跳板机 ssh 远程连接 redis](https://blog.csdn.net/shirlytm/article/details/79106123)

**2019.10.30**
