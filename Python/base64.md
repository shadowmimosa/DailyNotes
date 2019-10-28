<font size=4 face='楷体'>

## Python 中传统图片格式与 base64 转换

> Base64 是网络上最常见的用于传输 8Bit 字节码的编码方式之一，是一种基于 64 个可打印字符来表示二进制数据的方法。通过 http 传输图片常常将图片数据转换成 base64 之后再进行传输。

### 图片 转 base64

```python
import base64

with open("pic.png","rb") as f:
    # b64encode 是编码，b64decode 是解码
    base64_data = base64.b64encode(f.read())
print(base64_data)
```

### base64 转为 opencv 的 Mat 格式

```python
import cv2
import base64

imgData = base64.b64decode(base64_data)
nparr = np.fromstring(imgData, np.uint8)
img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
```

### opencv 的 Mat 格式转为 base64

```python
import cv2
import base64

imgData = base64.b64decode(base64_data)
nparr = np.fromstring(imgData, np.uint8)
img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

image = cv2.imencode('.jpg', img_np)[1]
base64_data = str(base64.b64encode(image))[2:-1])
```

### Reference

[Python 中传统图片格式与 base64 转换](https://blog.csdn.net/kl28978113/article/details/79034014)

**2019.10.28**
