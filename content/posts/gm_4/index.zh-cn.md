---
title: "狄拉克磁单极子——陈类与陈数【更高更妙的电动力学·4】"
date: 2025-04-06T01:08:16+08:00
draft: false
categories: ["数学物理方法"]
tags: ["微分几何", "拓扑", "陈数", "电动力学"]
---

在[前文](https://zhuanlan.zhihu.com/p/32173040413)中，我们说到，如果流形是拓扑平凡的，那么对 Berry 曲率在闭合曲面 $\Sigma$ 上积分应该得到零。这是因为根据 Stokes 定理，有：

$\int\_\Sigma F = \int\_{\partial \Sigma } A = 0$

然而，在非拓扑平凡的流形上，积分 $\int\_\Sigma F$ 不一定为零。这是因为，此时无法定义全局单值的联络 $A$ ，导致 Stokes 定理不再适用。此话怎讲？

## 一、上同调、陈类  

我们知道，恰当形式都是闭形式。因为 $\mathrm{d}\mathrm{d}=0$ 。

> 恰当形式指的是这样一种形式，它是另外一个形式的（外）微分： $\exists \alpha, \  \omega = \mathrm{d}\alpha$ 。  
> 闭形式指的是这样一种形式，它的（外）微分为零： $\mathrm{d}\omega =0$ 。

但反过来，是不是所有闭形式都是恰当形式呢？对于拓扑平凡的流形，例如 $\mathbb{R}^n$ ，的确如此。但对于一般的流形而言，并非所有闭形式都是恰当形式。我们下面举一个例子：

> **例**  
>   
> 想象一个无限长圆柱体的侧面（$\mathbb{R}^1 \times S^1$），上面有一个均匀环绕它一圈的电场 $E= c\ \mathrm{d}\theta$ ，其中 $c$ 是常数。这样的电场 $E$ 是无旋的 ( $\mathrm{d}E=0$ )，也就是说，该电场是一个闭形式。  
>   
> 然而，此时 $E$ 不是一个保守场：一个电子朝电场的方向绕一圈回到原来的位置，能量会减少。  
>   
> 可见，此时我们无法定义全局单值的电势，也就是说，我们无法找到一个 $\phi$ ，使得 $E = \mathrm{d} \phi$ 。换句话说， $E$ 不是恰当形式。

在物理中，我们通常默认：如果一个形式是闭形式，那么它也是恰当形式。这是因为在大部分情况下，我们研究的流形没有“孔洞”。这样的流形可以叫做拓扑平凡的。

然而，在有“孔洞”的流形上，这是不成立的。此时闭形式未必是恰当形式。

上同调（Cohomology）就是研究“不恰当的闭形式”的学问。具体来说，它研究可以把“不恰当的闭形式”分成多少类。这些等价类构成一个群，叫做上同调群。

所谓**陈类（Chern Class）**，就是上同调群中的元素，也即“不恰当的闭形式”的等价类。

回到一开始的问题，我们说不一定存在全局的联络。这是因为虽然曲率 2-形式是闭形式，但它不一定是恰当形式。因此不一定存在全局的联络 1-形式，使得其外微分是曲率 2-形式。这样的曲率 2-形式的拓扑等价类就是陈类。而陈数就是用来标记不同的等价类的。

> **选读**  
>   
> 具体来说，流形 $M$ 上的 n 阶（de Rham）上同调群定义为 $M$ 上所有 n 阶闭形式商掉所有 n 阶恰当形式（见[这篇文章](https://zhuanlan.zhihu.com/p/629852598)）：  
>   
>  $\boxed{H\_{\text{dR}}^n(M) = \frac{\{\omega\mid\mathrm{d}\omega = 0\}}{\{\omega\mid \exists\alpha,\mathrm{d}\alpha = \omega\}}} ​ $   
>   
> 其中 $\omega$ 是 n-形式。  
>   
> 除了 de Rham 上同调以外，还有其他上同调理论。奇异上同调（Singular Cohomology）使用了奇异同调（Singular Homology）中的单形（Simplex）和链（Chain）等概念来定义同调群：  
>   
>  $\boxed{ H^n(M;\mathbb{F}) = \frac{\{c\mid\delta c = 0\}}{\{c\mid \exists a,\delta a = c\}} } $   
>   
> 其中 $c$ 是 n 阶 co-chain， $\delta$ 是 co-boundary 算子。它们是借助同调中的 chain 和 boundary 算子定义的（见[这篇文章](https://zhuanlan.zhihu.com/p/629852598)）。另外， $\mathbb{F}$ 代表 co-chain 的系数环，可以是 $\mathbb{Z}$ 或者 $\mathbb{R}$ 。  
>   
> de Rham 上同调群 $H\_{\text{dR}}^n(M) $ 同构于奇异上同调群 $H^n(M;\mathbb{R})$ 。而（第一）陈类本质上是 2 阶奇异上同调群 $H^2(M;\mathbb{Z})$ 中的元素。

## 二、局部联络、缠绕数（Winding Number）  

回到一开始的问题。我们说在非拓扑平凡的流形上，积分 $\int\_\Sigma F$ 不一定为零。这是因为此时无法定义全局单值的联络 $A$ 。不过，联络 $A$ 虽然不可全局定义，但仍然可以局部定义——我们可以给它打补丁。

具体来说，我们在上半曲面 $\Sigma\_1$ 上定义联络 $A\_1$ ，在下半曲面 $\Sigma\_2$ 定义联络 $A\_2$ ，这两个半曲面在中间赤道处相交。对于相交区域 $U=\Sigma\_1 \cup \Sigma\_2 \simeq S^1$ ，我们需要让 $A\_1$ 与 $A\_2$ 只相差一个规范变换： $A\_2  = A\_1 + \mathrm{d}\lambda$ 。

相交区域 $U$ 是一个“圈”（ $\simeq S^1$ ），而 $e^{i\lambda} \in U(1)$ 也是一个“圈”，这引出了一个重要的概念：缠绕数。具体来说，在 $U$ 上转一圈回到原点之后， $\Delta \lambda = \oint\_{U} \mathrm{d}\lambda $ 不需要为零，相差 $2\pi$ 的整数倍也是没有问题的，即：

$\oint\_{U} \mathrm{d}\lambda = \oint\_{U} \nabla \lambda \cdot \mathrm{d}\mathbf{l} = 2k\pi \quad(k\in\mathbb{Z})$

> 从波函数的规范变换 $\psi \mapsto e^{i\lambda} \psi$ 可以看出，出发一圈后回到原点时，只需要 $\Delta \lambda = 2k\pi$ 即可。

这里的 $k$ 就是**缠绕数**。它代表两个局部联络之间连接处的规范变换“缠绕”了多少圈。

为什么 $\Delta \lambda$ 不必为零？因为 $A\_1$ 与 $A\_2$ 不是全局联络 $A$ 的一部分，而是两个完全不同的局部联络，我们只是把它们 “粘” 在一起，而胶水就是规范变换。这个规范变换的 $\lambda$ 无需满足单值条件 $\oint\_{U} \mathrm{d}\lambda  = 0$ 。

## 三、陈数（Chern Number）  

回到一开始的问题：在非拓扑平凡的流形上，Berry 曲率 $F$ 在闭合曲面 $\Sigma$ 上的积分 $\int\_\Sigma F$ 不一定为零。这看似违反了 Stokes 定理，究竟是怎么回事呢？

实际上，这并不违反 Stokes 定理，只是我们不能在整个 $\Sigma$ 上使用它了，而是要在“补丁”$\Sigma\_1$ 和 $\Sigma\_2$ 上分别使用它。

换句话说，虽然全局联络 $A$ 不存在，但 $\Sigma\_1$ 和 $\Sigma\_2$ 上的局部联络 $A\_1$ 和 $A\_2$ 仍然存在，所以我们可以分别在 $\Sigma\_1$ 和 $\Sigma\_2$ 上使用 Stokes 定理：

$\begin{aligned} \int\_{\Sigma\_1} F &=  \int\_{\partial \Sigma\_1} A\_1 = \int\_{U} A\_1 \\\\ \int\_{\Sigma\_2} F &=  \int\_{\partial \Sigma\_2} A\_2 = \int\_{U} A\_2 \end{aligned}$

于是：

$\begin{aligned} \int\_{\Sigma} F &=  \int\_{\partial \Sigma\_1} A\_1 - \int\_{\partial \Sigma\_2} A\_2\\\\ &= \int\_{U} (A\_1-A\_2)  \\\\ &= \int\_{U} \nabla \lambda \cdot \mathrm{d}l  \\\\ &=2k\pi \quad (k\in\mathbb{Z}) \end{aligned}$

可见， $\int\_\Sigma F$ 不一定为零，恰恰是因为缠绕数 $k$ 可以不为零。

于是我们定义**陈数**为

$\boxed{ C = \frac{1}{2\pi} \int\_\Sigma F }$

> 可见，在 $\Sigma \simeq S^2$ 上，陈数等于缠绕数。  
>   
> 当然，这只是 $\Sigma \simeq S^2$ 的情形。在凝聚态物理中，更常见的是“甜甜圈” $\Sigma \simeq T^2$ 。此时我们可以在 x 和 y 两个方向上缠绕。可以证明，此时的陈数是两个方向上的缠绕数的差。  
>   
> 这里定义的陈数是在 2 维闭合曲面上积分得到的。实际上，在 2n 维闭合曲面上积分即可得到第 n 陈数，而我们这里说的只是第一陈数。

不同的曲率 2-形式在闭合曲面上积分，可能得到相同的陈数，所以我们可以依据陈数对曲率 2-形式进行分类，这些等价类就叫做陈类。

## 四、狄拉克磁单极子  

接下来我们把以上所学应用到一个具体的例子：狄拉克磁单极子。

我们现在假设存在这么一种粒子：像点电荷射出电场线一样，它可以射出磁场线。我们把这种粒子叫做“磁单极子”。

$\nabla \cdot \mathbf{B} = g \delta^3(\mathbf{r})$

其中 $g$ 代表“磁荷”的大小。于是磁单极子外的磁场为：

$\begin{aligned} \mathbf{B} = \frac{g}{4\pi} \frac{\hat{r}}{r^2} \end{aligned}$

考虑以磁单极子为中心的半径为 $r$ 的球面，我们分别在上半球面和下半球面定义两个局部联络：

$\begin{aligned} \mathbf{A}\_1 &= \frac{g}{4\pi}\frac{1-\cos \theta}{\sin \theta} \hat{\phi} \\\\ \mathbf{A}\_2 &= -\frac{g}{4\pi}\frac{1+\cos \theta}{\sin \theta} \hat{\phi} \end{aligned}$

可以验证，在这两个半球面上，有 $\nabla \times \mathbf{A}\_1 = \mathbf{B}$ 和 $\nabla \times \mathbf{A}\_2 = \mathbf{B}$ 。

在赤道上， $\mathbf{A}\_1$ 和 $\mathbf{A}\_2$ 只能相差一个规范变换： $\frac{q}{\hbar}(\mathbf{A}\_1 -\mathbf{A}\_2) = \nabla \lambda$ ，于是 $\lambda = \frac{q}{\hbar}\frac{g}{2\pi r} \phi$ ，且

$\begin{aligned} \oint \nabla \lambda \cdot \mathrm{d} \mathbf{l} &= \oint  \frac{q}{\hbar}\frac{g}{2\pi r} \cdot r \mathrm{d} \phi\\\\ &= \frac{qg}{\hbar} \end{aligned}$

令 $\oint \nabla \lambda \cdot \mathrm{d} \mathbf{l}  = 2k\pi \ \  (k\in\mathbb{Z})$ 得：

$\boxed{\frac{qg}{2\pi \hbar} = k \in \mathbb{Z} }$

这就是狄拉克量子化条件。它告诉我们，如果磁单极子存在，那么磁荷一定是量子化的。

在这个例子中，Berry 联络是矢势，Berry 曲率是磁场，陈数 $qg/2\pi \hbar \in \mathbb{Z}$ 正比于磁荷 $g$ 。磁荷 $g$ 就是我们常说的**拓扑荷**的一种。

当然，人们至今都没有发现磁单极子。这意味着作为 Berry 曲率的磁场是拓扑平凡的：总是能找到全局的 Berry 联络，也就是矢势，使得磁场是它的外微分。换句话说，磁场的陈数总是为零。