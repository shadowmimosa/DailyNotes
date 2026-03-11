# iStoreOS 部署 Caddy 反向代理指南

> 原文来源：[少数派](https://sspai.com/post/96175)  
> 适用环境：iStoreOS (OpenWrt)，家庭宽带环境（无 80/443 端口）

## 核心优势
相比 Nginx，Caddy 的优势在于：
- **自动 HTTPS**：内置 ACME，自动申请和续期 SSL 证书。
- **配置简洁**：Caddyfile 语法直观，易于管理多服务。
- **插件丰富**：支持多种 DNS 服务商的 API 验证（解决无 80 端口证书申请问题）。

## 1. 环境准备与 Caddy 下载

### 1.1 下载 Caddy
访问 [Caddy 官网下载页](https://caddyserver.com/download)：
1.  选择对应架构（通常是 `linux_amd64` 或 `linux_arm64`）。
2.  **必选插件**：如果你使用腾讯云/DNSPod，必须勾选 `github.com/caddy-dns/tencentcloud`（注意不是 dnspod）。
3.  下载二进制文件。

### 1.2 安装
上传文件到路由器（如 `/usr/bin/caddy`）并赋予执行权限：
```bash
chmod +x /usr/bin/caddy
```

创建配置目录：
```bash
mkdir -p /etc/caddy
touch /etc/caddy/Caddyfile
```

## 2. 配置 Caddyfile

编辑 `/etc/caddy/Caddyfile`，针对家宽环境（端口非 80/443）的配置示例：

### 基础配置模板
```caddy
{
    # 修改默认 HTTP/HTTPS 端口（避开运营商封锁）
    http_port 667
    https_port 668
    
    email your-email@example.com
    
    # 配置 DNS 验证（以腾讯云为例）
    acme_dns tencentcloud {
        secret_id "YOUR_TENCENT_CLOUD_ID"
        secret_key "YOUR_TENCENT_CLOUD_KEY"
    }
}

# 多服务通配符配置
*.example.com:668 {
    # NAS 服务
    @nas host nas.example.com
    handle @nas {
        reverse_proxy 192.168.1.100:5000
    }

    # 路由器后台
    @router host router.example.com
    handle @router {
        reverse_proxy 192.168.1.1:80
    }
    
    # 其他服务...
}
```

> **注意**：
> 1. 访问时需带端口：`https://nas.example.com:668`。
> 2. 域名需在服务商处做泛解析（CNAME `*.example.com` -> `www.example.com`，A 记录 `www` -> 公网 IP）。

## 3. 系统集成

### 3.1 创建自启动脚本
编辑 `/etc/init.d/caddy`：

```bash
#!/bin/sh /etc/rc.common

START=99
USE_PROCD=1

start_service() {
    procd_open_instance
    procd_set_param command /usr/bin/caddy run --config /etc/caddy/Caddyfile
    procd_set_param respawn
    procd_set_param stdout 1
    procd_set_param stderr 1
    procd_close_instance
}
```

启用服务：
```bash
chmod +x /etc/init.d/caddy
/etc/init.d/caddy enable
/etc/init.d/caddy start
```

### 3.2 配置防火墙
在 OpenWrt 防火墙中开放自定义端口（667, 668）。
- **Web 界面**：网络 -> 防火墙 -> 流量规则 -> 打开路由器端口。
- **或者端口转发**：如果 Caddy 部署在主路由，直接开放端口即可；如果部署在旁路由，需主路由转发。

## 4. 维护与排查

- **查看状态**：`/etc/init.d/caddy status`
- **重启服务**：`/etc/init.d/caddy restart`
- **查看日志**：`logread | grep caddy` 或 `logread -f | grep caddy`（实时）

常见错误：
- `bind: address already in use`：端口冲突，检查是否被 uhttpd 或 nginx 占用。
- `acme: error presenting token`：DNS API 配置错误或密钥无效。
