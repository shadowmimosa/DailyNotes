<font size=4 face='楷体'>  

Python OSError: [Errno 22] Invalid argument:错误
1. 应为读取文件错误  
    注意检查文件路径，尤其是 '\\' & '/';  
    建议路径都使用 '\\\\' 或者 '/', 避免引入找不到路径的问题。  
    详见[这里](https://blog.csdn.net/u012561176/article/details/82107350)  

