<font size=4 face='楷体'>

## curl 的使用

- 常用参数
  > -A: 随意指定自己这次访问所宣称的自己的浏览器信息
  > -b/--cookie \<name=string/file\>: cookie 字符串或文件读取位置，使用 option 来把上次的 cookie 信息追加到 http request 里面去。
  > -c/--cookie-jar \<file\>: 操作结束后把 cookie 写入到这个文件中
  > -d/ --data \<data\>: HTTP POST 方式传送
  > -F/--form \<name=content\>: 模拟 http 表单提交数据
  > -H/--header \<header\>: 指定请求头参数
  > -s/--slient: 减少输出的信息，比如进度
  > -v/--verbose: 小写的 v 参数，用于打印更多信息，包括发送的请求信息，这在调试脚本是特别有用。
  > -o/--output \<file\>: 指定输出文件名称
  > --retry \<num\>: 指定重试次数
  > -x/--proxy \<proxyhost\[:port\]\>: 指定代理服务器地址和端口，端口默认为 1080
  > --connect-timeout \<seconds\>: 指定尝试连接的最大时长
  > -i: 输出时附带上返回的 HTTP-header
  > -g: 关掉 URL 的通配附解析。如{}、[]这种
  > -X: 指定请求 method。如 GET\POST\DELETE
- 使用
  \[ \]

  ```shell
  #curl发送get,curl请求本身属于get，也没找到指定发送参数的参数。。
  curl https://www.baidu.com/s?wd=xixi
  #curl 发送 post，curl 发送 post 有两个参数-d 和-F
  跟据 man 的结果，区别在于：
  -d 效果相当与在 HTML form 填好了信息按下了 submit 键，他会使用
  content-type “application/x-www-form-urlencoded”，按照它的使用例子，应该是普通内容 post 过去。
  -F 模拟用户按下 submit 键后传输填好的 form。使用 Content-Type multi‐part/form-data，按照它的例子一般是在传送文件的时候使用。
  curl -d "username=qujun&passwd=xixi" https://www.baidu.com
  curl -F "web=@index.html;type=text/html" example.com
  curl -F profile=@portrait.jpg https://example.com/upload.cgi
  ```

## Reference

[提交 http 请求之 python 与 curl](https://www.cnblogs.com/zhzhang/p/8576033.html)
