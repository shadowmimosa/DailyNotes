<font size=4 face='楷体'>

## Github 国内加速克隆及下载

本地推送经常报错，服务器拉取经常超时，本地图片显示异常

### 设置代理

为本地 git 插上小飞机的翅膀

```powershell
# 设置全局代理
git config --global http.proxy 127.0.0.1:8080

# 查看是否成功
git config --get http.proxy
127.0.0.1:8080
```

### 加速站点

- [fastgit.org](https://doc.fastgit.org/)
- [gitclone.com](https://gitclone.com/)
- [cnpmjs.org](https://github.com.cnpmjs.org/)

### 使用方法

- clone

  ```bash
  # 原链接
  git clone https://github.com/tencentyun/qcloud-documents.git

  # 加速连接
  git clone https://github.com.cnpmjs.org/tencentyun/qcloud-documents.git
  git clone https://hub.fastgit.org/tencentyun/qcloud-documents.git
  git clone https://gitclone.com/github.com/tencentyun/qcloud-documents.git
  ```

- download

  ```bash
  # 原链接
  wget https://github.com/tencentyun/qcloud-documents/archive/master.zip

  # 加速连接
  wget https://hub.fastgit.org/tencentyun/qcloud-documents/archive/master.zip
  wget https://github.com.cnpmjs.org/tencentyun/qcloud-documents/archive/master.zip
  wget https://gitclone.com/github.com/tencentyun/qcloud-documents/archive/master.zip
  ```

### Reference

[Github 国内加速克隆及下载](https://cloud.tencent.com/developer/article/1744627)
[Failed to connect to github.com port 443: Timed out](https://www.cnblogs.com/cbugs/p/12257443.html)
[在服务器里面，怎么给访问 github 加速](https://www.v2ex.com/t/728625)

**2021.04.28**
