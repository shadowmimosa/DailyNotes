<font size=4 face='楷体'>

## TailwindCSS 入门指南

### CSS 开发范式演进

1. 传统三层架构

- 结构层：HTML 负责页面结构和内容
- 样式层：CSS 负责页面样式和外观
- 交互层：JavaScript 负责页面交互和行为

2. 开发范式对比
   | 特点 | 语义化 CSS | 原子化 CSS (Utility-first) |
   |------|------------|---------------------------|
   | 可读性 | 类名语义清晰 | 需要熟悉原子类命名 |
   | 维护性 | 需要维护大量 CSS | 复用性强，减少重复代码 |
   | 灵活性 | 较低 | 高度灵活 |
   | 学习成本 | 较低 | 需要熟悉工具类 |
   | 文件体积 | 较大 | 按需生成，体积小 |

### TailwindCSS 特性

1. 版本特性

- v2.0

  ```css
  // @apply 支持
  .btn {
    @apply bg-indigo-500 hover:bg-indigo-600;
  }

  // 暗色模式支持
  <div class="bg-white dark:bg-black">
    <h1 class="text-gray-900 dark:text-white">标题</h1>
  </div>
  ```

- v3.0
  - Just-in-Time 引擎默认启用
  - 编译速度显著提升

2. 核心优势

- 统一页面样式
- 响应式设计
- 按需编译
- 高度可定制

### 实战示例

1. 基础布局

```html
<div
  class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-lg flex items-center space-x-4"
>
  <div class="shrink-0">
    <img class="h-12 w-12" src="/img/logo.svg" alt="Logo" />
  </div>
  <div>
    <div class="text-xl font-medium text-black">标题</div>
    <p class="text-slate-500">描述文本</p>
  </div>
</div>
```

2. 响应式设计

```html
<div class="md:flex">
  <div class="p-5">
    <div class="text-2xl md:text-3xl lg:text-4xl">响应式文本</div>
  </div>
</div>
```

3. 暗色模式

```html
<div class="bg-white dark:bg-gray-800 rounded-3xl shadow-md">
  <span class="text-sky-500 dark:text-sky-300"> 自适应暗色模式文本 </span>
</div>
```

### 配套生态

1. UI 框架集成

- NuxtUI: 基于 TailwindCSS 的 Nuxt 组件库
- 配置示例：

```javascript
export default defineAppConfig({
  ui: {
    primary: 'green',
    gray: 'cool',
  },
})
```

2. 开发工具

- VS Code 插件
- PostCSS 插件
- 主题构建器

### 最佳实践

1. 组件封装

- 将常用组合封装为组件
- 使用 @apply 抽取公共样式

2. 响应式设计

- 移动优先原则
- 使用断点前缀

3. 主题定制

- 配置 tailwind.config.js
- 扩展颜色和间距系统

### Reference

- [时机已到! 原子化接替语义化声明，TailwindCSS 使用指南](https://cloud.tencent.com/developer/article/2334240)
- [TailwindCSS 官方文档](https://tailwindcss.com/docs)

**Created On 2024.12.20**
</font>
