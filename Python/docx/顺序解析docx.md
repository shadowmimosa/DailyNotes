<font size=4 face='楷体'>

## 顺序解析 docx

### 实现参考

> ## Python-docx (Reading paragraphs,tables and images in document order)

> python-docx is a Python library for creating and manipulating Microsoft Word (.docx) files. The Python-docx package cannot read paragraphs, tables and images altogther in document order. In document order, either it can only render all the paragraphs at once or all tables at once or all images at once. Here, I provide a way in which paragraphs, tables and images present in a docx file can be read in document order into a dataframe in python.

> The code is present inside the file named "Para_table_image_extraction.py". While running this code with any docx file as input, this code genertes 3 dataframes namely `combined_df`, `table_list` ( a list basically) and `image_df`.

> All the contents of the docx file(including paragraphs, tables and images) are stored in a python dataframe called `combined_df`. If an image is present after a paragraph in the document, a reference to the image will be stored in the `combined_df` dataframe, but not the actual image. You will have to refer the image index from `combined_df` and retrieve the image data from a separate dataframe called `image_df` which stores the image_index and the corresponding base64 encoded image data of each and every image that is present in the document.

> Similarly, if a table is encountered in the document, the `table_id` column in `combined_df` dataframe gets filled up. And you will have to retrieve the corresponding table that is relevant to the `table_id` from `table_list`.

> I have illustrated this code on the following word document(docx): [![docx document](https://github.com/kmrambo/Python-docx-Reading-paragraphs-tables-and-images-in-document-order-/raw/master/images/snaphot_of_docx_document.png)](https://github.com/kmrambo/Python-docx-Reading-paragraphs-tables-and-images-in-document-order-/blob/master/images/snaphot_of_docx_document.png)

> Below is a sample of `combined_df` dataframe that is created based on the above docx file.

> [![combined_df](https://github.com/kmrambo/Python-docx-Reading-paragraphs-tables-and-images-in-document-order-/raw/master/images/combined_df.png)](https://github.com/kmrambo/Python-docx-Reading-paragraphs-tables-and-images-in-document-order-/blob/master/images/combined_df.png)

> In the above dataframe:

> 1.  `para_text` column denotes the actual paragraph content of the document. (Every row represents each paragraph in the document)
> 2.  `table_id` column represents the table id of a table if a table is present in that location of the document. If no table is present, then its value is represented as "Novalue"
> 3.  `style` represents the paragraph style of the corresponding paragraph

> You should note that images and tables are not stored as such inside combined_df dataframe. A reference to those objects are only stored in combined_df. Which means for every image id or table id present in combined_df, you will have to retrieve either the image id or table id from `combined_df` and refer those ids from `image_df` for image data and `table_list` for table data.

> Image files are represented in the following notation: "**Document_Imagefile/image1.png/rId7/0** in `combined_df` which denotes that the reference is actually an image file which has "**image1.png**" as image name and "**rId7**" as the unique id or identifier for the image and "**0**" for image index to be referred in `image_df`.

> [![image_df](https://github.com/kmrambo/Python-docx-Reading-paragraphs-tables-and-images-in-document-order-/raw/master/images/image_df.png)](https://github.com/kmrambo/Python-docx-Reading-paragraphs-tables-and-images-in-document-order-/blob/master/images/image_df.png)

> Table objects are represented as "**<docx.table.Table object at 0x1020f1160>**" which denotes that a table is present at that location with the corresponding table_id. You can refer to this table_id in `table_list`'s index to fetch the relevant table as a dataframe. `table_list` contains a list of all tables stored in dataframe format.

> [![table_list](https://github.com/kmrambo/Python-docx-Reading-paragraphs-tables-and-images-in-document-order-/raw/master/images/table_list.png)](https://github.com/kmrambo/Python-docx-Reading-paragraphs-tables-and-images-in-document-order-/blob/master/images/table_list.png)

> I have not included the code to extract the images and tables from `image_df` and `table_list` using their unique identifiers from `combined_df`. The reason I have not done this is because the use case might vary from case to case. You can extract them in your own way and do whatever successive operation you wish to.

---

译文：
python-docx 是用于创建和处理 Microsoft Word（.docx）文件的 Python 库。Python-docx 包无法按文档顺序完全读取段落，表格和图像。按照文档顺序，它只能一次获取所有段落，或者一次获取所有表格，或者一次获取所有图像。在这里，我提供了一种方法，可以将 docx 文件中的段落、表格和图像按文档顺序读取到 python 的数据框中。
该代码位于“Para_table_image_extraction.py”的文件内。在以任何 docx 文件作为输入运行此代码时，此代码将生成 3 个数据帧，即“combined_df”、“table_list”和“image_df”：

- docx 文件的所有内容（包括段落，表和图像）都按顺序存储在名为“combined_df”的 python 数据帧中
- 如果在文档的段落之后出现图像，则对该图像的引用将存储在“combined_df”数据框中，而不是实际图像。您将必须从“combined_df”引用图像索引，并从名为“image_df”的单独数据帧中检索图像数据，该数据帧存储 image_index 和每个图像的相应 base64 编码图像数据
- 类似地，如果在文档中遇到表，则将填充“combined_df”数据框中的“table_id”列。而且，您将不得不从“table_list”中检索与“ table_id”相关的对应表
  下图是示例 word 文档（docx）：
  ![](http://www.writebug.com/myres/static/uploads/2021/10/19/f77b943dbe95d174955c3cf63775ea2a.writebug)
  下图是根据上述 docx 文件生成的“combined_df”数据帧:
  ![](http://www.writebug.com/myres/static/uploads/2021/10/19/2f6488a53537d50a994d05c7a5a35032.writebug)
  在上述数据帧中：
- **para_text**：表示文档的实际段落内容（每一行代表文档中的每个段落）
- **table_id**：表示表格的表 ID（如果在该文档的该位置存在表）。如果没有表格，则其值表示为“ Novalue”
- **style**：代表相应段落的段落样式
  注意，图像和表格不会这样存储在 combined_df 数据框中。对这些对象的引用仅存储在 combined_df 中。这意味着对于在 Combined_df 中存在的每个图像 ID 或表格 ID，您将必须从 combined_df 中检索图像 ID 或表格 ID，并从 image_df 和 table_list 中根据这些 ID 来获取图像数据或表格数据。
  图像文件以以下符号表示：

```
combined_df中的 Document_Imagefile/image1.png/rId7/0
```

这表示该引用实际上是一个图像文件，其中“image1.png”作为图像名称，“rId7”作为图像的唯一 ID 或标识符，“0”图片索引将在 image_df 中引用。
![](http://www.writebug.com/myres/static/uploads/2021/10/19/36cdb9e9a5cad8fcf602295bc8298a88.writebug)
表格对象表示为“<docx.table.0x1020f1160 处的表对象>”，它表示在该位置存在一个带有相应 table_id 的表。您可以在“table_list”索引中根据 table_id 来获取获取表格数据。table_list 包含所有表格的信息。
![](http://www.writebug.com/myres/static/uploads/2021/10/19/9dbf841cf01738931f8f625010167985.writebug)
我还没有包含使用来自 combined_df 的唯一标识符从 image_df 和 table_list 提取图像和表格的代码。我之所以没有这样做，是因为用例可能因情况而异。您可以用自己的方式提取它们，然后执行您希望执行的任何后续操作。

### Reference

[原文链接](https://github.com/kmrambo/Python-docx-Reading-paragraphs-tables-and-images-in-document-order)
[译文链接](https://www.writebug.com/code/0c4abf18-c792-11ed-89d3-6479f0e5e323/#)

**2023.08.30**
