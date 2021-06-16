<font size=4 face='楷体'>

## ElasticSearch 添加 HTTP 基本认证

ES 默认没有提供任何权限控制，一旦部署在公共网络就容易有数据泄露的风险
elasticsearch-http-basic 就提供了针对 ES HTTP 连接的 IP 白名单、密码权限和信任代理功能

### 安装

elasticsearch-http-basic 还不支持 ES 标准的 `bin/plugin install [github-name]/[repo-name]` 的安装方式, 但作者有提供编译好的 jar 包, 不需要下载源码重新编译

插件的安装步骤如下:

- 从 elasticsearch-http-basic 的发布版下载对应版本的 jar 包
- `mkdir -p plugins/http-basic; mv elasticsearch-http-basic-x.x.x.jar plugins/http-basic`(注意文件夹的名称)
- 重启 ES 进程
- 验证插件是否生效: `curl localhost:9200/_nodes/[your-node-name]/plugins?pretty=true`
  如果看到 plugins 列表包含有`http-basic-server-plugin`就说明插件生效了

### 配置

elasticsearch-http-basic 和其他 ES 插件一样，在`config/elasticsearch.yml`中统一配置:

| 配置名                          | 默认值                     | 说明                                                                          |
| ------------------------------- | -------------------------- | ----------------------------------------------------------------------------- |
| http.basic.enabled              | true                       | 开关，开启会接管全部 HTTP 连接                                                |
| http.basic.user                 | admin                      | 账号                                                                          |
| http.basic.password             | admin_pw                   | 密码                                                                          |
| http.basic.ipwhitelist          | ["localhost", "127.0.0.1"] | 白名单内的 ip 访问不需要通过账号和密码,支持 ip 和主机名，不支持 ip 区间或正则 |
| http.basic.trusted_proxy_chains | []                         | 信任代理列表                                                                  |
| http.basic.log                  | false                      | 把无授权的访问事件添加到 ES 的日志                                            |
| http.basic.xforward             | ""                         | 记载代理路径的 header 字段名                                                  |

### 测试

- shell

```bash
# 无账号密码，不可访问
>>> curl http://[your-node-name]:[your-port]/[your-index]/_count?pretty=true
Authentication Required
# 通过user选项带上账号密码，返回正常数据
>>> curl --user [your-admin]:[your-password] http://[your-node-name]:[your-port]/[your-index]/_count?pretty=true
{
  "count" : xxx,
  "_shards" : {
    "total" : xxx,
    "successful" : xxx,
    "failed" : 0
  }
}
```

- 添加了 HTTP 基本认证后，elasticsearch-head 同样会弹窗要求你先进行权限认证

### Python

ES 官方的 Python 客户端可以通过 `http_auth` 配置账号密码:

```python
from elasticsearch import Elasticsearch
es = Elasticsearch(['localhost'], http_auth=('your-admin', 'your-password'), port=...)
```

## Reference

[为 ElasticSearch 添加 HTTP 基本认证](https://segmentfault.com/a/1190000002803609)

**2021.05.13**
