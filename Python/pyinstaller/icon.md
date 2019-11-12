<font size=4 face='楷体'>

## pyinstaller icon 报错

### 报错

在使用 pyinstaller 打包时，`-i` 指定图标时报错：

```python
    except win32api.error as W32E:
AttributeError: module 'win32ctypes.pywin32.win32api' has no attribute 'error'
```

开始觉得叕是虚拟环境和 pywin32 的锅，直接把这个地方源码给改了

```python
    except Exception as W32E:
```

然后报错变成了：

```shell
Unable to load icon file ..\icon.png
    <no description> (Error code 193)
```

然后盲猜路径的问题，图标文件使用全路径，报错不变

### 解决

查询得知，打包程序对图标格式和尺寸有要求  
[格式转换](https://lvwenhan.com/convertico/)

最终 `pyinstaller -i icon.ico my.py` 替换图标成功

### Windows icon 尺寸

stackoverflow 上一老哥很详细的回答，不过年代比较久远 并没有 win10

> I took some time to check it in detail. I created an icon whose images have sizes of 16, 24, 32, 40, 48, 64, 96, 128 and 256. Then I checked which image is shown. All these were done with normal 96dpi. If using a larger DPI, the larger sizes may be used (only checked this a bit in Windows 7). The results:

**Windows XP:**

- Explorer views:
- - Details / List: 16
- - Icons: 32
- - Tiles / Thumbnails: 48
- Right-click->Properties / choosing a new icon: 32
- Quickstart area: 16
- Desktop: 32

**Windows 7:**

- Explorer views:
- - Details / List / Small symbols: 16
- - All other options: 256 (resized, if necessary)
- Right-click->Properties / choosing a new icon: 32
- Pinned to taskbar: 32
- - Right-click-menu: 16
- Desktop:
- - Small symbols: 32
- - Medium symbols: 48
- - Large symbols: 256 (resized, if necessary)
- - Zooming using Ctrl+Mouse wheel: 16, 32, 48, 256

**Windows Runtime: (from here)**

- Main tile: 150x150, 310x150 (wide version)
- Small logo: 30x30
- Badge (for lockscreen): 24x24, monochromatic
- Splashscreen: 620x300
- Store: 50x50

> So the result: Windows XP uses 16, 32, 48-size icons, while Windows 7 (and presumably also Vista) also uses 256-size icons. All other intermediate icon sizes are ignored (they may be used in some area which I didn't check).

### Reference

[关于 pyinstaller 打包程序时设置 icon 时的一个坑](https://blog.csdn.net/sinat_21427221/article/details/80846743)
[wpyinstaller 打包 icon 报错](https://blog.csdn.net/hq_cjj/article/details/88619274)
[Which icon sizes should my Windows application's icon include?](https://stackoverflow.com/questions/3236115/which-icon-sizes-should-my-windows-applications-icon-include)

**2019.11.12**
