<font size=4 face='楷体'>

## docx 处理相关库

Go 中 docx 处理相关库并不多

- [unidoc/unioffice](https://github.com/unidoc/unioffice)
  功能比较齐全，但是收费的
- [carmel/gooxml](https://github.com/carmel/gooxml)
  这个库为 `unidoc/unioffice` 免费版，即 1.4.0 收费版，在双重许可证下提供的
  在 AGPLv3 的条款下可以免费使用。虽然没有收费版功能多，但涵盖了大部分基本功能
  最后版本 `Dec 15, 2019`
- [nguyenthenguyen/docx](https://github.com/nguyenthenguyen/docx)
  是一个简单的操作 docx 文件 go 语言库
  最后版本 `Oct 6, 2017`
- [gomutex/godocx](https://github.com/gomutex/godocx)
  Go library for reading and writing Microsoft Docx
  参考 [python-docx](https://github.com/python-openxml/python-docx) and docx-rs 的项目
  最后版本 `Feb 13, 2024`

- [fumiama/go-docx](https://github.com/fumiama/go-docx)
  One of the most functional libraries to partially read and write .docx files (a.k.a. Microsoft Word documents or ECMA-376 Office Open XML) in Go.
  简单好用，但是元素属性支持不全
  最后更新 `Mar 27, 2024`
- [qifengzhang007/gooxml](https://github.com/qifengzhang007/gooxml)
  go 语言 word 文档处理库，基于 `carmel/gooxml` 二次开发
  较为理想
  最后更新 `Mar 8, 2024`

### 使用参考

[oxmltotext](https://github.com/young2j/oxmltotext/blob/4a602c83705f9f9f0078eaba3eabf9e6c549d4ba/benchmark/parse_docx.go#L19)
[golang_development_notes](https://github.com/guyan0319/golang_development_notes/blob/f245c26a41ae9019cc336eebf4b1fbd40dc4e0dd/zh/4.11.md)

### OXML 结构参考

[officeopenxml](http://officeopenxml.com/anatomyofOOXML.php)

### Reference

[已解决 error: Microsoft Visual C++ 14.0 or greater is required.](https://blog.csdn.net/yuan2019035055/article/details/126934308)

**2024.05.24**
