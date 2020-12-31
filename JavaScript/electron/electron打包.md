<font size=4 face='楷体'>

## electron 打包

### Electron Forge

按照[官方文档](https://www.electronjs.org/docs/tutorial/quick-start#package-and-distribute-the-application)使用 electron-forge 打包示例

-   导入 Electron Forge 到您的应用文件夹

    ```js
    npx @electron-forge/cli import
    ```

-   创建一个分发版本
    ```js
    npm run make
    ```

### 打包安装包

使用[Inno Setup](https://jrsoftware.org/isinfo.php)将 electron 应用文件夹打包成安装包

### Reference

[electron 打包项目成 exe 桌面应用](https://blog.csdn.net/qq_41128253/article/details/102780384)
[electron 安装+运行+打包成桌面应用+打包成安装文件+开机自启动](https://www.cnblogs.com/kakayang/p/9559777.html)

**2020.12.30**
