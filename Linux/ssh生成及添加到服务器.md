<font size=4 face='楷体'>

## ssh 生成及添加到服务器

### 本地生成 ssh key

```bash
ssh-keygen -t rsa -b 4096
```

生成路径在

- MacOS/Linux
  `~/.ssh/id_rsa.pub`
- Win
  `~/.ssh\id_rsa.pub`

### 上传服务器

- MacOS / Linux

  ```bash
  ssh-copy-id your-user-name-on-host@host-fqdn-or-ip-goes-here
  ```

- Win

  ```bash
  # 自动
  $REMOTEHOST="your-user-name-on-host@host-fqdn-or-ip-goes-here"

  scp "$env:USERPROFILE\.ssh\id_rsa.pub" "${REMOTEHOST}:~/tmp.pub"
  ssh "$REMOTEHOST" "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat ~/tmp.pub >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys && rm -f ~/tmp.pub"

  # 手动
  mkdir -p ~/.ssh && chmod 700 ~/.ssh
  sudo vim ~/.ssh/authorized_keys
  chmod 600 ~/.ssh/authorized_keys
  ```

### Reference

[ssh 生成及添加到服务器](https://www.jianshu.com/p/fc8102b5e163)

**2021.04.28**
