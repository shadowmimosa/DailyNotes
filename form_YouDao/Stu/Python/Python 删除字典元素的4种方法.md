<font size=4 face='楷体'>

1. Python字典的clear()方法（删除字典内所有元素）  
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
dict = {'name': '我的博客地址', 'alexa': 10000, 'url': 'http://blog.csdn.net/uuihoo/'}
dict.clear();  # 清空词典所有条目
```

2. Python字典的pop()方法（删除字典给定键 key 所对应的值，返回值为被删除的值） 
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
site= {'name': '我的博客地址', 'alexa': 10000, 'url':'http://blog.csdn.net/uuihoo/'}
pop_obj=site.pop('name') # 删除要删除的键值对，如{'name':'我的博客地址'}这个键值对
print pop_obj   # 输出 ：我的博客地址
```

3. Python字典的popitem()方法（随机返回并删除字典中的一对键和值）
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
site= {'name': '我的博客地址', 'alexa': 10000, 'url':'http://blog.csdn.net/uuihoo/'}
pop_obj=site.popitem() # 随机返回并删除一个键值对
print pop_obj   # 输出结果可能是{'url','http://blog.csdn.net/uuihoo/'}
```

4. del 全局方法（能删单一的元素也能清空字典，清空只需一项操作）
```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
site= {'name': '我的博客地址', 'alexa': 10000, 'url':'http://blog.csdn.net/uuihoo/'}
del site['name'] # 删除键是'name'的条目 
del site  # 清空字典所有条目
```

[参考](https://blog.csdn.net/uuihoo/article/details/79496440)