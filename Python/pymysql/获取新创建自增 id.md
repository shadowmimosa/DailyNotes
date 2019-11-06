<font size=4 face='楷体'>

## 获取新插入数据的自增 id

```python
import pymsql

conn = pymysql.connect(host='localhost', user='test', password="123456", database='test1',
                       port=3306, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
try
	with conn.cursor() as curs:
		curs.execute("insert into user (name, age) values (%s, %s)", ("Marsen", '26'))
		last_id = curs.lastrowid # 获取最新 id
except Exception as e:
	conn.rollback()
finally:
	conn.commit()
	conn.close()
```

### Reference

[[Python 开发-pymysql]--获取新插入数据的 id](https://blog.csdn.net/qq_36609501/article/details/88362841)
[MySQL---pymysql 驱动操作---获取新创建数据自增 ID、获取查询数据](https://blog.csdn.net/qq562029186/article/details/81051304)

**2019.11.6**
