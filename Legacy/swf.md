<font size=4 face='楷体'>

## swf 解析

### pyswf

[Github](https://github.com/timknip/pyswf)
上次更新在四年前
上次某网站的 swf 处理很好，以为找到了解决方案
结果这次用不了了
一个是 pillow 更新了，废弃了 `Image.fromstrings`
针对这次的任务提取不出内容，只能提取公章和签名两张图片 奇怪

### swftools

[Github](https://github.com/matthiaskramm/swftools)
[swftools](http://www.swftools.org/)
[python bindings](http://www.swftools.org/gfx_tutorial.html)

可用，但 python 库无人维护现阶段无法直接打包，需要调用 exe 文件
linux 安装也失败
可尝试自行打包

工具包中的 `SWFStrings` 甚至能直接提取 swf 中字符串，但中文乱码需要解决
- 安装
  [centos安装SWFtools服务(pdf2swf)](https://developer.aliyun.com/article/515299)
  [centos7 安装swftools](https://www.jianshu.com/p/101994b03bf4)

### Reference

[python - 在 Linux 上将 SWF 文件转换为 PNG 图像](https://www.coder.work/article/1902414)
[freetype](https://www.freetype.org/)
[xpdfreader](https://www.xpdfreader.com/download.html)

**2020.11.30**
