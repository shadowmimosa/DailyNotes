---
created: 2024-06-26T11:12:31 (UTC +08:00)
tags: []
source: https://www.cnblogs.com/alphainf/p/17884055.html
author: AlphaInf
---

# 8 卡 3090GPU 云服务器上采用 VLLM 部署中文 llama2-70b 模型及 OpenAI 格式接口

---

根据实际测试，加载模型需要约 129G 显存，最低需要 6 张 3090 显卡（流水线并行）

如果使用 vllm 进行加速推理（张量并行），考虑 8 张 3090 显卡或者 4 张 A100-40G（模型分割要求）

### 模型下载

截至目前，模型数据仅在 huggingface 上保存，在恒源云上的下载方式如下：

开启恒源云代理

```bash
export https_proxy=http://turbo.gpushare.com:30000 http_proxy=http://turbo.gpushare.com:30000
```

访问模型下载地址

在这里建议使用 wget 下载模型文件，优点是能够断点续传，下方是 wget 示例

```bash
wget https://huggingface.co/TigerResearch/tigerbot-70b-chat-v4-4k/resolve/main/pytorch_model-00001-of-00015.bin
```

关闭恒源云代理

```bash
unset http_proxy && unset https_proxy
```

### 依赖安装

克隆官方 github 仓库

```bash
git clone https://github.com/TigerResearch/TigerBot.git && cd Tigerbot
```

安装依赖库

```bash
pip install -r requirements.txt
```

对于普通的多卡推理，示例推理代码如下

```bash
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 python infer.py --model_path /path/to/your/model --max_input_length 1024 --max_generate_length 1024 --streaming True
```

相关参数说明

```bash
--model_path: 模型路径
--model_type=chat: base/chat
--max_input_length=1024: 最大输入长度
--max_generate_length=1024: 最大输出长度
--rope_scaling=None: 长度外推方法(dynamic/yarn supported now)
--rope_factor=8.0: 外推参数
```

安装 vllm

```bash
pip install vllm
```

创建新的推理.py 文件

```python
import torch
from vllm import LLM, SamplingParams

# Set the number of GPUs you want to use
num_gpus = 8 # Change this to the number of GPUs you have

# Define your prompts and sampling parameters
prompts = """
### Instruction:
第一次指令

### Instruction:
第二次指令

### Response:
"""
sampling_params = SamplingParams(temperature=1, top_p=0.9, top_k=50, max_tokens=512, stop="</s>")

# Initialize the VLLM model
llm = LLM(model="/hy-tmp/tigerbot-70b-chat-v4-4k", tensor_parallel_size=8, trust_remote_code=True)

# Move the model to GPUs
llm = torch.nn.DataParallel(llm, device_ids=list(range(num_gpus)))

# Generate outputs
outputs = llm.module.generate(prompts, sampling_params)

# Print the outputs
for output in outputs:
prompt = output.prompt
generated_text = output.outputs[0].text
print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

```

需要注意的是这里的提示词格式与 llama2 不同，tigerbot 的提示词遵循以下格式（注意最上面的两个空换行）

```python


### Instruction:
第一次指令

### Response:
```

### 报错修复指引

安装过程中的报错大多是由于依赖库的版本问题，调整后可以解决。

#### flash-attn 库安装报错

```bash
/home/user/miniconda3/envs/textgen/lib/python3.10/site-packages/flash_attn_2_cuda.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZNK3c106SymIntltEl
```

修复方法：重新构建 flash-attn 库

```bash
pip uninstall flash-attn
FLASH_ATTENTION_FORCE_BUILD=TRUE pip install flash-attn
```

还是在一台 8 卡的 3090 上，我们可以通过一行命令，部署 TigerBot 模型：

```bash
python -m vllm.entrypoints.openai.api_server \
--model="/hy-tmp/tigerbot-70b-chat-v4-4k" \
--tensor-parallel-size 8 \
--served-model-name "tigerbot" \
--chat-template tiger_template.jinja \
--host 0.0.0.0 \
--port 8080

```

这里面的参数意思如下:

- `--model` 模型参数的地址，可以是本地的也可以是云端的，本处为本地加载这个模型
- `tensor-parallel-size` 张量并行的个数，本地有 8 卡，所以设置 8 （注意这个数字必须能够整除 head 的个数）
- `served-model-name` 这里是修改提供服务的模型的名称，默认情况下你的模型名字和 model 一样，你可以用这个进行修改（否则是一个很不美观的路径名，搞不好还要被攻击）
- `host` `port` API 暴露的本地 IP 和接口
- `--chat-template` 这是为了将 OpenAI 的 API 中多轮对话的头，与 TigerBot 的多轮对话格式进行适配而使用的脚本，这里要用 jinja 脚本，我撰写的 jinja 脚本如下:

```jinja2
{{ "" }}
{% for message in messages %}
{% if message['role'] == 'user' %}
{{ "\n### Instruction:" }}
{% else %}
{{ "\n### Response:" }}
{% endif %}
{{ message['content'] }}
{% endfor %}
{{ "\n### Response:\n" }}
```

这里的 chat_template 其实就是 huggingface 中的 chat_template 格式。

注意，这个东西比较新，vllm 0.2.3 开始才支持，如果你发现你报了下面这个错，请你马上升级。

```bash
api_server.py: error: unrecognized arguments: --chat-templat
```

上面的 jinja 脚本，第一行也要保留（制造多一个\\n），不要有缩进（有缩进会有额外的空格混进去）

如果你看到下面的信息出来了，那么就代表你启动成功了

```bash
INFO: Started server process [49087]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

你可以用 curl 命令连接系统，看下有什么模型可用

```bash
curl http://localhost:8080/v1/models
```

如果成功，你会看到下面这样的信息:

```json
{
  "object": "list",
  "data": [
    {
      "id": "tigerbot",
      "object": "model",
      "created": 1701951473,
      "owned_by": "vllm",
      "root": "tigerbot",
      "parent": null,
      "permission": [
        {
          "id": "modelperm-e084351f42514fd88aee16661312eaea",
          "object": "model_permission",
          "created": 1701951473,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": false,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ]
    }
  ]
}
```

我们可以 curl，发送一些信息让模型处理

下面这个是参照 OpenAI 的 completion 撰写的，但是我套上了 TigerBot 的多轮对话

### 补全

```bash
curl http://localhost:8080/v1/completions \
-H "Content-Type: application/json" \
-d '{
"model": "tigerbot",
"prompt": "\n\n### Instruction:\n你是谁？\n\n### Response:\n",
"max_tokens": 1024,
"temperature": 1
}'
```

### 一个标准的单轮对话

```bash
curl http://localhost:8080/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
"model": "tigerbot",
"messages": [
{"role": "user", "content": "3+5=?"}
]
}'
```

返回的信息:

```json
{
  "id": "cmpl-002b8cd331814cb6b8dde2d70340a024",
  "object": "chat.completion",
  "created": 10628423,
  "model": "tigerbot",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": " 3+5=8"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "total_tokens": 16,
    "completion_tokens": 7
  }
}
```

### 下面这个是多轮对话的测试

```json
curl http://localhost:8080/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
"model": "tigerbot",
"messages": [
{"role": "user", "content": "3+5=?"},
{"role": "assistant", "content": "3+5=8"},
{"role": "user", "content": "再加上4"}
]
}'
```

### 外网链接

我在恒源云上进行的测试部署

只要把端口部署在 8080，然后开启恒源云的 API 自定义服务，就会给你一个链接，替换上去就可以了

我当时测试的时候是`http://i-1.gpushare.com:30028/v1/chat/completions`这个连接。

理论上，你还能用各种 frp 转发来实现

### OpenAI 的 Python 代码实现

和正常的代码一样，但需要修改 API_base

注意 api_key，默认是 EMPTY

```python
from openai import OpenAI
# Set OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"

# 这里写内网IP和外网IP取决于你的连接环境
openai_api_base = "http://i-1.gpushare.com:30028/v1"

client = OpenAI(
api_key=openai_api_key,
base_url=openai_api_base,
)

completion = client.chat.completions.create(
model="tigerbot",
messages=[
{"role": "user", "content": "你是谁"},
]
)
print("Chat response:", completion.choices[0].message.content)
```

单线程情况下的输出速度在 23token 每秒

多线程可以达到 320token 每秒
