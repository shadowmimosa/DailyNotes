<font size=4 face='楷体'>

## top & htop

### top 命令的使用

> top 命令是 Linux 下常用的性能分析工具，能够实时显示系统中各个进程的资源占用状况，类似于 Windows 的任务管理器。

使用也比较简单，直接命令行输入 top 即可
退出 top 交互的命令为 q （在 top 运行中敲 q 键一次）

- 几种常用排序

  - P: 按进程的 CPU 使用率排序（大写 P, 即 shift + P）
  - M: 按进程的内存使用率排序（大写 M, 即 shift + M）

- 交互命令

  > c：显示完整的命令
  > d：更改刷新频率
  > f：增加或减少要显示的列(选中的会变成大写并加\*号)
  > F：选择排序的列
  > h：显示帮助画面
  > H：显示线程
  > i：忽略闲置和僵死进程
  > k：通过给予一个 PID 和一个 signal 来终止一个进程。（默认 signal 为 15。在安全模式中此命令被屏蔽）
  > l: 显示平均负载以及启动时间（即显示影藏第一行）
  > m：显示内存信息
  > M：根据内存资源使用大小进行排序
  > N：按 PID 由高到低排列
  > o：改变列显示的顺序
  > O：选择排序的列，与 F 完全相同
  > P：根据 CPU 资源使用大小进行排序
  > q：退出 top 命令
  > r：修改进程的 nice 值(优先级)。优先级默认为 10，正值使优先级降低，反之则提高的优先级
  > s：设置刷新频率（默认单位为秒，如有小数则换算成 ms）。默认值是 5s，输入 0 值则系统将不断刷新
  > S：累计模式（把已完成或退出的子进程占用的 CPU 时间累计到父进程的 MITE+ ）
  > T：根据进程使用 CPU 的累积时间排序
  > t：显示进程和 CPU 状态信息（即显示影藏 CPU 行）
  > u：指定用户进程
  > W：将当前设置写入~/.toprc 文件，下次启动自动调用 toprc 文件的设置
  > <：向前翻页
  > ：向后翻页
  > ?：显示帮助画面
  > 1(数字 1)：显示每个 CPU 的详细情况

- 内容解释

  第一行（top）：

        15:24:36 系统当前时刻

        14 days 系统启动后到现在的运作时间

        3 users 当前登录到系统的用户，更确切的说是登录到用户的终端数 -- 同一个用户同一时间对系统多个终端的连接将被视为多个用户连接到系统，这里的用户数也将表现为终端的数目

        load average 当前系统负载的平均值，后面的三个值分别为 1 分钟前、5 分钟前、15 分钟前进程的平均数，一般的可以认为这个数值超过 CPU 数目时，CPU 将比较吃力的负载当前系统所包含的进程

  第二行（Tasks）：

        288 total 当前系统进程总数

        1 running 当前运行中的进程数

        287 sleeping 当前处于等待状态中的进程数

        0 stoped 被停止的系统进程数

        0 zombie 僵尸进程数

  第三行（Cpus）：

        7.3% us 用户空间占用CPU百分比
        2.0% sy 内核空间占用CPU百分比
        0.0% ni 用户进程空间内改变过优先级的进程占用CPU百分比
        90.4% id 空闲CPU百分比
        0.3% wa 等待输入输出的CPU时间百分比
        0.0% hi
        0.0% si
        0.0% st

  第四行（Mem）：

        2042616 total 物理内存总量
        1770116 used 使用的物理内存总量
        272500 free 空闲内存总量
        163912 buffers 用作内核缓存的内存量

  第五行（Swap）：

        表示类别同第四行（Mem），但此处反映着交换分区（Swap）的使用情况。通常，交换分区（Swap）被频繁使用的情况，将被视作物理内存不足而造成的。

        2094076 total 交换区总量
        45052 used 使用的交换区总量
        2049024 free 空闲交换区总量
        346624 cached 缓冲的交换区总量

  最下部分的进程列表栏：

        以 PID 区分的进程列表将根据所设定的画面更新时间定期的更新。通过 top 内部命令可以控制此处的显示方式:

        PID：进程的ID
        USER：进程所有者
        PR：进程的优先级别，越小越优先被执行
        NInice：值
        VIRT：进程占用的虚拟内存
        RES：进程占用的物理内存
        SHR：进程使用的共享内存
        S：进程的状态。S表示休眠，R表示正在运行，Z表示僵死状态，N表示该进程优先值为负数
        %CPU：进程占用CPU的使用率
        %MEM：进程使用的物理内存和总内存的百分比
        TIME+：该进程启动后占用的总的CPU时间，即占用CPU使用时间的累加值。
        COMMAND：进程启动命令名称

### Tips

- 使用 top -c 命令过滤基于进程名称列出的进程
  ```bash
  # top -p 期望逗号分隔的 pid 列表
  # -d',' 在 pgrep 中使用
  # -f pgrep 中的标志使其与命令行相匹配，而不是程序名称
  top -c -p $(pgrep -d',' -f string_to_match_in_cmd_line)
  ```
  ```bash
  # 刷新输出
  top -bc |grep name_of_process
  ```

### top 各指标的含义

- VIRT：virtual memory usage 虚拟内存
- - 进程“需要的”虚拟内存大小，包括进程使用的库、代码、数据等
- - 假如进程申请 100m 的内存，但实际只使用了 10m，那么它会增长 100m，而不是实际的使用量

- RES：resident memory usage 常驻内存
- - 进程当前使用的内存大小，但不包括 swap out
- - 包含其他进程的共享
- - 如果申请 100m 的内存，实际使用 10m，它只增长 10m，与 VIRT 相反
- - 关于库占用内存的情况，它只统计加载的库文件所占内存大小

- SHR：shared memory 共享内存
- - 除了自身进程的共享内存，也包括其他进程的共享内存
- - 虽然进程只使用了几个共享库的函数，但它包含了整个共享库的大小
- - 计算某个进程所占的物理内存大小公式：RES – SHR
- - swap out 后，它将会降下来

- DATA
- - 数据占用的内存。如果 top 没有显示，按 f 键可以显示出来
- - 真正的该程序要求的数据空间，是真正在运行中要使用的

top 运行中可以通过 top 的内部命令对进程的显示方式进行控制

```bash
s – 改变画面更新频率
l – 关闭或开启第一部分第一行 top 信息的表示
t – 关闭或开启第一部分第二行 Tasks 和第三行 Cpus 信息的表示
m – 关闭或开启第一部分第四行 Mem 和 第五行 Swap 信息的表示
N – 以 PID 的大小的顺序排列表示进程列表
P – 以 CPU 占用率大小的顺序排列进程列表
M – 以内存占用率大小的顺序排列进程列表
h – 显示帮助
n – 设置在进程列表所显示进程的数量
q – 退出 top
s – 改变画面更新周期
```

### htop 安装

[htop on github](https://github.com/htop-dev/htop)

- CentOS 7
  ```bash
  yum install epel-release -y
  yum install htop -y
  ```
- CentOS 8
  ```bash
  # 启用 EPEL 存储库
  dnf install https://dl.Fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
  # 更新
  dnf update
  # 安装 htop
  dnf install htop
  ```

### Reference

[top 命令按内存和 cpu 排序](https://www.cnblogs.com/jiqing9006/p/9270504.html)
[Linux 查看 CPU 和内存使用情况](https://www.cnblogs.com/mengchunchen/p/9669704.html)
[Centos7 安装和使用 htop](https://blog.csdn.net/weixin_43960618/article/details/109055228)
[centos8 安装 htop](https://www.cnblogs.com/huangdashu/p/13921230.html)
[linux top 命令 VIRT,RES,SHR,DATA 的含义](https://javawind.net/p131)
[在 Linux 中如何使用 top -c 命令过滤基于进程名称列出的进程](https://cloud.tencent.com/developer/ask/52436)

**Create On 2020.10.31, Update On 2020.11.05**
