<font size=4 face='楷体'>

## 通过 url 打开图片

- OpenCV

  ```python
  import cv2
  cap = cv2.VideoCapture(img_src)
  if( cap.isOpened() ) :
      ret,img = cap.read()
      cv2.imshow("image",img)
      cv2.waitKey()
  ```

- OpenCV + Numpy + urllib

  ```python
  import numpy as np
  import urllib
  import cv2
  resp = urllib.urlopen(img_src)
  image = np.asarray(bytearray(resp.read()), dtype="uint8")
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  cv2.imshow("Image", image)
  cv2.waitKey(0)
  ```

- PIL + requests

  ```python
  import requests as req
  from PIL import Image
  from io import BytesIO
  response = req.get(img_src)
  image = Image.open(BytesIO(response.content))
  image.show()
  ```

- skimage
  ```python
  from skimage import io
  image = io.imread(img_src)
  io.imshow(image)
  io.show()
  ```

### Reference

[如何通过 URL 打开图片（Python）](https://www.jianshu.com/p/d64354a61359)

**2020.03.28**
