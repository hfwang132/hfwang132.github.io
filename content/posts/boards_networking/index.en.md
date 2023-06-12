---
title: "Access the Internet from evaluation boards via PC"
date: 2023-06-12T23:22:45+08:00
draft: false
categories: ["EECS"]
tags: ["Networking", "Linux"]
---

### Windows

Set a network adapter that can access the internet in the Control Panel and share it with Ethernet. The IP address of Ethernet will change to `192.168.137.1` (this is the default behavior in Windows).

Then, set the gateway as `192.168.137.1` in the terminal of the development board:

`sudo route add default gw 192.168.137.1`

Set the IP address as `192.168.137.x`, where x is any value except 1 and 255 (gateway address and broadcast address):

`sudo ifconfig <your-ifdev> 192.168.3.x`

If it still doesn't work, check if the DNS in `/etc/resolv.conf` is correct. You can add a line:

`nameserver 8.8.8.8`

### Ubuntu

Change the IPv4 of Ethernet in the PC's network settings to shared mode. The IP address of Ethernet will change to `10.42.0.1` (this is default in Ubuntu Linux, but I'm not sure if it is the same in other Linux distributions).

Then, set the gateway as `10.42.0.1` in the terminal of the development board:

`sudo route add default gw 10.42.0.1`

Set the IP address to any IP within the same subnet, as long as the subnet part of the IP is not the gateway address and broadcast address:

`sudo ifconfig 10.42.0.2`

If it still doesn't work, check if the DNS in `/etc/resolv.conf` is correct. You can add a line:

`nameserver 8.8.8.8`

### Troubleshooting

First, check if you can ping the host. If you can't ping the host, the gateway may not be set correctly.

If you can ping the host but not the external IP, it may be because you haven't shared the Ethernet for the development board in the PC, or the proxy is not set correctly, or the gateway is not set correctly.

If you can ping the external IP but not the domain name, it is most likely a DNS configuration issue.
