<font size=4 face='楷体'>  

HTTPLibrary 库已经基本被弃用，停止更新并停在了python2  
使用会有诸多障碍，建议转用 request 库  

[Link](https://github.com/peritus/robotframework-httplibrary/issues/57)  

There's an unsupported syntax in HttpLibrary init&period;py
```python
except ValueError, e:
```
is not supported in Python 3.6 (maybe other versions as well, not sure).   
Updating to  
```python
except ValueError as e:
```
works for Python 2.7 and above (maybe for lower versions of Python as well, not sure).  

Also:  
`from urllib import urlparse`  
becomes  
`from urllib.parse import urlparse`  

and it's failing on importing `livetest`.  
Tried `from HttpLibrary import livetest` but that's not working.  


Ok, got the imports for Python 3.6:  

- \_\_init__&period;py
```python
from robot.api import logger

from base64 import b64encode
from functools import wraps
from urllib.parse import urlparse

from HttpLibrary import livetest
import json
import jsonpointer
import jsonpatch
```

- livetest&period;py
```
import sys
import webtest
import http.client
from urllib.parse import urlparse
from http.cookies import BaseCookie, CookieError
from six.moves import http_cookiejar

conn_classes = {'http': http.client.HTTPConnection,
                'https': http.client.HTTPSConnection}
```

Also in `livetest.py`, line 121:`iteritems()` should be updated to `items()`  
```python
headers = dict((name, val) for name, val in req.headers.items())
```