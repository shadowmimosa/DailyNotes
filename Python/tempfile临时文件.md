<font size=4 face='楷体'>

## opencv 提取替换颜色

大量临时数据放在内存中会占用大量资源，可以使用临时文件来进行储存
临时文件不用命名，且使用后会被自动删除

### TemporaryFile

使用 TemporaryFile 创建的临时文件没有文件名，在文件系统中找不到，只能被当前进程访问

```python
import tempfile


f = tempfile.TemporaryFile()
f.write(b'test')
f.seek(0)
print(f1.read())
```

### NamedTemporaryFile

使用 NamedTemporaryFile 创建的临时文件有文件名，在文件系统中可以找到，因此可以多个进程同时访问

```python
import tempfile

f = tempfile.NamedTemporaryFile()
f.write(b'test')
print(f.name)
f.seek(0)
print(f2.read())
```

### Reference

[Python tempfile (临时文件)](https://www.cnblogs.com/dbf-/p/11383758.html)

**2020.12.30**
