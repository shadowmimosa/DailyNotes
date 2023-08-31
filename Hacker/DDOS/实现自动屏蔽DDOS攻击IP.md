<font size=4 face='楷体'>

## 实现自动屏蔽 DDOS 攻击 IP

### 用 iptable 防止 ddos

- CTOHOM 制作的 DDoS deflate 一键安装脚本

  ```bash
  wget http://www.ctohome.com/linux-vps-pack/soft/ddos/ddos.sh
  sh ddos.sh
  ```

  ```
  netstat -ntu | awk ‘{print }’ | cut -d: -f1 | sort | uniq -c | sort -n
  ```

  ddos deflate 提供了以上查看当前连接数的 shell

- 脚本做了什么

  默认将 iptables 防火墙作为拦截工具，并将并发数改成了 60/秒就触发屏蔽 IP

  将本机 IP 都加入了 IP 白名单，然后强行不允许自动更新白名单列表。如果你需要修改 IP 白名单列表，请先执行 chattr -i /usr/local/ddos/ignore.ip.list 然后再 vi 进行修改

- 卸载

  ```bash
  wget http://www.ctohome.com/linux-vps-pack/soft/ddos/uninstall.ddos
  sh uninstall.ddos
  ```

- 安装后，可以手工运行脚本
  ```bash
  # 强行屏蔽连接数大于30的IP
  /usr/local/ddos/ddos.sh -k 30
  # 更多使用说明，请直接 more /usr/local/ddos/ddos.sh 查看
  ```

### DDoS deflate 介绍

DDoS deflate 是一款免费的用来防御和减轻 DDoS 攻击的脚本。它通过 netstat 监测跟踪创建大量网络连接的 IP 地址，在检测到某个结点超过预设的限 制时，该程序会通过 APF 或 IPTABLES 禁止或阻挡这些 IP.

[DDoS deflate 官方网站](http://deflate.medialayer.com/)

如何确认是否受到 DDOS 攻击？

```
netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n
```

执行后，将会显示服务器上所有的每个 IP 多少个连接数。
每个 IP 几个、十几个或几十个连接数都还算比较正常，如果像上面成百上千肯定就不正常了。

- 安装 DDoS deflate
  ```bash
  wget http://www.inetbase.com/scripts/ddos/install.sh //下载DDoS deflate
  chmod 0700 install.sh //添加权限
  ./install.sh //执行
  ```
- 配置 DDoS deflate
  下面是 DDoS deflate 的默认配置位于/usr/local/ddos/ddos.conf

  ```
  ##### Paths of the script and other files

  PROGDIR=”/usr/local/ddos”

  PROG=”/usr/local/ddos/ddos.sh”

  IGNORE_IP_LIST=”/usr/local/ddos/ignore.ip.list” //IP地址白名单

  CRON=”/etc/cron.d/ddos.cron” //定时执行程序

  APF=”/etc/apf/apf”

  IPT=”/sbin/iptables”

  ##### frequency in minutes for running the script

  ##### Caution: Every time this setting is changed, run the script with –cron

  ##### option so that the new frequency takes effect

  FREQ=1 //检查时间间隔，默认1分钟

  ##### How many connections define a bad IP? Indicate that below.

  NO_OF_CONNECTIONS=150 //最大连接数，超过这个数IP就会被屏蔽，一般默认即可

  ##### APF_BAN=1 (Make sure your APF version is atleast 0.96)

  ##### APF_BAN=0 (Uses iptables for banning ips instead of APF)

  APF_BAN=1 //使用APF还是iptables。推荐使用iptables,将APF_BAN的值改为0即可。

  ##### KILL=0 (Bad IPs are’nt banned, good for interactive execution of script)

  ##### KILL=1 (Recommended setting)

  KILL=1 //是否屏蔽IP，默认即可

  ##### An email is sent to the following address when an IP is banned.

  ##### Blank would suppress sending of mails

  EMAIL_TO=”root” //当IP被屏蔽时给指定邮箱发送邮件，推荐使用，换成自己的邮箱即可

  ##### Number of seconds the banned ip should remain in blacklist.

  BAN_PERIOD=600 //禁用IP时间，默认600秒，可根据情况调整
  ```

  用户可根据给默认配置文件加上的注释提示内容，修改配置文件。

- 卸载

```bash
wget http://www.inetbase.com/scripts/ddos/uninstall.ddos
chmod 0700 uninstall.ddos
./uninstall.ddos
```

- 白名单设置

  有时候默认的白名单经常有失误，为了避免这个情况，我们可以手工设置白名单的 ip，然后强制不允许修改

  ```bash
  # 手工设置白名单IP
  vi /usr/local/ddos/ignore.ip.list
  ```

  ```bash
  # 强制不允许修改
  chattr +i /usr/local/ddos/ignore.ip.list
  ```

  ```bash
  # 解除不允许修改
  chattr -i /usr/local/ddos/ignore.ip.list
  ```

- 手工用 iptables 屏蔽 IP

```bash
# 单个IP的命令
iptables -I INPUT -s 124.115.0.199 -j DROP
# 恢复单个IP：
iptables -D INPUT -s 124.115.0.199 -j DROP

# 封IP段的命令
iptables -I INPUT -s 124.115.0.0/16 -j DROP
iptables -I INPUT -s 124.115.3.0/16 -j DROP
iptables -I INPUT -s 124.115.4.0/16 -j DROP
# 封整个段的命令
iptables -I INPUT -s 124.115.0.0/8 -j DROP
# 封几个段的命令
iptables -I INPUT -s 61.37.80.0/24 -j DROP
iptables -I INPUT -s 61.37.81.0/24 -j DROP
```

### shell 脚本实现屏蔽

```bash
#!/bin/bash

# 定义要屏蔽的IP地址列表文件
block_list_file="/etc/block_list.txt"

# 如果文件不存在，则创建文件
if [ ! -f $block_list_file ]; then
    touch $block_list_file
fi

# 获取当前时间戳
timestamp=`date +%s`

# 遍历文件中的所有IP地址
while read line; do
    # 获取IP地址和上次封禁时间
    ip=`echo $line | awk '{print $1}'`
    last_block_time=`echo $line | awk '{print $2}'`

    # 如果上次封禁时间超过1小时，则重新封禁该IP地址
    if [ $((timestamp-last_block_time)) -gt 3600 ]; then
        /sbin/iptables -A INPUT -s $ip -j DROP
        # 更新封禁时间
        sed -i "s/${ip}.*/${ip} ${timestamp}/g" $block_list_file
    fi
done < $block_list_file


# 定义了一个屏蔽IP列表文件，然后通过iptables命令对列表中的IP进行封禁。
# 该脚本可以定时执行，以自动屏蔽那些频繁发起DDOS攻击的IP地址。
```

大量请求进来，服务器会处理不过来，运营商&服务器厂商也会直接封 IP

### Reference

[SHELL 脚本实现自动屏蔽 DDOS 攻击 IP](https://zhuanlan.zhihu.com/p/590610010)
[参考](http://www.ctohome.com/FuWuQi/df/318.html)
[用 iptable 防止 ddos](https://javaforall.cn/140492.html)

**2023.03.12**
