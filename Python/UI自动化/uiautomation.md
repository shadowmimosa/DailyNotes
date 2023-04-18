<font size=4 face='楷体'>

## [Python-UIAutomation-for-Windows](Python-UIAutomation-for-Windows)

🐍Python 3 wrapper of Microsoft UIAutomation. Support UIAutomation for MFC, WindowsForm, WPF, Modern UI(Metro UI), Qt, IE, Firefox, Chrome ...

自动化测试工具
封装了微软 UIAutomation API, 支持自动化 Win32, MFC, WPF, Modern UI(Metro UI), Qt, IE, Firefox(version<=56 or >=60, Firefox57 是第一个 Rust 开发版本,前几个 Rust 开发版本个人测试发现不支持), Chrome 和基于 Electron 开发的应用程序(Chrome 浏览器和 Electron 应用需要加启动参数--force-renderer-accessibility 才能支持 UIAutomation).
[中文文档](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows/blob/master/readme_cn.md)

### 使用参考

[⭐UI 自动化工具轻松实现微信消息收发 ⚡ 朋友圈爬取⁉️](https://blog.csdn.net/as604049322/article/details/119899542)
[Windows 端 UI 自动化---python3 + uiautomation 框架](https://blog.csdn.net/chenmozhe22/article/details/106926071)

### 基本操作

[uiautomation：基于 windows 的 ui 自动化框架](https://www.modb.pro/db/136139)
[Windows 桌面程序自动化控制之 uiautomation 模块全面讲解](https://www.wangt.cc/2021/11/windows%E6%A1%8C%E9%9D%A2%E7%A8%8B%E5%BA%8F%E8%87%AA%E5%8A%A8%E5%8C%96%E6%8E%A7%E5%88%B6%E4%B9%8Buiautomation%E6%A8%A1%E5%9D%97%E5%85%A8%E9%9D%A2%E8%AE%B2%E8%A7%A3/)

### 相关工具

- Python tools

  - [pywinauto](https://github.com/pywinauto/pywinauto) - 是一组用于自动化 Microsoft Windows GUI 的 python 模块
  - [PyAutoGui](https://github.com/asweigart/pyautogui) - 一个流行的跨平台库 (具有基于图像的搜索, 没有基于文本的控件操作)
  - [Lackey](https://github.com/glitchassassin/lackey) - Sikuli 的纯 Python 替代品 (基于图像模式匹配)
  - [AXUI](https://github.com/xcgspring/AXUI) - MS UI Automation API 的一个包装器
  - [winGuiAuto](https://github.com/arkottke/winguiauto) - 另一个使用 Win32 API 的模块

- 其他脚本语言工具

  - (Perl) [Win32::GuiTest](http://winguitest.sourceforge.net/)
  - (Ruby) [Win32-Autogui](https://github.com/robertwahler/win32-autogui) - Win32 API 的包装器
  - (Ruby) [RAutomation](https://github.com/jarmo/RAutomation) - 有 3 个适配器: Win32 API, UIA, AutoIt

- 其他免费工具

  - (C#) [Winium.Desktop](https://github.com/2gis/Winium.Desktop) - 一个年轻但很好的基于 MS UI Automation 的工具
  - (C#) [TestStack.White](https://github.com/TestStack/White) - 另一个很好的基于 MS UI Automation 的库, 历史悠久
  - [AutoIt](http://www.autoitscript.com/) - 具有自己的类似 Basic 语言的免费工具 (基于 Win32 API, 没有.NET 计划)
  - [AutoHotKey](https://github.com/Lexikos/AutoHotkey_L/) - 具有自己的脚本语言的原生 C++工具 (.ahk)
  - [很棒的测试自动化列表](https://github.com/atinfo/awesome-test-automation)
  - [用于功能测试的大量开源工具](http://www.opensourcetesting.org/category/functional/)
  - winAppDriver
- 辅助工具
  - inspect.exe - 微软自带
  - UIspy.exe

- 商业工具
  - [WinRunner](http://www.mercury.com/us/products/quality-center/functional-testing/winrunner/)
  - [SilkTest](http://www.segue.com/products/functional-regressional-testing/silktest.asp)
  - [Many Others](http://www.testingfaqs.org/t-gui.html)

### Reference

[什么是 pywinauto](https://www.kancloud.cn/gnefnuy/pywinauto_doc/1193035)

**2022.08.22**
