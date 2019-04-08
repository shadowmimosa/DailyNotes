<font size=4 face='楷体'>

```python
import base64

copyright = 'Copyright (c) 2012 Doucube Inc. All rights reserved.'


def main():
    #转成bytes string
    bytesString = copyright.encode(encoding="utf-8")  # python2 中默认为bytes, encode()默认就为'utf-8'
    print(bytesString)

    #base64 编码
    encodestr = base64.b64encode(bytesString)
    print(encodestr)
    print(encodestr.decode())

    #解码
    decodestr = base64.b64decode(encodestr)
    print(decodestr.decode())  # print(decodestr), 直接输出为 b'str'

if __name__ == '__main__':
    main()
```

- TypeError: Incorrect padding

```python
# 需补齐'='
def decode_base64(data):
    """Decode base64, padding being optional.
    
    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.
    
    """
    # bype_string = bytes(data, 'utf-8')
    bype_string=data
    missing_padding = len(bype_string) % 4
    if missing_padding != 0:
        bype_string += b'=' * missing_padding
    return base64.decodestring(bype_string)
```