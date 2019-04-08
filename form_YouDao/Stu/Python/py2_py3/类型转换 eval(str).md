<font size=4 face='楷体'>

在python中，eval() 方法是一个经常用到的函数，我们在编写输入函数的时候，需要把 input() 函数写进 eval() 方法中，这样得到的输入结果就不会是字符串类型的了。

例如： 

```python
    a=input('请输入一个数字')
    print(type(a))
```
    
这样输出的类型就会使 string 类型的，但是当：  

```python
    b=eval(input('请输入一个数字'))
    print(type(b))
```
    
```python
    >>> list1 = [1,2,3,4,5]
    >>> repr(list1)
    '[1, 2, 3, 4, 5]'
    >>> type(repr(list1))
    <type 'str'>
    >>> type(eval(repr(list)))
    <type 'list'>
    >>> a = eval(repr(list1))
    >>> a
    [1, 2, 3, 4, 5]
```

eval(str) 函数很强大，官方解释为：将字符串 str 当成有效的表达式来求值并返回计算结果。所以，结合 math 当成一个计算器很好用。

- 描述  
    eval() 函数用来执行一个字符串表达式，并返回表达式的值。
- 语法  
    以下是 eval()方法的语法:
```
    eval(expression[, globals[, locals]])
```
- 语法  
    以下是 eval() 方法的语法:  
```
    eval(expression[, globals[, locals]])
```
- 参数  
    expression -- 表达式。  
    globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。  
    locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。返回值
    返回表达式计算结果。
- 返回值
    返回表达式计算结果。  

- eval()函数常见作用有： 
  
1、计算字符串中有效的表达式，并返回结果
```python
>>> eval('pow(2,2)')
4
>>> eval('2 + 2')
4
>>> eval("n + 4")
```

2、将字符串转成相应的对象（如list、tuple、dict和string之间的转换）
```python
>>> a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
>>> b = eval(a)   字符串-列表
>>> b
[[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
>>> a = "{1:'xx',2:'yy'}"            
>>> c = eval(a)   字符串-字典
>>> c
{1: 'xx', 2: 'yy'}
>>> a = "(1,2,3,4)"
>>> d = eval(a)   字符串-元组
>>> d
(1, 2, 3, 4)
```
3、将利用 repr 函数转换的字符串再反转回对象
```python
>>> list1 = [1,2,3,4,5]
>>> repr(list1)
'[1, 2, 3, 4, 5]'
>>> type(repr(list1))
<type 'str'>
>>> type(eval(repr(list)))
<type 'list'>
>>> a = eval(repr(list1))
>>> a
[1, 2, 3, 4, 5]
```