---
created: 2023-11-19T21:57:22 (UTC +08:00)
tags: [前端开发, Vue.js, 单元测试]
source: https://zhuanlan.zhihu.com/p/643446343
author:
---

# 前端 Vuer，请收好这份《Vue 组件单元测试》宝典，给自己多一些安全感 - 知乎

> ## Excerpt
>
> 大家好，我是 Kagol。 作为一名前端，在做业务开发的过程中，你是否曾经： 因为担心上线之后出 bug，而反复手工验证自己负责的模块不敢修改现有的“屎山”（别人写的或者是自己 1 年前写的）代码，从而不断地编写 if/e…

---

![](https://pic3.zhimg.com/v2-0f495f1f7bc77196f269480986d6a612_b.jpg)

大家好，我是 Kagol。

作为一名前端，在做业务开发的过程中，你是否曾经：

- 因为担心上线之后出 bug，而反复手工验证自己负责的模块
- 不敢修改现有的“屎山”（别人写的或者是自己 1 年前写的）代码，从而不断地编写 if/else
- 发现业务中有很多重复的代码，每次一改好多地方都要改，但又不敢重构，担心重构之后出 bug
- 战战兢兢地修复一个陈年 bug，就怕引起 N 个新 bug

如果你中了以上任何一条，说明你现在缺乏安全感，你担心、你害怕、你不敢、你战战兢兢、你如履薄冰。

每天写代码都处在担惊受怕当中，程序员的尊严何在！

程序员的安全感要自己给自己，是时候改变现状了！

我们有很多方法可以给自己安全感，比如：

- 配置代码检测工具 ESLint
- 安装拼写检查插件 Code Spell Checker
- 代码评审 Code Review
- 结对编程 Pair programming
- 编写单元测试 Unit Test

本文主要给大家介绍如何在 Vue 项目中编写单元测试。

## 1 搭环境

我们的单元测试环境基于 `vitest` + `@vue/test-utils`。

前提：你需要有一个 Vue 项目，没有的话可以参考 [Vite](https://link.zhihu.com/?target=https%3A//cn.vitejs.dev/guide/%23scaffolding-your-first-vite-project) 官网进行创建。

第一步，在你的 Vue 项目中安装必要的依赖包。

```
npm i -D vitest @vue/test-utils happy-dom @vitest/coverage-v8
```

在 `vite.config.ts` 文件中增加以下配置。

```
import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],

  // 新增
  test: {
    environment: 'happy-dom'
  }
})
```

在 `package.json` 文件中增加相应的脚本命令

```
"scripts": {
    "dev": "vite",
    "build": "vue-tsc && vite build",
    "preview": "vite preview",

    // 新增
    "test": "vitest"
  },
```

我们尝试执行以下命令：

会发现控制台会打印以下日志：

```
$ npm test

> vue3-vite@0.0.0 test
> vitest


 DEV  v0.33.0 /vue3-vite-demo

include: **/*.{test,spec}.?(c|m)[jt]s?(x)
exclude:  **/node_modules/**, **/dist/**, **/cypress/**, **/.{idea,git,cache,output,temp}/**, **/{karma,rollup,webpack,vite,vitest,jest,ava,babel,nyc,cypress,tsup,build}.config.*
watch exclude:  **/node_modules/**, **/dist/**

No test files found, exiting with code 1
```

意思是：没有找到单元测试文件。

除此之外，我们还能获取一些额外的信息，比如 include 表明了单元测试文件的命令格式：

```
**/*.{test,spec}.?(c|m)[jt]s?(x)
```

我们在 `src/components` 目录下创建一个 `HelloWorld.spec.ts` 文件。

```
import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import HelloWorld from './HelloWorld.vue'

describe('测试 HelloWorld 组件', () => {

  it('测试基本功能', async () => {
    const wrapper = mount(HelloWorld)
    expect(wrapper.exists()).toBeTruthy()
  })
})
```

再次执行 `npm test` 命令

```
$ npm test

 ✓ src/components/HelloWorld.spec.ts (1)
   ✓ 测试 HelloWorld 组件 (1)
     ✓ 测试基本功能

 Test Files  1 passed (1)
      Tests  1 passed (1)
   Start at  23:34:49
   Duration  126ms
```

会提示：有一个单元测试用例通过。

这样我们的 Vue 项目单元测试环境就搭建成功，并且完成了第一个 Vue 单元测试用例

## 2 测什么

有了单元测试环境，我们可以在其中任意发挥，给自己满满的安全感。

那么我们应该如何给 Vue 组件编写单元测试呢？

我们以 OpenTiny Vue 的 [DatePicker](https://link.zhihu.com/?target=https%3A//opentiny.design/tiny-vue/zh-CN/os-theme/components/date-picker) 组件为例。

效果图：

![](https://pic1.zhimg.com/v2-1a3d9c768cf33cd44e4a7494de8d7388_b.jpg)

image.png

我们可以按照以下步骤编写单元测试用例：

### Step 1：测试默认行为

- 测试基本功能：点击日期输入框，应该弹出日期选择面板，点击日期选择面板中的日期，面板消失，并在输入框中显示选中的日期
- 测试清除日期：鼠标移到已经选择日期的输入框中，应该出现清除日期的图标按钮，点击清除日期图标，输入框中的日期被清除
- ...

### Step 2：测试每一个单独的 API

- 测试 disabled 属性：设置 disabled 属性之后，日期输入框应该变成禁用状态，点击输入框，不会弹出日期选择面板
- 测试 clearable 属性：设置 clearable 为 false 之后，鼠标移到输入框上，不显示清除日期的图标
- ...

### Steps 3：测试 API 的边界值

- 测试日期越界：设置 v-model 的值为 `"2023-07-32"`，应该不显示日期
- 测试错误格式的日期：设置 v-model 的值为数值 `20230713`，应该不显示日期
- ...

### Steps 4：测试 API 之间的组合

- 测试 type/format 三个属性之间的组合：设置 `type="week"` 和 `format="yyyy 年第 WW 周"`，日期选择面板应该变成选择周，选择 5 月 7 日到 13 日这周之后，输入框中显示的内容应该是 `2023 年第19周`
- ...

```
<tiny-date-picker
  v-model="value"
  type="week"
  format="yyyy 年第 WW 周"
></tiny-date-picker>
```

![](https://pic4.zhimg.com/v2-17708174c3c967d33aa1c4c28980c7e7_b.jpg)

image.png

## 3 怎么测

### 单测三大件：describe / test / expect

一个单元测试包含三个部分： - describe 测试套，里面可以包含多个测试用例， - it(test) 测试用例 - expect 断言语句

```
import { describe, it, expect } from 'vitest'

describe('测试 HelloWorld 组件', () => {
  it('测试基本功能', async () => {
    const wrapper = mount(HelloWorld)
    wrapper.
    expect(wrapper.exists()).toBeTruthy()
    expect(wrapper.find('.card').exists()).toBeTruthy()
  })

  it('测试 msg 属性', () => { ... })
})
```

### 模拟 Vue 组件挂载：mount 和 wrapper

每个单元测试里面测试 Vue 组件的表现是否正常，需要借助 `@vue/test-utils` 的 mount 方法，模拟组件的挂载。

```
import { mount } from '@vue/test-utils'
import HelloWorld from './HelloWorld.vue'

const wrapper = mount(HelloWorld, {
  props: {
    msg: 'OpenTiny'
  }
})
```

用 mount 函数包裹组件，得到的是一个挂载好的组件对象，该对象包含了一系列实用的方法可以用于组件的测试。

![](https://pic2.zhimg.com/v2-68aa61e27d7112f9e74e397a7123ca89_b.jpg)

image.png

比较常用的有：

- find：寻找组件内部的 DOM 节点
- findComponent：寻找子组件
- exists：判断组件或元素是否存在
- attributes：获取 DOM 节点的属性
- classes：获取 DOM 节点的 class
- ...

更多 wrapper 方法请参考：[Vue Test Utils 官网文档](https://link.zhihu.com/?target=https%3A//test-utils.vuejs.org/api/%23wrapper-methods)

### 写单测就是写断言

有了 wrapper，就可以对 Vue 组件做断言。

比如以下断言用于判断 DOM 节点 `.card` 是否存在，`toBeTruthy()`用于断言一个值是否为 true。

```
expect(wrapper.find('.card').exists()).toBeTruthy()
```

常见的断言类型有： - toBe：用于断言原始类型是否相等，比如：`expect(1+1).toBe(2)` - toBeTruthy：用于断言一个值是否为 true - not：用于否定断言，比如：`expect(1+1).toBe(3)` - toBeGreaterThan：断言实际值是否大于接收到的值 - toEqual：断言实际值是否等于接收到的值或具有相同的结构（如果是对象，则递归比较它们），注意和 `toBe` 的区别 - toContain：断言实际值是否在数组中 - toMatch：断言字符串是否与正则表达式或字符串匹配 - toHaveBeenCalled：用于测试函数是否已被调用

更多断言类型请参考：[Vitest 官网](https://link.zhihu.com/?target=https%3A//cn.vitest.dev/api/expect.html)

### 一个 DatePicker 组件的小例子

测试 DatePicker 组件的基本功能：点击日期输入框，应该弹出日期选择面板。

```
it('测试 DatePicker 组件的基本功能', async () => {
  const value = ''
  const wrapper = mount(() => <DatePicker v-model={value}></DatePicker>)
  expect(wrapper.exists()).toBe(true)

  // 没有点击日期输入框之前，没有日期选择面板
  expect(document.querySelector('.tiny-date-picker')).not.toBeTruthy()

  await wrapper.find('input').trigger('focus')

  // 点击日期输入框之后，出现日期选择面板
  expect(document.querySelector('.tiny-date-picker')).toBeTruthy()
})
```

## 3 自己动手实践吧

OpenTiny Vue 正在招募社区贡献者，欢迎加入我们

你可以通过以下方式参与贡献：

- 在 [issue](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues) 列表中选择自己喜欢的任务
- 阅读[贡献者指南](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/blob/dev/CONTRIBUTING.zh-CN.md)，开始参与贡献

你可以根据自己的喜好认领以下类型的任务： - 编写[单元测试](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues%3Fq%3Dis%253Aopen%2Bis%253Aissue%2Blabel%253Aunit-test) - 修复组件[缺陷](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues%3Fq%3Dis%253Aopen%2Bis%253Aissue%2Blabel%253Abug) - 为组件添加[新特性](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues%3Fq%3Dis%253Aopen%2Bis%253Aissue%2B%2Blabel%253Aenhancement%2B) - 完善组件的[文档](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues%3Fq%3Dis%253Aopen%2Bis%253Aissue%2Blabel%253Adocumentation)

如何贡献单元测试： - 在`packages/vue`目录下搜索`it.todo`关键字，找到待补充的单元测试 - 按照以上指南编写组件单元测试 - 执行单个组件的单元测试：`pnpm test:unit3 button`

如果你是一位经验丰富的开发者，想接受一些有挑战的任务，可以考虑以下任务：

- [✨ \[Feature\]: tree 树形控件能增加虚拟滚动功能](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues/317)
- [✨ \[Feature\]: Tree 组件增加节点连接线](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues/212)
- [✨ \[Feature\]: 增加视频播放组件](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues/294)
- [✨ \[Feature\]: 增加思维导图组件](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues/312)
- [✨ \[Feature\]: 添加类似飞书的多维表格组件](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues/321)
- [✨ \[Feature\]: 添加到 unplugin-vue-components](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues/304)
- [✨ \[Feature\]: 兼容 formily](https://link.zhihu.com/?target=https%3A//github.com/opentiny/tiny-vue/issues/303)

参与 OpenTiny 开源社区贡献，你将收获：

直接的价值：

1.  通过参与一个实际的跨端、跨框架组件库项目，学习最新的`Vite`+`Vue3`+`TypeScript`+`Vitest`技术
2.  学习从 0 到 1 搭建一个自己的组件库的整套流程和方法论，包括组件库工程化、组件的设计和开发等
3.  为自己的简历和职业生涯添彩，参与过优秀的开源项目，这本身就是受面试官青睐的亮点
4.  结识一群优秀的、热爱学习、热爱开源的小伙伴，大家一起打造一个伟大的产品

长远的价值：

1.  打造个人品牌，提升个人影响力
2.  培养良好的编码习惯
3.  获得华为云 OpenTiny 团队的荣誉和定制小礼物
4.  受邀参加各类技术大会
5.  成为 PMC 和 Committer 之后还能参与 OpenTiny 整个开源生态的决策和长远规划，培养自己的管理和规划能力
6.  未来有更多机会和可能

## 关于 OpenTiny

[OpenTiny](https://link.zhihu.com/?target=https%3A//opentiny.design/) 是一套华为云出品的企业级组件库解决方案，适配 PC 端 / 移动端等多端，涵盖 Vue2 / Vue3 / Angular 多技术栈，拥有主题配置系统 / 中后台模板 / CLI 命令行等效率提升工具，可帮助开发者高效开发 Web 应用。

核心亮点：

1.  `跨端跨框架`：使用 Renderless 无渲染组件设计架构，实现了一套代码同时支持 Vue2 / Vue3，PC / Mobile 端，并支持函数级别的逻辑定制和全模板替换，灵活性好、二次开发能力强。
2.  `组件丰富`：PC 端有 80+组件，移动端有 30+组件，包含高频组件 Table、Tree、Select 等，内置虚拟滚动，保证大数据场景下的流畅体验，除了业界常见组件之外，我们还提供了一些独有的特色组件，如：Split 面板分割器、IpAddress IP 地址输入框、Calendar 日历、Crop 图片裁切等
3.  `配置式组件`：组件支持模板式和配置式两种使用方式，适合低代码平台，目前团队已经将 OpenTiny 集成到内部的低代码平台，针对低码平台做了大量优化
4.  `周边生态齐全`：提供了基于 Angular + TypeScript 的 [TinyNG](https://link.zhihu.com/?target=https%3A//opentiny.design/tiny-ng/overview) 组件库，提供包含 10+ 实用功能、20+ 典型页面的 [TinyPro](https://link.zhihu.com/?target=https%3A//opentiny.design/pro) 中后台模板，提供覆盖前端开发全流程的 TinyCLI 工程化工具，提供强大的在线主题配置平台 [TinyTheme](https://link.zhihu.com/?target=https%3A//opentiny.design/designtheme/home)

---

欢迎加入 OpenTiny 开源社区。

添加微信小助手：opentiny-official，一起参与共建！

[OpenTiny](https://link.zhihu.com/?target=https%3A//opentiny.design/) 官网：[https://opentiny.design/](https://link.zhihu.com/?target=https%3A//opentiny.design/)

[Vue 组件库](https://link.zhihu.com/?target=https%3A//opentiny.design/tiny-vue)：[https://opentiny.design/tiny-vue](https://link.zhihu.com/?target=https%3A//opentiny.design/tiny-vue)

[Angular 组件库](https://link.zhihu.com/?target=https%3A//opentiny.design/tiny-ng)：[https://opentiny.design/tiny-ng](https://link.zhihu.com/?target=https%3A//opentiny.design/tiny-ng)

OpenTiny 代码仓库：[https://github.com/opentiny/](https://link.zhihu.com/?target=https%3A//github.com/opentiny/) （欢迎 Star ⭐）

往期文章推荐

- [OpenTiny Vue 3.9.0 版本发布：新增 3 个新组件、支持 SSR](https://link.zhihu.com/?target=https%3A//juejin.cn/post/7250639505526407205)
- [OpenTiny 3.8.0 正式发布：推出「极客黑」新主题！](https://link.zhihu.com/?target=https%3A//juejin.cn/post/7235603140262838329)
- [使用 TinyCLI 两行命令创建一个美观大气的 Admin 系统](https://link.zhihu.com/?target=https%3A//juejin.cn/post/7217828263258423356)
- [一个 OpenTiny，Vue2 Vue3 都支持！](https://zhuanlan.zhihu.com/p/643446343/edit)
- [历史性的时刻！OpenTiny 跨端、跨框架组件库正式升级 TypeScript，10 万行代码重获新生！](https://link.zhihu.com/?target=https%3A//juejin.cn/post/7215971680350093349)

参考：

- [Vitest 官网](https://link.zhihu.com/?target=https%3A//cn.vitest.dev/guide/)
- [Vue Test Utils 官网](https://link.zhihu.com/?target=https%3A//test-utils.vuejs.org/guide/)
