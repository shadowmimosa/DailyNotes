<font size=4 face='楷体'>

## Jenkins 触发构建

安装 [AnsiColor](https://plugins.jenkins.io/ansicolor/) 插件

-   颜色对照表

    | 颜色            | 前景色 | 背景色 |
    | --------------- | ------ | ------ |
    | 黑色(Black)     | 30     | 40     |
    | 红色(Red)       | 31     | 41     |
    | 绿色(Green)     | 32     | 42     |
    | 黄色(Yellow)    | 33     | 43     |
    | 蓝色(Blue)      | 34     | 44     |
    | 紫红色(Magenta) | 35     | 45     |
    | 青色(Cyan)      | 36     | 46     |
    | 白色(White)     | 37     | 47     |

还需在 Job 中设置终端模拟器为 xterm

```bash
Color ANSI Console Output
ANSI color map
xterm
```

### Reference

[jenkins 输出 Log 改变颜色(jenkins 优化篇)](https://www.jianshu.com/p/12083063957b?from=timeline)

**2020.12.15**
