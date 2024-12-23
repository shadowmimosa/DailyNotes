---
created: 2024-08-05T17:07:01 (UTC +08:00)
tags: [LLM,大语言模型[话题]]
source: https://zhuanlan.zhihu.com/p/685355104
author: 
---

# 浅聊大模型（LLM）的工具调用（Function Call）

---

> **1\. 大模型在基于 funciton call 调用工具时并不是真的学习到了工具的描述，很可能是通过检测到一种特殊的标识符进行工具调用  
> 2\. 虽然大模型支持一次请求连续调用多个子函数，但并不建议**

## 接口说明

> Openai 对于 function call 示例 [Function calling and other API updates](https://openai.com/blog/function-calling-and-other-api-updates)

大模型可以处理大部分的问题（预训练时已经喂了足够多的训练数据），但是有两个致命缺陷：1.对于时间的处理；2.幻觉问题：对于一些比较专业的知识（在训练数据中未提及），大模型有很大的概率胡言乱语。

为了解决这两类问题，最直观的方法就是引入工具插件。但是 LLM 在返回时存在不确定性，无法很好地保证工具被正常调用。Function Call 可以更加明确地让大模型去选择工具。类似的 2023 大会上提到的 seed 功能或者 json-format 返回，也都是类似的功能。

下面展示了官网的一个[示例](https://openai.com/index/function-calling-and-other-api-updates/)

```bash
curl https://api.openai.com/v1/chat/completions -u :$OPENAI_API_KEY -H 'Content-Type: application/json' -d '{
  "model": "gpt-3.5-turbo-0613",
  "messages": [
    {"role": "user", "content": "What is the weather like in Boston?"}
  ],
  "functions": [
    {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"]
          }
        },
        "required": ["location"]
      }
    }
  ]
}'
```

可以看到在请求 body 多了 functions 字段对于 `天气` 工具进行了详细的介绍。通过这种方式请求 GPT 可以更好地调用工具。

## 原理说明（猜想

> 大模型是如何实现对自定义工具的调用的呢？

通过上面的 Function call 调用示例，我们直观的感觉是“大模型好像可以真可以理解我们自定义的工具，并且成功调用”。但事实真的是这样子吗？

OpenAi 并没有开源他们的训练 GPT 的数据构造方式，但有一篇 Toolken[论文](https://arxiv.org/abs/2305.11554)比较好地解释“大模型如何实现对工具调用”。让我采样 GPT 在训练时也是基于这种类似的方式实现的工具调用。

论文提到在 fine-tune 阶段，训练数据中引入一种特殊的工具标识符，称为 toolken。下图展示了部分的训练数据构成。“怎么训练就怎么推理”。当模型在推理时，toolken 会像一般的 token 一样被推理产生。一旦产生了 toolken，就会发生工具调用。

论文对比了 toolken 的效果和相比于在 ICL 中添加工具说明的效果：在 icl 中对工具进行说明的方法存在以下缺点：  
1\. 一旦工具多了，上下文变长，模型非常容易出现遗忘  
2.对于自定义的工具，如果在预训练时未曾出现过，有很大的概率无法触发工具调用。

![ToolkenGPT prompt for ReAct](image.png)

## 应用思考

> "能否通过 function call 连续调用多个工具呢"

通过 function-call 一次调用多个子函数是可行的（连续调用多个）。

为什么呢？依然还是从 next token_predict 的角度去看。既然工具调用只是预测下一次 token 是一个特殊标记的工具类 token 就会触发工具调用，那么只要在预测的过程中出现了特殊字符就是等待函数调用。

但是这种方法是否建议呢？其实并不是很建议。大模型在上下文过长的情况下很容易丢失记忆，也容易产生幻觉。虽然有这方面的能力，但是风险较高，在实际落地的时候，明确的逻辑还是建议通过代码实现

可以看一些 multi-agent 的框架，内部通常是是调用一次 llm 接口，调一次 function call。这样做的一个好处在对于过程的处理更加细致。比如 func1 的结果在传给 func2 时需要进行修改等情况。如果整个流程都交给大模型，结果的可控制性会下降。

不过往长远看，将所有的流程（流程制定，所有的工具调用）一股脑全交给大模型实现，无疑是一种更泛化的实现。现在这种方案存在一定风险知识因为模型能力还不够强。
