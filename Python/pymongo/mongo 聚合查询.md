<font size=4 face='楷体'>

## mongo 聚合 联表查询

这次是直接从没怎么用过 mongo 到用聚合了  
聚合基本语法在[这里](https://www.runoob.com/mongodb/mongodb-aggregate.html)
以及一些基本数据类型在[这里](https://www.cnblogs.com/guoxiaoyan/p/9403630.html)

### 联表查询

举个栗子

- 数据如下：

  ```javascript
  db.getCollection("user").insert([
    {
      _id: ObjectId("000000000000000015209201"),
      account: {
        token: "f648023cb03a3ec2f960a32cb65ee294a5702f0b"
      }
    },
    {
      _id: ObjectId("000000000000000015209202"),
      account: {
        token: "aef862b8f5ee404c18804a99de19ecbc0c647ab6"
      }
    },
    {
      _id: ObjectId("000000000000000000000059"),
      account: {
        token: "251bf53a44774957a436b3fd0a44c612"
      }
    }
  ]);

  db.getCollection("party").insert([
    {
      _id: ObjectId("000000000000000000052305"),
      status: NumberInt("0"),
      holderId: ObjectId("000000000000000015209201")
    },
    {
      _id: ObjectId("000000000000000000052304"),
      status: NumberInt("1"),
      holderId: ObjectId("000000000000000015209202")
    },
    {
      _id: ObjectId("000000000000000000052303"),
      status: NumberInt("1"),
      holderId: ObjectId("000000000000000000000059")
    }
  ]);
  ```

- lookup 关联表

  ```javascript
  db.user.aggregate([
    {
      $lookup: {
        from: "party",
        localField: "_id",
        foreignField: "holderId",
        as: "inventory_docs"
      }
    }
  ]);
  ```

  party 表会存为 `inventory_docs` 字段

- match 筛选数据

  ```javascript
  db.user.aggregate([
    {
      $lookup: {
        from: "party",
        localField: "_id",
        foreignField: "holderId",
        as: "inventory_docs"
      }
    },
    {
      $match: {
        "inventory_docs.status": 1
      }
    }
  ]);
  ```

  筛选出 party 表中 `status` 为 1 的

- project 指定获取字段

  ```javascript
  db.user.aggregate([
    {
      $lookup: {
        from: "party",
        localField: "_id",
        foreignField: "holderId",
        as: "inventory_docs"
      }
    },
    {
      $match: {
        "inventory_docs.status": 1
      }
    },
    {
      $project: {
        _id: 0,
        "account.token": 1
      }
    }
  ]);
  ```

- limit 指定个数
  ```javascript
  db.user.aggregate([
    {
      $lookup: {
        from: "party",
        localField: "_id",
        foreignField: "holderId",
        as: "inventory_docs"
      }
    },
    {
      $match: {
        "inventory_docs.status": 1
      }
    },
    {
      $project: {
        _id: 0,
        "account.token": 1
      }
    },
    {
      $limit: 1
    }
  ]);
  ```

### 在 python 中实现

```python
import pymongo

client = pymongo.MongoClient("127.0.0.1:9527")

db = client["uki"]

lookup = {
    "$lookup": {
        "from": "party",
        "localField": "_id",
        "foreignField": "holderId",
        "as": "inventory_docs"
    }
}
match = {"$match": {"inventory_docs.status": 1}}
project = {"$project": {"_id": 0, "account.token": 1}}
limit = {"$limit": 1}

data = list(db["user"].aggregate([lookup, match, project, limit])) # 这里要注意

token = data[0]["account"]["token"]
```

### 几处报错总结

```python
data = db["user"].aggregate([]) # 这里 data 是一个 cursor object，可以转换成 list 使用
```

转换成列表

```python
data = list(db["user"].aggregate([]))
```

pymongo 里 `sort` 和在 mongo 里执行不一样  
如下 是在 mongo 中执行排序

```javascript
db.getCollection("party")
  .find({ status: 1 })
  .sort({ "sum_n.sum_4_x": 1 });
```

在 pymongo 中 `sort()` 方法接收的是一个包含元组的列表

```python
db["party"].find({"status": 1}).sort([("_id", -1)])
```

### Reference

[mongodb 多表查询(附带 pymongo 实例)](https://www.cnblogs.com/lgh344902118/p/8656266.html)
[MongoDB 关联查询](https://www.cnblogs.com/my3306/p/9712494.html)
[解决 python - command cursor' object is not subscriptable](http://www.itkeyword.com/doc/5306793514858331424/command-cursor-object-is-not-subscriptable)
[Pymongo: TypeError: if no direction is specified, key_or_list must be an instance of list](https://blog.csdn.net/HHTNAN/article/details/78968759)

**2019.10.30**
