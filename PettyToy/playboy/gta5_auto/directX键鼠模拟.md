<font size=4 face='楷体'>

## DirectX 游戏模拟键鼠

普通模拟键鼠操作对使用了 DirectX 的游戏无效
查到了有针对 DirectX 输入模式的模块

```python
# https://github.com/Sentdex/pygta5/blob/master/directkeys.py

# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

import ctypes
import time

SendInput = ctypes.windll.user32.SendInput


W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

NP_2 = 0x50
NP_4 = 0x4B
NP_6 = 0x4D
NP_8 = 0x48

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

if __name__ == '__main__':
    PressKey(0x11)
    time.sleep(1)
    ReleaseKey(0x11)
    time.sleep(1)
```

能查到的最常见的都是类似上面的操作，然而各种无效
最后查到了[这个](https://stackoverflow.com/questions/51312300)和[这个](https://stackoverflow.com/questions/44886546)

> After a whole 3 months and multiple attempts to find a fix, I've just found out the issue - it wasn't running as admin, and Steam was.
> If anyone else stumbles across this, here is the code I've ended up with. You run elevate() at the start of the script, but make sure it's after freeze_support if you're using that.

因为脚本没用管理员运行, 而 steam 上都是管理员运行
所以, 用管理员命令行运行脚本, 或者在脚本运行入口调用:

```python
# pywin32

def elevate(console=True):
    arg = 'forced_elevate'
    if sys.argv[-1] != arg and not win32com.shell.shell.IsUserAnAdmin():
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [arg])
        try:
            win32com.shell.shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params, nShow=5 if console else 0)
        except pywintypes.error:
            pass
        else:
            sys.exit(0)
```

```python
# ctypes

def elevate(console=True):
    arg = 'forced_elevate'
    if sys.argv[-1] != arg and not ctypes.windll.shell32.IsUserAnAdmin():
        script = os.path.abspath(sys.argv[0])
        params = u' '.join([script] + sys.argv[1:] + [arg])
        ret = ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), params, None, 5 if console else 0)
        if int(ret) > 32:
            sys.exit(0)
```

### 基本键位对照

[基于图像处理和 tensorflow 实现 GTA5 的车辆自动驾驶——第四节通过 Python 控制人物前进后退](https://www.cnblogs.com/Coder-Photographer/p/14143208.html) - [Gitee](https://gitee.com/photographer_adam/Based-on-image-processing-and-tensorflow-to-realize-GTA5-vehicle-automatic-driving/blob/master/%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86%E9%83%A8%E5%88%86/Keys.py)

```python
class Key_Mapping:
    num1 = 0x02
    num2 = 0x03
    num3 = 0x04
    num4 = 0x05
    num5 = 0x06
    num6 = 0x07
    num7 = 0x08
    num8 = 0x09
    num9 = 0x0a
    num0 = 0x0b
    escape = 0x01
    equal = 0x0d
    backspace = 0x0e
    tab = 0x0f
    q = 0x10
    w = 0x11
    e = 0x12
    r = 0x13
    t = 0x14
    y = 0x15
    u = 0x16
    i = 0x17
    o = 0x18
    p = 0x19
    enter = 0x1c
    lcontrol = 0x1d
    a = 0x1e
    s = 0x1f
    d = 0x20
    f = 0x21
    g = 0x22
    h = 0x23
    j = 0x24
    k = 0x25
    l = 0x26
    z = 0x2c
    x = 0x2d
    c = 0x2e
    v = 0x2f
    b = 0x30
    n = 0x31
    m = 0x32
    shift = 0x36
    multiply = 0x37
    space = 0x39
    capital = 0x3a
    f1 = 0x3b
    f2 = 0x3c
    f3 = 0x3d
    f4 = 0x3e
    f5 = 0x3f
    f6 = 0x40
    f7 = 0x41
    f8 = 0x42
    f9 = 0x43
    f10 = 0x44
    numlock = 0x45
    f11 = 0x57
    f12 = 0x58
    divide = 0xb5
    home = 0xc7
    up = 0xc8
    prior = 0xc9
    left = 0xcb
    right = 0xcd
    end = 0xcf
    down = 0xd0
    next = 0xd1
    insert = 0xd2
    delete = 0xd3
    divide = 0xb5
    home = 0xc7
    up = 0xc8
    prior = 0xc9
    left = 0xcb
    right = 0xcd
    end = 0xcf
    down = 0xd0
    next = 0xd1
    insert = 0xd2
    delete = 0xd3
```

### 几个其它栗子

```python
# https://github.com/AlastairMelville/machine_learning/blob/a2bcb78de9b235faf49cabb1bd38bbed08b04f42/directkeys.py

# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
#https://github.com/SerpentAI/SerpentAI/blob/dev/serpent/input_controllers/native_win32_input_controller.py
# https://github.com/SerpentAI/SerpentAI/blob/dev/serpent/input_controllers/native_win32_input_controller.py

import ctypes
import time

SendInput = ctypes.windll.user32.SendInput


Keys = {
'A': 0x1E,


'D': 0x20,
'E': 0x12,
'R': 0x13,
'S': 0x1F,

'W': 0x11

}

mouse_button_down_mapping = {
    "LeftMouseButton": 0x0002,
    "MiddleMouseButton": 0x0020,
    "RightMouseButton": 0x0008
}

mouse_button_up_mapping = {
    "LeftMouseButton": 0x0004,
    "MiddleMouseButton": 0x0040,
    "RightMouseButton": 0x0010
}

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

NP_2 = 0x50
NP_4 = 0x4B
NP_6 = 0x4D
NP_8 = 0x48

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def LeftClick(SleepTime = 0.1):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    time.sleep(SleepTime)
    
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0004, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    
def ClickMouse(ButtonName="LeftMouseButton", SleepTime = 0.1):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, mouse_button_down_mapping[ButtonName], 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    time.sleep(SleepTime)
    
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, mouse_button_up_mapping[ButtonName], 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    
def PressMouse(ButtonName="LeftMouseButton"):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, mouse_button_down_mapping[ButtonName], 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseMouse(ButtonName="LeftMouseButton"):    
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, mouse_button_up_mapping[ButtonName], 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    
def MoveMouse(x, y):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(x, y, 0, 0x0001, 0, ctypes.pointer(extra))#(0x0001 | 0x8000), 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def move(self, x=None, y=None, duration=0.25, absolute=True, interpolate=True, **kwargs):
    if ("force" in kwargs and kwargs["force"] is True) or self.game_is_focused:
        if absolute:
            x += self.game.window_geometry["x_offset"]
            y += self.game.window_geometry["y_offset"]

            current_pixel_coordinates = win32api.GetCursorPos()
            start_coordinates = self._to_windows_coordinates(*current_pixel_coordinates)

            end_coordinates = self._to_windows_coordinates(x, y)

            if interpolate:
                coordinates = self._interpolate_mouse_movement(
                    start_windows_coordinates=start_coordinates,
                    end_windows_coordinates=end_coordinates
                )
            else:
                coordinates = [end_coordinates]

            for x, y in coordinates:
                extra = ctypes.c_ulong(0)
                ii_ = Input_I()
                ii_.mi = MouseInput(x, y, 0, (0x0001 | 0x8000), 0, ctypes.pointer(extra))
                x = Input(ctypes.c_ulong(0), ii_)
                ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

                time.sleep(duration / len(coordinates))
        else:
            x = int(x)
            y = int(y)

            coordinates = self._interpolate_mouse_movement(
                start_windows_coordinates=(0, 0),
                end_windows_coordinates=(x, y)
            )

            for x, y in coordinates:
                extra = ctypes.c_ulong(0)
                ii_ = Input_I()
                ii_.mi = MouseInput(x, y, 0, 0x0001, 0, ctypes.pointer(extra))
                x = Input(ctypes.c_ulong(0), ii_)
                ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

                time.sleep(duration / len(coordinates))

if __name__ == '__main__':
    time.sleep(5)
    #PressMouse("LeftMouseButton");
    #time.sleep(5)
    #ReleaseMouse("LeftMouseButton");
    #time.sleep(1)
    for i in range(10):
        MoveMouse(1, 0);
```

```python
# https://github.com/moonjaeang/v4/blob/333da53a3b852e859c422c1434a27c91ad3b8e69/likeyoubot_extra.py
import ctypes

PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


class LYBExtra:
    def __init__(self, configure, resolution):
        self.configure = configure
        self.resolution = resolution

    def set_pos(self, x, y):
        x = 1 + int(x * 65536. / float(self.resolution[0]))
        y = 1 + int(y * 65536. / float(self.resolution[1]))
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.mi = MouseInput(x, y, 0, (0x0001 | 0x8000), 0, ctypes.pointer(extra))
        command = Input(ctypes.c_ulong(0), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))

    def mouse_move(self, x, y):
        x = 1 + int(x * 65536. / float(self.resolution[0]))
        y = 1 + int(y * 65536. / float(self.resolution[1]))
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.mi = MouseInput(x, y, 0, (0x0001 | 0x8000), 0, ctypes.pointer(extra))
        command = Input(ctypes.c_ulong(0), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))


    def left_click(self):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.mi = MouseInput(0, 0, 0, 0x0002, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(0), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.mi = MouseInput(0, 0, 0, 0x0004, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(0), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def mouse_click(self, x, y):
        # rand_x = 0
        # rand_y = 0
        # if self.configure is not None and self.configure.common_config[
        #     lybconstant.LYB_DO_BOOLEAN_RANDOM_CLICK] is True:
        #     random_error = int(self.configure.common_config[lybconstant.LYB_DO_BOOLEAN_RANDOM_CLICK + 'pixel'])
        #     rand_x += int(random_error * random.random())
        #     rand_y += int(random_error * random.random())
        #
        # x += rand_x
        # y += rand_y

        x = 1 + int(x * 65536. / float(self.resolution[0]))
        y = 1 + int(y * 65536. / float(self.resolution[1]))
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.mi = MouseInput(x, y, 0x00FF, (0x0001 | 0x8000 | 0x0002 | 0x0004), 0, ctypes.pointer(extra))
        command = Input(ctypes.c_ulong(0), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))
```

```python
https://github.com/mohammed-Emad/controling-mouse-movement-and-clicks-with-camera/blob/a17863923aa67fca2fee1c8f7b7fd19e7b1cc62d/directkeys.py

# direct inputs
#SOURCES AND REFRENCES
#http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
#http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
#https://pythonprogramming.net/direct-input-game-python-plays-gta-v/
#https://pastebin.com/sE7aVWhp
#https://github.com/SerpentAI/SerpentAI/blob/dev/serpent/input_controllers/native_win32_input_controller.py
import win32api
import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
Q = 0x10
E = 0x12

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

#functions
def SetPosition(x, y):
    x = 1 + int(x * 65536.0/ctypes.windll.user32.GetSystemMetrics(0))
    y = 1 + int(y * 65536.0/ctypes.windll.user32.GetSystemMetrics(1))
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(x, y, 0, (0x0001 | 0x8000), 0, ctypes.pointer(extra))
    command = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))

def left_click_down():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def left_click_up():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0004, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def right_click_down():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def right_click_up():
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 0x0010, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def moveMouseRel(xOffset, yOffset):
        ctypes.windll.user32.mouse_event(0x0001, xOffset, yOffset, 0, 0)

if __name__ == '__main__':
    #PressKey(0x11)
    #time.sleep(1)
    #ReleaseKey(0x11)
    time.sleep(2)
    left_click_down()
    time.sleep(5)
    left_click_up()
    # print(win32api.GetCursorPos())
    # x_multiplier = 1
    # for x in range(1, 10000):
    #     xy_pos = win32api.GetCursorPos()
    #     #x_pos = xy_pos[0] + 1
    #     x_pos = xy_pos[0] - 1*x_multiplier
    #     moveMouseRel(int(-1.0), 0)
    #     time.sleep(0.001)
```

## Reference

[python 实现 GTA5 自动驾驶 - B 站字幕版](https://www.bilibili.com/video/BV1yC4y1s7gg?p=3)
[Direct Input to Game - Python Plays GTA V](https://pythonprogramming.net/direct-input-game-python-plays-gta-v/)
[pygta5](https://github.com/Sentdex/pygta5/)

[SerpentAI](https://github.com/SerpentAI/SerpentAI)

**2021.05.12**
