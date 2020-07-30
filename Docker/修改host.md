<font size=4 face='楷体'>

## 为 Docker 容器设置 hosts

- 启动参数

  ```bash
  # –add-host machine:ip
  docker run -it --name alpine-test1 --add-host=test.baidu.com:192.168.1.37 docker.io/alpine
  ```

- DockerFile

  ```DockerFile
  RUN mkdir /data
  COPY run.sh /data/
  RUN chmod +x /data/run.sh

  ENTRYPOINT /bin/sh -c /data/run.sh
  ```

  run.sh

  ```shell
  # 向hosts文件追加内容
  #cat /data/myhosts >> /etc/hosts
  echo "192.168.1.37 testgitlab.kuaidihelp.com"  >> /etc/hosts

  # 其他命令

  # 保留终端，防止容器自动退出
  /bin/sh
  ```

### Reference

[Docker 容器如何修改 hosts](https://www.cnblogs.com/mrnx2004/p/11767354.html)

**2020.07.30**
