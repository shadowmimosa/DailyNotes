<font size=4 face='楷体'>

## 字典批量赋值、更新

### 赋值

- 批量给键赋值

  ```python
  keys = {'Google': '', 'Runoob': '', 'Taobao': ''}
  values = ['google', 'runoob', 'taobao']

  dict_obj = dict(zip(keys.keys(), values))
  print(dict_obj)

  # {'Google': 'google', 'Runoob': 'runoob', 'Taobao': 'taobao'}
  ```

- 给可迭代对象赋值

  ```python
  keys = ['google', 'runoob', 'taobao']
  dict_obj = dict.fromkeys(keys, 1)
  print(dict_obj)

  # {'google': 1, 'runoob': 1, 'taobao': 1}
  ```

- 将两个列表组合字典

  ```python
  keys = ['Google', 'Runoob', 'Taobao']
  values = ['google', 'runoob', 'taobao']
  print(dict(zip(keys,  values)))

  # {'Google': 'google', 'Runoob': 'runoob', 'Taobao': 'taobao'}
  ```

### 更新

- 赋值

  ```python
  dict_obj = {'Google': 'google', 'Taobao': 'taobao'}
  dict_obj.update(Tianmao='tianmao', JinDong='jindong')
  print(dict_obj)

  # {'Google': 'google', 'Taobao': 'taobao', 'Tianmao': 'tianmao', 'JinDong': 'jindong'}
  ```

- 列表中嵌套元组

  ```python
  dict_obj = {'Google': 'google', 'Taobao': 'taobao'}
  dict_obj.update([('Jack', 'jack'), ('Tom', 'tom')])
  print(dict_obj)

  # {'Google': 'google', 'Taobao': 'taobao', 'Jack': 'jack', 'Tom': 'tom'}
  ```

- zip 关联两个列表

  ```python
  dict_obj = {'Google': 'google', 'Taobao': 'taobao'}
  keys = ['Lisa', 'Bruce']
  values = ['lisa', 'bruce']
  dict_obj.update(list(zip(keys, values)))
  print(dict_obj)

  # {'Google': 'google', 'Taobao': 'taobao', 'Lisa': 'lisa', 'Bruce': 'bruce'}
  ```

## Reference

[python 批量给字典赋值，更新字典](https://blog.csdn.net/weixin_43835542/article/details/111357558)

**2021.04.29**
