<font size=4 face='楷体'>

### Requests中常用的方法

1. #### 基本的get请求

b = requests.get(url="http://12076&period;222.26:8111/login?username=13554825492&password=123456")

2. #### 带参数的get请求

r = requests.get(url="http://120.76.222.26:8111/login?",params={"username":"13554825492","password":"123456"})  
3. #### 输出get请求返回的状态码
Print(r.stutus_code)  
4. #### 输出get请求返回的数据  
Print(r.text)
5. #### 简单的post方法  
p = requests.post(url="",data={"data1":"888"})
6. #### 输出post方法的返回值，状态码  
与get方法一致