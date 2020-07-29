<font size=4 face='楷体'>

## openpyxl.utils.exceptions.IllegalCharacterError

- 原因
  excel 中存在[\000-\010]|[\013-\014]|[\016-\037]这些非法的字符

- 解决
  将字符串中的非法字符替换掉即可

  ```python
  ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
  text= ILLEGAL_CHARACTERS_RE.sub(r'', text)
  ```

### Reference

[openpyxl.utils.exceptions.IllegalCharacterError 错误原因分析及解决办法](https://blog.csdn.net/javajiawei/article/details/97147219)

**2020.07.28**
