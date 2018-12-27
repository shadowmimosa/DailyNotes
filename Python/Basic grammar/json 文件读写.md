<font size=4 face='楷体'>  

### json 文件的读取与写入

- 写入
```python
model={} #数据
with open("./demo.json",'w',encoding='utf-8') as json_file:
    json.dump(model,json_file,ensure_ascii=False)
```

- 读取
```python 
model={} #存放读取的数据
with open("./hmm.json",'r',encoding='utf-8') as json_file:
    model=json.load(json_file)
```

关于 json 的 load, loads; dump, dumps.  
有待系统的整理学习

**2018.12.25**