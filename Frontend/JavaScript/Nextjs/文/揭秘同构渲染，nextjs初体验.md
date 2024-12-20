---
created: 2023-12-18T10:49:16 (UTC +08:00)
tags: [渲染,Next.js]
source: https://zhuanlan.zhihu.com/p/564818428?utm_id=0
author: 
---

# 揭秘同构渲染，nextjs初体验 - 知乎

> ## Excerpt
> 一、客户端渲染（一）概述说到渲染方式，我们使用最多的就是基于客户端渲染的前端框架，例如 Angular，React，Vue 等。 网页被当成了独立的应用程序（SPA，Single Page Application），前端团队接管了所有页面渲染…

---
## 一、客户端渲染

## （一）概述

说到渲染方式，我们使用最多的就是基于客户端渲染的前端框架，例如 Angular，React，Vue 等。

网页被当成了独立的应用程序（SPA，Single Page Application），前端团队接管了所有页面渲染的事，后端团队只负责提供所有数据查询与处理的API。大体流程是这样的：

1.  浏览器请求URL前端服务器直接返回一个**空的静态HTML文件**（不需要任何查数据库和模板组装），这个HTML文件中加载了很多渲染页面需要的 **JavaScript 脚本**和 **CSS 样式表**，
2.  浏览器拿到 HTML 文件后开始加载脚本和样式表，并且执行脚本，这个时候脚本请求后端服务提供的API，获取数据，获取完成后将数据**通过JavaScript脚本动态的将数据渲染到页面中**，完成页面显示。

![](%E6%8F%AD%E7%A7%98%E5%90%8C%E6%9E%84%E6%B8%B2%E6%9F%93%EF%BC%8Cnextjs%E5%88%9D%E4%BD%93%E9%AA%8C%20-%20%E7%9F%A5%E4%B9%8E/v2-5dee5d47309b037da87694c14955dced_b.jpg)

## （二）优点：

1.局部刷新。

当用户点击时，不会形成频繁的跳转。

2.前后端分离。

开发效率高。

## （二）缺点：

**1.首屏慢。**

客户端渲染，需要先得到一个空的HTML页面，这个时候页面已经进入白屏，之后还需要经过加载并执行 JavaScript、请求后端服务器获取数据、JavaScript 渲染页面几个过程才可以看到最后的页面。

特别是在复杂应用中，由于需要加载 JavaScript 脚本，越是复杂的应用，需要加载的 JavaScript 脚本就越多、越大，这会导致应用的首屏加载时间非常长，进而降低了体验感。

**2\. 不利于SEO。**

大多数情况下，爬虫只会读取服务端直出的内容，而不会执行网页中的脚本。从爬虫的角度来看，它也很难去捕获脚本中的绑定的事件和各种交互，而且，万一你的脚本中有死循环呢。

## 二、服务端渲染

## （一）概述

为了解决单页应用的不足，我们可能会想到采用**服务端直出 html** 方案，即：在服务器端执行前端框架代码，生成网页内容并将渲染好的网页内容返回给客户端，客户端只负责展示。即**纯服务端渲染**。

纯服务端渲染(server side render)，简称**SSR**，就是在浏览器请求页面URL的时候，服务端将我们需要的HTML文本组装好，并返回给浏览器，这个HTML文本被浏览器解析之后，不需要经过 JavaScript 脚本的执行，即可直接构建出希望的 DOM 树并展示到页面中。这个**服务端组装HTML的过程，叫做服务端渲染。**

![](%E6%8F%AD%E7%A7%98%E5%90%8C%E6%9E%84%E6%B8%B2%E6%9F%93%EF%BC%8Cnextjs%E5%88%9D%E4%BD%93%E9%AA%8C%20-%20%E7%9F%A5%E4%B9%8E/v2-5f92a38f8945fb762c962a1192e9b321_b.jpg)

## （二）示例

服务端渲染的原理非常简单，就是直出静态HTML。我们可以通过express简单实现。如下：

```text
const express = require('express'); const app = express(); app.get('/', function (req, res) { res.send(` <html> <head> <title>服务端渲染（SSR）</title> </head> <body> <p>hello world</p> </body> </html> `); }); app.listen(3001, function () {= console.log('listen:3001');= });
```

## （三）优点

1.  **首屏快**

相对于客户端渲染，服务端渲染在浏览器请求URL之后已经得到了一个带有数据的HTML文本，浏览器只需要解析HTML，直接构建DOM树就可以。

![](%E6%8F%AD%E7%A7%98%E5%90%8C%E6%9E%84%E6%B8%B2%E6%9F%93%EF%BC%8Cnextjs%E5%88%9D%E4%BD%93%E9%AA%8C%20-%20%E7%9F%A5%E4%B9%8E/v2-bbe0522ab8aa1518822ded43055cb610_b.jpg)

**2.利于SEO**

其实就是有利于爬虫来爬你的页面。

如果采用服务端渲染，不仅可以提升搜索引擎的排名，而且可以**动态设置网页标题、关键字以及描述等meta信息**，使网页在各个平台都更加友好。

## （四）缺点

1.  全局刷新

页面之间的跳转都是全局跳转。

**即使每次更新页面的一小的模块，都需要重新请求一次页面，重新查一次数据库，重新组装一次HTML。**

## 三、同构渲染

## （一）概述

**首先，我们整体对比一下服务端渲染和客户端渲染的优劣：**

|  | 客户端渲染 | 服务端渲染 |
| --- | --- | --- |
| 优点 | 局部刷新 | 首屏快 |
| 前后端分离 | 利于SEO |
| 缺点 | 首屏慢 | 全局刷新 |
| 不利于SEO | 前后端不分离 |

对比一下就会发现一个很有意思的事，服务端渲染的优点就是客户端渲染的缺点，服务端渲染的缺点同时也是客户端渲染的优点。二者非常互补。

只实现 SSR 其实没啥意义，技术上没有任何发展和进步，否则 SPA 技术就不会出现。

但是单纯的 SPA又不够完美，所以最好的方案就是这两种体验和技术的结合，**第一次访问页面是服务端渲染，基于第一次访问后续的交互就是 SPA 的效果和体验**，**还不影响SEO 效果**，这就有点完美了。我们把这种客户端渲染和服务器端渲染结合的方案，叫做**同构渲染**。

**前后端同构**是指在前后端维护同一份代码。它是在SPA的基础上，利用服务端渲染（SSR）直出首屏，解除单页面应用（SPA）在首屏渲染上面临的窘境。

## （二）优点

1.  首屏快。纯服务端直出的首屏。
2.  利于SEO。可以动态设置meta标签。
3.  可以实现局部刷新。SPA的站内体验。
4.  前后端解耦。

## （三）缺点

**1.代码复杂度增加。**

为了实现服务端渲染，应用代码中需要兼容服务端和客户端两种运行情况，而一部分依赖的外部扩展库却只能在客户端运行，需要对其进行特殊处理，才能在服务器渲染应用程序中运行。

2.占用服务端资源

由于服务器增加了渲染HTML的需求，使得原本只需要输出静态资源文件的nodejs服务，新增了数据获取的IO和渲染HTML的CPU占用，如果流量突然暴增，有可能导致服务器down机，因此需要使用响应的缓存策略和准备相应的服务器负载。

3.涉及构建设置和部署的更多要求

与可以部署在任何静态文件服务器上的完全静态单页面应用程序 (SPA) 不同，服务器渲染应用程序肯定不能运行在Nginx中，而是需要部署在Node.js server 运行环境。

## （四）核心原理

**node server** 接收客户端请求，得到当前的req url path,然后在已有的路由表内查找到对应的组件，拿到需要请求的数据，**将数据作为 props、context或者store 形式传入组件**，然后基于 react 内置的服务端渲染api renderToString() or renderToNodeStream() **把组件渲染为 html字符串**或者 stream 流, 在把最终的 html 进行输出前需要将数据注入到浏览器端(注水)，server 输出(response)后浏览器端可以得到数据(脱水)，浏**览器开始进行渲染和节点对比**，然后执行组件的componentDidMount **完成组件内事件绑定和一些交互**，浏览器重用了服务端输出的 html 节点，整个流程结束。

![](%E6%8F%AD%E7%A7%98%E5%90%8C%E6%9E%84%E6%B8%B2%E6%9F%93%EF%BC%8Cnextjs%E5%88%9D%E4%BD%93%E9%AA%8C%20-%20%E7%9F%A5%E4%B9%8E/v2-39a18edb171d4df1b088cd389323e7a8_b.jpg)

## （一）概述

**如果采用第三方同构框架，可以大大降低我们的开发难度。**在react生态内，[Next.js](https://link.zhihu.com/?target=https%3A//nextjs.org/)和[Umi](https://link.zhihu.com/?target=https%3A//v3.umijs.org/zh-CN/docs)都是比较高效的同构渲染解决方案。

Next 和 Umi 都完全支持构建用于生产的 React 应用程序，几乎不需要配置。 Next 对编写 CSS 和自定义 webpack 配置有更完整的支持，而 Umi 对 webpack 配置的支持并不多。

Next 有自己的一组插件,Umi的内部功能都是第三方插件。

目前Next的使用人数要比Umi更多，其生态也占优。我们这里主要研究Next.js。

当我们使用了Nextjs，我们要关注的开发流程就会变得像下面这样简单。

![](%E6%8F%AD%E7%A7%98%E5%90%8C%E6%9E%84%E6%B8%B2%E6%9F%93%EF%BC%8Cnextjs%E5%88%9D%E4%BD%93%E9%AA%8C%20-%20%E7%9F%A5%E4%B9%8E/v2-578cebcb499bccfb50d2f59f51af2e12_b.jpg)

## （二）快速创建next.js项目

1.  通过脚手架的方式

需要自己配置依赖和启动脚本。

```text
npx create-next-app@latest yarn create next-app --typescript
```

1.  通过脚手架+克隆demo项目的方式

```text
npx create-next-app nextjs-blog --use-npm --example "https://github.com/vercel/next-learn/tree/master/basics/learn-starter" --typescript
```

## （三）路由

1.  页面路由

Next.js 没有路由配置文件。创建页面之前首先需要在项目下创建一个 pages 的文件夹。**这个文件夹必须叫 pages，不能起其它名称。**然后在 pages 下创建对应的组件，比如 index.ts、about.ts、lists.ts、users.ts 等等。我们新增一个文件看效果pages/about.ts

```js
export default function About() { return ( <div> <p>This is the about page</p> </div> ) }
```

在浏览器输入http://localhost:3000/about，就能看到相应页面了。

1.  动态路由

对于动态路由，大家都很熟悉，那就是在 path 后面紧跟 id 或者 pid，比如 [http://localhost:3000/users/1。](https://zhuanlan.zhihu.com/write#) 那么这个 1 就是对应一个 id=1 的形式。我们就要根据用户输入的值来获取这个id 值。这里需要强调两个点：

对于路由组件，我们需要以 \[pid\].js 的这种形式。当然 id 是自定义的，看你需要对路由参数设置什么值而定。

如果想实现 [http://localhost:3000/posts/1](https://link.zhihu.com/?target=http%3A//localhost%3A3000/posts/1) 的这种形式，只需要建个文件夹 posts，把 \[pid\].js 扔到这个文件夹下就行。

**动态路由匹配参数规则如下**：

-   pages/blog/\[slug\].js → /blog/:slug (/blog/hello-world)
-   pages/\[username\]/settings.js → /:username/settings (/foo/settings)
-   pages/post/\[...all\].js → /post/\* (/post/2020/id/title)

1.  页面切换

(1) 通过Link 组件实现页面的跳转

```js
import Link from "next/link"; export function A(){ return ( <Link href="/a/1"> <a>页面跳转到a</a> </Link> ); };
```

(2) 通过Router函数实现跳转

```js
import { useRouter } from "next/router"; export default function ActiveLink({ children, href }) { const router = useRouter(); const handleClick = (e) => { e.preventDefault(); router.push(href); }; return ( <a href={href} onClick={handleClick}> {children} </a> ); }
```

## （四）服务端渲染(SSR)

如果在页面上导出一个**getServerSideProp**函数，那么nextjs将采用服务端渲染模式。该函数返回一个props参数，可以在组件中使用。

**运行时机：**

-   **getServerSideProps只会在服务端执行，永远不会在客户端执行**。
-   无论是直接请求页面，还是刷新页面，getServerSideProps都会在服务端运行，这个页面会和返回的 props 一起预渲染。
-   当在客户端通过next/link或者next/router切换页面（路由）时，服务端也会运行getServerSideProps。

**代码示例：**

```js
//index.js function Home(props){ console.log(props) return ( <div> <Head> <title>index page</title> </Head> <h3>hello world</h3> <img src="/01.jpg"></img> </div> ) } export async function getServerSideProps(context) { const datas = await getDatas(); // 从服务端获取数据 return { props: { data }, // 返回一个props对象，可以在组件内接受这个对象 } } export default Home;
```

**参数说明**

getServerSideProps有一个上下文参数context，包含以下属性：

-   params：如果此页面使用[动态路由](https://link.zhihu.com/?target=https%3A//nextjs.org/docs/routing/dynamic-routes)，params则包含路由参数。如果页面名称是\[id\].js，那么params会像这样{ id: ... }。
-   query：表示查询字符串的对象。
-   req: 请求对象。
-   res: 响应对象。

## （五）静态页面生成(SSG)

静态页面生成（Static Site Generation），简称SSG。**其实就是把组件提前编译成 html 文件，然后把整个 html 文件响应到客户端，从而达到预渲染的目的**。

如果在页面上导出一个**getStaticProps**函数，那么nextjs将采用服务端预渲染模式。**此时页面 HTML 是在构建时生成的，将在每个请求上重复使用，也可以由 CDN 缓存。**

当页面上的数据更新频率不大，并且允许用户缓存的时候，推荐使用**getStaticProps**。

**运行时机：**

-   **getStaticProps只会在服务端执行，永远不会在客户端执行**；
-   在开发环境 ，每次请求都会运行一次 getStaticProps ，这是为了方便我们修改代码重新运行；
-   在生产环境，getStaticProps 只在 build 时运行一次，这样可以提供一份 HTML 给所有的用户访问；

**代码示例：**

```js
//index.js import React from "react" import Head from "next/head" import Axios from "axios"function Home(props){ console.log(props) return ( <div> <Head> <title>index page</title> </Head> <h3 className="h3">hello world</h3> <img src="/01.jpg"></img> <style jsx>{` .h3{ color:skyblue; } `}</style> </div> ) } export async function getStaticProps(context) { console.log("------") return { props: {name:"lisi"}, // will be passed to the page component as props } } export default Home;
```

## （五）动态路由静态化

在动态路由页面中，如果想预先在服务端生成静态页面，则需要使用**getStaticPaths()**这个方法。

**运行时机：**

-   **getStaticPaths只会在服务端执行，永远不会在客户端执行**；
-   getStaticPaths 仅在构建时在服务器端运行；
-   必须配合 getStaticProps({params}) 使用，可以获取这些对应的 params 值。

**代码示例：**

```js
//[pid].tsx import React from "react" import Head from "next/head" function Ha(props){ console.log(props) return ( <div> <h3>hello haha</h3> </div> ) } export async function getStaticPaths() { return { paths: [ {params:{ pid:"1" }},{params:{pid:"2"}} ], fallback: false }; } export async function getStaticProps({params}){ console.log("------",params) console.log("----","hello") return {props:{data:[12,23,34]}} }
```

内部必须返回 {paths:\[{params:{pid:"1"}},{params:{pid:"2"}}\],fallback:false||true} 这种形式，在执行这个函数的时候会根据 paths 生成对应的静态文件 1.html，2.html。

**参数说明**

paths **参数 (必须)**

paths 属性决定了哪些路径将被预渲染。

fallback **参数 (必须)**

如果fallback 是 false，那么在构建时未生成路径都会产生一个**404页面**；如果fallback 是 true，页面将不会一次性构建，而是在首次访问这个路径的时候，生成一个静态页面。

## （六）客户端渲染(CSR)

**useEffect**

useEffec是在客户端执行的，可以使用useEffect在客户端获取数据。

```js
function Profile() { const [data, setData] = useState(null) const [isLoading, setLoading] = useState(false) useEffect(() => { setLoading(true) fetch('/api/profile-data') .then((res) => res.json()) .then((data) => { setData(data) setLoading(false) }) }, []) if (isLoading) return <p>Loading...</p> if (!data) return <p>No profile data</p> return ( <div> <h1>{data.name}</h1> <p>{data.bio}</p> </div> ) }
```

**dom事件**

**服务端没有window和document对象**，dom事件是在客户端执行的。

例如，我们实现一个获取客户端设备类型的需求。

**错误用法：**

```js
export default function AddressPage() { const openDownloadUrl = /(iPhone|iPad|iPod|iOS|Mac)/i.test(window.navigator.userAgent) ? 'https://apps.apple.com/app/nft-track-follow-nft-whale/id1607058815' : 'https://play.google.com/store/apps/details?id=org.bituniverse.nft' return ( <a href={openDownloadUrl} className='btn--large btn--green' target='_blank' rel='noreferrer'> Download </a> ) }
```

**正确用法，采用onClick事件：**

```js
export default function AddressPage() { const openDownloadUrl = () => { window.open( /(iPhone|iPad|iPod|iOS|Mac)/i.test(window.navigator.userAgent) ? 'https://apps.apple.com/app/nft-track-follow-nft-whale/id1607058815' : 'https://play.google.com/store/apps/details?id=org.bituniverse.nft', ) } return ( <a onClick={openDownloadUrl} className='btn--large btn--green' target='_blank' rel='noreferrer'> Download </a> ) }
```

**正确用法，采用useEffect更新：**

```js
export default function AddressPage() { const [openDownloadUrl, setOpenDownloadUrl] = useState('') useEffect(() => { setOpenDownloadUrl( /(iPhone|iPad|iPod|iOS|Mac)/i.test(window.navigator.userAgent) ? 'https://apps.apple.com/app/nft-track-follow-nft-whale/id1607058815' : 'https://play.google.com/store/apps/details?id=org.bituniverse.nft', ) }, []) return ( <a href={openDownloadUrl} className='btn--large btn--green' target='_blank' rel='noreferrer'> Download </a> ) }
```

## （七）集成less

nextjs内置对css、sass和styled-jsx的支持。但是为了尽可能和派网其它项目保持技术栈的统一，我们依然推荐采用less。注意：**nextjs12.0以上一定要安装next-with-less插件，才能正常编译less。**

**安装：**

```text
yarn add less less-loader next-with-less --save
```

**在next.config.js配置支持less**

```js
const withLess = require("next-with-less"); module.exports = withLess({ })
```

## （八）图像优化

用Next.js 中的 Image 组件，替换img标签，具有布局稳定性、跨设备自适应、懒加载和预加载等优点。

**本地图像**

动态await import()或require()不支持。必须是静态的import，因此可以在构建时进行分析。

Next.js 将根据导入的文件自动确定图像的width和height，防止布局变化。

```js
import Image from 'next/image' import profilePic from '../public/me.png' function Home() { return ( <> <h1>My Homepage</h1> <Image src={profilePic} alt='Picture of the author' // width={500} automatically provided // height={500} automatically provided /> <p>Welcome to my homepage!</p> </> ) }
```

**远程图像**

Next.js 在构建过程中无法访问远程文件，**因此需要手动提供width,height**。

```js
import Image from 'next/image' export default function Home() { return ( <> <h1>My Homepage</h1> <Image src='https://www.pionex.com/me.png' alt='Picture of the author' width={500} height={500} /> <p>Welcome to my homepage!</p> </> ) }
```

## （九）组件懒加载

Next.js 默认按照页面路由来分包加载。如果希望对一些特别大的组件做按需加载时，可以使用框架提供的next/dynamic工具函数。

```js
import React, { useState } from 'react' import dynamic from 'next/dynamic' const One = dynamic(import('../components/one')) function Time() { const [nowTime, setTime] = useState(Date.now()) const changeTime = async () => { const moment = await import('moment') setTime(moment.default(Date.now()).format()) } return ( <> <div>显示时间为:{nowTime}</div> <One /> <div> <button onClick={changeTime}>改变时间格式</button> </div> </> ) } export default Time
```

## （十）静态文件服务

Next.js 可以public在根目录中的一个文件夹下提供静态文件，如图像。public然后，您的代码可以从基本 URL ( ) 开始引用其中的文件/。

```js
import React from 'react' import Image from 'next/image' function Avatar() { return <Image src='/me.png' alt='me' width='64' height='64' /> } export default Avatar
```

**更新不频繁的资源，比如网站logo、banner等可以放在public目录下，上传到S3服务缓存起来。**

## （十一）SEO优化

对于 SEO 免不了需要 head 标签，而 next 给我们提供了自定义 head 的功能，我们可以添加 title meta 等。

```js
import Head from "next/head" function Home(props){ return ( <Head> <title>index page</title> <meta charSet="UTF-8"> // 注意这里的charSet大写，不然React jsx语法 会报错 <meta name="viewport" content="width=device-width, initial-scale=1.0"> <meta name="keywords" content="Next.js | React.js"> <meta name="description" content="这是一个跟next.js服务端相关的页面"> </Head> ) }
```

## 五、meta标签和常用社交平台分享

## （一）概述

meta标签主要是用来标注页面的类型和描述页面的内容。

**如果是页面中通过JS获取到数据后，动态修改meta标签内容，在分享时是无效的**；因为facebook、twitter以及搜索引擎在页面刚打开时JS还没有加载时就读取了meta标签。

因此想要实现图文并茂的分享（预览）效果，必须由服务端直出meta标签。

| 标签 | 说明 |
| --- | --- |
| og:url | 页面的标准网址。此标签应该是未加修饰的网址，没有会话变量、用户识别参数或计数器。相应网址的“赞”和“分享”将在此网址中汇总。例如，移动域网址应指向桌面版网址并将其作为标准网址，以汇总不同页面版本的“赞”和“分享”。 |
| og:title | 文章的标题，不包含网站名称等任何品牌信息。 |
| og:description | 内容的简略说明，通常为 2-4 个句子。此标签会显示在 Facebook 帖子的标题下方。 |
| og:image | 用户将内容分享到 Facebook 时所显示图像的网址。请参阅下文了解详情，并查看我们的最佳实践指南，了解如何指定高质量的预览图。 |
| og:type | 内容的媒体类型。此标签会影响您的内容在动态中的显示方式。如果不指定类型，则默认为 website。每个网址都应该是单一对象，因此不可能存在多个 og:type 值。请参阅对象类型参考文档，查看完整的对象类型列表 |
| og:locale | 资源的语言。默认为 en\_US。如果提供其他可用语言的翻译，您还可使用 og:locale:alternate。请阅读本地化文档，了解我们支持的语言。 |

## （二）meta标签汇总

**1、Facebook的meta tags：(og:开头)**

```text
<meta property="og:url" content="https://www.baidu.com"> <meta property="og:type" content="website"> <meta property="og:title" content="百度一下，你就知道"> <meta property="og:description" content="全球领先的中文搜索引擎、致力于让网民更便捷地获取信息，找到所求。百度超过千亿的中文网页数据库，可以瞬间找到相关的搜索结果。"> <meta property="og:image" content="https://psstatic.cdn.bcebos.com/video/wiseindex/aa6eef91f8b5b1a33b454c401_1660835115000.png"> <meta property="og:image:width" content="1200"> <meta property="og:image:height" content="640">
```

**2、Twitter的meta tags:（twitter:开头）**

```text
<meta property="twitter:url" content="https://www.baidu.com"> <meta property="twitter:type" content="website"> <meta property="twitter:card" content="summary_large_image"> <meta property="twitter:title" content="百度一下，你就知道"> <meta property="twitter:description" content="全球领先的中文搜索引擎、致力于让网民更便捷地获取信息，找到所求。百度超过千亿的中文网页数据库，可以瞬间找到相关的搜索结果。"> <meta property="twitter:image" content="https://psstatic.cdn.bcebos.com/video/wiseindex/aa6eef91f8b5b1a33b454c401_1660835115000.png"> <meta name="twitter:image:src" content="https://psstatic.cdn.bcebos.com/video/wiseindex/aa6eef91f8b5b1a33b454c401_1660835115000.png"> //图片要用绝对路径
```

**3、通用的meta tags：**

```text
<meta property="url" content="https://www.baidu.com"> <meta property="type" content="website"> <meta property="title" content="百度一下，你就知道"> <meta property="description" content="全球领先的中文搜索引擎、致力于让网民更便捷地获取信息，找到所求。百度超过千亿的中文网页数据库，可以瞬间找到相关的搜索结果。"> <meta property="image" content="https://psstatic.cdn.bcebos.com/video/wiseindex/aa6eef91f8b5b1a33b454c401_1660835115000.png"> <meta itemprop="image" content="https://psstatic.cdn.bcebos.com/video/wiseindex/aa6eef91f8b5b1a33b454c401_1660835115000.png">
```

**4、坑点**

为什么设置了image标签，在facebook等社交平台分享时图片加载出不来？

可能的原因如下：

（1）所有的img标签都要采用绝对路径，包括image、og:image以及twitter:image；

（2）图片名称后边不要叫版本号或者其它参数；

（3）尝试给设置og:image:width和og:image:height,为图片设置宽高。这里的宽高只是为了确保图片在第一次分享的时候正确加载。不必担心图片的适配问题，在分享到社交平台显示时，它将会按照正确的比例展示。

（4）尝试设置og:image:type标签，它是图像的 MIME 类型。image/jpeg、image/gif 或 image/png 其中之一。

**5、meta调试工具：**

如果开发过程中遇到困难，也可以使用一些社交媒体提供的工具来测试、调试你的标签：

-   [Facebook](https://link.zhihu.com/?target=https%3A//developers.facebook.com/tools/debug/)
-   [Twitter](https://link.zhihu.com/?target=https%3A//cards-dev.twitter.com/validator)
-   [Pinterest](https://link.zhihu.com/?target=https%3A//www.pinterest.com/login/%3Fnext%3Dhttp%253A%252F%252Fdevelopers.pinterest.com%252Ftools%252Furl-debugger%252F)

## （三）常用社交平台分享链接

**1、Facebook：**

[https://www.facebook.com/sharer/sharer.php?u=](https://link.zhihu.com/?target=https%3A//www.facebook.com/sharer/sharer.php%3Fu%3D){链接}

**2、twitter：**  
[https://twitter.com/intent/tweet?text=](https://link.zhihu.com/?target=https%3A//twitter.com/intent/tweet%3Ftext%3D){内容}&url={链接}

**3、Telegram**

[https://t.me/share?url=](https://link.zhihu.com/?target=https%3A//t.me/share%3Furl%3D){链接}&text={内容}

**4、Reddit**

[https://www.reddit.com/submit?url=](https://link.zhihu.com/?target=https%3A//www.reddit.com/submit%3Furl%3D){链接}&title={主题}

**注意以上分享的链接和内容需要用encodeURIComponent加密一下。分享链接必须是公网能访问的链接，测试环境的链接是无效的哦。**
