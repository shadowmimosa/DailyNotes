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

### Reference

[解决 pip 使用异常 No module named 'pip'](https://www.jianshu.com/p/8cba020b284b)

**2019.10.31**
