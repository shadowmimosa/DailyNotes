# Prisma 与 Nuxt 3 兼容性问题

## 问题概述

在将 Nuxt 3 项目升级到最新版本（Nuxt 3.16.0 与 Nitro 2.11.6）后，使用 Prisma 进行构建时出现错误。

GitHub Issue: [https://github.com/prisma/prisma/issues/26565](https://github.com/prisma/prisma/issues/26565)

## 错误信息

```
(node:12996) [DEP0155] DeprecationWarning: Use of deprecated trailing slash pattern mapping "./" in the "exports" field module resolution of the package at E:\src\xxxxxxx\node_modules\@prisma\client\package.json imported from E:\src\xxxxxxx\server\utils\prisma.ts. Mapping specifiers ending in "/" is no longer supported.

[nitro 18:11:14] ERROR TypeError [ERR_INVALID_MODULE_SPECIFIER]: Invalid module ".prisma" is not a valid package name imported from E:\src\xxxxxxx\node_modules\@prisma\client\default.js
```

## 问题分析

这个问题是由于 Prisma Client 与 Nuxt 3 最新版本之间存在兼容性问题导致的。具体表现为：

1. Prisma Client 的 package.json 中 [exports](file:///c%3A/Users/Phoenix/Documents/Repos/DailyNotes/Python/%E5%BA%93%E5%86%85%E5%AD%98%E7%9B%B8%E5%85%B3%E7%9F%A5%E8%AF%86%E7%82%B9.md#L39-L40) 字段使用了已弃用的尾部斜杠模式映射
2. 模块解析时 ".prisma" 被认为是无效的包名

## 影响范围

该问题已被标记为：
- bug/2-confirmed (已确认的 Bug)
- domain/client (客户端领域问题)
- kind/bug (已报告的 Bug)
- topic: bundler (打包工具相关)
- topic: nuxt (Nuxt 框架相关)

## 解决方案

目前还没有官方的解决方案，但可以尝试以下几种方法：

### 临时解决方案

1. **降级 Nuxt 版本**：
   如果业务允许，可以暂时将 Nuxt 版本降级到之前可以正常工作的版本。

2. **等待官方修复**：
   关注 GitHub Issue 的更新，等待 Prisma 团队发布修复版本。

### 社区提供的解决方案

根据 GitHub Issue 中的评论 [#2960042226](https://github.com/prisma/prisma/issues/26565#issuecomment-2960042226)，有用户提出以下解决方案：

在 Ubuntu 环境中运行代码可以解决此错误，无论使用哪个版本的 Nitro、Nuxt 或 Prisma，它总是有效。这是一个 Windows 平台特有的错误。

如果无法直接在 Ubuntu 系统中运行，建议在 Windows 中使用 WSL（Windows Subsystem for Linux）安装 Ubuntu，而无需使用虚拟机或双系统启动。

#### 使用 WSL 的具体步骤：

1. 启用 WSL 功能：
   - 以管理员身份打开 PowerShell，运行以下命令：
     ```powershell
     wsl --install
     ```
   - 或者使用传统方式启用 WSL：
     ```powershell
     dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
     dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
     ```

2. 重启计算机

3. 安装 Linux 发行版（如 Ubuntu）：
   - 打开 Microsoft Store，搜索并安装 Ubuntu
   - 或者使用命令行安装：
     ```powershell
     wsl --install -d Ubuntu
     ```

4. 启动 Ubuntu 并设置用户名和密码

5. 在 WSL 环境中安装 Node.js 和项目依赖：
   ```bash
   # 更新包管理器
   sudo apt update
   
   # 安装 Node.js
   curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
   sudo apt-get install -y nodejs
   
   # 进入项目目录并安装依赖
   cd /path/to/your/project
   npm install
   ```

6. 运行项目：
   ```bash
   npm run build
   ```

但也有其他用户反馈，即使在原生 Ubuntu 系统中也会遇到此问题，因此这个解决方案可能并不适用于所有情况。

## 相关链接

- GitHub Issue: https://github.com/prisma/prisma/issues/26565
- Prisma 官方文档: https://www.prisma.io/docs/

**2025.03.10**