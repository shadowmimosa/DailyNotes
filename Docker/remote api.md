<font size=4 face='楷体'>

## Docker Remote API

Docker 开放远程访问一般有两种

- 2375 端口: 没有加密
- 2376 端口: TLS 认证

即使是在测试服务器依然**强烈不建议**使用未加密的 2375 端口并开放公网
_血与泪的教训, 第二天就被黑了_

- 生成密钥证书脚本

  ```bash
  #!/bin/bash

  # 相关配置信息
  SERVER="输入你的服务器外网IP"
  PASSWORD="输入你的密码"
  COUNTRY="CN"
  STATE="输入你的省份"
  CITY="输入你的城市"
  ORGANIZATION="输入你的组织"
  ORGANIZATIONAL_UNIT="Dev"
  EMAIL="输入你的邮箱"

  ### 开始生成文件 ###
  echo "开始生成文件"

  # 切换到生产密钥的目录
  cd /opt/docker_ca
  # 生成ca私钥(使用aes256加密)
  openssl genrsa -aes256 -passout pass:$PASSWORD  -out ca-key.pem 4096
  # 生成ca证书，填写配置信息
  openssl req -new -x509 -passin "pass:$PASSWORD" -days 365 -key ca-key.pem -sha256 -out ca.pem -subj "/C=$COUNTRY/ST=$STATE/L=$CITY/O=$ORGANIZATION/OU=$ORGANIZATIONAL_UNIT/CN=$SERVER/emailAddress=$EMAIL"

  # 生成server证书私钥文件
  openssl genrsa -out server-key.pem 4096
  # 生成server证书请求文件
  openssl req -subj "/CN=$SERVER" -sha256 -new -key server-key.pem -out server.csr
  # 配置白名单，多个用逗号隔开
  sh -c 'echo subjectAltName = IP:'$SERVER',IP:0.0.0.0 >> extfile.cnf'
  # 把 extendedKeyUsage = serverAuth 键值设置到extfile.cnf文件里，限制扩展只能用在服务器认证
  sh -c 'echo extendedKeyUsage = serverAuth >> extfile.cnf'
  # 使用CA证书及CA密钥以及上面的server证书请求文件进行签发，生成server自签证书
  openssl x509 -req -days 365 -sha256 -in server.csr -CA ca.pem -CAkey ca-key.pem -passin "pass:$PASSWORD" -\CAcreateserial -out server-cert.pem -extfile extfile.cnf

  # 生成client证书RSA私钥文件
  openssl genrsa -out key.pem 4096
  # 生成client证书请求文件
  openssl req -subj '/CN=client' -new -key key.pem -out client.csr
  # 继续设置证书扩展属性
  sh -c 'echo extendedKeyUsage = clientAuth >> extfile.cnf'
  # 生成client自签证书（根据上面的client私钥文件、client证书请求文件生成）
  openssl x509 -req -days 365 -sha256 -in client.csr -CA ca.pem -CAkey ca-key.pem -passin "pass:$PASSWORD" -\CAcreateserial -out cert.pem -extfile extfile.cnf

  # 更改密钥权限
  chmod 0400 ca-key.pem key.pem server-key.pem
  # 更改密钥权限
  chmod 0444 ca.pem server-cert.pem cert.pem
  # 删除无用文件
  rm client.csr server.csr

  echo "生成文件完成"
  ```

  注: 多个 IP 白名单配置 `SERVER="49.243.231.200,IP:172.17.0.1,DNS:docker.mysite.com"`

- 修改 Docker 配置

  ```bash
  vim /lib/systemd/system/docker.service
  ```

  在 ExecStart 的 /usr/bin/dockerd 后面加\, 然后添加配置，如下

  ```conf
  ExecStart=/usr/bin/dockerd \
          --tlsverify \
          --tlscacert=/opt/docker_ca/ca.pem \
          --tlscert=/opt/docker_ca/server-cert.pem \
          --tlskey=/opt/docker_ca/server-key.pem \
          -H tcp://0.0.0.0:2376 \
          -H unix:///var/run/docker.sock \
          -H fd:// --containerd=/run/containerd/containerd.sock
  ```

- 重启 Docker
  将 2376 端口添加到安全组然后重启 Docker
  ```bash
  systemctl daemon-reload && systemctl restart docker
  ```

### Reference

[[Shell]Docker remote api 未授权访问漏洞(Port=2375)](https://www.cnblogs.com/-mo-/p/11529387.html)
[Docker 开启 2376 端口](https://blog.csdn.net/Assassin_EZI0/article/details/105167118)
[centos7 docker 配置 TLS 认证的远程端口的证书生成教程（shell 脚本一键生成）](https://blog.csdn.net/qq_21187515/article/details/90268345)

**2020.09.07**
