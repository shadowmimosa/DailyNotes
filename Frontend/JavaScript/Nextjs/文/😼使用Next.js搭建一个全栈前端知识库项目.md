---
created: 2023-12-18T10:48:43 (UTC +08:00)
tags: [前端,JavaScript,全栈]
source: https://juejin.cn/post/7262364351531810876
author: 董员外
---

# 😼使用Next.js搭建一个全栈前端知识库项目 - 掘金

> ## Excerpt
> 使用Next.js+NotionAPI数据库开发一个全栈项目🚩前端知识非常琐碎，所以想把前端知识点汇总到一起，于是有了这个项目

---
最近在做一个全栈项目，前端知识非常琐碎，所以想把前端知识点汇总到一起，无论是以后想查询某个知识点，还是学习到新的知识，都可以快速的查询和记录

全部代码已开源到GitHub；先赞后看，年入百万！

技术栈使用React的Next.js框架和Tailwind CSS，大纲如下 ![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/0e6e3f940e56487882ce6ef386b479f3~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

## 为什么是Next.js

> Next.js是一个基于React的服务端渲染框架。 这是一个用于 生产环境的 React 框架

Next.js 提供了许多优点和功能：

1.  **服务端渲染 (SSR) 和预渲染 (SSG)** ：Next.js 支持服务端渲染和预渲染，这意味着页面在服务器端生成，而不是在客户端。这有助于提高网页的加载速度和搜索引擎优化（SEO），同时也提供更好的首次渲染体验。
    
2.  **快速加载时间**：由于 Next.js 支持预渲染和服务端渲染，用户可以更快地看到页面内容，因为大部分工作在服务器端完成，减少了客户端加载所需的时间。
    
3.  **热模块替换 (HMR)** ：Next.js 支持热模块替换，这意味着在进行开发时，您可以在保持应用程序运行的同时修改代码，并立即看到变化，无需刷新页面。
    
4.  **简单的部署**：Next.js 的默认配置使得应用程序的部署非常简单。您可以使用 Vercel、Netlify 等平台将应用程序快速部署到云端，或者将其部署到自己的服务器上。
    
5.  **丰富的生态系统**：Next.js 是一个非常受欢迎的框架，拥有庞大的社区和丰富的插件，扩展和工具支持。这使得开发人员能够轻松解决常见问题，并快速构建复杂的 web 应用程序。
    
6.  **自动优化**：Next.js 内置了许多优化功能，包括自动压缩和缓存等，这些功能有助于提高应用程序的性能和用户体验。
    
7.  **支持多种数据获取方法**：Next.js 提供了多种数据获取方式，如 `getServerSideProps` 和 `getStaticProps`，使得获取数据变得简单和灵活。
    

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/f3aa7a79ecc94ade94ce733f32093c44~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

## 初始化项目

> 使用的node版本 是 16.x

### 创建项目

```js
npx create-next-app frontend-knowledge
```

没有使用TS，也没有用src目录

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/fbc654ea79254539bbb107948258f258~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

Next的Tailwind CSS内置 `postcss`、 `autoprefixer`

Tailwind CSS使用教程可以看这篇文章👉[Tailwind css 在项目中的使用与问题](https://juejin.cn/post/7260756459671207993 "https://juejin.cn/post/7260756459671207993")

### 项目结构目录

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/c3ef877e92264f5bbb550fa33f643b2a~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

-   app文件夹用于定义路由，`layout.tsx`和`page.tsx`文件。当用户访问应用程序的根目录 `/`时，访问到的就是 app下的page.jsx.

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/6f8a1eefc2f549f494cd303b580fa1d2~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

每个文件夹表示一个路由，映射到一个URL ![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/a94c249f16fe48ce966efe6a25aa9ba8~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

-   pages/api 用于编写next后端接口

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/1012c7e88695499a91d30b9cbcac7875~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

## 前端页面

### app文件路由

Next 中 app里的每一个文件就是一个路由

-   根目录 `http://localhost:3000/`，对应 app下的page.jsx

`Layout.jsx` 是一个用于组织页面结构和共享组件的重要概念。Layout 可以看作是一个组件包裹器，它包含了页面共享的部分，例如页眉（Header）、页脚（Footer）和导航栏（Navigation）或者 `page.jsx`；`layout.jsx`相当于`page`的布局组件.

前端知识库 无论是首页还是子路由都需要有一个左侧导航栏，所以可以把导航栏放到`Layout.jsx`页面，page页面会映射到 children 里

```jsx
import '@/styles/globals.css'; import SlideBar from '@/components/SlideBar'; function RootLayout({ children }) { return ( <html lang='en'> <body > <main className='app'> <SlideBar /> <div className='w-full h-full'>{children}</div> </main> </body> </html> ) }
```

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/71c9a89ec3ea4c59922dcad6f8c10e9a~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

-   二级目录 `http://localhost:3000/category`，对应 `app/category`下的page.jsx ![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/dd90b223bc814fe29829347fc470ea61~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

### "use client"

`"use client"` 指令是声明服务器和客户端组件模块图之间边界的约定。

NextJS 13默认情况下，App 文件夹内的 所有组件都是服务器组件。并且 服务器组件 不能使用 **useState、useEffect** 等客户端特性。

```jsx
'use client' import { useState, useEffect } from "react"; import Image from 'next/image'; const Home = () => { return ( <div> <h1>Welcome to Next.js</h1> <p>This is the home page content.</p> {/* 使用 Next Image 组件 */} <Image src="/path/to/your/image.jpg" alt="Description of the image" width={300} height={200} /> </div> ); }; export default Home;
```

### 组件引入

**引入路由 `Link`**

```jsx
import React from 'react'; import Link from 'next/link'; const Home = () => { return ( <div> <h1>Welcome to Next.js</h1> <p>This is the home page content.</p> {/* 使用 Link 组件实现导航链接 */} <Link href="/category"> 跳转路由 </Link> </div> ); }; export default Home;
```

`Link` 组件使用客户端导航而不是传统的页面刷新。当用户点击链接时，只有目标页面的内容会被加载，而不会重新加载整个应用程序

**Image 图片引入**

在 `Image` 组件中，您需要提供以下属性：

-   `src`：图像的路径。它可以是本地路径或远程 URL。
-   `alt`：图像的替代文本，用于辅助技术和当图像无法加载时显示。
-   `width`：图像的宽度，应以像素为单位提供。
-   `height`：图像的高度，应以像素为单位提供。

```jsx
import React from 'react'; import Image from 'next/image'; const Home = () => { return ( <div> <h1>Welcome to Next.js</h1> <p>This is the home page content.</p> {/* 使用 Next Image 组件 */} <Image src="/path/to/your/image.jpg" alt="Description of the image" width={300} height={200} /> </div> ); }; export default Home;
```

## Notion数据库

Notion 不仅是一款个人笔记软件，还可以当作数据库使用 [Notion在线笔记](https://link.juejin.cn/?target=https%3A%2F%2Fwww.notion.so%2F "https://www.notion.so/")

可以通过安装 Notion API SDK 来进行连接数据库，获取数据

### 创建数据库

创建一个DATABASE数据库 ![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/52206b545387468a85ef0abe4ef6c13f~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp) 然后再创建各个字段

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/721b8b0ec4fe4bed98cdcaaa500b0991~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

### 创建应用集成，获取密钥

去Notion创建一个应用集成，获取 API Key👉[Notion Developers](https://link.juejin.cn/?target=https%3A%2F%2Fwww.notion.so%2Fmy-integrations "https://www.notion.so/my-integrations")

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/e0927a455bd1418cb194ba36f2b568c5~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

数据库就创建好了，接下来就可以再Next里连接数据库进行获取数据了

## 连接数据库

### 创建Notion服务

安装Notion API 客户端

```js
npm install @notionhq/client
```

创建一个 NotionServer 服务，将请求数据库的方法进行封装

`lib/NotionServer.js`

```js
import { Client } from "@notionhq/client"; const auth = process.env.NOTION_AUTH; const database = process.env.NOTION_DATABASE_ID; export default class NotionService { constructor() { this.client = new Client({ auth }); } async query() { const response = await this.client.databases.query({ database_id: database, }); return response.results; } }
```

`NOTION_AUTH`是数据库集成的密钥

`NOTION_DATABASE_ID`是notion链接上面的 id

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/46efe1596770459383cb454e42db34a5~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

再新建一个`pages/api/question.js`路由，调用NotionServer查询服务

```js
import NotionServer from "../../lib/NotionServer"; const notionServer = new NotionServer(); export default async function handler( req, res ) { const data = await notionServer.query(); res.status(200).json(data); }
```

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/976546e491dc4556814e17ea31996e3e~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp) 在浏览器中输入 `localhost:3000/api/question` 就可以看到获取的数据，此时数据还比较杂乱，可以处理一下，返回自己想要的数据

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/d435ed59df1543429e4429535d924aeb~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

### 展示到前端页面

在首页的 `page.jsx页面里`使用 fetch方法获取数据，前端页面

```jsx
"use client"; import { useState, useEffect } from "react"; import QuestionCard from "@/components/QuestionCard" function Home() { const [questionList, setQuestionList] = useState([]); const [jsList, setJsList] = useState([]); const getQuestionList = () => { fetch('/api/question') .then((res) => res.json()) .then((res) => { if (res) { setQuestionList(res.sort((a, b) => a.id - b.id)); } }) .catch((error) => { console.error(error); }); }; useEffect(() => { getQuestionList(); }, []); useEffect(() => { const jsItems = questionList.filter(item => item.tags === "JavaScript"); setJsList(jsItems); }, [questionList]); return ( <div className="w-full h-full overflow-auto"> <section className=" gap-4 p-6 space-y-4 md:columns-2"> <QuestionCard questionList={jsList} type="JavaScript" /> </section> </div> ) } export default Home
```

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/4f45d5968d664f3ea6fd20caa743f816~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

## Markdown数据渲染

数据存储采用的是Markdown格式，所以就需要第三方的Markdown插件进行展示

### markdown-it 数据展示

安装 `markdown-it`

```js
npm install markdown-it
```

```jsx
'use client' import { useState,useEffect } from 'react' // 1. 引入markdown-it库 import markdownIt from 'markdown-it' // 2. 生成实例对象 const md = new markdownIt(); function DialogCard({data,closeDialog}) { const [htmlString, setHtmlString] = useState('') // 存储解析后的html字符串 // 3. 解析markdown语法 const parse = (data) => setHtmlString(md.render(data.explanation)); useEffect(()=>{ parse(data) },[]) return ( <div className='show w-full mt-1 flex-grow overflow-auto '> <div className='w-full' dangerouslySetInnerHTML={{ __html: htmlString }} // 将html字符串解析成真正的html标签 /> </div> ) } export default DialogCard
```

Tailwind css 默认将所有的 h1-h6和ul,li 基础样式重写，所以markdown展示的样式和普通文本没有区别 ![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/fd80d950529e43689f18cd3f77459987~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

官方的Tailwind CSS Typgraphy插件提供了一组 `prose` 类，可以使用它们为任何不受控制的**普通HTML**添加漂亮的排版默认值，**例如从Markdown呈现的HTML或从CMS中提取的HTML。**

安装：

```js
npm install -D @tailwindcss/typography
```

然后将插件添加到 `tailwind.config.js` 文件中：

```js
/** @type {import('tailwindcss').Config} */ module.exports = { plugins: [ require("@tailwindcss/typography") ], }
```

最后在 div 添加 `prose` 类

```js
<div className='prose w-full' dangerouslySetInnerHTML={{ __html: htmlString }} // 将html字符串解析成真正的html标签 />
```

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/d6094cbf11b5484e90a4f5f88a68c667~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

### 代码高亮

`markdown-it` 默认的代码块格式没有样式，可以安装highlight 插件进行添加代码块样式

```js
npm install highlight.js
```

然后引入样式文件,在生成实例时，进行初始化

```js
import hljs from "highlight.js"; import 'highlight.js/styles/monokai-sublime.css' // 2. 生成实例对象 const md = new markdownIt({ highlight: function (str, lang) { if (lang && hljs.getLanguage(lang)) { try { return hljs.highlight(str, { language: lang }).value; } catch (_) {} } return ""; // 使用额外的默认转义 }, });
```

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/174cd91ed92747719380bfe5aaae50f4~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

写到这里项目也算是完成了，源码放到了GitHub上👨🦼➡️[frontend-konwledge](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdongyuanwai%2Ffrontend-interview-konwledge "https://github.com/dongyuanwai/frontend-interview-konwledge") 欢迎大家 star🌟🌟🌟

## 部署到Vercel

使用github账号登录到 [Vercel](https://link.juejin.cn/?target=https%3A%2F%2Fvercel.com%2Fnew "https://vercel.com/new") 上

找到项目，选择导入

![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/63ef296840644a17a71c416a95e780f5~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

添加环境变量名和值，相当于`.env`里的值 ![image.png](%F0%9F%98%BC%E4%BD%BF%E7%94%A8Next.js%E6%90%AD%E5%BB%BA%E4%B8%80%E4%B8%AA%E5%85%A8%E6%A0%88%E5%89%8D%E7%AB%AF%E7%9F%A5%E8%AF%86%E5%BA%93%E9%A1%B9%E7%9B%AE%20-%20%E6%8E%98%E9%87%91/97a24ec8f5f646dc9678e66664ff9893~tplv-k3u1fbpfcp-zoom-in-crop-mark1512000.awebp)

部署成功后就可以访问了

更新新代码时，不用再次部署，它会自动更新到最新代码。只不过国内访问可能会被🧱墙

在线预览地址🏂 [前端知识点 (frontend-konwledge.vercel.app)](https://link.juejin.cn/?target=https%3A%2F%2Ffrontend-interview-konwledge.vercel.app%2F "https://frontend-interview-konwledge.vercel.app/")

## 最后

本文只介绍了项目中使用到的Next技巧，和其他的一些使用教程

像一些SSR，动态路由，元数据等使用方式，准备在项目优化时配合着真实的案例再记录

> Tailwind css教程可以看这篇文章👀[Tailwind css 在项目中的使用与问题](https://juejin.cn/post/7260756459671207993 "https://juejin.cn/post/7260756459671207993")
> 
> 项目源码放到了GitHub上👨🦼➡️[frontend-konwledge](https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fdongyuanwai%2Ffrontend-interview-konwledge "https://github.com/dongyuanwai/frontend-interview-konwledge")
> 
> 在线预览地址🏂 [前端知识点 (frontend-konwledge.vercel.app)](https://link.juejin.cn/?target=https%3A%2F%2Ffrontend-interview-konwledge.vercel.app%2F "https://frontend-interview-konwledge.vercel.app/")
