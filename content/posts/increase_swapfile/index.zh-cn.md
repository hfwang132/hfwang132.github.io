---
title: "给 Linux 增加 swapfile"
date: 2023-06-12T22:59:29+08:00
draft: false
categories: ["CS"]
tags: ["存储/分区", "Linux"]
---

Xilinx 的工具链也太占内存了，有时候会导致系统死机。。毕竟我这个小破本才 8G 内存。没办法，只能加虚拟内存了。

增加了 swapfile 之后就好很多了：

```bash
sudo swapoff /swapfile
sudo dd if=/dev/zero of=/swapfile bs=1M count=16384
sudo mkswap /swapfile
sudo swapon /swapfile
```