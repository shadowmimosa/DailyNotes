<font size=4 face='楷体'>

## openpyxl 常用方法

- 安装

  ```bash
  pip install openpyxl
  ```

- 打开文件
- - 创建
    ```python
    from  openpyxl import  Workbook
    # 实例化
    wb = Workbook()
    # 激活 worksheet
    ws = wb.active
    ```
- - 打开
    ```python
    from openpyxl  import load_workbook
    wb2 = load_workbook('文件名称.xlsx')
    ```

- 储存数据

  ```python
  # 方式一：数据可以直接分配到单元格中(可以输入公式)
  ws['A1'] = 42
  # 方式二：可以附加行，从第一列开始附加(从最下方空白处，最左开始)(可以输入多行)
  ws.append([1, 2, 3])
  # 方式三：Python 类型会被自动转换
  ws['A3'] = datetime.datetime.now().strftime("%Y-%m-%d")
  ```

- 创建表

  ```python
  # 方式一：插入到最后(default)
  ws1 = wb.create_sheet("Mysheet")
  # 方式二：插入到最开始的位置
  ws2 = wb.create_sheet("Mysheet", 0)
  ```

- 选择表
  ```python
  # sheet 名称可以作为 key 进行索引
  ws3 = wb["New Title"]
  ws4 = wb.get_sheet_by_name("New Title")
  ws is ws3 is ws4 # True
  ```
- 查看表名

  ```python
  # 显示所有表名
  print(wb.sheetnames) # ['Sheet2', 'New Title',  'Sheet1']
  # 遍历所有表
  for sheet in  wb:
      print(sheet.title)
  ```

- 访问单元格
- - 单一单元格访问
    ```python
    # 方法一
    c = ws['A4']
    # 方法二：row 行；column 列
    d = ws.cell(row=4, column=2, value=10)
    # 方法三：只要访问就创建
    for i in  range(1,101):
        for j in range(1,101):
            ws.cell(row=i, column=j)
    ```
- - 多单元格访问
    ```python
    # 通过切片
    >>> cell_range = ws['A1':'C2']
    # 通过行(列)
    >>> colC = ws['C']
    >>> col_range = ws['C:D']
    >>> row10 = ws[10]
    >>> row_range = ws[5:10]
    # 通过指定范围(行 → 行)
    >>> for row in  ws.iter_rows(min_row=1, max_col=3, max_row=2):
    ...    for cell in  row:
    ...        print(cell)
    <Cell Sheet1.A1>
    <Cell Sheet1.B1>
    <Cell Sheet1.C1>
    <Cell Sheet1.A2>
    <Cell Sheet1.B2>
    <Cell Sheet1.C2>　
    # 通过指定范围(列 → 列)
    >>> for row in  ws.iter_rows(min_row=1, max_col=3, max_row=2):
    ...    for cell in  row:
    ...        print(cell)
    <Cell Sheet1.A1>
    <Cell Sheet1.B1>
    <Cell Sheet1.C1>
    <Cell Sheet1.A2>
    <Cell Sheet1.B2>
    <Cell Sheet1.C2>
    # 遍历所有 方法一
    >>> ws = wb.active
    >>> ws['C9'] = 'hello world'
    >>> tuple(ws.rows)
    ((<Cell Sheet.A1>, <Cell Sheet.B1>, <Cell Sheet.C1>),
    (<Cell Sheet.A2>, <Cell Sheet.B2>, <Cell Sheet.C2>),
    ...
    (<Cell Sheet.A8>, <Cell Sheet.B8>, <Cell Sheet.C8>),
    (<Cell Sheet.A9>, <Cell Sheet.B9>, <Cell Sheet.C9>))
    # 遍历所有 方法二
    >>> tuple(ws.columns)
    ((<Cell Sheet.A1>,
    <Cell Sheet.A2>,
    <Cell Sheet.A3>,
    ...
    <Cell Sheet.B7>,
    <Cell Sheet.B8>,
    <Cell Sheet.B9>),
    (<Cell Sheet.C1>,
    ...
    <Cell Sheet.C8>,
    <Cell Sheet.C9>))
    ```

- 保存数据

  ```python
  wb.save('filename.xlsx')
  ```

- 改变 sheet 标签按钮颜色

  ```python
  ws.sheet_properties.tabColor = "1072BA"
  ```

- 获取最大行, 最大列

  ```python
  # 获得最大列和最大行
  sheet.max_row
  sheet.max_column
  ```

- 获取每一行, 每一列
- - `sheet.rows` 为生成器, 里面是每一行的数据, 每一行又由一个 tuple 包裹
- - `sheet.columns`类似, 不过里面是每个 tuple 是每一列的单元格

  ```python
  # 因为按行，所以返回A1, B1, C1这样的顺序
  for row in sheet.rows:
      for cell in row:
          print(cell.value)

  # A1, A2, A3这样的顺序
  for column in sheet.columns:
      for cell in column:
          print(cell.value)
  ```

- 根据数字得到字母, 根据字母得到数字

  ```python
  from openpyxl.utils import get_column_letter, column_index_from_string

  # 根据列的数字返回字母
  print(get_column_letter(2))  # B
  # 根据字母返回列的数字
  print(column_index_from_string('D'))  # 4
  ```

- 删除工作表

  ```python
  # 方式一
  wb.remove(sheet)
  # 方式二
  del wb[sheet]
  ```

- 矩阵置换(行 → 列)

  ```python
  rows = [
      ['Number', 'data1', 'data2'],
      [2, 40, 30],
      [3, 40, 25],
      [4, 50, 30],
      [5, 30, 10],
      [6, 25, 5],
      [7, 50, 10]]

  list(zip(*rows))

  # out
  [('Number', 2, 3, 4, 5, 6, 7),
   ('data1', 40, 40, 50, 30, 25, 50),
   ('data2', 30, 25, 30, 10, 5, 10)]

  # 注意 方法会舍弃缺少数据的列(行)
  rows = [
      ['Number', 'data1', 'data2'],
      [2, 40	  ],	# 这里少一个数据
      [3, 40, 25],
      [4, 50, 30],
      [5, 30, 10],
      [6, 25, 5],
      [7, 50, 10],
  ]
  # out
  [('Number', 2, 3, 4, 5, 6, 7), ('data1', 40, 40, 50, 30, 25, 50)]
  ```

- 设置单元格风格
- - 需要导入的类
    ```python
    from openpyxl.styles import Font, colors, Alignment
    ```

- - 字体
    ```python
    # 指定了等线24号，加粗斜体，字体颜色红色。直接使用cell的font属性，将Font对象赋值给它
    bold_itatic_24_font = Font(name='等线', size=24, italic=True, color=colors.RED, bold=True)
    sheet['A1'].font = bold_itatic_24_font
    ```

- - 对齐方式
    ```python
    # 使用cell的属性aligment，这里指定垂直居中和水平居中。除了center，还可以使用right、left等等参数
    sheet['B1'].alignment = Alignment(horizontal='center', vertical='center')
    ```

- - 设置行高和列宽
    ```python
    # 第2行行高
    sheet.row_dimensions[2].height = 40
    # C列列宽
    sheet.column_dimensions['C'].width = 30
    ```

- - 设置所有行和全部列的长和宽
    ```python
    width = 2.0
    height = width * (2.2862 / 0.3612)

    print("row:", ws.max_row, "column:", ws.max_column)
    for i in range(1, ws.max_row+1):
        ws.row_dimensions[i].height = height
    for i in range(1, ws.max_column+1):
        ws.column_dimensions[get_column_letter(i)].width = width
    ```

- - 合并和拆分单元格
    所谓合并单元格，即以合并区域的左上角的那个单元格为基准，覆盖其他单元格使之称为一个大的单元格
    相反，拆分单元格后将这个大单元格的值返回到原来的左上角位置
    ```python
    # 合并单元格， 往左上角写入数据即可
    sheet.merge_cells('B1:G1') # 合并一行中的几个单元格
    sheet.merge_cells('A1:C3') # 合并一个矩形区域中的单元格
    ```
- - 合并和拆分单元格
    所谓合并单元格，即以合并区域的左上角的那个单元格为基准，覆盖其他单元格使之称为一个大的单元格
    相反，拆分单元格后将这个大单元格的值返回到原来的左上角位置
    ```python
    # 合并单元格， 往左上角写入数据即可
    sheet.merge_cells('B1:G1') # 合并一行中的几个单元格
    sheet.merge_cells('A1:C3') # 合并一个矩形区域中的单元格
    ```
    - 合并后只可以往左上角写入数据，也就是区间中:左边的坐标。
    - 如果这些要合并的单元格都有数据，只会保留左上角的数据，其他则丢弃。换句话说若合并前不是在左上角写入数据，合并后单元格中不会有数据。
    - 以下是拆分单元格的代码。拆分后，值回到 A1 位置。
    ```python
    sheet.unmerge_cells('A1:C3')
    ```

- 保存数据

  ```python
  wb.save('filename.xlsx')
  ```

### Reference

[Python_Openpyxl 浅谈（最全总结 足够初次使用）](https://blog.csdn.net/weixin_43094965/article/details/82226263)

**2020.09.07**
