<font size=4 face='楷体'>  

1. 安装 Git  
> yum install git  

2. 设置用户和邮箱  
> git config --global user.name'用户名'
> git config --global user.email'邮箱'  

3. 在本地仓库进行 git 初始化操作，本地仓库即拉取代码的存放位置  
> git init  

4. 链接 github 或者码云  
> git remote add origin +'githun地址'  

5. 拉取 github 上的代码  
> git pull origin +'分支'  

6. 查看修改代码或者文件  
> git status  

7. 进行代码或文件的推送   
> git add .     # '.'代表的是所有文件，当然也可以指定文件  

> git commit -m '提交说明'  

> git push origin +'分支'  


### Reference  

[linux 下使用git拉取和推送文件](https://www.jianshu.com/p/1b9715cf6a46)  