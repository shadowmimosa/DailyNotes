<font size=4 face='楷体'>

在 python3 中将 stringIO 归入到了 io 中，所以导入方式有变化  
Change `import StringIO` to `from io import StringIO`  

StringIO.StringIO 和 cStringIO.StringIO 在 Python3 中改为 ~~io.StringIO~~ StringIO  

遇到 string argument expected, got 'bytes' 这种报错时，可以尝试改为 io.BytesIO