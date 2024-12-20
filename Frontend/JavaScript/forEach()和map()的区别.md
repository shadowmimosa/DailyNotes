<font size=4 face='楷体'>

## forEach() 和 map() 的区别

### 相同点

- 都是循环遍历数组中的每一项
- forEach 和 map 方法里每次执行匿名函数都支持 3 个参数，参数分别是 item（当前每一项）、index（索引值）、arr（原数组）
- 匿名函数中的 this 都是指向 window
- 只能遍历数组

### map

- map 定义和用法
  map 方法返回一个新的数组，数组中的元素为原始数组调用函数处理后的值
  map 方法按照原始数组元素顺序依次处理元素
  注意：map 方法不会对空数组进行检测
  map 方法不会改变原始数组
- 浏览器支持
  chrome、safari、opera 都支持
  IE：>=9 版本
  safari： >=1.5
- 语法
  ```js
  array.map(function (item, index, arr) {}, thisValue);
  ```
- 参数说明
  item 当前元素的值
  index 索引值
  arr 原数组

### forEach

- 定义和用法
  forEach 方法用于调用数组的每个元素，将元素传给回调函数
  注意：forEach 对于空数组是不会调用回调函数的
- 语法
  ```js
  Array.forEach(function (item, index, arr) {}, this);
  ```
  参数说明同 map 方法

### Reference

[forEach()和 map()的区别：](https://blog.csdn.net/boysky0015/article/details/72983766)

**2020.09.10**
