<font size=4 face='楷体'>

## Electron 之使用 WebView 实现浏览页面

> electron 是使用 JavaScript，HTML 和 CSS 构建跨平台的桌面应用程序  
> 目前最新版本已經是 8.0.0

最终实现效果:

![](https://pic3.zhimg.com/v2-fd6ee1559fb2d04d58f2f3755780de6a_b.jpg)

页面功能说明：

1.  electron 开发的程序中一个浏览外部网页的一个子组件
2.  使用 js+electron 的方式开发，实现可以显示连接内容。 并提供简单的网页操作。
3.  使用 toolbar，模仿 wechat 中桌面版本的 toolbar 实现后退，刷新，外部默认浏览器开启等功能。

主要技术难点：

1.  webview 的嵌入和使用
2.  右键菜单在 electron MainProcess 模块中实现和在 Renderer Process 模块中的实现方式
3.  开启新页面的处理

## RendererProcess 主要实现内容

HTML 页面代码

```java
<div id="nav-body-ctrls">
        <!-- toolbar and address -->
        <i id="nav-ctrls-back" class="nav-icons disabled" title="后退" >
          <svg>此处省略 </svg>
        </i>
        <i id="nav-ctrls-reload" class="nav-icons disabled" title="刷新">
        <svg>此处省略 </svg
        </i>
        <i id="nav-ctrls-cplink" class="nav-icons " title="复制连接地址">
        <svg>此处省略 </svg
        </i>
        <i id="nav-ctrls-open" class="nav-icons " title="用默认浏览器打开">
        <svg>此处省略 </svg
        </i>
    </div>

    <div id="nav-body-views">
      <webview id="browser" class="webview-body" src="" allowpopups></webview>
    </div>
```

说明: 本次需求是实现简单浏览以及简单控制， 所以没有加地址部分的控制

toolbar 中，仅仅 4 个简单功能（地址的部分， 可以通过 event 关联到 dom 中元素来实现）

electron 模块引入

```java
const {  clipboard,  remote,Menu,MenuItem } = require('electron');
var $ = require('jquery');
```

页面初始化，绑定事件

```java
var webview = $('.webview-body');														// 获取到对应的webview
    webview.on('dom-ready', function () {											// 当页面载入完成，更新toolbar
      MBrowser.updateCtrl();
    });

		webview.on('page-title-updated', function () {
      document.title = MBrowser.webview.getTitle();		// 当title更新，更新外部框架的title
    });
  	webview.on('did-start-loading', function () {						// 更新进度条以及刷新按钮变为loading的图示，表示载入中
      MBrowser._loading();
    });
    webview.on('did-stop-loading', function () {         // 停止加载显示
      MBrowser._stopLoading();
    });
		webview[0].addEventListener('did-navigate', (res) => {
      MBrowser._updateUrl(res.url);
    });
```

按钮对应的操作

```java
$('#nav-body-ctrls').on('click', '#nav-ctrls-reload', function () {
      if (MBrowser.webview.isLoading()) {
        MBrowser.webview.stop();
      } else {
        MBrowser.webview.reload();
      }
    });

    $('#nav-body-ctrls').on('click', '#nav-ctrls-back', function () {
      MBrowser.webview.goBack();
    });

    $('#nav-body-ctrls').on('click', '#nav-ctrls-cplink', function () {
      clipboard.writeText(MBrowser.curUrl);
    });

    $('#nav-body-ctrls').on('click', '#nav-ctrls-open', function () {
      remote.shell.openExternal(MBrowser.curUrl)
    });
```

RendererProcess 实现

```java
webview[0].addEventListener('context-menu', function (event) {
      let params = event.params;
      let menu = MBrowser.createMenu(params);
      menu.popup(remote.getCurrentWindow());
    });
```

使用 content-menu 的事件来进行处理，该事件会使用 electron 创建一个 menu 并显示

菜单创建

```java
createMenu(options) {
    const hasText = options.selectionText.trim().length > 0;
    const can = type => options.editFlags[`can${type}`] && hasText;
    var that = this;
    let menu = new remote.Menu();
    menu.append(new remote.MenuItem(
        {
          role: 'selectAll',
          label: '全選',
          enabled: options.editFlags.canSelectAll,
          visible: options.isEditable,
        }
      ));
   menu.append(new remote.MenuItem(
        {
          role: 'cut',
          label: '剪切',
          enabled: can('Cut'),
          visible: options.isEditable,
        }
      ));

  ....

  return menu
}
```

## MainProcess 主要实现内容

因为对应模块在整个项目中是一个独立的 class

构造函数

```java
constructor(url) {
    this._browserWin = new BrowserWindow({
      width:1000,
      height:1200,
   	...
      icon: path.join(__dirname, '../assets/icon.png'),
      webPreferences: {
        webviewTag:true,
        javascript: true,
      ...
      },
    });

  this._browserWin.loadURL(
    'file://' + path.join(__dirname,'../assets/mbrowser.html')
  );
    this.initWindowEvents();  // 构建相关事件
    this.initWindowWebContent();
    this.initScreenEvent();
 // 因为开启是一个BrowswerWindow， 当dom-ready后将调用loadUrl 的方法将要开启的页面让rendererprocess中的webview 开启
  // 所以执行了页面中loadUrl的方法。
    this._browserWin.webContents.on('dom-ready', () => {
      let code = `MBrowser.loadUrl("` + url + `");`;
      log.debug(code);
      this._browserWin.webContents.executeJavaScript(code);
    });
```

### Reference

[Electron 之使用 WebView 实现浏览页面](https://zhuanlan.zhihu.com/p/106984364)

**2022.08.18**
