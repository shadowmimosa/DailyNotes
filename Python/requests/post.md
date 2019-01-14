<font size=4 face='楷体'>  


## 使用 requests 发送 post 请求  

一个 http 请求包括三个部分：
- 请求头
- 请求报头
- 消息主体  

HTTP 协议规定 post 提交的数据必须放在消息主体中。服务端根据请求头中的 `Content-Type` 字段来获知请求中的消息主体是用何种方式进行编码，再对消息主体进行解析。具体的编码方式包括：  
- application/x-www-form-urlencoded 
   最常见post提交数据的方式，以form表单形式提交数据
- application/json 
   以json串提交数据
- multipart/form-data 
   一般使用来上传文件  


### 以 form 形式发送数据  

requests 支持以 form 表单形式发送 post 请求，只需要将请求的参数构造成一个字典，然后传给 `requests.post()` 的 `data` 参数即可  

```python
# 获取小米有品的分类信息  
import requests

headers = {
        "Host": "youpin.mi.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://youpin.mi.com/",  # 必须带这个参数，不然会报错
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
             }
url = "https://youpin.mi.com/app/shopv3/pipe"
form_data = {"data": '{"result": {"model": "Homepage", "action": "BuildClass", "parameters": {"id": -6}}}'}
results = requests.post(url, data=form_data, headers=headers,verify=False).text
print(results)
```


### 以 json 形式发送数据  

可以将一串 json 数据传给 `requests.post()` 的 `data` 参数  

```python
# http://jinbao.pinduoduo.com/index?page=1里面的分类，
import requests
import json

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "Referer": "http://jinbao.pinduoduo.com/index?page=5",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
url = "http://jinbao.pinduoduo.com/network/api/common/goodsList"
pyload = {"keyword": "", "sortType": 0, "withCoupon": 0, "categoryId": 16, "pageNumber": 1,"pageSize": 60}
response = requests.post(url, data=json.dumps(pyload), headers=headers).text
print(response
```  

这里的 `data=json.dumps(pyload)`, 因为在 python 中，json 被视作一个 dict, `json.dumps()` 是将 json 字典，转换为 json 字符串；  
这里也可以直接使用 requests 的 `json` 参数传参，`json=pyload`  


### 以 multipart 形式发送数据  

requests 也支持以 multipart 形式发送 post 请求，只需将一文件传给 `requests.psot()` 的 files 参数即可  

```python
import requests

url = 'http://httpbin.org/post'
files = {'file': open('report.txt', 'rb')}
r = requests.post(url, files=files)
print(r.text)
```


## Reference  

[Python 使用requests发送POST请求](https://blog.csdn.net/weixin_40283480/article/details/79208413)  

**2019.1.7**