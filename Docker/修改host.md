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

- 进入容器修改
  直接进入文件修改 /etc/hosts, 在重启容器后, 增加的内容会丢失

- docker-compose.yml
  通过配置参数 extra_hosts 来实现
  ```bash
  extra_hosts:
  - "somehost:162.242.195.82"
  - "otherhost:50.31.209.229"
  ```

### Reference

[Docker 容器如何修改 hosts](https://www.cnblogs.com/mrnx2004/p/11767354.html)
[修改 docker 容器中的 hosts 文件](https://www.cnblogs.com/sucretan2010/p/12123767.html)

**Create On 2020.07.30, Update On 2022.03.03**
