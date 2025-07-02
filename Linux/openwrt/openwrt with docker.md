---
created: 2023-12-06T19:23:55 (UTC +08:00)
tags: [Docker,OpenWrt,macvlan]
source: https://zhuanlan.zhihu.com/p/113664215
author: 
---

# Openwrt 下 Docker 网络食用方法 - 知乎

> ## Excerpt
> Bridge 网络Docker 使用 Bridge 网络时，会创建docker0 网桥，用于连接容器，然后 docker0 通过 NAT 转发访问外部网络，具体细节在这里就不赘述了。 当容器进行映射时，Docker 会自动添加 DNAT 进行转发，实现访问…

---
## Bridge 网络

Docker 使用 `Bridge` 网络时，会创建docker0 网桥，用于连接容器，然后 `docker0` 通过 `NAT` 转发访问外部网络，具体细节在这里就不赘述了。 当容器进行映射时，Docker 会自动添加 `DNAT` 进行转发，实现访问宿主机端口的时候，将流量转发到容器内部。

在普通宿主机中使用 `Docker Bridge` 网络没有任何问题，但是，如果宿主机是网关，或者 `Openwrt` 的时候，`WAN` 口也能轻松访问容器暴露出来的端口，带来很大的安全问题。

### WAN 口访问的控制

所以核心问题是阻止 `WAN` 口访问，此前也有大佬 LEAN 采用阻止 `Docker` 操作 iptables的方案，这个方法简单粗暴，Docker 就不会添加 `DNA`T 转发，当然不存在端口暴露问题，但是带来的问题也有不少，有几率存在没有给 `docker0` 做 `SNAT` 导致整个 `bridge` 网络下的容器都无法联网，实现下来还有其他一些奇奇怪怪的问题。

对于这种问题，Docker 官方的这篇[文档](https://zhuanlan.zhihu.com/p/113664215/Docker%20and%20iptables)给出了解决方案 下面就针对 `Openwrt` 来实现访问控制：

```text
# 新建 DOCKER-MAN 自定义链
iptables -N DOCKER-MAN

# 挟持 DOCKER-USER 转到 DOCKER-MAN 自定义链
iptables -I DOCKER-USER -j DOCKER-MAN

# 若流量来自 br-lan 放行，目的是 `LAN` 口可以访问容器暴露的端口
iptables -A DOCKER-MAN -i br-lan -o docker0 -j RETURN

# 阻止所有新建以及无效的连接。
iptables -A DOCKER-MAN -m conntrack --ctstate NEW,INVALID -o docker0 -j DROP

# 接受容器主动访问的流量，目的是容器能够联网。
iptables -A DOCKER-MAN -m conntrack --ctstate ESTABLISHED,RELATED -o docker0 -j RETURN
iptables -A DOCKER-MAN -j RETURN
```

这样一来，LAN 口是可以访问容器暴露的端口，对与其他`接口`，容器主动访问不受限制，而外面是无法直接访问容器的，做到了单项访问。

到这里，又有问题来了，如果我有一个容器比如 `qBittorrent`，暴露的端口就是希望从外部(公司)等管理的，这样一来就无法访问了，当然也有解决方案：

```text
# 在 DOCKER-MAN 自定义链加入对 172.17.0.9 的放行
iptables -I DOCKER-MAN -d 172.17.0.9 -o docker0 -j RETURN
```

这样一来，这个容器就可以被正常访问了

最后一个问题，`Bridge` 网络下面的 `ip` 地址不是固定的，每次重启 `Docker daemon` 都有可能改变容器的 ip 这样手动操作起来就相对比较麻烦了，所以在 [luci-app-dockerman](https://link.zhihu.com/?target=https%3A//github.com/lisaac/luci-app-dockerman)中加入了`访问控制`选项，可以轻松实现对容器的访问控制

## Macvlan 网络

Macvlan 网络的真的是好处多多，有兴趣的同学自己翻阅资料查看，使用 `macvlan` 网络就基本和虚拟机的桥接模式类似，而且不存在 `Bridge` 网络的端口暴露的风险，在 `Openwrt` 下使用 `macvlan` 网络最大的问题就是无法上网的问题。

这里讲一个简单的方案，首先通过 `Docker` 新建 `macvlan` 网络

```bash
docker network create -d macvlan \
  --subnet=192.168.3.0/24 --gateway=92.168.3.1 \
  -o parent=br-lan \
  -o macvlan_mode=bridge \
  macnet
```

请注意这里的`subnet`不要和其他接口冲突（若要使用同网段后面会讲），`parent`使用`br-lan`，然后在 `Openwrt` 上创建 `macvlan` 设备

```text
ip link add link br-lan docker_mac0 type macvlan mode bridge
ip link set docker_mac0 up
```

接下来 `Openwrt` 中添加接口，你也可以在 `luci` 中添加

```text
uci set network.docker_mac0=interface
uci set network.docker_mac0.ifname=docker_mac0
uci set network.docker_mac0.proto=static
uci set network.docker_mac0.ipaddr=192.168.3.1
uci set network.docker_mac0.netmask=255.255.255.0
uci commit network
```

至此，`Docker macvlan` 网络就可以正常使用了，这个步骤相对比较简单，但是网络重启或者 `Openwrt` 重启的时候就会失效，解决这个问题，已经在 [luci-app-dockerman](https://zhuanlan.zhihu.com/p/113664215/lisaac/luci-app-dockerman) 实现，当创建 `macvlan` 网络时，dockerman 会自动做好这些工作，网络重启也会自动添加，删除网络，则会自动删除创建的 `macvlan` 网络。

### Macvlan 进阶

有些老哥觉得用这个方案 `macvlan` 网络，使用的是与 `LAN` 不同的网段，访问容器会存在转发。 解决这个其实很简单，禁用 br-lan 的 DHCP, 同时开启 `docker_mac0` 的 `DHCP` 就可以，这样路由器下的所有主机和容器内的所有主机都在同一个网段之下了。 所以，如果你开始就想用这个进阶方案的话，从创建 `macvlan` 网络的时候就应该规划好自己偏好的网段。

好了，分享就这么多，感谢捧场
