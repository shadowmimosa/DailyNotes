<font size=4 face='楷体'>

## Android 平台签名证书(.keystore)生成指南

### 安装 JRE 环境

略

### 生成签名证书

使用 keytool -genkey 命令生成证书

```bash
keytool -genkey -alias testalias -keyalg RSA -keysize 2048 -validity 36500 -keystore test.keystore
```

- testalias 是证书别名，可修改为自己想设置的字符，建议使用英文字母和数字
- test.keystore 是证书文件名称，可修改为自己想设置的文件名称，也可以指定完整文件路径
- 36500 是证书的有效期，表示 100 年有效期，单位天，建议时间设置长一点，避免证书过期

回车后会提示

```bash
Enter keystore password:  //输入证书文件密码，输入完成回车
Re-enter new password:   //再次输入证书文件密码，输入完成回车
What is your first and last name?
  [Unknown]:  //输入名字和姓氏，输入完成回车
What is the name of your organizational unit?
  [Unknown]:  //输入组织单位名称，输入完成回车
What is the name of your organization?
  [Unknown]:  //输入组织名称，输入完成回车
What is the name of your City or Locality?
  [Unknown]:  //输入城市或区域名称，输入完成回车
What is the name of your State or Province?
  [Unknown]:  //输入省/市/自治区名称，输入完成回车
What is the two-letter country code for this unit?
  [Unknown]:  //输入国家/地区代号（两个字母），中国为CN，输入完成回车
Is CN=XX, OU=XX, O=XX, L=XX, ST=XX, C=XX correct?
  [no]:  //确认上面输入的内容是否正确，输入y，回车

Enter key password for <testalias>
        (RETURN if same as keystore password):  //确认证书密码与证书文件密码一样（HBuilder|HBuilderX要求这两个密码一致），直接回车就可以
```

以上命令运行完成后就会生成证书
**注意：上述信息填写要规范，乱填有可能会影响应用上架应用市场**

### 查看证书信息

可以使用以下命令查看

```bash
keytool -list -v -keystore test.keystore
Enter keystore password: //输入密码，回车
```

会输出以下格式信息

```bash
Keystore type: PKCS12
Keystore provider: SUN

Your keystore contains 1 entry

Alias name: test
Creation date: 2019-10-28
Entry type: PrivateKeyEntry
Certificate chain length: 1
Certificate[1]:
Owner: CN=Tester, OU=Test, O=Test, L=HD, ST=BJ, C=CN
Issuer: CN=Tester, OU=Test, O=Test, L=HD, ST=BJ, C=CN
Serial number: 7dd12840
Valid from: Fri Jul 26 20:52:56 CST 2019 until: Sun Jul 02 20:52:56 CST 2119
Certificate fingerprints:
         MD5:  F9:F6:C8:1F:DB:AB:50:14:7D:6F:2C:4F:CE:E6:0A:A5
         SHA1: BB:AC:E2:2F:97:3B:18:02:E7:D6:69:A3:7A:28:EF:D2:3F:A3:68:E7
         SHA256: 24:11:7D:E7:36:12:BC:FE:AF:2A:6A:24:BD:04:4F:2E:33:E5:2D:41:96:5F:50:4D:74:17:7F:4F:E2:55:EB:26
Signature algorithm name: SHA256withRSA
Subject Public Key Algorithm: 2048-bit RSA key
Version: 3
```

其中证书指纹信息（Certificate fingerprints）

- MD5
  证书的 MD5 指纹信息（安全码 MD5）
- SHA1
  证书的 SHA1 指纹信息（安全码 SHA1）
- SHA256
  证书的 SHA256 指纹信息（安全码 SHA245）

### 安卓签名获取工具

直接通过一个 apk，获取安装到手机的第三方应用签名的 apk 包。 [详情](https://developers.weixin.qq.com/doc/oplatform/Downloads/Android_Resource.html)

### 注意事项

云端打包默认会添加 V1/V2 签名，已知 V1 签名不支持 2048 位的 DSA 算法，使用 2048-bit DSA key 云端打包可能失败，提示以下错误

```bash
* What went wrong:
Execution failed for task ':app:packageRelease'.
> A failure occurred while executing com.android.build.gradle.tasks.PackageAndroidArtifact$IncrementalSplitterRunnable
   > java.io.IOException: Failed to generate v1 signature
```

#### 解决方法

- 第一种方法：重新生成证书，在生成证书命令中添加“-keyalg RSA”参数指定使用 RSA 算法
- 第二种方法：设置 miniSdkVersion 大于等于 24，因为 V2 签名需 Android7 及以上设备才支持，设置 miniSdkVersion 大于等于 24 表示不支持 android7 以下设备，从而不需要包含 V1 签名，设置 miniSdkVersion [详情参考](https://ask.dcloud.net.cn/article/193)

#### 查看证书算法的方法

使用“keytool -list -v”查看证书信息，看“Subject Public Key Algorithm: ”项的信息，如下表示使用 DSA 算法

```bash
Subject Public Key Algorithm: 2048-bit DSA key
```

### 其它

- [Android 平台公共测试证书](https://ask.dcloud.net.cn/article/36522)
- [Android 平台 DCloud 公用证书（DCloud 老版本证书）](https://ask.dcloud.net.cn/article/68)

### Reference

[Android 平台签名证书(.keystore)生成指南](https://ask.dcloud.net.cn/article/id-35777)

**2023.07.05**
