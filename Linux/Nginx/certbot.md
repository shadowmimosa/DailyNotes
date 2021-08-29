<font size=4 face='楷体'>

## Certbot 自动 https 证书

[官网](https://certbot.eff.org/)

### 安装&使用

- Install [snapd](https://snapcraft.io/docs/installing-snap-on-centos)
  Adding EPEL

  ```bash
  CentOS 8
  $ sudo dnf install epel-release
  $ sudo dnf upgrade

  CentOS 7
  $ sudo yum install epel-release
  ```

  Installing snapd

  ```bash
  # install the snapd package
  $ sudo yum install snapd
  # enable the main snap communication socket
  $ sudo systemctl enable --now snapd.socket
  # create a symbolic link
  $ sudo ln -s /var/lib/snapd/snap /snap
  ```

- Ensure that your version of snapd is up to date

  ```bash
  sudo snap install core; sudo snap refresh core
  ```

- Remove any Certbot OS packages

  ```bash
  # CentOS 8
  $ sudo dnf remove certbot
  # CentOS 7
  $ sudo yum remove certbot.
  # or
  $ sudo apt-get remove certbot
  ```

- Install Certbot

  ```bash
  sudo snap install --classic certbot
  ```

- Prepare the Certbot command

  ```bash
  sudo ln -s /snap/bin/certbot /usr/bin/certbot
  ```

- Run Certbot

  ```bash
  # Certbot edit your Nginx configuration automatically
  $ sudo certbot --nginx
  # just get a certificate
  $ sudo certbot certonly --nginx
  ```

- Test automatic renewal

  ```bash
  sudo certbot renew --dry-run
  ```

  renew certbot is installed in one of the following locations

  ```bash
  /etc/crontab/
  /etc/cron.*/*
  systemctl list-timers
  ```

- Confirm that Certbot worked

### docker & certbot

参考[这里](https://www.cnblogs.com/txb1989/p/13079961.html)
[官方](https://certbot.eff.org/docs/install.html#running-with-docker)

### cretbot-auto

```bash
# certbot-auto 生成 nginx 证书指定 nginx 配置路径
./certbot-auto --nginx --nginx-server-root=/usr/local/nginx/conf
```

### 报错

> expected ../cert.pem to be a symlink, Renewal configuration file ....conf is broken

- 原因
  更换服务器后 /etc/letsencrypt/live/xxx.com/cert.pem 等文件不是软连接了, 造成更新失败

- 解决

  ```bash
  cd /etc/letsencrypt/
  chmod -R 0755 live/
  chmod -R 0755 renewal/
  chmod -R 0755 archive/

  cd live/xxx.com/
  rm ./*.*
  ln -s ../../archive/xxx.com/cert1.pem .
  ln -s ../../archive/xxx.com/chain1.pem .
  ln -s ../../archive/xxx.com/fullchain1.pem .
  ln -s ../../archive/xxx.com/privkey1.pem .

  mv cert1.pem cert.pem
  mv chain1.pem chain.pem
  mv fullchain1.pem fullchain.pem
  mv privkey1.pem privkey.pem

  cd /etc/letsencrypt/
  ```

  再次尝试更新

  ```bash
  certbot update_symlinks
  certbot renew
  ```

- [参考](https://blog.csdn.net/qq285744011/article/details/90214729)

### Reference

[Nginx on CentOS/RHEL 8](https://certbot.eff.org/lets-encrypt/centosrhel8-nginx)

**2020.11.30**
