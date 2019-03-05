<font size=4 face='楷体'>  

## 设置 Pythonpath   

介于时常发生相对导入错误的问题，get 了新的办法 `sys.path.append()`  
关于 `sys.path.append()` , 网上有大量的用法。用的最多的就是：
```python
import sys

sys.path.append('..')
```  

理论上这条语句的操作会将上层目录加入到 pythonpath 中，然而在 Win 和 Linux 上各种尝试了很久都没实现，只是将 '..' 加到了 pythonpath 中。  

所以，干脆直接加入绝对路径  
```python
import sys, os 

sys.path.append(os.path.dirname(os.path.abspath(__file__))) # 当前文件的上层目录 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 当前文件的上两层目录 
```  

由此，就可以加入想要的路径了 XD  
不过可能有点怪，插入绝对路径、再相对导入  


### Reference

[python 环境变量设置PYTHONPATH](https://www.cnblogs.com/lifeofershisui/p/8135702.html)   


**2019.03.04**
