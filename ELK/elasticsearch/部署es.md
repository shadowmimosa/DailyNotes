<font size=4 face='楷体'>

## 部署 elasticsearch

### docker 部署

使用 docker 部署 es，简化部署环境配置

- 单实例
  ```bash
  docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 \
    -v $PWD/elasticsearch/data:/usr/share/elasticsearch/data \
    -e "discovery.type=single-node" \
    --name elasticsearch \
    docker.elastic.co/elasticsearch/elasticsearch-oss:6.2.4
  ```
  如果挂载卷时[报错](https://stackoverflow.com/questions/51201699/elasticsearch-docker-image-with-data-persistence) `java.nio.file.AccessDeniedException` 或 `java.io.IOException` 需要创建该文件夹并赋权：
  ```bash
  sudo mkdir -p $PWD/elasticsearch/data
  sudo chmod 777 -R $PWD/elasticsearch/data
  ```

### Reference

- [Logstash 导入 mysql 数据到 es 慢的解决方法](https://blog.csdn.net/qq_38798909/article/details/120825512)
- [logstash 导入 mysql 越来越慢](https://blog.csdn.net/xujiamin0022016/article/details/100789622/)

**2024.07.04**
