<font size=4 face="楷体">


#### import包时出错

***

原因：  
- 注意文件名不能与包名重复
- 把.py文件命名与包名重复了，所以调用时一直报错，我把脚本文件改一下名，问题解决了  

[详细信息](https://bbs.csdn.net/topics/392402946)

#### 打开文件出错

***

- 报错实例：  
```
home='C:\Users\ShadowMimosa\Desktop\STU\Top\Lib'
```

- 错误信息：  
```python
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
```

- 解决方法：
```
home='C:\\Users\ShadowMimosa\Desktop\STU\Top\Lib'
采用双反斜杠
```

- 原因：文件名中的 \U 开始的字符被编译器认为是八进制  
- 以后注意凡是有'\\'的文件路径都尽量采用双反斜杠的写法，避免这类问题

[参考信息](https://www.cnblogs.com/zhxhdean/p/3173663.html)

#### Python3对字典操作时遇到错误：dictionary changed size during iteration

- 报错实例：  
```
a={'a':1, 'b':0, 'c':1, 'd':0}
for key in a.keys():
	del a[key]
```

- 错误信息：  
```python
dictionary changed size during iteration
```

- 解决方法：
```
a={'a':1, 'b':0, 'c':1, 'd':0}
for key in list(a.keys()):
	del a[key]
```

- 原因：字典在遍历时不能进行修改
- 建议转成列表或集合处理
 
[参考信息](https://blog.csdn.net/zhihaoma/article/details/51265168)