<font size=4 face='楷体'>

## 遍历 docx

### 分别遍历文字、图片与表格

docx 库会将文字、图片与表格分别存成一个对象，可以遍历这三个对象实现全文的遍历
**但是无法保证文字、图片与表格之间的顺序**

以遍历如下图的 word 文件作为例子
![image](https://img2022.cnblogs.com/blog/2913315/202207/2913315-20220717181301473-1502532712.png)

- 导入所需要的库

```py
import docx
from docx.document import Document
from docx.table import _Cell, Table
from docx.oxml.text.paragraph import CT_P
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
import pandas as pd
```

该部分主要使用了`docx`库和`pandas`库

```py
doc = docx.Document('test.docx')
```

- 编写能依次遍历文档内容的函数

```py
'''依次遍历文档内容的函数'''
def iter_block_items(parent):
    # 判断传入的是否为word文档对象，是则获取文档内容的全部子对象
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    # 判断传入的是否为单元格，是则获取单元格内全部子对象
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    # 遍历全部子对象
    for child in parent_elm.iterchildren():
        # 判断是否为段落，是则返回段落对象
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        # 判断是否为表格，是则返回表格对象
        if isinstance(child, CT_Tbl):
            yield Table(child, parent)
```

`yield`与`return`用法相似，`yield`在返回结果后，第二次调用该函数的时候将会是接着`yield`之后开始进行执行
所以第二次之后执行该函数是都在 for 循环里面，直到遍历完 word 内容的全子对象

- 处理表格对象数据

```py
'''获取表格数据，转换为dataframe数据结构'''
def get_table_dataframe(table):
    date = []
    keys = None
    for i, row in enumerate(table.rows):
        # 获取表格一行的数据
        text = (cell.text for cell in row.cells)  # text为generator生成器类型
        # 判断是否是表头
        if i == 0:
            keys = tuple(text)
            continue
        date.append(dict(zip(keys, text)))  # zip方法，按列打包为元组的列表。再转换为字典
    df = pd.DataFrame(date)  # pd依赖的DataFrame方法将字典数据转换成列表集
    return df
```

- 遍历 word 文档对象

```py
# 遍历word文档，最后调用函数没有返回值时停止遍历
for block in iter_block_items(doc):
    # print(block.style.name)
    # 判断是否是表格
    if block.style.name == 'Table Grid':
        df = get_table_dataframe(block)
        print(df)
    # 判断该子对象是否是正文
    elif block.style.name == 'Normal':
        print(block.text)
    # 判断是否为标题1。如果是Heading 2则判断是否为标2，以此类推。
    elif block.style.name == 'Heading 1':
        print(block.text)
```

运行效果如下：

```
这是标题1
这是正文的一段话。下面是表格。

   1  2  3
0  1  1  2
1  3  1  2
2  3  1  3

这是正文的一段话。上面是表格
```

- 保存表格对象数据
- - 保存到 csv

```py
# path为：保存路径+文件名.csv。sep表示用逗号分隔,index是否要索引，header是否要列名
df.to_csv(path, sep=',', index=False, header=True, encoding='utf_8_sig')
```

- - 保存到 excel

```py
# path为：保存路径+文件名.xlsx。
df.to_excel(path, index=False, header=True, encoding='utf_8_sig')
```

- 读取表格数据

如果之后还需要读取在 csv 或者 excel 中的数据，我们可以用一下方法获取数据。

- - 从 csv 中读取

```py
df = pd.read_csv(path)
```

- - 从 excel 中读取

```py
# 读取工作簿第一个表
df = pd.read_excel(path, sheet_name='Sheet1')
```

### Reference

[Python 遍历读取 Word 文档全部内容](https://www.cnblogs.com/wl0924/p/16531087.html)

**2023.08.30**
