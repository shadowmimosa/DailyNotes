<font size=4 face='楷体'>

## RGB 转 HSV

```python
def rgb2hsv(r, g, b, cv2=True):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g - b) / m) * 60
        else:
            h = ((g - b) / m) * 60 + 360
    elif mx == g:
        h = ((b - r) / m) * 60 + 120
    elif mx == b:
        h = ((r - g) / m) * 60 + 240
    if mx == 0:
        s = 0
    else:
        s = m / mx
    v = mx
    if cv2:
        H = h / 2
        S = s * 255.0
        V = v * 255.0
        return H, S, V
    return h, s, v
```

openCV 中 H, S, V 的范围是 0-180, 0-255, 0-255 所以要做额外处理

### Reference

[python 实现 RGB 转换 HSV](https://blog.csdn.net/weixin_43360384/article/details/84871521)

**2020.12.30**
