<font size=4 face='楷体'>

## go-elasticsearch 介绍及简单使用

### 介绍

go-elasticsearch 时 Elasticsearch 的官方 Go 客户端。

可以直接调用官方准备好的 api。简单易用。

### 兼容性

语言客户端是向前兼容的，这代表这客户端可以和更高或是相等版本的 Elasticsearch 进行通讯。简单来说就是，允许使用 7.X 的 Elasticsearch 的语言客户端何以访问 8.X 的 Elasticsearch。

### 相关文档

如果想要了解详情，建议阅读官方文档。本文只是简单的介绍该包的使用。

[GitHub - elastic/go-elasticsearch：Elasticsearch 的官方 Go 客户端](https://github.com/elastic/go-elasticsearch)

[esapi package - github.com/elastic/go-elasticsearch/esapi - Go Packages](https://pkg.go.dev/github.com/elastic/go-elasticsearch/esapi)

[go-elasticsearch/\_examples at main ·elastic/go-elasticsearch ·GitHub](https://github.com/elastic/go-elasticsearch/tree/main/_examples)

## 使用

### 安装

可以使用 go get

```bash
go get -u github.com/elastic/go-elasticsearch
```

或者添加包到你的 go.mod 文件

```bash
require github.com/elastic/go-elasticsearch v0.0.0
```

再或者是从仓库里克隆

```bash
git clone https://github.com/elastic/go-elasticsearch.git && cd go-elasticsearch
```

### 配置客户端

一个默认配置的客户端，请求并接受响应。

```go
es, _ := elasticsearch.NewDefaultClient()
	res, _ := es.Info()
	defer res.Body.Close()
	log.Println(res)
```

当然客户端也可以根据自己的需要自行配置，如下

```go
// 自定义配置
cfg := elasticsearch.Config{



   // 有多个节点时需要配置
   Addresses: []string{



      "http://localhost:9200",
   },
   // 配置HTTP传输对象
   Transport: &http.Transport{



      //MaxIdleConnsPerHost 如果非零，控制每个主机保持的最大空闲(keep-alive)连接。如果为零，则使用默认配置2。
      MaxIdleConnsPerHost:   10,
      //ResponseHeaderTimeout 如果非零，则指定在写完请求(包括请求体，如果有)后等待服务器响应头的时间。
      ResponseHeaderTimeout: time.Second,
      //DialContext 指定拨号功能，用于创建不加密的TCP连接。如果DialContext为nil(下面已弃用的Dial也为nil)，那么传输拨号使用包网络。
      DialContext:           (&net.Dialer{


     Timeout: time.Second}).DialContext,
      // TLSClientConfig指定TLS.client使用的TLS配置。
      //如果为空，则使用默认配置。
      //如果非nil，默认情况下可能不启用HTTP/2支持。
      TLSClientConfig: &tls.Config{



         MaxVersion:         tls.VersionTLS11,
         //InsecureSkipVerify 控制客户端是否验证服务器的证书链和主机名。
         InsecureSkipVerify: true,
      },
   },
}
es, _ := elasticsearch.NewClient(cfg)
res, _ := es.Info()
defer res.Body.Close()
log.Println(res)
```

### CRUD

#### 新增文档

使用 index api 对文档进行增添或是修改操作。如果 id 不存在为创建文档，如果文档存在则进行修改。

```go
es, _ := elasticsearch.NewDefaultClient()
// 在索引中创建或更新文档。
res, err := es.Index(
   "test",                                  // Index name
   strings.NewReader(`{"title" : "Test"}`),    // Document body
   es.Index.WithDocumentID("1"),               // Document ID
   //es.Index.WithRefresh("true"),               // Refresh
)
if err != nil {



   log.Fatalf("ERROR: %s", err)
}
defer res.Body.Close()

log.Println(res)
```

也可以使用 esapi 进行请求的包装，然后使用 Do()方法执行请求。我们做同上面一样的操作，如下

```go
es, _ := elasticsearch.NewDefaultClient()
req := esapi.IndexRequest{



   Index:      "test",                                  // Index name
   Body:       strings.NewReader(`{"title" : "Test"}`), // Document body
   DocumentID: "1",                                     // Document ID
   Refresh:    "true",                                  // Refresh
}
res, err := req.Do(context.Background(), es)
if err != nil {



   log.Fatalf("Error getting response: %s", err)
}
defer res.Body.Close()

log.Println(res)
```

同

```go
PUT /test/_doc/1
{
  "title": "Test"
}
```

下面都将之使用 esapi 方法实现。

##### 不覆盖的创建文档

如果不想因为在创建文档填写错了 id 而对不想进行操作的文档进行了修改，那么可以使用 CreateRequest 包装请求。

```go
es, _ := elasticsearch.NewDefaultClient()
   req := esapi.CreateRequest{



      Index:        "learn",
      DocumentType: "user",
      DocumentID:   "1",
      Body: strings.NewReader(`
{
   "name": "张三",
   "age": 25,
   "about": "一个热爱刑法的男人，但是不精通唱跳Rap"
}`),
   }
   res, err := req.Do(context.Background(), es)
   if err != nil {



      log.Println("出错了，这个你麻麻滴错误是", err)
   }
   log.Println(res)
```

#### 查询文档

##### 查询单个文档

使用 GetRequest 包装请求。

```go
es, _ := elasticsearch.NewDefaultClient()

req := esapi.GetRequest{



   Index: "learn",
   DocumentType: "user",
   DocumentID: "1",
}
res, err := req.Do(context.Background(), es)
if err != nil {



   log.Fatalf("ERROR: %s", err)
}
defer res.Body.Close()

log.Println(res)
```

同

```go
GET /learn/user/1
```

##### 查询多个文档

使用 MgetRequest 包装请求。

```go
es, _ := elasticsearch.NewDefaultClient()
   request := esapi.MgetRequest{



      Index:        "learn",
      DocumentType: "user",
      Body:         strings.NewReader(`{
  "docs": [
    {
      "_id": "1"
    },
    {
      "_id": "2"
    }
  ]
}`),
   }
   res, err := request.Do(context.Background(), es)
   if err != nil {



      log.Println("出错了，错误是", err)
   }
   log.Println(res)
```

#### 修改文档

在上面我们已经进行了创建或者修改的操作，但是使用 index api 进行的修改操作需要提供所有的字段，不然会返回 400。但我们大多数时候只是进行单个字段或多个字段的修改，并不会修改整个文档，这时候我们可以使用 UpdateRequest 包装请求。

```go
es, _ := elasticsearch.NewDefaultClient()
   req := esapi.UpdateRequest{



      Index:        "learn",
      DocumentType: "user",
      DocumentID:   "1",
      Body: strings.NewReader(`
{
   "doc": {
   "name": "张三"
   }
}`),
   }
   res, err := req.Do(context.Background(), es)
   if err != nil {



      log.Println("出错了，这个你麻麻滴错误是", err)
   }
   log.Println(res)
```

#### 删除文档

使用 DeleteRequest 包装请求。

```go
// 创建一个默认配置的客户端
es, _ := elasticsearch.NewDefaultClient()

// 使用index请求
req := esapi.DeleteRequest{



   Index: "test",
   DocumentType: "_doc",
   DocumentID: "1",
}
res, err := req.Do(context.Background(), es)
if err != nil {



   log.Fatalf("ERROR: %s", err)
}
defer res.Body.Close()

log.Println(res)
```

同

```go
DELETE /test/_doc/1
```

### 批量操作

使用 BulkRequest 包装请求。

```go
es, _ := elasticsearch.NewDefaultClient()

   // 使用index请求
   req := esapi.BulkRequest{



      // 在body中写入bulk请求
      Body: strings.NewReader(`{ "index" : { "_index" : "test", "_id" : "1" } }
{ "title" : "Test2" }
{ "delete" : { "_index" : "test", "_id" : "2" } }
{ "create" : { "_index" : "test", "_id" : "3" } }
{ "field1" : "value3" }
{ "update" : {"_id" : "1", "_index" : "test"} }
{ "doc" : {"field2" : "value2"} }
`),
   }
   res, err := req.Do(context.Background(), es)
   if err != nil {



      log.Fatalf("ERROR: %s", err)
   }
   defer res.Body.Close()

   log.Println(res)
```

注意：格式一定要按照 bulk api 的格式来写，不然会 400，最后别忘了回车

上面请求同

```go
PUT /_bulk
{ "index" : { "_index" : "test", "_id" : "1" } }
{ "title" : "Test2" }
{ "delete" : { "_index" : "test", "_id" : "2" } }
{ "create" : { "_index" : "test", "_id" : "3" } }
{ "field1" : "value3" }
{ "update" : {"_id" : "1", "_index" : "test"} }
{ "doc" : {"field2" : "value2"} }
```

### 搜索

使用 SearchRequest 对请求进行包装。

```go
es, _ := elasticsearch.NewDefaultClient()
   req := esapi.SearchRequest{



      Index:        []string{


     "learn"},
      DocumentType: []string{


     "user"},
      Body:         strings.NewReader(`{
  "query": {
    "match": {
      "about": "唱跳"
    }
  }
}`),
   }
   response, err := req.Do(context.Background(), es)
   if err != nil {



      log.Println("出错了，这个你麻麻滴错误是", err)
   }
   log.Println(response)
```

### Reference

[Go --- go-elasticsearch 介绍及简单使用](https://blog.csdn.net/weixin_52025712/article/details/126253327)

**2023.03.12**
