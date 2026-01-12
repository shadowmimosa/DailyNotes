# N150 主机 PVE9 配置核显直通

## 支持情况

```bash
后缀带F为没核显型号也不行
常见支持列表:
N100 N150 N200 N350 N355 8505
I3 12XXX 13XXX 14XXX
I5 12XXX 13XXX 14XXX
I7 12XXX 13XXX 14XXX
I9 12XXX 13XXX 14XXX
U5 245 U7 265 U9 285
```

```bash
确认支持列表Meteor-lake确认支持:
###Meteor-lake确认支持:https://github.com/strongtz/i915-sriov-dkms/issues/210#issuecomment-2701882332
https://www.intel.com/content/www/us/en/ark/products/codename/232598/products-formerly-alder-laken.html
https://www.intel.com/content/www/us/en/ark/products/codename/238004/products-formerly-twin-lake.html
https://www.intel.com/content/www/us/en/ark/products/codename/147470/products-formerly-alder-lake.html
https://www.intel.com/content/www/us/en/ark/products/codename/215599/products-formerly-raptor-lake.html
https://www.intel.com/content/www/us/en/ark/products/series/241071/intel-core-ultra-processors-series-2.html
https://www.intel.com/content/www/us/en/ark/products/codename/90353/products-formerly-meteor-lake.html
```

## 替换源（可选）

```bash
# 替换默认PVE9源 PS:不带ceph源
wget http://share.geekxw.top/pve9yuan.sh -O pve9yuan.sh && chmod +x pve9yuan.sh && ./pve9yuan.sh
# 更新源
apt update
```

## 配置核显

在[i915-sriov-dkms](https://github.com/strongtz/i915-sriov-dkms/releases)下载最新驱动

```bash
nano /etc/default/grub
# GRUB_CMDLINE_LINUX_DEFAULT 后面追加
i915.enable_guc=3 i915.max_vfs=7 module_blacklist=xe
```

## 配置虚拟化

```bash
# 安装依赖
apt install -y build-essential git dkms sysfsutils proxmox-headers-$(uname -r) intel-gpu-tools

# 配置虚拟化数量
echo "devices/pci0000:00/0000:00:02.0/sriov_numvfs = 7" >> /etc/sysfs.conf
```

```bash
# 更新配置
update-grub
```

```bash
# 重启生效
reboot
# 查看虚拟显卡
lspci | grep VGA
```

**不要勾选全部功能，或者直通物理核显** 否则虚拟化将失效，需要重启恢复

## 参考资料

- [Bilibili 教程视频](https://www.bilibili.com/video/BV1mtvNzwEis)
- [PVE9.x 开启 Intel 核显 SR-IOV 保姆级教程](https://www.geekxw.top/3324/)
