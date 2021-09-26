<font size=4 face='楷体'>

## mvn 常用命令

- 创建一个新的 Maven 项目：

  - 普通 java 项目

    ```bash
    mvn archetype:create -DgroupId=packageName -DartifactId=projectName
    ```

  - web 项目

    ```bash
    mvn archetype:create -DgroupId=packageName -DartifactId=webappName -DarchetypeArtifactId=maven-archetype-webapp
    ```

    ```bash
    mvn archetype:create -DgroupId=org.sonatype.mavenbook.ch3 -DartifactId=simple -DpackageName=org.sonatype.mavenbook
    ```

- 构建打包应用

  - mvn install
    在 pom.xml 同级目录下执行

- 查看项目完整的 pom.xml 文件，包括系统默认设置以及用户自定义设置

  ```bash
  mvn help:effective-pom
  ```

- 生成报告或者文档

  ```bash
  mvn site
  ```

- 执行目标类

  ```bash
  mvn exec:java -Dexec.mainClass=org.sonatype.mavenbook.weather.Main
  ```

- 查看插件的完整描述

  ```bash
  mvn help:describe -Dplugin=exec -Dfull
  ```

- 找出该项目所依赖的项目(jar)列表

  ```bash
    mvn dependency:resolve
    mvn dependency:analyze # 找出项目非直接依赖
  ```

- 查看整个项目的依赖树

  ```bash
  mvn dependency:tree
  ```

- 查看完整的依赖，包括那些因为冲突而被拒绝引入的依赖

  ```bash
  mvn install -X
  ```

- 打包应用(jar)

  ```bash
  mvn install assembly:assembly
  ```

- 在 Jetty Servlet 容器中启动你的 web 应用

  ```bash
  mvn jetty:run
  ```

- 重新编译

  ```bash
  mvn compile
  ```

- 编译测试代码

  ```bash
  mvn test-compile
  ```

- 运行测试

  ```bash
  mvn test
  ```

- 打包

  ```bash
  mvn package
  ```

- 清除产生的项目

  ```bash
  mvn clean
  ```

- 生成 eclipse 项目

  ```bash
  mvn eclipse:eclipse
  ```

- 只打 jar 包

  ```bash
  mvn jar:jar
  ```

- 跳过单元测试

  ```bash
  mvn test -D maven.test.failure.ignore=true
  ```

- 跳过整个测试

  ```bash
  mvn install -D maven.test.skip=true
  ```

- maven 打包跳过测试
  mvn 命令增加参数

  ```bash
  mvn package -D maven.test.skip=true
  ```

  单元测试增加注解

  ```Java
  @Ignore
  ```

  maven 插件

  ```xml
  <configuration>
      <skip>true</skip>
  </configuration>
  ```

- 下载依赖包的源代码

  ```bash
  mvn dependency:sources
  ```

### Reference

[mvn 常用命令](https://www.jianshu.com/p/ee7bc34d7ccc)
[maven 设置跳过测试](https://www.cnblogs.com/flying607/p/9952033.html)

**Create on 2020.09.07, Update on 2020.09.17**
