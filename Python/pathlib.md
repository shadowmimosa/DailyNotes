<font size=4 face='楷体'>

## 文件操作 pathlib 模块

在 Python 3.4, 标准库添加了新的模块 - pathlib  
可替代 os.path 文件操作

| os and os.path          | pathlib                                             |
| ----------------------- | --------------------------------------------------- |
| os.path.abspath()       | Path.resolve()                                      |
| os.chmod()              | Path.chmod()                                        |
| os.mkdir()              | Path.mkdir()                                        |
| os.makedirs()           | Path.mkdir()                                        |
| os.rename()             | Path.rename()                                       |
| os.replace()            | Path.replace()                                      |
| os.rmdir()              | Path.rmdir()                                        |
| os.remove(),os.unlink() | Path.unlink()                                       |
| os.getcwd()             | Path.cwd()                                          |
| os.path.exists()        | Path.exists()                                       |
| os.path.expanduser()    | Path.expanduser() and Path.home()                   |
| os.listdir()            | Path.iterdir()                                      |
| os.path.isdir()         | Path.is_dir()                                       |
| os.path.isfile()        | Path.is_file()                                      |
| os.path.islink()        | Path.is_symlink()                                   |
| os.link()               | Path.link_to()                                      |
| os.symlink()            | Path.symlink_to()                                   |
| os.readlink()           | Path.readlink()                                     |
| os.stat()               | Path.stat(), \***\*Path\*\***.owner(), Path.group() |
| os.path.isabs()         | PurePath.is_absolute()                              |
| os.path.join()          | PurePath.joinpath()                                 |
| os.path.basename()      | PurePath.name                                       |
| os.path.dirname()       | PurePath.parent                                     |
| os.path.samefile()      | Path.samefile()                                     |
| os.path.splitext()      | PurePath.suffix                                     |

### 参考

- 递归删除  
  纯 pathlib 实现

  ```python
  from pathlib import Path


  def rm_tree(pth):
      pth = Path(pth)
      for child in pth.glob('*'):
          if child.is_file():
              child.unlink()
          else:
              rm_tree(child)
      pth.rmdir()
  ```

- 第三方库  
  [path.py](https://github.com/jaraco/path)

- 文件大小  
  [Link](https://www.pythonheidong.com/blog/article/854020/0ee77bd60c8a10315cfa/)

  ```python
  Path(filename).stat().st_size
  ```

## Reference

[你应该使用 pathlib 替代 os.path](https://zhuanlan.zhihu.com/p/87940289)
[pathlib — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html#methods)
[PathLib 递归删除目录](https://www.cnpython.com/qa/66838)

**2021.04.29**
