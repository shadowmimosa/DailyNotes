<font size=4 face='楷体'>

## Python 生成唯一 id

### UUID

```python
import uuid

def create_uid():
    return str(uuid.uuid1())

if __name__ == '__main__':
    print(type(create_uid()))
    print(create_uid())
    print(create_uid())
    print(create_uid())

---
<class 'str'>
cdcb9030-51e8-11e7-881d-3c52824c8d6f
cdcb9031-51e8-11e7-86b4-3c52824c8d6f
cdcb9032-51e8-11e7-be6c-3c52824c8d6f
```

### hashlib + time

- 示例 1

  ```python
  import time,hashlib

  def create_id():
      m = hashlib.md5(str(time.clock()).encode('utf-8'))
      return m.hexdigest()
  if __name__ == '__main__':
      print(type(create_id()))
      print(create_id())
      print(create_id())
      print(create_id())

  ---
  <class 'str'>
  b96d5fca757c00cbd53ae672f60e7ffe
  3e8391327caa4850077768d88ee18c7e
  df28a1e9895052608c2a6897f13d5659
  ```

- 示例 2

  ```python
  import time,hashlib

  def create_id():
      m = hashlib.md5()
      m.update(bytes(str(time.clock()),encoding='utf-8'))
      return m.hexdigest()
  if __name__ == '__main__':
      print(type(create_id()))
      print(create_id())
      print(create_id())
      print(create_id())

  ---
  <class 'str'>
  be4a24bec22f46c84a4dde78e68cb838
  53e8e0c48c885b91fb2565cbe87b8423
  f8fd24c3b8ce1a39217134e22203a5c4
  ```

### scrapy.utils.request.request_fingerprint

[参考](http://www.cnblogs.com/standby/p/7846478.html)

### [shortuuid](https://pypi.org/project/shortuuid/)

shortuuid 通过使用 Python 内置的 uuid 模块生成简洁, 明确, URL 安全的 uuid, 然后使用大小写字母和数字将它们转换为 base57, 并删除类似的字符, 如 l, 1, I, O 和 0

- 使用举例

  ```bash
  >>> import shortuuid
  >>> shortuuid.uuid()
  '4jYtG2xGoFvTcNPbnoyCNq'
  ```

- 生成 uuid5
  可以将名称( DNS 或者 URL ) 传递给函数调用, 它将用作产生的 UUID 的命名空间(UUID.namespace_dns 或者 UUID.namespace_url )

  ```bash
  >>> shortuuid.uuid(name="example.com")
  'exu3DTbj2ncsn9tLdLWspw'

  >>> shortuuid.uuid(name="http://example.com")
  'T35fvrnVz6SMSdh9y5hs8c'
  ```

- 生成带密码的安全随机字符串(内部使用 os.urandom())

  ```bash
  >>> shortuuid.ShortUUID().random(length=22)
  '42qBMavZJGyFmCpA49WgMv'
  ```

- 查看用于生成新 uuid 的字母表

  ```bash
  >>> shortuuid.get_alphabet()
  '23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
  ```

- 使用自定义字母表生成 uuid
  可使用`set_alphabet()`

  ```bash
  >>> shortuuid.set_alphabet('LMNPaaaaabcdefgh1230123fghijk')
  >>> shortuuid.get_alphabet()
  '0123LMNPabcdefghijk'
  ```

- 对已生成的 uuid 进行加解码

  ```bash
  >>> import uuid
  >>> u = uuid.uuid4()
  >>> u
  UUID('8b6b07db-d753-4627-8e1c-4873fe427439')

  >>> s = shortuuid.encode(u)
  >>> s
  '0hMMNLce3gecchjf31N11kkh3MN1fej'

  >>> shortuuid.decode(s) == u
  True
  ```

### Reference

[Python 生成唯一 id 的方法](https://www.cnblogs.com/standby/p/7021943.html)
[shortuuid 生成库学习小结](https://www.cnblogs.com/shouke/p/13423045.html)

**2022.10.19**
