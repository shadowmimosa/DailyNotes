<font size=4 face='楷体'>

## crontab 获取环境变量

crontab 执行脚本获取不到用户全局变量,通过查阅资料获知 crontab 载入配置的时候 并未载入 /etc/profile
针对这个现象 初期解决方式是在 crontab 任务内添加配置文件载入
```bash
* * * * * source /etc/profile && command
或
* * * * * export PHP_ENV=prod && command
或
* * * * * /home/user_name/task.sh && command
```
之后发现配置文件的载入顺序

-   /etc/environment

> 是系统在登录时读取的第一个文件，用于为所有进程设置环境变量。系统使用此文件时并不是执行此文件中的命 令，而是根据KEY=VALUE模式的代码，对KEY赋值以VALUE，因此文件中如果要定义PATH环境变量，只需加入一行形如 PATH=$PATH:/xxx/bin的代码即可。

-   /etc/profile

> 是系统登录时执行的第二个文件，可以用于设定针对全系统所有用户的环境变量。

-   ~/.profile

> 是对应当前登录用户的profile文件，用于定制当前用户的个人工作环境。

-   /etc/bash.bashrc

> 是针对所有用户的bash初始化文件，在此中设定的环境变量将应用于所有用户的shell中，此文件会在用户每次打开shell时执行一次。

-   ~/.bashrc

> 是对应当前登录用户的bash初始化文件，当用户每次打开shell时，系统都会执行此文件一次。


### Reference

[Linux Crontab 获取环境变量](https://www.jianshu.com/p/202e95eb79be)

**2024.09.23**
