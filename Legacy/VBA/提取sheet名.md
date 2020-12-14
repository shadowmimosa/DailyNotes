<font size=4 face='楷体'>

## 提取 sheet 名

### 使用宏

```vba
Sub GetSheetsName()

Dim sht As Worksheet
Dim i As Integer

i = 1
For Each sht In Sheets
    Cells(i, 2) = sht.Name
    i = i + 1
    Next
End Sub
```

### 使用函数

需要安装函数拓展包，未测试

```
=IFERROR(GetSheetName(ROW(A1)),'')
```

### Reference

[用 Substats 和 Shields.io 为你的个人主页定制动态数据小牌子](http://www.360doc.com/content/19/0707/10/8260830_847206132.shtml)

**2020.12.14**
