<font size=4 face='楷体'>

## JS 删除 DOM 元素方法

### 删除子节点

```javascript
var box = document.getElementById('box')
box.parentNode.removeChild(box)
```

### 删除自身

```javascript
var box = document.getElementById('box')
box.remove()
```

### Reference

[JS 删除 DOM 元素的两种方法](https://blog.csdn.net/staywithc/article/details/3740980)

**2022.08.18**
