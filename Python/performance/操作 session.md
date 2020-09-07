<font size=4 face='楷体'>

## flask 操作 session

在 flask 中操作 session 有一点需要注意，就是需要设置一个 `SECRET_KEY`

```python
import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
```

- 写入 session

  ```python
  from flask import session

  session['username'] = 'zhangsan'
  ```

- 获取 session

  ```python
  from flask import session

  session.get('username')
  ```

- 删除清空 session

  ```python
  from flask import session

  # 删除 username
  session.pop('username')

  # 清空
  session.clear()
  ```

- 设置 session 的过期时间

  > 如果没有指定 session 的过期时间，那么默认是浏览器关闭就自动结束，
  > 如果设置了 session 的 permanent 属性为 True，那么过期时间是 31 天。

  ```python
  from flask import Flask
  from flask import session
  from datetime import timedelta

  app = Flask(__name__)

  # 设置过期时间为 7 天
  app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

  # 过期时间为 31 天
  session.permanent = True
  ```

### Reference

[Flask 操作 session](https://www.jianshu.com/p/dd0aa75f3f0e)

**2020.09.07**
