<font size=4 face='楷体'>

## JSONDecodeError

以 'w' or 'w+' 的模式打开 json 文件时，`json.load()` 报错

```python
with open("xxx.json", 'w+', encoding='utf-8') as fn:
    data = json.load(fn)
```

报错：

> json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

原因：

> 以 'w' or 'w+' 的模式打开文件时，**打开即清空文件**，就会造成 json 模块加载的是一个空的对象，抛出错误

## Reference

[读取文件的坑](https://blog.csdn.net/longzhinuhou/article/details/86634949)

**2019.8.9**
