<font size=4 face='楷体'>

python3中的filter与python2中的是不一样的   
其中，在python2中  
`filter(function, iterable)` filter返回的是一个list，可以直接使用它
```
#在python2中
q = filter(lambda x:x%2 == 0, range(1,10))
print(q)
#输出：「 2，4，6，8」
```

然而在python3中就不一样了;   
filter返回的并不是一个list，而是一个filter对象   
结果是：  
```
<filter object at 0x7f5e4661dcc0>
```
应该将filter转换成list，如下：
```
q = list(filter(lambda x:x%2 == 0, range(1,10)))
```