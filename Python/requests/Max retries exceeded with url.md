<font size=4 face='楷体'>  

### requests 请求报错：`Max retries exceeded with url`  

及时关闭 http 连接：

```python
session = requests.session()
session.keep_alive = False  # Max retries exceeded with url 错误，及时关闭http连接
response = session.get(url, headers=headers)
```


[Link](https://www.cnblogs.com/dailycode/p/9582213.html)