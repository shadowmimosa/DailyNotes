<font size=4 face='楷体'>

## `python.exe` 和 `pythonw.exe` 的区别 (区分 `.py、` `.pyw` 、 `.pyc` 、 `.pyo` 文件)

### python 和 pythonw

在 Windows 系统搭建好 Python 的环境后, 进入 Python 的安装目录, 会发现目录中有 python `.exe` 和 pythonw `.exe` 两个程序

- `python.exe`
  在运行程序的时候, 会弹出一个黑色的控制台窗口（也叫命令行窗口、DOS/CMD 窗口）；

- `pythonw.exe`
  是无窗口的 Python 可执行程序, 意思是在运行程序的时候, 没有窗口, 代码在后台执行。

安装视窗版 Python 时, 扩展名为 `.py ` 的文件被默认为用 python `.exe` 运行的文件, 而 `.pyw` 文件则被默认为用 pythonw `.exe` 运行

### pyw

`.pyw` 格式是被设计用来运行开发的纯图形界面程序的, 纯图形界面程序的用户不需要看到控制台窗口。在开发纯图形界面程序的时候, 可以暂时把 `.pyw` 改成 `.py ` , 运行时能调出控制台窗口, 方便看到所有错误信息

### pyc

至于 `.pyc` 文件, 是 Python 解释器运行程序的过程中产生的字节码文件（也就是中间文件）

### pyo

在 pyc 的基础上, 去掉了 assert 和 docstring

python3.5 之后, 无 `.pyo` 文件

### py 文件执行后不马上关闭窗口

这里还要解释一个问题, 如果 `.py ` 文件直接用 python `.exe` 打开, 文件被执行完成之后, 视窗会立即关闭, 如果想让视窗停留, 给大家提供几个方法

- 可以在程序中加入超长睡眠语句, 如`time.sleep(1800)`, 如果你不手动关闭视窗, 视窗将会停留 30min

- 可以调用 sys 和 os 模块, 使用命令行语句 pause, 示例：`import os os.system("pause")`

- 在脚本的最后加入一行 `input("请按任意键继续")`, 这样会等待输入任意字符后才会关闭窗口

### Reference

[python.exe 和 pythonw.exe 的区别（区分.py、.pyw、.pyc、.pyo 文件）](https://www.cnblogs.com/zhaoqingqing/p/14869679.html)

**2022.10.27**
