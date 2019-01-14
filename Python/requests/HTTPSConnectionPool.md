<font size=4 face='楷体'>  

## requests.exceptions.SSLError: HTTPSConnectionPool

### 使用 requests 在访问某些网址时，报错：SSLError  

这是因为这个网页的证书没有被官方CA机构信任，所以这里会出现证书验证错误；  
典型 url 如：https://www.12306.cn  

直接访问这种的 url, 就会抛出异常
```python
import requests

re = requests.get('https://www.12306.cn')
```

### 解决方法  

比较粗暴的解决方法:  
```python
import requests

re = requests.get('https://www.12306.cn', verify=False)
```  

requests 增加传参 `verify=false`, 绕过验证；  
目前尚未发现这种方法的弊端  


[Link](https://blog.csdn.net/a19990412/article/details/80358084)


**2019.1.7**