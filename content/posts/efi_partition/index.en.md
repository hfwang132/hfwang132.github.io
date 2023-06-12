---
title: "Mounting the EFI partition in Windows OS"
date: 2023-06-12T22:26:16+08:00
draft: false
categories: ["CS"]
tags: ["Storage/Partition", "Linux"]
---

To mount the EFI partitions, run the following commands in PowerShell:

```powershell
diskpart
list disk  # make sure which is the disk that contains the EFI partition. usually 0
select disk 0
list partition # make sure which is the EFI partition. normally 0
select disk 0
assign letter=z
```

Then we will mount the EFI partition as drive Z.

This operation may be useful when using a dual-boot system with Windows and Ubuntu: Sometimes, after removing the Ubuntu system, only the Windows system remains, but the GRUB interface still appears every time the computer boots. In this case, you need to delete the old Ubuntu EFI partition.
