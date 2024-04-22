<font size=4 face='楷体'>

## AFormItem 表单验证问题

### 绑定嵌套的多维(多层)数组的方法

如果是多维数组，需要这样绑定到 a-form-item 才能生效

```html
<a-form-item
  label="用户名"
  :name="['my','username']"
  :rules="[{ required: true }]"
>
  <a-input v-model:value="data.my.username" />
</a-form-item>
```

当然也可以使用 `useForm() + v-bind="validateInfos['my.username']"` 的方式绑定

### Reference

- [antd 表单验证、表单重置 绑定嵌套的多维(多层)数组的方法](https://www.cnblogs.com/alpiny/p/16196925.html)

**2023.12.06**
