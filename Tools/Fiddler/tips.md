<font size=4 face='楷体'>

## Tips

### 使指定 URL 支持 CORS 跨域请求

设置路径 `Rules->Customize Rules`

修改 `OnBeforeResponse` 函数

```java
static function OnBeforeResponse(oSession: Session) {
        ...

        if(oSession.uriContains("要处理的url")){
            oSession.oResponse["Access-Control-Allow-Origin"] = "允许的域名";
            oSession.oResponse["Access-Control-Allow-Credentials"] = true;
        }
    }
```

### 使指定 URL 支持 CORS 跨域请求

设置路径 `Rules->Customize Rules`, 修改 `OnBeforeResponse` 函数

```java
static function OnBeforeResponse(oSession: Session) {
        ...

        if(oSession.uriContains("要处理的url")){
            oSession.oResponse["Access-Control-Allow-Origin"] = "允许的域名";
            oSession.oResponse["Access-Control-Allow-Credentials"] = true;
        }
    }
```

### Fiddler Script 向指定页面中注入 js 或修改页面内容

设置路径 `Rules->Customize Rules`, 修改 `OnBeforeResponse` 函数

- 修改页面内容
  ```java
  static function OnBeforeResponse(oSession: Session) {
      if (m_Hide304s && oSession.responseCode == 304) {
          oSession["ui-hide"] = "true";
      }
      if (oSession.HostnameIs("www.jd.com")||oSession.uriContains('jd.com') && oSession.oResponse.headers.ExistsAndContains("Content-Type","text/html")){
         oSession.utilDecodeResponse();
          oSession.utilReplaceInResponse('</head>','<script>alert(1);</script></head>');
      }
  }
  ```
- 正则替换
  ```java
  // 解码响应内容
  oSession.utilDecodeResponse();
  var oBody = System.Text.Encoding.UTF8.GetString(oSession.responseBodyBytes);
  // 使用正则进行替换
  var oRegEx=/<\/head>/ig;
  oBody = oBody.replace(oRegEx, "<script>alert(1);</script></head>");
  //设置新的响应内容
  oSession.utilSetResponseBody(oBody);
  ```
- json 格式替换
  ```java
  oSession.utilDecodeResponse();
  var str=oSession.GetResponseBodyAsString();
  //替换内容
  str=str.Replace("msg","message");
  // 转成json对象修改内容
  var json=Fiddler.WebFormats.JSON.JsonDecode(str);
  json.JSONObject["code"]="200";
  json.JSONObject["data"]["message"]="200";
  oSession.utilSetResponseBody(Fiddler.WebFormats.JSON.JsonEncode(json.JSONObject));
  ```

### Reference

[Fiddler 设置浏览器跨域访问接口](https://www.jianshu.com/p/2c21fe883280)
[使用 Fiddler Script 向指定页面中注入 js 或修改页面内容,本地文件/目录响应请求(三)](https://www.zhaokeli.com/article/8100.html)

**2021.12.13**
