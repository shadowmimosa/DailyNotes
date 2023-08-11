---
title: JWT身份认证(附带源码讲解)
date: 2023-06-14 15:35:16
copyright: false
author: 阿兵云原生
home: https://www.zhihu.com/people/qing-bing-70
origin: zhihu
url: https://zhuanlan.zhihu.com/p/361420808
tag: 
categories: 
description: JWT（Json Web Token）验证(附带源码讲解)一天，正是午休时段兵长路过胖sir座位，大...
---
**JWT（Json Web Token）验证(附带源码讲解)**
  
一天，正是午休时段
  
兵长路过胖sir座位，大吃一惊，今天胖sir居然没有打呼噜，而是在低着头聚精会神盯着一本书
  
兵长凑近一看，胖sir居然在看史书…
  
兵长：（轻声道），你在看 什 么 ~~
  
胖sir：我在想我要是穿越到清朝，我会是啥身份？
  
what？？~~~ ， 能是啥身份，肯定是重量级人物呗
  
胖sir： 我呸， 今天我倒要给你讲讲啥叫身份
  
讲到身份，不得不说一下cookie、session、Token的区别，come on
  

## **1 cookie、session、Token的区别**

### **Cookie**
Cookie总是保存在客户端中，按在客户端中的存储位置，可分为 `内存Cookie` 和 `硬盘Cookie`。
  
内存Cookie由浏览器维护，保存在内存中，浏览器关闭后就消失了，其存在时间是短暂的。
  
硬盘Cookie保存在硬盘⾥，有⼀个过期时间，除⾮⽤户⼿⼯清理或到了过期时间，硬盘Cookie不会被删除，其存在时间 是⻓期的。
  
所以，按存在时间，可分为 `⾮持久Cookie`和`持久Cookie`。
  
**那么cookies到底是什么呢？**
  
cookie 是⼀个⾮常具体的东⻄，指的就是浏览器⾥⾯能永久存储的⼀种数据，仅仅是浏览器实现的⼀种数
  
据存储功能。
  
cookie由服务器⽣成，发送给浏览器 ，浏览器把cookie以key-value形式保存到某个⽬录下的⽂本⽂件
  
内，下⼀次请求同⼀⽹站时会把该cookie发送给服务器。由于cookie是存在客户端上的，所以浏览器加⼊
  
了⼀些限制确保cookie不会被恶意使⽤，同时不会占据太多磁盘空间，所以每个域的cookie数量是有限的。
  

### **Session**
Session字⾯意思是会话，主要⽤来标识⾃⼰的身份。
  
⽐如在⽆状态的api服务在多次请求数据库时，如何 知道是同⼀个⽤户，这个就可以通过session的机制，服务器要知道当前发请求给⾃⼰的是谁，为了区分客户端请求， 服务端会给具体的客户端⽣成身份标识session ，然后客户端每次向服务器发请求 的时候，都带上这个“身份标识”，服务器就知道这个请求来⾃于谁了。
  
⾄于客户端如何保存该标识，可以有很多⽅式，对于浏览器⽽⾔，⼀般都是使⽤ cookie 的⽅式 ，服务器使⽤session把⽤户信息临时保存了服务器上，⽤户离开⽹站就会销毁，这种凭证存储⽅式相对于 ，cookie来说更加安全。
  
但是session会有⼀个缺陷: 如果web服务器做了负载均衡，那么下⼀个操作请求到 了另⼀台服务器的时候session会丢失。
  
因此，通常企业⾥会使⽤ redis,memcached 缓存中间件来实现session的共享，此时web服务器就是⼀ 个完全⽆状态的存在，所有的⽤户凭证可以通过共享session的⽅式存取，当前session的过期和销毁机制 需要⽤户做控制。
  

### **Token**
token的意思是“令牌”，是⽤户身份的验证⽅式，最简单的token组成: uid(⽤户唯⼀标识) + time(当前 时间戳) + sign(签名,由token的前⼏位+盐以哈希算法压缩成⼀定⻓度的⼗六进制字符串) ，同时还可 以将不变的参数也放进token
  
这里说的token只的是 JWT（Json Web Token）
  

## **2 JWT是个啥？**
⼀般⽽⾔，⽤户注册登陆后会⽣成⼀个jwt token返回给浏览器，浏览器向服务端请求数据时携带 token ，服务器端使⽤ signature 中定义的⽅式进⾏解码，进⽽对token进⾏解析和验证。
  

### **jwt token 的组成部分**
![](./JWT身份认证(附带源码讲解)/e3d588c1f4aad124808630629f0ba9ba.jpg)
  

* header: ⽤来指定使⽤的算法(HMAC SHA256 RSA)和token类型(如JWT)  
  官网上可以找到各种语言的jwt库，例如我们下面使用这个库进行编码，因为这个库使用的人是最多的，值得信赖  
  1go get [http://github.com/dgrijalva/jwt-go](https://link.zhihu.com/?target=http%3A//github.com/dgrijalva/jwt-go)
![](./JWT身份认证(附带源码讲解)/94c3e5b97e7f3d331e23ecba54955f2b)
  
  

* payload: 包含声明(要求)，声明通常是⽤户信息或其他数据的声明，⽐如⽤户id，名称，邮箱等. 声明。可分为三种: registered,public,private
* signature: ⽤来保证JWT的真实性，可以使⽤不同的算法

### **header**
token的第一部分，如
  

```text
1{
2  "alg": "HS256",
3  "typ": "JWT"
4}
```
对上⾯的json进⾏base64编码即可得到JWT的第⼀个部分
  
payload
  
token第二部分如
  

* registered claims: 预定义的声明，通常会放置⼀些预定义字段，⽐如过期时间，主题等(iss:issuer,exp:expiration time,sub:subject,aud:audience)
* public claims: 可以设置公开定义的字段
* private claims: ⽤于统⼀使⽤他们的各⽅之间的共享信息
不要在header和payload中放置敏感信息，除⾮信息本身已经做过脱敏处理，因为payload部分的具体数据是可以通过token来获取到的
  

```text
1{
2  "sub": "1234567890",
3  "name": "John Doe",
4  "admin": true
5}
```

### **Signature**
token的第三部分
  
为了得到签名部分，必须有编码过的header和payload，以及⼀个秘钥，签名算法使⽤header中指定的那 个，然后对其进⾏签名即可
  
**HMACSHA256(base64UrlEncode(header)+"."+base64UrlEncode(payload),secret)**
  
签名是 ⽤于验证消息在传递过程中有没有被更改 ，并且，对于使⽤私钥签名的token，它还可以验证JWT
  
的发送⽅是否为它所称的发送⽅。
  
![](./JWT身份认证(附带源码讲解)/894cba30ed811781732b3bed898b8f86.jpg)
  

### **签名的⽬的**
最后⼀步签名的过程，实际上是对头部以及载荷内容进⾏签名。
  
⼀般⽽⾔，加密算法对于不同的输⼊ 产⽣的输出总是不⼀样的。对于两个不同的输⼊，产⽣同样的输出的概率极其地⼩。所以，我们就把“不⼀样的输⼊产⽣不⼀样的输出”当做必然事件来看待。
  
所以，如果有⼈对头部以及载荷的内容解码之后进⾏修改，再进⾏编码的话，那么新的头部和载荷的 签名和之前的签名就将是不⼀样的。⽽且，如果不知道服务器加密的时候⽤的密钥的话，得出来的签名也 ⼀定会是不⼀样的。
  
![](./JWT身份认证(附带源码讲解)/c0bffcd5f075bf674ef471edf96cc230.jpg)
  
服务器应⽤在接受到JWT后，会⾸先对头部和载荷的内容⽤同⼀算法再次签名。那么服务器应⽤是怎 么知道我们⽤的是哪⼀种算法呢？
  
**在JWT的头部中已经⽤alg字段指明了我们的加密算法了**。
  
如果服务器应⽤对头部和载荷再次以同样⽅法签名之后发现，⾃⼰计算出来的签名和接受到的签名不 ⼀样，那么就说明这个Token的内容被别⼈动过的，我们应该拒绝这个Token，
  
**注意**：在JWT中，不应该在载荷⾥⾯加⼊任何敏感的数据，⽐如⽤户的密码。具体原因上文已经给过答案了
  

### **[http://jwt.io](https://link.zhihu.com/?target=http%3A//jwt.io)⽹站**
在[http://jwt.io](https://link.zhihu.com/?target=http%3A//jwt.io)(`https://jwt.io/#debugger-io`)⽹站中，提供了⼀些JWT token的编码，验证以及⽣成jwt的⼯具。
  
下图就是⼀个典型的jwt-token的组成部分。
  
![](./JWT身份认证(附带源码讲解)/8f371cbe2dd2b6b6ad7915ac113a30c3.jpg)
  

### **啥时候使用JWT呢？**
我们要明白的时候，JWT是用作认证的，而不是用来做授权的。明白他的功能，那么对应JWT的应用场景就不言而喻了
  

* Authorization(授权): 典型场景，⽤户请求的token中包含了该令牌允许的路由，服务和资源。单点登录其实就是现在⼴泛使⽤JWT的⼀个特性
* Information Exchange(信息交换): 对于安全的在各⽅之间传输信息⽽⾔，JSON Web Tokens⽆疑 是⼀种很好的⽅式.因为JWTs可以被签名  
  例如，⽤公钥/私钥对，你可以确定发送⼈就是它们所说的 那个⼈。另外，由于签名是使⽤头和有效负载计算的，您还可以验证内容没有被篡改

### **JWT工作方式是怎样的？**
![](./JWT身份认证(附带源码讲解)/0bbe9dd6bd2dffcebed8570e51825a7f.jpg)
  
JWT认证过程基本上整个过程分为两个阶段
  

* 第⼀个阶段，客户端向服务端获取token
* 第⼆阶段，客户端带着该token去请求相关的资源
通常⽐较重要的是，服务端如何根据指定的规则进⾏token的⽣成。
  
在认证的时候，当⽤户⽤他们的凭证成功登录以后，⼀个JSON Web Token将会被返回。 此后，token就是⽤户凭证了，你必须⾮常⼩⼼以防⽌出现安全问题。 ⼀般⽽⾔，你保存令牌的时间不应该超过你所需要它的时间。
  
⽆论何时⽤户想要访问受保护的路由或者资源的时候，⽤户代理（通常是浏览器）都应该带上JWT，典型 的，通常放在Authorization header中，⽤Bearer schema: Authorization: Bearer 服务器上的受保护的路由将会检查Authorization header中的JWT是否有效，如果有效，则⽤户可以访问 受保护的资源。
  
如果JWT包含⾜够多的必需的数据，那么就可以减少对某些操作的数据库查询的需要，尽管可能并不总是如此。 如果token是在授权头（Authorization header）中发送的，那么跨源资源共享(CORS)将不会成为问题，因为它不使⽤cookie。
  
来感受一张官方的图
  
![](./JWT身份认证(附带源码讲解)/f8dd4e42d22092fc8c5a6617cd0327b4.jpg)
  
获取JWT以及访问APIs以及资源
  

* 客户端向授权接⼝请求授权
* 服务端授权后返回⼀个access token给客户端
* 客户端使⽤access token访问受保护的资源

## **3 基于Token的身份认证和基于服务器的身份认证**

### **1、给予服务器的身份认证，通常是基于服务器上的session来做用户认证，使用session会有如下几个问题**

* Sessions：认证通过后需要将⽤户的session数据保存在内存中，随着认证⽤户的增加，内存开销会⼤
* 扩展性问题： 由于session存储在内存中，扩展性会受限，虽然后期可以使⽤redis,memcached来缓存数据
* CORS: 当多个终端访问同⼀份数据时，可能会遇到禁⽌请求的问题
* CSRF: ⽤户容易受到CSRF攻击（Cross Site Request Forgery, 跨站域请求伪造）

### **2、基于Token的身份认证证是⽆状态的，服务器或者session中不会存储任何⽤户信息.(很好的解决了共享 session的问题)**

* ⽤户携带⽤户名和密码请求获取token(接⼝数据中可使⽤appId,appKey，或是自己协商好的某类数据)
* 服务端校验⽤户凭证，并返回⽤户或客户端⼀个Token
* 客户端存储token,并在请求头中携带Token
* 服务端校验token并返回相应数据
需要注意几点：
  

* 客户端请求服务器的时候，必须将token放到header中
* 客户端请求服务器每一次都需要带上token
* 服务器需要设置 为接收所有域的请求: `Access-Control-Allow-Origin: *`
3、Session和JWT Token的有啥不一样的？
  

* 他俩都可以存储用户相关的信息
* session 存储在服务器， JWT存储在客户端
![](./JWT身份认证(附带源码讲解)/2cef140862f2574b5f19a9ba85211306.jpg)
  

## **4 ⽤Token有什么好处呢？**

* 他是`无状态`的 且 `可扩展性好`
* 他相对安全：防⽌CSRF攻击，token过期重新认证
上文有说说，JWT是用于做身份认证的而不是做授权的，那么在这里列举一下 做认证和做授权分别用在哪里呢？
  

* 例如`OAuth2`是⼀种授权框架，是用于授权，主要用在 使⽤第三⽅账号登录的情况 (⽐如使⽤weibo, qq, github登录某个app)
* JWT是⼀种认证协议 ，⽤在 前后端分离 , 需要简单的对后台API进⾏保护时使⽤
* 无论是授权还是认证，都需要记住使用HTTPS来保护数据的安全性

## **5 实际看看JWT如何做身份验证**

* jwt做身份验证，这里主要讲如何根据header，payload，signature生成token
* 客户端带着token来服务器做请求，如何校验？
下面实例代码，主要做了2个接口
  
**用到的技术点：**
  

* gin
* 路由分组
* 中间件的使用
* gorm
* 简单操作mysql数据库，插入，查询
* jwt
* 生成token
* 解析token

### **登录接口**
访问url ： [http://127.0.0.1:9999/v1/login](https://link.zhihu.com/?target=http%3A//127.0.0.1%3A9999/v1/login)
  
功能：
  

* 用户登录
* 生成jwt，并返回给到客户端
* gorm对数据库的操作

### **认证后Hello接口**
访问url ： [http://127.0.0.1:9999/v1/auth/hello](https://link.zhihu.com/?target=http%3A//127.0.0.1%3A9999/v1/auth/hello)
  
功能：
  

* 校验 客户端请求服务器携带token
* 返回客户端所请求的数据

### **代码结构如下图**
![](./JWT身份认证(附带源码讲解)/8795efe850ab11258a808c382563cfba)
  
main.go
  

```text
 1package main
 2
 3import (
 4   "github.com/gin-gonic/gin"
 5   "my/controller"
 6   "my/myauth"
 7)
 8
 9func main() {
10   //连接数据库
11   conErr := controller.InitMySQLCon()
12   if conErr != nil {
13      panic(conErr)
14   }
15
16   //需要使用到gorm，因此需要先做一个初始化
17   controller.InitModel()
18   defer controller.DB.Close()
19
20
21   route := gin.Default()
22
23   //路由分组
24   v1 := route.Group("/v1/")
25   {
26      //登录（为了方便，将注册和登录功能写在了一起）
27      v1.POST("/login", controller.Login)
28   }
29
30
31   v2 := route.Group("/v1/auth/")
32   //一个身份验证的中间件
33   v2.Use(myauth.JWTAuth())
34   {
35      //带着token请求服务器
36      v2.POST("/hello", controller.Hello)
37   }
38
39   //监听9999端口
40   route.Run(":9999")
41
42}
```
controller.go
  
文件中基本的数据结构定义为：
  
![](./JWT身份认证(附带源码讲解)/73c2f5b069b25a4d43a659665055341d.jpg)
  
文件中涉及的处理函数：
  
![](./JWT身份认证(附带源码讲解)/3dce49d98f9cf9b846e382171b28258b.jpg)
  
实际源码：
  

```text
  1package controller
  2
  3import (
  4   "errors"
  5   "fmt"
  6   jwtgo "github.com/dgrijalva/jwt-go"
  7   "github.com/gin-gonic/gin"
  8   "github.com/jinzhu/gorm"
  9   "log"
 10   "net/http"
 11   "time"
 12   _ "github.com/jinzhu/gorm/dialects/mysql"
 13)
 14
 15//登录请求信息
 16type ReqInfo struct {
 17   Name   string `json:"name"`
 18   Passwd string `json:"passwd"`
 19}
 20
 21// 构造用户表
 22type MyInfo struct {
 23   Id        int32  `gorm:"AUTO_INCREMENT"`
 24   Name      string `json:"name"`
 25   Passwd    string `json:"passwd"`
 26   CreatedAt *time.Time
 27   UpdateTAt *time.Time
 28}
 29
 30//Myclaims
 31// 定义载荷
 32type Myclaims struct {
 33   Name string `json:"userName"`
 34   // StandardClaims结构体实现了Claims接口(Valid()函数)
 35   jwtgo.StandardClaims
 36}
 37//密钥
 38type JWT struct {
 39   SigningKey []byte
 40}
 41//hello 接口
 42func Hello(c *gin.Context) {
 43   claims, _ := c.MustGet("claims").(*Myclaims)
 44   if claims != nil {
 45      c.JSON(http.StatusOK, gin.H{
 46         "status": 0,
 47         "msg":    "Hello wrold",
 48         "data":   claims,
 49      })
 50   }
 51}
 52
 53var (
 54   DB               *gorm.DB
 55   secret                 = "iamsecret"
 56   TokenExpired     error = errors.New("Token is expired")
 57   TokenNotValidYet error = errors.New("Token not active yet")
 58   TokenMalformed   error = errors.New("That's not even a token")
 59   TokenInvalid     error = errors.New("Couldn't handle this token:")
 60)
 61//数据库连接
 62func InitMySQLCon() (err error) {
 63   // 可以在api包里设置成init函数
 64   connStr := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?charset=utf8mb4&parseTime=True&loc=Local", "root", "123456", "127.0.0.1", 3306, "mygorm")
 65   fmt.Println(connStr)
 66   DB, err = gorm.Open("mysql", connStr)
 67
 68   if err != nil {
 69      return err
 70   }
 71
 72   return DB.DB().Ping()
 73}
 74//初始化gorm对象映射
 75func InitModel() {
 76   DB.AutoMigrate(&MyInfo{})
 77}
 78func NewJWT() *JWT {
 79   return &JWT{
 80      []byte(secret),
 81   }
 82}
 83// 登陆结果
 84type LoginResult struct {
 85   Token string `json:"token"`
 86   Name string `json:"name"`
 87}
 88// 创建Token(基于用户的基本信息claims)
 89// 使用HS256算法进行token生成
 90// 使用用户基本信息claims以及签名key(signkey)生成token
 91func (j *JWT) CreateToken(claims Myclaims) (string, error) {
 92   // 返回一个token的结构体指针
 93   token := jwtgo.NewWithClaims(jwtgo.SigningMethodHS256, claims)
 94   return token.SignedString(j.SigningKey)
 95}
 96//生成token
 97func generateToken(c *gin.Context, info ReqInfo) {
 98   // 构造SignKey: 签名和解签名需要使用一个值
 99   j := NewJWT()
100
101   // 构造用户claims信息(负荷)
102   claims := Myclaims{
103      info.Name,
104      jwtgo.StandardClaims{
105         NotBefore: int64(time.Now().Unix() - 1000), // 签名生效时间
106         ExpiresAt: int64(time.Now().Unix() + 3600), // 签名过期时间
107         Issuer:    "pangsir",                       // 签名颁发者
108      },
109   }
110
111   // 根据claims生成token对象
112   token, err := j.CreateToken(claims)
113   if err != nil {
114      c.JSON(http.StatusOK, gin.H{
115         "status": -1,
116         "msg":    err.Error(),
117         "data":   nil,
118      })
119   }
120
121   log.Println(token)
122   // 返回用户相关数据
123   data := LoginResult{
124      Name:  info.Name,
125      Token: token,
126   }
127
128   c.JSON(http.StatusOK, gin.H{
129      "status": 0,
130      "msg":    "登陆成功",
131      "data":   data,
132   })
133
134   return
135}
136//解析token
137func (j *JWT) ParserToken(tokenstr string) (*Myclaims, error) {
138   // 输入token
139   // 输出自定义函数来解析token字符串为jwt的Token结构体指针
140   // Keyfunc是匿名函数类型: type Keyfunc func(*Token) (interface{}, error)
141   // func ParseWithClaims(tokenString string, claims Claims, keyFunc Keyfunc) (*Token, error) {}
142   token, err := jwtgo.ParseWithClaims(tokenstr, &Myclaims{}, func(token *jwtgo.Token) (interface{}, error) {
143      return j.SigningKey, nil
144   })
145
146   fmt.Println(token, err)
147   if err != nil {
148      // jwt.ValidationError 是一个无效token的错误结构
149      if ve, ok := err.(*jwtgo.ValidationError); ok {
150         // ValidationErrorMalformed是一个uint常量，表示token不可用
151         if ve.Errors&jwtgo.ValidationErrorMalformed != 0 {
152            return nil, TokenMalformed
153            // ValidationErrorExpired表示Token过期
154         } else if ve.Errors&jwtgo.ValidationErrorExpired != 0 {
155            return nil, TokenExpired
156            // ValidationErrorNotValidYet表示无效token
157         } else if ve.Errors&jwtgo.ValidationErrorNotValidYet != 0 {
158            return nil, TokenNotValidYet
159         } else {
160            return nil, TokenInvalid
161         }
162
163      }
164   }
165
166   // 将token中的claims信息解析出来和用户原始数据进行校验
167   // 做以下类型断言，将token.Claims转换成具体用户自定义的Claims结构体
168   if claims, ok := token.Claims.(*Myclaims); ok && token.Valid {
169      return claims, nil
170   }
171
172   return nil, errors.New("token NotValid")
173}
174//登录
175func Login(c *gin.Context) {
176   var reqinfo ReqInfo
177   var userInfo MyInfo
178
179   err := c.BindJSON(&reqinfo)
180
181   if err == nil {
182      fmt.Println(reqinfo)
183
184      if reqinfo.Name == "" || reqinfo.Passwd == ""{
185         c.JSON(http.StatusOK, gin.H{
186            "status": -1,
187            "msg":    "账号密码不能为空",
188            "data":   nil,
189         })
190         c.Abort()
191         return
192      }
193      //校验数据库中是否有该用户
194      err := DB.Where("name = ?", reqinfo.Name).Find(&userInfo)
195      if err != nil {
196         fmt.Println("数据库中没有该用户 ，可以进行添加用户数据")
197         //添加用户到数据库中
198         info := MyInfo{
199            Name:   reqinfo.Name,
200            Passwd: reqinfo.Passwd,
201         }
202         dberr := DB.Model(&MyInfo{}).Create(&info).Error
203         if dberr != nil {
204            c.JSON(http.StatusOK, gin.H{
205               "status": -1,
206               "msg":    "登录失败，数据库操作错误",
207               "data":   nil,
208            })
209            c.Abort()
210            return
211         }
212      }else{
213         if userInfo.Name != reqinfo.Name || userInfo.Passwd != reqinfo.Passwd{
214            c.JSON(http.StatusOK, gin.H{
215               "status": -1,
216               "msg":    "账号密码错误",
217               "data":   nil,
218            })
219            c.Abort()
220            return
221         }
222      }
223      //创建token
224      generateToken(c, reqinfo)
225   } else {
226      c.JSON(http.StatusOK, gin.H{
227         "status": -1,
228         "msg":    "登录失败，数据请求错误",
229         "data":   nil,
230      })
231   }
232}
```
myauth.go
  

```text
 1package myauth
 2
 3import (
 4   "fmt"
 5   "github.com/gin-gonic/gin"
 6   "my/controller"
 7   "net/http"
 8)
 9
10//身份认证
11func JWTAuth() gin.HandlerFunc {
12   return func(c *gin.Context) {
13      //拿到token
14      token := c.Request.Header.Get("token")
15      if token == "" {
16         c.JSON(http.StatusOK, gin.H{
17            "status": -1,
18            "msg":    "token为空，请携带token",
19            "data":   nil,
20         })
21         c.Abort()
22         return
23      }
24
25      fmt.Println("token = ", token)
26
27      //解析出实际的载荷
28      j := controller.NewJWT()
29
30      claims, err := j.ParserToken(token)
31      if err != nil {
32         // token过期
33         if err == controller.TokenExpired {
34            c.JSON(http.StatusOK, gin.H{
35               "status": -1,
36               "msg":    "token授权已过期，请重新申请授权",
37               "data":   nil,
38            })
39            c.Abort()
40            return
41         }
42         // 其他错误
43         c.JSON(http.StatusOK, gin.H{
44            "status": -1,
45            "msg":    err.Error(),
46            "data":   nil,
47         })
48         c.Abort()
49         return
50      }
51
52      // 解析到具体的claims相关信息
53      c.Set("claims", claims)
54   }
55}
```
myauth.go
  

```text
 1package myauth
 2
 3import (
 4   "fmt"
 5   "github.com/gin-gonic/gin"
 6   "my/controller"
 7   "net/http"
 8)
 9
10//身份认证
11func JWTAuth() gin.HandlerFunc {
12   return func(c *gin.Context) {
13      //拿到token
14      token := c.Request.Header.Get("token")
15      if token == "" {
16         c.JSON(http.StatusOK, gin.H{
17            "status": -1,
18            "msg":    "token为空，请携带token",
19            "data":   nil,
20         })
21         c.Abort()
22         return
23      }
24
25      fmt.Println("token = ", token)
26
27      //解析出实际的载荷
28      j := controller.NewJWT()
29
30      claims, err := j.ParserToken(token)
31      if err != nil {
32         // token过期
33         if err == controller.TokenExpired {
34            c.JSON(http.StatusOK, gin.H{
35               "status": -1,
36               "msg":    "token授权已过期，请重新申请授权",
37               "data":   nil,
38            })
39            c.Abort()
40            return
41         }
42         // 其他错误
43         c.JSON(http.StatusOK, gin.H{
44            "status": -1,
45            "msg":    err.Error(),
46            "data":   nil,
47         })
48         c.Abort()
49         return
50      }
51
52      // 解析到具体的claims相关信息
53      c.Set("claims", claims)
54   }
55}
```

## **6 jwt是如何将header,paylaod,signature组装在一起的？**

### **1> 我们从创建token的函数开始看起**
![](./JWT身份认证(附带源码讲解)/0f8af6f90b1828ab6c09860e22c69033.jpg)
  
CreateToken用JWT对象绑定，对象中包含密钥，函数的参数是载荷
  

### **2> NewWithClaims 函数参数是加密算法，载荷**
NewWithClaims的具体作用是是初始化一个Token对象
  
![](./JWT身份认证(附带源码讲解)/87f7e9be3057d35d22b5c98cbe88054e.jpg)
  
![](./JWT身份认证(附带源码讲解)/46b9ea3e16606bc43e951488d4bd03e3.jpg)
  

### **3> SignedString函数，参数为密钥**
主要是得到一个完整的token
  
SigningString 将header 与 载荷 处理后拼接在一起
  
Sign 将密钥计算一个hash值，与header，载荷拼接在一起，进而制作成token
  
此处的Sign 方法具体是调用哪一个实现，请继续往下看
  
![](./JWT身份认证(附带源码讲解)/44b4666d58f2eb70c2706543852f5bf0.jpg)
  

### **4> SigningString**
将header通过json序列化之后使用base64加密
  
同样的也将载荷通过json序列化之后使用base64加密
  
将这俩加密后的字符串拼接在一起
  
![](./JWT身份认证(附带源码讲解)/6053d43a383738cf7fea55e161979d7a.jpg)
  
![](./JWT身份认证(附带源码讲解)/1204cb23def0619bcc6d706d5f22cd67.jpg)
  
5> 回到创建token函数的位置
  

```text
1func (j *JWT) CreateToken(claims Myclaims) (string, error) {
2   // 返回一个token的结构体指针
3   token := jwtgo.NewWithClaims(jwtgo.SigningMethodHS256, claims)
4   return token.SignedString(j.SigningKey)
5}
```
SigningMethodHS256 对应这一个结构`SigningMethodHMAC`，如下
  
![](./JWT身份认证(附带源码讲解)/1c9a3fe4d050e16aad41bbbd6ad832dd.jpg)
  
看到这里，便解开了上述第4点 Sign方法具体在哪里实现的问题
  
![](./JWT身份认证(附带源码讲解)/3ad3f9a22ce13f8a1e381c8e014745b2.jpg)
  

## **7> 效果查看**

### **登录&注册接口**
![](./JWT身份认证(附带源码讲解)/d1ec7279473c3c31014cf8ca9145ab9f.jpg)
  
数据库展示（若对编码中的gorm有疑问，可以看小魔童哪吒的上一期gorm的整理）
  
![](./JWT身份认证(附带源码讲解)/7892c375eb89da257d37b329805ef0ab.jpg)
  

### **Hello接口**
![](./JWT身份认证(附带源码讲解)/5f31232850dc2d4337294bd22299c03b.jpg)
  
以上为本期全部内容，如有疑问可以在评论区或后台提出你的疑问，我们一起交流，一起成长。
  
好家伙要是文章对你还有点作用的话，请帮忙点个关注，分享到你的朋友圈，分享技术，分享快乐
  
技术是开放的，我们的心态，更应是开放的。拥抱变化，向阳而生，努力向前行。
  
作者：小魔童哪吒

> 当前文档由 [markdown文档下载插件](https://github.com/kscript/markdown-download) 下载, 原文链接: [JWT身份认证(附带源码讲解)](https://zhuanlan.zhihu.com/p/361420808)  