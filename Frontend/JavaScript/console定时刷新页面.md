<font size=4 face='楷体'>

## Chrome console 定时刷新

```js
// 弹出对话框，获取用户输入的文本
prompt()
// 延迟执行函数
setTimeout(,)
// 可向指定对象写入 html 代码或者 js 代码
write()
// 设定代码的作用域
with()
```

```js
var timeout = prompt("设置刷新时间");
current = location.href;
if (timeout > 0) {
    setTimeout("reload()", 1000 * timeout);
} else {
    location.replace(current);
}

function reload() {
    setTimeout("reload()", 1000 * timeout);
    var frame =
        "<frameset cols='*'>\n<frame src='" + current + "' /></frameset>";
    with (document) {
        // 引用document对象，调用write方法写入框架，打开新窗口
        write(frame); //此处输入代执行的代码
        // 关闭上面的窗口
        void close();
    }
}
```

### Reference

[刷新页面后，让控制台的js代码继续执行](https://blog.csdn.net/ainu2919/article/details/102037343)

**2020.11.16**
