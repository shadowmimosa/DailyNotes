<font size=4 face='楷体'>

## xpath

### 语法

#### 选取节点

XPath 使用路径表达式在 XML 文档中选取节点
节点是通过沿着路径或者 step 来选取的
有用的路径表达式

| 表达式   | 描述                                                     |
| -------- | -------------------------------------------------------- |
| nodename | 选取此节点的所有子节点。                                 |
| /        | 从根节点选取。                                           |
| //       | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置 |
| .        | 选取当前节点。                                           |
| ..       | 选取当前节点的父节点。                                   |
| @        | 选取属性。                                               |

#### 谓语（Predicates）

谓语用来查找某个特定的节点或者包含某个指定的值的节点。
谓语被嵌在方括号中。
在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：

| 路径表达式                           | 结果                                                                                      |
| ------------------------------------ | ----------------------------------------------------------------------------------------- |
| `/bookstore/book[1]`                 | 选取属于 bookstore 子元素的第一个 book 元素。                                             |
| `/bookstore/book[last()]`            | 选取属于 bookstore 子元素的最后一个 book 元素。                                           |
| `/bookstore/book[last()-1]`          | 选取属于 bookstore 子元素的倒数第二个 book 元素。                                         |
| `/bookstore/book[position()<3]`      | 选取最前面的两个属于 bookstore 元素的子元素的 book 元素。                                 |
| `//title[@lang]`                     | 选取所有拥有名为 lang 的属性的 title 元素。                                               |
| `//title[@lang='eng']`               | 选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。                                |
| `/bookstore/book[price>35.00]`       | 选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。                |
| `/bookstore/book[price>35.00]/title` | 选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。 |

#### 选取未知节点

XPath 通配符可用来选取未知的 XML 元素。

| 通配符 | 描述                 |
| ------ | -------------------- |
| \*     | 匹配任何元素节点。   |
| @\*    | 匹配任何属性节点。   |
| node() | 匹配任何类型的节点。 |

在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：

| 路径表达式     | 结果                              |
| -------------- | --------------------------------- |
| `/bookstore/*` | 选取 bookstore 元素的所有子元素。 |
| `//*`          | 选取文档中的所有元素。            |
| `//title[@*]`  | 选取所有带有属性的 title 元素。   |

#### 选取若干路径

通过在路径表达式中使用"|"运算符，您可以选取若干个路径。
在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：

| 路径表达式             | 结果          |
| ---------------------- | ------------- | ----------------------------------------------------------------------------------- |
| `//book/title          | //book/price` | 选取 book 元素的所有 title 和 price 元素。                                          |
| `//title               | //price`      | 选取文档中的所有 title 和 price 元素。                                              |
| `/bookstore/book/title | //price`      | 选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。 |

### JS 使用 XPath

```js
var result = document.evaluate(
  '//a[@href]',
  document,
  null,
  XPathResult.ANY_TYPE,
  null
)
var nodes = result.iterateNext() //枚举第一个元素
while (nodes) {
  // 对 nodes 执行操作;
  nodes = result.iterateNext() //枚举下一个元素
}

// 如果只查找单个元素，可以简写成这样
nodes = document.evaluate("//div[@id='xxx']", document).iterateNext()
```

### xpath 获取当前标签的兄弟节点，父节点

```html
<div>
  <a id="1" href="www.baidu.com">我是第1个a标签</a>
  <p>我是p标签</p>
  <a id="2" href="www.baidu.com">我是第2个a标签</a>
  <a id="3" href="www.baidu.com">我是第3个a标签</a>
  <a id="4" href="www.baidu.com">我是第4个a标签</a>
  <p>我是p标签</p>
  <a id="5" href="www.baidu.com">我是第5个a标签</a>
</div>
```

- 获取第三个 a 标签的下一个 a 标签
  `"//a[@id='3']/following-sibling::a[1]"`

- 获取第三个 a 标签后面的第 N 个标签
  `"//a[@id='3']/following-sibling::\*[N]"`

- 获取第三个 a 标签的上一个 a 标签
  `"//a[@id='3']/preceding-sibling::a[1]"`

- 获取第三个 a 标签的前面的第 N 个标签
  `"//a[@id='3']/preceding-sibling::\*[N]"`

- 获取第三个 a 标签的父标签
  `"//a[@id=='3']/.."`

### 取最后元素

```
# 取xpath最后一个book元素
book[last()]

# 取xpath最后第二个book元素
book[last()-1]
```

### Reference

[xpath 获取当前标签的兄弟节点，父节点](https://blog.csdn.net/qq_37059367/article/details/83819828)
[js 中 xpath 使用](https://www.cnblogs.com/xtreme/p/7839509.html)

**Create On 2020.11.16, Update On 2020.11.18**
