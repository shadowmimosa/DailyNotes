# PVEtools - Proxmox VE 一键配置脚本

> 项目地址：[https://github.com/ivanhao/pvetools](https://github.com/ivanhao/pvetools)  
> 🌟 Stars: 5.2k | 🍴 Forks: 613 | 📄 License: GPL-3.0

## 项目简介

PVEtools 是一个为 Proxmox VE 设计的一键配置脚本工具集，适用于 Debian 9+ 版本。它提供了丰富的功能模块，可以大大简化 PVE 的配置和管理过程，是 PVE 用户必备的管理工具。

## 主要功能

### 🛠️ 核心功能
- **邮件配置**：自动配置邮件服务，支持告警通知
- **Samba 共享**：一键配置 SMB/CIFS 文件共享，支持回收站功能
- **NFS 配置**：网络文件系统配置，支持高性能文件共享
- **ZFS 优化**：设置 ZFS 最大内存使用，优化性能
- **嵌套虚拟化**：启用嵌套虚拟化支持
- **Docker 安装**：集成 Docker 环境，包含 Portainer Web 界面
- **PCI 直通**：硬件直通配置，支持显卡、网卡等设备

### 🎨 界面增强
- **温度监控**：Web 界面实时显示 CPU、主板温度和频率
- **黑暗模式**：为 PVE 界面提供暗色主题
- **去除订阅提示**：移除企业版订阅提醒

### ⚡ 性能优化
- **CPU 省电模式**：节能配置，降低功耗
- **内存释放**：清理系统内存缓存
- **ROOT 分区扩展**：自动扩展系统分区空间
- **USB 系统盘优化**：针对 USB 启动的性能优化

### 🌐 网络工具
- **APT 国内源**：配置国内软件源，加速更新
- **DNS 配置**：自定义 DNS 服务器设置
- **BBR/BBR+ 加速**：网络加速优化
- **SpeedTest**：网络速度测试

### 📊 管理工具
- **局域网扫描**：扫描局域网设备
- **虚拟机备份**：自动备份 VM 配置文件
- **Chroot 环境**：Alpine Linux 轻量级容器环境
- **硬盘映射**：物理硬盘直通到虚拟机

## 安装使用

### 中文用户

```bash
apt update && apt -y install git && git clone https://github.com/ivanhao/pvetools.git
cd pvetools
./pvetools.sh
```

### English Users

```bash
export LC_ALL=en_US.UTF-8
apt update && apt -y install git && git clone https://github.com/ivanhao/pvetools.git
cd pvetools
./pvetools.sh
```

> 如果更新出错，可以先删除企业源：`rm /etc/apt/sources.list.d/pve-enterprise.list` 然后重试

### 运行方式

进入 pvetools 目录后，运行：
```bash
chmod +x pvetools.sh
./pvetools.sh
```

## 版本历史

### v2.4.0 (2024.02.08)
- 修复有些功能还原配置时出现问题（温度显示、去除订阅等）
- 修复配置apt国内源、安装配置VIM可导致原配置文件被覆盖

### v2.3.9 (2023.10.19)
- 增加 PVE 8 的支持
- 优化英文语言的显示

### v2.3.6 (2023.02.16)
- 合并网友提交的 PCI 直通修复

### v2.3.5 (2022.09.14)
- 修复 Docker 无法安装的问题，更换 Alpine 的安装源

### v2.3.2 (2022.07.14)
- 温度显示上方增加 CPU 频率显示

### v2.3.1 (2022.07.13)
- 调整省电模式 powersave 为 conservative

### v2.3.0 (2022.05.30)
- 修复 PVE7 (Debian 11) 后 security 更新源地址格式变动的影响
- 添加 PVE7 以上版本配置硬件直通里的参数 `iommu=pt pcie_acs_override=downstream`
- 增加去除订阅提示的修复

## 功能详解

### 📧 邮件配置
- 自动配置 Postfix 邮件服务
- 支持 SMTP 认证
- 配置时选择 "Internet Site" 并保持其他默认设置

### 🗂️ Samba 共享配置
- 一键创建 SMB/CIFS 共享文件夹
- 自动配置用户权限和访问控制
- 支持回收站功能，误删文件可恢复
- 删除共享时自动还原原始权限

### 🌡️ 温度监控
- 在 PVE Web 界面显示实时温度
- 支持 CPU、主板、硬盘温度监控
- 显示 CPU 频率信息
- 界面高度自适应

### 🐋 Docker 集成
- 一键安装 Docker 环境
- 包含 Portainer Web 管理界面
- 配置国内镜像源
- 支持容器迁移和管理

### 🎮 硬件直通
- PCI 设备直通配置
- 支持显卡、网卡等硬件
- 提供 N卡 vBIOS 提示功能
- 适配不同 PVE 版本的配置参数

### 🗄️ ZFS 优化
- 设置 ZFS ARC 最大内存
- 防止 ZFS 占用过多系统内存
- 优化系统整体性能

## 注意事项

### ⚠️ 使用建议
1. **系统要求**：Debian 9+ / Proxmox VE 6+
2. **权限要求**：需要 root 权限运行
3. **备份重要**：配置前建议备份重要数据和配置文件
4. **网络环境**：确保能正常访问 GitHub 和软件源
5. **分步操作**：建议分步骤测试，避免一次性配置所有功能

### 🔧 常见问题
1. **更新失败**：删除企业源 `/etc/apt/sources.list.d/pve-enterprise.list`
2. **权限问题**：确保脚本有执行权限 `chmod +x pvetools.sh`
3. **网络问题**：配置国内 APT 源和 Docker 镜像源
4. **版本兼容**：不同 PVE 版本功能支持可能有差异

### 🔄 卸载方法
直接删除 pvetools 文件夹即可，大部分功能支持还原配置。

## 适用场景

### 🏠 家庭用户
- 搭建家庭 NAS 和媒体服务器
- 配置文件共享和远程访问
- 优化功耗和散热管理

### 🏢 小型企业
- 构建虚拟化基础设施
- 配置网络存储和备份
- 设置监控和告警系统

### 🧪 学习实验
- 快速搭建测试环境
- 学习虚拟化技术
- 体验各种网络服务

## 相关资源

- **项目地址**：[https://github.com/ivanhao/pvetools](https://github.com/ivanhao/pvetools)
- **问题反馈**：[GitHub Issues](https://github.com/ivanhao/pvetools/issues)
- **下载地址**：[Releases](https://github.com/ivanhao/pvetools/releases)

## 贡献者

感谢以下贡献者的支持：
- @ivanhao (主要开发者)
- @for5million (PCI 直通修复)
- @justwho
- 以及众多社区贡献者和测试用户

---

> PVEtools 是一个成熟稳定的 Proxmox VE 管理工具，经过长期社区验证，适合各种规模的部署场景。无论是新手入门还是专业运维，都能从中获益。
