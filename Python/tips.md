<font size=4 face='楷体'>

## 小工具

### atexit

在 python 退出时强制运行一段代码

```python
import atexit
  
@atexit.register
def clean():
  print('清理环境相关的代码')
  
'''
do something
'''
```

[参考](https://www.jb51.net/article/185741.htm)

### python-magic

识别文件类型
安装需要注意一下

```python
import magic

magic.from_file('filepath')
```

[参考-1](https://www.52pojie.cn/thread-1322425-1-1.html)
[参考-2](https://www.cnblogs.com/chenyuting/p/12085337.html)

### Reference

[Python tempfile (临时文件)](https://www.cnblogs.com/dbf-/p/11383758.html)

**2020.12.30**
