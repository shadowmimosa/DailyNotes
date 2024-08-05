---
created: 2024-08-05T18:01:36 (UTC +08:00)
tags: [GitHub, 搜索引擎, LLM]
source: https://juejin.cn/post/7363545737873768487?utm_source=gold_browser_extension
author: IT咖啡馆
---

# 想了解 AI 搜索实现，可以看看这个开源项目

---

如何利用 AI 的能力来强化搜索一直是业内的关注方向，大家都希望可以给用户带来更好的体验。

今天我们分享一个开源项目，它也同样受 Perplexity 启发，利用 AI 的能力来提升搜索体验，它就是：llm-answer-engine

## llm-answer-engine 是什么

llm-answer-engine 是一个开源的 AI 增强搜索引擎，它包含构建复杂答案引擎所需的代码和指令，该引擎利用 Groq、Mistral AI 的 Mixtral、Langchain.JS、Brave Search、Serper API 和 OpenAI 的功能。

该项目旨在根据用户查询高效地返回源、答案、图像、视频和后续问题，是对自然语言处理和搜索技术感兴趣的开发人员的理想起点。

项目使用的技术栈：

- **Next.js**：用于构建服务器端渲染和静态 Web 应用程序的 React 框架。
- **Tailwind CSS**：实用程序优先的 CSS 框架，用于快速构建自定义用户界面。
- **Vercel AI SDK**：Vercel AI SDK 是一个用于构建人工智能驱动的流文本和聊天 UI 的库。
- **Groq & Mixtral**：处理和理解用户查询的技术。
- **Langchain.JS**：一个专注于文本操作的 JavaScript 库，例如文本分割和嵌入。
- **Brave Search**：一个注重隐私的搜索引擎，用于采购相关内容和图像。
- **Serper API**：用于根据用户的查询获取相关的视频和图像结果。
- **OpenAI Embeddings**：用于创建文本块的矢量表示。
- **Cheerio**：用于 HTML 解析，允许从网页中提取内容。
- **Ollama（可选）** ：用于流式推理和嵌入。
- **Upstash Redis 速率限制（可选）** ：用于为应用程序设置速率限制。

项目的作者在网上发布了很详细的项目介绍，里面详细的说明的项目的基本结构和实现的思路等，有条件的话，非常值得去看一下，这样还可以省下阅读代码的时间，效率更高。可以看下下图，里面就有了大致的一个思路和步骤，其实看起来不难，但是落地就不容易。

## 安装使用 llm-answer-engine

**安装前准备：**

```markdown
1. 需要确保你的环境中已经安装好 Nodejs 和 NPM
2. 项目会使用到 4 种 API key：
   OpenAI
   Groq
   Brave Search
   Serper
   密钥的获取方式可以从对应的网站查看。
```

**安装部署**

接下来我们可以开始从源码安装，可以通过以下步骤：

```bash
#获取代码
git clone <https://github.com/developersdigest/llm-answer-engine.git>
#安装依赖
npm install
#配置env，在根目录下新建.env,添加提前准备好的API key
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
BRAVE_SEARCH_API_KEY=your_brave_search_api_key
SERPER_API=your_serper_api_key
```

安装完成后就可以起动服务了。

```bash
npm run dev
```

完成安装后我们可以体验 llm-answer-engine ，它总体上可以帮我们：

- 快速建立问答系统：通过集成不同 AI 模型，快速搭建一个能够处理多种类型问题的智能问答平台。
- 高效答案检索：利用 Groq 的向量数据库能力，对大规模知识库进行高效的近似最邻近搜索，确保问题得到精准匹配的答案。
- 模块化开发：借助 Mixtral 和 Langchain，开发者可以便捷地添加、移除或替换不同模块，以适应不同场景需求。

**编辑配置**

配置文件位于该 app/config.tsx 文件中。您可以修改以下值

```diff
- useOllamaInference: false,
- useOllamaEmbeddings：假，
- 推理模型：'mixtral-8x7b-32768'，
- inferenceAPIKey：process.env.GROQ_API_KEY，
- embeddingsModel: 'text-embedding-3-small',
- 文本块大小：800，
- 文本块重叠：200，
- numberOfSimilarity结果：2，
- 扫描页数：10，
- nonOllamaBaseURL: ' <https://api.groq.com/openai/v1>'
- useFunctionCalling: true
- useRateLimiting: false
```

## 总结

llm-answer-engine 构建了一个比较完整的 AI 增强搜索，覆盖到了目前主流的技术实现，所以如果对这个方向有关注，那么可以参考和学习一下其内在的实现逻辑。从整体上也可以总结一下它具备的特点：

1.  多模型融合：项目支持集成多种 AI 服务商的大型语言模型，如 OpenAI GPT 系列，为用户提供丰富且准确的答案来源。
2.  高性能架构：运用 Groq 作为底层向量数据库，确保了在大规模数据环境下快速有效地检索和生成答案。
3.  灵活性与扩展性：通过 Mixtral 和 Langchain 组件，项目具备极强的模块化和可扩展能力，方便开发者根据不同需求定制和增强问答引擎。
4.  前端优化：依托 Next.js 框架，构建出响应式、高性能的用户界面，实现无缝的交互体验。
5.  隐私与安全性：与 Brave 浏览器技术相结合，强化了用户数据保护和隐私安全措施。

目前国内在这个方向上也有很多的企业在发力，比如 Kimi 和秘塔搜索等，所以了解现有的一些实现方式，思考如何进一步创新非常重要。

## 项目信息

- 项目名称： llm-answer-engine
- GitHub 链接：[github.com/developersd…](https://github.com%2Fdevelopersdigest%2Fllm-answer-engine)
- Star 数：3K
