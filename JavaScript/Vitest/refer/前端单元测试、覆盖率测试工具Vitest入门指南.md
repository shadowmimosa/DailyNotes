---
created: 2023-11-19T21:57:57 (UTC +08:00)
tags: [前端单元测试工具]
source: https://blog.csdn.net/qq_28255733/article/details/132479859
author: 成就一亿技术人!
---

# 【前端】前端单元测试、覆盖率测试工具 Vitest 入门指南*前端单元测试工具*莫诺库诺的博客-CSDN 博客

> ## Excerpt
>
> 文章浏览阅读 283 次。单元测试的重要性不言而喻，可以很大程度的减少一些 bug 的产生。在前端项目中，有很多用于单元测试的工具，如最常见的`Jest`。但对于由 vite 构建的前端项目而言，使用 vite 配套的 vitest 会更加方便、舒适。[官方文档](https://cn.vitest.dev/guide/)是最好的入门方式，这篇文章记录在入门过程中可能遇到的一些问题，方便想了解的人更快速的上手。本文暂时只介绍单元测试和覆盖率测试的使用方法。\_前端单元测试工具

---

## 前言

[单元测试](https://so.csdn.net/so/search?q=%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95&spm=1001.2101.3001.7020)的重要性不言而喻，可以很大程度的减少一些 bug 的产生。在前端项目中，有很多用于单元测试的工具，如最常见的`Jest`。但对于由 vite 构建的[前端项目](https://so.csdn.net/so/search?q=%E5%89%8D%E7%AB%AF%E9%A1%B9%E7%9B%AE&spm=1001.2101.3001.7020)而言，使用 vite 配套的 vitest 会更加方便、舒适。[官方文档](https://cn.vitest.dev/guide/)是最好的入门方式，这篇文章记录在入门过程中可能遇到的一些问题，方便想了解的人更快速的上手。本文暂时只介绍单元测试和覆盖率测试的使用方法。

## 安装与配置

### 安装方法

- npm  
  `npm install -D vitest`
- yarn  
  `yarn add -D vitest`

### 基础配置

在`package.json`文件中，添加以下代码：

```
{
  "scripts": {
    "test": "vitest"
  }
}
```

### 测试 Vitest 是否能正常工作

按照官方文档的示例，准备两个文件 sum.ts 和 sum.test.ts(可以在项目根目录下创建一个 test 文件夹，专门用来存放测试文件)：

```
// sum.ts
export function sum(a, b) {
  return a + b
}
```

```
// sum.test.ts
import { expect, test } from 'vitest'
import { sum } from './sum'

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3)
})
```

然后，在终端中运行指令`npm run test`(或者`yarn test`)。  
如果没有意外，那么将出现以下结果：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/4aaa63b55ee2463c9f56de7cb9b2cdf8.png)

### 关键字解释

如果你之前没有用过 Jest，那么对于`sum.test.ts`文件中的`test`、`expect`、`toBe`方法，肯定一头雾水。

1.  test（别名为 it）  
    test 方法是用于编写单元测试的函数。test 方法接受两个参数：测试名称和测试函数。语法如下：

```
test(name: string, testFn: Function, timeout?: number | TestOptions): Promise<void>;
```

- name  
  接收一个字符串，作为测试的名称显示在控制台中。一般用来描述该项测试的内容。
- testFn  
  是一个异步或同步的函数，用于执行测试逻辑和断言。
- timeout  
  可选参数，用于设置测试的超时时间（以毫秒为单位）。如果测试在超时时间内没有完成，则会失败并抛出错误。

2.  expect  
    expect 方法是用于创建断言的函数。断言是一种用于验证代码的行为和输出是否符合预期的方式。  
    expect 方法的基本语法如下：

```
expect(actual).matcher(expected)
```

其中，`actual`是一个表达式或变量，表示要检查的实际值。`matcher`是一个函数，表示要使用的比较方法。`expected`是一个值或对象，表示期望的结果。  
在本例中，`expect(sum(1, 2)).toBe(3)`表示使用`expect`方法来测试`sum`函数是否能正确地将两个数字相加。此处使用 `toBe`来进行断言，这是 Vitest 提供的一个匹配器函数，用于比较实际值和期望值是否严格相等。

### 配合 IDE 使用

Vitest 在各大主流前端 IDE 中都有对应的插件供开发者更方便的使用测试功能，这里以 vscode 为例，直接在插件市场搜索 Vitest，点击安装即可。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/457dcd17704b4d7d8545242ac4ddee07.png)  
然后打开`sum.test.ts`文件，可以看到 test 方法的那一行的左边出现了一个图标：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/d36e7b9af14347919cc5e227a20f99a8.png)  
点击该图标即可运行该文件下的测试代码，右键该图标可以进行更多选择，比如调试。

## 实际应用

### 测试文件准备

所谓单元测试，指的是对**最小测试单元**进行测试。比如在项目中写了一个计算文本宽度的方法，方法写好之后如果直接拿过去用，除非是经过验证的现有方法，否则是容易出现处理上的漏洞的。因此我们可以把这个方法单独提取出来，放到测试文件夹中。

1.  首先，在项目根目录下创建一个`test`文件夹，并在其下创建两个文件，分别为`util.ts`、`util.test.ts`。打开`util.ts`，写入以下代码：

```
export function getTextWidth(str: string | number): number {
if (!str) return 0;
// 如果str是数字，则转换为字符串
if (typeof str === 'number') {
str = str.toString();
}
if (str.length < 3) {
return 40;
}
let regx = /^[0-9]+.?[0-9]*$/;
let flexWidth = 0;
for (const char of str) {
if ((char >= 'A' && char <= 'Z') || (char >= 'a' && char <= 'z')) {
// 如果是英文字符，为字符分配10个单位宽度
flexWidth += 10;
} else if (char >= '\u4e00' && char <= '\u9fa5') {
// 如果是中文字符，为字符分配15个单位宽度
flexWidth += 15;
} else if (regx.test(char)) {
flexWidth += 9;
} else {
// 其他种类字符，为字符分配7个单位宽度
flexWidth += 7;
}
}
return flexWidth;
}
```

2.  然后打开`util.test.ts`，写入以下代码：

```
// textWidth.test.js
import { expect, test, describe } from 'vitest'
import { getTextWidth } from './utilTemp'

describe('getTextWidth function', () => {
  // test for empty string
  test('returns 0 if the input is an empty string', () => {
    expect(getTextWidth('')).toBe(0)
  })

  // test for single character
  test('returns 40 if the input is a single character', () => {
    expect(getTextWidth('a')).toBe(40)
    expect(getTextWidth('中')).toBe(40)
    expect(getTextWidth(1)).toBe(40)
  })

  // test for numbers
  test('returns the correct width for numbers', () => {
    expect(getTextWidth(123)).toBe(27)
    expect(getTextWidth(3.14)).toBe(34)
    expect(getTextWidth(-100)).toBe(34)
  })

  // test for english characters
  test('returns the correct width for english characters', () => {
    expect(getTextWidth('Hello')).toBe(50)
    expect(getTextWidth('World')).toBe(50)
    expect(getTextWidth('Hello World')).toBe(107)
  })

  // test for chinese characters
  test('returns the correct width for chinese characters', () => {
    expect(getTextWidth('你好')).toBe(40)
    expect(getTextWidth('世界')).toBe(40)
    expect(getTextWidth('你好世界')).toBe(60)
  })

  // test for mixed characters
  test('returns the correct width for mixed characters', () => {
    expect(getTextWidth('Hello你好')).toBe(80)
    expect(getTextWidth('World世界')).toBe(80)
    expect(getTextWidth('Hello World你好世界')).toBe(167)
  })
})
```

然后在 vscode 里面点击运行，或者在命令行里执行`yarn test(npm run test)`，就能看到结果了：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/89654b0d6a0d481ba9a40aea6b07bedf.png)

### 测试覆盖率

代码覆盖率是一种用于评估代码的质量和完整性的指标，它表示代码中有多少比例被测试用例所覆盖。测试覆盖率的工具可以帮助开发者生成和查看覆盖率报告，从而发现代码中的潜在问题和改进点。

1.  先去 package.json 中添加以下代码：

```
{
  "scripts": {
    "coverage": "vitest run --coverage"
  }
}
```

2.  安装覆盖率工具  
    Vitest 提供两种覆盖率工具：`v8`和`istanbul`。这两种工具的区别感兴趣可以自己去了解，这里不做说明。默认情况下，Vitest 启用 v8，因此需要安装 v8 工具：  
    `yarn add -D @vitest/coverage-v8`。
3.  开启覆盖率测试  
    打开`vite.config.ts`，在`defineConfig`下添加以下配置：

```
{
test: {
reporters: ['default', 'html'],
coverage: {
enabled: true,
provider: 'v8',
cleanOnRerun: true,
reporter: ['text', 'json', 'html'],
},
},
}
```

> 这里需要说明的是，官方说在`vite.config.ts`的顶部添加三斜线指令`/// <reference types="vitest" />`即可在 vite 的配置文件里添加 Vitest 的选项，但我试了，会报类型错误，所以我直接把 defineConfig 的导入改为了`import { defineConfig } from 'vitest/config';`。或者你可以单独新建一个`vitest.config.ts`文件进行配置。

配置完成后，运行`yarn test`，就能看到结果：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/45284c268c2946eead0380717bffedf7.png)  
可以看到，`utilTemp.ts`这一行对应的列都为 100，说明覆盖率测试通过。（当然不一定非得是百分百才算通过，但一般规定至少得 90%）

### 通过 UI 查看结果

在命令行里查看测试结果相对来说不够直观，因此 Vitest 提供一个漂亮的 UI 界面来查看并与之交互。Vitest 的 UI 界面是可选的，你可以通过以下方式安装：

```
yarn add -D @vitest/ui
```

或者

```
npm i -D @vitest/ui
```

安装完后，执行指令：`yarn test --ui`，就会开启一个服务器，然后会在浏览器里自动打开 Vitest UI 的界面：  
![在这里插入图片描述](https://img-blog.csdnimg.cn/c073b7824ef3439090fbe74bd01207b9.png)  
点击右侧的文件，可以详细查看测试代码的覆盖情况，绿色代表已覆盖，红色代表未覆盖，说明需要修改测试代码以保证全覆盖。  
![在这里插入图片描述](https://img-blog.csdnimg.cn/310322bb0c384ca184e4a3ac70f304e5.png)

## 结语

至此，有关 Vitest 的入门操作已介绍完毕。当然，Vitest 的功能远不止如此，更多的功能，比如组件测试、快照测试、以及更多的配置、API 等，请自行转到官方文档了解。
