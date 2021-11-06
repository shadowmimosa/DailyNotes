<font size=4 face='楷体'>

## WSL2 安装 docker

### 原生 linux 安装 docker 方式

```bash
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
$ sudo service docker start
```

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository    "deb [arch=amd64] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt update
apt list --upgradable
sudo apt install -y docker-ce
sudo service docker start
docker run hello-world
```

### Docker Desktop for windows 方式

不优雅 略过

### Reference

[win10 利用 WSL2 安装 docker 的 2 种方式](https://www.pianshen.com/article/65361454253/)

**2020.11.18**
