<font size=4 face='楷体'>

## Vue 获取 dom 节点

- 原生 js 获取节点

```javascript
// 使用 id 获取
document.getElementById()
// 使用 类名 获取
document.getElementByClassName()
// 使用 标签名 获取
document.getElementByTagName()
// 使用 name属性 获取
document.getElementByName()
// 使用 css选择器 获取
// 返回该模式匹配的第一个元素, 结果为一个元素; 没有匹配元素时, 返回值为 null
document.querySelector()
```

- 在 vue 中引入 jquery

jQuery 中包裹后的 DOM 对象实际上是一个数组, 要获得纯粹的 DOM 对象可以有两种方式

```javascript
// 使用数组索引方式访问
var dom = $(dom)[0]
$('#id')[0]

// 使用函数get()访问
// get() 函数中的参数为索引号
var dom = $(dom).get(0)
```

- ref 属性

此属性是获取 dom 对象, 作用与 id 作用相似, 相当于给标签起了一个类似于 id
ref 用来给元素或子组件引用信息, 引用信息会注册在父组件的 `$refs` 对象中
在普通的 DOM 元素上使用, 引用指向时 DOM 元素, 在子组件上, 引用指向组件实例
操作一个元素时, 在元素上添加 ref 属性, 之后使用 `$refs` 来获取该元素, 之后进行操作

- 直接使用 DOM API 寻找元素

```javascript
<script>
    //这种方法足够简单直观，Vue组件在patch阶段结束时会把this.$el赋值为挂载的根dom元素，我们可以直接使用$el的querySelector, querySelectorAll等方法获取匹配的元素。
	...
	mounted () {
		let elm = this.$el.querySelector('#id')
	}
</script>
```

### Reference

[Vue 获取 DOM 节点方式](https://blog.csdn.net/qq_45829293/article/details/123361448)

**2022.08.16**
