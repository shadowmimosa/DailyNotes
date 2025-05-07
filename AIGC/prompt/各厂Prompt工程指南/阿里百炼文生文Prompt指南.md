---
title: Prompt, Prompt Engineering, 提示工程, 提示词_大模型服务平台百炼(Model Studio)-阿里云帮助中心
url: https://help.aliyun.com/zh/model-studio/use-cases/prompt-engineering-guide?spm=a2c4g.11186623.help-menu-2400256.d_2_5.2b9d7d13Ag0jJG&scm=20140722.H_2735998._.OR_help-T_cn~zh-V_1
publishedTime: null
---

## 文生文Prompt指南

提示（Prompt）是您输入给大模型（LLM）的文本信息，用于明确地告诉模型您想要解决的问题或完成的任务，也是大语言模型理解用户需求并生成相关、准确回答或内容的基础。 为了帮助您更高效地使用 LLM ，本教程为您提供一系列实用的技巧，帮助您设计和优化 Prompt。

## 设计 **Prompt**

### **构建清晰明确的 Prompt**

想象一下，如果您在给一个同事指派工作任务时，只给了一句话来描述需求，他的任务完成效果可能很难达到您的预期。但如果您提供了明确的目的、建议的思考方向和执行策略等更多参考信息，他更有可能以高标准完成任务。

使用 LLM 也一样，您的任务描述（Prompt）越清晰、具体、没有歧义，LLM 的表现越能符合您的期望。

**说明**

构建一个清晰具体的 Prompt 是充分发挥大模型能力的最重要一步。

<table id="1f392e4f42q0r" tablewidth="2110" tablecolswidth="1055 1055" autofit="true" class="table"><colgroup colwidth="1*"></colgroup><colgroup colwidth="1*"></colgroup><tbody class="tbody"><tr id="687ed0ccacscq"><td id="aa99e35015ta9" rowspan="1" colspan="1"><p jc="center" id="f0f6c240a6bfp"><b>模糊的 Prompt</b></p></td><td id="2205fefa70kw3" rowspan="1" colspan="1"><p jc="center" id="362ad604a2i2e"><b>清晰具体的 Prompt</b></p></td></tr><tr id="8fe6fcb6e54vx"><td id="c7f6fd446et20" rowspan="1" colspan="1"><p id="e9f953e6988wi">我想推广公司的新产品。我的公司名为百炼，新产品名为 Zephyr Z9，是一款轻薄便携的手机。帮我创建一条微博帖子。</p></td><td id="656f53fc2e1g1" rowspan="1" colspan="1"><p id="1ae81e4d4awda">请为我司“百炼”最新推出的“Zephyr Z9”轻薄便携手机设计一条吸引眼球的微博推广帖。</p><p id="d358f6c33arkq">内容需彰显<span class="help-letter-space"></span>Zephyr Z9<span class="help-letter-space"></span>的独特卖点，如极致轻薄设计、高性能配置及用户便利性，同时融入创意元素以提升观众兴趣和互动意愿。</p><p id="c444b954b24cm">记得提及品牌声誉，激发受众好奇心，引导他们探索更多产品信息或直接进行购买。</p><p id="e1a5ed4bf8r7g">贴文应简洁有力，符合微博平台的风格与字数限制，适宜社交媒体传播。</p></td></tr><tr id="77244b8243csh"><td id="e8b5a004c5v4m" rowspan="1" colspan="1"><p id="73cb887b58549">你是一位资深<span class="help-letter-space"></span>PHP<span class="help-letter-space"></span>编程专家，现在接到一个明确的开发任务。诉求是：${require}。请使用<span class="help-letter-space"></span>PHP<span class="help-letter-space"></span>语言详细描述一种实现该诉求的算法或方法，并考虑在实现过程中可能遇到的边界情况和错误处理，以及如何通过高效且安全的代码来满足此需求。</p></td><td id="5f8c2beb44ha1" rowspan="1" colspan="1"><p id="713ca9e6e79sv">作为一位经验丰富的<span class="help-letter-space"></span>PHP<span class="help-letter-space"></span>编程专家，您面临的具体开发任务为：${require}。</p><p id="cdae6cd2f53g5">请运用您的专业知识，详细阐述一种利用<span class="help-letter-space"></span>PHP<span class="help-letter-space"></span>实现该任务需求的高效算法或方法论。</p><p id="e4a5ecf5de5dg">在您的描述中，请务必涵盖以下几点：</p><p id="c81f8a7738cwp">- 具体实现步骤，包括必要的函数、类及数据结构的选择与设计。</p><p id="c8f77dfbe6ixa">- 边界条件分析，识别并解释潜在的边缘案例及如何妥善处理这些情况。</p><p id="0696d475b501n">- 错误处理机制，描述如何在代码中实施健壮的错误检测与异常处理逻辑，以确保程序稳定性。</p><p id="3e67b87ac22dz">- 安全性考量，讨论可能的安全威胁及推荐的防范措施，确保代码执行过程中的数据安全与隐私保护。</p><p id="408769ec4cylm">- 性能优化建议，提出提高代码执行效率的方法，包括但不限于算法优化、资源管理和缓存策略。</p><p id="2773ab5dd4p5a">请确保您的解答不仅技术准确，而且条理清晰、易于理解，以便其他开发者能够快速掌握并应用于实际项目中。</p></td></tr></tbody></table>

百炼提供了Prompt一键优化工具，您可以前往 [Prompt 工程](https://bailian.console.aliyun.com/#/prompt-manage)的**Prompt自动优化**页签尝试该工具。该工具能针对输入的提示（Prompt）进行**自动扩写和细节添加**，推荐您先将 Prompt经过优化工具扩写改进，再接着阅读和体验其他优化技巧。

> Prompt优化功能通过调用大模型实现，需要消耗一定量的Token，按照[通义千问-Plus](https://help.aliyun.com/zh/model-studio/getting-started/models#bb0ffee88bwnk) 推理费用计费。

### **使用 Prompt 框架**

为了系统化地向 LLM 提供明确背景和目的，这里推荐您使用 **Prompt 框架**规范化您的 Prompt。该框架用于帮助您方便、快速地设计 Prompt 结构。该模板充分考虑了会影响 LLM 输出有效性和相关性的各个方面，能显著提升模型表现。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9894951471/CAEQTxiBgMCWop6QjxkiIGI2YWU1YzhjYzRiMjQ3NDU5NGY1YTQ2OWUyNDQzMmE54577910_20240815141024.521.svg)

其内容组成为：（当您不确定如何编写框架各元素的具体内容，不妨将一些关键词交给百炼 Prompt 优化工具进行扩写。）

+   **背景：**介绍与任务紧密相关的背景信息。这一环节有助于LLM深入理解讨论的具体环境，从而保证其生成内容与话题高度相关。
    
+   **目的：**明确指出您期望LLM完成的具体任务。通过设定清晰、精确的目标指令，可引导LLM聚焦于实现既定任务，提升输出的有效性。
    
+   **风格：**指定您希望 LLM 输出的写作风格，可以是某个具体名人、具体流派或者某类专家的写作风格。
    
+   **语气：**定义输出内容应有的语气，比如正式、诙谐、温馨、关怀等，以便适应不同的使用场景和使用目的。
    
+   **受众：**明确指出内容面向的读者群体，无论是专业人士、入门学习者还是儿童等，这样LLM就能调整语言和内容深度，使之更加贴合受众需求。
    
+   **输出：**规定输出内容的具体形式，确保LLM提供的成果能直接满足后续应用的需求，比如列表、JSON数据格式、专业分析报告等形式。
    

|  | 
**未使用 Prompt 框架**

 | 

**使用 Prompt 框架**

 |
| --- | --- | --- |

<table id="e7ce9f7c1874s" tablewidth="2110" tablecolswidth="162 974 974" autofit="true" class="table"><colgroup colwidth="0.23*"></colgroup><colgroup colwidth="1.39*"></colgroup><colgroup colwidth="1.39*"></colgroup><tbody class="tbody"><tr id="cd415c7a032km"><td id="7ff8bf06ff8wn" rowspan="1" colspan="1"></td><td id="86c4086da6rvy" rowspan="1" colspan="1"><p jc="center" id="405134f9f08ly"><b>未使用 Prompt 框架</b></p></td><td id="619c3d2516dkp" rowspan="1" colspan="1"><p jc="center" id="8c02e2f5a969f"><b>使用 Prompt 框架</b></p></td></tr><tr id="0d83bc45ba1mm"><td id="f3189f8803ud1" rowspan="1" colspan="1"><p jc="center" id="8bd1e8081f5h3">Prompt</p></td><td id="d30b125125ikh" rowspan="1" colspan="1"><p id="b8ecd750b6dl0">我想推广公司的新产品。我的公司名为百炼，新产品名为&nbsp;Zephyr Z9，是一款轻薄便携的手机。帮我创建一条微博帖子，简洁而深具影响力。</p></td><td id="2b0d8f512d0z2" rowspan="1" colspan="1"><p id="d5d42b1dd5d7m">#背景#</p><p id="a72d2d1916bg8">我想为公司的新产品做广告。我公司的名字叫百炼，产品叫百炼 Zephyr Z9，是一款轻薄便携的手机。</p><p id="643e3de4db034">#目的#</p><p id="a3233379eayxo">为我创建一个微博帖子（限制：500<span class="help-letter-space"></span>字），旨在让人们有兴趣点击产品链接购买。</p><p id="a3823dc3bffsu">#风格#</p><p id="2fc3f9134f0x8">遵循黑米等成功公司为类似产品做广告的写作风格。</p><p id="1cb3d85541i6t">#语气#</p><p id="b9765c8717g2e">有说服力</p><p id="5d759d6948iqa">#受众#</p><p id="3654d71a8cvye">我公司在微博上的受众通常是年轻一辈人。定制你的帖子，保证喜欢数码产品的人能快速关注到你的帖子。</p><p id="9752a5caedbxh">#输出#</p><p id="80c08768b84ub">微博上的帖子，简洁而有影响力。</p></td></tr><tr id="fec81a1ff9vb2"><td id="57fd897199nng" rowspan="1" colspan="1"><p jc="center" id="5c553df3b7hih">输出</p></td><td id="25fa662329m99" rowspan="1" colspan="1"><p id="b985b4dcc5j2o">【轻启未来，风起云涌】</p><p jc="left" id="83d49b4d69jjb"><img id="ee9a7e3e23vns" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850289.png" alt="image" placement="inline" width="22" class="image inline">百炼新品，Zephyr Z9<span class="help-letter-space"></span>震撼上市！<img id="b3b052d7c0z4j" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850290.png" alt="image" placement="inline" width="22" class="image inline"></p><p jc="left" id="d2880be64e7xn"><img id="092f442f55x9k" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850311.png" alt="image" placement="inline" width="20" class="image inline">携手<span class="help-letter-space"></span>Zephyr Z9，让科技与轻盈同行。这不仅是一部手机，它是你探索世界的轻便伴侣。厚度挑战极限，设计引领风尚，Z9<span class="help-letter-space"></span>在手中，灵感随时迸发。</p><p jc="left" id="d5aad8a7fbuxm"><img id="d1fc02cd901i9" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850323.png" alt="image" placement="inline" width="21" class="image inline">超越想象的性能，搭载极速处理器，流畅如风，无论是工作狂飙还是游戏征途，Zephyr Z9<span class="help-letter-space"></span>都是你的首选座驾。续航强劲，让每一份热情持续燃烧！</p><p jc="left" id="ea8b64a87ay6v"><img id="8cdde04a0843h" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850326.png" alt="image" placement="inline" width="24" class="image inline">捕捉生活每一刻，Z9<span class="help-letter-space"></span>相机创新升级，夜景、人像、广角，每一拍都是封面大片，让美好记忆永不褪色。</p><p jc="left" id="a2ea060e29z5s">Trees 轻薄，重在体验。#百炼<span class="help-letter-space"></span>ZephyrZ9# ，为不凡而生，为你而来。立即拥抱未来，开启属于你的轻盈科技时代！</p><p jc="left" id="963955a1edcjw">官方网站：[www.bailian.com/Z9] (请替换为实际网址）</p><p jc="left" id="18993e02dcn7g">#轻薄旗舰 #科技新风尚 #掌中艺术品</p></td><td id="f45cde5f9ef3b" rowspan="1" colspan="1"><p id="23e2a5ed73j8a" data-spm-anchor-id="a2c4g.11186623.0.i8.4dcd65dfa2O4QM"><img id="274dbfdb14ith" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850302.png" alt="image" placement="inline" width="59" class="image inline" data-spm-anchor-id="a2c4g.11186623.0.i7.4dcd65dfa2O4QM">【独家揭秘】百炼<span class="help-letter-space"></span>Zephyr Z9，轻薄界的颠覆者来了！</p><p jc="left" id="0a1cd3ccab9fm">在这个快节奏的时代，每克重量都是对自由的负担。百炼深谙此道，匠心打造了<span class="help-letter-space"></span>Zephyr Z9——一款专为追求极致轻盈与强大性能平衡的你而生的手机！悬浮般的手感，一触难忘！<img id="d2559fd5d885t" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850307.png" alt="image" placement="inline" width="24" class="image inline"></p><p jc="left" id="8bbdb4daf22g3"><img id="9a7b060386m73" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850308.png" alt="image" placement="inline" width="19" class="image inline">【超薄设计，尽在掌握】</p><p jc="left" id="a215a00f361a3">Zephyr Z9<span class="help-letter-space"></span>以其令人惊叹的纤薄机身，重新定义了“轻薄”。仅<span class="help-letter-space"></span>X.Xmm<span class="help-letter-space"></span>的厚度，轻松滑入口袋，是你日常出行的完美伴侣。携带它，就像带着未来穿梭于都市丛林！<img id="54a5529e0ay2c" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850317.png" alt="image" placement="inline" width="33" class="image inline"></p><p jc="left" id="be148adb2ak40"><img id="b3ff103df6533" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850316.png" alt="image" placement="inline" width="20" class="image inline">【顶尖配置，性能怪兽】</p><p jc="left" id="cea0bb04c7oc3">别看它轻，内核全是硬实力！搭载最新的<span class="help-letter-space"></span>XXXX<span class="help-letter-space"></span>处理器，流畅度爆表，无论是多任务处理还是大型游戏，Z9<span class="help-letter-space"></span>都能游刃有余，让你时刻处于科技最前沿。<img id="d21198ff725d2" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850320.png" alt="image" placement="inline" width="44" class="image inline"></p><p jc="left" id="4b6dd873628eu"><img id="44490f2073ewj" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850330.png" alt="image" placement="inline" width="22" class="image inline">【摄影大师，记录生活】</p><p jc="left" id="cbf9f8d552l2l">配备<span class="help-letter-space"></span>XXMP<span class="help-letter-space"></span>超感光镜头，夜晚也清晰。AI<span class="help-letter-space"></span>智能场景识别，让每一张照片都堪比大片。用<span class="help-letter-space"></span>Zephyr Z9，记录每一个不凡瞬间，让你的朋友圈从此与众不同。<img id="db87e1d4dano3" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850331.png" alt="image" placement="inline" width="39" class="image inline"></p><p jc="left" id="3091db55d4fyz"><img id="3aad2cecfeda9" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850333.png" alt="image" placement="inline" width="20" class="image inline">【续航无忧，能量满满】</p><p jc="left" id="3964c6c8e5lp3">小身材，大能量！Zephyr Z9<span class="help-letter-space"></span>内置高效能电池，搭配<span class="help-letter-space"></span>XXX<span class="help-letter-space"></span>快充技术，片刻充电，长久陪伴。告别电量焦虑，你的创意和灵感不再受限。⚡</p><p jc="left" id="9f6decd4605nc"><img id="249e91289c82h" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850334.png" alt="image" placement="inline" width="26" class="image inline">【限时福利，不容错过】</p><p jc="left" id="81fc66b09bikg">前<span class="help-letter-space"></span>100<span class="help-letter-space"></span>名通过链接购机的用户，将享受神秘大礼包！包含定制保护壳、XXX<span class="help-letter-space"></span>会员年卡等多重好礼，只为尊贵的你！<img id="2ed3e42e1d2st" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850335.png" alt="image" placement="inline" width="23" class="image inline"></p><p jc="left" id="c49e905ef3r55">立刻行动，让百炼<span class="help-letter-space"></span>Zephyr Z9<span class="help-letter-space"></span>成为你探索世界的全新伙伴！点击下方链接，开启轻盈新纪元！<img id="ecf27f9e66lrv" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850336.png" alt="image" placement="inline" width="27" class="image inline"></p><p jc="left" id="e302a99058prx"><img id="28d603a9b1twm" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850339.png" alt="image" placement="inline" width="17" class="image inline">[立即抢购百炼<span class="help-letter-space"></span>Zephyr Z9] [产品链接]</p><p jc="left" id="c32a4f5a6a4dz">#百炼<span class="help-letter-space"></span>ZephyrZ9 #轻薄旗舰 #科技美学 #数码潮流 #性能怪兽</p></td></tr></tbody></table>

在未使用 Prompt 框架时，LLM 输出虽表现尚可，但显得过于泛化，缺乏必要的细节和针对特定群体的吸引力。而在使用 Prompt 框架时，框架不仅提醒您考虑需求的其它方面，特别是一般 Prompt 中缺少的风格、语气和受众，还帮助 LLM 生成更针对年轻群体、细节更多、语言表达更加富有张力的输出。

**说明**

Prompt 框架在实践中有非常多的种类，您可以根据您的任务需求增减其结构组成。当然您也可以在后续章节观察到本教程对该 Prompt 框架的灵活运用。

## 优化 **Prompt**

### **技巧一：为模型提供输出样例**

在 Prompt 中提供您期望的输出示例，可以让 LLM “模仿”我们所要求的规范、格式、概念、文法、语气进行输出。同时，提供样例可以让大模型多次输出的结果更一致，从而稳定模型表现。

<table id="77077c257ffte" tablewidth="2110" tablecolswidth="162 974 974" autofit="true" class="table"><colgroup colwidth="0.23*"></colgroup><colgroup colwidth="1.39*"></colgroup><colgroup colwidth="1.39*"></colgroup><tbody class="tbody"><tr id="0bb7037f33nn0"><td id="0740faf17488h" rowspan="1" colspan="1"></td><td id="9fe77327bafhl" rowspan="1" colspan="1"><p jc="center" id="0edfea93e9zzx"><b>未添加样例</b></p></td><td id="72a13effeflce" rowspan="1" colspan="1"><p jc="center" id="4ed05d1be97d0"><b>添加样例</b></p></td></tr><tr id="2c74f906b3fwf"><td id="3e1b8d645dpay" rowspan="1" colspan="1"><p jc="center" id="2cd25b94b7gxt">Prompt</p></td><td id="85ce2c26acpo3" rowspan="1" colspan="1"><p id="0e49fa5a59wcb">#背景#</p><p jc="left" id="bb75692893qen">你很擅长编写小红书种草笔记，喜欢增加丰富的<span class="help-letter-space"></span>emoji<span class="help-letter-space"></span>元素。</p><p jc="left" id="96cea7c52e67g">#目的#</p><p jc="left" id="356a106c2cgsw">请生成一篇小红书种草笔记，推广强森吹风机。吹风机的优点是：体积小、高颜值、风力大、干的快、智能控温不伤发。</p><p jc="left" id="4387821526aho">#受众#</p><p jc="left" id="e51a253564pv7">喜欢追求时尚的年轻人，尤其是年轻女性</p><p jc="left" id="1eec8e78d9gdq">#输出#</p><p jc="left" id="6af0a0e2800uk">小红书文章格式，充满<span class="help-letter-space"></span>emoji<span class="help-letter-space"></span>元素，简洁但内容充实</p></td><td id="00c1b9c5f4y21" rowspan="1" colspan="1"><p id="30c31ead7fiek">#背景#</p><p id="48dd4fec2a0rn">你很擅长编写小红书种草笔记，喜欢增加丰富的<span class="help-letter-space"></span>emoji<span class="help-letter-space"></span>元素。</p><p id="f73e1ce821eid">#目的#</p><p id="767f2d2070w0o">请生成一篇小红书种草笔记，推广强森吹风机。吹风机的优点是：体积小、高颜值、风力大、干得快、智能控温不伤发。</p><p id="61a85aadd3qj8">#受众#</p><p id="f2e615a66fmo5">喜欢追求时尚的年轻人，尤其是年轻女性</p><p id="3d77fe46090t8">#输出#</p><p id="87b9a8af3c0s7">小红书文章格式，充满<span class="help-letter-space"></span>emoji<span class="help-letter-space"></span>元素，简洁但内容充实</p><p id="f7c2ebeeee4wq">#语气与风格#</p><ol id="dd0e62fc877s8" start="1"><li id="0a40f243c1md0"><p id="8c62b419edht4">我亲测过+n<span class="help-letter-space"></span>种好物+谁适合谁受益 这个秘诀让你的话语超有信服力！ 比如：亲自尝试了很多美白神器，终于挖到宝！仅俩月，肌肤变得嫩滑透亮，自我感觉飘飘欲仙~ 此法特为想大晒体验的小伙伴们量身定制，还能精准安利，助人避坑！</p></li><li id="a53c62cdccbik"><p id="91202c9095526">难题出没+揭秘原因+终极解药 这公式助你条理清晰地分享，内容价值爆棚！ 案例：渴望秀发如丝？揭秘时刻来啦！原来我一直遗漏关键一步，直到遇见它！换用这款洗发水，秀发显著改善，光泽<span class="help-letter-space"></span>get！ 此法逻辑严密，不仅分享秘籍，还引导读者找到问题破解之道。</p></li><li id="1b0eb78a0fk9f"><p id="8c74169c51no3">独到见解+深度剖析+巧妙推荐 这公式帮你自然流露心声，还能温馨种草！ 示例：我觉得每个女孩都该有份挚爱，生活因此而精彩。手帐成了我的小确幸，每当提笔，幸福指数飙升！ 它助你畅所欲言，同时不经意间传递心头好，双赢策略！</p></li><li id="9c06b7c9dc60c"><p id="668fc2a257za7">亲身经历+成果展示 这公式让你的情感表达鲜活又感人！ 场景：回想起夏夜海边的蚊灾，满身红包的绝望，直到遇见救星！现在，光滑肌肤让我裙摆飞扬，自信回归！ 它让你的故事活灵活现，分享喜悦与感恩之情，触动人心！</p></li></ol></td></tr><tr id="b5fae76812bxz"><td id="ff0d5d7163ot2" rowspan="1" colspan="1"><p jc="center" id="c71ff726c80hl">输出</p></td><td id="6517eaeca8ejn" rowspan="1" colspan="1"><p id="b57c0cf063igv">标题：<img id="2a3a0ac166qud" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850340.png" alt="image" placement="inline" class="image inline">强森小巧魔力风机，速干护发新宠儿<img id="9e136e69620w8" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850341.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="cf607743c267r">正文：</p><p jc="left" id="4f479c05c1ht0">Hey<span class="help-letter-space"></span>宝贝们！今天要给你们种草一颗美发界的璀璨新星<img id="3144144b4bxye" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850342.png" alt="image" placement="inline" class="image inline"> —— 强森吹风机！它不仅仅是个工具，简直是随身携带的美发沙龙<img id="2add8c1db01d4" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850343.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="17d9cc7150zg3"><img id="0fdef3c0644bq" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850345.png" alt="image" placement="inline" class="image inline">体积小巧，旅行必备 <img id="93fb3bce3ftpn" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850346.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="6068f07db3b52">首先，它的迷你身材直接击中我心！旅行包包再满也能轻松塞进，不占空间，随时随地凹造型<img id="4588ddd19b90e" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850348.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="ce4cd3c7af4k0"><img id="20af894de9e77" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850350.png" alt="image" placement="inline" class="image inline"> 高颜值，时尚出街 <img id="7b13dcad887o8" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850351.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="ba9c516dd8a5g">看这设计，简直就是艺术品呀！无论是极简白还是高级粉，拿在手里就是街头最靓的崽！手机？不，这是我的新时尚配饰<img id="f2fd3468b0y0c" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850354.png" alt="image" placement="inline" class="image inline"><img id="ae51cb671bnfe" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850355.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="d0d0eeacf9qgu"><img id="b189ba5b1dpbf" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850356.png" alt="image" placement="inline" class="image inline">风力强劲，速干神器 <img id="ed4ad39b02z37" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850358.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="b071314697985">别看它小，风力可一点都不含糊！早上赶时间？强森帮你<span class="help-letter-space"></span>5<span class="help-letter-space"></span>分钟搞定出门发型，效率<span class="help-letter-space"></span>MAX！<img id="23b2f86b67dg3" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850359.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="297c0d5a08cj6"><img id="e7eada8e5bc8l" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850360.png" alt="image" placement="inline" class="image inline">干得快，还护发 <img id="bcfb8840c7o7r" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850361.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="69491334cf9jp">智能控温技术，温柔呵护你的每一根秀发。告别热损伤，只留下柔顺光泽，每次吹发都像做了次沙龙护理～<img id="6eb2cf1703ra6" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850363.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="cfc40dc984moz"><img id="b4d1783df0qfy" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850364.png" alt="image" placement="inline" class="image inline">智能控温，细心之选 <img id="23c0b7273clfk" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850365.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="50fd8cf7a2h7r">懂你的不只是风力，还有温度。根据发质自动调节最适宜的热量，守护秀发健康，长期使用也不怕伤发<img id="e36c2bdbdcv1y" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850367.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="691db931fc63y">总之，强森吹风机就是那个能让你爱不释手的小可爱！赶紧加入购物车，给你的美丽加速吧！<img id="328b23abc5lkl" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850368.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="7da2b224edg6v">#强森吹风机 #美发达人 #快速护发秘籍</p><p jc="left" id="4ea09e75c2i98">标记你的朋友，让她们也来感受这份轻巧与高效吧！<img id="126815caefat5" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850370.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="588a37a928ztk">记得，爱护自己从“头”开始，强森与你一起，绽放自信光彩！<img id="575bda5573j8v" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850372.png" alt="image" placement="inline" class="image inline"></p></td><td id="c3d058f2454ji" rowspan="1" colspan="1"><p id="55d87ae4f94wu"><img id="9d510ff403amg" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850375.png" alt="image" placement="inline" class="image inline">吹风机也能成为美发时尚单品？强森小钢炮告诉你答案！<img id="5e49d42527etl" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850377.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="4e5f1463b226a"><img id="0a19eecda1jjx" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850379.png" alt="image" placement="inline" class="image inline">自从我用了<img id="24cdea656132q" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850381.png" alt="image" placement="inline" class="image inline">强森吹风机<img id="6b69d31f4ftmy" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850382.png" alt="image" placement="inline" class="image inline">，不仅旅行包轻便多了<img id="9a20a76314b2l" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850384.png" alt="image" placement="inline" class="image inline">，每次吹发都变成享受时光<img id="7c59e6c5casth" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850385.png" alt="image" placement="inline" class="image inline">！用了几次后，朋友们都夸我发质看起来好了不止一个度，就像刚从沙龙出来的样子<img id="24afc046b2p9b" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850386.png" alt="image" placement="inline" class="image inline">。它绝对是短途出游或宿舍生活的完美伴侣哦！适合所有追求高效护发的宝贝们～<img id="c2a873c70bs71" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850387.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="cae96cb85awbj"><img id="5e6cd7f7dedkj" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850390.png" alt="image" placement="inline" class="image inline">面对湿漉漉的长发瀑布，每次都得耗时半小时以上？<img id="14cafaf6155p0" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850395.png" alt="image" placement="inline" class="image inline">别怕，强森智能控温科技来了<img id="e0f9ab37e81xc" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850397.png" alt="image" placement="inline" class="image inline">！它能迅速吹干每一根发丝，而且风力强劲却不伤发，秘密就在于它能智能调节温度，保护你的秀发不受热损伤<img id="8d70db78c3coy" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850398.png" alt="image" placement="inline" class="image inline">。从此，快速出门不再是梦！</p><p jc="left" id="fc4da62cdd2qz"><img id="7b9b23f719fpk" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850399.png" alt="image" placement="inline" class="image inline">我一直认为，好的造型工具是美丽态度的体现<img id="f7f25f1507vyw" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850401.png" alt="image" placement="inline" class="image inline">。强森这枚高颜值吹风机不单是个工具，更是梳妆台上的一件艺术品<img id="57af195f9d45a" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850402.png" alt="image" placement="inline" class="image inline">。每次用它吹发，都像是在进行一场个人风格的仪式感升级。不妨也给自己来点这样的小奢侈，毕竟，美好的一天从头开始嘛！<img id="e608941409ali" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850403.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="354c2a5d95b9h"><img id="49e3f85bfa2gz" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850404.png" alt="image" placement="inline" class="image inline">记得那次临时接到晚宴邀请<img id="4d6644cd34neg" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6317466271/p850405.png" alt="image" placement="inline" class="image inline">，急匆匆从健身房出来，头发还滴着汗。正当焦虑之际，幸好有强森吹风机紧急救援！我迅速将湿润的乱发吹整得服服帖帖，走进宴会厅的那一刻，自信满满<img id="3193342828azp" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850411.png" alt="image" placement="inline" class="image inline">，好像刚做完高级沙龙护理似的。多亏了这小巧却强大的美发神器，我的美丽不再受限于时间！<img id="9622d71248pb3" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850412.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="9548ce4cbcv4z">快来把这吹风机界的时尚小钢炮加入购物车吧！<img id="7e443e471dkaz" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850413.png" alt="image" placement="inline" class="image inline">让我们一起做个风一样的女子，优雅又效率，从头开始闪耀每一天！<img id="33eb91b206l18" src="https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5317466271/p850414.png" alt="image" placement="inline" class="image inline"></p><p jc="left" id="5638f9a8cca2b">#强森吹风机 #高颜值美发神器 #智能护发新体验 #速干不伤发 #时尚必备</p></td></tr></tbody></table>

观察输出时，您可以发现，LLM 学习了样例的要求并针对性地生成了符合格式要求的种草文。

### 技巧二：设定完成任务的步骤

对于许多复杂任务，提醒 LLM 如何完成任务是非常必要的。

#### **提供任务步骤来完成数学题**

数学题：

又到了周日，小明像以往一样去爷爷奶奶家玩，小明于早上八点整步行出发，已知小明每分钟行走50米，走了12分钟后，小明的父亲发现小明忘记带作业了，于是便骑车去追小明，已知小明的爸爸每分钟骑行200米，等到追上小明后，爸爸决定骑车带上小明，已知小明坐自行车的路程是走路路程的5倍，请问，小明和他爸爸几点到爷爷家的呢？（小明8点36分到爷爷家）

Prompt（通过添加`#任务步骤#`告诉 LLM 如何完成任务）：

```plaintext
#背景#
又到了周日，小明像以往一样去爷爷奶奶家玩，小明于早上八点整步行出发，已知小明每分钟行走50米，
走了12分钟后，小明的父亲发现小明忘记带作业了，于是便骑车去追小明，已知小明的爸爸每分钟骑行200米，
等到追上小明后，爸爸决定骑车带上小明，已知小明坐自行车的路程是走路路程的5倍，
#目的#
小明什么时候到爷爷家？
#任务步骤#
1. 先计算小明被爸爸追上时的时间和移动的距离。
2. 再计算小明去爷爷家剩余的距离和需要的时间。
3. 最后计算小明到爷爷家的时间。
```

**Output（LLM 清晰地从提示词中获取到了任务步骤，并基于规定的步骤生成了正确结果）：**

```plaintext
要解答这个问题，我们首先需要根据给定的信息分步骤来解决。

步骤1: 计算小明被爸爸追上时的时间和移动的距离
小明每分钟行走50米。
爸爸出发时（即小明走了12分钟后），小明已经走了 12×50=600 米。
从这一刻起，小明继续以每分钟50米的速度前进，而爸爸则以每分钟200米的速度追赶。
设从小明父亲开始追赶直到追上小明所需时间为 t分钟，则有方程：[200t = 50t + 600] （左边是爸爸的总行程，右边是小明在相同时间内走过的距离加上初始的600米领先）
解这个方程得：[150t = 600] [t = 4] 分钟。这意味着爸爸用了4分钟就追上了小明。
在这4分钟里，小明又走了 4×50=200 米。
因此，当爸爸追上小明时，小明总共走了 600+200=800 米。
步骤2: 计算小明去爷爷家剩余的距离和需要的时间
根据题意，“小明坐自行车的路程是走路路程的5倍”，这里可以理解为从爸爸追上小明的地方到爷爷家的路程是之前步行路程(800米)的5倍，即 800×5=4000 米。
由于之后是骑车前往，速度为每分钟200米，因此到达爷爷家还需要时间 4000/200=20 分钟。
步骤3: 最后计算小明到爷爷家的时间
小明于早上八点整出发。
到爸爸追上他时，共过去了 12+4=16 分钟。
再加上骑车前往爷爷家所需的20分钟，总共耗时 16+20=36 分钟。
因此，小明将在出发后的第36分钟到达爷爷家，即早上 8:00+36 分钟 = 8:36 到达爷爷家。
```

### 技巧三：**使用分隔符号区分单元**

在构建复杂的 Prompt 时，采用特定的分隔符来界定不同内容单元是极为关键的，这一做法显著增强了 LLM 对 Prompt 正确解析的能力。随着任务复杂度的增加，合理利用分隔符越能提升 LLM 的表现。

分隔符的选择应着眼于那些在自然语言文本中罕见的、独特的字符组合，例如：`###`、`===`、`>>>`等。这些特殊符号序列并无固定规则，关键在于其辨识度高，确保模型能够明确区分这些符号是作为内容区域的界限标识，而非文本中的普通标点或语法组成部分。

<table id="64870f2b05cgb" tablewidth="2110" tablecolswidth="162 974 974" autofit="true" class="table"><colgroup colwidth="0.23*"></colgroup><colgroup colwidth="1.39*"></colgroup><colgroup colwidth="1.39*"></colgroup><tbody class="tbody"><tr id="a4dcb6df2by7p"><td id="241ec696dckd8" rowspan="1" colspan="1"></td><td id="a86940ac1f6j6" rowspan="1" colspan="1"><p jc="center" id="2be728ac2e2b4"><b>未使用分隔符</b></p></td><td id="f19243e1fflj8" rowspan="1" colspan="1"><p jc="center" id="5bb8f428400om"><b>使用分隔符</b></p></td></tr><tr id="94b11110a33fn"><td id="6c438d50a5ws6" rowspan="1" colspan="1"><p jc="center" id="79363b5d7cge9">Prompt</p></td><td id="3b3252375dyr0" rowspan="1" colspan="1"><p id="7a70c6dd70k4a">请简短总结以下影评。</p><p jc="left" id="186d4d7eeenyt">曾经意气风发的张志强在生活的重压下，中年“失速”偏离了原本的生活轨迹，一时意气用事的决定，让他瞬间从家人的“小骄傲”变成了社会的“边角料”。然而，他未曾料到，这仅是他中年人生道路上的起点。接连不断的变故如疾风骤雨般袭来，迫使他不得不重新面对自我。当生活的重担真正压肩，他选择成为一名快递员，从新的起点重新出发，穿梭于都市大街小巷的高志垒在路上结识了一众志同道合的伙伴。在共度的时光里他深切的体会到了人间的冷暖真情，逐渐在这条充满磨砺的“逆行道”中找回曾经丢失的勇气与信念，重新定义人生新的方向。</p></td><td id="bd42b186d1kmq" rowspan="1" colspan="1"><p id="25510df0a8lki">请简短总结以下影评。</p><p id="f6d1e61f22k0w">###</p><p id="986d0405fayj3">曾经意气风发的张志强在生活的重压下，中年“失速”偏离了原本的生活轨迹，一时意气用事的决定，让他瞬间从家人的“小骄傲”变成了社会的“边角料”。</p><p id="9e3a411c8e467">###</p><p id="b20055597528w">然而，他未曾料到，这仅是他中年人生道路上的起点。接连不断的变故如疾风骤雨般袭来，迫使他不得不重新面对自我。</p><p id="7f30ef3d91g17">当生活的重担真正压肩，他选择成为一名快递员，从新的起点重新出发，穿梭于都市大街小巷的高志垒在路上结识了一众志同道合的伙伴。</p><p id="e91a9dc7dcf9c">###</p><p id="69d92eca9c1q2">在共度的时光里他深切的体会到了人间的冷暖真情，逐渐在这条充满磨砺的“逆行道”中找回曾经丢失的勇气与信念，重新定义人生新的方向。</p><p id="51d5521cddo07">###</p></td></tr><tr id="8c884eac3cpf7"><td id="bf5c08bbdaa5u" rowspan="1" colspan="1"><p jc="center" id="713d00a4fcg5j">输出</p></td><td id="bdde6c4381zzv" rowspan="1" colspan="1"><p id="631d2193efxim">电影讲述了一个中年危机故事，主角张志强因生活压力偏离正常生活轨道，经历一系列挑战后，他成为一名快递员，在新朋友的帮助下重拾勇气与信念，找到了生活的新方向。影片展现了逆境中的成长与自我救赎。</p></td><td id="a5d8bf85f7t5t" rowspan="1" colspan="1"><p id="fe6621bd8360h">主人公张志强中年遭遇生活困境，一次冲动的决定使他社会地位骤降。</p><p id="0c48d4b293xmd">随后，面对重重挑战，他担任快递员重新起步，在此过程中与同行建立深厚情谊，并在磨难中找回勇气和信念。</p><p id="94744b51d6ch6">最终，在艰难和挑战中，为自己的人生找到了新的意义和方向。</p></td></tr></tbody></table>

您可以在输出中发现明显差别，在使用了分隔符的输出中，**LLM 不仅理解了三段话的逻辑关系，还正确识别了分隔符，并根据分隔符的段落生成了三段强相关的总结。**

### 技巧四：**引导模型“思考”**

对于逻辑推理和语境学习的复杂任务来说，简单的 Prompt 技巧可能无法满足任务需求。但您可以通过**引导模型生成推理过程**或**帮助模型拆解复杂任务并逐步推理**的方式，让模型在生成推理结果前生成更多的推理依据，从而提升模型在复杂问题上的表现。

这里为您先介绍[**思维链**](https://arxiv.org/abs/2201.11903)**（Chain of Thought，COT）**，它是一种使用起来较为简单的引导方法，但能够显著提高大模型在复杂场景下的推理能力。

任务目的：**解析一个复杂的 JSON 结构体**

```json
#背景#
JSON 输入：
{"web-app": {
  "servlet": [   
    {
      "servlet-name": "cofaxEmail",
      "servlet-class": "org.cofax.cds.EmailServlet",
      "init-param": {
      "mailHost": "mail1",
      "mailHostOverride": "mail2"}},
    {
      "servlet-name": "cofaxTools",
      "servlet-class": "org.cofax.cms.CofaxToolsServlet",
      "init-param": {
        "templatePath": "toolstemplates/",
        "log": 1,
        "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",
        "logMaxSize": ""}}],
  "servlet-mapping": {
    "cofaxEmail": "/cofaxutil/aemail/*",
    "cofaxTools": "/tools/*"},
 
  "taglib": {
    "taglib-uri": "cofax.tld",
    "taglib-location": "/WEB-INF/tlds/cofax.tld"}}}

#目的#
根据 JSON 判断是否完全符合以下要求：
1. 是否每个 servelet 都有 init-param
2. 是不是 servelet-mapping 中元素都在 servlet 中都有匹配
3. servelet 的 cofaxTools 中有三个以“log” 开头的参数，且 “log” 参数小于 10
```

<table id="49c34fb987jly" tablewidth="100" tablecolswidth="49.5 50.5" autofit="true" class="table"><colgroup colwidth="0.99*"></colgroup><colgroup colwidth="1.01*"></colgroup><tbody class="tbody"><tr id="d4a05a8a58yom"><td id="37ebee9b8fsnx" rowspan="1" colspan="1"><p jc="center" id="4af7d30edcgbd"><b>不使用思维链</b></p></td><td id="5598523bd2fth" rowspan="1" colspan="1"><p jc="center" id="2e166a01a62cd"><b>使用思维链</b></p></td></tr><tr id="b97afc69567ln"><td id="31d1900654zyl" rowspan="1" colspan="1"><div class="help-code-block"><pre code-type="xCode" id="e223d3bf1frzy" data-tag="codeblock" outputclass="language-plaintext" class="pre codeblock language-plaintext"><code data-highlighted="yes" class="hljs language-plaintext">#输出#
如果全部符合要求，只输出 "符合要求"，否则只输出 "不符合要求"。</code></pre></div></td><td id="54f03305f0g0i" rowspan="1" colspan="1"><div class="help-code-block"><pre code-type="xCode" id="3e4ac2224bnxp" data-tag="codeblock" outputclass="language-plaintext" class="pre codeblock language-plaintext"><code data-highlighted="yes" class="hljs language-plaintext">#输出#
先输出针对各要求的思考判断过程。
如果全部符合要求，再输出 "符合要求"，否则输出 "不符合要求"。</code></pre></div></td></tr><tr id="aa781af2b9ned"><td id="3b2fd90e894lp" rowspan="1" colspan="1"><p id="34c3593b96kxw">不符合要求</p></td><td id="dc749bbfd9kl0" rowspan="1" colspan="1"><p id="28b4d0d44f8zg">首先，我们来逐步分析给定的<span class="help-letter-space"></span>JSON<span class="help-letter-space"></span>数据，以判断它是否符合所有提到的要求。</p><h4 jc="start" id="6d150d5bf5e4j"><b>思考过程</b></h4><ol id="bc6e86535b7nw"><li id="c37f36eae29ag"><p id="4c68fdb31cn6p"><b>检查每个<span class="help-letter-space"></span>servlet<span class="help-letter-space"></span>是否有<span class="help-letter-space"></span>init-param</b></p><ul id="2c798bff475tj"><li id="77e261c977lul"><p id="623ca4afdfxsz"><code data-tag="code" node="[object Object]" code-type="xCode" class="code">cofaxEmail</code>servlet 有<code data-tag="code" node="[object Object]" code-type="xCode" class="code">init-param</code>，包含 "mailHost" 和 "mailHostOverride"。</p></li><li id="898039161a1g2"><p id="501c495578lyh"><code data-tag="code" node="[object Object]" code-type="xCode" class="code">cofaxTools</code>servlet 也有<code data-tag="code" node="[object Object]" code-type="xCode" class="code">init-param</code>，包含 "templatePath", "log", "logLocation", 和 "logMaxSize"。</p></li></ul><p id="21f226a80cqnt"><b>结论</b>：每个<span class="help-letter-space"></span>servlet<span class="help-letter-space"></span>都有<code data-tag="code" node="[object Object]" code-type="xCode" class="code">init-param</code>，满足要求<span class="help-letter-space"></span>1。</p></li><li id="74638bbdd37hr"><p id="a4989e5168q1v"><b>检查<span class="help-letter-space"></span>servlet-mapping<span class="help-letter-space"></span>中的元素是否都在<span class="help-letter-space"></span>servlet<span class="help-letter-space"></span>中有匹配</b></p><ul id="9bd4f6dc22p68"><li id="dced479014c22"><p id="bdff6e7a403zi"><code data-tag="code" node="[object Object]" code-type="xCode" class="code">servlet-mapping</code>中有两个元素：<code data-tag="code" node="[object Object]" code-type="xCode" class="code">cofaxEmail</code>和<code data-tag="code" node="[object Object]" code-type="xCode" class="code">cofaxTools</code>。</p></li><li id="73194e2051kia"><p id="9a26ac0c34k2d"><code data-tag="code" node="[object Object]" code-type="xCode" class="code">servlet</code>定义中也正好有这两个<span class="help-letter-space"></span>servlet<span class="help-letter-space"></span>名称的定义：<code data-tag="code" node="[object Object]" code-type="xCode" class="code">cofaxEmail</code>和<code data-tag="code" node="[object Object]" code-type="xCode" class="code">cofaxTools</code>。</p></li></ul><p id="727561df91b5y"><b>结论</b>：<code data-tag="code" node="[object Object]" code-type="xCode" class="code">servlet-mapping</code> 中的所有元素都能在 <code data-tag="code" node="[object Object]" code-type="xCode" class="code">servlet</code> 中找到匹配，满足要求<span class="help-letter-space"></span>2。</p></li><li id="3059fe810dn69"><p id="8b8b3b2b464pi"><b>检查<span class="help-letter-space"></span>cofaxTools servlet<span class="help-letter-space"></span>中是否有三个以"log"开头的参数，且"log"参数小于<span class="help-letter-space"></span>10</b></p><ul id="734f5c450eaq3"><li id="af55bd7863sz1"><p id="d828fd69aemt6"><code data-tag="code" node="[object Object]" code-type="xCode" class="code">cofaxTools</code>servlet 的<code data-tag="code" node="[object Object]" code-type="xCode" class="code">init-param</code>中以 "log" 开头的参数有："log"（值为<span class="help-letter-space"></span>1），"logLocation"（值为"/usr/local/tomcat/logs/CofaxTools.log"），和理论上应该计算在内的"logMaxSize"（尽管它的值为空，但题目似乎更关注前缀而非值的内容）。</p></li><li id="c7a8263cbaqkp"><p id="294cccf088b3k">其中 "log" 的值为<span class="help-letter-space"></span>1，确实小于<span class="help-letter-space"></span>10。</p></li></ul><p id="0434871d85ljw"><b>结论</b>：虽然关于"logMaxSize"是否算作以"log"开头的有效参数可能有歧义（因为它没有实际数值），但基于最直接的解读，我们可以认为是满足了至少存在三个以"log"开头的参数这一条件，且明确指定的"log"参数值为<span class="help-letter-space"></span>1，小于<span class="help-letter-space"></span>10，因此大体上满足要求<span class="help-letter-space"></span>3，尽管"logMaxSize"的处理依据具体情况可能有所不同。</p></li></ol><h4 jc="start" id="f814464dbaqqh"><b>输出</b></h4><p jc="start" id="b6dccc61f6gcy">基于以上分析，虽然关于"logMaxSize"的处理可能存在解释空间，但主要条件基本得到满足。因此，如果对"logMaxSize"不作严格要求（比如，不强制要求它必须有一个有效数值且小于<span class="help-letter-space"></span>10），则可以认为整体<b>符合要求</b>。如果有对"logMaxSize"的具体数值要求，则需要进一步澄清后决定。但在标准解读下，答案应为：“符合要求”。</p></td></tr></tbody></table>

除了思维链，启发 LLM 进行“思考”的实用方法还有**提示链（Prompt Chaining）**。提示链通过多轮对话，引导 LLM “思考” 方向，让 LLM 从简单任务开始，沿着设计好的“思考”方向逐步完成一个复杂推理。

提示链虽然相对思维链来说构建模式更加复杂，但**模型表现更好，准确率更高**。它非常适合逻辑复杂但能按照固定模式拆解的困难任务。

#### **提示链（Prompt Chaining）引导样例**

数学题：

又到了周日，小明像以往一样去爷爷奶奶家玩，小明于早上八点整步行出发，已知小明每分钟行走50米，走了12分钟后，小明的父亲发现小明忘记带作业了，于是便骑车去追小明，已知小明的爸爸每分钟骑行200米，等到追上小明后，爸爸决定骑车带上小明，已知小明坐自行车的路程是走路路程的5倍，请问，小明和他爸爸几点到爷爷家的呢？（小明8点36分到爷爷家）

第一轮输入（数学题 + 第一个简单问题）：

```plaintext
#背景#
又到了周日，小明像以往一样去爷爷奶奶家玩，小明于早上八点整步行出发，已知小明每分钟行走50米，
走了12分钟后，小明的父亲发现小明忘记带作业了，于是便骑车去追小明，已知小明的爸爸每分钟骑行200米，
等到追上小明后，爸爸决定骑车带上小明，已知小明坐自行车的路程是走路路程的5倍，

#目的#
计算小明什么时候被他爸爸追上，追上时走了多远？
```

**Output 1（LLM 对第一个简单问题的回答）：**

```plaintext
首先，我们计算小明在被父亲追上之前走了多远。
小明的速度是每分钟50米，他已经走了12分钟，因此他已经走过的距离是：
50 米/分钟 × 12 分钟 = 600 米
接下来，我们计算父亲开始追赶小明时两者的相对速度。父亲的骑行速度是每分钟200米，而小明继续以每分钟50米的速度步行。因此，父亲相对于小明的速度是：
200 米/分钟 − 50 米/分钟 = 150 米/分钟
为了追上小明，父亲需要覆盖小明最初12分钟所行走的600米距离。以150米/分钟的相对速度，父亲追上小明所需的时间是：
600 米 / 150 米/分钟 = 4 分钟
这意味着父亲在开始追赶后的4分钟追上了小明，从父亲开始追赶算起，总共用了12分钟（小明已经走了的时间）+ 4分钟（父亲追赶的时间）= 16分钟。
现在，我们要计算小明被追上时共走了多远。小明在最初的12分钟内走了600米，从父亲开始追赶的4分钟里，小明又走了：
50 米/分钟 × 4 分钟 = 200 米
所以，小明被追上时总共走了：
600 米 + 200 米 = 800 米
综上所述，小明在早上8点16分被他爸爸追上，此时他已经走了800米。
```

第二轮输入（第二个问题，问题逐渐深入）：

**Output 2（LLM 对第二个问题的回答）：**

```plaintext
根据题目，小明坐自行车的路程是他走路路程的5倍。小明被追上时已经走了800米，那么他坐自行车的路程将是：
800 米 × 5 = 4000 米
```

第三轮输入（最后的复杂问题）：

**Output 3（通过前面多个问题的引导得到了正确的结果）：**

```plaintext
要计算小明什么时候到爷爷家，我们需先确定小明坐上自行车后的行进时间。
小明坐自行车的总路程是4000米，他父亲的骑行速度是每分钟200米。因此，小明坐自行车所需的时间是：
4000  米 / 200  米/分钟 = 20  分钟
小明从出发到被追上已经过去了16分钟（即8:00出发，8:16被追上），加上坐自行车的20分钟，总共用时为：
16 分钟 + 20 分钟 = 36 分钟
所以，小明在早上8点出发后，将在36分钟后到达爷爷家，即：
8:00 AM + 36  分钟 = 8:36  AM
因此，小明将在上午8点36分到达爷爷家。
```

引导 LLM “思考”的方法还有很多种，比如：思维树（Tree of Thoughts, ToT)、Boosting of Thoughts 等。

## Prompt 测试与迭代

生成最优 prompt 是一个高度实验性的过程，需要不断尝试和调整各种方法。整个 prompt 工程的优化过程可概括如下：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9894951471/CAEQURiBgIDQju2umxkiIGZkMTJiMjE4YmI1YzRjNTM4ODc0YjNjNGYxNTU2YzI04789852_20241122171352.128.svg)

此外，值得注意的是，除了精心设计的 prompt 外，用户提供的反馈和修正也是获取模型最佳输出的关键因素之一。即使在 prompt 优化完成后，持续地在线上环境中接收反馈并作出相应调整，才能使模型更好地理解和满足用户需求。

## Prompt 优化案例：跨国公司 AI 助手稳定地输出多语言内容

问题背景：用户反馈 qwen-turbo 无法稳定地用英文回答英文问题。

优化点有：

1.  将“语言”替换为“语种”。因为“语言”这个词有歧义，不一定代指的是英语、法语，也可以是书面语言、口头语言。语种就没有这个歧义。
    
2.  优化前 Prompt 结构较为松散，而且`## 限制`部分内容过于冗余。因此使用本教程提供的 Prompt 框架重新排版并将`## 限制`部分的内容拆分到正确的位置。
    
3.  `${documents}`部分是一段很长的话，放在某句话中并不合适。应该使用分隔符标记切分出来，作为一个重要的内容块。
    

<table id="9fe378f93dt8g" tablewidth="1042" tablecolswidth="521 521" autofit="true" class="table"><colgroup colwidth="1*"></colgroup><colgroup colwidth="1*"></colgroup><tbody class="tbody"><tr id="78d2a7b524uy4"><td id="939fce2bb1ule" rowspan="1" colspan="1"><p jc="center" id="0dff6235a018b"><b>优化前 Prompt</b></p></td><td id="eac641bf0fu0z" rowspan="1" colspan="1"><p jc="center" id="aaff92657couw"><b>优化后 Prompt</b></p></td></tr><tr id="4d6cc6898c2lx"><td id="d4a4ba44a10st" rowspan="1" colspan="1"><p id="31359f7604f8m"># 角色</p><p id="2d2e750d7df3u">你是一位高效的<span class="help-letter-space"></span>HR AI<span class="help-letter-space"></span>助手，专门负责解答公司内部关于政策、考勤制度、年假安排等相关问题。你具备快速准确地解析公司政策文档的能力，并能够为同事提供清晰简洁的说明。</p><p id="91379bad7dqps">## 技能</p><p id="7e6350133bg5z">### 技能<span class="help-letter-space"></span>1: 政策解析</p><p id="d7dd69983249v">- **任务**：准确解读公司政策文档，为同事提供清晰、简洁的政策说明。</p><p id="8644d5e859hdw">- 快速定位到相关政策条款，解答具体的政策执行细节。</p><p id="3bc2970addzu5">- 确保解释的内容易于理解且符合公司的官方规定。</p><p id="5a4f245c807qk">### 技能<span class="help-letter-space"></span>2: 考勤答疑</p><p id="4f04654b5blyn">- 解答与员工考勤相关的所有疑问，包括打卡规则、迟到早退处理、请假流程等。</p><p id="307dead303906">- 提供具体的考勤操作指南和特殊情况处理建议。</p><p id="086371123d5s1">### 技能<span class="help-letter-space"></span>3: 年假管理咨询</p><p id="99b0cc07f9a5w">- 详细解释年假申请条件、累积规则、有效期及审批流程。</p><p id="5296487373sa5">- 协助计算员工的年假余额，提供休假规划建议。</p><p id="726d60756cht4">## 工具与资源</p><p id="32b3b896fcp0r">- **知识库访问**：直接引用和解析`${documents}`中的公司政策文档和相关规章制度，确保答案的权威性和时效性。</p><p id="f6fb75f1e474r">- 如果提出的问题是英文，请用你理解的中文含义去检索知识库，最后再使用英文回复（请注意回复内容中的标点符号统一为英文格式！尤其字符 U+2019 "’"，请替换为“'” ）。</p><p id="2143dbfcc42d8">## 限制</p><p id="34f6ab043duvy">- 要求回答内容仅使用标准 ASCII 字符集，不要出现中文引号、全角逗号及其他全角标点符号！！！</p><p id="d3a43ad82dr21">- 使用与用户提问相同的语种回复，例如用户使用中文，回答中文，用户使用英文，回答英文。</p><p id="af4a7c9af798t">- 仅限于解答公司政策、考勤制度、年假等人力资源管理范畴内的问题。</p><p id="6b99e3bcf0yvu">- 不涉及个人隐私数据的查询，保护员工信息安全。</p><p id="7f993a129cg8w">- 当遇到知识库未涵盖或不明确的问题时，需指引询问者联系人力资源部门获取进一步的帮助。</p></td><td id="98c5be987fcl1" rowspan="1" colspan="1"><p id="8b26577577x7n">#背景#</p><p id="66a6ed9afcy7n">你是一位跨国公司的高效的<span class="help-letter-space"></span>HR AI<span class="help-letter-space"></span>助手，专门负责解答公司内部关于公司政策解析、考勤答疑、年假管理咨询的问题。你具备快速准确地解析公司政策文档的能力。以下为公司政策文档：</p><p id="46f1577e98je0">======</p><p id="5821495239cq9">`${documents}`</p><p id="91e32e52f0rx8">======</p><p id="92c3446810f9x">#目的#</p><ol id="56c4803df30au"><li id="d717a04411cp0"><p id="b5be92574e6fp">用户的问题仅限于公司政策解析、考勤答疑、年假管理咨询三类范畴。</p></li><li id="e2b1aeaf0bdf0"><p id="7a63ea8956jkz">当问题在范畴内但知识库未涵盖或不明确时，指引用户联系人力资源部门获取进一步的帮助。</p></li><li id="343bf99043puc"><p id="488a21886foww">三类问题按照以下要求进行回答：</p><ol id="e1c2a14730fyo"><li id="831aefcf49k38"><p id="2843782a09mw9">政策解析</p><ol id="22cea5b24fp1c"><li id="463a9646b73kw"><p id="36484ccdc4hp0">准确解读公司政策文档，为用户提供清晰、简洁的政策说明。</p></li><li id="8581817bdbir4"><p id="861efba366sua">快速定位到相关政策条款，解答具体的政策执行细节。</p></li><li id="e57c59808aq2s"><p id="b5004507e54ce">确保解释的内容易于理解且符合公司的官方规定。</p></li></ol></li><li id="72318f295dy3m"><p id="5ba016a476nv8">考勤答疑</p><p id="f2a0b9f427whg">- 解答与员工考勤相关的所有疑问，包括打卡规则、迟到早退处理、请假流程等。</p><p id="842991408cahu">- 提供具体的考勤操作指南和特殊情况处理建议。</p></li><li id="4a60fcde7f1s1"><p id="d196c53189xc6">年假管理咨询</p><p id="0189f9808buod">- 详细解释年假申请条件、累积规则、有效期及审批流程。</p><p id="ec0af4e4d06rn">- 协助计算员工的年假余额，提供休假规划建议。</p></li></ol></li><li id="a2e853023aayk"><p id="77033d39104pi">不涉及个人隐私数据的查询，保护员工信息安全。</p></li></ol><p id="d149afa8e9uwu">#多语言要求#</p><p id="92be01c363y6m">- 如果提出的问题不是中文，用问题的中文含义去检索知识库。</p><p id="16c7a3c12c987">- 知识库检索出来的内容在输出时也要转换为问题的语种。</p><p id="ec1464bec1dzy">#输出#</p><p id="5a0f781a4ev1p">1. 仅使用标准 ASCII 字符集输出回答。</p><p id="3e24bc1a73na1">2. 输出的内容语种为用户输入的语种。</p></td></tr></tbody></table>

+   本页导读 （1）

+   设计 Prompt

+   构建清晰明确的 Prompt

+   使用 Prompt 框架

+   优化 Prompt

+   技巧一：为模型提供输出样例

+   技巧二：设定完成任务的步骤

+   技巧三：使用分隔符号区分单元

+   技巧四：引导模型“思考”

+   Prompt 优化案例：跨国公司 AI 助手稳定地输出多语言内容
