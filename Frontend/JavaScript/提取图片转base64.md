<font size=4 face='楷体'>

## 提取图片转 bae64

```js
// 下载图片转换为 base64
axios({
  method: "GET",
  url: url,
  headers: {
    Accept: "image/webp,image/apng,image/*,*/*;q=0.8",
  },
  responseType: "arraybuffer",
}).then(function (response) {
  let binary = "";
  const bytes = new Uint8Array(response.data);
  const len = bytes.byteLength;
  for (let i = 0; i < len; i += 1) {
    binary += String.fromCharCode(bytes[i]);
  }
  var img = window.btoa(binary);
  resolve("data:image/jpeg;base64," + img);
});
```

```js
// canvas 方案，不推荐
/**
 *
 * @param url 图片路径
 * @param ext 图片格式
 * @param callback 结果回调
 */
function getUrlBase64(url, ext, callback) {
  var canvas = document.createElement("canvas"); //创建canvas DOM元素
  var ctx = canvas.getContext("2d");
  var img = new Image();
  img.crossOrigin = "Anonymous";
  img.src = url;
  img.onload = function () {
    canvas.height = 60; //指定画板的高度,自定义
    canvas.width = 85; //指定画板的宽度，自定义
    ctx.drawImage(img, 0, 0, 60, 85); //参数可自定义
    var dataURL = canvas.toDataURL("image/" + ext);
    callback.call(this, dataURL); //回掉函数获取Base64编码
    canvas = null;
  };
}
```

```js
function downloadImg(url) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", url, false);
  xhr.onload = function (e) {
    if (xhr.readyState === 4) {
      if (xhr.status === 200) {
        xhr.response;
      } else {
        console.error(xhr.statusText);
      }
    }
  };
  xhr.onerror = function (e) {
    console.error(xhr.statusText);
  };
  xhr.send(null);
  return xhr.response;
}
```

```js
var xhr = new XMLHttpRequest();
xhr.open("GET", url, false);
xhr.send(null);
// xhr.responseType = "blob";
var blob = new Blob([xhr.response], {
  type: xhr.getResponseHeader("Content-Type"),
});
var reader = new FileReader();
reader.readAsDataURL(blob);
reader.result;
```

### Reference

[js 可否获取到 img 标签中图片的二进制数据](https://segmentfault.com/q/1010000019122380)
[XMLHttpRequest.response](https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest/response)
[ajax 请求返回数据转换为 Blob 对象进行下载文件](https://blog.csdn.net/zhou13528482267/article/details/89474648)

**2020.09.17**
