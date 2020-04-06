<font size=4 face='楷体'>

## python requests 提示警告 InsecureRequestWarning

调试 requests 过程中总好出现 InsecureRequestWarning
记录一下解决方法

```python
import requests
requests.packages.urllib3.disable_warnings()
response = requests.get(url, verify=False)
```

### Reference

[python requests 提示警告 InsecureRequestWarning](https://blog.csdn.net/weixin_39461487/article/details/81132922)

**2020.04.02**
