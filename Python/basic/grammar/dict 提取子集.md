<font size=4 face='楷体'>

## 从字典中提取子集

- 直接创建字典方式

  ```bash
  prices = {
      'ACME': 45.2,
      'APPLE': 612.2,
      'IBM': 205.55,
      'HPQ': 37.20,
      'FB': 10.75
  }
  >>> p1 = {key:value for key,value in prices.items() if value>200}
  >>> p1
  {'APPLE': 612.2, 'IBM': 205.55}
  ```

- 使用字典推导式
  效率是第一种的 2 倍多

  ```bash
  >>> p2 = dict((key,value) for key,value in prices.items() if value>200)
  >>> p2
  {'APPLE': 612.2, 'IBM': 205.55}
  ```

- 使用 key 与已知序列求交集
  比第一种效率还要低 1.6 倍

  ```bash
  >>> tech_names = ['IBM','APPLE']
  >>> p3 = {key:prices[key] for key in prices.keys() & tech_names }
  >>> p3
  {'APPLE': 612.2, 'IBM': 205.55}
  ```

### Reference

[python 从字典中提取子集的 3 种方法](https://www.jianshu.com/p/a4aa2d800b8e)

**2021.11.15**
