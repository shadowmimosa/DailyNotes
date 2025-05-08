<font size=4 face='楷体'>

## vuex-刷新页面 state 数据消失

### 一、Vuex

- 一个状态管理的插件，可以解决不同组件之间的数据共享和数据持久化，解决组件之间同一状态的共享问题。
- Vuex 优势：相比 sessionStorage，存储数据更安全，sessionStorage 可以在控制台被看到。
- Vuex 劣势：在刷新页面后，vuex 会重新更新 state，所以，存储的数据会丢失。

### 二、实际问题

- 在 vue 项目中，使用 Vuex 做状态管理时，调试页面时，刷新后 state 上的数据消失了，该如何解决？
- 消失的原因：因为 store 的数据是保存在运行内存中，当页面刷新时，页面会重新加载 vue 实例，store 里面的数据就会被重新赋值
- 解决思路：将 state 中的数据放在浏览器 sessionStorage 和 localStorage

### 三、解决办法一：存储到 localStorage/sessionStorage

- 通过监听页面的刷新操作，即 beforeunload 前存入本地 localStorage,页面加载时再从本地 localStorage 读取信息
- 在 App.vue 中加入下面代码，以 localStorage 为例：

```java
created(){
    //在页面刷新时将vuex里的信息保存到localStorage里
    window.addEventListener("beforeunload",()=>{    		localStorage.setItem("messageStore",JSON.stringify(this.$store.state))
                                              })

    //在页面加载时读取localStorage里的状态信息
    localStorage.getItem("messageStore") &&this.$store.replaceState(Object.assign(this.$store.state,JSON.parse(localStorage.getItem("messageStore"))));
}
```

问题 1：又需要使用 localStorage/sessionStorage，为什么不直接使用 localStorage/sessionStorage，要使用 vuex 呢

- vuex 中的变量是响应式的，而 localStorage 和 sessionStorage 都不是响应式
- 当你改变 vuex 中的状态，组件会检测到改变，而 localStorage 和 sessionStorage 就不会了，页面要重新刷新才可以看到改变
- 所以应让 vuex 中的状态从 localStorage/sessionStorage 中得到，这样组件就可以响应式的变化

问题 2：存储到 localStorage/sessionStorage 的区别

- sessionStorage，关闭窗口，数据消失
- localStorage，关闭窗口，数据也还在，除非将它移除

### 四、解决办法二：使用 vuex-persistedstate 插件

安装插件： npm install vuex-persistedstate

配置：在 vuex 初始化时候，作为组件引入。

```java
/******store/index.js******/
import createPersistedState from 'vuex-persistedstate'
export default new Vuex.Store({
    //...
    //没有设置是存储所以数据
    plugins: [createPersistedState()]
})
```

设定存储特定数据：

```java
plugins: [createPersistedState({
    storage: window.sessionStorage,
    reducer(data) {
        return {
            // 设置只储存state中的address
            address: data.address
        }
    }
})]
```

自定义存储方式：

- `vuex-persistedstate`默认存储到`localStorage`。
- 需要使用`sessionStorage`的情况

```java
plugins: [
    createPersistedState({
        storage: window.sessionStorage
    })
]
```

- 使用`cookie`的情况

  - 需要安装 cookies 插件

```java
import createPersistedState from 'vuex-persistedstate'
import * as Cookies from 'js-cookie'

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: {
        getItem: key => Cookies.get(key),
        setItem: (key, value) => Cookies.set(key, value, { expires: 7 }),
        removeItem: key => Cookies.remove(key)
      }
    })
  ]
})
```

### 五、解决办法三：使用 vuex-along 插件

安装插件： npm install vuex-along

配置：在 vuex 初始化时候，作为组件引入。

```java
import createVuexAlong  from 'vuex-along'
export default new Vuex.Store({
    //...
    //没有设置是存储所以数据
	plugins: [createVuexAlong ()]
})
```

自定义存储方式：

- `vuex-along`默认存储到`localStorage`

```java
plugins: [
    createVuexAlong ({
        name: "hello-vuex-along", // 设置保存的集合名字，避免同站点下的多项目数据冲突
        local: {
            list: ["address"],
            isFilter: true // 过滤模块 address数据， 将其他的存入 localStorage
        },
        session: {
            list: ["address.city"] // 保存 address.city到 sessionStorage
        }
        //如果对于sessionstorage不进行任何操作，也可将session设为false
    })
]
```

> 学习转自：  
> [vuex-persistedstate][]  
> [vuex-along][]  
> [vuex-along 解决 vuex 中存储的数据在页面刷新之后失去的问题][vuex-along_vuex]  
> [vuex 持久化 vuex-persistedstate][vuex_ vuex-persistedstate]

[vuex-persistedstate]: https://www.npmjs.com/package/vuex-persistedstate
[vuex-along]: https://www.npmjs.com/package/vuex-along
[vuex-along_vuex]: https://blog.csdn.net/weixin_45977625/article/details/108836697
[vuex_ vuex-persistedstate]: https://www.jianshu.com/p/c22861ec5f21

### Reference

[vuex-刷新页面 state 数据消失](https://www.cnblogs.com/jiajia-hjj/p/13882849.html)

**2022.08.15**
