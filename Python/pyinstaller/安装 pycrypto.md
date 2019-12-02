<font size=4 face='楷体'>

## python 安装 pycrypto

在使用 pyinstaller 加密打包时，`--key` 参数需要 pycrypto 模块支持，然而这个包装起来并不是那么简单

### Windows 下

直接通过 pip install 安装会各种报错，查询得知需要环境支持，好在本地已经安装了 VS

- 进入虚拟环境（这里使用的是 pipenv）

  ```shell
  set CL=/FI"C:\MyComputer\Tools\Microsoft Visual Studio\2019\Preview\VC\Tools\MSVC\14.20.27404\include\stdint.h"
  ```

  这是将文件 stdint.h 的路径赋值给 CL 变量

  或者

  > 根据你的 vs 实际安装目录替换目录部分。

  > 手动将 C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\include\stdint.h 复制到 C:\Windows Kits\10\Include\10.0.17763.0\ucrt\ 目录下

  > 然后修改 C:\Windows Kits\10\Include\10.0.17763.0\ucrt\inttypes.h 文件，将开头的#include <stdint.h> 改为#include "stdint.h"

- 安装 pycrypto  
  这里使用源码安装：[下载地址](https://pypi.org/project/pycrypto/)  
  这里吐槽一句，源码上次更新时间：Last released: Oct 18, 2013, 是真的久远，装起来也是真的费劲，而好多包还非依赖不可
  在虚拟环境中执行：`python setup.py install`

至此，安装成功

### Linux 下

先执行：

> apt-get install python-dev

### Reference

[python3 安装 pycrypto](https://www.jianshu.com/p/830a3d8a95e2)
[windows 安装 pycrypto 出错问题](https://blog.csdn.net/A156348933/article/details/86137203)

[出现：Microsoft Visual C++ 14.0 is required 的解决方案](https://www.jianshu.com/p/7b24274c569a)
[解释 Crypto 模块怎么就这么"皮"？No module named "Crypto"](https://www.cnblogs.com/fawaikuangtu123/p/9761943.html)

**2019.11.12**
