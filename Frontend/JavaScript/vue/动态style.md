<font size=4 face='楷体'>

## 动态修改 style 样式

- html 结构

  ```html
  <Upload
    ref="upload"
    :show-upload-list="false"
    :before-upload="handleBeforeUpload"
    :disabled="disabled"
    :max-size="maxSize"
    action
  ></Upload>
  ```

- 作用区域范围内设置 "CSS 变量"

  ```html
  <style lang="less" scoped>
  .info-img-wrap {

   --textAlignPosition: center;

   /deep/ .ivu-upload {

    text-align: var(--textAlignPosition);

   }

  }
  <style/>
  ```

- setProperty 方法

  在 JS 中通过 setProperty() 方法修改 `--textAlignPosition` 的值, 从而间接改变对应子元素的`text-align` 文本对齐方式

  ```javascript
  mounted() {

     this.$nextTick(function () {

      this.$refs.upload.$el.style.setProperty(

       '--textAlignPosition',

       this.textAlign

      );

     });

  }
  ```

### vue 中可以通过对象语法和数组语法来修改 class

- 对象语法

  ```html
  <div v-bind:class="{ 'active': isActive, 'text-danger': hasError }"></div>
  ```

  ```javascript
  data: {
  isActive: false,
  hasError: true
  }
  ```

- 数组语法

  ```html
  <div v-bind:class="\[isActive ? activeClass : '', errorClass\]"></div>
  ```

  ```javascript
  data: {
   isActive: false,
   hasError: true,
   activeClass: 'active',
   errorClass: 'text-danger'
  }
  ```

### vue 中可以通过对象语法和数组语法来修改 style

- 对象语法

  ```html
  <div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
  ```

  ```javascript
  data: {
   activeColor: 'red',
   fontSize: 30
  }
  ```

- 数组语法

  ```html
  <div v-bind:style="\[styleColor, styleSize\]"></div>
  ```

  ```javascript
  data: {
   styleColor: {
     color: 'red'
    },
   styleSize:{
     fontSize:'23px'
   }
  }
  ```

eg.
```javascript
<template>
  <p @click="changeColor">hello</p>
</template>

<script setup>
import { reactive } from "vue"
const theme = reactive({
  color: 'red'
}) 
 const changeColor = ()=>{
  theme.color="black"
  console.log(theme);

}
</script>



<style scoped>
p {
  color: v-bind('theme.color');
}
</style>
```

### Reference

[在 VUE style 中使用 data 中的变量的方法](https://www.jb51.net/article/189040.htm)
[vue3-动态修改style](https://www.jianshu.com/p/e640a7691dcb)

**2022.05.10**
