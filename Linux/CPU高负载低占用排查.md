<font size=4 face='楷体'>

## Linux CPU 高负载低占用排查

top 或 htop 查看 CPU 占用较低，但是 load average 持续异常高

load average 是对 CPU 负载的评估，其值越高，说明其任务队列越长，处于等待执行的任务越多
出现此种情况时，可能是由于僵死进程导致的。可以通过指令 ps -axjf 查看是否存在 D 状态进程

```bash
# 查看假死进程
ps -axjf
```

实际使用未筛出假死进程
后在 htop 中对状态进行查询，筛出大量 mysql 假死子进程，重启 mysql 解决

附 mysql 进程导致的负载高处理办法

-   常见的就是 mysql 慢查询导致，可以在 mysql 慢查询日志找到相关 sql 语句，这需要对 sql 进行优化
-   还可以进入 mysql，用 show full processlist\G; 查看那个 mysql 进程执行时间比较久的慢查询。如果是内部后台使用的语句，可以先 kill 掉，优化后再执行。
-   mysql 读写太频繁，如果是读写频繁可以在 %wa 等待输入输出看的出来占用 cpu 百分比很大。也可以通过命令 iostat 查看系统读写情况。

子进程大概不怕 ps 或 top 探测到

### 指标含义

#### 进程

Linux 中，进程分为三种状态：

-   阻塞的进程 blocked process
-   可运行的进程 runnable process
-   正在运行的进程 running process
    当进程阻塞时，进程会等待 I/O 设备的数据或者系统调用。
    进程处于可运行状态时，它处在一个运行队列中，与其他可运行进程争夺 CPU

#### CPU 使用率

-   CPU 使用率指的是程序在运行期间实时占用的 CPU 百分比，这是对一个时间段内 CPU 使用状况的统计。
    通过这个指标可以看出在某一个时间段内 CPU 被占用的情况

-   CPU 负载（load）
    它指的是正在运行（running）和准备运行（runnable）的进程的总数，也就是是等待处理的任务队列

-   load-average

    它指的就是特定时间内运行队列中(在 CPU 上运行或者等待运行)的平均进程数。
    在 linux top 命令中指的是是最近 1 分钟、5 分钟和 15 分钟的系统平均负载

如果一个进程满足以下条件，则其就会位于运行队列中

-   它没有在等待 I/O 操作的结果
-   它没有主动进入等待状态(也就是没有调用 wait)
-   没有被停止

#### cpu 负载的计算

CPU 数量和 CPU 内核数都会影响到 CPU 负载，因为任务最终是要分配到 CPU 核心去处理的。

两块 CPU 要比一块 CPU 好，双核要比单核好。因此，除去 CPU 性能上的差异，CPU 负载是基于内核数来计算的。

"有多少内核，就有多少 load" 如单核负载为 1.00，双核负载为 2.00 以此类推

> CPU 利用率高也并不意味着负载就一定大可能这个任务是一个 CPU 密集型的。CPU 低利用率的情况下也会有高 Load Average 的情况。当 CPU 分配时间片以后，是否使用完全取决于使用者，因此完全可能出现低利用率高 Load Average 的情况。

### Reference

[CPU 使用率较低但负载较高](https://www.cnblogs.com/fjping0606/p/10103294.html)
[负载高导致服务器变慢处理方法](https://blog.csdn.net/yuanlin65/article/details/52663224)
[性能测试-cpu 负载和 cpu 利用率](https://cloud.tencent.com/developer/article/1506724)

**2020.09.18**
