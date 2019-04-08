<font size=4 face="楷体">

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

#### 读取文件报错

***

- 报错实例：  
```python
    #读取模板信息：
    result = list()
    opendemo = open(demopath, 'r')
    demo = opendemo.readlines()
    opendemo.close()
    demolen = len(demo)
```

- 错误信息：  
```python
UnicodeDecodeError: 'gbk' codec can't decode byte 0xae in position 439: illegal multibyte sequence
```

- 解决方法：
```python
    #读取模板信息：
    result = list()
    opendemo = open(demopath, 'r',encoding='UTF-8')
    demo = opendemo.readlines()
    opendemo.close()
    demolen = len(demo)
```

- 原因：打开文件编码格式不对
- 需给定一个打开编码格式

[参考信息](https://www.cnblogs.com/arctique/p/5699620.html)

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

#### 编码出错

***

- 报错实例：  
```python
print(***.decode('utf-8'))
```


- 解决方法：  
    可以修改为 `print(***.encode('utf-8').decode('utf-8'))`，意义不大  
    直接删除`decode('utf-8')`


- 原因：
    python3默认编码格式就是Unicode，str和byte也是严格分开的

[参考信息](https://www.cnblogs.com/zhxhdean/p/3173663.html)

#### json.decoder.JSONDecodeError

***

- The key or value in Dictionary lacks quotation marks.