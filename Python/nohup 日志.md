<font size=4 face='楷体'>

## 使用 nohup 运行 python 时日志不同步问题

在一次使用 nohup 后台运行 python 时，在两个模块中分别使用了 `logger` 和 `print` 输出日志
但 `print` 不同步输出，程序运行结束在日志结尾输出 `print` 的内容，而 `logger` 无影响

- 原因:

  > 这是因为 python 的输出有缓冲，导致 nohup.out 并不能够马上看到输出

- 解决:
  > python 有个 `-u` 参数，使得 python 不启用缓冲
  ```shell
  nohup python -u main.py > nohup.out 2>&1 &
  ```

之前单独用 `print` 时并无问题，这次 `print` & `nohup` 同时混用出现这种  
`-u` 参数可以解决，但依然迷惑
_待填坑_

### Reference

[nohup python程序，print无输出](https://www.cnblogs.com/sixloop/p/8488769.html)

**2019.9.24**
