<font size=4 face='楷体'>

## SSH 跳板机到目标机

```bash
ssh username@目标机器ip -p 22 -o ProxyCommand='ssh -p 22 username@跳板机ip -W %h:%p'
```

[MagicalCoder](http://lowcode.magicalcoder.com/element) 增值付费
[Form Generator](https://mrhj.gitee.io/form-generator) 开源表单生成器

### Reference

[基于 VUE 的 ElementUi 可视化表单设计器布局器](https://blog.csdn.net/heye520/article/details/101228401)
[vue 开源 Element UI 表单设计及代码生成器
](https://www.lagou.com/lgeduarticle/91345.html)

**2020.10.27**
