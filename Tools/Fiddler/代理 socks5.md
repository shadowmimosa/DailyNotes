<font size=4 face='楷体'>

## fiddlerScript oSession 方法等收集（发送请求、保存到文件）

### 判断请求 响应的网络状态码

```javascript
oSession.responseCode === 200
```

### 判断请求 uri 是否包含某些字符

```javascript
oSession.uriContains('xieboke.net')
oSession.fullUrl.Contains('xieboke.net')
```

### 获取返回结果并转成字符串

```javascript
oSession.GetResponseBodyAsString()
```

### 获取 json 返回结果中的中某个字段

```javascript
var response_string = oSession.GetResponseBodyAsString()

// 字符串 转成可以操作的 json 格式
var response_json = Fiddler.WebFormats.JSON.JsonDecode(response_string)
var is_double = response_json.JSONObject['isDouble']
```

### 修改 Session 的样式等

```javascript
oSession['ui-backcolor'] = 'yellow' // 背景色 - yellow 黄色，red 红色，green 绿色，Lavender 淡紫色

oSession['ui-color'] = 'red' // 字体颜色

oSession['ui-hide'] = 'true' // 不显示

oSession['ui-bold'] = 'true' // 字体加粗

oSession['ui-italic'] = 'yup' //设置字体斜体，字符串无所谓

oSession['ui-customcolumn'] = '高佣api' //设置Custom一列显示文案

FiddlerObject.playSound('C:\\windows\\media\\tada.wav') //设置请求时播放的声音
```

### 获取请求的参数

```javascript
oSession.oRequest.headers // 获取整个请求头

oSession.oRequest.headers['token'] // 获取 请求头 token 的值

oSession.oRequest.headers.Exists('Authorization') // 判断请求头 Authorization 是否存在

oSession.Hostname // 获取请求的域名

oSession.port // 获取请求的端口
```

### 修改请求头的参数

```javascript
oSession.RequestHeaders.Remove('User-Agent') // 删除 User-Agent 传参

oSession.RequestHeaders['uid'] = '0' //修改请求头
```

### 修改返回的参数

```javascript
oSession.oResponse['Cache-Control'] = 'no-cache'
```

### 打印日志

```javascript
FiddlerApplication.Log.LogString('xieboke_net_log: ' + 'test')
```

## 弹个对话框

```javascript
FiddlerObject.alert('弹个对话框')

MessageBox.Show('弹个框')
```

### 修改请求的域名

```javascript
if (oSession.HostnameIs('baidu.com')) {
  oSession.hostname = '=xieboke.net'
}
```

### 发起网络请求

```javascript
if (
  oSession.hostname.Contains('xieboke.net') ||
  oSession.hostname.Contains('zhuoqun.info')
) {
  var key = ''
  var request_body = oSession.GetRequestBodyAsString().replace(/"/g, "'")
  var response_body = oSession.GetResponseBodyAsString().replace(/"/g, "'")
  var content =
    '[' +
    oSession.responseCode +
    '] ' +
    oSession.oRequest.headers +
    '\r\nRequests:\r\n' +
    request_body +
    '\r\nResponse:\r\n' +
    response_body
  //MessageBox.Show(content)
  //var content="test"
  var dingding_hook = 'https://oapi.dingtalk.com/robot/send?access_token=xxx'
  var user_agent =
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
  var body = '{"msgtype": "text","text": {"content": "' + content + '"}}'
  var body_length = body.toString().length

  var method = 'POST'
  var myUrl = dingding_hook
  var url = myUrl
  var protocol = 'HTTP/1.1'
  var raw = ''

  raw += method + ' ' + url + ' ' + protocol + '\r\n'
  raw += 'User-Agent:' + user_agent + '\r\n'
  raw += 'Content-Length:' + body_length + '\r\n'
  raw += 'Content-Type:application/json; charset=utf-8' + '\r\n\r\n'
  raw += body + '\r\n\\r\n'
  //MessageBox.Show(raw)

  try {
    // Make a recursive HTTP request for the next item.
    FiddlerObject.utilIssueRequest(raw)
  } catch (e) {
    MessageBox.Show(e.ToString())
  }
}
```

### 保存到文件

```javascript
//文件保存路径，可自定义
file = fso.OpenTextFile(
  'E:\\zhuoyuebiji\\fiddler_session\\convert.log',
  8,
  true,
  true
)
file.writeLine(
  'Response code: ' +
    oSession.responseCode +
    ' [' +
    curDate.toLocaleString() +
    ']'
)
//file.writeLine("Response body: " + oSession.GetResponseBodyAsString());
//file.writeLine("Test: " + typeof(resultToJson));
file.writeLine('tbkConvertURL:[' + tbkConvertURL + ']')
file.writeLine('\n')
file.close()
```

### 时间格式化

```jsx
var now = new Date()
var ts =
  now.getFullYear() +
  now.getMonth() +
  now.getDate() +
  now.getDay() +
  now.getHours() +
  now.getMinutes() +
  now.getSeconds() +
  now.getMilliseconds()
var timeString =
  now.getFullYear() + now.getMonth() + now.getDate() + now.getDay()
```

### Reference

[fiddlerScript oSession 方法等收集（发送请求、保存到文件）](https://www.jianshu.com/p/47ddbf92d00e)

**2023.01.04**
