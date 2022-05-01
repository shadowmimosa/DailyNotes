<font size=4 face='楷体'>

## Git 中撤销 commit

```bash
# 本地提交
git add file
git commit -m ""

# HEAD^ 表示上一个版本
# --soft 不删除工作空间的改动代码, 撤销 commit, 不撤销 add
git reset --soft HEAD^
# --hard 删除工作空间的改动代码, 撤销 commit 且撤销 add
git reset --soft HEAD^

# 修改 commit 注释
git commit --amend
```

## Reference

[git commit后，如何撤销commit](https://www.jianshu.com/p/a9f327da3562)

**2021.05.12**
