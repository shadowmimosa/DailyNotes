# ddns-go 完整部署指南（LXC/VM 双方案）

## 部署方式选择

### 1. LXC容器部署（推荐）
**优势：**
- 资源占用少，启动快
- 易于管理和备份
- 网络配置简单

**配置步骤：**
```bash
# 创建Ubuntu/Debian LXC容器
pct create 200 local:vztmpl/ubuntu-22.04-standard_22.04-1_amd64.tar.zst \
  --memory 512 --swap 0 --cores 1 --net0 name=eth0,bridge=vmbr0,ip=dhcp \
  --storage local-lvm --rootfs 8

# 启动容器
pct start 200

# 进入容器
pct enter 200
```

### 2. VM虚拟机部署
适合需要完整操作系统环境或有特殊网络需求的场景。

## ddns-go安装配置

### 方式一：直接安装
```bash
# 下载最新版本
wget https://github.com/jeessy2/ddns-go/releases/download/v5.6.0/ddns-go_5.6.0_linux_x86_64.tar.gz

# 解压并安装
tar -zxvf ddns-go_5.6.0_linux_x86_64.tar.gz
chmod +x ddns-go
sudo mv ddns-go /usr/local/bin/

# 创建systemd服务
sudo tee /etc/systemd/system/ddns-go.service > /dev/null <<EOF
[Unit]
Description=DDNS-GO
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/ddns-go -l :9876 -f 300
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# 启动服务
sudo systemctl enable ddns-go
sudo systemctl start ddns-go
```

### 方式二：Docker部署
```bash
# 安装Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# 运行ddns-go容器
docker run -d \
  --name ddns-go \
  --restart=unless-stopped \
  -p 9876:9876 \
  -v /opt/ddns-go:/root \
  jeessy/ddns-go:latest
```

## 网络配置最佳实践

### 1. 端口配置
```bash
# 开放防火墙端口（如果启用了防火墙）
ufw allow 9876/tcp

# PVE主机防火墙配置
# 在PVE web界面: 数据中心 -> 防火墙 -> 添加规则
# 动作: ACCEPT, 协议: TCP, 端口: 9876
```

### 2. 网络模式选择
- **桥接模式**：容器获得独立IP，适合大多数场景
- **NAT模式**：通过端口转发访问，适合IP资源受限场景

### 3. 内网穿透配置
```bash
# 如果需要外网访问管理界面，可配置反向代理
# 使用nginx proxy manager或直接配置nginx
```

## 配置优化建议

### 1. 基础配置
访问 `http://容器IP:9876` 进行web配置：

- **更新间隔**：建议300-600秒，避免频繁请求
- **TTL设置**：设置为600秒，平衡解析速度和缓存
- **Webhook**：配置状态通知到微信/钉钉

### 2. 多域名配置
```yaml
# 支持多个DNS服务商和多个域名
domains:
  - name: "home.example.com"
    provider: "cloudflare"
  - name: "nas.example.com" 
    provider: "aliyun"
```

### 3. IP获取策略
- **IPv4**：优先使用接口IP，备用公网IP检测
- **IPv6**：建议启用，支持双栈解析
- **网卡选择**：指定正确的网络接口

## 监控和维护

### 1. 日志管理
```bash
# 查看服务状态
systemctl status ddns-go

# 查看日志
journalctl -u ddns-go -f

# 日志轮转配置
sudo tee /etc/logrotate.d/ddns-go > /dev/null <<EOF
/var/log/ddns-go/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
}
EOF
```

### 2. 备份策略
```bash
# 备份配置文件
cp /root/.ddns_go_config.yaml /backup/

# LXC容器备份
vzdump 200 --compress gzip --storage local
```

### 3. 健康检查
```bash
# 创建检查脚本
cat > /usr/local/bin/ddns-check.sh << 'EOF'
#!/bin/bash
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:9876)
if [ $response -ne 200 ]; then
    systemctl restart ddns-go
    echo "$(date): DDNS-GO restarted" >> /var/log/ddns-check.log
fi
EOF

# 添加到crontab
echo "*/5 * * * * /usr/local/bin/ddns-check.sh" | crontab -
```

## 安全建议

1. **访问控制**：仅允许内网访问管理界面
2. **HTTPS配置**：生产环境建议配置SSL证书
3. **密码安全**：设置强密码保护配置页面
4. **定期更新**：关注版本更新，及时升级

## 故障排查

### 常见问题：
1. **无法获取公网IP**：检查网络连接和防火墙
2. **DNS更新失败**：验证API密钥和域名配置
3. **服务无法启动**：检查端口占用和权限问题

这套配置方案在资源占用、稳定性和可维护性之间取得了良好平衡，特别适合PVE环境使用。

---

**By @Claude**
