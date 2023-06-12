---
title: "在 Windows 中挂载 EFI 分区的方法"
date: 2023-06-12T22:17:46+08:00
draft: false
categories: ["EECS"]
tags: ["存储/分区", "Linux"]
---

为了在 Windows 中挂载 EFI 分区，我们可以在 PowerShell 中运行如下命令

```powershell
diskpart
list disk  # make sure which is the disk that contains the EFI partition. usually 0
select disk 0
list partition # make sure which is the EFI partition. normally 0
select disk 0
assign letter=z
```

然后我们就将 EFI 挂载为盘符为 Z 的盘了。

使用 Windows + Ubuntu 双系统时可能会用到这个操作：有时候，移除了 Ubuntu 系统之后，只留下 Windows 系统，但每次开机时仍然会弹出 grub 界面。这个时候就需要将旧的 ubuntu EFI 分区给删掉。
