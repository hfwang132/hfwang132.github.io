---
title: "狄拉克磁单极子——陈类与陈数【更高更妙的电动力学·4】"
date: 2025-03-30T01:13:18+08:00
originalURL: "https://zhuanlan.zhihu.com/p/1889370433708609679"
aliases:
  - "/gm_4/"
  - "/Post_20250406_狄拉克磁单极子-陈类与陈数-更高更妙的电动力学-4/"
draft: false
categories: ["数学物理方法"]
tags: ["微分几何", "拓扑", "陈数", "电动力学"]
math: true
author: "Haifei"
---

本系列上一篇文章：

[Godfly：电磁场不只是电场和磁场——AB效应与Berry联络【更高更妙的电动力学·3】](https://zhuanlan.zhihu.com/p/32173040413)

---

在[上篇文章](https://zhuanlan.zhihu.com/p/32173040413)中，我们说到，如果流形是拓扑平凡的，那么对 Berry 曲率在闭合曲面 \(\Sigma\) 上积分应该得到零。这是因为根据 Stokes 定理，有：

\[\int_\Sigma F = \int_{\partial \Sigma } A = 0\]

然而，在非拓扑平凡的流形上，积分 \(\int_\Sigma F\) 不一定为零。这是因为，此时无法定义全局单值的联络 \(A\) ，导致 Stokes 定理不再适用。此话怎讲？

## 一、上同调、陈类  

我们知道，恰当形式都是闭形式。因为 \(\mathrm{d}\mathrm{d}=0\) 。

> 恰当形式指的是这样一种形式，它是另外一个形式的（外）微分： \(\exists \alpha, \, \omega = \mathrm{d}\alpha\) 。  
> 闭形式指的是这样一种形式，它的（外）微分为零： \(\mathrm{d}\omega =0\) 。

但反过来，是不是所有闭形式都是恰当形式呢？对于拓扑平凡的流形，例如 \(\mathbb{R}^n\) ，的确如此。但对于一般的流形而言，并非所有闭形式都是恰当形式。我们下面举一个例子：

> **例**  
>   
> 想象一个无限长圆柱体的侧面（\(\mathbb{R}^1 \times S^1\)），上面有一个均匀环绕它一圈的电场 \(E= c\,\mathrm{d}\theta\) ，其中 \(c\) 是常数。这样的电场 \(E\) 是无旋的 ( \(\mathrm{d}E=0\) )，也就是说，该电场是一个闭形式。  
>   
> 然而，此时 \(E\) 不是一个保守场：一个电子朝电场的方向绕一圈回到原来的位置，能量会减少。  
>   
> 可见，此时我们无法定义全局单值的电势，也就是说，我们无法找到一个 \(\phi\) ，使得 \(E = \mathrm{d} \phi\) 。换句话说， \(E\) 不是恰当形式。

在物理中，我们通常默认：如果一个形式是闭形式，那么它也是恰当形式。这是因为在大部分情况下，我们研究的流形没有“孔洞”。这样的流形可以叫做拓扑平凡的。

然而，在有“孔洞”的流形上，这是不成立的。此时闭形式未必是恰当形式。

上同调（Cohomology）就是研究“不恰当的闭形式”的学问。具体来说，它研究可以把“不恰当的闭形式”分成多少类。这些等价类构成一个群，叫做上同调群。

所谓**陈类（Chern Class）**，就是上同调群中的元素，也即“不恰当的闭形式”的等价类。

回到一开始的问题，我们说不一定存在全局的联络。这是因为虽然曲率 2-形式是闭形式，但它不一定是恰当形式。因此不一定存在全局的联络 1-形式，使得其外微分是曲率 2-形式。这样的曲率 2-形式的拓扑等价类就是陈类。而陈数就是用来标记不同的等价类的。

> **选读**  
>   
> 具体来说，流形 \(M\) 上的 n 阶（de Rham）上同调群定义为 \(M\) 上所有 n 阶闭形式商掉所有 n 阶恰当形式（见[这篇文章](https://zhuanlan.zhihu.com/p/629852598)）：  
>   
>  \(\boxed{H_{\text{dR}}^n(M) = \frac{\{\omega\mid\mathrm{d}\omega = 0\}}{\{\omega\mid \exists\alpha,\mathrm{d}\alpha = \omega\}}} ​ \)   
>   
> 其中 \(\omega\) 是 n-形式。  
>   
> 除了 de Rham 上同调以外，还有其他上同调理论。奇异上同调（Singular Cohomology）使用了奇异同调（Singular Homology）中的单形（Simplex）和链（Chain）等概念来定义同调群：  
>   
>  \(\boxed{ H^n(M;\mathbb{F}) = \frac{\{c\mid\delta c = 0\}}{\{c\mid \exists a,\delta a = c\}} } \)   
>   
> 其中 \(c\) 是 n 阶 co-chain， \(\delta\) 是 co-boundary 算子。它们是借助同调中的 chain 和 boundary 算子定义的（见[这篇文章](https://zhuanlan.zhihu.com/p/629852598)）。另外， \(\mathbb{F}\) 代表 co-chain 的系数环，可以是 \(\mathbb{Z}\) 或者 \(\mathbb{R}\) 。  
>   
> de Rham 上同调群 \(H_{\text{dR}}^n(M) \) 同构于奇异上同调群 \(H^n(M;\mathbb{R})\) 。而（第一）陈类本质上是 2 阶奇异上同调群 \(H^2(M;\mathbb{Z})\) 中的元素。

## 二、局部联络、缠绕数（Winding Number）  

回到一开始的问题。我们说在非拓扑平凡的流形上，积分 \(\int_\Sigma F\) 不一定为零。这是因为此时无法定义全局单值的联络 \(A\) 。不过，联络 \(A\) 虽然不可全局定义，但仍然可以局部定义——我们可以给它打补丁。

具体来说，我们在上半曲面 \(\Sigma_1\) 上定义联络 \(A_1\) ，在下半曲面 \(\Sigma_2\) 定义联络 \(A_2\) ，这两个半曲面在中间赤道处相交。对于相交区域 \(U=\Sigma_1 \cup \Sigma_2 \simeq S^1\) ，我们需要让 \(A_1\) 与 \(A_2\) 只相差一个规范变换： \(A_2  = A_1 + \mathrm{d}\lambda\) 。

相交区域 \(U\) 是一个“圈”（ \(\simeq S^1\) ），而 \(e^{i\lambda} \in U(1)\) 也是一个“圈”，这引出了一个重要的概念：缠绕数。具体来说，在 \(U\) 上转一圈回到原点之后， \(\Delta \lambda = \oint_{U} \mathrm{d}\lambda \) 不需要为零，相差 \(2\pi\) 的整数倍也是没有问题的，即：

\[\oint_{U} \mathrm{d}\lambda = \oint_{U} \nabla \lambda \cdot \mathrm{d}\mathbf{l} = 2k\pi \quad(k\in\mathbb{Z})\]

> 从波函数的规范变换 \(\psi \mapsto e^{i\lambda} \psi\) 可以看出，出发一圈后回到原点时，只需要 \(\Delta \lambda = 2k\pi\) 即可。

这里的 \(k\) 就是**缠绕数**。它代表两个局部联络之间连接处的规范变换“缠绕”了多少圈。

为什么 \(\Delta \lambda\) 不必为零？因为 \(A_1\) 与 \(A_2\) 不是全局联络 \(A\) 的一部分，而是两个完全不同的局部联络，我们只是把它们 “粘” 在一起，而胶水就是规范变换。这个规范变换的 \(\lambda\) 无需满足单值条件 \(\oint_{U} \mathrm{d}\lambda  = 0\) 。

## 三、陈数（Chern Number）  

回到一开始的问题：在非拓扑平凡的流形上，Berry 曲率 \(F\) 在闭合曲面 \(\Sigma\) 上的积分 \(\int_\Sigma F\) 不一定为零。这看似违反了 Stokes 定理，究竟是怎么回事呢？

实际上，这并不违反 Stokes 定理，只是我们不能在整个 \(\Sigma\) 上使用它了，而是要在“补丁”\(\Sigma_1\) 和 \(\Sigma_2\) 上分别使用它。

换句话说，虽然全局联络 \(A\) 不存在，但 \(\Sigma_1\) 和 \(\Sigma_2\) 上的局部联络 \(A_1\) 和 \(A_2\) 仍然存在，所以我们可以分别在 \(\Sigma_1\) 和 \(\Sigma_2\) 上使用 Stokes 定理：

\[\begin{aligned} \int_{\Sigma_1} F &=  \int_{\partial \Sigma_1} A_1 = \int_{U} A_1 \\ \int_{\Sigma_2} F &=  \int_{\partial \Sigma_2} A_2 = \int_{U} A_2 \end{aligned}\]

于是：

\[\begin{aligned} \int_{\Sigma} F &=  \int_{\partial \Sigma_1} A_1 - \int_{\partial \Sigma_2} A_2\\ &= \int_{U} (A_1-A_2)  \\ &= \int_{U} \nabla \lambda \cdot \mathrm{d}l  \\ &=2k\pi \quad (k\in\mathbb{Z}) \end{aligned}\]

可见， \(\int_\Sigma F\) 不一定为零，恰恰是因为缠绕数 \(k\) 可以不为零。

于是我们定义**陈数**为

\[\boxed{ C = \frac{1}{2\pi} \int_\Sigma F }\]

> 可见，在 \(\Sigma \simeq S^2\) 上，陈数等于缠绕数。  
>   
> 当然，这只是 \(\Sigma \simeq S^2\) 的情形。在凝聚态物理中，更常见的是“甜甜圈” \(\Sigma \simeq T^2\) 。此时我们可以在 x 和 y 两个方向上缠绕。可以证明，此时的陈数是两个方向上的缠绕数的差。  
>   
> 这里定义的陈数是在 2 维闭合曲面上积分得到的。实际上，在 2n 维闭合曲面上积分即可得到第 n 陈数，而我们这里说的只是第一陈数。  
>   
> 在非阿贝尔的情况下，我们可以计算第 n 陈数，它们定义为：  
>   
>  \(\boxed{ C_n = \frac{1}{n!(2\pi)^n}  \int \operatorname{tr}[\underbrace{F\wedge \cdots \wedge F}_{\text{n } F}] = \frac{1}{n!(2\pi)^n}  \int \operatorname{tr}[F^{\wedge n}] }\)   
>   
> 在阿贝尔的情况下， \(C_{n>1} =0\) ，因为 \(F \wedge F=0\) 。

不同的曲率 2-形式在闭合曲面上积分，可能得到相同的陈数，所以我们可以依据陈数对曲率 2-形式进行分类，这些等价类就叫做陈类。

## 四、狄拉克单极子（Dirac Monopole）  

接下来我们把以上所学应用到一个具体的例子：狄拉克磁单极子。

我们现在假设存在这么一种粒子：像点电荷射出电场线一样，它可以射出磁场线。我们把这种粒子叫做“磁单极子”。

\[\nabla \cdot \mathbf{B} = g \delta^3(\mathbf{r})\]

其中 \(g\) 代表“磁荷”的大小。于是磁单极子外的磁场为：

\[\begin{aligned} \mathbf{B} = \frac{g}{4\pi} \frac{\hat{r}}{r^2} \end{aligned}\]

考虑以磁单极子为中心的半径为 \(r\) 的球面，我们分别在上半球面和下半球面定义两个局部联络：

\[\begin{aligned} \mathbf{A}_1 &= \frac{g}{4\pi}\frac{1-\cos \theta}{\sin \theta} \hat{\phi} \\ \mathbf{A}_2 &= -\frac{g}{4\pi}\frac{1+\cos \theta}{\sin \theta} \hat{\phi} \end{aligned}\]

可以验证，在这两个半球面上，有 \(\nabla \times \mathbf{A}_1 = \mathbf{B}\) 和 \(\nabla \times \mathbf{A}_2 = \mathbf{B}\) 。

在赤道上， \(\mathbf{A}_1\) 和 \(\mathbf{A}_2\) 只能相差一个规范变换： \(\frac{q}{\hbar}(\mathbf{A}_1 -\mathbf{A}_2) = \nabla \lambda\) ，于是 \(\lambda = \frac{q}{\hbar}\frac{g}{2\pi r} \phi\) ，且

\[\begin{aligned} \oint \nabla \lambda \cdot \mathrm{d} \mathbf{l} &= \oint  \frac{q}{\hbar}\frac{g}{2\pi r} \cdot r \mathrm{d} \phi\\ &= \frac{qg}{\hbar} \end{aligned}\]

令 \(\oint \nabla \lambda \cdot \mathrm{d} \mathbf{l}  = 2k\pi \,\, (k\in\mathbb{Z})\) 得：

\[\boxed{\frac{qg}{2\pi \hbar} = k \in \mathbb{Z} }\]

这就是狄拉克量子化条件。它告诉我们，如果磁单极子存在，那么磁荷一定是量子化的。

在这个例子中，Berry 联络是矢势，Berry 曲率是磁场，陈数 \(qg/2\pi \hbar \in \mathbb{Z}\) 正比于磁荷 \(g\) 。磁荷 \(g\) 就是我们常说的**拓扑荷**的一种。

当然，人们至今都没有发现磁单极子。这意味着作为 Berry 曲率的磁场是拓扑平凡的：总是能找到全局的 Berry 联络，也就是矢势，使得磁场是它的外微分。换句话说，磁场的陈数总是为零。

## 五、磁场中的自旋  

在上一节中我们看到，以位形空间作为底流形的情况是拓扑平凡的。这太无聊了，我们下面给一个拓扑不平凡的例子。

现在考虑磁场中的一个自旋，其哈密顿量为：

\[H = - \mu\ \mathbf{B}\cdot \bm\sigma\]

其中 \(\bm\sigma = (\sigma_x, \sigma_y,\sigma_z)\) 为三个泡利算符构成的向量。该自旋两个能级的能量为 \(\pm \mu B \) 。

现在让磁场大小不变，改变方向。换句话说，我们让磁场 \(\mathbf{B}\) 的所有可能的方向构成纤维丛的底流形。这个流形是二维球面 \(S^2\) 。

当磁场的方向为球坐标下的 \((\theta,\varphi)\) 时，基态为 \(|\psi\rangle= (\cos \frac{\theta}{2} , \sin \frac{\theta}{2} \mathrm{e}^\mathrm{i\varphi})^T\)

于是 Berry 联络为：

\[\begin{aligned} A_\theta &= \mathrm{i} \langle \psi | \partial_\theta \psi\rangle \\ &= \mathrm{i}\left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2}\mathrm{e}^\mathrm{-i\varphi} \right) \partial_\theta \left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2} \mathrm{e}^\mathrm{i\varphi}\right)^T \\ &= \mathrm{i}\left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2}\mathrm{e}^\mathrm{-i\varphi} \right) \left(-\sin \frac{\theta}{2} , \cos\frac{\theta}{2}\mathrm{e}^\mathrm{i\varphi} \right)^T \\ &= 0 \end{aligned}\]

\[\begin{aligned} A_\theta &= \mathrm{i} \langle \psi | \partial_\varphi \psi\rangle \\ &= \mathrm{i}\left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2}\mathrm{e}^\mathrm{-i\varphi} \right) \partial_\varphi\left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2} \mathrm{e}^\mathrm{i\varphi}\right)^T \\ &= \mathrm{i}\left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2}\mathrm{e}^\mathrm{-i\varphi} \right) \left(0 , \mathrm{i}\sin\frac{\theta}{2}\mathrm{e}^\mathrm{i\varphi} \right)^T \\ &= -\sin^2 \frac{\theta}{2} \\ &= -\frac{1-\cos\theta}{2} \end{aligned}\]

类似地，对于激发态，有

\[\begin{aligned} A_\theta &= 0,\\ A_\varphi&= -\cos^2\frac{\theta}{2} = -\frac{1+\cos\theta}{2} \end{aligned}\]

也就是说，两个本征态的 \(A_\theta\) 都为零，而 \(A_\varphi\) 分别为 \(\frac{\pm \cos\theta - 1}{2}\) ，其中 \(+\) 对应基态， \(-\) 对应激发态。

于是 Berry 曲率为

\[\Omega_{\theta \varphi} = \partial_\theta A_\varphi - \partial_\varphi A_\theta = \mp \frac{1}{2} \sin \theta\]

陈数为

\[\begin{aligned} C&=\frac{1}{2\pi}\int_{S^2} \Omega_{\theta \varphi} \mathrm{d}\theta\wedge \mathrm{d}\varphi \\ &=\frac{1}{4\pi}\int_{S^2}  \mp  \sin \theta \ \mathrm{d}\theta\wedge \mathrm{d}\varphi \\ &= \mp 1 \end{aligned}\]

可见，对于自旋 1/2 而言，其基态的陈数为 \(-1\) ，激发态的陈数为 \(+1\) 。

对于一般的自旋 \(j\) ，可以证明，其磁量子数为 \(m\) 的本征态的陈数为 \(C_m = -2m\) 。

> **选读**  
>   
> 磁场中的自旋还可以涉及**非阿贝尔几何相位**。  
>   
> 考虑磁四极子哈密顿量 \(H= \mu(\mathbf{B} \cdot \mathbf{J})^2\) [[1]](#ref\_1)，其中 \(\mathbf{J} = (J_x,J_y,J_z)\) 是自旋 3/2 的角动量算符。  
>   
> 显然，本征态 \(m=\pm\frac{1}{2}\) 和 \(m=\pm\frac{3}{2}\) 的能级分别都是简并的。  
>   
> 此时如果缓慢变化磁场 \(\mathbf{B}\) 的方向，那么在 \(m=\pm\frac{1}{2}\) 的本征子空间上有**非阿贝尔几何相位**。但 \(m=\pm\frac{3}{2}\) 的本征子空间没有，因为有选择定则 \(\Delta m = 0, \pm1\) 。  
>   
> 对于这个例子，可以计算非阿贝尔联络和曲率[[1]](#ref\_1)，然后计算第一陈数。经过计算会发现第一陈数为零。但这不意味着这个例子是拓扑平凡的。它有一个非平凡的拓扑不变量：Stiefel–Whitney class，这里就不介绍了。

---

本系列下一篇文章：

[哈密顿力学视角下的电动力学【更高更妙的电动力学·5】](https://zhuanlan.zhihu.com/p/32052863470)## 参考  

1. ^[a](#ref\_1\_0)[b](#ref\_1\_1)A. Zee, Phys. Rev. A 38, 1 (1988).
