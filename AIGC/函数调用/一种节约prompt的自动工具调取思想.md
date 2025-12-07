---
created: 2024-08-05T16:58:29 (UTC +08:00)
tags: [智谱, 智谱AI, GLM]
source: https://zhuanlan.zhihu.com/p/679211310
author:
---

# GLM-4 函数调用：一种节约 prompt 的自动工具调取思想

---

一种利用 Python 工具类与 LLM 模型实现自动化任务处理的方法。这种方法可以帮助我们节约 prompt（由于传入 tools 字段同样计算 token 数量，当工具较多时比较浪费），提高工作效率，同时也能够自动化地调取工具，让我们的工作更加便捷。

首先，让我们来看一下这个 Python 工具类的核心代码。这个工具类名为 Tool，它提供了一系列的方法，用于管理工具函数的注册、调用和卸载。通过使用这个工具类，我们可以方便地将各种工具函数集成到我们的应用程序中，同时也可以自动化地调用这些工具函数，从而实现任务处理的自动化。

**Tool 类用于管理所有工具：**

```python
class Tool:
    AVAILABLE_TOOLS = []  # 存储可用工具信息
    ZHIPUAI_TOOLS = []  # 存储工具信息

    @classmethod
    def dispatch(cls, func_name: str, params: Dict[str, Any], raise_error: bool = False) -> Any:
        # 在ZHIPUAI_TOOLS中查找具有给定名称的函数
        for tool in cls.ZHIPUAI_TOOLS:
            if tool['meta']['function']['name'] == func_name:
                # 检查所有必需的参数是否都已提供
                required_params = tool['meta']['function']['parameters']['required']
                for param in required_params:
                    if param not in params:
                        if raise_error:
                            raise ValueError(f"Missing required parameter: {param}")
                        else:
                            return f"Missing required parameter: {param}"

                # 执行找到的函数并返回结果
                try:
                    return tool['func'](**params)
                except Exception as e:
                    if raise_error:
                        raise
                    else:
                        return str(e)

        # 如果没有找到函数，则根据raise_error的值决定是否抛出异常或返回提示
        if raise_error:
            raise ValueError(f"Function '{func_name}' not found in ZHIPUAI_TOOLS")
        else:
            return f"Function '{func_name}' not found in ZHIPUAI_TOOLS"

    @classmethod
    def get_tools(cls) -> List[Dict[str, Any]]:
        return [tool["meta"] for tool in cls.ZHIPUAI_TOOLS]

    @classmethod
    def load_tool(cls, tool_name: str):
        # 检查工具是否已经加载
        for tool in cls.ZHIPUAI_TOOLS:
            if tool['meta']['function']['name'] == tool_name:
                return f"Tool '{tool_name}' is already loaded."
        # 如果工具未加载，则从AVAILABLE_TOOLS中查找并添加到ZHIPUAI_TOOLS
        for tool in cls.AVAILABLE_TOOLS:
            if tool['meta']['function']['name'] == tool_name:
                cls.ZHIPUAI_TOOLS.append(tool)
                return f"Tool '{tool_name}' loaded successfully."
        return f"Tool '{tool_name}' not found in AVAILABLE_TOOLS."

    @classmethod
    def unload_tool(cls, tool_name: str):
        # 在ZHIPUAI_TOOLS中查找名为tool_name的工具并删除
        for tool in cls.ZHIPUAI_TOOLS:
            if tool['meta']['function']['name'] == tool_name:
                cls.ZHIPUAI_TOOLS.remove(tool)
                return f"Tool '{tool_name}' unloaded successfully."
        return f"Tool '{tool_name}' not found in ZHIPUAI_TOOLS."

    @classmethod
    def list_available_tools(cls):
        # 列出所有的AVAILABLE_TOOLS中的函数名称和函数描述。
        return [(tool['meta']['function']['name'], tool['meta']['function']['description']) for tool in cls.AVAILABLE_TOOLS]

    def __init__(self, name=None, description='', params=None, required_params=None):
        self.name = name
        self.description = description
        self.params = params or {}
        self.required_params = required_params or []

    def __call__(self, func):
        # 使用`self`中的参数创建参数的meta信息
        params_meta = {}
        for param_name, param_info in self.params.items():
            param_type = param_info.get('type', 'string')
            param_desc = param_info.get('description', '')
            params_meta[param_name] = {
                "type": param_type,
                "description": param_desc,
            }

        # 创建函数的meta信息
        meta = {
            "type": "function",
            "function": {
              "name": self.name or func.__name__,
              "description": self.description or func.__doc__,
              "parameters": {
                  "type": "object",
                  "properties": params_meta,
                  "required": self.required_params,
              },
            }
        }

        # 将meta信息和函数本身加入到AVAILABLE_TOOLS列表中
        Tool.AVAILABLE_TOOLS.append({"meta": meta, "func": func})

        # 返回原函数
        return func
```

接下来，让我们来看一下这个工具类的具体应用。我们定义了三个基础工具函数：add、multiply 和 print_message，分别用于加法运算、乘法运算和打印消息。这些工具函数都使用了 Tool 类作为装饰器来注册，这样它们就可以被 Tool 类管理了。

```python
@Tool(name='add', description='工具用于加法运算', params={'a': {'type': 'number', 'description': '第一个加数'}, 'b': {'type': 'number', 'description': '第二个加数'}}, required_params=['a', 'b'])
def add(a, b):
    """这是一个加法工具，用于计算两个数的和。"""
    return a + b

@Tool(name='multiply', description='工具用于乘法运算', params={'a': {'type': 'number', 'description': '第一个乘数'}, 'b': {'type': 'number', 'description': '第二个乘数'}}, required_params=['a', 'b'])
def multiply(a, b):
    """这是一个乘法工具，用于计算两个数的乘积。"""
    return a * b

@Tool(name='print_message', description='工具用于打印消息', params={'message': {'type': 'string', 'description': '要打印的消息'}}, required_params=['message'])
def print_message(message):
    """这是一个打印消息的工具，用于在控制台输出消息。"""
    print(message)
    return f"Message printed: {message}"
```

最重要的是：我们还需要三个基础工具，列出所有可用工具、加载工具、卸载工具。

```python
class BaseTool:
    @staticmethod
    @Tool(name='load_tool', description='加载工具', params={'tool_name': {'type': 'string', 'description': '工具名称'}}, required_params=['tool_name'])
    def load_tool(tool_name: str):
        Tool.load_tool(tool_name)
        return f"Tool '{tool_name}' loaded successfully."
    @staticmethod
    @Tool(name='unload_tool', description='卸载工具', params={'tool_name': {'type': 'string', 'description': '工具名称'}}, required_params=['tool_name'])
    def unload_tool(tool_name: str):
        Tool.unload_tool(tool_name)
        return f"Tool '{tool_name}' unloaded successfully."
    @staticmethod
    @Tool(name='list_tools', description='列出所有可用工具', params={}, required_params=[])
    def list_tools():
        return Tool.list_available_tools()

Tool.load_tool('list_tools')
Tool.load_tool('load_tool')
Tool.load_tool('unload_tool')
```

然后，我们使用这个工具类与 GLM-4 模型进行交互，执行一个特定的计算任务。GLM-4 模型扮演了一个能够调用工具的 AI 角色，根据系统的提示，它首先列出了所有可用的工具，然后加载了所需的 multiply 工具，执行了乘法运算，并最后卸载了该工具。下面是操作的代码：

```python
messages = [
    {"role": "system", "content": """你是一个能够调用工具的AI，系统将提供三个基础函数: list_tools, load_tool, unload_tool，首先使用list_tools查看所有可用的工具，如果存在合适的工具，你将使用load_tool函数加载该工具，使用完毕后调用unload_tool释放工具。"""},
    {"role": "user", "content": "我希望你通过工具计算9999999999 * 8888877777"}
    ]
response = client.chat.completions.create(model='glm-4', messages=messages, tools=Tool.get_tools())

while response.choices[0].message.tool_calls:
    messages.append(response.choices[0].message.model_dump())
    tool_call = response.choices[0].message.tool_calls[0]
    args = tool_call.function.arguments


    function_result = Tool.dispatch(tool_call.function.name, json.loads(args))

    print(f"GLM-4调用函数: {tool_call.function.name}，参数: {args}，结果: {function_result}")

    messages.append(
        {
            "role": "tool",
            "content": f"{json.dumps(function_result)}",
            "tool_call_id": tool_call.id,
        }
    )

    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=messages,
        tools=Tool.get_tools(),
    )

print(f"GLM-4响应文本: {response.choices[0].message.content}")
```

这个过程中，GLM-4 模型正确地识别了需要使用的工具，并且通过 Tool 类提供的接口成功地调用了 multiply 函数。这表明我们的工具类设计是合理的，能够支持自动化工具调取，并且能够与语言模型有效配合。

```text
GLM-4调用函数: list_tools，参数: {}，结果: [('load_tool', '加载工具'), ('unload_tool', '卸载工具'), ('list_tools', '列出所有可用工具'), ('add', '工具用于加法运算'), ('multiply', '工具用于乘法运算'), ('print_message', '工具用于打印消息')]
GLM-4调用函数: load_tool，参数: {"tool_name":"multiply"}，结果: Tool 'multiply' loaded successfully.
GLM-4调用函数: multiply，参数: {"a":9999999999,"b":8888877777}，结果: 88888777761111122223
GLM-4调用函数: unload_tool，参数: {"tool_name":"multiply"}，结果: Tool 'multiply' unloaded successfully.
GLM-4响应文本: 9999999999 * 8888877777 = 88888777761111122223
```

通过这个案例，我们可以看到，利用 Python 工具类与 LLM 模型实现自动化任务处理的方法是非常有效的。它可以帮助我们节约 prompt，提高工作效率，同时也能够自动化地调取工具，让我们的工作更加便捷。

最后，我想强调的是，这种方法不仅适用于这个案例，还可以应用于更多的场景。无论是在数据分析、自动化测试还是命令行工具中，我们都可以利用 Python 工具类与 LLM 模型实现自动化任务处理，从而提高工作效率，简化复杂任务的处理。

希望大家能够从这个案例中受到启发，将这种方法应用到自己的工作中，提高工作效率，同时也欢迎大家在评论区分享自己的经验和想法。谢谢大家！

最后给出 Colab 链接：[Colab](https://colab.research.google.com/drive/17ZVTubVyhvfKU0wC4tt2kMkZqp5Ykr05?usp=sharing)

**仍然存在的问题：**

- 需要链式调用函数时，导致 load 和 unload 次数过多
- 有时候并不会那么稳定地同文章所述那样乖乖地调用 list_tools
