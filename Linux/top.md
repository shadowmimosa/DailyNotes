<font size=4 face='楷体'>

## Linux top 命令

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

### Reference

[linux top 命令 VIRT,RES,SHR,DATA 的含义](https://javawind.net/p131)
[在 Linux 中如何使用 top -c 命令过滤基于进程名称列出的进程](https://cloud.tencent.com/developer/ask/52436)

**2020.10.22**
