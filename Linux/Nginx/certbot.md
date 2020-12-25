<font size=4 face='楷体'>

## Certbot 自动 https 证书

[官网](https://certbot.eff.org/)

### 安装&使用

-   Install [snapd](https://snapcraft.io/docs/installing-snap-on-centos)
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

-   Ensure that your version of snapd is up to date
    ```bash
    $ sudo snap install core; sudo snap refresh core
    ```
-   Remove any Certbot OS packages

    ```bash
    # CentOS 8
    $ sudo dnf remove certbot
    # CentOS 7
    $ sudo yum remove certbot.
    # or
    $ sudo apt-get remove certbot
    ```

-   Install Certbot
    ```bash
    $ sudo snap install --classic certbot
    ```
-   Prepare the Certbot command

    ```bash
    $ sudo ln -s /snap/bin/certbot /usr/bin/certbot
    ```

-   Run Certbot

    ```bash
    # Certbot edit your Nginx configuration automatically
    $ sudo certbot --nginx
    # just get a certificate
    $ sudo certbot certonly --nginx
    ```

-   Test automatic renewal

    ```bash
    $ sudo certbot renew --dry-run
    ```

    renew certbot is installed in one of the following locations

    ```bash
    /etc/crontab/
    /etc/cron.*/*
    systemctl list-timers
    ```

-   Confirm that Certbot worked

### docker & certbot

[这里](https://www.cnblogs.com/txb1989/p/13079961.html)

### Reference

[Nginx on CentOS/RHEL 8](https://certbot.eff.org/lets-encrypt/centosrhel8-nginx)

**2020.11.30**
