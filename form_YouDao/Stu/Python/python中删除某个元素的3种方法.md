<font size=4 face='楷体'>

python中关于删除list中的某个元素，一般有三种方法:remove、pop、del

1. remove: 删除单个元素，删除首个符合条件的元素，按值删除  
举例说明:
>>> str=[1,2,3,4,5,2,6]  
>>> str.remove(2)  
>>> str  
[1, 3, 4, 5, 2, 6]

2. pop:  删除单个或多个元素，按位删除(根据索引删除)  
>>> str=[0,1,2,3,4,5,6]  
>>> str.pop(1)   #pop删除时会返回被删除的元素  
>>> str  
[0, 2, 3, 4, 5, 6]  
>>> str2=['abc','bcd','dce']  
>>> str2.pop(2)  
'dce'  
>>> str2  
['abc', 'bcd']  

3. del：它是根据索引(元素所在位置)来删除  
举例说明:
>>> str=[1,2,3,4,5,2,6]  
>>> del str[1]  
>>> str  
[1, 3, 4, 5, 2, 6]  
>>> str2=['abc','bcd','dce']  
>>> del str2[1]  
>>> str2  
['abc', 'dce']  

除此之外，del还可以删除指定范围内的值。  
>>> str=[0,1,2,3,4,5,6]  
>>> del str[2:4]  #删除从第2个元素开始，到第4个为止的元素(但是不包括尾部元素)  
>>> str  
[0, 1, 4, 5, 6]  

del 也可以删除整个数据对象(列表、集合等)  
>>> str=[0,1,2,3,4,5,6]  
>>> del str   
>>> str         #删除后，找不到对象  
```
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    str
NameError: name 'str' is not defined
```
注意：del是删除引用(变量)而不是删除对象(数据)，对象由自动垃圾回收机制（GC）删除。

补充: 删除元素的变相方法   
```python
s1=(1,2,3,4,5,6)
s2=(2,3,5)
s3=[]
for i in s1:
if i not in s2:
    s3.append(i)
print 's1-1:',s1
s1=s3
print 's2:',s2
print 's3:',s3
print 's1-2:',s1
```

[参考](https://www.cnblogs.com/huangbiquan/articles/7740894.html)