<font size=4 face='楷体'>

## thinker 基础使用

### scrollbar 回调事件

```python
# https://stackoverflow.com/questions/18839464/python-tkinter-want-to-call-a-function-when-scrollbar-clicked-in-scrolledtext/18839674#18839674

from Tkinter import *

def yscroll(*args):
    print('yscroll: {}'.format(args))
    scrollbar.set(*args)

def yview(*args):
    print('view: {}'.format(args))
    textbox.yview(*args)

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
textbox = Text(root, yscrollcommand=yscroll)
for i in range(1000):
    textbox.insert(END, '{}\n'.format(i))
textbox.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=yview)
mainloop()
```

### Combobox 禁用输入

```python
# https://www.thinbug.com/q/44959253

# state 设置为 "readonly"
cb = ttk.Combobox(root, state="readonly",
                  values=("one", "two", "three"))
```

### Entry 默认值

ttk 小部件对垃圾收集更敏感

```python
# https://www.cnpython.com/qa/291903

box = ttk.Entry(self.mainframe)
box.insert(0, arg.get("default", "")
```

### 向 Button 传递参数

[Reference](https://zhuanlan.zhihu.com/p/475384940)

#### 通过 partials 向 Tkinter 按钮命令传递参数

可以通过使用 functools 模块中的 partial 对象来传递参数

```python
from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk

from functools import partial



app = tk.Tk()
labelExample = tk.Button(app, text="0")

def change_label_number(num):
    counter = int(str(labelExample['text']))
    counter += num
    labelExample.config(text=str(counter))

buttonExample = tk.Button(app, text="Increase", width=30,
                          command=partial(change_label_number, 2))

buttonExample.pack()
labelExample.pack()
app.mainloop()
```

```python
buttonExample = tk.Button(app, text="Increase", width=30,
                          command=partial(change_label_number, 2))
```

`partial(change_label_numer, 2)` 返回了一个可以来调用的对象, 在引用的时候它跟一个函数 func 很类似

#### 通过 lambda 函数向 Tkinter 按钮命令传递参数

也可以通过 Python 的 lambda 操作符或者函数来创建一个临时的、一次性的简单函数用以按钮被按下时候来调用

```python
from sys import version_info
if version_info.major == 2:
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk



app = tk.Tk()
labelExample = tk.Button(app, text="0")

def change_label_number(num):
    counter = int(str(labelExample['text']))
    counter += num
    labelExample.config(text=str(counter))

buttonExample = tk.Button(app, text="Increase", width=30,
                          command=lambda: change_label_number(2))

buttonExample.pack()
labelExample.pack()
app.mainloop()
```

lambda 函数的语法如下

```python
lambda: argument_list: expression
```

```python
buttonExample = tk.Button(app, text="Increase", width=30,
                          command=lambda: change_label_number(2))
```

#### 使用 StringVar()和 Entry textvariable 对参数进行绑定


### Reference

[pip 换国内源以及设置代理](https://blog.csdn.net/yueludanfeng/article/details/104584398)

**2022.07.27**