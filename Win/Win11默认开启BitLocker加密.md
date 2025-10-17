<font size=4 face='楷体'>

## 微软 Win11 默认开启 BitLocker 加密

有文章称[实测显示：微软 Win11 开启 BitLocker 默认加密会使 SSD 减速 20~45%](https://baijiahao.baidu.com/s?id=1780201905196695256&wfr=spider&for=pc)

### 查看是否开启

以管理员身份运行命令提示符

```shell
manage-bde -status
```

其中，Conversion Status 将显示你是否启用加密，而 Encryption Method 将显示是硬件加密还是软件加密。如果跟上图一样显示为“XTS-AES”那就是 BitLocker 软件加密；如果显示为“Hardware Encryption”则代表 BitLocker 硬件加密。

### Reference

[实测显示：微软 Win11 开启 BitLocker 默认加密会使 SSD 减速 20~45%](https://baijiahao.baidu.com/s?id=1780201905196695256&wfr=spider&for=pc)

**2023.11.19**
