<font size=4 face='楷体'>

## WSL2 挂载 EXT4 硬盘

### WSL2 的安装

略

### 查询硬盘

powershell 中执行

```powershell
GET-CimInstance -query "SELECT * from Win32_DiskDrive"
```
或者
```powershell
Get-Disk
```

找到你需要挂载的磁盘后，执行以下命令：

```powershell
# wsl --mount DeviceID --partition 分区 --type 文件系统类型
wsl --mount \\.\PHYSICALDRIVE5 --partition 1 --type ext4
```

这时候我们在 WSL2 系统下已经能看到挂载的磁盘目录，默认挂载点为 `/mnt/wsl`。但以上在每次系统重启后都需要重新配置一下，比较繁琐。

或者使用 Ext2Fsd 先挂载到 Windows 中，WSL 中 `/mnt/` 就会有该盘符，但是性能应该会有影响。

### Reference

[WIN11 借助 wsl2 挂载 ext4 磁盘](https://blog.csdn.net/MacwinWin/article/details/140066378)

**2024.12.05**
