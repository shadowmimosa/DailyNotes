<font size=4 face='楷体'>

## concurrent 模块基本使用

### Python 标准模块

[concurrent.futures 官方文档](https://docs.python.org/dev/library/concurrent.futures.html)

### 介绍

concurrent.futures 模块提供了高度封装的异步调用接口

- ThreadPoolExecutor: 线程池，提供异步调用
- ProcessPoolExecutor: 进程池，提供异步调用
  两者都实现相同的接口，该接口由抽象 Executor 类定义

### 基本方法

`submit(fn, *args, **kwargs)`: 异步提交任务
`map(func, *iterables, timeout=None, chunksize=1)`: 取代 for 循环 submit 的操作
`shutdown(wait=True)`: 相当于进程池的 pool.close()+pool.join()操作

- wait=True，等待池内所有任务执行完毕回收完资源后才继续
- wait=False，立即返回，并不会等待池内的任务执行完毕
  但不管 wait 参数为何值，整个程序都会等到所有任务执行完毕
  submit 和 map 必须在 shutdown 之前

`result(timeout=None)`: 取得结果
`add_done_callback(fn)`: 回调函数
`done()`: 判断某一个线程是否完成
`cancle()`: 取消某个任务

### ProcessPoolExecutor

```python
# 介绍
"""
The ProcessPoolExecutor class is an Executor subclass that uses a pool of
processes to execute calls asynchronously. ProcessPoolExecutor uses the
multiprocessing module, which allows it to side-step the Global Interpreter
Lock but also means that only picklable objects can be executed and returned.

class concurrent.futures.ProcessPoolExecutor(max_workers=None, mp_context=None)
An Executor subclass that executes calls asynchronously using a pool of at most
max_workers processes. If max_workers is None or not given, it will default to
the number of processors on the machine. If max_workers is lower or equal to 0,
then a ValueError will be raised.
"""

# 用法
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

import os,time,random
def task(n):
    print('%s is runing' %os.getpid())
    time.sleep(random.randint(1,3))
    return n**2

if __name__ == '__main__':

    executor=ProcessPoolExecutor(max_workers=3)

    futures=[]
    for i in range(11):
        future=executor.submit(task,i)
        futures.append(future)
    executor.shutdown(True)
    print('+++>')
    for future in futures:
        print(future.result())
```

### ThreadPoolExecutor

```python
# 用法
与ProcessPoolExecutor相同
```

### map 的用法

```python
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

import os,time,random
def task(n):
    print('%s is runing' %os.getpid())
    time.sleep(random.randint(1,3))
    return n**2

if __name__ == '__main__':

    executor=ThreadPoolExecutor(max_workers=3)

    # for i in range(11):
    #     future=executor.submit(task,i)

    executor.map(task,range(1,12)) #map取代了for+submit
```

### 回调函数

```python
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from multiprocessing import Pool
import requests
import json
import os

def get_page(url):
    print('<进程%s> get %s' %(os.getpid(),url))
    respone=requests.get(url)
    if respone.status_code == 200:
        return {'url':url,'text':respone.text}

def parse_page(res):
    res=res.result()
    print('<进程%s> parse %s' %(os.getpid(),res['url']))
    parse_res='url:<%s> size:[%s]\n' %(res['url'],len(res['text']))
    with open('db.txt','a') as f:
        f.write(parse_res)


if __name__ == '__main__':
    urls=[
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'
    ]

    # p=Pool(3)
    # for url in urls:
    #     p.apply_async(get_page,args=(url,),callback=pasrse_page)
    # p.close()
    # p.join()

    p=ProcessPoolExecutor(3)
    for url in urls:
        p.submit(get_page,url).add_done_callback(parse_page) #parse_page拿到的是一个future对象obj，需要用obj.result()拿到结果
```

### Reference

[Python 程序中的线程操作-concurrent 模块](https://www.cnblogs.com/Dr-wei/p/11852447.html)
[Python 程序中的线程操作-concurrent 模块](https://www.cnblogs.com/Lin2396/p/11568457.html)

**2020.09.17**
