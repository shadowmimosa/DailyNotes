<font size=4 face='楷体'>

## 部署 logstash

### 常用参数


### 创建目录

```bash
mkdir -p /home/data/logstash/config
mkdir -p /home/data/logstash/pipeline
mkdir -p /home/data/logstash/data
mkdir -p /home/data/logstash/pipeline/mappings
```

### 配置文件

- logstash 配置

  ```yaml
  # /home/data/logstash/config/logstash.yml

  http.host: '0.0.0.0'
  xpack.monitoring.elasticsearch.username: 'logstash'
  xpack.monitoring.elasticsearch.password: '密码'
  xpack.monitoring.elasticsearch.hosts: ['http://es-ip:9200']
  ```

- pipeline 配置

  ```conf
  # /home/data/logstash/pipeline/logstash.conf
  input {
    tcp {
      mode => "server"
      host => "0.0.0.0"  # 允许任意主机发送日志
      port => 5044 # logstash暴露的端口
      codec => json_lines    # 数据格式
    }
  }

  filter {
      ruby {
          # 将时间转成毫秒的时间戳
          code => "event.set('createTime',(event.get('@timestamp').to_f.round(3)*1000).to_i)"
      }
      ruby {
          # 设置一个自定义字段'timestamp'[这个字段可自定义]，将logstash自动生成的时间戳中的值加8小时，赋给这个字段
      code => "
            event.set('timestamp', event.get('@timestamp').time.localtime + 8*3600)
            event.set('threadName', event.get('thread_name'))
            event.set('levelValue', event.get('level_value'))
            event.set('loggerName', event.get('logger_name'))
            event.set('callerClassName', event.get('caller_class_name'))
            event.set('callerFileName', event.get('caller_file_name'))
            event.set('callerLineNumber', event.get('caller_line_number'))
            event.set('callerMethodName', event.get('caller_method_name'))
            event.set('stackTrace', event.get('stack_trace'))
          "
      }
      ruby {
          # 将自定义时间字段中的值重新赋给@timestamp
          # code => "event.set('@timestamp',event.get('timestamp'))"
      }
      mutate {
          # 删除自定义字段
          remove_field => ["timestamp","thread_name","level_value","logger_name","HOSTNAME","caller_class_name","caller_file_name","caller_line_number","caller_method_name","stack_trace"]
      }
  }

  output {
    elasticsearch {
        hosts  => ["http://es-ip:9200"]   # ElasticSearch 的地址和端口
        user   => "elastic"
        password => "es密码"
        index  => "application-logs-%{[appName]}-%{[springProfile]}-%{+YYY-MM}"         # 指定索引名
        # document_type => "_doc"
        codec  => json
        # 是否使用模板创建索引，在模板中可提前定义索引的字段类型
        manage_template => true
        # 索引模板文件
        template => "/usr/share/logstash/pipeline/mappings/application-log-mapping.json"
        template_name => "application-log"
        # 在logstash重启后，是否使用模板文件覆盖es中已存在的索引模板
        template_overwrite => true
    }
    #stdout {
    #  codec => rubydebug
    #}
    file {
      path => "/usr/share/logstash/pipeline/logs/%{+YYYY-MM-dd}-%{appName}-%{springProfile}.log"
    }
  }
  ```

- mapping 配置
  ```json
  # /home/data/logstash/pipeline/mappings/application-log-mapping.json
  # 7.X后的es，type 不是再是 string 而是 type="keyword" 或 type="text"
  {
    "index_patterns": ["application-log*"],
    "order": 1,
    "mappings" : {
      "dynamic_templates" : [{
        "message_field" : {
          "match" : "message",
          "match_mapping_type" : "string",
          "mapping" : {
            "type" : "keyword",
            "index" : true
          }
        }
      }, {
        "string_fields" : {
          "match" : "*",
          "match_mapping_type" : "string",
          "mapping" : {
            "type" : "keyword",
            "index" : true
          }
        }
      }],
      "properties" : {
        "@timestamp": { "type": "date" },
        "@version": { "type": "keyword", "index": true },
        "message": {
          "type": "text",
          "analyzer": "ik_max_word"
        }
      }
    }
  }
  ```

### 运行

```bash
docker run -d --name logstash --net elk-network \
  --privileged=true \
  -p 5044:5044 \
  -v /home/data/logstash/data/:/usr/share/logstash/data \
  -v /home/data/logstash/config/logstash.yml:/usr/share/logstash/config/logstash.yml \
  -v /home/data/logstash/pipeline/:/usr/share/logstash/pipeline \
  logstash:7.17.18
```

## 连接到带有 HTTPS 访问的集群

### 使用证书&密码连接

```conf
# logstash.conf
input {
  generator {
    message => "liuxg"
    count => 1
  }
}

output {
	stdout {
		codec => rubydebug
	}

    elasticsearch {
      ; Elasticsearch 集群的终端地址
    	hosts => ["https://localhost:9200"]
      ; Elasticsearch 中创建的索引的名称
    	index => "data-%{+YYYY.MM.dd}"
      ;  Elasticsearch 中创建的用户
      ; 这里使用的是超级用户 elastic
    	user => "elastic"
      ; 上面的 user 用户对应的密码
    	password => "ndktp2Xr2h_*Q6EZfq4t"
    ; 当为 true 时，启动 SSL 检验
		ssl_certificate_verification => true
    ; Elasticsearch 的证书所在的地址
		truststore => "/Users/liuxg/elastic/elasticsearch-8.4.1/config/certs/http.p12"
    ; truststore 的密码
		truststore_password => "buSYG3l-R0mdN6pggG76VA"
  	}
}
```

获取证书密码

```bash
$ pwd
/Users/liuxg/elastic/elasticsearch-8.4.1
$ ./bin/elasticsearch-keystore list
keystore.seed
xpack.security.http.ssl.keystore.secure_password
xpack.security.transport.ssl.keystore.secure_password
xpack.security.transport.ssl.truststore.secure_password
$ ./bin/elasticsearch-keystore show xpack.security.http.ssl.keystore.secure_password
buSYG3l-R0mdN6pggG76VA
```

在 Logstash 的安装目录下使用如下的方式来进行运行

```bash
./bin/logstash -f logstash.conf
```

查看这个证书

```bash
$ pwd
/Users/liuxg/elastic/elasticsearch-8.4.1
$ ./bin/elasticsearch-keystore list
keystore.seed
xpack.security.http.ssl.keystore.secure_password
xpack.security.transport.ssl.keystore.secure_password
xpack.security.transport.ssl.truststore.secure_password
$ ./bin/elasticsearch-keystore show xpack.security.http.ssl.keystore.secure_password
Jn1YI7FMSNaiAXjUsdp4Mw
$ cd config/certs/
$ keytool -keystore http.p12 -list
Enter keystore password:
Keystore type: PKCS12
Keystore provider: SUN

Your keystore contains 2 entries

http, Sep 26, 2022, PrivateKeyEntry,
Certificate fingerprint (SHA-256): 97:D0:50:B0:31:73:42:67:D1:00:7C:71:F2:4D:D4:9E:AC:73:99:39:AC:E8:34:EB:DA:2F:0B:5E:F6:65:D3:CD
http_ca, Sep 26, 2022, PrivateKeyEntry,
Certificate fingerprint (SHA-256): B4:8C:3E:33:FE:E5:AA:42:CF:1F:36:AC:94:D2:47:B2:3E:A3:B1:27:52:67:C5:6F:7B:CB:FF:9F:30:47:56:99
```

上面的输出中可以看出来，在 http.p12 中有两个 entry，其中一个是私钥。考虑到我们并不便于发送这个给客户端。我们可以使用如下的方法来创建 truststore

```bash
keytool -import -file http_ca.crt -keystore truststore.p12 -storepass password -noprompt -storetype pkcs12
```

在当前的目录下创建了一个叫做 truststore.p12 的文件，它的密码是 password
使用如下的命令来查看这个 truststore 的内容

```bash
keytool -keystore truststore.p12 -list
$ pwd
/Users/liuxg/elastic/elasticsearch-8.4.1/config/certs
$ ls
http.p12      http_ca.crt   transport.p12
$ keytool -import -file http_ca.crt -keystore truststore.p12 -storepass password -noprompt -storetype pkcs12
Certificate was added to keystore
$ ls
http.p12       http_ca.crt    transport.p12  truststore.p12
$ keytool -keystore truststore.p12 -list
Enter keystore password:
Keystore type: PKCS12
Keystore provider: SUN

Your keystore contains 1 entry

mykey, Sep 30, 2022, trustedCertEntry,
Certificate fingerprint (SHA-256): B4:8C:3E:33:FE:E5:AA:42:CF:1F:36:AC:94:D2:47:B2:3E:A3:B1:27:52:67:C5:6F:7B:CB:FF:9F:30:47:56:99
```

可以看到在生成的 truststore.p12 中只有一个项目，别名叫做 mykey

根据上面所生成的 truststore.p12 及其访问密码 password，我们可以修改上面的 elasticsearch 配置如下

```conf
; # logstash.conf
    elasticsearch {
    	hosts => ["https://localhost:9200"]
    	index => "data-%{+YYYY.MM.dd}"
    	user => "elastic"
    	password => "ndktp2Xr2h_*Q6EZfq4t"
		ssl_certificate_verification => true
		truststore => "/Users/liuxg/elastic/elasticsearch-8.4.1/config/certs/truststore.p12"
		truststore_password => "password"
  	}
```

我们再次重新运行之前的命令即可

### 使用 API key 连接

可以通过 API Key 来连接到 Elasticsearch

- 在 Kibana 中创建一个 API Key
  `Stack Management > API keys` 新建并复制为 Logstash 格式
- API 创建
  ```bash
  POST /_security/api_key
  {
    "name": "logstash-api-key",
    "role_descriptors": {
      "logstash_writer": {
        "cluster": ["manage_index_templates", "monitor", "manage_ingest_pipelines"],
        "index": [
          {
            "names": ["*"],
            "privileges": ["write", "create", "create_index", "manage"]
          }
        ]
      }
    }
  }
  ```
  或者 cURL
  ```bash
  curl -X POST "https://your-elasticsearch-host:9200/_security/api_key" -H "Content-Type: application/json" -d'
  {
    "name": "logstash-api-key",
    "role_descriptors": {
      "logstash_writer": {
        "cluster": ["manage_index_templates", "monitor", "manage_ingest_pipelines"],
        "index": [
          {
            "names": ["*"],
            "privileges": ["write", "create", "create_index", "manage"]
          }
        ]
      }
    }
  }' -u elastic:your_password
  ```

使用 API KEY

```conf
nput {
  generator {
    message => "liuxg"
    count => 1
  }
}

output {
    stdout {
      codec => rubydebug
    }

    elasticsearch {
      hosts => ["https://localhost:9200"]
      index => "data-%{+YYYY.MM.dd}"
      ssl => true
      ilm_enabled => true
      ssl_certificate_verification => false
      api_key => "GMl1S4QBW_e6QIS4FQXK:KtC_17NAQt6Ef_7xuqzUCA"
    }
}
```

### 使用 fingerprint 连接
Fingerprint 的好处是，我们不必把把证书拷贝到 Logstash 运行的服务器中

### Reference

- [docker 安装 logstash](https://www.jianshu.com/p/f45e4b6de0e8)
- [Logstash：如何连接到带有 HTTPS 访问的集群](https://blog.csdn.net/UbuntuTouch/article/details/126868040)

**2024.07.04**
