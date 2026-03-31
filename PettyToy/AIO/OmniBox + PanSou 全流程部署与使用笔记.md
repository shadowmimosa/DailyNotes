# NAS 影视私有化方案：OmniBox + PanSou

## 1. OmniBox：全聚合一站式观影平台

### 1.1 简介

OmniBox 是一个功能强大的影视综合站，核心特点是「多源聚合」：

- 支持采集站、网盘资源、IPTV、直播平台等多种资源
- 提供一站式的观影解决方案
- 支持弹幕互动与 TMDB API 接入，显示分季分集海报、剧情概要、演员表、评分等
- 兼容网页端、移动端、TV 端

> 适合想整合多平台资源，避免频繁切换视频 App 的用户。

### 1.2 核心功能

| 功能            | 说明                         |
| --------------- | ---------------------------- |
| 多源聚合        | 支持采集站、网盘资源在线观看 |
| IPTV / 电视直播 | 支持 IPTV 及电视直播源观看   |
| 平台直播        | 集成 6 大主流直播平台        |
| 全能解析        | 支持解析各大主流视频站链接   |
| 跨平台观看      | 网页、移动端、TV 端均可使用  |
| 弹幕互动        | 所有客户端支持弹幕           |
| 高清画质        | 支持 4K 超高清视频播放       |

---

## 2. OmniBox 部署指南

### 2.1 Docker 单容器部署

```bash
docker run -d \
  --restart unless-stopped \
  --name omnibox \
  -p 7023:7023 \
  -v $PWD/data:/app/data \
  lampon/omnibox:latest
```

- `$PWD/data`：当前目录的数据存放路径

### 2.2 Docker Compose 部署

`docker-compose.yml` 示例：

```yaml
version: '3'
services:
  omnibox:
    image: lampon/omnibox:latest
    container_name: omnibox
    restart: unless-stopped
    ports:
      - '7023:7023'
    volumes:
      - ./data:/app/data
```

启动命令：

```bash
docker-compose up -d
```

### 2.3 使用

1. 浏览器访问 `http://NAS_IP:7023`
2. 搜索影视资源，需要手动导入第三方视频源
3. 后台管理：

   - 影视站资源导入/导出
   - 配置直播资源和电视源

4. 影视播放：

   - 影视站：本地及导入资源
   - 平台直播：同步观看主流平台
   - 电视直播：配置 m3u 测试源即可播放

---

## 3. PanSou：网盘资源搜索 API 服务

### 3.1 简介

PanSou 是高性能网盘搜索服务，特点：

- 支持多 Telegram 频道和自定义插件搜索
- 并发搜索，结果智能排序
- 自动分类网盘类型
- 提供简约网页界面，开箱即用
- Docker 集成，前后端一体化

### 3.2 支持的网盘类型

- 百度网盘、阿里云盘、夸克网盘、天翼云盘
- UC 网盘、移动云盘、115 网盘、PikPak
- 迅雷网盘、123 网盘
- 磁力链接、电驴链接及其他

### 3.3 部署方式

#### Docker CLI 安装

```bash
mkdir -p /volume1/docker/pansou/{data,logs}
cd /volume1/docker/pansou
docker run -d \
  --name pansou-app \
  --restart unless-stopped \
  -p 17080:80 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  -e DOMAIN=localhost \
  -e PANSOU_PORT=8888 \
  -e PANSOU_HOST=127.0.0.1 \
  ghcr.io/fish2018/pansou-web:latest
```

#### Docker Compose 安装

`docker-compose.yml` 示例：

```yaml
version: '3.8'
services:
  pansou:
    image: ghcr.io/fish2018/pansou-web:latest
    container_name: pansou-app
    restart: unless-stopped
    ports:
      - '17080:80'
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    environment:
      - DOMAIN=localhost
      - PANSOU_PORT=8888
      - PANSOU_HOST=127.0.0.1
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost/api/health']
      interval: 30s
      timeout: 10s
      retries: 3
```

### 3.4 使用

1. 在 OmniBox 后台配置 PanSou 地址
2. 允许网盘授权后即可搜索并播放网盘资源
3. 搜索结果可直接在影视站或全局搜索中显示

---

## 4. 总结

- **OmniBox**：提供一站式影视观影体验，多平台聚合，支持高清、弹幕、跨平台观看
- **PanSou**：高性能网盘资源搜索服务，可与 OmniBox 集成，实现私有化网盘资源搜索和播放
- 适合家庭影院用户和 NAS 爱好者，避免广告、切换 App 和复杂配置问题
- 部署方式简单，Docker 或 Docker Compose 均可使用

---

## 5. 版本更新说明

### v1 vs v2

- **当前使用版本**：v1.4.4（最后稳定版）
- **v2 发布时间**：2026年1月底/2月初（约两个月前）
  - 新增：爬虫源更新等功能
- **v2 反馈**：存在使用体验问题，爬虫源管理繁琐，部分功能不够易用
- **更新时间**：2026年3月31日
- **决定**：已退回至 v1.4.4 版本，等待 v2 进一步优化后再升级

---

## 6. 参考

- [OmniBox Spider - GitHub](https://github.com/Silent1566/OmniBox-Spider)
- [NAS 部署 OmniBox：全聚合一站式观影解决方案，轻松打造家庭影院](https://post.smzdm.com/p/a7gd6m6o/)
[OmniBox：你的下一代家庭影视中心](https://laosu.tech/2025/10/26/OmniBox%EF%BC%9A%E4%BD%A0%E7%9A%84%E4%B8%8B%E4%B8%80%E4%BB%A3%E5%AE%B6%E5%BA%AD%E5%BD%B1%E8%A7%86%E4%B8%AD%E5%BF%83/)
[网盘资源搜索 API 服务 PanSou](https://laosu.tech/2025/08/15/%E7%BD%91%E7%9B%98%E8%B5%84%E6%BA%90%E6%90%9C%E7%B4%A2API%E6%9C%8D%E5%8A%A1PanSou)
[Omnibox 配置篇 --- 一站搞定你所有观影需求](https://lazycatcloud.com/playground/guideline/1403)
