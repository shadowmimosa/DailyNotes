<font size=4 face='楷体'>

## uWSGI 配置说明

### 启动报错

> Listen queue size is greater than the system max net.core.somaxconn (128)

如字面意思，监听端口超过了系统默认设置 128, 那么:

- 修改 uwsgi 配置，listen 小于 128
  ```shell
  listen = 127
  ```
- 修改系统设置
  ```shell
  echo 1024 > /proc/sys/net/ipv4/tcp_max_syn_backlog
  ```

## Reference

[Listen queue size is greater than the system max net.core.somaxconn (128)解决](https://blog.csdn.net/yaolong336/article/details/78523442)
