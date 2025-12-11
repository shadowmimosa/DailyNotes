## Chrome 离线安装与 ChromeDriver 下载整理笔记

### 一、Chrome 谷歌浏览器离线安装

**参考链接：** [Chrome 离线安装教程](https://blog.csdn.net/weixin_45132755/article/details/142133541)

#### 1. 下载离线安装包

- 官方提供 **32 位（x86）** 和 **64 位（x64）** 两种离线安装包。
- 示例文件名：
  - `chrome_dev_x64-v68.0.3423.2.exe`
  - `chrome_dev_x86-v68.0.3423.2.exe`
- 文件名说明：
  - `x64`：适用于 64 位操作系统。
  - `x86`：适用于 32 位操作系统。
  - `v68.0.3423.2`：浏览器版本号。

#### 2. 下载地址

- 离线包下载链接（第三方）：[https://pan.quark.cn/s/ab6ed9424307](https://pan.quark.cn/s/ab6ed9424307)
- 官方完整离线安装包（Standalone Installer）：[https://www.google.cn/intl/zh-CN/chrome/?standalone=1&platform=win](https://www.google.cn/intl/zh-CN/chrome/?standalone=1&platform=win)

#### 3. 版本选择说明

- **64 位 Chrome 优势**：
  - 使用更多内存、性能更高。
  - 更好适配现代硬件。
  - 安全性更强。
- **32 位 Chrome 场景**：
  - 老旧系统仍需使用 32 位版本。
  - 某些低资源环境下使用。

#### 4. 安装流程

1. 双击安装包（`.exe`）。
2. 接受协议 ➝ 选择安装路径 ➝ 创建桌面快捷方式。
3. 按提示完成安装。
4. 若安装遇到问题，可查看提示或联系技术支持。

#### 5. Chrome 主要特点

- 简洁 UI
- 页面加载速度快（Blink 引擎）
- JavaScript 性能强（V8 引擎）
- 内置翻译、书签管理
- 丰富插件扩展（Chrome Web Store 支持）

---

### 二、ChromeDriver 下载整理

**原文链接：** [ChromeDriver 下载文章](https://www.cnblogs.com/architectforest/p/19299351)

#### 官方 Chrome for Testing 主站（含最新 Chrome & ChromeDriver）

[https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)

ChromeDriver 常用于自动化测试（如 Selenium），需与浏览器版本对应。

#### 1. 最新版本下载地址

适用于 Chrome 115 及以上版本：

```
https://googlechromelabs.github.io/chrome-for-testing/
```

此页面提供：

- 最新 Chrome 版本
- 对应 ChromeDriver
- 全平台安装包

#### 2. 旧版本（Chrome < 115）下载

```
https://chromedriver.storage.googleapis.com/index.html
```

适用于旧版 Selenium 项目或兼容性测试需求。

---

### 三、总结

- Chrome 离线安装需根据系统选择 32/64 位。
- ChromeDriver 需与浏览器版本严格匹配。
- 115 版本为分界点：
  - **115+ 使用 chrome-for-testing**
  - **115- 使用 storage.googleapis**

---

> 本笔记整合自 CSDN 与 博客园相关内容，仅作技术整理使用。