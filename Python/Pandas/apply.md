<font size=4 face='楷体'>

## pandas 中 apply 使用

```python
apply(func [, args [, kwargs ]])
'''
args: 是一个包含将要提供给函数的按位置传递的参数的元组。如果省略了args，任 何参数都不会被传递
kwargs: 是一个包含关键字参数的字典
'''
```

- 遍历修改某行
  ```python
  df = df['age'].apply(lambda x : 1 if x >18 else 0)
  ```

### Reference

[Pandas 详解二十六之 Apply--对行、列用函数处理](https://blog.csdn.net/weixin_38168620/article/details/82312617)
[pandas 数据处理里最好用的函数 apply+lambda](https://blog.csdn.net/mochou111/article/details/95311065)

**2019.10.28**
