<font size=4 face='楷体'>

## TLS Warnings

* 禁用警告

``` python
>>> import urllib3
>>> urllib3.disable_warnings()
```

* 日志捕获

``` python
>>> logging.captureWarnings(True)
```

### Reference

[TLS Warnings](https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings)

**2021.04.28**
