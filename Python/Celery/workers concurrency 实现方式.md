<font size=4 face='楷体'>

## Celery - Workers 并发(Concurrency)实现方式

### 原理

当 Celery 启动一个 Worker 时, 这个 Worker 会与 Broker 建立链接（tcp 长链接）, 然后如果有数据传输, 则会创建相应的 channel, 这个连接可以有多个 channel.然后, Worker 就会去 borker 的队列里面取相应的 task 来进行消费了, 这也是典型的消费者生产者模式.

其中, 这个 worker 主要是有四部分组成的, task_pool, consumer, scheduler, mediator.task_pool 主要是用来存放的是一些 worker, 当启动了一个 worker, 并且提供并发参数的时候, 会将一些 worker 放在这里面.

celery 默认的并发方式是 prefork,也就是多进程的方式, 这里只是 celery 对 multiprocessing.Pool 进行了轻量的改造, 然后给了一个新的名字叫做 prefork, 这个 pool 与多进程的进程池的区别就是这个 task_pool 只是存放一些运行的 worker.consumer 也就是消费者, 主要是从 broker 那里接受一些 message,然后将 message 转化为 celery.worker.request.Request 的一个实例.并且在适当的时候, 会把这个请求包装进 Task 中, Task 就是用装饰器 app_celery.task() 装饰的函数所生成的类, 所以可以在自定义的任务函数中使用这个请求参数, 获取一些关键的信息.

### Workers 类型

#### Solo
Solo 池是一个內联池(inline pool)，意味着，任务不会同时处理，其只是创建一个线程(thread) 并使用该线程执行任务.
  
- 使用方式
  ```bash
  celery -A tasks worker --pool=solo --loglevel=info
  ```
- 适用场景

  Solo适用需要逐一执行(one by one)的任务. 不过，实际中不使用并发而仅使用 solo pool 的场景不多.

#### Prefork
Prefork 池是 Celery 对 Python 标准库 multiprocess 的改造，其能够同时处理多个任务.

- 使用方式
  ```bash
  celery -A tasks worker --pool=prefork --concurrency=4 --loglevel=info
  ```
- 适用场景
  CPU密集型(CPU-bound)，即，任务的大部分时间主要是 CPU 计算；只有 CPU 越快时才会速度更快.
  CPU密集型任务如：文件转换、压缩、搜索算法等.

#### Eventlet & Gevent
Eventlet & Gevent 池使用协程(coroutlines，也被称为绿色线程，green threads) 来执行任务，不是产生传统线程. 能够同时处理多个任务.

- Eventlet Pool 使用方式
  ```bash
  celery -A tasks worker --pool=eventlet --concurrency=500 --loglevel=info
  ```
- Gevent Pool 使用方式
  ```bash
  celery -A tasks worker --pool=gevent --concurrency=500 --loglevel=info
  ```
- 适用场景
  I/O 密集型任务，即，任务的主要瓶颈是 I/O 操作的等待时间. 与 Prefork 不同的是，其可以设置并发高的数量，而不受限于 CPUs 的数量.
  I/O密集型任务如，邮件发送、API请求等.

## Reference

[Celery - Workers并发(Concurrency)实现方式](http://aiuai.cn/aifarm2045.html)

**2023.06.14**
