<font size=4 face='楷体'>

# PROMISE

promise 是一个容器，保存着某个未来才会结束的事件（异步操作）的结果。

promise 有三种状态：pending（进行中）、fulfilled（成功）和 reject（失败），只有异步操作的结果可以改变 promise 的状态。一旦 promise 从 pending 状态转化为 fulfilled 或 reject 后就不会再改变。

- ### 1. 新建一个 Promise

Promise 在新建后就会立即执行，Promise.then()方法会在当前脚本所有同步任务执行完后才会执行

```java
const promise = new Promise(function(resolve, reject) {



  //...异步操作
  if (/* 异步操作成功 */){



    resolve(value); 	// resolve将Promise的状态由pending变为resolved
  } else {



    reject(error);		// reject将Promise的状态由pending变为失败
  }
});
```

- ### 2. 用 then 方法指定 resolve 和 reject 状态的处理方法

1.  then 的两个参数分别是 resolve 和 reject 的回调函数，reject 回调不是必须的
2.  then 方法在异步操作完成后，将 Promise 的状态修改为 resolve 或 reject 后才会触发对应的回调函数

```java
promise.then(function(value) {



  // 异步操作执行成功后的处理
}, function(error) {



  // 异步操作失败的处理
});
```

- ### 3. 回调函数的参数

如果调用`resolve`函数和`reject`函数时带有参数，那么它们的参数会被传递给回调函数。

`resolve`函数的参数除了正常的值以外，还可能是另一个 Promise 实例

`p1`和`p2`都是 Promise 的实例，但是`p2`的`resolve`方法将`p1`作为参数，即一个异步操作的结果是返回另一个异步操作。

注意，这时`p1`的状态就会传递给`p2`，也就是说，`p1`的状态决定了`p2`的状态。如果`p1`的状态是`pending`，那么`p2`的回调函数就会等待`p1`的状态改变；如果`p1`的状态已经是`resolved`或者`rejected`，那么`p2`的回调函数将会立刻执行

```java
const p1 = new Promise(function (resolve, reject) {



  //三秒后返回reject
  setTimeout(() => reject(new Error('fail')), 3000)	//reject参数为错误信息ERROR
})

const p2 = new Promise(function (resolve, reject) {



  //p1的状态决定了p2的状态，后续语句便针对p1的状态
  setTimeout(() => resolve(p1), 1000)
})

//由于p1返回reject，p1又决定了p2的状态，因此触发了.catch 打印error
p2
  .then(result => console.log(result))
  .catch(error => console.log(error))
```

### 4. Promise 的 then 方法

`then`方法返回的是一个新的 Promise 对象，因此可以采用链式写法。使用链式的写法， 可以指定一组按照次序的回调函数。

```java
axios.get('“异步请求”')
  .then(function(reslut) {



  	//获取返回结果reslut
  	return reslut
	})
  .then(function(reslut) {



  	// 执行得到返回结果后相应的操作
	});
```

### 5. Promise 的 catch 方法

`catch`方法用于指定发生错误（reject）时的回调函数

```java
let promise = new Promise(
  function(resolve, reject) {



    throw new Error('test'); //reject
  }
);
promise
  .then(function(){



  //正常情况的回调resolve
	})
	.catch(function(){



  //异常情况的回调reject:test
})
```

### 6. Promise 的 finally 方法

无论 Promise 最后状态如何都会执行的方法，在 ES2018 引入。

finally()不接受任何参数，在 finally 里的方法与状态无关，finally 本质上是 then 的特例。如果不使用 finally，相当于在 then 和 catch 的方法里将 finally 的方法各写一次。

```java
promise
.then(result => {


     ···})
.catch(error => {


     ···})
.finally(() => {


     ···});
```

### 7. Promise.all()方法

将多个 Promise 实例包装为一个新的 Promise 实例。

Promise.all()接受一个数组作为参数，p1,p2, p3 都是 Promise 实例。

`const p = Promise.all([p1, p2, p3])`

p 的状态由 p1,p2,p3 决定，只有`p1`、`p2`、`p3`的状态都变成`fulfilled`，`p`的状态才会变成`fulfilled`，此时`p1`、`p2`、`p3`的返回值组成一个数组，传递给`p`的回调函数。

只要`p1`、`p2`、`p3`之中有一个被`rejected`，`p`的状态就变成`rejected`，此时第一个被`reject`的实例的返回值，会传递给`p`的回调函数。

```java
const databasePromise = connectDatabase();

const booksPromise = databasePromise
  .then(findAllBooks);

const userPromise = databasePromise
  .then(getCurrentUser);

Promise.all([
  booksPromise,
  userPromise
])
.then(([books, user]) => pickTopRecommendations(books, user));
```

### 8. Promise.race()

`const p = Promise.race([p1, p2, p3]);`

Race()与 all 方法参数一致，但是 race 只要`p1`、`p2`、`p3`之中有一个实例率先改变状态，`p`的状态就跟着改变。那个率先改变的 Promise 实例的返回值，就传递给`p`的回调函数。

### 9.Promise.resolve()

将现有对象转化为 Promise 对象

```java
const jsPromise = Promise.resolve($.ajax('/whatever.json'));
```

上面代码将 jQuery 生成的`deferred`对象，转为一个新的 Promise 对象。

（1）参数是一个 Promise 实例

如果参数是 Promise 实例，那么`Promise.resolve`将不做任何修改、原封不动地返回这个实例。

（2）参数是一个`thenable`对象

`Promise.resolve`方法会将这个对象转为 Promise 对象，然后就立即执行`thenable`对象的`then`方法。

（3）参数不是具有`then`方法的对象，或根本就不是对象

如果参数是一个原始值，或者是一个不具有`then`方法的对象，则`Promise.resolve`方法返回一个新的 Promise 对象，状态为`resolved`。

（4）不带有任何参数

`Promise.resolve()`方法允许调用时不带参数，直接返回一个`resolved`状态的 Promise 对象。

### 10. Promise.reject()

`Promise.reject(reason)`方法也会返回一个新的 Promise 实例，该实例的状态为`rejected`。

```java
const p = Promise.reject('出错了');
// 等同于
const p = new Promise((resolve, reject) => reject('出错了'))

p.then(null, function (s) {



  console.log(s)
});
// 出错了
```

上面代码生成一个 Promise 对象的实例`p`，状态为`rejected`，回调函数会立即执行。

注意，`Promise.reject()`方法的参数，会原封不动地作为`reject`的理由，变成后续方法的参数。这一点与`Promise.resolve`方法不一致。

```java
const thenable = {



  then(resolve, reject) {



    reject('出错了');
  }
};

Promise.reject(thenable)
.catch(e => {



  console.log(e === thenable)
})
// true
```

上面代码中，`Promise.reject`方法的参数是一个`thenable`对象，执行以后，后面`catch`方法的参数不是`reject`抛出的“出错了”这个字符串，而是`thenable`对象。

================================================================

在 JavaScript 中需要在数组中循环调用异步方法，又需要等待上一轮异步方法的执行结果才能继续，因此我们需要使用 Promise 来完成调用异步方法的顺序执行。

## 方式一

```java
let usePromise = async()=>{



  let result = [], array = [1,2,3,4] // array作为循环遍历用
 	let pro

  //开始循环遍历
  array.forEach(element=>{



    pro = new Promise(resolve=>{



      //setTimeout代表异步方法，等待一秒后执行
			setTimeout(()=>{



        result.push(element);
        resolve();
      }, 1000);
    })
  })
  await pro;
  console.log(result); 	// [1,2,3,4]
}
```

## 方式二

```java
let array1 = [1]

function prom1 (){



  return new Promise(function(resovle){



    setTimeout(()=>{



      array1.push('a');
      resovle(array1);
    }, 1000);
  })
}

function prom2 (){



  return new Promise(function(resovle){



    setTimeout(()=>{



      array1.push('b');
      resovle(array1);
    }, 1000);
  })
}

function prom3 (){



  return new Promise(function(resovle){



    console.log(array1)
  })
}

let pro = new Promise(function(resolve, reject){



  resolve();
})

pro.then(prom1)
	 .then(prom2)
	 .then(prom3)	// [1, a, b]
```

## 方式三

以下代码功能： 获取一个 URL 数组，通过 for 循环依次访问数组中的各个 URL 地址，进入各个 URL 页面的子页面获取数据，当一个页面的所有数据都获取到并处理完毕，才会进入下一个 for 循环的异步请求访问新的 URL 页面请求数据。

```java
let array =[1,2,3,4];
let p = Promise.resolve();

for (let i = 0; i < array.length; i ++){



  p = p.then(_=>new Promise(resolve=>{



    //异步方法，发送http的GET请求获取数据
    superagent.get(bookUrl[i]).end(async(err, res) => {



                if (err) {



                    console.log("err",err);
                    return
                } else {



                    let $ = cheerio.load(res.text);
                    bookName.push($('div.book-info').find('h1').find('em').text())
                    let readURL = $('div.book-info').find('a#readBtn').attr('href');
                  			//异步方法，获取数据中的请求路由
                        superagent.get("https:"+readURL).end((err, res)=>{



                            if(err){



                                console.log(err);
                              	//reject(); 使用reject需要在new Promise传入该参数，并有.catch方法
                            }else{



                                let $ = cheerio.load(res.text);
                                content.push($('div.read-content').find('p').text());
                                if($('div.read-content').find('p').text()!=="")  {



                                  	// 当resolve时此次方法调用才算完成，才会进入下次循环发送交易
                                    resolve(content)
                                }
                            }
                        })

                }
            })
  	}))
}

p.then(function(){



  doSomething();
})

=============================>>>
//大体框架
let p = Promise.resolve();
array.forEach((value,index, array)=>{



  p= p.then(_=>{


     new Promise(resolve)=>{



    doSomething({



      ...
      resolve();
    })
  }})
})
p.then(function(){



  doSomething...
})
```

### Reference

[使用 Promise 将异步转化为同步执行](https://blog.csdn.net/weixin_45987920/article/details/107094382)

**2022.08.17**
