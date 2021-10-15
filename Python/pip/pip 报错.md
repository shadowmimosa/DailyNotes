<font size=4 face='楷体'>

## pip 异常报错

### No module named 'pip'

确认 pip 安装正常、环境变量设置正常时，尝试升级

- Windows

  ```powershell
  python -m ensurepip
  python -m pip install --upgrade pip
  ```

- Linux

  ```shell
  sudo apt-get install python3-pip
  ```

> Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-\*

更新 pip

```bash
pip3 install --upgrade pip
```

### WARNING: Ignoring invalid distribution -rotli

到提示的目录 site-packages 下删除 `~rotli` 开头的目录

### Reference

[解决 pip 使用异常 No module named 'pip'](https://www.jianshu.com/p/8cba020b284b)
[Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-\*解决办法](https://www.cnblogs.com/xiao987334176/p/12600835.html)
[WARNING: Ignoring invalid distribution -ip](https://blog.csdn.net/qq_47750984/article/details/117357267)

**Create On 2019.10.31, Update On 2021.06.15**
