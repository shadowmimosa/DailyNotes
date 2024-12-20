<font size=4 face='楷体'>

## Element plus 图标使用

### 单个图标引入

```html
<template>
  <el-menu
    active-text-color="#ffd04b"
    background-color="#545c64"
    class="el-menu"
    default-active="2"
    text-color="#fff"
    @open="handleOpen"
    @close="handleClose"
  >
    <el-sub-menu index="1">
      <template #title>
        <el-icon><location /></el-icon>
        <span>Navigator One</span>
      </template>
    </el-sub-menu>
  </el-menu>
</template>

<script>
  import { Location } from '@element-plus/icons-vue'

  export default {
    name: 'SideMenu',
    components: {
      Location,
    },
  }
</script>
```

### 全局注册为组件

```javascript
// main.js
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElIcons from '@element-plus/icons-vue'

import App from './App.vue'

const app = createApp(App)

// 统一注册Icon图标
for (const iconName in ElIcons) {
  app.component(iconName, ElIcons[iconName])
}

app.mount('#app')
```

### Reference

[Element plus 图标使用](https://segmentfault.com/a/1190000041746262?utm_source=sf-similar-article)

**2022.08.16**
