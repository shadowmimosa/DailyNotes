<font size=4 face='楷体'>

## Vuex Store 使用

在 src 文件夹下新增 store 文件夹, 里面包含 index.js

```javascript
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    //这里放全局参数
  },

  mutations: {
    //这里是set方法
  },

  getters: {
    //这里是get方法
  },

  actions: {},

  modules: {
    //这里是为了给全局变量分组, 所以需要写提前声明其他store文件, 然后引入这里
  },
})
```

### 与 localStorage, 全局变量区别

- 与 localStorage 区别

  1. 最重要的区别: vuex 存储在内存, localStorage 则以文件的方式存储在本地

  2. 应用场景: vuex 用于组件之间的传值, localStorage 则主要用于不同页面之间的传值。

  3. 永久性: 当刷新页面时 vuex 存储的值会丢失, localStorage 不会。

- 与全局变量区别

  1. 由于使用 Vuex 需要将 store 实例挂载到 Vue 实例中, 因此 Vue 实例可以对 Vuex 的 state 数据加监听, 这跟 Vue 实例 data 的数据双向绑定是类似的。
     而全局变量由于没有被“数据劫持”, 因此即使全局变量的值发生改变, 也无法在 Vue 实例中监听到他的变化。

  2. Vuex 中的状态值, 不能通过赋值的方式(state.xxx = yyy)改变, 需要通过 mutation 触发变更。这样做方便状态管理, 而一般的全局变量是支持直接赋值的。

### Reference

[Vuex 之 store 的使用](https://www.cnblogs.com/yyp-technology/p/16416288.html)

**2022.08.15**
