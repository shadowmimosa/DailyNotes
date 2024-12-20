<font size=4 face='楷体'>

## 请求返回数据转换为 Blob 对象进行下载文件

```js
toExport: function(urlStr,name) {
			var _this = this;
			var xhr = new XMLHttpRequest()
			var fileName = name + '.xls'; // 文件名称
			xhr.open('GET', urlStr, true);
			xhr.responseType = 'blob';
			xhr.setRequestHeader("Authorization","Basic a2VybWl0Omtlcm1pdA=="); // 请求头中的验证信息等（如果有）
			xhr.onload = function(res) {
				if (this.status === 200) {
				  	var type = xhr.getResponseHeader('Content-Type');
				  	var blob = new Blob([this.response], {type: type});
				  	if (typeof window.navigator.msSaveBlob !== 'undefined') {
					    /*
					     * For IE
					     * >=IE10
					     */
				    	window.navigator.msSaveBlob(blob, fileName);
				  	} else {
				  		/*
				  		 * For Non-IE (chrome, firefox)
				  		 */
					    var URL = window.URL || window.webkitURL;
					    var objectUrl = URL.createObjectURL(blob);
					    if (fileName) {
					      	var a = document.createElement('a');
					      	if (typeof a.download === 'undefined') {
					        	window.location = objectUrl;
					      	} else {
					        	a.href = objectUrl;
					        	a.download = fileName;
					        	document.body.appendChild(a);
					        	a.click();
					        	a.remove();
					      	}
					    } else {
					      		window.location = objectUrl;
					    }
				  	}
				}
			}
			xhr.send()
}
```

### Reference

[ajax 请求返回数据转换为 Blob 对象进行下载文件](https://blog.csdn.net/zhou13528482267/article/details/89474648)

**2020.09.10**
