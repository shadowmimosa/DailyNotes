<font size=4 face='楷体'>

## sqlite3 使用

一、安装 sqlite3

```java
npm install sqlite3 –save
```

二、编写建表脚本，导入数据库

```javascript
//  建表脚本，导出db对象供之后使用
import fse from 'fs-extra'
import path from 'path'
import sq3 from 'sqlite3'

export const dbPath = path.join(__dirname, '/library/seed.db')
fse.ensureFileSync(dbPath)

const sqlite3 = sq3.verbose()
const seedDB = new sqlite3.Database(dbPath)
seedDB.serialize(() => {
  /**
   * 上传任务列表 upload_table
   * ID 任务id
   * FileCount 文件数量
   * Status 任务状态
   * CreateDate 任务创建日期
   * SuccessDate 任务完成日期
   */
  seedDB.run(
    `CREATE TABLE "upload_table" (
    "ID"  INTEGER NOT NULL,
    "FileCount"  INTEGER NOT NULL,
    "Status"  INTEGER NOT NULL,
    "CreateDate"  TEXT,
    "SuccessDate"  TEXT,
    PRIMARY KEY ("ID")
    )`,
    (err) => {
      console.log(err)
    }
  )

  /**
   * 下载任务列表 download_table
   * ID 任务id
   * FileCount 文件数量
   * Status 任务状态
   * CreateDate 任务创建日期
   * SuccessDate 任务完成日期
   */
  seedDB.run(
    `CREATE TABLE "download_table" (
    "ID"  INTEGER NOT NULL,
    "FileCount"  INTEGER NOT NULL,
    "Status"  INTEGER NOT NULL,
    "CreateDate"  TEXT,
    "SuccessDate"  TEXT,
    PRIMARY KEY ("ID")
    )`,
    (err) => {
      console.log(err)
    }
  )
})

export default {
  seedDB,
}
```

三、导入数据存储

将数据存储导入到 src/renderer/main.js 里，并将其附加到 Vue 的原型（prototype）上。后续通过在所有组件文件中使用 this.$db，就可以访问数据存储的 API。

```javascript
import Vue from 'vue'
import axios from 'axios'

import App from './App'
import router from './router'
import store from './store'

//  新添加
//------------------------------------------------
import ElementUI, { Button, Select, Tabs, Table } from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

//  本地数据库
import db from './datastore'
Vue.prototype.$seeddb = db.seedDB
//------------------------------------------------

if (!process.env.IS_WEB) Vue.use(require('vue-electron'))
Vue.http = Vue.prototype.$http = axios
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  components: { App },
  router,
  store,
  template: '<App/>',
}).$mount('#app')
```

四、在组件中使用数据库

serialize 可以使内部的 sql 语句都顺序执行。node 的函数都是异步的，所以这个函数应该多多重点使用。

```javascript
//  更新上传列表
updateUploadList() {
  this.tableUploadData = [];

  var temp = this.tableUploadData;
  this.$seeddb.serialize(() => {
    this.$seeddb.all('select * from [upload_table]', function(err, res) {
      res.forEach(function(obj, index, arr) {
        temp.push({
          mission_id: obj.ID,
          count: '2/3',
          process: '80%',
          status: obj.Status
        });
      });
    });
  });
}
```

五、遇到的问题

![](https://img2020.cnblogs.com/blog/1055709/202012/1055709-20201224155120576-2103820924.png)

提示在 node_modules\\sqlite3\\lib\\binding\\electron-v2.0-win32-x64 下 cannot find mudule，去 binding 下找不到 electroon-v1.4-win32-x64 文件夹，原因是 npm install 时加载 package.json 时会在 node_modules 下安装原生 sqlite3 模块，binding 下会产生一个类似 node-v64-win32-x64 的文件夹，需要做的是编译产生 node_modules\\sqlite3\\lib\\binding\\ electron-v2.0-win32-x64 路径，手动修改并不能解决问题，需要重新手动编译。

进入 node_modules\\sqlite3 文件夹，运行以下命令：

```bash
npm install nan –save
node-gyp configure --module_name=node_sqlite3 --module_path=../lib/ electron-v2.0-win32-x64
node-gyp rebuild --target=2.0.4 --arch=x64 --target_platform=win32 --dist-url=https://npm.taobao.org/mirrors/atom-shell --module_name=node_sqlite3 --module_path=../lib/binding/ electron-v2.0-win32-x64
```

注意：

1. --target 指的是 Electron 的版本号

2. 最后的部分，一定要跟红色框上的路径保持一致!

3. 如果执行到对应的 sql 语句还是报错，并错误原因跟 NODE_MODULE_VERSION 有关，大意是 version 不匹配，则运行以下命令重新并编译即可。

```bash
npm install --save-dev electron-rebuild
.\node_modules\.bin\electron-rebuild.cmd
```

### [demo](https://github.com/luwanquan/electron-vue-sqlite3-demo/blob/master/src/utils/db.js)

```javascript
const sqlite3 = require('sqlite3').verbose()
let db

// 连接数据库
function conn() {
  if (!db || !db.open) {
    db = new sqlite3.Database('base.db')
  }
  return db
}

// 初始化数据表
export const initTable = () => {
  return new Promise((resolve, reject) => {
    let db = conn()
    db.serialize(() => {
      db.run(
        'CREATE TABLE if not exists TreeTable (id int primary key, name varchar(64), fatherId int)'
      )
      db.run(
        'CREATE TABLE IF NOT EXISTS ProductTable (id int primary key, name varchar(64))'
      )
      resolve()
    })
  })
}

export const queryAllTree = () => {
  return new Promise((resolve, reject) => {
    let db = conn()
    db.all(
      'select id, name, fatherId from TreeTable order by fatherId',
      (err, rows) => {
        if (err) reject(err)
        resolve(rows || [])
      }
    )
  })
}

export const queryAllProduct = () => {
  return new Promise((resolve, reject) => {
    let db = conn()
    db.all('select id, name from ProductTable', (err, rows) => {
      if (err) reject(err)
      resolve(rows || [])
    })
  })
}

export const insertProduct = (product) => {
  return new Promise((resolve, reject) => {
    let db = conn()
    let prepare = db.prepare(
      'replace into ProductTable (id, name) values (?, ?)'
    )
    prepare.run(product.id, product.name)
    prepare.finalize((err) => {
      if (!err) resolve()
    })
  })
}
```

### Reference

[Electron-Vue 调用本地数据库](https://www.cnblogs.com/zerotoinfinity/p/14184576.html)

**2022.08.18**
