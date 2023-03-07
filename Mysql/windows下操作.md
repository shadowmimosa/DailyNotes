<font size=4 face='楷体'>

## Windows 下 Mysql 操作

### 安装

官网下载 msi 文件, 傻瓜式安装即可

### 找到 mysql 服务器名

- 命令行运行(Win + R) `services.msc`
- 找到 mysql 服务
  eg. mysql80 服务名为 `MySQL80`
- 以管理员的身份运行命令行

  ```powershell
  # 停止运行
  NET STOP MySQL80

  # 启动
  NET START MySQL80
  ```

### 报错提示

- 提示 `服务名无效`
  服务名称不对, 按照上述步骤找到 mysql 的服务名
- 提示 `发生系统错误 5`
  未以管理员身份运行命令行

### 修改数据存储路径

- 查看当前路径

  ```sql
  SELECT @@datadir;
  ```

- 停掉 mysql 服务
- 找到对应的数据存放路径，和 Data 同路径下有一个 my.ini 文件
- 备份好 my.ini 文件
- 修改 my.ini 文件 (datadir 参数)
- 重启 mysql 服务

## Reference

[Windows10 开启、关闭、重启 MySQL 服务](https://blog.csdn.net/fwdwqdwq/article/details/123705089)

**2022.07.06**
