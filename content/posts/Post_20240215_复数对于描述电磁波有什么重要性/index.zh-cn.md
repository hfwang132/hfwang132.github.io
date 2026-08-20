---
title: "复数对于描述电磁波有什么重要性？"
date: 2024-02-15T23:46:31+08:00
originalURL: "https://www.zhihu.com/question/614307607/answer/3397335289"
aliases:
  - "/complex_numbers_in_em/"
  - "/Post_20240216_复数对于描述电磁波有什么重要性/"
draft: false
tags: ["量子光学"]
categories: ["量子信息/量子光学"]
author: "Haifei"
---

在经典力学中，复数只是一个用来简化计算的数学技巧。

在量子力学中，复数不再只是一个数学技巧，而是有一定的物理意义。考虑经典矢势：

$\begin{aligned} \mathbf{A}(\mathbf{r},t)=\sum_{\mathbf{k}\lambda} \left( A_{\mathbf{k}\lambda}e^{i(\mathbf{k}\cdot\mathbf{r}-\omega_{\mathbf{k}}t)} + \text{c.c.}\right)\mathbf{e}_{\mathbf{k}\lambda} \end{aligned}$ 


> 其中 $\mathbf{k}$ 和 $\lambda$ 分别代表空间模式和偏振模式

对其进行量子化得到海森堡表象下的矢势算子：

$\begin{aligned} \mathbf{A}(\mathbf{r},t)=\sum_{\mathbf{k}\lambda} \left( C_{\mathbf{k}\lambda}\hat{a}_{\mathbf{k}\lambda}e^{i(\mathbf{k}\cdot\mathbf{r}-\omega_{\mathbf{k}}t)} + C_{\mathbf{k}\lambda}^{*}\hat{a}^{\dag}_{\mathbf{k}\lambda} e^{i(\mathbf{k}\cdot\mathbf{r}+\omega_{\mathbf{k}}t)}\right)\mathbf{e}_{\mathbf{k}\lambda} \end{aligned}$ 

可见顺时针旋转的部分对应湮灭算子 $\hat{a}_{\mathbf{k}\lambda}$ ，而逆时针旋转的部分对应产生算子 $\hat{a}_{\mathbf{k}\lambda}^{\dag}$ 。由于这两个算子不对易（ $[\hat{a}_{\mathbf{k}\lambda},\hat{a}_{\mathbf{k}\lambda}^{\dag}]=1$ ），导致真空不再是“真空”，而是充满了电磁场的涨落。


> 具体来说，电磁场的哈密顿量为：  
>  $\begin{aligned} \hat{H}&=\hbar\sum_{\mathbf{k}\lambda}\frac{\omega_\mathbf{k}}{2}\left\{\hat{a}_{\mathbf{k}\lambda},\hat{a}_{\mathbf{k}\lambda}^{\dag}\right\} \\\\ &= \hbar \sum_{\mathbf{k}\lambda}\frac{\omega_{\mathbf{k}}}{2}\left(\hat{a}_{\mathbf{k}\lambda}^{\dag}\hat{a}_{\mathbf{k}\lambda}+\hat{a}_{\mathbf{k}\lambda}\hat{a}_{\mathbf{k}\lambda}^{\dag}\right) \\\\ &= \hbar \sum_{\mathbf{k}\lambda}\frac{\omega_{\mathbf{k}}}{2}\left(\hat{a}_{\mathbf{k}\lambda}^{\dag}\hat{a}_{\mathbf{k}\lambda}+\hat{a}_{\mathbf{k}\lambda}^{\dag}\hat{a}_{\mathbf{k}\lambda} + [\hat{a}_{\mathbf{k}\lambda},\hat{a}_{\mathbf{k}\lambda}^{\dag}]\right) \\\\ &=\hbar \sum_{\mathbf{k}\lambda}\omega_{\mathbf{k}}\left(\hat{a}_{\mathbf{k}\lambda}^{\dag}\hat{a}_{\mathbf{k}\lambda} + \frac{1}{2}\right) \\\\ &= \hbar \sum_{\mathbf{k}\lambda} \omega_{\mathbf{k}}\left(\hat{n}_{\mathbf{k}\lambda}+\frac{1}{2}\right) \end{aligned}$   
> 当所有模式的激发数都为零，也就是真空时，电磁场的能量并不为零。这是由真空涨落导致的。

