<font size=4 face='楷体'>  

## 常见报错

### Cannot assign "A1": "B1" must be a "C1" instance.  

告诉我们 必须使用 C1 模型类的 实例，而不是具体的参数值。  

> 这个错误信息，是在写入数据库时，外键传了实际参数造成的

> 如果外键用 fid 表示
> 写入数据库时：Model.objects.create(fid=1, ...)就会报错

把 fid 改为
> A = Model.objects.get(id=1)
> Model.objects.create(fid=A, ...)

或者
> A = Model.objects.get(...)  
> Model.objects.create(fid=A.id, ...)  


### Reference

[Link](https://blog.csdn.net/sunt2018/article/details/81772343)   


### `ForeignKey` Django 中的外键  

在创建表时，指定外键的列名会自动加上 `_id`  

例如：  

> belong_project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)

这条语句生成的列名为 `belong_project_id`

查询时可以使用
> belong_project = id
> belong_project_id = id
> belong_project__id = id

这三种语句都能得到同样的结果
或者
> belong_project = 'id'
这种方式是因为，Django 查询时，会强转类型为 `int`，所以如果 id 异常会报错。

**2018.12.25**

