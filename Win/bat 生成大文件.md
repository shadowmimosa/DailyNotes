<font size=4 face='楷体'>

## windows 生成大文件

```bash
@echo off
echo 正在创建1.3G文件.file
fsutil file createnew 1.3G文件.file 1403148000
echo 正在创建1.3G文件.file
fsutil file createnew 660MB.file 630840000
echo ubuntu-16.04.1-clourdfort-amd64.iso
fsutil file createnew ubuntu-16.04.1-clourdfort-amd64.iso 1932735283
pause
```

### Reference

[windows 生成大文件.bat](https://www.cnblogs.com/xiaomifeng0510/p/13923477.html)

**2023.03.07**
