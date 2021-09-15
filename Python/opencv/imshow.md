<font size=4 face='楷体'>

## imshow

### 弹出窗口图片未响应, 无法显示图片

```python
import cv2
import numpy as np

img = cv2.imread('image.jpg')
cv2.imshow('image.jpg',img)
```

会出现弹出窗口图片未响应, 无法显示图片的情况

```python
import cv2
import numpy as np

img = cv2.imread('image.jpg')
cv2.imshow('image.jpg',img)
cv2.waitKey()
cv2.destroyAllWindows()
```

保证显示视频时窗口上的帧可以一直进行更新
即可正常显示

### Reference

[OpenCV | imshow()弹出窗口图片未响应；无法显示图片](https://blog.csdn.net/yefcion/article/details/79435591)

**2021.09.15**
