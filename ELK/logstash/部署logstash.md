<font size=4 face='楷体'>

## 部署 logstash

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

### Reference

- [docker 安装 logstash](https://www.jianshu.com/p/f45e4b6de0e8)
- [logstash 导入 mysql 越来越慢](https://blog.csdn.net/xujiamin0022016/article/details/100789622/)

**2024.07.04**
