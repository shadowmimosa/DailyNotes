<font size=4 face='楷体'>

## Arrow 使用

第三方库 Arrow 提供了一个合理的、人性化的方法来创建、操作、格式转换的日期，时间，和时间戳，帮助我们使用较少的导入和更少的代码来处理日期和时间

- 安装
  ```bash
  pip install arrow
  ```
- 获取当前时间
  ```python
  arrow.utcnow()
  arrow.now()
  ```
- 将时间戳转化为 arrow 对象
  ```python
  arrow.get(timestamp)
  ```
- 将字符串转换为 arrow 对象
  ```python
  arrow.get('2018-02-24 12:30:45', 'YYYY-MM-DD HH:mm:ss')
  ```
  遵循 ISO-8601 的字符串不需要格式字符串参数即可转换
  ```python
  arrow.get('2018-02-24T13:00:00.000-07:00')
  ```
  可以从字符串中通过格式参数搜索时间
  ```python
  arrow.get('June was born in May 1980', 'MMMM YYYY')
  ```
- 创建 arrow 对象
  ```python
  arrow.get(2018, 2, 24)
  arrow.Arrow(2018, 2, 24)
  ```
- arrow 对象属性
  datetime, timestamp, native, tzinfo
  year, month, day, hour, minute, second

- 时间推移
  shift 方法获取某个时间之前或之后的时间,关键字参数为 years, months, weeks, days, hours, seconds, microseconds

  ```python
  arrow.now().shift(days=1)  # 一天后
  arrow.now().shift(days=-1)  # 一天前
  ```

- 时间替换
  replace 方法返回一个被替换后的 arrow 对象，原对象不变
  ```python
  arrow.now().replace(hour=10)
  ```
- 格式化输出
  format 方法
  ```python
  arrow.now().format()
  arrow.now().format('YYYY-MM-DD HH:mm:ss ZZ')
  ```
- 人性化输出
  humanize 方法
  ```python
  >>> present = arrow.utcnow()
  >>> past = present.shift(hours=-1)
  >>> past.humanize()       #相对于当前时间
  'an hour age'
  >>> future = present.shift(hours=2)
  >>> future.humanize(present)    #相对于参数时间
  'in 2 hours'
  >>> past.humanize(present, locale='zh')   #locale参数可以指定地区语言
  '1天前'
  ```
- 时间范围和区间
  span, span_range 方法

### Reference

[Python 处理日期时间——Arrow 库](https://blog.csdn.net/dagu131/article/details/79365301)

**2020.09.16**
