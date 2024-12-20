<font size=4 face='楷体'>

## Element-Plus Form 表单组件

### label 实现两端对齐（左右对齐）

在使用 Element-Plus 的 form 的时候, label 只有左右, 居中对齐
缺少两端对齐的选项
css 实现如下

```css
/deep/ .el-form-item label:after {
  content: '';
  width: 100%;
}
/deep/ .el-form-item__label {
  /* display: inline-block必须要有，不然布局出问题，之前我看别人都加在伪类中，我试了没效果 */
  display: inline-block;
  text-align: justify;
  text-align-last: justify;
}
/* 这里去除必选字段的*,这个符号会造成一定影响,去掉之后我用了li列表进行定位,在前面加上" * ". */
/deep/ .el-form-item.is-required .el-form-item__label:before {
  content: none !important;
}
```

### Reference

[Element-Plus表单label实现两端对齐（左右对齐）](https://blog.csdn.net/qq_34082921/article/details/134330273)

**2023.11.17**
