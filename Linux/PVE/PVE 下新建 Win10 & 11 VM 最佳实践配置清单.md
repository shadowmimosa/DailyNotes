# PVE 下图形化创建 Windows 10 / 11 虚拟机（最佳实践完整步骤）

> 说明：本笔记用于 **Proxmox VE 7/8/9** 的 Web 界面（GUI）一步步创建 Win10/11。  

---

## 0. 前置准备

- 准备好 **Windows 10/11 官方 x64 ISO**（带 UEFI 引导）。  
- 准备好 **VirtIO 驱动 ISO**（从 Fedora virtio-win 下载，版本任意稳定版）。  
- 宿主机存储推荐 **NVMe/SSD（如 990 Pro）**。  
- 规划示例（可按需调整）：
  - vCPU：20 核（1 Socket × 20 Cores）
  - 内存：8 GB
  - 系统盘：64 GB
  - 机器类型：Q35
  - BIOS：OVMF (UEFI)

---

## 1. 在 PVE GUI 新建虚拟机（Create VM 向导）

**路径**：左侧选择节点 → 右上角 **Create VM**

### 1.1 General
- Node：选择你的节点  
- VM ID/Name：自定义  
- Start at boot：可勾选  
- QEMU Guest Agent：建议勾选（后续 Windows 内安装 Agent 后生效）

### 1.2 OS
- Use CD/DVD disc image file (iso)：选择 **Windows ISO**  
- Guest OS：Microsoft Windows  
- Version：Win10/Win11 x64（接近的即可）

### 1.3 System
- Graphic card：默认（后续可调）  
- **Machine**：选 **q35**  
- **BIOS**：选 **OVMF (UEFI)**  
- **EFI Disk**：勾选（放在快速存储）  
- Secure Boot：
  - Win10：建议 **关闭**（兼容性最佳）
  - Win11：可 **开启**（如需 TPM + Secure Boot 满足安装要求）
- SCSI Controller：**VirtIO SCSI (single)**

### 1.4 Hard Disk
- Bus/Device：**SCSI**  
- Storage：选你的存储（SSD/NVMe）  
- Disk size：如 64GB  
- Format：`qcow2`（要快照）或 `raw`（极致性能）  
- **Cache**：**Write back**（性能优，建议配合可靠电源/UPS）  
- **IO Thread**：勾选  
- **Discard/TRIM**：可勾选（便于回收未用空间）  
- **SSD emulation（SSD 仿真）**：勾选（让 Win 识别为 SSD）

### 1.5 CPU
- Sockets：**1**  
- Cores：按需（如 **20**）  
- Type：**host**  
- NUMA：  
  - ≤8 vCPU 可不勾  
  - >8 vCPU 或高负载：**勾选**（更贴近物理拓扑）  
- （若界面有）Hyper-V enlightenments：可 **启用**，提升 Win 虚拟化优化

### 1.6 Memory
- Memory (MB)：如 **8192**  
- Ballooning：**关闭**（固定内存更稳）

### 1.7 Network
- Model：**VirtIO (paravirtualized)**  
- Bridge：vmbr0（或你的桥）  
- Firewall：按需

### 1.8 Confirm
- 检查配置 → **Finish**

> 完成后，**再挂载第二个光驱**：把 **VirtIO 驱动 ISO** 挂到该 VM 的第二个 CD/DVD。

---

## 2. 首次安装 Windows（加载 VirtIO 驱动）

1) 选中 VM → **Console** → 启动。  
2) 进入 Windows 安装器：语言/键盘 → 下一步 → 安装到“自定义（高级）”。  
3) 若看不到磁盘：  
   - 点击 **加载驱动（Load Driver）**  
   - 浏览到 **VirtIO ISO** → `viostor`/`vioscsi` 目录（win10/win11/amd64）  
   - 载入后即可识别磁盘  
4) 选择磁盘 → **下一步** 开始安装 → 自动重启进入桌面。

> 如果出现 OVMF 报错“BdsDxe … Not Found/Timeout”：  
> - 确认 ISO 为 UEFI 版；  
> - 硬盘用 VirtIO 时务必 **加载驱动**；  
> - 如仍异常，可临时将系统盘改为 SATA 安装，装完驱动后再迁回 VirtIO SCSI。

---

## 3. 安装 VirtIO 全套驱动 & QEMU Guest Agent

进入 Windows 桌面后，确保 **VirtIO ISO** 仍挂载：

- 运行 `virtio-win-guest-tools.exe`（一键安装常用驱动与 QEMU Guest Agent）  
  或在设备管理器中逐个更新：`NetKVM`（网卡）、`Balloon`、`viostor/vioscsi`（存储）、`viofs`（文件共享）等。  
- Windows 服务里确认 **QEMU Guest Agent** 已安装并运行。  
- 回到 PVE：在 VM **Options** 或 **Hardware → Agent** 中确认 **QEMU Guest Agent: Enabled**。  
- 控制台/概要页应能看到来宾 IP、磁盘使用等信息。

---

## 4. Windows 内优化与校验

### 4.1 磁盘识别为 SSD
- 因已勾选 SSD/Discard，Windows 应显示为 SSD。  
- 检查 TRIM：
,,,
fsutil behavior query DisableDeleteNotify
,,,
- 返回 `0` 代表已启用 TRIM。也可在“优化驱动器”里确认“介质类型：SSD”。

### 4.2 电源与性能
- 电源计划：高性能/平衡按需。  
- 关闭无关启动项。  
- 生产环境建议：宿主机有 UPS；快照/备份策略就绪。

### 4.3 远程访问
- Windows 自带远程桌面（RDP）最稳，客户端用 **mstsc/Remote Desktop**。  
- **VNC Viewer 不能直接连 Windows 的 RDP**；VNC 只连 VNC 服务器。  
- 也可在 PVE 用 **SPICE** 或直通 GPU 获得更佳图形体验。

---

## 5. Win11 专项（可选）

- **TPM 2.0**：Hardware → Add → **TPM State (v2.0)**（需 OVMF）  
- **Secure Boot**：可开启（微软证书），若驱动签名或旧 ISO 兼容性差则关闭。  
- 若 Win11 安装校验受限，可用官方 22H2/23H2 ISO 或在安装界面使用旁路校验方法（合规环境不建议）。

---

## 6. 针对你主机（双路 AMD EPYC 7542 / 128GB / NVMe 990 Pro）的推荐参数

- Machine：**Q35**  
- BIOS：**OVMF (UEFI)**  
- vCPU：**1 Socket × 20 Cores**；Type：**host**；NUMA：**开启**  
- 内存：**8GB**（Ballooning 关闭）  
- 磁盘：**VirtIO SCSI (single)**，64GB，**Write back + IO Thread + SSD + Discard**  
- 网络：**VirtIO**  
- QEMU Guest Agent：**开启**  
- 说明：990 Pro 为 NVMe SSD，已足够快；VM 内部选择 VirtIO SCSI 比 SATA/IDE 更优。

---

## 7. 常见问题速查

- **安装器找不到磁盘**：未加载 VirtIO 存储驱动 → Load Driver 选择 `viostor`/`vioscsi`。  
- **UEFI 启动报 BdsDxe Not Found/Timeout**：ISO 非 UEFI 或硬盘驱动未加载；检查引导顺序/ISO/磁盘类型。  
- **Win 显示 HDD**：PVE 磁盘未勾选 SSD/Discard 或未用 VirtIO 控制器。  
- **网络无驱动**：安装 VirtIO `NetKVM`。  
- **关机不响应**：安装并启用 **QEMU Guest Agent**，PVE 才能优雅关机。  

---

## 8. 备份与快照（强烈建议）

- 新装完成/打补丁前：创建 **Snapshot** 或使用 **Backup (vzdump)**。  
- 系统盘用 `qcow2` 可快照更灵活；生产极致性能可选 `raw` 并配合备份。

---

## 9. （可选）安装完成后验证清单

- 设备管理器无感叹号，网络/存储/显示驱动齐全（VirtIO）。  
- QEMU Guest Agent 状态“Running”，PVE 概要能显示来宾 IP。  
- 磁盘在“优化驱动器”显示 **SSD**，TRIM 启用。  
- Windows 更新正常，RDP 可连接。  
- 创建初始快照/备份。

---
**By @ChatGPT**