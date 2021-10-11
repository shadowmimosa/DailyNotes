<font size=4 face='楷体'>

## Loguru 基本使用

Loguru 一个能彻底解放你的日志记录器
它即插即用, 具备多种方式滚动日志、自动压缩日志文件、定时删除等功能
除此之外, 多线程安全、高亮日志、日志告警等功能也不在话下

### 安装

```bash
pip install loguru
```

### 滚动日志与压缩

`rotation`参数

#### 按时间滚动

```python
from loguru import logger

logger.add("log.log", rotation="12:00") # 每天12:00会创建一个新的文件
```

#### 按大小滚动

```python
from loguru import logger

logger.add("log.log", rotation="1 MB") # 滚动大日志文件
```

#### 压缩日志

`compression` 参数

```python
from loguru import logger

logger.add("log.log", compression="zip") # 压缩日志
```

### 自定义颜色

```python
from loguru import logger

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
```

#### 支持颜色关键字

| Color (abbr) | Styles (abbr) |
| ------------ | ------------- |
| Black (k)    | Bold (b)      |
| Blue (e)     | Dim (d)       |
| Cyan (c)     | Normal (n)    |
| Green (g)    | Italic (i)    |
| Magenta (m)  | Underline (u) |
| Red (r)      | Strike (s)    |
| White (w)    | Reverse (v)   |
| Yellow (y)   | Blink (l)     |
|              | Hide (h)      |

#### 使用

| Description  | Foreground                            | Background                  |
| ------------ | ------------------------------------- | --------------------------- |
| Basic colors | `<red>`, `<r>`                        | `<GREEN>`, `<G>`            |
| Light colors | `<light-blue>`, `<le>`                | `<LIGHT-CYAN>`, `<LC>`      |
| 8-bit colors | `<fg 86>`, `<fg 255>`                 | `<bg 42>`, `<bg 9>`         |
| Hex colors   | `<fg #00005f>`, `<fg #EE1>`           | `<bg #AF5FD7>`, `<bg #fff>` |
| RGB colors   | `<fg 0,95,0>`                         | `<bg 72,119,65>`            |
| Stylizing    | `<bold>`, `<b>`, `<underline>`, `<u>` |                             |

[官方文档](https://loguru.readthedocs.io/en/stable/api/logger.html#color)

### 多进程安全

Loguru 默认情况下是线程安全的, 但它不是多进程安全的
需要多进程/异步记录日志, 需要添加 `enqueue` 参数

```python
from loguru import logger

logger.add("log.log", enqueue=True)
```

### Backtrace

Loguru 允许显示整个堆栈信息来帮助你发现问题(包括变量)

```python
from loguru import logger

logger.add("log.log", backtrace=True, diagnose=True) # Caution, may leak sensitive data in prod

try:
    raise RuntimeError
except Exception:
    logger.exception('RuntimeError')
```

### 邮件告警

Loguru 可以和强大的邮件通知模块 notifiers 库结合使用

```python
import notifiers
from loguru import logger

params = {
    "username": "username@mail.com",
    "password": "password",
    "to": "mail@mail.com"
}

# 初始化时发送一封邮件
notifier = notifiers.get_notifier("gmail")
notifier.notify(message="The application is running!", **params)

# 发生Error日志时，发邮件进行警报
from notifiers.logging import NotificationHandler

handler = NotificationHandler("gmail", defaults=params)
logger.add(handler, level="ERROR")
```

### format 格式

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

[Python - loguru 日志库, 高效输出控制台日志和日志记录](https://www.cnblogs.com/poloyy/p/12435089.html)
[使用 loguru 记录日志](https://www.jianshu.com/p/2945634fe349)
[Python 中更优雅的日志记录方案 loguru](https://cuiqingcai.com/7776.html)

[loguru.logger](https://loguru.readthedocs.io/en/stable/api/logger.html)
[Loguru：优雅的 Python 程序日志](https://www.jianshu.com/p/0c27ac960546)
[Python 优雅日志记录器-Loguru](https://www.cnblogs.com/kcxg/p/14509851.html)

**Create On 2020.09.17, Update On 2020.11.02**
