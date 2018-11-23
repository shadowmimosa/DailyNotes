<font size=4 face='楷体'>  

## Python2 & Python coexist on Linux  

### 为什么需要两个版本的 Python  

在前一阵子，一直在忙着将公司的测试用例从 Python2 迁到 Python3, 前几天才终于完成了，所有三百多个测试用例终于能在我本地的 Python3 环境下跑通了。  
改别人的东西很煎熬，也学到不少东西。  
接下来的任务就是把改好的用例部署在 Jenkins 服务器上，需要安装 Python3 环境，**但不能影响现有的 Python2 下的运行环境**。   
于是就有了两个版本并存的需求。  

### 

在 Windows 中，可以[这样](http://www.cnblogs.com/weswes/p/9896312.html)  
暂时还没有在 Windows 下并存的需要，方法有待验证