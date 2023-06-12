---
title: "开发板通过 PC 连接互联网"
date: 2023-06-12T23:22:42+08:00
draft: false
categories: ["EECS"]
tags: ["网络", "Linux"]
---

### Windows

在控制面板中设置能上网的网卡，共享给以太网。此时以太网的 IP 会变成 `192.168.137.1`。

然后在开发板终端中设置网关为 `192.168.137.1` 即可：

`sudo route add default gw 192.168.137.1`

IP 设置为 `192.168.137.x`，x 不是 1 和 255（网关地址和广播地址）就行：

`sudo ifconfig <your-ifdev> 192.168.3.x`

如果还是不行，要检查一下 `/etc/resolv.conf` 里的 DNS 对不对，可以加一行：

`nameserver 8.8.8.8`

### Ubuntu

在 PC 的网络设置里，将以太网的 IPv4 一栏改为共享方式。此时以太网的 IP 会变成 `10.42.0.1`（在 Ubuntu Linux 上是这样，其他 Linux 分发版我就不清楚了）。

然后在开发板终端中设置网关为 `10.42.0.1` 即可：

`sudo route add default gw 10.42.0.1` 

IP 设置为同一个子网下的任意一个 IP，只要 IP 的子网部分不是网关地址和广播地址就行：

`sudo ifconfig 10.42.0.2`

如果还是不行，要检查一下 `/etc/resolv.conf` 里的 DNS 对不对，可以加一行：

`nameserver 8.8.8.8`

### 错误排查

先看能不能 ping 通主机。如果不能 ping 通主机，可能是网关没有设置对。

如果能 ping 通主机但是不能 ping 通外网 IP，可能是没有在 PC 里给开发板以太网设置共享，也可能是代理没有设置正确，也可能是网关没有设置对。

如果能 ping 通外网 IP，但是不能 ping 通域名，基本上就是 DNS 配置的问题。