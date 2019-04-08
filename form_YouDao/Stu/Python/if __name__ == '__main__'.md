<font size=4 face="楷体">

---
### 这段代码的功能
一个python文件有两种使用的方法：  
- 直接作为脚本执行
- import到其他的python脚本中被调用（模块重用）执行

因此if \_\_name__ == 'main':的作用就是控制着这两种情况执行代码的过程。  
在if \_\_name__ == 'main':下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而import到其它脚本中是不会被执行的。  

---
### 运行的原理
- 每个python模块（python文件）都包含内置的变量\_\_name\_\_,当运行模块被执行的时候，\_\_name__等于文件名（包含了后缀&period;py）
- 如果import到其它模块中，则\_\_name\_\_等于模块名称（不包含后缀&period;py）
- 而\_\_main\_\_等于当前执行文件的名称（包含了后缀&period;py）  

进而当模块被直接执行时，\_\_name\_\_ == 'main'结果为真。

 
 ---
 ### [<font color=#79f>example](http://www.dengfeilong.com/post/60.html)
 
 </font>   