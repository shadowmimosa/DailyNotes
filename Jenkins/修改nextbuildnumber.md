<font size=4 face='楷体'>

## 重置或修改 nextBuildNumber

清理 build 文件之后，可能会因为 nextBuildNumber 的问题无法开始构建，比如报错

> java.lang.IllegalStateException: JENKINS-27530: cannot create a build with number 11 since that (or higher) is already in use among [156]

#### 原因

这是清理日志时候只重置了 nextBuildNumber 文件，Jenkins 管理的自增 Job ID 没做处理

#### 解决方案

1. 使用 [Next Build Number](https://plugins.jenkins.io/next-build-number/) 插件，修改 Job ID 到大于 Jenkins 管理，上例中是大于 156
2. 使用 API，例如 python 版的 [jenkinsapi](https://github.com/pycontribs/jenkinsapi)，但该版本未提供直接修改 nextBuildNumber 的功能，需要遍历，一直运行改 Job，直到运行成功，因为每次运行 nextBuildNumber 都会增加
3. 脚本

   ```bash
   def jobNames = ['job_name']

   // 循环遍历作业名称列表
   jobNames.each { jobName ->
     item = Jenkins.instance.getItemByFullName(jobName)
     item.updateNextBuildNumber(162)
   }
   ```

### Reference

[解决 VSCode 运行或调试 python 文件无反应的问题](https://blog.csdn.net/kraisi/article/details/127287966)

**2023.07.17**
