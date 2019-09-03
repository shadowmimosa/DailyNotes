<font size=4 face='楷体'>

## Python float 计算精度问题

在一次处理微信支付的时候，发现一个简单的计算出了 bug  
栗子：

```python
print(2 - 1.59)
```

输出：

> 0.4099999999999999

浮点数的具体原理日后再做深究，暂且先看如果处理

### 使用 decimal 模块

Python 提供了 decimal 模块用于十进制数学计算，它具有以下特点：

- 提供十进制数据类型，并且存储为十进制数序列
- 有界精度：用于存储数字的位数是固定的，可以通过 decimal.getcontext（）.prec=x 来设定，不同的数字可以有不同的精度
- 浮点：十进制小数点的位置不固定（但位数是固定的）

改进后的栗子：

```python
from decimal import Decimal

# 保留两位
print('{:.2f}'.format(Decimal('2') - Decimal('1.59')))
```

输出：

> 0.41

### 使用 round 模块

在中午吃饭的时候，跟某研究生说起这个。。然后发现，其实一个四舍五入就行

栗子：

```python
# 保留两位
print(round(2 - 1.59, 2))
```

输出：

> 0.41

使用起来比 decimal 方便很多  
但网上查到的 python 处理 float 精度问题都是清一色的用 decimal  
具体差异还是日后再做深究，目前的需求，这两个都能满足

### 性能

既然具体实现原理先不深究，这里先简单做个性能对比

- 测试函数设计：

  ```python
    from decimal import Decimal
    import time


    def timer(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            f = func(*args, **kwargs)
            end_time = time.time()
            print("执行函数{}使用了{}秒".format(
                getattr(func, "__name__"), end_time - start_time))
            return f

        return wrapper


    @timer
    def test_decimal():
        for _ in range(1000000):
            num = '{:.2f}'.format(Decimal('2') - Decimal('1.59'))


    @timer
    def test_round():
        for _ in range(1000000):
            number = round(2 - 1.59, 2)


    if __name__ == "__main__":
        test_round()
        test_decimal()
    ```

- 执行后输出：

  > 执行函数 test_round 使用了 0.8265297412872314 秒
  > 执行函数 test_decimal 使用了 2.240535020828247 秒

- 结论：

  > 多次运行测试函数后：
  > 使用 round 执行一百万次大概耗时在 0.7 - 1.1 左右；
  > 使用 decimal 执行一百万次大概耗时在 2.1 - 2.2 左右。

  由此可见：

  > round 耗时更低，而 decimal 更..稳定？

## Reference

[Python3.+ float 精确度的问题](https://www.jianshu.com/p/01ecc435ec8e)
[python--使用浮点类型 float 计算后，数值不对](https://www.cnblogs.com/wangyanyan/p/9543395.html)

**2019.8.9**
