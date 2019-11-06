<font size=4 face='楷体'>

## pyinstaller + pipenv 打包

### pipenv 创建虚拟环境

一直使用 pipenv 作为虚拟环境管理工具，具体功能这里不再赘述。可以参考[这里](https://www.jianshu.com/p/d08a4aa0008e)

- 安装 pipenv

  ```shell
  pip install pipenv
  ```

- 初始化虚拟环境
  尽量在干净的目录下

  ```shell
  pipenv --python 3.7 # 安装 python3 虚拟环境
  ```

- 进入虚拟环境

  ```shell
  pipenv shell
  ```

- 在虚拟环境内，安装依赖环境
  在虚拟环境内安装包 使用 `pipenv install`, 会把依赖包写入当前虚拟环境目录中的 Pipfile ~~否则可能会影响虚拟环境外~~

  ```shell
  pipenv install pywin32
  pipenv install pyinstaller # 根据需要安装对应包
  ```

  [Pipfile 详细描述](https://blog.windrunner.me/python/pip.html)、[更多 pipenv 参数介绍](http://blog.51cto.com/1840558/2073283)

- 退出虚拟环境

  ```shell
  exit
  ```

### 在虚拟环境内打包

### 添加管理员权限启动（UAC）

某些情况下可能需要以管理员身份启动应用程序，这里添加在启动时获取管理权限功能。

1. 同级目录下生成 manifest 文件
   在生成后的 exe 跟目录创建一个后缀为 .manifest 具有相同 exe 名的文件，将下面代码写入

   ```xml
   <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
   <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
   <assemblyIdentity
       version="1.0.0.0"
       processorArchitecture="X86"
       name="myapp.exe.manifest"
       type="win32"
   />
   <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
       <security>
           <requestedPrivileges>
               <requestedExecutionLevel level="requireAdministrator" uiAccess="false"/>
           </requestedPrivileges>
       </security>
   </trustInfo>
   </assembly>
   ```

2. 可以将 manifest 文件写入应用程序，适合单个文件的应用
   - mt 工具位置：C:\Windows Kits\10\bin\10.0.17763.0\x86\mt.exe
   - cmd 命令进入 mt.exe 文件根目录
   - 将 manifest 文件写入应用程序，目标应用程序 my.exe
     ```shell
     mt -manifest C:\my.exe.manifest -outputresource:C:\my.exe;1
     ```

### Reference

[pipenv 创建虚拟环境，并用 Pyinstaller 打包流程](https://blog.csdn.net/laiyaoditude/article/details/85278037)

**2019.11.6**
