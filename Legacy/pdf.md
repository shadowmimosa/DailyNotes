<font size=4 face='楷体'>

## PDF 转换

### poppler

[poppler](https://poppler.freedesktop.org/)
[python-poppler-qt5](https://github.com/frescobaldi/python-poppler-qt5)

### PyMuPDF & fitz & traits

- 需要的库

**traits**

```bash
pip install traits‑5.2.0‑cp37‑cp37m‑win_amd64.whl
```

> 注意, traits 要先在[这里](https://www.lfd.uci.edu/~gohlke/pythonlibs/#traits)下载

**fitz**

```bash
https://www.lfd.uci.edu/~gohlke/pythonlibs/#traits
```

**PyMuPDF**

```bash
pip install PyMuPDF
```

- 代码

```py
import fitz

'''
# 将PDF转化为图片
pdfPath pdf文件的路径
imgPath 图像要保存的文件夹
zoom_x x方向的缩放系数
zoom_y y方向的缩放系数
rotation_angle 旋转角度
'''
def pdf_image(pdfPath,imgPath,zoom_x,zoom_y,rotation_angle):
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.writePNG(imgPath+str(pg)+".png")
    pdf.close()

pdf_image(r"C:\Users\12624\Desktop\a.pdf",r"C:\Users\12624\Desktop\\",5,5,0)
```

_**zoom_x 和 zoom_y 一般取相同值, 值越大, 图像分辨率越高。**_

### PythonMagick & wand

[利用 Python 将 pdf 转为图片](https://www.jianshu.com/p/dd225ba31be4)

## PDF 文字提取

pdfplumber 应用层需要写的代码很少, 还能自动提取表格, 但有一个问题绕不过去

`pdfminer.pdfparser.PDFSyntaxError: No /Root object! - Is this really a PDF?`

pdfplumber 用 pdfminer 解析 pdf 文件, pdfminer 的官网上 2020 年就有人提这个问题[issues-476](https://link.zhihu.com/?target=https%3A//github.com/pdfminer/pdfminer.six/issues/476)
2023 年 08 月 30 号去看,issues 还是标为 open 状态

用 fitz 能正常打开上述 pdf 文件

[Wayne：Python 处理 PDF 神器：PyMuPDF 的安装与使用](https://zhuanlan.zhihu.com/p/517737462)

可以用`page.get\_text('text')`得到文字内容, 包括了表格里的文字, 如果用`page.get\_text('blocks')`, 会得到一个列表

![](https://pic1.zhimg.com/v2-952455fcbc785227886eae2e6871d944_b.jpg)

```
(79.66999816894531, 45.409751892089844, 515.573974609375, 59.409751892089844, 'A200000中华人民共和国企业所得税月（季）度预缴纳税申报表（A类）\n', 0, 0),
(171.65000915527344, 70.24056243896484, 423.6499938964844, 80.74056243896484, '税款所属期间：2022年01月01日  至  2022年03月31日\n', 1, 0),
(26.850000381469727, 85.3735580444336, 568.449951171875, 111.00756072998047, '纳税人识别号（统一社会信用代码）：**********\n纳税人名称：~~~~~~~~~~\n金额单位：人民币元(列至角分)\n', 2, 0),
(55.82500076293945, 120.56056213378906, 232.09999084472656, 131.06056213378906, '预缴方式\n按照实际利润额预缴\n', 3, 0),
(55.82500076293945, 143.31056213378906, 179.59999084472656, 153.81056213378906, '企业类型\n一般企业\n', 4, 0),
(218.84999084472656, 164.9105682373047, 376.4024658203125, 175.4105682373047, '优 惠 及 附 报 事 项 有 关 信 息\n', 5, 0),
```

看起来是坐标, 内容, 行, 列
坐标是左、上、右、下

---

附 pdfplumber 读文本的代码

```py
@classmethod
def get_content(cls, pdf_path: str or Path) -> (str, []):
    pdf_text = ''
    pdf_table = []
    with pdfplumber.open(pdf_path) as pdf:
        # print(len(pdf.pages))
        if len(pdf.pages) >= 0:
            page = pdf.pages[0]
            # Table settings.
            ts = {
                "vertical_strategy": "lines",
                "horizontal_strategy": "lines",
            }

            # Get the bounding boxes of the tables on the page.
            bboxes = [table.bbox for table in page.find_tables(table_settings=ts)]

            def not_within_bboxes(obj):
                """Check if the object is in any of the table's bbox."""

                def obj_in_bbox(_bbox):
                    """See https://github.com/jsvine/pdfplumber/blob/stable/pdfplumber/table.py#L404"""
                    v_mid = (obj["top"] + obj["bottom"]) / 2
                    h_mid = (obj["x0"] + obj["x1"]) / 2
                    x0, top, x1, bottom = _bbox
                    return (h_mid >= x0) and (h_mid < x1) and (v_mid >= top) and (v_mid < bottom)

                return not any(obj_in_bbox(__bbox) for __bbox in bboxes)

            pdf_text = page.filter(not_within_bboxes).extract_text()
            # print('---------------------------------')
            pdf_table = page.extract_table()
    return pdf_text, pdf_table
```

### Reference

[python 实现高质量 PDF 转 PNG](https://zhuanlan.zhihu.com/p/102742847)
[python 用 fitz 读取 Pdf 中的文字](https://zhuanlan.zhihu.com/p/575233497)

**Create On 2020.12.04, Update On 2023.08.30**
