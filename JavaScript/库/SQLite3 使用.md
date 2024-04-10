<font size=4 face='楷体'>

## NodeJS 中使用 SQLite3

### SQLite 简介

sqlite 是一款轻量级的数据库, sqlite 的第一个版本是 2000 年就发布了的, 经过十多年的历练, 显然 sqlite 目前已经相当成熟. sqlite 最大的特点就是没有任何数据库服务器, 无论是 C、java、node.js, 只需要相应的驱动, 就可以直接对数据库进行读写, 速度是相当的快. 相比之下, 其他的 sql 数据库必须启动一个服务, 而且还要安装、配置, sqlite 简洁的令人感动.

### Node.js 安装 sqlite3 模块

和其他语言一样, node.js 仍然只需要一个 module 就可以对 sqlite 进行操作了.

```bash
npm find sqlite
```

发现 sqlite 的模块居然有几十个, 足见 node.js 目前的火爆程度, 小小的 sqlite 就有这么多可用模块.
其中一个就叫做 sqlite3, 解释如下:

> sqlite3 Asynchronous, non-blocking SQLite3 bindings 异步, 非阻塞 sqlite3 绑定.

node.js 最大的特点就是异步, 这款 sqlite 的驱动太符合 node 的核心思想了, 经过与其他模块的比较, 最终还是选择了这款.

```bash
npm install sqlite3
```

就将 sqlite 的驱动安装进来了.

### 调用 SQLite3 的接口

```javascript
1.  var sqlite3 = require('sqlite3');
2.  var db = new sqlite3.Database('/tmp/1.db',function() {
3.    db.run("create table test(name varchar(15))",function(){
4.      db.run("insert into test values('hello,world')",function(){
5.        db.all("select * from test",function(err,res){
6.          if(!err)
7.            console.log(JSON.stringify(res));
8.          else
9.            console.log(err);
10.       });
11.     })
12.   });
13. });
```

执行:

```bash
node test.js
[{"name":"hello,world"}]
```

插入的时候使用`db.run()`, 查询的时候使用`db.all()`
由于是异步, 必须在执行 sql 后注册回调函数, 这样如果连续执行几十条 sql, 那代码就跟楼梯差不多了. 但这就是 node 的特点, 所以还是要慢慢适应.

### 引入 SQLite3 模块

```javascript
1.  var fs = require('fs');
2.  var file = 'test.db';//这里写的就是数据库文件的路径
3.  var exists = fs.existsSync(file);
4.  var sqlite3 = require('sqlite3').verbose();
5.  var db = new sqlite3.Database(file);
```

### 增删改查操作

```javascript
1. //增
2. var sql1 = db.prepare("insert into 表名 values (内容, 跟mysql一样)");
3. sql1.run();
4. //删
5. var sql2 = db.prepare("delete from 表名 where id = 1");
6. sql2.run();
7. //改
8. var sql3 = db.prepare("update 表名 set name = winston where id = 1");
9. sql3.run();
10. //查
11. //查一个表的所有数据
12. db.all("select * from 表名",function(err,row){
13.     console.log(JSON.stringify(row));
14. })
15. //查一条数据
16. db().each("select * from 表名",function(err,row){
17.      console.log(row);
18. })
```

### SQLite3 API 介绍

在 nodejs 的模块安装模块下, 进入 sqlite3/lib 目录下, 打开 sqlite3.js 文件查看, 操作数据库主要是用 Database, Database 相关的函数有: run、prepare、each、get、all、exec、map 和 close.

### Database

- 用法: `new sqlite3.Database(filename,[mode],[callback])`.
- 功能: 返回数据库对象并且自动打开和连接数据库, 它没有独立打开数据库的方法.

close

- 用法: `close([callback])`.
- 功能: 关闭和释放数据库对象.

run

- 用法: `run(sql,param,...],[callback])`.
- 功能: 运行指定参数的 SQL 语句, 完成之后调用回调函数, 它不返回任何数据, 在回调函数里面有一个参数, SQL 语句执行成功, 则参数的值为 null,反之为一个错误的对象, 它返回的是数据库的操作对象. 在这个回调函数里面当中的 this,里面包含有 lastId(插入的 ID)和 change(操作影响的行数,如果执行 SQL 语句失败, 则 change 的值永远为 0).

get

- 用法: `get(sql,[param,...],[callback])`.
- 功能: 运行指定参数的 SQL 语句, 完成过后调用回调函数. 如果执行成功, 则回调函数中的第一个参数为 null,第二个参数为结果集中的第一行数据, 反之则回调函数中只有一个参数, 只参数为一个错误的对象.

all

- 用法: `all(sql,[param,...],[callback])`.
- 功能: 运行指定参数的 SQL 语句, 完成过后调用回调函数. 如果执行成功, 则回调函数中的第一个参数为 null,第二个参数为查询的结果集, 反之, 则只有一个参数, 且参数的值为一个错误的对象.

prepare

- 用法: `prepare(sql,[param,...],[callback])`.
- 功能: 预执行绑定指定参数的 SQL 语句, 返回一个 Statement 对象, 如果执行成功, 则回调函数的第一个参数为 null,反之为一个错误的对象.

### 具体事例

由于 sqlite3 API 具体使用过程中重复代码量较多, 所以进行了简单封装, 在使用过程中如果第一次创建数据库和表, 紧接着插入数据的话, 可能导致表还未创建完成就查询出现错误（Nodejs 是基于异步的且顺序不可控）, 所以在表创建和插入数据时使用同步方式操作来保证表已经存在. 封装的代码如下:

```javascript
1.  var fs = require('fs');
2.  var sqlite3 = require('sqlite3').verbose();
3.
4.  var DB = DB || {};
5.
6.  DB.SqliteDB = function(file){
7.      DB.db = new sqlite3.Database(file);
8.
9.      DB.exist = fs.existsSync(file);
10.     if(!DB.exist){
11.         console.log("Creating db file!");
12.         fs.openSync(file, 'w');
13.     };
14. };
15.
16. DB.printErrorInfo = function(err){
17.     console.log("Error Message:" + err.message + " ErrorNumber:" + errno);
18. };
19.
20. DB.SqliteDB.prototype.createTable = function(sql){
21.     DB.db.serialize(function(){
22.         DB.db.run(sql, function(err){
23.             if(null != err){
24.                 DB.printErrorInfo(err);
25.                 return;
26.             }
27.         });
28.     });
29. };
30.
31. /// tilesData format; [[level, column, row, content], [level, column, row, content]]
32. DB.SqliteDB.prototype.insertData = function(sql, objects){
33.     DB.db.serialize(function(){
34.         var stmt = DB.db.prepare(sql);
35.         for(var i = 0; i < objects.length; ++i){
36.             stmt.run(objects[i]);
37.         }
38.
39.         stmt.finalize();
40.     });
41. };
42.
43. DB.SqliteDB.prototype.queryData = function(sql, callback){
44.     DB.db.all(sql, function(err, rows){
45.         if(null != err){
46.             DB.printErrorInfo(err);
47.             return;
48.         }
49.
50.         /// deal query data.
51.         if(callback){
52.             callback(rows);
53.         }
54.     });
55. };
56.
57. DB.SqliteDB.prototype.executeSql = function(sql){
58.     DB.db.run(sql, function(err){
59.         if(null != err){
60.             DB.printErrorInfo(err);
61.         }
62.     });
63. };
64.
65. DB.SqliteDB.prototype.close = function(){
66.     DB.db.close();
67. };
68.
69. /// export SqliteDB.
70. exports.SqliteDB = DB.SqliteDB;
```

针对以上封装接口的调用代码如下:

```javascript
1.  /// Import SqliteDB.
2.  var SqliteDB = require('./sqlite.js').SqliteDB;
3.  var file = "Gis1.db";
4.  var sqliteDB = new SqliteDB(file);
5.
6.  /// create table.
7.  var createTileTableSql = "create table if not exists tiles(level INTEGER, column INTEGER, row INTEGER, content BLOB);";
8.  var createLabelTableSql = "create table if not exists labels(level INTEGER, longitude REAL, latitude REAL, content BLOB);";
9.  sqliteDB.createTable(createTileTableSql);
10. sqliteDB.createTable(createLabelTableSql);
11.
12. /// insert data.
13. var tileData = [[1, 10, 10], [1, 11, 11], [1, 10, 9], [1, 11, 9]];
14. var insertTileSql = "insert into tiles(level, column, row) values(?, ?, ?)";
15. sqliteDB.insertData(insertTileSql, tileData);
16.
17. /// query data.
18. var querySql = 'select * from tiles where level = 1 and column >= 10 and column <= 11 and row >= 10 and row <=11';
19. sqliteDB.queryData(querySql, dataDeal);
20.
21. /// update data.
22. var updateSql = 'update tiles set level = 2 where level = 1 and column = 10 and row = 10';
23. sqliteDB.executeSql(updateSql);
24.
25. /// query data after update.
26. querySql = "select * from tiles where level = 2";
27. sqliteDB.queryData(querySql, dataDeal);
28. sqliteDB.close();
29.
30. function dataDeal(objects){
31.     for(var i = 0; i < objects.length; ++i){
32.         console.log(objects[i]);
33.     }
34. }
```

### Reference

[NodeJS 中使用 SQLite3](https://www.jianshu.com/p/33b132078b05)

**2022.10.13**
