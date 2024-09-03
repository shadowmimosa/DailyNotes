<font size=4 face='楷体'>

## logstash multi pipeline

假设我们需要从多个渠道来收集数据，比如：1、从文件收集。2、从 tcp 收集。不同的渠道收集过来的数据需要做不同的处理。那么我们这个时候应该如何处理呢？

### 方案一

使用同一个 logstash 实例，然后将在一个 pipeline 中，接收多个输入

```xml
input {
    file {}
    file {}
    tcp {}
}
```

这样虽然可以实现，但是我们 在 `filter` 和 `output`阶段如果不同的输入存在不同的过滤、输出等，那么这个文件将会非常复杂，需要进行各种判断，不好维护。

### 方案二

使用多个 logstash 实例，每个 logstash 实例处理不同的输入。这样虽然可以实现，但是 logstash 稍微有点耗费性能，也是不可取的。

### 方案三

在同一个 logstash 实例中，使用多个 pipeline，每个 pipeline 处理不同的 `input`,`filter`和`out`。即配置分散在多个配置文件中。

### 实现步骤

> 此处采用上方的 `方案三` 来实现。

- 从文件收集，输出到控制台

```yaml
# file-pipeline.conf
input {
file {
path => ["/Users/huan/soft/elastic-stack/logstash/logstash/pipeline.conf/multi-pipeline/file-pipeline.log"]
start_position => "end"
sincedb_path => "/Users/huan/soft/elastic-stack/logstash/logstash/pipeline.conf/multi-pipeline/sincedb.db"
sincedb_write_interval => "15 seconds"
mode => "tail"
type => "file-pipeline"
}
}

filter {

}

output {
stdout {
codec => rubydebug {
metadata => true
}
}
}
```

- 从 socket 收集，输出到控制台

```yaml
# tcp-pipeline.conf
# 开启一个tcp监听在9092端口
# id 的值建议设置成唯一的值，这在多个tcp input时，使用监控api时非常有用的。
input {
tcp {
port => 9202
host => "127.0.0.1"
mode => "server"
type => "tcp-pipeline"
id => "console-tcp"
}
}

filter {

}

output {
stdout {
codec => line {
charset => "UTF-8"
}
}
}
```

**注意 ⚠️** tcp 中的 `id`的值建议设置成一个唯一的值，这个当我们有多个 `tcp` 输入时，在我们使用监控 api 会非常有用。

- pipelines.yml 配置文件

```yaml
# LS_HOME/config/pipelines.yml
- pipeline.id: file-pipeline
  path.config: '/Users/huan/soft/elastic-stack/logstash/logstash/pipeline.conf/multi-pipeline/file-pipeline.conf'
- pipeline.id: tcp-pipeline
  queue.type: persisted
  path.config: '/Users/huan/soft/elastic-stack/logstash/logstash/pipeline.conf/multi-pipeline/tcp-pipeline.conf'
```

**注意 ⚠️** 如果上方的配置文件使用的是一个 `pipeline`，比如删除下方的 tcp-pipeline,将 file-pipeline 的 path.config 的值修改成 `.../*.conf`,

那么此时会共用 `output`，会发现数据重复。

即修改成：

```yaml
# 这样是多个配置文件共用一个 pipeline，filter\output等会共享。
- pipeline.id: file-pipeline
  path.config: '/Users/huan/soft/elastic-stack/logstash/logstash/pipeline.conf/multi-pipeline/*.conf'
```

- 启动 logstash

**注意 ⚠️** 此处的启动命令后不可跟 `-e`或`-f`，如果跟了，则不会使用默认的 `config/pipelines.yml`。

### Reference

- [logstash multi pipeline的使用](https://www.jianshu.com/p/9da006b4bec4)

**2024.08.02**
