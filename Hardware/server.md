<font size=4 face='楷体'>

## 服务器相关

### DELL iDRAC 重置密码

- 环境
  DellR630 服务器（也主要用于 R720、R730、R620、R420、R530）
- 问题
  服务器 iDRAC 忘记密码
- 表明
  13 代机器默认 iDRAC 账号密码为 `root/calvin`
  14 代机器默认 iDRAC 账号为`root`, 密码在机器前小抽拉卡片的背面 `iDRACpassword` 上

两代的机器重置密码的方法皆一样, 处理过程:

1. 开机时 F2 进去 BIOS, 选择 DRACsettings
2. 选择 userconfiguration, 可在这里界面下更改密码
3. 选择 enabled, 在 changepassword 中输出密码, 点击 Back 后, 再次输入密码, 更改完过后, 重启服务器, 就能用该密码登录 idrac 界面了
4. 进去 idrac 登录界面
5. 已登入 idrac 界面, 重置密码成功

### iDRAC 虚拟控制台

打开方式有两种

- 通过 ie 浏览器直接打开
  win10 之后不再支持 ie
- JRE 打开
  太高版本可能无法运行

### 阵列卡 H710 配置

[阵列卡 PERCH330_H730 配置手册](https://blog.51cto.com/u_960683/2087089)

### 超微主板配置 ipmi

ipmi 类似 iDRAC
[超微主板使用配置 ipmi 功能流程介绍](https://zhuanlan.zhihu.com/p/597490170)

### Reference

[Dell 服务器 iDRAC 卡重置密码怎么操作?](https://blog.csdn.net/ichen820/article/details/128931563)
[idrac 虚拟控制台的使用](https://blog.csdn.net/hb_wxz/article/details/102521157)

**2023.06.14**
