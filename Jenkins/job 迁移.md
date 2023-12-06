<font size=4 face='楷体'>

## Jenkins Job 迁移

某次升级 Jenkins 版本后, 因为 Java 版本不匹配导致 Jenkins 无法正常使用
通过非正常手段勉强启动后, 开始迁移 Job

### 使用 `Job Import Plugin` 插件

这种方式比较方便

- 首先到新的 Jenkins 上的插件管理里先安装下 Job Import Plugin
- 安装完后进入"Manage Jenkins" -> "Configure System"下, 找到 Job Import Pluguin 配置的地方, 进行如下设置
  name: 这个可以任意命名
  Url: 指要从哪里拷贝的 Jenkins 的 URL, 要设置成旧的 Jenkins 的 URL
  Credentials：需要添加一个旧 Jenkins 的账号

- 设置完后点击保存下, 回到 Jenkins 首页点击 Job Import Plugin 就可以进行 Job 的迁移了

因为有时候旧的 Jenkins 上的插件新 Jenkins 上未必有, 因此可以根据实际情况勾选是否需要安装必要的插件, 需不需要覆盖已有的 job 也根据实际情况勾选下

Job Import Pugin 也支持多个 job 同时拷贝, 如果旧的 Jenkins 里有多个 job, query 出来就有很多 job 可供选择, 只需要勾选多个即可同时进行多个 job 的导入了

### Jenkins CLI 方式

网络无法互通等情况可以考虑使用 CLI 导出导入

点击进入 Jenkins CLI,可以看到有提供了 get-job 这样一个命令, 这个命令可以将 job 的定义导出到 xml 的格式到输出流, 可以通过这个命令将旧 Jenkins 上的 job 导出到外部文件
然后还可以看到有另外一个命令 create-job, 这个命令可以根据已有的 xml 配置文件进行 job 创建, 可以根据从旧 job 导出的 job 配置文件做为输入进行 job 的创建

- 点击 jenkins-cli.jar 就可以下载这个 jar 到本地

- 点击下 Jenkins 右上角的账号, 选择 Configure, 然后点击 Show API Token, 拷贝 token, 这个 token 可以用来进行配置导出的时候做为认证使用

- 在 jenkins-cli.jar 下载的根目录下执行如下命令进行 job 导出

  ```bash
  java -jar jenkins-cli.jar -s http://192.168.9.10:8080/jenkins -auth admin:493375c06bc0006a455005804796c989 get-job "job" > job.xml
  ```

  http://192.168.9.10:8080/jenkins: 就 Job 的 Jenkins 地址
  admin： 上面截图获取 Show API Token 下的 User ID
  493375c06bc0006a455005804796c989：上面截图获取 API Token 的值
  job: 需要导出配置的 job 名
  job.xml: 导出的文件的名称, 可任意

  根据实际情况替换下上面的四个值即可
  执行完上面的命令就可以看到 job.xml 文件生成了

- 在新的 Jenkins 下同样先下载下 jenkins-cli.jar, 将 job.xml 拷贝到新的 Jenkins 机器下, 同样获取下新 Jenkins 登录账号的 API Token 和 User ID

  ```bash
  java -jar jenkins-cli.jar -s http://192.168.9.8:8080/jenkins -auth admin:51964e7b89a427be5dd2a28f38c86eff create-job job. < job..xml
  ```

  记得将 URL 替换成新 Jenkins 的 URL, User ID 和 token 也替换下

  上面的命令执行完后, 就可以看到在新的 Jenkins 下新 job 被成功导入了

### Reference

[Jenkins job迁移](https://cloud.tencent.com/developer/article/1470433)

**2023.03.15**
