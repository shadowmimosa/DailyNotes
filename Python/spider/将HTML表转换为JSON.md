<font size=4 face='楷体'>

## 将 Html 中表格转化为 Json

eg.

``` python
# html字符串
html_data = """
<table>
  <tr>
    <td>Card balance</td>
    <td>$18.30</td>
  </tr>
  <tr>
    <td>Card name</td>
    <td>NAMEn</td>
  </tr>
  <tr>
    <td>Account holder</td>
    <td>NAME</td>
  </tr>
  <tr>
    <td>Card number</td>
    <td>1234</td>
  </tr>
  <tr>
    <td>Status</td>
    <td>Active</td>
  </tr>
</table>
"""

import json
from bs4 import BeautifulSoup
from collections import OrderedDict

table_data = [[cell.text for cell in row("td")]
                         for row in BeautifulSoup(html_data)("tr")]
# 不关心字典顺序
print json.dumps(dict(table_data))

# 关心字典顺序
print json.dumps(OrderedDict(table_data))
```

### Reference

[python – 将 HTML 表转换为 JSON](http://www.cocoachina.com/cms/wap.php?action=article&id=65591)

**2021.04.28**
