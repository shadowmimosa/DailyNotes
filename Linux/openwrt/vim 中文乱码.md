<font size=4 face='楷体'>

## openwrt vim 打开中文乱码

openwrt 默认安装的其实并不是 vim, 而是 vi, 只是一个别名

```bash
 [ -x /usr/bin/vim ] && alias vi=vim || alias vim=vi
```

通过 `type` 可以查看

```bash
type vim
# vim is /usr/bin/vi
```

### 安装完整版 vim

```bash
# 确保已经更新过了
opkg update
# 安装 vim 环境
opkg install vim-full vim-runtime
# 取消之前定义的别名
unalias vim
```

### 设置中文编码

```bash
vim ~/.vimrc

echo "set termencoding=utf-8" >> filename.txt
echo "set encoding=utf8" >> filename.txt
echo "set fileencodings=utf8,ucs-bom,gbk,cp936,gb2312,gb18030" >> filename.txt
```

### Reference

[openwrt vim 打开中文乱码](https://blog.csdn.net/huangfu6long/article/details/124888878)

**2023.09.11**
