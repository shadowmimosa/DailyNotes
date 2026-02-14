# 萤石摄像头RTSP配置与EasyNVR推流使用指南

## 目录
- [1. 概述](#1-概述)
- [2. 开启RTSP连接](#2-开启rtsp连接)
- [3. RTSP视频流格式](#3-rtsp视频流格式)
- [4. 连接验证](#4-连接验证)
- [5. EasyNVR配置](#5-easynvr配置)
- [6. 常见问题](#6-常见问题)

---

## 1. 概述

萤石摄像头是海康威视旗下的智能家居摄像头品牌，支持通过RTSP协议获取视频流。本文介绍如何开启萤石摄像头的RTSP功能，并使用EasyNVR等软件进行推流管理。

**适用型号**：
- 萤石C6C系列（2K+星光增强版、400万极清等）
- 其他支持RTSP的萤石摄像头型号

**应用场景**：
- 第三方软件集成（NVR、视频管理平台）
- 二次开发和视频分析
- 多路视频流统一管理

---

## 2. 开启RTSP连接

萤石摄像头默认未开启RTSP功能，需要通过官方APP手动激活。

### 2.1 操作步骤

#### 步骤1：打开萤石云视频APP
- 在APP底部选项卡中点击**"我的"**
- 点击**"工具"**图标

![打开工具](https://raw.githubusercontent.com/yongdaimi/img/master/image-20231228110609558.png)

#### 步骤2：选择局域网设备预览
- 点击**"局域网设备预览"**选项

![局域网设备预览](https://raw.githubusercontent.com/yongdaimi/img/master/image-20231228110837596.png)

#### 步骤3：扫描局域网设备
- 点击**"开始扫描"**按钮
- 等待扫描完成，显示局域网内的摄像头设备

![开始扫描](https://raw.githubusercontent.com/yongdaimi/img/master/image-20231228110918363.png)

#### 步骤4：连接目标设备
- 点击需要配置的摄像头设备
- **首次连接时**需要输入设备密码

> **重要提示**：设备密码不是APP登录密码，而是摄像头底座贴纸上的6位数字验证码

![设备列表](https://raw.githubusercontent.com/yongdaimi/img/master/image-20231228222656266.png)

#### 步骤5：进入设备设置
- 连接成功后，点击预览画面右上角的**齿轮图标**

![设置入口](https://raw.githubusercontent.com/yongdaimi/img/master/image-20231228223849904.png)

#### 步骤6：开启RTSP服务
- 点击**"更多设置"**
- 依次进入**"本地服务开关"**
- **勾选"RTSP"选项**

![开启RTSP](https://raw.githubusercontent.com/yongdaimi/img/master/image-20231228223805760.png)

### 2.2 获取设备信息

在设置页面可以查看：
- 设备IP地址
- 设备序列号
- 固件版本等信息

![设备信息](https://raw.githubusercontent.com/yongdaimi/img/master/image-20231228224016110.png)

---

## 3. RTSP视频流格式

### 3.1 标准格式

```
rtsp://[username]:[password]@[ip]:[port]/[codec]/[channel]/[subtype]/av_stream
```

### 3.2 参数说明

| 参数 | 说明 | 示例值 |
|------|------|--------|
| **username** | 用户名 | admin（默认） |
| **password** | 设备密码 | 摄像头底座6位验证码 |
| **ip** | 设备IP地址 | 192.168.31.108 |
| **port** | 端口号 | 554（默认，可省略） |
| **codec** | 编码格式 | h264 / MPEG-4 / mpeg4 |
| **channel** | 通道号 | ch1（从1开始） |
| **subtype** | 码流类型 | main（主码流）/ sub（辅码流） |

### 3.3 实际示例

**主码流（高清）**：
```
rtsp://admin:LAUWEN@192.168.31.108:554/h264/ch1/main/av_stream
```

**辅码流（流畅）**：
```
rtsp://admin:LAUWEN@192.168.31.108:554/h264/ch1/sub/av_stream
```

**简化格式（默认端口）**：
```
rtsp://admin:LAUWEN@192.168.31.108/h264/ch1/main/av_stream
```

---

## 4. 连接验证

### 4.1 使用VLC播放器验证

#### 步骤1：打开VLC
- 点击菜单**"媒体"** → **"打开网络串流"**

![VLC菜单](https://raw.githubusercontent.com/yongdaimi/img/master/image-20231228111551917.png)

#### 步骤2：输入RTSP地址
- 在网络URL框中输入完整的RTSP地址
- 点击**"播放"**按钮

![输入地址](https://raw.githubusercontent.com/yongdaimi/img/master/image-20231228111635719.png)

#### 步骤3：查看视频画面
- 连接成功后会显示实时视频画面

![播放成功](https://raw.githubusercontent.com/yongdaimi/img/master/image-20231228224317607.png)

### 4.2 使用FFplay验证

```bash
ffplay -rtsp_transport tcp "rtsp://admin:密码@192.168.31.108/h264/ch1/main/av_stream"
```

---

## 5. EasyNVR配置

EasyNVR是一款流媒体服务软件，可以将RTSP流转换为多种格式（RTMP、HTTP-FLV、HLS等）。

### 5.1 EasyNVR安装

1. 从官网下载对应系统版本：[EasyNVR官网](https://www.easynvr.com/)
2. 解压并运行程序
3. 默认访问地址：`http://localhost:10800`
4. 默认账号：admin / admin

### 5.2 添加萤石摄像头

#### 方法一：单个添加
1. 登录EasyNVR管理后台
2. 点击**"通道管理"** → **"添加通道"**
3. 填写以下信息：
   - **通道名称**：自定义名称
   - **RTSP地址**：`rtsp://admin:密码@IP地址/h264/ch1/main/av_stream`
   - **传输协议**：选择TCP（推荐）或UDP
   - **是否录像**：根据需求选择
4. 点击**"确定"**保存

#### 方法二：批量导入
1. 准备CSV或Excel文件，格式如下：
```
通道名称,RTSP地址
客厅摄像头,rtsp://admin:123456@192.168.31.101/h264/ch1/main/av_stream
卧室摄像头,rtsp://admin:123456@192.168.31.102/h264/ch1/main/av_stream
```
2. 在通道管理页面选择**"批量导入"**
3. 上传文件并确认导入

### 5.3 获取推流地址

添加成功后，EasyNVR会自动生成多种格式的播放地址：

- **RTSP**：`rtsp://服务器IP:554/通道ID.sdp`
- **RTMP**：`rtmp://服务器IP:1935/live/通道ID`
- **HTTP-FLV**：`http://服务器IP:10800/通道ID.flv`
- **HLS**：`http://服务器IP:10800/通道ID/hls.m3u8`
- **WebRTC**：`webrtc://服务器IP:10800/通道ID`

### 5.4 Web播放

在EasyNVR后台点击**"视频广场"**可直接在浏览器中预览所有摄像头画面。

---

## 6. 常见问题

### 6.1 无法连接RTSP流

**问题原因**：
- RTSP功能未开启
- 密码错误
- 网络不通
- 防火墙阻止

**解决方案**：
1. 确认已在APP中开启RTSP功能
2. 核对设备密码（底座6位验证码）
3. 检查摄像头与电脑是否在同一局域网
4. 关闭防火墙或开放554端口
5. 尝试使用TCP传输协议：
   ```
   rtsp://admin:密码@IP/h264/ch1/main/av_stream?tcp
   ```

### 6.2 VLC黑屏但有声音

**问题原因**：编码格式不兼容

**解决方案**：
1. 更换codec参数：
   - 尝试 `h264`、`MPEG-4`、`mpeg4`
2. 更新VLC到最新版本
3. 使用辅码流（sub）代替主码流

### 6.3 延迟较高

**问题原因**：
- 使用主码流分辨率过高
- 网络带宽不足

**解决方案**：
1. 使用辅码流（sub）降低延迟
2. 在EasyNVR中设置缓冲时间
3. 使用有线网络代替WiFi
4. 调整摄像头码率设置

### 6.4 无法获取设备IP

**解决方案**：
1. 在萤石APP的设备设置页查看
2. 登录路由器管理后台查看DHCP分配
3. 使用IP扫描工具（如Advanced IP Scanner）
4. 通过ping设备序列号（部分路由器支持）

### 6.5 密码错误

**解决方案**：
1. 使用摄像头底座贴纸上的6位验证码
2. 如果修改过密码，使用修改后的密码
3. 在萤石APP中重置设备密码

### 6.6 EasyNVR添加通道失败

**解决方案**：
1. 先用VLC验证RTSP地址是否正确
2. 检查EasyNVR服务是否正常运行
3. 查看EasyNVR日志文件排查错误
4. 确认EasyNVR授权和通道数限制

---

## 7. 进阶配置

### 7.1 多码流同时使用

```
# 主码流用于录像
rtsp://admin:密码@192.168.31.108/h264/ch1/main/av_stream

# 辅码流用于实时预览
rtsp://admin:密码@192.168.31.108/h264/ch1/sub/av_stream
```

### 7.2 录像存储配置

在EasyNVR中可以设置：
- 录像保存路径
- 录像时长（循环覆盖）
- 录像计划（全天/时间段）
- 录像码率和格式

### 7.3 云端推流

EasyNVR支持将RTSP流推送到云端平台：
- 阿里云直播
- 腾讯云直播
- 七牛云直播
- 自建RTMP服务器

---

## 8. 参考资料

- [萤石摄像头RTSP流获取（黑屏解决）](https://blog.csdn.net/Douz_lungfish/article/details/131148208)
- [海康萤石的本地在线码流](https://blog.51cto.com/leekwen/5930314)
- [EasyNVR官方文档](https://www.easynvr.com/)

---

## 9. 附录

### 9.1 常用RTSP工具

| 工具名称 | 用途 | 平台 |
|---------|------|------|
| VLC | 播放测试 | Windows/Mac/Linux |
| FFmpeg | 转码推流 | 跨平台 |
| PotPlayer | 播放测试 | Windows |
| EasyNVR | 流媒体服务 | Windows/Linux |
| ZLMediaKit | 流媒体服务 | 跨平台 |

### 9.2 萤石摄像头常见型号

- C6系列：室内云台摄像头
- C3系列：室外枪机摄像头
- C8系列：高端室内摄像头
- DP系列：智能门铃
- DB系列：可视门锁

---

**文档版本**：v1.0  
**最后更新**：2024年12月  
**作者整理**：基于多个技术博客整理汇总