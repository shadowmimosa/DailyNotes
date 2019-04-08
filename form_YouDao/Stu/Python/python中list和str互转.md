<font size=4 face='楷体'>

1. list转str

假设有一个名为test_list的list，转换后的str名为test_str  
则转换方法：  
test_str = "".join(test_list)

需要注意的是该方法需要list中的元素为字符型，若是整型，则需要先转换为字符型后再转为str类型。

2. str转list

假设有一个名为test_str的str，转换后的list名为test_list  
则转换方法：  
test_list=list(test_str)

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。  

[链接](http://www.cnblogs.com/klb561/p/9211268.html)
