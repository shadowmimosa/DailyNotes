<font size=4 face='楷体'>

## watch 使用

- watch 入参格式

```javascript
watch(监听的数据，副作用函数，配置对象)
watch(data, (newData, oldData) => {}, {immediate: true, deep: true})
```

- 创建响应式数据

```javascript
import { ref, watch, reactive } from 'vue'

let name = ref('moxun')
let age = ref(18)
let person = reactive({
  Hobby: 'photo',
  city: {
    jiangsu: {
      nanjing: '雨花台',
    },
  },
})
```

- 监听单个 refimpl 数据

```javascript
watch(name, (newName, oldName) => {
  console.log('newName', newName)
})
```

- 创建响监听多个 refimpl 数据应式数据

vue3 允许多个 watch 监听器存在

```javascript
watch(name, (newValue, oldValue) => {
  console.log('new', newValue, 'old', oldValue)
})
watch(age, (newValue, oldValue) => {
  console.log('new', newValue, 'old', oldValue)
})
```

将需要监听的数据添加到数组

```javascript
watch([name, age], (newValue, oldValue) => {
  console.log('new', newValue, 'old', oldValue)
})
```

- 监听 proxy 数据
  此时 vue3 将强制开启 deep 深度监听
  当监听值为 proxy 对象时, oldValue 值将出现异常, 此时与 newValue 相同

```javascript
// 监听proxy对象
watch(person, (newValue, oldValue) => {
  console.log('newValue', newValue, 'oldValue', oldValue)
})
```

- 监听 proxy 数据的某个属性

需要将监听值写成函数返回形式, vue3 无法直接监听对象的某个属性变化

```javascript
watch(
  () => person.Hobby,
  (newValue, oldValue) => {
    console.log('newValue', newValue, 'oldvalue', oldValue)
  }
)
```

注意

当监听 proxy 对象的属性为复杂数据类型时, 需要开启 deep 深度监听

```javascript
watch(
  () => person.city,
  (newvalue, oldvalue) => {
    console.log('person.city newvalue', newvalue, 'oldvalue', oldvalue)
  },
  {
    deep: true,
  }
)
```

- 监听 proxy 数据的某些属性

```javascript
watch([() => person.age, () => person.name], (newValue, oldValue) => {
  // 此时newValue为数组
  console.log('person.age', newValue, oldValue)
})
```

### 总结

- 与 vue2 中的 watch 配置一致

- 两个坑
- - 监听 reactive 定义的 proxy 代理数据时
- - oldValue 无法正确获取
- - 强制开启 deep 深度监听(无法关闭)
- - 监听 reactive 定义的 proxy 代理对象某个属性时 deep 配置项生效

### Reference

[VUE3 中 watch 监听使用实例详解](https://www.jb51.net/article/250652.htm)

**2022.08.15**
