<font size=4 face='楷体'>

## jQuery 定位元素

id 是定位到的是单个 element 元素对象，其它的都是 elements 返回的是 list 对象

1. 通过 id 获取

    ```js
    document.getElementById("id");
    ```

2. 通过 name 获取

    ```js
    document.getElementsByName("Name");
    ```

3. 通过标签名选取元素
    ```js
    document.getElementsByTagName("tag");
    ```
4. 通过 CLASS 类选取元素

    ```js
    document.getElementsByClassName("class");
    ```

    兼容性：IE8 及其以下版本的浏览器未实现 getElementsByClassName 方法

5. 通过 CSS 选择器选取元素
    ```js
    document.querySelectorAll("css selector");
    ```

### Reference

[js 或 Jquery 操作定位元素](https://www.cnblogs.com/dangkai/p/9948573.html)

**2020.11.16**
