<font size=4 face='楷体'>

## multipart/form-data 类型请求以及 boundary 值

使用 requests_toolbelt 包

```python
from requests_toolbelt import MultipartEncoder
import requests

def test():
    m = MultipartEncoder(fields={'data': data},
                          boundary='----WebKitFormBoundary')
    header.update({'Content-Type': m.content_type})
    params = {}
    url = ''
    response = requests.post(url,
                       params=params,
                              data=m,
                              headers={'Content-Type': m.content_type})

 if __name__ == '__main__':
    test()
```

### Reference

[Python requests 库处理 multipart/form-data 请求以及 boundary 值问题](https://blog.csdn.net/Enderman_xiaohei/article/details/89421773)

**2021.08.13**
