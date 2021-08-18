<font size=4 face='楷体'>

## Loguru 基本使用

| Key       | Description                                           | Attributes               |
| --------- | ----------------------------------------------------- | ------------------------ |
| elapsed   | The time elapsed since the start of the program       | See datetime.timedelta   |
| exception | The formatted exception if any, None otherwise        | type, value, traceback   |
| extra     | The dict of attributes bound by the user (see bind()) | None                     |
| file      | The file where the logging call was made              | name (default) , path    |
| function  | The function from which the logging call was made     | None                     |
| level     | The severity used to log the message                  | name (default), no, icon |
| line      | The line number in the source code                    | None                     |
| message   | The logged message (not yet formatted)                | None                     |
| module    | The module where the logging call was made            | None                     |
| name      | The `__name__` where the logging call was made        | None                     |
| process   | The process in which the logging call was made        | name, id (default)       |
| thread    | The thread in which the logging call was made         | name, id (default)       |
| time      | The aware local time when the logging call was made   | See `datetime.datetime`  |

### Reference

[Python - loguru 日志库，高效输出控制台日志和日志记录](https://www.cnblogs.com/poloyy/p/12435089.html)
[使用 loguru 记录日志](https://www.jianshu.com/p/2945634fe349)
[Python 中更优雅的日志记录方案 loguru](https://cuiqingcai.com/7776.html)

[loguru.logger](https://loguru.readthedocs.io/en/stable/api/logger.html)
[Loguru：优雅的Python程序日志](https://www.jianshu.com/p/0c27ac960546)

**Create On 2020.09.17, Update On 2020.11.02**
