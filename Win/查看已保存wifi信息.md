<font size=4 face='楷体'>

## Win 查询已保存 wifi 信息

```powershell
netsh wlan export profile folder=c:\ key=clear
```

该操作将导出各个 wifi 的配置信息到 C 盘根目录, 保存在 xml 格式的文件中

打开其中一个 xml 文件, 里面的 KeyMaterial 标签保存的就是该 WiFi 的密码

### Reference

- [一条命令查看 Win10 已保存的 WiFi 密码](https://zhuanlan.zhihu.com/p/538646442)

**2022.10.13**
