---
title: "在 Linux 中给 SD 卡分区并创建文件系统"
date: 2023-06-12T22:43:39+08:00
draft: false
categories: ["CS"]
tags: ["存储/分区", "Linux"]
---

为了在 Linux 中给 SD 卡分区和格式化，先将 SD 卡接入 PC，然后在 bash 命令行使用 `fdisk` 给 SD 卡分区，最后使用 `mkfs` 给 SD 卡创建文件系统（即格式化）。

主要命令如下：

首先，使用 `sudo fdisk -l` 确认 SD 卡对应 `/dev` 中的哪一个设备。

接着，假设我们已经确定 SD 卡对应 `/dev/sde`，那么我们可以输入 `sudo fdisk /dev/sde` 来开始分区操作：

- 输入 `d` 来删除分区。不断输入，直到所有分区被删除。
- 输入 `n` 来创建第一个分区，作为启动分区。
- 输入 `t` 来将分区类型改成 `W95 FAT32`。启动分区一般都是这个类型。。
- 输入 `a` 来将分区设置为启动分区。
- 输入 `n` 来创建第二个分区，作为根文件系统分区。
- 由于根文件系统分区类型一般是 `Linux`，而默认的分区类型正是 `Linux`，因此无需再输入 `t` 来改变分区类型。

最后，在分好区之后，我们就可以来创建文件系统了：

```bash
sudo mkfs.vfat -F 32 -n "BOOT" /dev/sde1
sudo mkfs.ext4 -L "rootfs" /dev/sde2
```

其中第一行为启动分区创建 FAT32 文件系统，并将其命名为 `BOOT`；第二行为根文件系统分区创建 ext4 文件系统，并将其命名为 `rootfs`。
