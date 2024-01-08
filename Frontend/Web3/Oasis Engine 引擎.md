<font size=4 face='楷体'>

## Oasis Engine 引擎

- [Oasis-Engine](https://gitee.com/unholypanda/Oasis-Engine)
  Oasis Engine 引擎是一款以 Web 为先，移动为先的互动/创作平台，使用组件系统架构、逻辑编写采用脚本系统、引擎源码使用 TypeScript 编写，并且追求易用和轻量

![](./Web3.0来了，花呗借呗前端团队开源的Web图形引擎会成为元宇宙的技术支撑吗？/efbb07a7494d5ffa8566e6f607d778c2.awebp)

大家好，我是马建仓。

要说最近这半年什么词比较火，相信 **Web 3.0** 是许多关注前沿技术的开发者们耳熟能详的。

那什么是 **Web3.0？**

> 《中国金融》在今年 3 月发布的《**姚前：Web3.0：渐行渐近的新一代互联网**》中曾提到：Web3.0 不止是智能互联网，同时还是立体全息互联网，为用户提供前所未有的交**互性以及高度的沉浸感和参与感**。

在主流市场看来，Web3.0 很可能就是新一代互联网的雏形。他们认为，新一代互联网不仅能够组合信息，同时也能像人类一样读懂信息，并以类似人类的方式自主学习于知识推理，从而为人类提供准确可靠的信息，从而使得人与互联网的交互更加自动化、智能化及人性化。而这样的场景设想也诞生了时下热议的**元宇宙、crypto、NFT、DAO** 等新兴概念。

然而，概念落地背后需要技术支撑，**怎样的技术**才能支撑起这些实现中的奇幻场景，**实现高度的真实性与沉浸感**呢？

今天，我们给大家推荐一个很可能助力元宇宙实现的 Web3D 引擎关键技术的开源项目—— **Oasis engine**。

这并非是强加概念，不久前该项目作者之一就曾在沙龙会议上做了个题为：《元宇宙级 Web3D 引擎关键技术》的分享，参考内容如下：

![](./Web3.0来了，花呗借呗前端团队开源的Web图形引擎会成为元宇宙的技术支撑吗？/bd909ca212d6ade143e18cbb5286c3dd.awebp)

这究竟是个怎样的宝藏项目？我们今天计划从以下几个方面来介绍。欢迎各位开发者共同讨论。

### Oasis engine 是什么？

Oasis engine 是一个移动优先的高性能 Web 图形引擎，也是追求易用和轻量的高性能互动创作平台，具备 2D/3D 互动创作能力，目前已经推出到 v0.6 版，并已在 Gitee 开源。

> 项目地址：<[gitee.com/unholypanda…](https://gitee.com/unholypanda/Oasis-Engine)> 开源许可证： MIT

或许你不熟悉它，但是它却是**支付宝集五福、打年兽、蚂蚁庄园**等各种互动业务背后的**图形引擎**。同时，他的研发团队也大有来头。站在 Oasis engine 背后的核心开发者是蚂蚁集团业务能力十足的 RichLab 前端团队。从知乎界面我们能知道，这也是花呗、借呗的前端团队。

![](./Web3.0来了，花呗借呗前端团队开源的Web图形引擎会成为元宇宙的技术支撑吗？/1e80f73b2470c8bfada2fc8d98c2f038.awebp)

从官方公号介绍得知，Oasis Engine 主要包含 Oasis Runtime、Oasis Editor 和 Oasis Store 三部分。该项目采用组件系统架构，不仅需要具备三维渲染能力，还需要包含了非常多来自各领域的功能，比如 2D、3D、UI、音频、物理、VR/AR、逻辑编写等等。

![](./Web3.0来了，花呗借呗前端团队开源的Web图形引擎会成为元宇宙的技术支撑吗？/a2edb7860b91c0610967bfc68bc7ae05.awebp)

目前主要用于仿真展示、互动营销或者趣味小游戏，编辑器采用云端 IDE，协同编写。

![](./Web3.0来了，花呗借呗前端团队开源的Web图形引擎会成为元宇宙的技术支撑吗？/6d1428311993abc196e6a9caf81da2cd.awebp)

### 为何选择 TypeScript？

Oasis 的开发语言是 TypeScript。项目负责人烧鹅曾在媒体采访中这样解释：

> 他认为对于大型复杂项目，TypeScript 的研发效率优势较 JavaScript 明显。首先对于引擎用户，最大的优势就是拥有代码提示；其次对于引擎开发者，TypeScript 定义了弱类型语言缺失的能力，能够帮助开发者减少引擎的代码量。

### 功能

Engine 在 Oasis engine 中扮演着总控制器的角色，主要包含了**画布、渲染控制和引擎子系统管理**等三大功能：

- **画布**：主画布相关的操作，如修改画布宽高等。
- **渲染控制**： 控制渲染的执行/暂停/继续、垂直同步等功能。
- **引擎子系统管理**：场景管理和资源管理等。
- **执行环境的上下文管理**：控制 WebGL 等执行环境的上下文管理。

### 特点

- 组件系统结构清晰、灵活性强、易扩展
- 逻辑化脚本组件，简单易用，复用性强
- 针对移动设备多方面优化
- 具备 2D/3D 互动创作能力
- 支持前端开发工作流

![](./Web3.0来了，花呗借呗前端团队开源的Web图形引擎会成为元宇宙的技术支撑吗？/d53d9b3fc694a36fc464a023c9ea94b9.awebp)

### 如何安装？

#### NPM

若是在项目中使用，可通过 NPM 安装 1.安装包

```
npminstall--saveoasis-engine
```

2.引入引擎模块

```
import{WebGLEngine,Camera}from'oasis-engine'
```

#### 本地创建 Demo

![](./Web3.0来了，花呗借呗前端团队开源的Web图形引擎会成为元宇宙的技术支撑吗？/2375d7f254deeae008a6ff980b8a1713.awebp)

#### 使用示例

```
//CreateenginebypassingintheHTMLCanvasElementidandadjustcanvassize.
constengine=newWebGLEngine("canvas-id");
engine.canvas.resizeByClientSize();

//Getsceneandcreaterootentity.
constscene=engine.sceneManager.activeScene;
constrootEntity=scene.createRootEntity("Root");

//Createlight.
constlightEntity=rootEntity.createChild("Light");
constdirectLight=lightEntity.addComponent(DirectLight);
lightEntity.transform.setRotation(-45,-45,0);
directLight.intensity=0.4;

//Createcamera.
constcameraEntity=rootEntity.createChild("Camera");
cameraEntity.addComponent(Camera);
cameraEntity.transform.setPosition(0,0,12);

//Createsphere.
constmeshEntity=rootEntity.createChild("Sphere");
constmeshRenderer=meshEntity.addComponent(MeshRenderer);
constmaterial=newBlinnPhongMaterial(engine);
meshRenderer.setMaterial(material);
meshRenderer.mesh=PrimitiveMesh.createSphere(engine,1);

//Runengine.
engine.run();
```

### Oasis Editor 暂未对外开放

Oasis Editor （目前未对外开放）是一个基于移动优先的高性能图形开源引擎 Oasis Engine 的云端 Web 互动内容创作平台，可以在线完成一个互动项目的创建、编辑、导出。推荐使用 Chrome 浏览器 打开它，因目前该编辑器未对外公开，暂不详细介绍。若感兴趣，可前往[作者仓库](https://gitee.com/unholypanda/Oasis-Engine)查看操作指南。

![](./Web3.0来了，花呗借呗前端团队开源的Web图形引擎会成为元宇宙的技术支撑吗？/9861fdb8c2652d0617aa32235a382e65.awebp)

### 项目架构图

![](./Web3.0来了，花呗借呗前端团队开源的Web图形引擎会成为元宇宙的技术支撑吗？/f968b5bdc8e72025f71e316950eaa59e.awebp)

### 往期推荐

[北京大学白帽黑客创业，做了个开源供应链安全治理引擎](https://juejin.cn/post/7089996216523554823)

[全中文注释，让单片机开发和 Arduino 一样高效](https://juejin.cn/post/7088592123825487880)

[CNCF 云原生全景图收录了一个国产轻量级 RPC 框架](https://juejin.cn/post/7086658595969990693)

> 当前文档由 [markdown 文档下载插件](https://github.com/kscript/markdown-download) 下载, 原文链接: [Web3.0 来了，花呗借呗前端团队开源的 Web 图形引擎会成为元宇宙的技术支撑吗？](https://juejin.cn/post/7091187236342874143)

### Reference

[Web3.0 来了，花呗借呗前端团队开源的 Web 图形引擎会成为元宇宙的技术支撑吗？](https://juejin.cn/post/7091187236342874143)
 
**2022.07.06**
