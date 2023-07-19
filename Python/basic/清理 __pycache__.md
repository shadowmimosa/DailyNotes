<font size=4 face='楷体'>

## 清理 \_\_pycache\_\_

### 关于 pycache

当第一次运行 python 脚本时, 解释器会将 `*.py` 脚本进行编译并保存到 \_\_pycache\_\_ 目录
下次执行脚本时, 若解释器发现你的 `*.py` 脚本没有变更, 便会跳过编译一步, 直接运行保存在 \_\_pycache\_\_ 目录下的 `*.pyc` 文件

### 清理 pycache

- 单次关闭
  运行脚本时添加 -B 参数即可

- 永久关闭
  设置环境变量 `PYTHONDONTWRITEBYTECODE=1` 即可

- 一次递归删除
  ```python
  import os
  def clear(filepath):
      files = os.listdir(filepath)
      for fd in files:
          cur_path = os.path.join(filepath, fd)            
          if os.path.isdir(cur_path):
              if fd == "__pycache__":
                  print("rm %s -rf" % cur_path)
                  os.system("rm %s -rf" % cur_path)
              else:
                  clear(cur_path)

  if __name__ == "__main__":
      clear("./")
  ```

## Reference

[删除项目中所有的__pycache__ 文件](https://www.cnblogs.com/lmh001/p/10057371.html)

**2022.10.27**
