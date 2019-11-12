<font size=4 face='楷体'>

## python 打包成 so

某次萌生了讲 python 混淆的想法  
了解后发现，目前 python 的混淆工具多数都是只支持单个文件，不支持整个项目文件夹，而且混淆效果并不理想；而 python 的编译文件 pyc 又极其容易反编译

这里编译成 so 文件效果应该 ok，但会比较麻烦，兼容性也会有问题
对应的，Windows 下需要编译成 dll

    elif "\t" in base_url:
        temp = base_url.split("\t")
        base_url = temp[0]
        for _ in range(int(temp[-1])):
            run_by_single(id, base_url, path) 
            
**待填坑**

### Reference

[【转】python 打包成 so](https://www.jianshu.com/p/6690089a6229)

**2019.10.31**
