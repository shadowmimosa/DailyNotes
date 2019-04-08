<font size=4>

[Link](https://blog.csdn.net/weixin_38332967/article/details/81159219)  
 
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

a = "哈哈"


#字符串转换成字节
b = bytes(a,encoding='utf-8')
print(b)
b1 = bytes(a,encoding='gbk')
print(b1)

#将字节转换成字符

c=str(b,encoding='utf-8')
print(c)

c1=str(b1,encoding='gbk')
print(c1)
```