<font size=4 face='楷体'>

## python 使用 xpath

### lxml

- 安装
  ```bash
  pip install lxml
  ```

- 使用示例
  ```python
  import requests 

  from lxml import html 
  url = 'https://movie.douban.com/chart' 

  r = requests.get(url).content 
  sel = html.fromstring(r) 

  # 提取h1标签 
  title = sel.xpath("//h1/text()") 

  # 提取链接 
  links = sel.xpath('//div[@class="pl2"]/a/@href') 

  # 上面返回的是所有符合条件的链接的列表，for循环来读取一下 
  for link in links: 
      print link  
  ```


### Reference
[Python 解析库 lxml 与 xpath 用法总结](https://www.cnblogs.com/dcpeng/p/14528019.html)
[Python爬虫（2）：XPath语法](https://zhuanlan.zhihu.com/p/26303926)

**2022.01.12**
