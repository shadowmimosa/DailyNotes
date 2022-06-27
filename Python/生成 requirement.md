<font size=4 face='楷体'>

## 生成 requirement.txt 文件

```bash
pip install pipreqs

# 指定编码, 替换 requirement.txt
pipreqs ./ --encoding='utf8' --force
```

> 鸡肋 只能生成 pip 环境中有的库, 并且是整个文件目录扫描, 不是依赖文件扫描

### Reference

[python 项目如何生成 requirements](https://www.jianshu.com/p/bc2e29932dbe)

**2021.07.30**
