# python-docx: paragraph.text 缺失文本问题

## 问题概述
- **来源**: https://github.com/python-openxml/python-docx/issues/1123
- **发布时间**: 2022-07-29

## 问题描述

在某些类型的注释中（注意：这不是存储在comments.xml中的注释），存在**删除旧文本并插入新文本**的情况。这类注释在Word文档中会显示为追踪更改（Track Changes）。

![问题截图](https://user-images.githubusercontent.com/65615554/181587625-85f32ed3-6295-4bc0-935c-3d933015a6f0.png)

## 问题现象

### 代码
```python
file = docx.Document(filepath)
print(file.paragraphs[0].text)
```

### 实际输出（错误）
```
The civil war literature has substantial gaps. wo primary theoriescivil wars occur when citizens 1) become sufficiently motivated and 2) have the opportunity to rebel.  explain
```

### 预期输出（正确）
```
The civil war literature has substantial gaps. Two primary theories argue civil wars occur when citizens 1) become sufficiently motivated to commit violence and 2) have the opportunity to rebel. Neither theory explains
```

## 问题分析

- 缺失的文本部分：
  - "Two" 变成了 "wo"
  - "argue" 完全缺失
  - "to commit violence" 缺失
  - "Neither" 变成了空白

- 可能原因：python-docx 在处理Word文档中的追踪更改（Track Changes）或修订标记时，没有正确合并已删除和已插入的文本。

## 相关知识点

- **Word追踪更改**: 文档中被修改的部分会被标记为删除和插入
- **python-docx**: 用于读写Microsoft Word文档的Python库
- **XML结构**: Word文档本质上是XML格式，追踪更改信息存储在特定的XML标签中

## 解决方向

1. 检查python-docx是否有处理追踪更改的相关功能
2. 可能需要手动处理Word XML中的修订标记
3. 考虑在提取文本前接受所有修订更改

## 标签
`#bug` `#python-docx` `#文本提取` `#追踪更改`
