<font size=4 face='楷体'>

## Linux kill 四种用法

1. > pkill 进程名
2. > killall 进程名
3. > kill -9 \$(ps -ef|grep 进程名关键字|grep -v grep|awk '{print \$2}')
4. > kill -9 \$(pidof 进程名关键字)
5. > ps aux | grep 进程名关键字 | awk '{print \$2}' | xargs kill -9

ps 列出所有进程，参数：

    a - 显示现行终端机下的所有进程，包括其他用户的进程；
    u - 以用户为主的进程状态；
    x - 通常与 a 这个参数一起使用，可列出较完整信息。

## Reference

[Linux kill 指定进程名的四种方式](https://www.cnblogs.com/chay/p/10473091.html)
[linux kill 掉所有匹配到名字的进程](https://blog.csdn.net/zhanjianjiu/article/details/87285784)

**2020.03.28**
