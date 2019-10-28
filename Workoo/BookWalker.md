<font size=4 face='楷体'>

## BookWalker TW - 抓取反混淆后的漫画页

前两天有一活，解密一漫画网站的图片。钱不钱的都无所谓，主要是 18 禁好看。  
然而我懒拖得久了，没接成（才不是这个网站的混淆 加密什么的超级变态

后来网上 get 了一个大佬的方法

```js
const c = document.createElement("canvas");
const backup = window.NFBR.a6G.a5x.prototype.b9b;

window.NFBR.a6G.a5x.prototype.b9b = function() {
  const [targetCanvas, page, image, drawRect, flag] = arguments;
  if (image) {
    // 如果 image === null ，那么这一页是空白页。
    c.width = image.width;
    c.height = image.height;
    backup.call(
      this,
      c,
      page,
      image,
      { x: 0, y: 0, width: image.width, height: image.height },
      flag
    );
    // c 现在有整页图
    // 用 c.toDataURL() 等函数提取图像内容
  }
  return backup.apply(this, arguments);
};
```

嗯 原理大概 就是 拿已经渲染好了画布内容

### Reference

[BookWalker TW - 抓取反混淆后的漫画页](https://jixun.moe/intercept-bookwalker-tw-image)
[有没有大佬知道 BOOK☆WALKER 电子书的破解方法](http://bangumi.tv/group/topic/350167)
[fireattack/scripts](https://github.com/fireattack/scripts/blob/master/bookwalker.js)

**2019.10.28**
