<font size=4 face='楷体'>

## nvm 使用

### 安装 nvm

- 安装包下载安装
  [nvm for Window](https://github.com/coreybutler/nvm-windows/releases)

- nvm 安装成功验证

  ```bash
  nvm version
  ```

- nvm 配置
  NVM 文件夹可以看到 NVM 的一些文件 (注意, 此后安装的 NPM 都会存放在 NVM 文件夹里，是以 Node 的版本号命名的文件夹)
  可以修改 NVM 文件夹的 settings.txt 文件
  ```yaml
  root:
  path:
  #下面的是追加的镜像地址
  node_mirror: https://npmmirror.com/mirrors/node/
  npm_mirror: https://npmmirror.com/mirrors/npm/
  ```

### 用 nvm 安装 node, npm

```bash
# 安装最新node, npm
nvm install latest

# 切换node
nvm use '版本号'

# 验证node
node -v

# 验证node
npm -v
```

### Reference

[nvm 安装 node 及 npm](https://blog.csdn.net/qq_41939859/article/details/120180144)

**2022.07.27**
