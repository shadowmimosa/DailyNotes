### Git bash
- $ git config --global user.name "Your Name"
- $ git config --global user.email "email@example.com"

### build repository（版本库）
- $ mkdir git  
- $ cd git
- $ pwd
- /c/Users/ShadowMimosa/desktop/stu/top/git

### 管理版本库
- $ git init  
### 添加到仓库
- $ git add xxx
### 提交到仓库，备注xxx
- git commit -m "xxx"
### 查看状态
- git status
## 查看修改
- git diff
### 查看提交日志（从最近到最远的）
- git log 可加参数（--pretty=oneline）
### 查看命令历史
- git reflog
### 回退版本
- git reset --hard HEAD^ (HEAD^^,HEAD~100)
### 回退某一版本
- git reset --hard commit_id
### 读文件
- cat xxx
### 
