<font size=4 face='楷体'>

## electron 控制新开窗口大小

```js
function createWindow() {
    mainWindow -
        new Browserwindow({
            height: 600,
            width: 600,
            webPreferences: {
                nodeIntegration: false,
            },
        });
    //mainWindow.maximize();
    mainWindow.loadURL(config.url);
    win_event(mainWindow);
    mainWindow.on("closed", function () {
        mainWindow - null;
    });
}

function win_event(win) {
    win.webContents.on(
        "new-window",
        function (event, url, fname, disposition, options) {
            // let childwindow;
            // childwindow = new Browserwindow({
            //     height: 360,
            //     width: 360,
            //     webPreferences: {
            //         nodeIntegration: false
            //     }
            // });
            // win_event(childwindow);
            // childwindow.loadURL(url);
            event.preventDefault();
        }
    );
}
```

这里自定义了一个 win_event 函数，在这里拦截了 new-window 事件。同时，使用 event.preventDefault()，来阻止默认行为（打开固定尺寸的窗口）。然后新建了一个 BrowserWindow，利用它来控制新开窗口的尺寸，同时再次调用该函数，使得新开窗口中的新开窗口，也能够在控制拦截范围内

```js
function win_event(win) {
    win.webContents.on(
        "new-window",
        function (event, url, fname, disposition, options) {
            let childwindow;
            childwindow = new BrowserWindow({
                height: 360,
                width: 360,
                webPreferences: {
                    nodeIntegration: false,
                },
            });
            win_event(childwindow);
            childwindow.loadURL(url);
            event.preventDefault();
        }
    );
}
```

### Reference

[electron 如何控制 BrowserWindow 的新开窗口尺寸?](https://newsn.net/say/electron-browserwindow-size.html)


**2020.12.30**
