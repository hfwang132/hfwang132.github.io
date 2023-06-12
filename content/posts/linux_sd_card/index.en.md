---
title: "Partitioning and Formatting SD Cards with Linux"
date: 2023-06-12T22:43:36+08:00
draft: false
categories: ["CS"]
tags: ["Storage/Partition", "Linux"]
---

To partition and format an SD card in Linux, follow these steps: First, connect the SD card to your PC. Then, use the fdisk command in the bash command line to partition the SD card. Finally, use the mkfs command to create a file system (format) on the SD card.

The main commands are as follows:

First, use `sudo fdisk -l` to confirm which device in `/dev` corresponds to the SD card.

Assuming we have determined that the SD card corresponds to `/dev/sde`, we can enter `sudo fdisk /dev/sde` to start the partitioning operation:

Enter `d` to delete partitions. Keep entering until all partitions are deleted.

Enter `n` to create the first partition as the boot partition.

Enter `t` to change the partition type to `W95 FAT32`. Boot partitions are generally of this type.

Enter `a` to set the partition as the boot partition.

Enter `n` to create the second partition as the root file system partition.

Since the root file system partition type is usually `Linux`, and the default partition type is already `Linux`, there is no need to enter `t` to change the partition type.

Finally, after partitioning, we can create the file systems:

```bash
sudo mkfs.vfat -F 32 -n "BOOT" /dev/sde1
sudo mkfs.ext4 -L "rootfs" /dev/sde2
```

In the above code, the first line creates a FAT32 file system for the boot partition and names it as `BOOT`. The second line creates an ext4 file system for the root file system partition and names it as `rootfs`.
