<font size=4 face='楷体'>

## Html 清洗

### 移除属性

-   lxml

    -   手动遍历

        ```python
        import lxml
        from HTMLParser import HTMLParser

        html_string = u'''
        <img src="http://abc.com/1.jpg" width="1" height="2" style="width:1px;hegiht:23px;"/>
        '''
        html = lxml.html.fromstring(html_string)
        for tag in html.xpath(u'//*[@style]'):
            tag.attrib.pop(u'style')
        for tag in html.xpath(u'//*[@height]'):
            tag.attrib.pop(u'height')
        for tag in html.xpath(u'//*[@width]'):
            tag.attrib.pop(u'width')

        print(HTMLParser().unescape(lxml.html.tostring(html)))
        # 如果不想用HTMLParser，可以用如下代码：
        print(tostring(html, encoding="utf-8").decode('utf-8'))
        ```

    -   clean 方法

        ```python
        import lxml.html.clean as clean

        safe_attrs = set(['src', 'alt', 'href', 'title'])
        cleaner = clean.Cleaner(safe_attrs=safe_attrs)
        html_string = u'''
        <img src="http://abc.com/1.jpg" width="1" height="2" style="width:1px;hegiht:23px;"/>
        '''
        cleaned_html = cleaner.clean_html(html_string)
        print(cleaned_html)
        ```

        这，当然是用 clean 方法了

-   BeautifulSoup
    也是用手动遍历

    ```python
    from BeautifulSoup import BeautifulSoup

    def _remove_attrs(soup):
        for tag in soup.findAll(True):
            tag.attrs = None
        return soup


    def example():
        doc = '<html><head><title>test</title></head><body id="foo" οnlοad="whatever"><p class="whatever">junk</p><div style="background: yellow;" id="foo" class="blah">blah</div></body></html>'

        print 'Before:\n%s' % doc
        soup = BeautifulSoup(doc)
        clean_soup = _remove_attrs(soup)
        print '\nAfter:\n%s' % clean_soup
    ```

### w3lib

-   remove_tags
    作用：去除或保留标签，但是仅仅是去除标签，正文部分是不做处理的

-   remove_tags_with_content
    作用：去除标签，包括其正文部分
-   remove_comments
    作用：去除掉网页的注释
-   remove_entities
    作用：将网页中的一些特殊字符的源码显示改变成正常显示

## tips

~~_还没有找到已有去除 html 标签之间的 \n, \t 的方法_~~
找到了

```python
import re

re.sub(">\s*<", "><", "[here your html string]")
```

### Reference

[Python 移除 HTML width hegiht style 属性(remove attributes from HTML tags)](https://blog.csdn.net/lilongsy/article/details/87931234)
[python 爬虫去除 html 中特定标签、去除注释、替换实体](https://blog.csdn.net/qq_41849471/article/details/89527706)

[在 python 中的 html 中删除标签之间的空格和换行符](https://www.it1352.com/2122589.html)

**Create on 2020.06.09, Update on 2020.12.30**
