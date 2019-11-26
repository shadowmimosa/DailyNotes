<font size=4 face='楷体'>

## 使用 xlsxwrite 模块向 Excel 中插入图片

python 中其它的操作 Excel 的模块好像暂时不支持插入图片，这里只使用 xlsxwriter 的 `insert_image()` 功能

xlsxwriter 暂时不支持读取和修改，只能新建。可以结合其它模块使用

### worksheet.insert_image()

**insert_image(row, col, image[, options])**

在工作表单元格中插入一张图片。

- 参数：

  row(int) - 单元格所在的行（索引从 0 开始计数）
  col(int) - 单元格所在的列（索引从 0 开始计数）
  image(string) - 图片文件名（如有需要含路径）
  options(dict) - 可选的图片位置，缩放，url 参数

这种方法可用于向工作表插入图片。图片可以是 PNG， JPEG 或者 BMP 格式的：

```python
worksheet.insert_image('B2', 'python.png')
```

文件路径可与图片文件名一起指定：

```python
worksheet1.insert_image('B10', '../images/python.png')
worksheet2.insert_image('B20', r'c:\images\python.png')
```

insert_image()方法接受字典形式的可选参数来定位和缩放图片。可用的参数和它们的默认值有：

    {
    'x_offset': 0,
    'y_offset': 0,
    'x_scale': 1,
    'y_scale': 1,
    'url': None,
    'tip': None,
    'image_data': None,
    'positioning': None,
    }

- offset 的值是以像素为单位的：
  ```python
  worksheet1.insert_image('B2', 'python.png', {'x_offset': 15, 'y_offset': 10'})
  ```
  offset 的值可以大于基础单元格的宽度与高度。如果想将两个及以上的图片相对于同一单元格对齐，这有时会很有用。
- x_scale 和 y_scale 参数可以用于水平及垂直的缩放图片：
  ```python
  worksheet.insert_image('B3', 'python.png', {'x_scale': 0.5, 'y_scale': 0.5})
  ```
- url 参数可以为图片添加超链接/url，tip 参数为含有超链接的图片提供可选的鼠标悬停时的提示信息：
  ```python
  worksheet.insert_image('B4', 'python.png', {'url': 'http://python.org'})
  ```
- image_data 参数用于在 io.BytesIO 中添加内存中的字节流：
  ```python
  worksheet.insert_image('B5', 'python.png', {'image_data': image_data})
  ```
  这通常用来从 URL 中添加图片：
  ```python
  url = 'http://python.org/logo.png'
  image_data = io.BytesIO(urllibs.urlopen(url).read())
  worksheet.insert_image('B5', url, {'image_data': image_data})
  ```
  当使用 image_data 参数时文件名必须传递到 insert_image()因为这是 Excel 要求的。在前面的例子中文件名是从 URL 字符串中提取的。
- positioning 参数可以用来控制图片对象的位置：

  ```python
  worksheet.insert_image('B3', 'python.png', {'positioning': 1})
  ```

  postioning 有以下允许的值：

        1.移动和调整单元格的大小
        2.移动但不调整单元格的大小（默认）
        3.不移动或调整单元格的大小

注意：
如果由于字体大小大于默认字体大小或者打开了文本换行而导致更改了默认行高，则图片的缩放可能会受到影响。
如果它与插入的图像交叉，你应该使用 set_row()方法明确的设定行高来避免此问题。

BMP 图片只向后兼容。由于 BMP 图片不能压缩，通常情况下最好避免使用 BMP 图片。如果使用 BMP 图片，必须是 24bit、true color、bitmap 的。

### 实际使用

以上其实是从官方文档翻译的，大部分没什么问题。~~`postioning` 这个参数尝试多次没有效果。~~ 这里理解错了
最后只能通过手动调节单元格大小

```python
import xlsxwriter
from PIL import Image
from io import BytesIO
from urllib.request import urlopen

img_data = BytesIO(urlopen(img).read()) # 通过链接得到二进制图片
pic = Image.open(img_data) # 使用 PIL 打开图片

width, height = pic.size[0], pic.size[0] # 获取图片大小

# 新建 sheet 
workbook = xlsxwriter.Workbook("./data.xlsx")
worksheet = workbook.add_worksheet("sheet 1")

# 设置单元格
worksheet.set_row(1, height)
worksheet.set_column("A:A", width)

worksheet.insert_image(
    "A1", "img", {
        "image_data": img_data,
        "x_offset": 1,
        "y_offset": 1,
        "x_scale": 1,
        "y_scale": 1,
        "positioning": 1 # 这个参数不知道是什么问题，没有效果（雾
    })
```

经某群友指正，这里的 `positioning` 参数指的是 **插入的图片会不会随着单元格变化而变化**  
并不是开始理解的随着图片大小调整单元格，所以还是要手动调整单元格大小

### Reference

[Python Excel 操作模块 XlsxWriter 之插入图片 worksheet.insert_image()](https://blog.csdn.net/auserbb/article/details/79259328)
[XlsxWriter 的使用](https://www.jianshu.com/p/187e6b86e1d9)

### Written in the end

昨晚电脑开始疯狂蓝屏，最后 Chrome 浏览器的几百个标签页没了，心痛  
还没整理，四舍五入等于没记得过

所以以后坚决 **今日事今日毕**，做个**行动派**

以及早睡早起（XD

**2019.11.18**
