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

- 安装 pywin32

  - 安装过程：
    直接使用 pip

    > pip install pywin32 # 或者 pypiwin32

    如果安装不成功，尝试源码安装，参考[这里](https://blog.51cto.com/alun51cto/2407692?source=dra)

  - 安装后
    在虚拟环境内安装后不一定可以 import, 需要修改虚拟环境中 Lib\site-packages\pywin32.pth 文件

    ```
    win32
    win32\lib
    Pythonwin
    ```

    将虚拟环境 pywin32.pth 文件的路径替换为本地 python 的绝对路径

    ```
    C:\Users\user\AppData\Local\Programs\Python\Python37\Lib\site-packages\win32
    C:\Users\user\AppData\Local\Programs\Python\Python37\Lib\site-packages\win32\lib
    C:\Users\user\AppData\Local\Programs\Python\Python37\Lib\site-packages\Pythonwin
    ```

  至此，虚拟环境中暂时可以使用 pywin32 相关模块了  
  为什么说暂时呢，因为还有问题，比如 `from win32com.shell import shellcon, shell` 中的 `shell` 就会 import 失败

### 在虚拟环境内打包

这里使用 pyinstaller 打包

- 详细使用过程
  [参考这里](http://www.imooc.com/article/286538)

- 相关参数

    <!-- <style>
    table th:first-of-type {
        width: 120px;
    }
    </style> -->

  | 命令                       | 详解                                                                                                                                                                                                    |
  | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | -F–onefile                 | 打包一个单个文件，如果你的代码都写在一个 py 文件的话，可以用这个，如果是多个 py 文件就别用                                                                                                              |
  | -D –onedir                 | 打包多个文件，在 dist 中生成很多依赖文件，适合以框架形式编写工具代码，我个人比较推荐这样，代码易于维护                                                                                                  |
  | -K –tk                     | 在部署时包含 TCL/TK                                                                                                                                                                                     |
  | -a –ascii                  | 不包含编码.在支持 Unicode 的 python 版本上默认包含所有的编码                                                                                                                                            |
  | -d –debug                  | 产生 debug 版本的可执行文件                                                                                                                                                                             |
  | -w<br>–windowed –noconsole | 使用 Windows 子系统执行.当程序启动的时候不会打开命令行(只对 Windows 有效)                                                                                                                               |
  | -c<br>–nowindowed –console | 使用控制台子系统执行(默认)(只对 Windows 有效)<br>pyinstaller -c xxxx&period;py<br>pyinstaller xxxx&period;py --console                                                                                  |
  | -s –strip                  | 可执行文件和共享库将 run through strip.注意 Cygwin 的 strip 往往使普通的 win32 Dll 无法使用                                                                                                             |
  | -X –upx                    | 如果有 UPX 安装(执行 Configure.py 时检测),会压缩执行文件(Windows 系统中的 DLL 也会)(参见 note)                                                                                                          |
  | -o DIR<br>–out=DIR         | 指定 spec 文件的生成目录,如果没有指定,而且当前目录是 PyInstaller 的根目录,会自动创建一个用于输出(spec 和生成的可执行文件)的目录.如果没有指定,而当前目录不是 PyInstaller 的根目录,则会输出到当前的目录下 |
  | -p DIR<br>–path=DIR        | 设置导入路径(和使用 PYTHONPATH 效果相似).可以用路径分割符(Windows 使用分号,Linux 使用冒号)分割,指定多个目录.也可以使用多个-p 参数来设置多个导入路径，让 pyinstaller 自己去找程序需要的资源              |
  | –icon=<FILE&period;ICO>    | 将 file.ico 添加为可执行文件的资源(只对 Windows 系统有效)，改变程序的图标   pyinstaller -i  ico 路径 xxxxx.py                                                                                           |
  | –icon=<FILE&period;EXE,N>  | 将 file.exe 的第 n 个图标添加为可执行文件的资源(只对 Windows 系统有效)                                                                                                                                  |
  | -v FILE<br>–version=FILE   | 将 verfile 作为可执行文件的版本资源(只对 Windows 系统有效)                                                                                                                                              |
  | -n NAME<br>–name=NAME      | 可选的项目(产生的 spec 的)名字.如果省略,第一个脚本的主文件名将作为 spec 的名字                                                                                                                          |

- 通过配置文件编译

  配置文件示例：
  一个后缀 .spec 的文件，实际上就是一个 python 文件

  ```python
  # -*- mode: python ; coding: utf-8 -*-

  # 虚拟环境内打包需要在文件头导入 distutils 模块
  import distutils
  if distutils.distutils_path.endswith('__init__.py'):
      distutils.distutils_path = os.path.dirname(distutils.distutils_path)

  # 加密参数
  block_cipher = pyi_crypto.PyiBlockCipher(key='passwd')

  a = Analysis(['auto.py'],
              # 打包路径
              pathex=['C:\\Users\\work'],
              binaries=[],
              # 外包文件
              datas=[],
              # 隐性导入模块，按需添加
              hiddenimports=['pandas', 'pandas._libs.tslibs.timedeltas', 'pandas._libs.tslibs.np_datetime', 'pandas._libs.tslibs.nattype', 'pandas._libs.skiplist', 'pymysql', 'openpyxl'],
              hookspath=[],
              runtime_hooks=[],
              excludes=[],
              win_no_prefer_redirects=False,
              win_private_assemblies=False,
              cipher=block_cipher,
              noarchive=False)
  pyz = PYZ(a.pure, a.zipped_data,
              cipher=block_cipher)
  exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          # 应用程序名
          name='work',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='icon.ico') # 图标路径

  ```

  然后使用 `pyinstaller my.spec` 命令进行打包

- 相关报错  
   虚拟环境中报错：

       ModuleNotFoundError: No module named 'distutils'

  解决：

  - 可以降级虚拟环境，参考[这里](https://blog.csdn.net/MacwinWin/article/details/88242432)

  - 或者在 \*.spec 文件头导入 distutils：

  ```python
  import distutils
  if distutils.distutils_path.endswith('__init__.py'):
          distutils.distutils_path = os.path.dirname(distutils.distutils_path)
  ```

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
[PyInstaller：编译 exe 与反编译](https://blog.csdn.net/HW140701/article/details/93494869)
[pyinstaller 参数介绍以及总结](https://blog.csdn.net/bearstarx/article/details/81054134)
[解决 pyinstaller 打包后运行 exe 程序出现的"ModuleNotFindError"](https://blog.csdn.net/zyc121561/article/details/79562935)
[社区的解决方案](https://github.com/pyinstaller/pyinstaller/issues/4064)
[windows 下 pyinstaller distutils not included with latest virtualenv (16.4.0)](https://www.cnblogs.com/wuyaSama/p/10784183.html)
[python--pipenv 环境下使用 pyinstaller 打包 py 脚本遇到的坑](https://blog.csdn.net/liuyingying0418/article/details/100152759)
[Pyinstaller 中 pandas 出错问题的解决（详细）](https://www.cnblogs.com/pprp/p/10246583.html)

**2019.11.6**
