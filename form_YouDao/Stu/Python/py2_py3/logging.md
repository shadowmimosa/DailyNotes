<font size=4 face='楷体'>  

- logging日志基本格式化
```python
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
```
```
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='new.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
```

- 打印日志
```python
logging.debug('debug 信息')
logging.info('info 信息')
logging.warning('warning 信息')
logging.error('error 信息')
logging.critical('critial 信息')
```
> 这种打印日志需要将日志格式化放在首次调用的位置，一旦格式化执行执行后，其余格式化将不再执行  
[Link](https://www.cnblogs.com/nancyzhu/p/8551506.html)  

> 如需要多个日志输出则需要使用动态输出日志  
[Link](http://www.voidcn.com/article/p-whoikwnb-bhx.html)


