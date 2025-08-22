# Windows WebDAV 挂载完整笔记 —— RaiDrive 与 rclone 对比及服务化方案

---

## 目录

1. RaiDrive 使用体验与问题
2. rclone 使用体验与问题
3. rclone 配置文件及管理
4. WebDAV 配置文件示例
5. rclone 挂载常用参数说明
6. 挂载刷新与 Windows 资源管理器
7. 开机自动挂载及盘符可见方案
8. nssm 与 sc 创建服务对比
9. rclone 远程控制（rc）与 Web GUI
10. 文件修改时间保留相关
11. 一键安装批处理脚本示例
12. 常见问题及补充说明
13. 软件下载地址

---

## 1. RaiDrive 使用体验与问题

### 优点

- 方便快捷，Windows 原生驱动挂载，盘符直接可见
- 服务端文件删除或修改，挂载盘自动快速刷新
- 勾选“维护文件和文件夹的修改时间”后，文件夹时间能正确保留

### 缺点

- 文件（非文件夹）修改时间不稳定，不能完全保持
- 软件带有弹窗广告，影响体验
- 功能不够灵活，难以满足复杂缓存和高级需求

---

## 2. rclone 使用体验与问题

### 优点

- 功能强大，支持多云存储和多协议（包括 WebDAV）
- 支持符号链接、缓存控制、远程控制（rc）和 Web GUI
- 支持自定义配置文件和灵活启动参数

### 缺点

- 配置复杂，需要一定命令行和配置文件知识
- 目录缓存导致服务端文件删除后挂载盘不自动刷新，需要手动刷新缓存
- Windows 服务启动挂载时，盘符可见性需要`--network-mode`且服务须以用户身份运行
- 无广告，但缺少像 RaiDrive 那样的原生驱动集成体验

---

## 3. rclone 配置文件及管理

- 默认配置文件路径（Windows）：

  ```
  C:\Users<用户名>\AppData\Roaming\rclone\rclone.conf
  ```

- 查看配置文件路径：

  ```bash
  rclone config file
  ```

- 指定自定义配置文件：

  ```bash
  rclone --config D:\configs\myrclone.conf <command>
  ```

- 生成加密密码：

  ```bash
  rclone obscure your_password
  ```

---

## 4. WebDAV 配置文件示例

```ini
[mydav]
type = webdav
url = https://webdav.example.com/remote.php/webdav/
vendor = other
user = phoenix
pass = ObfuscatedEncryptedPassword
```

---

## 5. rclone 挂载常用参数说明

```bash
rclone mount mydav:/ X: --vfs-cache-mode full --links --dir-cache-time 10s --network-mode
```

| 参数                      | 作用                               |
| ------------------------- | ---------------------------------- |
| `--vfs-cache-mode full`   | 本地完全缓存读写，兼容随机读写场景 |
| `--vfs-cache-mode writes` | 只缓存写操作，读直接访问远程       |
| `--vfs-cache-max-age`     | 本地缓存文件最大保留时间           |
| `--links`                 | 启用符号链接支持                   |
| `--dir-cache-time`        | 目录缓存时间，减小刷新延迟         |
| `--network-mode`          | Windows 网络上下文，保证盘符可见   |
| `--use-server-modtime`    | 使用服务器返回的时间戳保持文件时间 |
| `--rc`                    | 启用远程控制接口                   |

---

## 6. 挂载刷新与 Windows 资源管理器

- 资源管理器刷新（F5）只刷新本地缓存视图，不强制拉取远程最新目录

- 手动刷新缓存：

  ```bash
  rclone rc vfs/refresh dir="/"
  ```

- 挂载时加远程控制参数，方便管理：

  ```bash
  rclone mount mydav:/ X: --rc --rc-user admin --rc-pass admin ...
  ```

---

## 7. 开机自动挂载及盘符可见方案

### 推荐方案：nssm 创建服务

1. 下载 nssm：[https://nssm.cc/download](https://nssm.cc/download)

2. 创建挂载脚本（`mount_mydav.bat`）：

   ```bat
   @echo off
   C:\rclone\rclone.exe mount mydav:/ X: --vfs-cache-mode full --links --dir-cache-time 10s --network-mode
   ```

3. 用 nssm 创建服务：

   ```cmd
   C:\nssm\nssm.exe install RcloneMount
   ```

4. 设置服务启动参数、登录账户（当前用户）

5. 启动服务并设置自动启动：

   ```cmd
   C:\nssm\nssm.exe start RcloneMount
   sc config RcloneMount start= auto
   ```

### 备选方案：sc 创建服务（不推荐）

```cmd
sc create RcloneMount binPath= "C:\rclone\rclone.exe mount mydav:/ X: --vfs-cache-mode full --links --dir-cache-time 10s --network-mode" start= auto
sc start RcloneMount
```

> 注意：sc 创建的服务默认系统会话运行，挂载盘符对用户不可见。

---

## 8. nssm 与 sc 创建服务对比

| 特性           | nssm               | sc                     |
| -------------- | ------------------ | ---------------------- |
| 支持控制台程序 | 专业支持，自动重启 | 不完全支持，崩溃服务停 |
| 配置界面       | GUI 简单配置       | 仅命令行配置           |
| 运行用户身份   | 支持 GUI 配置      | 需额外命令配置         |
| 日志重定向     | 支持               | 不支持                 |
| 启动停止钩子   | 支持               | 不支持                 |

---

## 9. rclone 远程控制（rc）与 Web GUI

- 启动远程控制：

  ```bash
  rclone rcd --rc-user admin --rc-pass admin --rc-web-gui-no-open-browser
  ```

- 浏览器访问：

  ```
  http://localhost:5572
  ```

- 可远程刷新缓存、查看状态、管理挂载。

---

## 10. 文件修改时间保留相关

- 推荐挂载参数：

  ```bash
  rclone mount mydav:/ X: --vfs-cache-mode full --links --dir-cache-time 10s --use-server-modtime --network-mode
  ```

- `--use-server-modtime` 使用服务器返回的修改时间，减少时间戳差异

- 依赖 WebDAV 服务器对时间戳的支持

- RaiDrive 需勾选“维护文件和文件夹的修改时间”才能部分保留时间戳

---

## 11. 一键安装批处理脚本示例

> ChatGPT 生成 未验证

```bat
@echo off
setlocal

REM ==== 配置区域 ====
set RCLONE_PATH=C:\rclone\rclone.exe
set NSSM_PATH=C:\nssm\nssm.exe
set REMOTE_NAME=mydav
set MOUNT_POINT=X:
set SERVICE_NAME=RcloneMount

REM ==== 卸载已有服务（如果存在） ====
echo 停止并删除已有服务（如果存在）...
%NSSM_PATH% stop %SERVICE_NAME% >nul 2>&1
%NSSM_PATH% remove %SERVICE_NAME% confirm >nul 2>&1

REM ==== 创建新的服务 ====
echo 创建服务 %SERVICE_NAME% ...
"%NSSM_PATH%" install %SERVICE_NAME%

REM 设置服务路径和参数
"%NSSM_PATH%" set %SERVICE_NAME% Application "%RCLONE_PATH%"
"%NSSM_PATH%" set %SERVICE_NAME% AppParameters mount %REMOTE_NAME%:/ %MOUNT_POINT% --vfs-cache-mode full --links --dir-cache-time 10s --network-mode

REM 设置工作目录（rclone 所在目录）
for %%I in ("%RCLONE_PATH%") do set RCLONE_DIR=%%~dpI
"%NSSM_PATH%" set %SERVICE_NAME% AppDirectory "%RCLONE_DIR%"

REM 设置服务以当前登录用户身份运行（需手动设置密码）
echo 配置服务以当前用户身份运行...
sc config %SERVICE_NAME% obj= ".\%USERNAME%" password= ""

REM 设置服务自动启动
sc config %SERVICE_NAME% start= auto

REM 启动服务
echo 启动服务...
"%NSSM_PATH%" start %SERVICE_NAME%

echo.
echo 服务安装并启动完成！
echo 请确认 %MOUNT_POINT% 盘符是否已挂载，资源管理器是否可见。
echo 如果需要更改运行账户密码，请使用“服务”管理工具手动设置。
pause
endlocal
```

> 注意：用户身份运行需密码，批处理不能自动输入密码，需手动补充。

---

## 12. 常见问题及补充说明

- **上传带宽满**
  由于 `--vfs-cache-mode full` 本地缓存完整文件，写入量大时上传一直占用带宽。可用 `--vfs-cache-mode writes` 缓解。

- **服务端删除文件 rclone 不刷新**
  目录缓存导致，调小 `--dir-cache-time` 或用远程控制刷新。

- **Windows 资源管理器刷新无效**
  只刷新本地缓存，不强制远程拉取。

- **符号链接提示**
  `Symlinks support enabled` 是正常信息。

- **RaiDrive 广告问题**
  广告可能影响体验，rclone 无此问题。

---

## 13. 软件下载地址

| 软件                       | 下载链接                                                                                                       | 说明                                      |
| -------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| rclone                     | [https://rclone.org/downloads/](https://rclone.org/downloads/)                                                 | 官方最新版，多平台支持                    |
| nssm                       | [https://nssm.cc/download](https://nssm.cc/download)                                                           | Windows 服务管理工具                      |
| RaiDrive                   | [https://www.raidrive.com/](https://www.raidrive.com/)                                                         | Windows WebDAV 挂载工具，有免费版和付费版 |
| WinFsp (rclone 依赖，可选) | [https://github.com/billziss-gh/winfsp/releases/latest](https://github.com/billziss-gh/winfsp/releases/latest) | Windows FUSE 文件系统支持                 |

---

## 附录

- rclone 官方文档
  [https://rclone.org/](https://rclone.org/)

- rclone WebDAV 说明
  [https://rclone.org/webdav/](https://rclone.org/webdav/)

- nssm 使用文档
  [https://nssm.cc/usage](https://nssm.cc/usage)

---

**如需更详细使用指导或定制脚本，欢迎随时联系！**