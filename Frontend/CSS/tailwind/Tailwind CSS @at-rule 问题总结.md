# Tailwind CSS 中的未知 at 规则问题及解决方案

## 问题概述

在使用 Tailwind CSS 时，VSCode 编辑器可能会显示一个关于未知 at 规则`@tailwind`的警告。这表示 VSCode 不识别`@tailwind`指令，该指令用于将 Tailwind 的基类、组件、实用工具样式注入到 CSS 文件中。

## 解决方案

以下方法可以解决此警告问题：

1. **配置 VSCode 忽略警告**
   在`settings.json`文件中添加以下配置：
   ```json
   {
     "css.lint.unknownAtRules": "ignore"
   }
   ```
   如果使用 SCSS 或其他 CSS 预处理器，需要相应调整设置，例如：
   ```json
   {
     "scss.lint.unknownAtRules": "ignore"
   }
   ```
2. **为 CSS 语言服务添加自定义数据**
   在`.vscode`文件夹中创建`css_custom_data.json`文件，内容如下：
   ```json
   {
     "version": 1.1,
     "atDirectives": [
       {
         "name": "@tailwind",
         "description": "Use the @tailwind directive to insert Tailwind's `base`, `components`, `utilities`, and `screens` styles into your CSS."
       }
     ]
   }
   ```
   然后在`settings.json`文件中引用此文件：
   ```json
   {
     "css.customData": [".vscode/css_custom_data.json"]
   }
   ```
3. **安装 Tailwind CSS IntelliSense 扩展**
   为 VSCode 安装 Tailwind CSS IntelliSense 扩展，提供增强的 Tailwind CSS 编辑体验。安装后，在`settings.json`中配置：
   ```json
   {
     "files.associations": {
       "*.css": "tailwindcss"
     }
   }
   ```
4. **使用@import 指令替换@tailwind**
   可以用`@import`指令替换`@tailwind`指令，以避免 VSCode 中的未知 at 规则警告。但请注意，这可能会增加构建时间并使 CSS 文件变大。
   ```css
   @import 'tailwindcss/base';
   @import 'tailwindcss/components';
   @import 'tailwindcss/utilities';
   ```
5. **使用 PostCSS 语言支持扩展**
   安装 PostCSS Language Support 扩展，并将 CSS 文件与 PostCSS 关联：
   ```json
   {
     "files.associations": {
       "*.css": "postcss"
     }
   }
   ```

## Tailwind 指令简介

Tailwind 指令是 Tailwind CSS 项目中使用的自定义 at 规则，提供特殊功能。Tailwind 有以下四个指令：

- `@tailwind`：用于插入 Tailwind 的基类、组件、实用工具和变体样式。
- `@apply`：允许将实用工具类应用于任何 CSS 选择器。
- `@layer`：用于定义自定义组件和实用工具的层。
- `@config`：用于在 CSS 文件中直接配置 Tailwind。

---

以上内容基于 GitHub 上的讨论[tailwindlabs/tailwindcss #13881](https://github.com/tailwindlabs/tailwindcss/discussions/13881)和 Byby.dev 的文章[《How to fix the unknown at rule @tailwind warning》](https://byby.dev/at-rule-tailwind)整理而成。
