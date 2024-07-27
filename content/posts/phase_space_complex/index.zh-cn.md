---
title: "相空间为什么有时看起来像一个复平面？"
date: 2024-07-27T15:52:22+08:00
draft: false
tags: ["量子光学"]
categories: ["量子信息"]
---

学过物理的同学们都知道相空间，它是由广义坐标 $q$ 和广义动量 $p$ 构成的。


> 例 1：单摆的角度构成一个构型空间 $S\_1$ 。角度和角动量构成一个相空间 $S\_1 \times \mathbb{R}$ 。  
>   
> 例 2：给定经典电磁场的哈密顿量和边界条件，某个模式上的电场强度构成一个构型空间，该模式上电场强度的余弦分量和正弦分量构成一个相空间。

  
实际上，给定一个构型空间 $M$ ，相空间就是 $M$ 上的**余切丛** $T^\*M$ 。

然而，解题的时候，我们物理人往往也会用到**复平面**。


> 例 1：给定谐振子的哈密顿方程  
> $\begin{cases} \frac{\mathrm{d}q}{\mathrm{d}t} = \omega p\\\\ \frac{\mathrm{d}p}{\mathrm{d}t} = -\omega q \end{cases}$   
> 即  
> $\frac{\mathrm{d}}{\mathrm{d}t} \begin{bmatrix} q \\\\ p \end{bmatrix} = \begin{bmatrix} 0 & \omega \\\\ -\omega & 0 \end{bmatrix} \begin{bmatrix} q\\\\ p \end{bmatrix}$   
> 对角化得到特征向量 $a^{\pm} =  q\pm\mathrm{i}p$ ，于是 $a^{\pm}$ 的导数就只和自己有关：  
> $\frac{\mathrm{d}a^{\pm}}{\mathrm{d}t}=\mp\mathrm{i}\omega a^{\pm},\quad a^{\pm}=a\_0^{\pm} \exp (\mp\mathrm{i}\omega t)$   
> 虽然经典力学中没有复数，但是这里的复数作为特征值出现是非常自然的。这个手段量子化之后就得到了产生和湮灭算符。  
>   
> 例 2：描述单模经典电磁场的相量图（Phasor diagram）定义在复平面上。当然，也可以描述电流电压等量。  
>   
> 例 3：描述单模量子电磁场的 Wigner function 定义在复平面上。
  
这些种种都在暗示我们：难道余切丛可以是个复平面？经过与数学系同学的讨论，的确如此，但**前提是该余切丛自身是一个向量空间**。论证如下：

**（1）**相空间是构型空间的余切丛。

**（2）**任何一个余切丛都自带一个典范的辛结构。


> 或者说，余切丛上任意一点的切空间自带一个典范的辛形式。

**（3）**如果余切丛本身恰好也是一个向量空间，那么其切空间就自然同构于它自身。从而，根据 (2)，该余切丛也是一个辛向量空间。

**（4）**一个带内积 $g$ 的辛向量空间 $(V,\omega)$ 自带一个典范的复结构 $J$ [1]。


> $V$ 上的复结构 $J$ 定义为 $J \in \operatorname{End}(V) \quad\text{s.t.} \quad J^2 = -\operatorname{id}$ 。

由**（1-4）**可知，如果一个相空间恰好是一个向量空间，那么该相空间自带一个复结构。

所以， $T^\*\mathbb{R} = \mathbb{R} \times \mathbb{R}^\*$ 和 $\mathbb{C}$ 有相同的数学结构。 $T^\*(\mathbb{R}^n) = \mathbb{R}^n \times (\mathbb{R}^{n})^\*$ 和 $\mathbb{C}^n$ 有相同的数学结构。这就是我们可以用复平面来代替相空间的原因。

但要注意，不是所有相空间都可被看作复平面。只有构型空间本身是一个向量空间时，相空间才是一个向量空间，从而才能被看成复平面。例如，单摆的相空间就不是一个向量空间，不能被看作复平面。



---

更：以上（1-4）有点抽象。下面给个具体的构造。

考虑构型空间 $\mathbb{R}$ ，相空间 $T^\*(\mathbb{R}) = \mathbb{R} \times \mathbb{R}^\*$ ，有全局坐标系 $(p,q)$。

$T^\*(\mathbb{R})$ 上典范的辛形式为 $\omega= \mathrm{d} p \wedge \mathrm{d} q$ ，它不依赖于基。矩阵形式为 $M(\omega)=\begin{pmatrix} 0 & 1\\\\ -1 & 0 \end{pmatrix}$ 。

$T^\*(\mathbb{R})$ 上的典范欧式内积为 $g = \mathrm{d}q^2 + \mathrm{d}p^2$ ，其矩阵形式为 $M(g)=\begin{pmatrix} 1 & 0\\\\ 0 & 1 \end{pmatrix}$ 。

我们可以借助 $g(u,v)=\omega(u,Jv)$ 定义复结构 $J\in \text{End}[T^\*(\mathbb{R})]$ 。显然，其矩阵形式满足 $M(g)=M(\omega)M(J)$ ，所以 $M(J)=\begin{pmatrix} 0 & -1\\\\ 1 & 0 \end{pmatrix}$ 。这个矩阵是不是有点眼熟？没错，它就是虚数单位 $\mathrm{i}$ 的一种二阶矩阵表示。

## 参考  
1. [https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/resources/lect07/](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/resources/lect07/)
