<font size=4 face='楷体'>

#### python如何在列表、字典中筛选数据？

实际问题有哪些？

1. 过滤掉列表[3,9，-1,10.-2......] 中负数
2. 筛选出字典`{‘li_ming':90,'xiao_hong':60,'li_kang':95,'bei_men':98}`中值高于90的项
3. 筛选出集合`｛3,9，-1,10.-2......}`中能被3整除的数  

问题1如何解决？

- 最普通方法：
```python
#!/usr/bin/python3
 
def filter_l(data):
  res = []
  for i in data:
    if i > 0:
      res.append(i)
  return res
 
 
if __name__ == '__main__':
  data = [3, 9, -1, 10, -2]
  new_l = filter_l(data)
  print(new_l)
```

- 如何解决列表问题？

初始化列表： 生成 -10 到 10 的随机数列表，去除负数

1. filter方法:
```
#!/usr/bin/python3
 
from random import randint
 
 
def filter_l(data):
  # 循环data列表，把值一个一个取出 交个lambda中x，如何lambda函数为True，返回x生成一个新的filter对象
  return filter(lambda x: x >= 0, data)
 
if __name__ == '__main__':
  # 列表生成10个 -10 到 10 的随机数
  data = [randint(-10, 10) for _ in range(10)]
  print(data)
  # new_l 为可迭代对象
  new_l = filter_l(data)
  print(list(new_l), type(new_l))
```

2. 列表解析：
```
#!/usr/bin/python3
 
from random import randint
 
def filter_l(data):
  # 循环data列表，把值一个一个取出 是否满足if条件，满足True返回x生成一个新列表
  return [x for x in data if x >=0 ]
 
if __name__ == '__main__':
  # 列表生成10个 -10 到 10 的随机数
  data = [randint(-10, 10) for _ in range(10)]
  print(data)
  # new_l 为可迭代对象
  new_l = filter_l(data)
  print(list(new_l), type(new_l))
```

运行速度比较：解析 > filter > 普通

- 如何解决字典？

字典解析，筛选数据：
```
#!/usr/bin/python3
 
from random import randint
 
 
def filter_l(data):
  print(data.items())
  # 把字典转换成dict_items，循环里面的key和value，满足if条件返回对应的key和value值
  return {k: v for k, v in data.items() if v > 90}
 
if __name__ == '__main__':
  # 字典生成式
  data = {x: randint(0, 100) for x in range(10)}
  print(data)
  new_l = filter_l(data)
  print(new_l, type(new_l))
```

- 如何解决集合问题？
```
#!/usr/bin/python3
from random import randint
 
 
def filter_l(data):
  # 迭代集合中值，满足条件为True返回x
  return {x for x in data if x % 3 == 0}
 
if __name__ == '__main__':
  # 集合生成式
  data = {randint(0, 100) for x in range(10)}
  print(data)
  new_l = filter_l(data)
  print(new_l, type(new_l))
```

- 如何逻辑整理？

无论是解析器还是普通方法，都需要for循环，if判断，逻辑都是满足条件返回值，过滤出满足条件的值，无论是生成器还是解析器都满足这个格式：“ 返回值 for循环 if判断 “，通过lambda满足格式：“lambda 输入值：条件, 格式化数据

[参考](https://www.jb51.net/article/136692.htm)