<font size=4 face='楷体'>

## python 中 ftp 操作

ftp 登陆连接

```python
from ftplib import FTP #加载 ftp 模块

ftp=FTP() #设置变量
ftp.set_debuglevel(2) #打开调试级别 2，显示详细信息
ftp.connect("IP","port") #连接的 ftp sever 和端口
ftp.login("user","password") #连接的用户名，密码
print ftp.getwelcome() #打印出欢迎信息
ftp.cmd("xxx/xxx") #进入远程目录
bufsize=1024 #设置的缓冲区大小
filename="filename.txt" #需要下载的文件
file_handle=open(filename,"wb").write #以写模式在本地打开文件
ftp.retrbinaly("RETR filename.txt",file_handle,bufsize) #接收服务器上文件并写入本地文件
ftp.set_debuglevel(0) #关闭调试模式
ftp.quit() #退出 ftp
```

ftp 相关命令操作

```python
ftp.cwd(pathname) #设置 FTP 当前操作的路径
ftp.dir() #显示目录下所有目录信息
ftp.nlst() #获取目录下的文件
ftp.mkd(pathname) #新建远程目录
ftp.pwd() #返回当前所在位置
ftp.rmd(dirname) #删除远程目录
ftp.delete(filename) #删除远程文件
ftp.rename(fromname, toname)#将 fromname 修改名称为 toname。
ftp.storbinaly("STOR filename.txt",file_handel,bufsize) #上传目标文件
ftp.retrbinary("RETR filename.txt",file_handel,bufsize) #下载 FTP 文件
```

### Reference

[使用 python 操作 FTP 上传和下载](https://www.cnblogs.com/z3286586/p/11014468.html)

**2019.11.5**
