<font size=4 face='楷体'>  

### Dict 遍历  

```python
if key in dict.keys():
    print("判断 key 是否存在于键中")

if values in dict.values():
    print("判断 value 是否存在于值中")

if key, value in dict.item():
    print("判断 key, value 是否存于字典项中")
```

同样的，可以使用 `for` 遍历字典：

```python 
for key in dict:
    print("遍历键")
    for key in dict.key():
        print("也可以这样遍历")

for value in dict.values():
    print("遍历值")    

for kv in dict.items():
    print("遍历字典项")

for key, value in dict.items():
    print("遍历字典键值")
    for (key, value) in dict.items():
        print("也可以这样遍历")
```  

有待整理 [Python 字典常用方法总结](https://www.cnblogs.com/chendai21/p/8137601.html)

**2018.12.25**