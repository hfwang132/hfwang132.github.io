---
title: "Increasing the swapfile for Linux"
date: 2023-06-12T22:59:26+08:00
draft: false
categories: ["EECS"]
tags: ["Storage/Partition", "Linux"]
---

Xilinx's toolchain consumes soooo much memory! Sometimes it causes the system to freeze... After all, my laptop only has 8GB of RAM. So there's no other choice but to add virtual memories. 

After increase the swapfile, the system performance has improved a lot:

```bash
sudo swapoff /swapfile
sudo dd if=/dev/zero of=/swapfile bs=1M count=16384
sudo mkswap /swapfile
sudo swapon /swapfile
```