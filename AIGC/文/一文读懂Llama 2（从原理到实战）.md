---
created: 2024-06-20T10:34:45 (UTC +08:00)
tags: []
source: https://www.zhihu.com/tardis/bd/art/653303123?source_id=1001
author: 
---

# 一文读懂Llama 2（从原理到实战）


在上一篇文章中，我们介绍了 Llama 1 的技术原理。**相比于 Llama 1 ，Llama 2 的训练数据多了 40%，上下文长度也翻倍，并采用了分组查询注意力机制**。具体来说，Llama 2预训练模型是在**2 万亿的 token**上训练的，精调 Chat 模型是在**100 万人类标记数据上训练**的。

本篇文章介绍下LlaMa 2的技术原理以及如何Fine-tuning。

![Alt text](image-12.png)

图1：LLaMa-2

论文：[Llama 2: Open Foundation and Fine-Tuned Chat Models](https://link.zhihu.com/?target=https%3A//scontent-tpe1-1.xx.fbcdn.net/v/t39.2365-6/10000000_662098952474184_2584067087619170692_n.pdf%3F_nc_cat%3D105%26ccb%3D1-7%26_nc_sid%3D3c67a6%26_nc_ohc%3DVldy0tYq-X8AX9WATfk%26_nc_ht%3Dscontent-tpe1-1.xx%26oh%3D00_AfDPv5UzyJGxSQcMYP6xJDkEdmqdiFlUrecaTqWmtt5Siw%26oe%3D64F3CBBF)

github地址：[https://github.com/facebookresearch/llama-recipes](https://link.zhihu.com/?target=https%3A//github.com/facebookresearch/llama-recipes)

HuggingFace地址：[meta-llama (Meta Llama 2)](https://link.zhihu.com/?target=https%3A//huggingface.co/meta-llama)

Llama 2是一系列预训练和微调的大型语言模型（LLMs），参数规模从70亿到700亿不等。Meta的微调LLMs，叫做Llama 2-Chat，是为对话场景而优化的。Llama 2模型在大多数基准上都比开源的对话模型表现得更好，并且根据人类评估的有用性和安全性，可能是闭源模型的合适替代品。Meta提供了他们对Llama 2-Chat进行微调和安全改进的方法的详细描述。

![Alt text](image-13.png)

图2：HuggingFace上开源的Llama 2模型

**Llama 2**

-   训练数据增加40%
-   上下文窗口4k
-   分组查询注意力（ Grouped-query attention）
-   开源7B、13B、70B模型

**Llama 2-chat（经过微调和强化）**

-   开源了7B、13B、70B模型
-   **Llama 2-Chat的训练过程**：这个过程从使用公开可用的在线资源对Llama 2进行预训练开始。接下来，通过应用有监督微调，创建了Llama 2-Chat的初始版本。随后，使用人类反馈强化学习（RLHF）方法，具体是通过拒绝采样和近端策略优化（PPO），对模型进行迭代优化。在RLHF阶段，累积迭代奖励建模数据与模型改进并行进行，这对于确保奖励模型保持在分布内是至关重要的。

![Alt text](image-14.png)

图3：Llama 2训练过程

## 1\. 预训练

为了创建新的Llama 2模型系列，Meta从预训练方法开始，使用一个优化的自回归Transformer，但做了一些改进性能的改变。具体来说，他们进行了更强大的数据清洗，更新了他们的数据混合，训练了40%更多的token，加倍了上下文长度，并使用分组查询注意力（GQA）来提高他们更大模型的推理可扩展性。表1比较了新的Llama 2模型与Llama 1模型的属性。

![Alt text](image-15.png)

表1：Llama 2模型家族。token数仅指预训练数据。所有模型都使用4M token的全局批量大小进行训练。较大的模型——34B和70B——使用分组查询注意力（GQA）来提高推理可扩展性。

### 1.1 预训练数据

Llama 2 的训练语料包括了一个新的公开可用数据的混合，其中不包括来自 Meta 产品或服务的数据。Meta 努力删除了来自某些已知包含大量关于私人个人信息的网站的数据。他们在2万亿 token 的数据上进行训练，因为这提供了一个良好的性能-成本权衡，对最有事实性的来源进行上采样，以增加知识和减少幻觉。 他们进行了各种预训练数据调查，以便用户能够更好地理解他们的模型的潜在能力和局限性。

-   **隐私数据清洗**：根据一些特定站点site，去掉含有大量个人信息的数据。
-   **数据混合**：对于含有事实来源（factual sources）的数据进行上采样（up-sampling），来增强知识，抑制幻觉。

### 1.2 训练细节

Llama 2 采用了 Llama 1 的大部分预训练设置和模型架构。他们使用标准的Transformer架构，应用RMSNorm进行预归一化，使用SwiGLU激活函数和旋转位置编码。与 Llama 1 相比，主要的架构差异包括增加的上下文长度和分组查询注意力（GQA）。

**超参数**。Llama 2 使用 AdamW 优化器进行训练，其中 β1 = 0.9，β2 = 0.95，eps = 10−5 。使用余弦学习率，warm up 为2000，并将最终学习率衰减到峰值学习率的10%。使用0.1的权重衰减和1.0的梯度裁剪。图4显示了使用这些超参数的 Llama 2 的训练损失。

![Alt text](image-16.png)

图4：Llama 2模型的训练损失。在2T token的预训练后，模型仍然没有显示出任何饱和的迹象

**网络结构**

-   标准 Transformer
-   pre-normalization using RMSNorm \[GPT3\]
-   SwiGLU 激活函数\[PaLM\]
-   旋转位置编码\[GPTNeo\]
-   上下文长度到 4k（Llama 1是2k）
-   分组查询注意力 (Grouped-Query Attention, GQA)

**超参数**

-   AdamW 优化器，β1 = 0.9, β2 = 0.95, eps = 10.5
-   cosine 学习率调度，warmup of 2000 steps ，最终学习率衰减到最大值的10%
-   权重衰减（weight decay） 0.1
-   梯度裁剪（gradient clipping） 1.0

**分词器（Tokenizer）**

-   BPE，使用 SentencePiece 实现
-   所有数字 split 成 individual digits
-   未知的 UTF-8 字符用 byte 表示
-   词表大小 32K

### 1.3 Llama 2 预训练效果评估

如表2所示，Llama 2 模型优于 Llama 1 模型。特别是，与 Llama 1 65B 相比，Llama 2 70B 在 MMLU 和 BBH上的结果分别提高了≈5和≈8个点。Llama 2 7B 和 30B 模型在除代码基准外的所有类别上都优于相应大小的 MPT模型。对于 Falcon 模型，Llama 2 7B 和 34B 在所有类别的基准上都优于 Falcon 7B 和 40B 模型。

![Alt text](image-17.png)

表2：与开源基础模型相比

此外，Llama 2 70B 模型优于所有开源模型。 除了开源模型，Meta 还将 Llama 2 70B 的结果与闭源模型进行了比较。如表3所示，Llama 2 70B 在 MMLU 和 GSM8K 上接近 GPT-3.5（OpenAI，2023），但在编码基准上有显著差距。Llama 2 70B 的结果在几乎所有基准上都与 PaLM（540B）相当或更好。但是，Llama 2 70B 与 GPT-4 和 PaLM-2-L 之间仍然存在很大的性能差距。

![Alt text](image-18.png)

表3：与闭源模型在学术基准上的比较

**评测结果**

-   和开源模型相比，在同等模型参数量规模下，Llama 2 所有能力项都胜出（除了 code 能力）
-   和闭源模型相比，Llama 2 比 GPT-4 和 PaLM-2-L 还有差距

### 1.4 细节

**Context length**：4k的上下文，对于chat、summarization、understanding longer documents 等任务有较好效果，在150B tokens上进行2k和4k的对比，发现SQUAD任务性能没降低，SCROLLS上有提升（平均长度3.5k）。

**Grouped-Query Attention** ：对于更大参数量、更大的 context length、更大的 batchsize 来说，原始的MHA（multi-head attention）的内存占用会更高（因为在计算时要缓存pre token的K、V矩阵）。MQA（multi-query attention）让所有的 head 共享 1 个 KV projection 矩阵；GQA（grouped-query attention ）使用 8 个 KV projections（选择8是因为A100 8GPUs） 来减少内存占用。在 30B 模型上训练 150B tokens，发现 GQA 效果和 MHA 差不多，比 MQA 要好；在 1 个node的 8 个 A100 GPUs 上推理速度 GQA 和 MQA差不多，比 MHA 要好（MQA 在推理的时候，要把 KV projections 复制到8张卡上）。

## 2\. Fine-tuning

使用 Llama 2 pretraining 模型，通过 instruction tuning 和 RLHF 技术，结合大量数据标注，得到 Llama 2-Chat 。

### 2.1 Supervised Fine-Tuning (SFT)

**构建指令数据集**

-   **再次重申**：SFT数据集的质量很重要，万级别的高质量效果就很好。没有使用公开的几百万指令数据集，而是找供应商精标了27,540条（人工撰写prompt 和answer，包括 helpfulness 和 safety 两大类 ），发现效果比几百万公开的要好。
-   人写的数据集，质量参差不齐，需要做仔细的质检工作。
-   发现人写的数据和使用SFT模型采样出来的数据质量差不多，因此后续可以把更多精力投入到RLHF的数据标注上。

**超参数**

-   batch size 64
-   cosine 学习率调度 + 初始学习率 2 × 10−5
-   权重衰减（weight decay） of 0.1
-   序列长度（sequence length） 4096

**训练细节**

-   concatenate 所有 prompts 和 answers ，保证 sequence length 是4096
-   在 prompt 和 answer 间加入 special token
-   计算 loss 的时候 mask 掉 user prompt ，只对 answer tokens 进行反向传播
-   fine-tune model 2 epochs

## 3\. 基于人类反馈的强化学习（RLHF)

RLHF 环节的目标是使模型输出对齐 align 人类偏好 (human preferences) 和遵循指令 (instruction following)。

### 3.1 收集人类偏好数据

通过收集人类偏好数据用于奖励建模，从而提高 Llama 2-Chat 的有用性和安全性。Meta 选择了二元比较协议（binary comparison ）标注样本，因为它能让我们最大化收集到的提示的多样性。

标注过程包括以下几个步骤。

首先，要求标注者写一个提示，然后根据提供的标准在两个采样的模型回应之间进行选择。

其次，Meta 还要求标注者标记他们对所选回应相对于另一种回应的偏好程度：要么他们的选择明显更好（significantly better），更好（better），稍微更好（slightly better），或者微不足道地更好/不确定（negligibly better/unsure）。

最后，Meta 根据不同的方面给参与者提供特定的指南。

Meta 关注有用性（helpfulness ）和安全性（safety ）两个方面。有用性指的是 Llama 2-Chat 回应如何满足用户的请求和提供所需的信息；安全性指的是 Llama 2-Chat 的回应是否安全，例如，“给出制作炸弹的详细指示”可以被认为是有用的，但根据 Meta 的安全指南是不安全的。分开两者可以让我们更好地指导标注者。

通过这个过程，Meta 收集了一个大型数据集，包含超过100万个基于人类应用我们指定的指南的二元比较，称之为 Meta 奖励建模数据。随着收集到更多的偏好数据，我们能够训练出逐渐更好的 Llama 2-Chat 版本。

Llama 2-Chat 改进也改变了模型的数据分布。由于如果不接触这种新样本分布，Reward Model 准确度会很快下降，所以在新一轮 Llama 2-Chat 调优之前收集最新 Llama 2-Chat 迭代版本使用的新偏好数据是很重要的。这一步有助于保持 Reward Model 在分布上，并为最新模型维持准确奖励。

**总结：**

-   使用二元比较（binary comparison） 方式标注样本，获得偏好数据

• 标注数据集构建：

◦ prompt 生成方式：人写。先写简单的 prompt，再写复杂的。

◦ 为了保证多样性，使用 2 个 model 生成 response，并使用不同的 temperature。

• 标注lable：4类。significantly better, better, slightly better, negligibly better/unsure

• 标注任务：helpfulness 和 safety ，分开标注。

-   流程：因为使用偏好数据训练的 reward model 训练 Llama-chat 模型后，Llama-chat 的数据分布会变，如果还是采样前一个版本 Llama-chat 生成的样本来训练 reward model，会造成 reward model 的分布和新的 LLama-chat 的分布不一样，因此使用最新的Llama-Chat。

![Alt text](image-19.png)

图5：每次训练reward model之前使用最新llama-chat生成偏好数据

### 3.2 Reward 模型

Reward Model 将模型 response 和 prompt（包括前几轮的上下文）作为输入，输出一个标量分数来表示模型生成的质量（例如，有用性和安全性）。利用这样的回应 score 作为奖励，可以在 RLHF 过程中优化 Llama 2-Chat，以实现更好的人类偏好对齐和提高有用性和安全性。

但是有人发现有用性和安全性有时会相互抵消，这可能使得单个 reward model 难以在两者上都表现良好。为了解决这个问题，Meta 训练了两个单独的 reward model，一个针对有用性（称为有用性 RM），另一个针对安全性（称为安全性 RM）。

Meta 选择从预训练模型 checkpoint 初始化 reward model，因为它确保了两个模型都能从预训练中获得的知识中受益。简而言之，reward model“知道”预训练模型知道的东西。这可以防止出现信息不匹配的情况，例如，两个模型可能会偏爱幻觉。

模型架构和超参数与预训练语言模型相同，除了最后一层\[CLS\]从预测 next token 换成了 regression 来预测一个scalar score 。

**训练目标**。为了训练 reward model，将收集到的成对人类偏好数据转换为二元排序标签格式（即，选择和拒绝）。使用二元排序损失（binary ranking loss）：

![Alt text](image-20.png) 其中， ![Alt text](image-21.png) 是 scalar score。 ![Alt text](image-22.png) 是标注者选择的偏好回应， ![Alt text](image-23.png) 是被拒绝的对应回应，![Alt text](image-24.png) 是 prompt。

在这个二元排序损失的基础上，Meta 进一步分别修改它，以获得更好的有用性和安全性，如下所示。考虑到偏好评级是分为4个（例如，明显更好（significantly better）），利用这些信息来显式地指导 reward model 给那些有更多差异的生成，分配更大的分数差异可能是有用的。为此，Meta在损失中进一步增加了一个边际成分（ ![Alt text](image-25.png) ）：

![Alt text](image-26.png)

其中，边际 ![Alt text](image-27.png) 是偏好评级的一个离散函数。自然地，我们对有明显差异的回应对使用一个大的边际，对有相似回应的对使用一个小的边际。我们发现这个边际成分可以提高有用性 reward model 在两个回应更可分的样本上的准确度。

**训练数据混合配比**

-   使用了开源的 RLHF 数据和 Meta 自己标注的 RLHF 数据
-   做了大量的实验，来确定数据混合比例
-   有用性 reward model 数据配比：Meta Helpfulness：(Meta Safety + open-source) = 1:1
-   安全性 reward model 数据配比：Meta Safety ：(Meta Helpfulness+open-source) = 9:1

**训练细节**

-   one epoch。训练更长时间会导致over-fitting

• 优化器参数和 base model 一致

• 最大学习率：70B：5 × 10−6；其他：1 × 10−5

• cosine 学习率调度 ，最终学习率衰减到最大值的10%

• warmup：3% of the total number of step ，最小5步

• batch size ：512 pairs 或者 1024 rows

**reward model 训练结果**

test set ：1000条，每个batch评估一次效果

结论：reward model 对于不同分级样本的准确率是逐渐下降的，区分性更强的样本 reward model 准确率越高。经过经验分析，对 Llama 2-Chat 模型效果优化最有用的还是区分性更强的样本，只要这部分样本的reward model 准确率足够高就行，所以问题不大。

**规模趋势**

-   在同等训练样本的情况下，reward model 模型越大，效果越好
-   在当前的训练样本量还不够，reward model 的性能还有提升空间，增加更多的样本，会继续提升
-   reward model 的性能越好，Llama 2-Chat 模型的效果越好，所以要努力提升 reward model 的准确率

### 3.3 迭代微调

Meta主要用两种主要算法探索了 RLHF 的微调效果：

-   近端策略优化（PPO）
-   拒绝采样微调

这两种 RL 算法主要有以下不同：

**广度**——在拒绝采样中，模型对给定的提示探索 K 个样本，而 PPO 只进行一次生成。

**深度**——在 PPO 中，在训练的第 t 步，样本是更新后的模型策略的函数，该策略来自前一步的梯度更新后的 t-1。在拒绝采样微调中，在应用类似于SFT的微调之前，根据模型的初始策略采样所有输出以收集新数据集。然而，由于我们应用了迭代模型更新，所以两种 RL 算法之间的基本差异不太明显。

直到 RLHF（V4），Meta 只使用了拒绝采样微调，之后，将两者顺序结合起来，在再次采样之前，在拒绝采样 checkpoint 上应用 PPO。

**PPO**。进一步训练 Llama 2，该方案使用 reward model 作为真实 reward 函数（人类偏好）的估计，使用预训练的语言模型作为要优化的策略。在这个阶段，使用以下优化目标：

![Alt text](image-28.png)

通过从数据集 D 中采样 prompt p 和从策略 π 中采样生成 g，迭代地改进策略，并使用 PPO 算法和损失函数来实现这个目标。 优化过程中使用的最终 reward 函数是：

![Alt text](image-29.png)包含一个偏离原始策略 π0 的惩罚项。与其他工作观察到的一样，我们发现这个约束对于训练稳定性很有用。

Meta 定义了 Rc 为安全性（Rs）和有用性（Rh）reward model 的分段组合，这两个模型分别评估生成的回答是否安全和是否有帮助。

Meta 在数据集中标记了可能引发潜在不安全回答的 prompt，并优先考虑安全性模型的分数。0.15的阈值是用于过滤不安全回答的，对应于在 Meta Safety 测试集上评估的0.89的精确度和0.55的召回率。

Meta 还发现将最终的线性分数进行白化（这里用逆sigmoid函数即logit函数表示）是很重要的，因为这样可以增加稳定性，并与上面的KL惩罚项（β）合理地平衡。

**参数**

-   对于所有的模型，Meta 使用 AdamW 优化器，β1 = 0.9，β2 = 0.95，eps = 10-5。
-   使用0.1的权重衰减，1.0的梯度裁剪，和10-6的恒定学习率。
-   对于每个 PPO 迭代，使用512 batch size，0.2的PPO裁剪阈值，64的micro batch size，并在每个micro batch size 上进行一次梯度步骤。对于 7B 和 13B 的模型，设置 β = 0.01（KL惩罚），对于 34B 和 70B 的模型，设置β = 0.005。
-   所有的模型训练 200 到 400 次迭代，并使用保留的 prompt 进行评估以提前停止。
-   70B 模型上的每次 PPO 迭代平均需要≈ 330秒。为了使用大的 batch size 快速训练，使用了FSDP。

## 4\. 论文总结

**RLHF 机制很重要，可以超越 SFT 的人类监督信号**

RLHF 的成功关键在于 RLHF 训练过程和人工标注的协同。

**SFT 的问题**：即使是熟练的标注人员，每个人的写作也会存在很大 diversity。 在 SFT 数据集上进行微调的模型可以学习这种多样性，但是也会学到一些不好的长尾标注数据。 此外，模型的性能主要受到最熟练标注人员的写作能力的限制。

**RLHF 的优势**：在比较两个 RLHF 的输出哪个更好的时候，任务相对更简单一些。 因此，奖励机制很快学会将低分分配给不好的长尾分布，并与人类的偏好保持一致。 研究表明最差的答案逐渐被删除，使分布向右移动。而且大模型超越人类的能力上限，更是来自于 RLHF 而不是 SFT。

RLHF 学会了根据 prompt 类型动态调整 temperature 的能力：对于开放性的问题，temperature 越大 diversity 越好；对于事实性问题，temperature 越大并不太会影响事实性。

**涌现的能力**

时间感知能力：Llama2-chat 具备了一定的时间概念的泛化能力。比如“奥巴马啥时候当上美国总统？”，模型会识别出来2个时间：1）当前提问时间；2）query 里面的事件发生的时间。

## 5\. HuggingFace 玩转 Llama 2

目前，Llama 2 已经全面集成入 Hugging Face，并全力支持其发布。 Llama 2 的社区许可证相当宽松，且可商用。

通过与 Meta 合作，HuggingFace 已经顺利地完成了对 Llama 2 的集成，你可以在 Hub 上找到 12 个开放模型 (3 个基础模型以及 3 个微调模型，每个模型都有 2 种 checkpoint: 一个是 Meta 的原始 checkpoint，一个是Transformer 格式的 checkpoint)。以下列出了 Hugging Face 支持 Llama 2 的主要工作:

-   <u><a href="https://link.zhihu.com/?target=https%3A//huggingface.co/meta-llama" target="_blank" rel="nofollow noreferrer">Llama 2 已入驻 Hub</a></u>: 包括模型卡及相应的许可证。
-   <u><a href="https://link.zhihu.com/?target=https%3A//github.com/huggingface/transformers/releases/tag/v4.31.0" target="_blank" rel="nofollow noreferrer">支持 Llama 2 的 transformers 库</a></u>
-   使用单 GPU 微调 Llama 2 小模型的示例
-   <u><a href="https://link.zhihu.com/?target=https%3A//github.com/hug%253C/u%253Egingface/text-generation-inference" target="_blank" rel="nofollow noreferrer">Text Generation Inference (TGI) </a>已集成 Llama 2，以实现快速高效的生产化推理</u>
-   推理终端 (Inference Endpoints) 已集成 Llama 2

接下来我们体验下不同版本的Llama 2。

**Llama-2 7B Chat**

**访问地址：**[Llama 2 7B Chat - a Hugging Face Space by huggingface-projects](https://link.zhihu.com/?target=https%3A//huggingface.co/spaces/huggingface-projects/llama-2-7b-chat)

意图理解了，只是没有答对，而且回答中中英混合。

![Alt text](image-30.png)

**Llama2 70B Chatbot**

**访问地址：**[Explore Llamav2 With TGI - a Hugging Face Space by ysharma](https://link.zhihu.com/?target=https%3A//huggingface.co/spaces/ysharma/Explore_llamav2_with_TGI)

70B的也还是没有答对
![Alt text](image-31.png)
太难的不行，换个简单的吧。简单的还是没有问题。
![Alt text](image-32.png)
可以发现目前 Llama 2 chat主要还是英文为主，在要求回答中文时，还是不遵循指令，接下来我们就用中文数据集微调Llama 2，使其能够回答中文。

## 6\. 实战：微调Llama 2

### 6.1 下载训练脚本

首先我们从github上下载Llama 2的微调代码：[GitHub - facebookresearch/llama-recipes: Examples and recipes for Llama 2 model](https://link.zhihu.com/?target=https%3A//github.com/facebookresearch/llama-recipes)

执行命令：

```text
git clone https://github.com/facebookresearch/llama-recipes .
```

下载完成之后，安装对应环境，执行命令：

```text
pip install -r requirements.txt
```

### 6.2 下载模型

接着我们从HuggingFace上下载模型，可以看到目前有多个版本可供选择，这里我们就选择Llama-2-7b-half。

![Alt text](image-33.png)

可以通过手动下载，也可以通过命令下载：

```python3
import huggingface_hub huggingface_hub.snapshot_download( "meta-llama/Llama-2-7b-hf", local_dir="./Llama-2-7b-hf", token="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" )
```

这里的token可以在HuggingFace中获取，如下图所示：

![Alt text](image-34.png)


### 6.3 下载数据

这里选择[GuanacoDataset](https://link.zhihu.com/?target=https%3A//huggingface.co/datasets/JosephusCheung/GuanacoDataset)数据集。数据格式如下：

![Alt text](image-35.png)


可以看到里面包含了各类任务，而且还有其它语言。

### 6.4 微调模型

数据准备好后，接下来就可以微调模型。如果是单卡，可以使用如下脚本：

```text
#if running on multi-gpu machine export CUDA_VISIBLE_DEVICES=0 python llama_finetuning.py --use_peft --peft_method lora --quantization --model_name /patht_of_model_folder/7B --output_dir Path/to/save/PEFT/model
```

如果是多卡，执行以下命令：

```text
torchrun --nnodes 1 --nproc_per_node 4 llama_finetuning.py --enable_fsdp --use_peft --peft_method lora --model_name /patht_of_model_folder/7B --pure_bf16 --output_dir Path/to/save/PEFT/model
```

模型微调完成后，就可以在线推理。

可以使用[alpaca-lora](https://link.zhihu.com/?target=https%3A//github.com/tloen/alpaca-lora)中提供的脚本`generate.py`进行推理，启动命令：

```text
python generate.py --base_model ./Llama-2-7b-hf --lora_weights ./lora
```

接着就可以体验具体效果了。

## 参考

[Llama 2: Open Foundation and Fine-Tuned Chat Models](https://link.zhihu.com/?target=https%3A//scontent-tpe1-1.xx.fbcdn.net/v/t39.2365-6/10000000_662098952474184_2584067087619170692_n.pdf%3F_nc_cat%3D105%26ccb%3D1-7%26_nc_sid%3D3c67a6%26_nc_ohc%3DVldy0tYq-X8AX9WATfk%26_nc_ht%3Dscontent-tpe1-1.xx%26oh%3D00_AfDPv5UzyJGxSQcMYP6xJDkEdmqdiFlUrecaTqWmtt5Siw%26oe%3D64F3CBBF)

[https://github.com/facebookresearch/llama](https://link.zhihu.com/?target=https%3A//github.com/facebookresearch/llama)

[JosephusCheung/GuanacoDataset · Datasets at Hugging Face](https://link.zhihu.com/?target=https%3A//huggingface.co/datasets/JosephusCheung/GuanacoDataset)

[Llama 2 来袭 - 在 Hugging Face 上玩转它](https://link.zhihu.com/?target=https%3A//huggingface.co/blog/zh/llama2)

[meta-llama (Meta Llama 2)](https://link.zhihu.com/?target=https%3A//huggingface.co/meta-llama)

[Explore Llamav2 With TGI - a Hugging Face Space by ysharma](https://link.zhihu.com/?target=https%3A//huggingface.co/spaces/ysharma/Explore_llamav2_with_TGI)

[Llama 2 7B Chat - a Hugging Face Space by huggingface-projects](https://link.zhihu.com/?target=https%3A//huggingface.co/spaces/huggingface-projects/llama-2-7b-chat)

## 书籍推荐
