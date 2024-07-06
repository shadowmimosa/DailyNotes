---
created: 2024-06-25T10:55:58 (UTC +08:00)
tags: []
source: https://www.53ai.com/news/hangyeyingyong/2024052952318.html
author: 广州网站建设-优网科技 www.uweb.net.cn
---

# Dataherald 核心 Text-to-SQL 引擎全面开源

---

Dataherald 公司近日将其核心产品——自然语言到 SQL 引擎——开源，引发业界关注。这一举动为开发者和企业提供了构建、集成和扩展 Text-to-SQL 应用的全新机会。

### **Dataherald：应对现实世界数据分析挑战**

Dataherald 的开源引擎旨在解决现实世界数据分析中，使用大型语言模型（LLM）将自然语言转换为 SQL 时面临的挑战。虽然 LLM 在生成语法正确的 SQL 查询方面表现出色，但在处理复杂的现实数据和模式时却常常力不从心。这是因为：

- **现实世界的数据和模式往往复杂混乱**，而 LLM 的训练数据大多来自结构化的公开数据集，难以应对实际应用中的多样性挑战。
- **自然语言本身存在歧义性**，同样的问题在不同语境下可能对应不同的 SQL 查询逻辑，而 LLM 难以准确捕捉这些细微差别。
- **LLM 缺乏对特定数据集的深入理解**，无法针对特定业务场景进行精准的 SQL 查询生成。

为了解决这些难题，Dataherald 打造了一套强大的 NL-to-SQL 引擎，其核心是一个基于 LLM 的智能代理，它利用思维链（CoT）推理和多种工具，从用户提问中生成高精度的 SQL 查询。

### **Dataherald 核心引擎：四大关键技术**

Dataherald 的 NL-to-SQL 引擎之所以能够在复杂场景下表现出色，主要得益于以下四大关键技术：

2.  **上下文收集与注入:** 引擎在配置阶段从数据库、数据字典和非结构化文档等来源收集上下文信息，并将这些信息存储在数据存储或向量数据库中。在生成 SQL 查询时，引擎会根据用户提问的相关性，动态地将上下文信息注入到 LLM 中，帮助其更好地理解问题语义。
3.  **样本学习与微调:** Dataherald 允许用户上传样本 NL-SQL 对（golden SQL），这些样本可以用于少样本提示学习或微调 NL-to-SQL LLM 模型，使其更适应特定数据集和业务场景。
4.  **SQL 执行与错误恢复:** 引擎会将生成的 SQL 查询在数据库中执行，并获取少量样本数据，以便评估查询结果的正确性。如果查询执行过程中出现错误，引擎会尝试自动修复错误并重新执行。
5.  **置信度评估与排序:** 引擎使用评估器为生成的 SQL 查询分配置信度得分，并根据得分对多个候选查询进行排序，最终返回置信度最高的查询结果给用户。

### **Dataherald 开源代码解析：核心模块深度解读**

Dataherald 开源代码库包含四大服务模块：引擎、管理控制台、企业后端和 Slackbot。其中，核心引擎模块包含了 LLM 代理、向量存储和数据库连接器等关键组件。 Dataherald 代码的亮点之一是模块化设计，将不同的功能模块封装成独立的类和方法，便于代码维护和扩展，也使得 Dataherald 可以轻松地集成新的工具和功能。

#### **核心代码分析：dataherald_sqlagent.py**

dataherald_sqlagent.py 文件定义了 Dataherald SQL 代理的核心逻辑，展示了如何利用 Langchain 框架构建智能代理，以及如何与数据库交互、执行 SQL 查询等。 Dataherald 代码充分利用了 Langchain 框架的优势，简化了智能代理的构建过程，并受益于 Langchain 提供的模块化设计和丰富的功能组件。

- **SQLDatabaseToolkit:**   该类定义了与 SQL 数据库和上下文信息交互的工具集。 这些工具帮助代理理解用户问题并与数据库交互。每个工具都有特定的用途，并被设计用于处理与数据库相关的不同任务。

- **SystemTime:** 获取当前日期和时间。 在处理包含时间或日期信息的用户问题时，此工具非常重要。
- **QuerySQLDataBaseTool:**   执行 SQL 查询并将结果返回给代理。 它是代理与数据库交互的主要方式。
- **GetUserInstructions:** 获取用户在 Dataherald 平台上设置的数据库管理员指令，用于约束 SQL 查询的生成过程，确保生成的查询符合管理员定义的规范和安全策略。
- **TablesSQLDatabaseTool:** 分析用户问题并识别与问题相关的数据库表，并计算每个表与问题的相关性得分，帮助代理选择最相关的表用于 SQL 查询生成。
- **ColumnEntityChecker:**   检查数据库列中是否存在与用户问题中提到的实体相似的值。 例如，如果用户询问"哪个城市的人口最多"，该工具会尝试在数据库中找到包含城市名称的列，并识别"人口"相关的关键词。
- **SchemaSQLDatabaseTool:** 获取数据库中表的 schema 信息，包括表名、列名、数据类型、主键、外键等。代理利用 schema 信息理解数据库的结构，并生成符合 schema 规范的 SQL 查询语句。
- **InfoRelevantColumns:**   提供有关数据库列的更多信息，例如列的数据分布、唯一值的数量等。 代理可以利用这些信息优化 SQL 查询或进行更深入的数据分析。
- **GetFewShotExamples:** 从样本库中检索与当前用户问题语义相似的历史问题及对应的 SQL 查询语句。 代理可以利用这些样本进行少样本学习，从而更好地理解用户意图并生成更准确的 SQL 查询。

- **DataheraldSQLAgent:**   该类定义了 Dataherald SQL 代理的主要功能，负责协调不同的工具和流程，最终生成 SQL 查询并返回结果。

- **create_sql_agent:**   根据指定的 LLM 模型、工具集和其他参数，创建 SQL 代理。**值得注意的是，Dataherald 使用 Langchain 的 ZeroShotAgent 来构建代理，这意味着它默认情况下不使用 CoT 推理。**
- **generate_response:**   根据用户提问，生成 SQL 查询并返回结果。 它首先使用 SQLDatabaseToolkit 中的工具收集必要的信息，然后使用 LLM 模型生成 SQL 查询，最后执行查询并将结果返回给用户。 Dataherald 在这一过程中展现了其上下文感知能力，能够收集和利用上下文信息，提高 SQL 查询的准确性。
- **stream_response:** 以流式方式生成 SQL 查询，并将中间步骤发送到队列中。 这种方式允许 Dataherald 平台向用户实时展示 SQL 查询的生成过程，提高用户体验。

Dataherald 在 SQL 查询执行过程中能够捕获和处理异常，提高系统的鲁棒性，例如，如果代理生成的 SQL 查询包含语法错误，Dataherald 会尝试识别错误并进行修复，以避免查询失败。

### **Dataherald 开源， Text-to-SQL 技术发展新机遇**

Dataherald 开源其核心引擎，为 Text-to-SQL 技术的发展带来了新的机遇。开发者和企业现在可以利用 Dataherald 的开源代码构建更强大、更易用的 Text-to-SQL 应用。

**相关链接：**

- Dataherald 官网：https://www.dataherald.com
- Dataherald GitHub 代码库：https://github.com/Dataherald/dataherald
