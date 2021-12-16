<font size=4 face='楷体'>

## python 构建浏览器应用

### [cefpython](https://github.com/cztomczak/cefpython)

查到了这个东西，不过年代久远，文档教程缺乏，最新版维护到 python 3.7
最没办法使用的点是 配合 pyinstaller 打包巨费劲 还没成功

有成功案例感觉还挺好康的
[cefpython 浏览器](https://gitee.com/zhangleijay/cefpython_browser)
[tkinter + cefpython 仿美团桌面程序](https://www.cnblogs.com/wangleiblog/p/11105841.html)

### PyQt5

能用能打包
打包文件略大，启动应用延迟明显
痛点是 依赖程序 `QtWebEngineProcess.exe` 某零报毒

#### 隐藏表头

1.  ```js
    ui->tabWidget->setTabEnabled(0,false);
    ui->tabWidget->setTabEnabled(1,false);
    ui->tabWidget->setStyleSheet(“QTabBar::tab:disabled {width: 0; color: transparent;}”);
    ```
    这种方法看似很秀，实际上，你 tab 里面东西都不可选中，那我要你干嘛
2.  ```js
    ui->tabWidget->removeTab(0);
    ```

    我好不容易加了一个你叫我删除了？这删了啥都不显示有毛用。

3.  ```js
    ui->tab->hide();
    ```
    没用。毫无效果。看似很对
4.  ```js
    ui.tabWidget->tabBar()->hide();
    ```
    整个 tabbar 隐藏掉，正解。
5.  ```js
    ui->tabWidget->findChildren<QTabBar*>().at(0)->hide();
    ```

    同样也行。

可是为什么不用 stockwidget 呢，那只能说 tabwidget 看起来比较舒服，方便管理添加。理由很充分。

### Reference

[Python GUI: cefpython3 的简单分析和应用](https://www.jianshu.com/p/1ca206b28e28)
[python 做个谷歌内核浏览器-有标签页](https://www.cnblogs.com/Ctrl-cCtrl-v/p/12350228.html)
[利用 Python 和 PyQt5 实现简易浏览器](https://github.com/RogerLZH/Browser)
[Python 使用 Pyqt5 实现简易浏览器！非常实用！](https://blog.csdn.net/weixin_43881394/article/details/105838498)

[tabwidget 的 tab 隐藏问题](https://blog.csdn.net/m0_46398174/article/details/106398033)
[从 Exe 文件中提取图标资源](https://www.jianshu.com/p/5849a108e1e5?utm_campaign=maleskine)

**2020.12.29**
