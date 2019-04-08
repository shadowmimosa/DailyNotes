<font size=4 face='楷体'>  

#### logging.logger & logging.handler  

典型的日志记录步骤：  

- 创建 logger  
- 创建 handler  
- 定义 formatter  
- 给 handler 添加 formatter  
- 给 logger 添加 handler  

代码：
```python
import logging 

# 1、创建一个logger 
logger = logging.getLogger('mylogger') 
logger.setLevel(logging.DEBUG) 

# 2、创建一个handler，用于写入日志文件 
fh = logging.FileHandler('test.log') 
fh.setLevel(logging.DEBUG) 

# 再创建一个handler，用于输出到控制台 
ch = logging.StreamHandler() 
ch.setLevel(logging.DEBUG) 

# 3、定义handler的输出格式（formatter）
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 

# 4、给handler添加formatter
fh.setFormatter(formatter) 
ch.setFormatter(formatter) 

# 5、给logger添加handler 
logger.addHandler(fh)
logger.addHandler(ch)
```

