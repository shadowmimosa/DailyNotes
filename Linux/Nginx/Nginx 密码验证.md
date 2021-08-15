<font size=4 face='楷体'>

## Nginx 启用密码验证

- 安装 htpasswd
  htpasswd 是开源 http 服务器 apache httpd 的一个命令工具，用于生成 http 基本认证的密码文件

  Ubuntu

  ```bash
  sudo apt-get install apache2-utils
  ```

  CentOS

  ```bash
  yum -y install httpd
  ```

- htpasswd 参数

  ```bash
  -c 创建passwdfile.如果passwdfile 已经存在,那么它会重新写入并删去原有内容.
  -n 不更新passwordfile，只将加密后的用户名密码显示在屏幕上；
  -m 默认采用MD5算法对密码进行加密
  -d 采用CRYPT算法对密码进行加密
  -p 不对密码进行进行加密，即使用普通文本格式的密码
  -s 采用SHA算法对密码进行加密
  -b 命令行中一并输入用户名和密码而不是根据提示输入密码，可以看见明文，不需要交互
  -D 删除指定的用户
  ```

- 利用 htpasswd 命令添加用户
  默认采用 MD5 加密方式

  ```bash
  # -c 指定密码文件 用户名
  htpasswd -c /usr/local/nginx/.htpasswd admin

  # 不使用交互式
  htpasswd -bc /usr/local/nginx/.htpasswd admin adminpassword
  ```

- 在原有密码文件中增加下一个用户

  ```bash
  htpasswd -b /usr/local/nginx/.htpasswd admin adminpassword
  ```

- 不更新密码文件, 只显示加密后的用户名和密码

  ```bash
  htpasswd -nb admin adminpassword
  ```

- 删除用户名和密码

  ```bash
  htpasswd -D /usr/local/nginx/.htpasswd  admin
  ```

- 修改密码
  htpasswd 并没有直接修改密码的函数，需要先使用 htpasswd 删除命令删除指定用户，再利用 htpasswd 添加用户命令创建用户即可实现修改密码的功能

  ```bash
  # 删除 admin
  htpasswd -D /usr/local/nginx/.htpasswd admin
  # 创建 admin
  htpasswd -b /usr/local/nginx/.htpasswd admin adminpassword
  ```

- Nginx 中启用密码认证

  ```bash
  location /status {
       auth_basic "Restricted"; #这里是验证时的提示信息
       auth_basic_user_file /usr/local/nginx/.htpasswd;  #这里是密码文件, 可以填写绝对路径
       vhost_traffic_status_display;
       vhost_traffic_status_display_format html;
  }
  ```

### Reference

[Nginx 中使用 htpasswd](https://blog.csdn.net/zyw_java/article/details/80561316)
[nginx配置访问密码，输入用户名和密码才能访问 nginx autoindex](https://www.cnblogs.com/faberbeta/p/nginx001.html)

**2020.09.07**
