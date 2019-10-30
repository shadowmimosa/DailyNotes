<font size=4 face='楷体'>

## redis 取值时报错

连接 redis 取值时，报了个错: `WRONGTYPE Operation against a key holding the wrong kind of value` 字面不明所以，遂百度如下

> 比如数据库中有一个 key 的数据存储的是 Hash 类型的，但是你使用 redis 执行数据操作的时候却使用了非 Hash 的操作方法

redis 取值方法用错了，在 python 里修改如下（这里以 key 的类型是 Hash 举例）：

```python
import redis

r = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
# value = r.get(key) # 直接使用 get 报错
value = r.hget(name=name, key=key) # 这里 `name` 是 redis 键名，`key` 是 这条数据的属性名
```

### Reference

[Redis 报错：WRONGTYPE Operation against a key holding the wrong kind of value 解决处理](https://www.cnblogs.com/jeffen/p/6091385.html)
[Redis：WRONGTYPE Operation against a key holding the wrong kind of value](https://blog.csdn.net/hanchao5272/article/details/79051364)
[Python操作redis（二）hash类型](https://blog.csdn.net/chenggong2dm/article/details/52126566)

**2019.10.30**
