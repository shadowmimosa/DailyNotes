<font size=4 face='楷体'>

## pymongo 使用 ObjectId

在 python 使用 ObjectId 作为查询条件时，不能通过普通的字符串查询

- 将字符串转成 ObjectId

  ```python
  from bson.objectid import ObjectId

  def get(post_id):
      # Convert from string to ObjectId:
      document = client.db.collection.find_one({'_id': ObjectId(post_id)})
  ```

- 格式化后的数字或者字符串转成 ObjectId
  结合 zfill() 进行补位

  ```python
  from bson.objectid import ObjectId

  def get(post_id):
      # Convert from string or int to ObjectId:
      document = client.db.collection.find_one({'_id': ObjectId(str(post_id).zfill(24))})
  ```

### Reference

[Python：补零操作](https://www.cnblogs.com/kangjianwei101/p/5621723.html)
[pymongo 关于 ObjectId 查询](https://www.jianshu.com/p/7c40bdc51c8a)

**2019.12.11**
