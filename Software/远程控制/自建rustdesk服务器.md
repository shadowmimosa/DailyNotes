<font size=4 face='楷体'>

## 自建 rustdesk 中继服务器

[rustdesk](https://github.com/rustdesk/rustdesk/tree/master) 是一个功能齐全的开源远程控制替代方案，可通过最少的配置实现自托管和安全性。

### Docker 搭建 rustdesk 中继服务器

```bash
# 下载镜像
docker image pull rustdesk/rustdesk-server

# 运行 hbbs
docker run --name hbbs -p 21115:21115 -p 21116:21116 -p 21116:21116/udp -p 21118:21118 -v /opt/volumes/rustdesk/hbbs/root:/root -td rustdesk/rustdesk-server hbbs -r 47.11.11.11 -m youxiang@163.com -k key123456

# 运行 hbbr
docker run --name hbbr -p 21117:21117 -p 21119:21119 -v /opt/volumes/rustdesk/hbbr/root:/root -td rustdesk/rustdesk-server hbbr -m youxiang@163.com -k key123456
```

`47.11.11.11`: 这个要换成对应的公网 ip
`youxiang@163.com`: 这个要换成自己的邮箱
`key123456`: 换成自定义的 key, 用于 rustdesk 的加密链接

Rustdesk 需要开放 21115-21119 端口才能正常运行

```bash
# 开放防火墙端口
firewall-cmd --zone=public --add-port=21115-21119/tcp --permanent
firewall-cmd --zone=public --add-port=21116/udp --permanent
# 重启防火墙
firewall-cmd --reload
# 端口是否开放
firewall-cmd --list-ports
```

下载对应的[客户端软件](https://github.com/rustdesk/rustdesk/releases/), 填写 ID 服务器地址和 Key 即可运行

### Reference

[Docker 搭建 rustdesk 中继服务器](https://zhuanlan.zhihu.com/p/638622475)

**2023.10.07**
