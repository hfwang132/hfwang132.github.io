---
title: "量子态/算符的 Weyl 和 Wigner 表示"
date: 2025-01-08T20:25:50+08:00
draft: false
tags: ["量子信息"]
categories: ["数学物理方法"]
---

## 前言  

在经典力学中，物理量是相空间上的一个函数，系统状态是相空间上的一个点（对于系综而言则是相空间上的一个概率分布）。这一套语言量子化之后，就得到了量子态/算符的相空间表示，也就是 Wigner 表示。Weyl 表示则是它的傅里叶变换。

大部分作者都将 Wigner 表示定义为：

$F_W(x,p)=\int \mathrm{d}y \langle x+\frac{y}{2}\mid F \mid x - \frac{y}{2} \rangle e^{\mathrm{i} p y}$

然后再推导出它的各种性质。但从物理人的角度来看，这个式子物理意义不明，且 $(x,p)$ 的地位不平等，让人看了不太舒服。

本文将从一个更加舒服的角度引入 Wigner 和 Weyl 表示。本文只作介绍，不涉及严格证明和推导。

## 离散情形的幺正基  

给定一个 $N$ 维希尔伯特空间 $\mathcal{H}$ ，以及它的一个标准正交基 $|v_l\rangle\,\,( l=1,...,N)$ 。定义

$U = \sum_{l=1}^N |v_{l+1}\rangle\langle v_{l}|$

其中 $|v_{N+1}\rangle := |v_1\rangle$ 。

记 $U$ 的特征向量为 $|u_k\rangle$ ，则可以定义

$V = \sum_{k=1}^N |u_k\rangle\langle u_{k+1} |$ ，

且 $\langle u_k| v_l\rangle=e^{\frac{2\pi}{N}kl}$ ，证略。

任何一个 $\mathcal{H}$ 上的算符都可以写成 $U$ 和 $V$ 的多项式（证略）：

$F = \sum_{kl} f_{kl}U^k  V^l$

$f_{kl} = \frac{1}{N} \text{tr}[U^{-k}FV^{-l}]$

> 例：在 $\mathbb{C}^2$ 上，令 $U = \sigma_x$ ， $V=\sigma_y$ ，则 $UV = \mathrm{i}\sigma_z$ 。那么  
>  $F = \frac{1}{2}\sum_{k=0}^3 \text{tr}[F\sigma_k] \sigma_k$   
> 其中 $\sigma_0 :=\mathbb{I}$ 。注意 $\sigma_k^{-1} = \sigma_k^\dagger = \sigma_k$ 。

可见，给定一个有限维希尔伯特空间，我们总能找到一对幺正算符 $U,V$ 以及它们作为生成元所生成的 $U^k V^l$ ，作为算符的基，共 $N^2$ 个。

## 连续情形的幺正基（Weyl 基）  

以上步骤可以推广到无穷维希尔伯特空间。此时我们以 $X,P$ 作为生成元，生成 $e^{\mathrm{i}pX}e^{\mathrm{i}xP}$ 作为作为算符的基。

$F=\int\frac{\mathrm{d}x\mathrm{d}p}{2\pi} f(x,p) e^{\mathrm{i}pX} e^{\mathrm{i}xP}$

$f(x,p)=\text{tr}[e^{-\mathrm{i}pX}Fe^{-\mathrm{i}xP}]$

然而，此时 $X,P$ 的地位是不平等的。这是因为在 $e^{\mathrm{i}pX}e^{\mathrm{i}xP}$ 这个表达式里面，所有 $X$ 都在 $P$ 的前面。而如果我们让 $P$ 在 $X$ 的前面，同样可以得到另一个 $\tilde{f}(x,p)$ 。

让 $X,P$ 地位平等的办法是定义 $U(x,p)=e^{\mathrm{i}(xP-pX)}$ 。这其实就是常说的平移算符（Displacement operator）。我们也称它为 Weyl 算符。我们接下来以它作为算符的基，并称其为 Weyl 基。可以证明：

$F=\int\frac{\mathrm{d}x\mathrm{d}p}{2\pi} f_W(x,p) U(x,p)$

$f_W(x,p) = \text{tr}[FU^\dagger(x,p)]$

其中 $f_W(x,p)$ 就是算符 $F$ 的 Weyl 表示，它是算符在 Weyl 基下的展开形式。

## 连续情形的厄米基（Wigner 基）  

上面介绍的 Weyl 基是幺正的。有没有厄米的基？答案是有的，它们叫做 Wigner 基。

我们先来定义反演算符：

$\frac{1}{2}W:=\int \mathrm{d}x \mid -x\rangle\langle x| = \int \mathrm{d}p \mid -p\rangle\langle p|$

我们之所以引入 $\frac{1}{2}$ 因子，是因为 $\text{tr}[W]=1$ 。

$\frac{1}{2}W$ 的作用就是将 $(x,p)$ 平面绕着原点旋转 180 度。显然，它是一个厄米算符。

可以证明，它能写成

$\frac{1}{2}W=e^{-\mathrm{i}2X;P} = \sum_{k=0}^\infty \frac{1}{k}(-2\mathrm{i})^k X^kP^k$ 。

其中 $X;P$ 表示在多项式中，所有 $X$ 排到 $P$ 的前面。

我们再定义绕着点 $(x,p)$ 旋转 180 度的算符：

$\frac{1}{2}W(x,p):=e^{\mathrm{i}2(X-x);(P-p)}$。

可以证明， $W(x,p)$ 也能作为算符的基，叫做 Wigner 基：

$F=\int \frac{\mathrm{d}x\mathrm{d}p}{2\pi} F_W(x,p)W(x,p)$

$F_W(x,p) = \text{tr}[FW(x,p)]$

其中 $F_W(x,p)$ 就是算符 $F$ 的 Wigner 表示。

## Weyl 和 Wigner 表示之间的关系  

Weyl 基是幺正的，Wigner 基是厄米的。

可以证明，Wigner 表示是 Weyl 表示的傅里叶变换：

$F_W(x,p)=\int \frac{\mathrm{d}x^\prime\mathrm{d}p^\prime}{2\pi} e^{-\mathrm{i}(xp^\prime-px^\prime)}f_W(x^\prime,p^\prime)$

## 尾声  

值得一提，以上所有步骤都没有任何物理上的动机，而只有数学上的动机，即，为希尔伯特空间上的算符在一组方便的基下找到对应的表示。
