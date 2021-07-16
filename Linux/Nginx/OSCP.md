<font size=4 face='楷体'>

## 临时处理 OCSP 域名无法访问的问题

近期由于众所周知的原因，[国内无法直接访问 Let's Encrypt 的 OSCP 域名](https://v2ex.com/t/658605)，导致出现了不能签发证书、OCSP Stapling 失败、网页打开慢等问题。
经检查目前是 ocsp.int-x3.letsencrypt.org 的 cname 域名 a771.dscq.akamai.net 受到了干扰，可以采用本地修改 hosts 的方案进行临时处理。
在/etc/hosts 中添加

```
    23.32.3.72     ocsp.int-x3.letsencrypt.org
```

获取 OCSP 响应

```
    openssl ocsp -no_nonce \
                 -respout /path/to/certs/holmesian.org/ocsp_res.der \
                 -issuer /path/to/certs/holmesian.org/ca.cer \
                 -cert /path/to/certs/holmesian.org/holmesian.org.cer \
                 -url http://ocsp.int-x3.letsencrypt.org/ \
                 -header "HOST" "ocsp.int-x3.letsencrypt.org"

```

-cert 、 -issuer 、 -CAfile 分别对应的是子证书、中间证书、根证书，其实全部使用 acme.sh 文件夹中的 fullchain.cer 也是可以的。
-respout 是 OCSP 响应保存位置，将这个位置填入在 nginx 配置文件的 ssl_stapling_file 中，如下开启 ssl_stapling。
这里如果出现如下错误的话，说明你的[openssl 使用了 1.1.0 版本](https://github.com/h2o/h2o/pull/1270)，这个时候已经不需要指定 HOST，把上面命令中的“-header "HOST" "ocsp.int-x3.letsencrypt.org"”删掉就好了。

```
Missing = in header key=value
ocsp: Use -help for summary.
```

```
    ssl_stapling on;
    ssl_stapling_verify on;
    ssl_stapling_file /root/.acme.sh/*.holmesian.org_ecc/ocsp_res.der;
```

重载 nginx 服务之后，检查是否成功开启。

```
    openssl s_client -connect holmesian.org:443 -status -tlsextdebug < /dev/null 2>&1 | grep -i "OCSP response"
```

最后将有关操作制成脚本，添加到 crontab 中自动更新。

### Reference

[临时处理 OCSP 域名无法访问的问题](https://holmesian.org/letsencrypt-ocsp-fix)
[OCSP check failed for /xxx/cert1.pem (are we offline?)](https://goodmemory.cc/ocsp-check-failed-for-xxx-cert1-pem-are-we-offline/)

**2020.12.01**
