<font size=4 face='楷体'>

## python 中的 classmethod 与 staticmethod

- staticmethod
  只要要定义的方法里不涉及到 self 参数, 就用静态方法承担, 因为这样就表明这个方法和本身的类没有关系, 明确的区别出类相关和不相关
- classmethod
  在实例化之前就需要先和类做一定的交互, 这种交互可能会影响实际实例化的过程, 所以必须放在调用构造函数之前

### Reference

[python中的classmethod与staticmethod](https://www.jb51.net/article/234598.htm)

**2023.06.28**
