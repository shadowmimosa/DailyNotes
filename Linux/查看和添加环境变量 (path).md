<font size=4 face='楷体'>  

### PATH

`$PATH`: 决定了 shell 将到哪些目录中寻找命令或程序，PATH 的值是一系列的目录，当运行一个程序时，Linux 在这些目录下进行搜寻编译链接。  
    编辑你的 PATH 声明，其格式为：  
    PATH = \$PATH: <PATH 1>: <PATH 2>: <PATH 3>: ------: <PATH N>   
    你可以自己加上指定的路径，中间用冒号隔开。  
    环境变量更改后，在用户下次登陆时生效，如果想立刻生效，则可执行下面的语句：  
    `$ source .bash_profile`  
    \
    需要注意的是，最好不要把当前路径 `./` 放到 PATH 里，这样可能会受到意想不到的攻击。完成后，可以通过 `$ echo $PATH` 查看当前的搜索路径。这样定制后，就可以避免频繁的启动位于 shell 搜索的路径之外的程序了。  

- 可用 export 命令查看 PATH 值  
    [apps@vm167 ~]\$ **export**  
- 单独查看 PATH 环境变量，可用：  
    [apps@vm167 ~]\$ **echo $PATH**   
- 添加 PATH 环境变量（临时），可用：
    [apps@vm167 ~]\$ **export PATH=/usr/bin/python:\$PATH** 
    使用时替换具体路径即可  
    此方法添加的 PATH, 在终端关闭后即消失  
- 永久添加环境变量（影响当前用户）  
    \$ **vim ~/.bashrc export PATH="/usr/bin/python:$PATH"**  
- 永久添加环境变量（影响所有用户）  
    \$ **vim /etc/profile**  
    在文档最后添加：  
    `export PATH="/usr/bin/python:$PATH"`  
    保存，退出，然后运行：  
    \$ **source /etc/profile**  
    \
    不报错即成功。  

### Reference

[Linux下查看和添加环境变量](https://www.cnblogs.com/aaronLinux/p/5837702.html)  


**2018.11.23**