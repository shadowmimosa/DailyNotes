<font size=4 face='楷体'>

## adb 命令取出安装在手机中的 apk

- 列出手机中程序列表
  使用 adb shell pm list 命令，将手机中安装的应用包名列出来

  ```shell
  $ adb shell pm list packages
  package:android
  package:cn.wps.moffice
  package:com.android.backupconfirm
  package:com.android.bluetooth
  package:com.android.browser
  package:com.android.calculator2
  package:com.android.camera
  package:com.android.certinstaller
  package:com.android.contacts
  ```

- 找到所需 apk 的位置
  使用 adb shell pm path 命令，列出 apk 所在路径（这里以 cn.wps.moffice 为例

  ```shell
  $ adb shell pm path cn.wps.moffice
  package:/data/app/cn.wps.moffice.apk
  ```

- 拉取 apk
  将所需 apk 拉取到本地

  ```shell
  $ adb pull /data/app/cn.wps.moffice.apk ~/apks
  ```

### Reference

[Android 实战技巧之十八：adb 取出安装在手机中的 apk](https://blog.csdn.net/lincyang/article/details/44418379)

**2019.11.26**
