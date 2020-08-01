<font size=4 face='楷体'>

## 日志

- 命令格式

  ```bash
  docker logs [OPTIONS] CONTAINER
    Options:
          --details        显示更多的信息
      -f, --follow         跟踪实时日志
          --since string   显示自某个timestamp之后的日志，或相对时间，如42m（即42分钟）
          --tail string    从日志末尾显示多少行日志， 默认是all
      -t, --timestamps     显示时间戳
          --until string   显示自某个timestamp之前的日志，或相对时间，如42m（即42分钟）
  ```

- 例子
  查看指定时间后的日志，只显示最后 100 行

  ```bash
  $ docker logs -f -t --since="2018-02-08" --tail=100 CONTAINER_ID
  ```

  查看最近 30 分钟的日志

  ```bash
  $ docker logs --since 30m CONTAINER_ID
  ```

  查看某时间之后的日志

  ```bash
  $ docker logs -t --since="2018-02-08T13:23:37" CONTAINER_ID
  ```

  查看某时间段日志

  ```bash
  $ docker logs -t --since="2018-02-08T13:23:37" --until "2018-02-09T12:23:37" CONTAINER_ID
  ```

### Reference

[docker logs－查看 docker 容器日志](https://www.cnblogs.com/gylhaut/p/9317843.html)

**2020.07.30**
