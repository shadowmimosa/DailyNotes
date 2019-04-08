<font size=4 face='楷体'>

- 遍历key值
>>> a  
{'a': '1', 'b': '2', 'c': '3'}  
>>> for key in a:  
       print(key+':'+a[key])  
a:1  
b:2  
c:3  
>>> for key in a.keys():  
       print(key+':'+a[key])  
a:1  
b:2  
c:3  

在使用上，for key in a和 for key in a.keys():完全等价。

- 遍历value值
 
>>> for value in a.values():  
       print(value)  
1  
2  
3  

- 遍历字典项
 
>>> for kv in a.items():  
       print(kv)  
('a', '1')  
('b', '2')  
('c', '3')  

- 遍历字典健值

>>> for key,value in a.items():  
       print(key+':'+value)  
a:1  
b:2  
c:3  
>>> for (key,value) in a.items():  
       print(key+':'+value)  
a:1  
b:2  
c:3  

[参考](https://www.cnblogs.com/stuqx/p/7291948.html)