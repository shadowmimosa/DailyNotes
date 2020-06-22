<font size=4 face='楷体'>

## 校验 MD5

通常资源站下载的文件之类都会附带一串 MD5 值
为防止文件被篡改，对下载好的文件进行 MD5 校验

### Win

```bash
certutil -hashfile filename MD5
```

### Mac

```bash
md5 filename
```

### Reference

[参考](https://github.com/xiandanin/magnetW/wiki)

**2020.06.20**
