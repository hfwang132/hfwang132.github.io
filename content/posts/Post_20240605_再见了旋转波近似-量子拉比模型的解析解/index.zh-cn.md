---
title: "再见了旋转波近似：量子拉比模型的解析解"
date: 2024-06-05T20:52:29+08:00
originalURL: "https://zhuanlan.zhihu.com/p/701838204"
aliases:
  - "/rabi/"
  - "/Post_20240727_再见了旋转波近似-量子拉比模型的解析解/"
draft: false
tags: ["量子光学"]
categories: ["量子信息/量子光学"]
math: true
author: "Haifei"
---

## 1. 前言  

在量子力学的早期阶段，拉比为了处理电磁场与原子的相互作用，提出了拉比模型。由于这个模型只量子化了原子，而没有量子化电磁波，因此它虽然能解释众多现象（例如拉比振荡），但不能解释自发辐射这种涉及电磁场量子化的现象。

为了解释自发辐射等涉及电磁场量子化的现象，Jaynes 和 Cummings 在 1962 年提出了量子拉比模型（Quantum Rabi Model，**QRM**），这个模型将电磁场也量子化了，使得电磁场的真空涨落不能被忽略，于是自发辐射无非就是电磁场的真空涨落所“激发”的“受激辐射”。

然而，在 QRM 被提出后相当长一段时间内，人们都认为它没有解析解，只有做了旋转波近似（RWA）之后才有解析解。人们把做了旋转波近似后的模型叫做 Jaynes-Cummings 模型（**JCM**）。

JCM 成功解释了自发辐射和真空拉比振荡等现象，但由于做了旋转波近似，它仍然不能解释兰姆位移等现象。另外，如今人们已经能在 Circuit QED 系统中实现强耦合，而当耦合非常强的时候，旋转波近似会失效，此时 JCM 与实验结果有较大的偏差。可见，在一些情况下，人们仍然需要 QRM。

令人惊讶的是，QRM 的解析解直到 2011 年才被发现 [[1]](#ref\_1)。自那以后，人们对各种推广量子拉比模型解析解也开始感兴趣，例如推广到多原子（Dicke 模型）和多光场模式的情形。

本文将推导 QRM 的解析解，结构如下：

第二节：介绍 QRM 和 JCM 的哈密顿量

第三节：简要推导 JCM 的解析解

第四节：推导 QRM 的解析解

第五节：介绍 JCM 和 QRM 的守恒量与对称性

## 2. QRM 和 JCM 的哈密顿量  

量子拉比模型（QRM）描述了一个单模光场和二能级系统的相互作用。

记单模光场的希尔伯特空间为 $\mathcal{H} \cong L^{2}(\mathbb{R})$ ，二能级系统的希尔伯特空间为 $\mathcal{K} \cong \mathbb{C}^2$ ，则 QRM 的哈密顿量 $H\in \mathcal{L}(\mathcal{H}\otimes \mathcal{K})$ 如下：

$$\begin{aligned} H&= \underbrace{\omega \left(a^\dag a+\frac{1}{2}\right)}_{\text{field}}+ \underbrace{ \frac{\Delta}{2} \sigma_z}_{\text{atom}} +  \underbrace{g\sigma_x(a+a^\dag)}_{\text{atom-field coupling}} \\&= \underbrace{\omega \left(a^\dag a+\frac{1}{2}\right)}_{\text{field}}+ \underbrace{ \frac{\Delta}{2} \sigma_z}_{\text{atom}} +  \underbrace{g(\sigma_++\sigma_-)(a+a^\dag)}_{\text{atom-field coupling}} \end{aligned}$$

其中 $a^\dag , a$ 是 $\mathcal{H} $ 上的产生和湮灭算符， $\sigma_z, \sigma_{\pm}$ 是 $\mathcal{K}$ 上的泡利 Z 算符和升降算符。 $g$ 叫做拉比频率，它衡量了光场与二能级系统之间的耦合强度。

如果将其中能量差较大的项 $\sigma_- a$ 和 $\sigma_+ a^\dag$ 去掉，我们就得到了 Jaynes-Cummings 模型（JCM）的哈密顿量：

$$\begin{aligned} H&= \underbrace{\omega \left(a^\dag a+\frac{1}{2}\right)}_{\text{field}}+ \underbrace{ \frac{\Delta}{2} \sigma_z}_{\text{atom}} +  \underbrace{g(\sigma_+ a + \sigma_- a^{\dag})}_{\text{atom-field coupling}}\end{aligned}$$

这就是旋转波近似。被去掉的项叫做逆时针旋转项（Counter-Rotating Terms），留下来的项叫做顺时针旋转项（Co-rotating Terms）。

> 旋转波近似之所以合理，是因为逆时针旋转项涉及的两个能级的能量差为 $\omega + \Delta$ ，远大于顺时针旋转项的能量差 $|\omega - \Delta|$ 。前者涉及的指数因子为 $e^{\pm\mathrm{i} (\omega + \Delta) t}$ ，后者为 $e^{\pm\mathrm{i}(\omega-\Delta)}t$ 。由于 $e^{\pm\mathrm{i} (\omega + \Delta) t}$ 变化太快，可以视作平均为零而消掉。  
>   
> 另外，从微扰计算也可以看出这一点：做微扰计算后得到的项会正比于能量差的倒数，前者为 $\frac{1}{\omega +\Delta}$ ，后者为 $\frac{1}{|\omega - \Delta|}$ 。而 $\frac{1}{\omega + \Delta}$ 远小于 $\frac{1}{|\omega - \Delta|}$ ，因此可以将前者忽略掉。

## 2. JCM 的解析解  

我们可以将 $H$ 在光子数表象下展开：

$$\begin{aligned} H &= \color{gray}{ \begin{matrix} |g,0\rangle \\ |e,0\rangle \\ |g,1\rangle \\ |e,1\rangle \\ |g,2\rangle \\ \vdots \end{matrix} } \begin{bmatrix} 1 & 0 & 0 & 0 & 0 & \cdots \\ 0 & 1 & 0 & 0 & 0 & \cdots \\ 0 & 0 & 3 & 0 & 0 & \cdots \\ 0 & 0 & 0 & 3& 0 & \cdots \\ 0 & 0 & 0 & 0 & 5& \cdots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix} \frac{\omega}{2}+\begin{bmatrix} -1 & 0 & 0 & 0 & 0 & \cdots \\ 0 & 1 & 0 & 0 & 0 & \cdots \\ 0 & 0 & -1 & 0 & 0 & \cdots \\ 0 & 0 & 0 & 1 & 0 & \cdots \\ 0 & 0 & 0 & 0 & -1 & \cdots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix} \frac{\Delta}{2} +\begin{bmatrix} 0 & 0 & 0 & 0 & 0 & \cdots \\ 0 & 0 & 1 & 0 & 0 & \cdots \\ 0 & 1 & 0 & 0 & 0 & \cdots \\ 0 & 0 & 0 & 0 & \sqrt{2} & \cdots \\ 0 & 0 & 0 & \sqrt{2} & 0 & \cdots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix} g \end{aligned} $$

其中 $g,e$ 分别代表二能级系统的基态和激发态， $0,1,2,\cdots$ 代表光场的激发数（即光子数）。

它可以进一步写成：

$$\begin{aligned} H = \bigoplus_{n=1}^\infty  \begin{bmatrix} n\omega+\frac{\Delta}{2} & g\sqrt{n} \\ g\sqrt{n} & (n+1)\omega -\frac{\Delta}{2} \end{bmatrix} \end{aligned}$$

其中 $n$ 代表总激发数，即二能级系统激发数和光场激发数（即光子数）的总和。

这个矩阵显然可以精确对角化，特征值为 $\left(n+ \frac{1}{2}\right)\omega \pm \sqrt{\left(\frac{\omega - \Delta}{2}\right)^2 + ng^2}$ 。记 $\Delta_n =  \sqrt{\left(\frac{\omega - \Delta}{2}\right)^2 + ng^2}$，则能级就是 $E_{\pm,n} =   \left(n + \frac{1}{2}\right)\omega \pm \frac{\Delta_n}{2}$ 。

这些能级上的本征态叫做缀饰态（dressed state）：

$$\begin{aligned} |-,n\rangle &= \cos \theta_n |e,n-1\rangle - \sin \theta_n |g,n\rangle \\ |+,n\rangle &= \sin \theta_n |e,n-1\rangle + \cos \theta_n |g,n\rangle  \end{aligned}$$

其中

$$\begin{aligned} \cos \theta_n &= \frac{2\sqrt{n}g}{\sqrt{(\Delta_n-\Delta_0)^2 + 4ng^2}} \\ \sin \theta_n &= \frac{\Delta_n-\Delta_0}{\sqrt{(\Delta_n-\Delta_0)^2 + 4ng^2}} \end{aligned}$$

且 $\Delta _0 := \Delta - \omega$ 。

{{< figure src="images/v2-c32525334ed66a8d0106b3b308fe7b38_r.jpg" >}}

缀饰态的能级示意图，该图对应失谐为零（$\omega = \Delta$）的情况，$g_0:=g$ 为拉比频率，图源互联网

  
  
## 4. QRM 的解析解  

接下来我们按照 2012 年的一篇文献的方法[[2]](#ref\_2)推导 QRM 的解析解。较于 2011 年文献[[1]](#ref\_1)的最早方法，它更加适合物理学工作者而不是数学工作者。

我们把 QRM 哈密顿量在基 $\{|+\rangle, |-\rangle\} =\left\{\frac{|e\rangle + |g\rangle}{\sqrt{2}} ,\frac{|e\rangle - |g\rangle}{\sqrt{2}}\right\}$ 下展开得：

$$H =  \begin{bmatrix} \omega a^\dag a + g(a+a^\dag) & \Delta/2 \\ \Delta/2 & \omega a^\dag a + g(a-a^\dag) \end{bmatrix}$$

> 可以验证 $H = [\omega a^\dag a + g(a+a^\dag)] |+\rangle\langle+| + [\omega a^\dag a - g(a+a^\dag)] |-\rangle\langle-|  + \frac{\Delta}{2}(|+\rangle\langle-| + |-\rangle\langle+|)$

做 Bogoliubov 变换 $A = a +g/\omega,\,B=a-g/\omega$ ，并且定义 Extended Fock states：

$$|0\rangle_A=e^{-\frac{g}{\omega}(a^\dag - a)} |0\rangle = |\frac{-\omega}{g}\rangle$$

$$|n\rangle_A = \frac{A^{\dag n}}{\sqrt{n!}} |0\rangle_A$$

注意到 $|0\rangle_A$ 是一个参数为 $-\frac{\omega}{g}$ 的相干态。

可以验证 $[A,A^\dag]=1$ ，因此对于普通 Fock states 成立的关系对于 Extended Fock states 也成立：

$$A|n\rangle_A = \sqrt{n} |n-1\rangle_A$$

$$A^\dag |n\rangle_A = \sqrt{n+1} |n + 1\rangle_A$$

此时有

$$H =  \begin{bmatrix} \omega A^\dag A - g^2 /\omega& \Delta/2 \\ \Delta/2 & \omega A^\dag A - 2g(A+A^\dag) + 3g^2/\omega \end{bmatrix}$$

设本征态为：

$$|\psi\rangle=\begin{bmatrix} \sum \sqrt{n!} e_n |n\rangle_A \\ \sum \sqrt{n!} f_n |n\rangle_A \end{bmatrix}$$

代入 $H|\psi\rangle = E|\psi\rangle$ 得：

$$\begin{cases} e_n = -\frac{\Delta/2}{ n\omega -g^2/\omega - E} f_n \\ nf_n = \Omega(n-1) f_{n-1} - f_{n-2} \end{cases}$$

其中 $\Omega(n) = \frac{2g}{\omega}+\frac{1}{2g}\left[ n\omega - g^2/\omega -E - \frac{(\Delta/2)^2}{n\omega  - g^2/\omega - E}\right]$

同理，哈密顿量也可以写成：

$$H =  \begin{bmatrix} \omega B^\dag B -2g(B + B^\dag) + 3g^2 & \Delta/2 \\ \Delta/2 & \omega  B^\dag B - g^2/\omega \end{bmatrix}$$

设本征态为

$$|\psi^\prime\rangle=\begin{bmatrix} \sum \sqrt{n!} (-1)^nf_n^\prime |n\rangle_B \\ \sum \sqrt{n!} (-1)^ne_n^\prime |n\rangle_B \end{bmatrix}$$

代入 $H|\psi\rangle = E|\psi\rangle$ 得：

$$\begin{cases} e_n^\prime = -\frac{\Delta/2}{n\omega - g^2/\omega -E} f^\prime_n \\ nf^\prime_n  = \Omega(n-1)f^\prime_{n-1} - f_{n-2} \end{cases}$$

可见 $f_n$ 和 $f_n^\prime$ 以及 $e_n$ 和 $e_n^\prime$ 都满足相同的递归关系。令 $f_0 = f_0^\prime = 1$ ，则 $f_n = f_n^\prime$ ， $e_n = e_n^\prime$ 。

由于两个本征态 $|\psi \rangle, |\psi^\prime\rangle$ 之间必须成比例 $|\psi^\prime\rangle = \kappa |\psi\rangle$ ，其中 $\kappa \in \mathbb{C}$ ，于是有：

$$\begin{cases} \sum \sqrt{n!} (-1)^nf_n |n\rangle_B = \kappa \sum \sqrt{n!} e_n |n\rangle_A \\ \sum \sqrt{n!} (-1)^ne_n |n\rangle_B = \kappa\sum \sqrt{n!} f_n |n\rangle_A \end{cases}$$

两边同时左乘真空态 $\langle0|$ ，由于

$$\begin{aligned} \sqrt{n!}\langle 0 | n\rangle_A &= \langle 0 |A^{\dag n}|0\rangle_A \\&= \langle 0|(a+\lambda)^\dag | 0 \rangle_A \\&= \lambda^n\langle 0|0\rangle_A \\&= \lambda^n e^{-\lambda^2/2} \end{aligned}$$

$$\sqrt{n!} \langle 0|n\rangle_B = (-\lambda)^n e^{-\lambda^2/2}$$

其中 $\lambda = g/\omega$ 。

于是：

$$\begin{cases} \sum \lambda^n e^{-\lambda^2/2} f_n = \kappa \sum \lambda^n e^{-\lambda^2/2} e_n \\ \sum\lambda^n e^{-\lambda^2/2}e_n  = \kappa\sum \lambda^n e^{-\lambda^2/2} f_n  \end{cases}$$

$$\Rightarrow \left(\sum \lambda^n e^{-\lambda^2/2} f_n\right)^2 = \left(\sum\lambda^n e^{-\lambda^2/2} e_n \right)^2 $$

$$\Rightarrow \sum \lambda^n e^{-\lambda^2/2} (f_n \pm e_n )= 0$$

$$\begin{aligned} \Rightarrow \sum \lambda^n e^{-\lambda^2/2} f_n \left(1\pm \frac{\Delta/2}{n\omega - g\lambda -E}\right) = 0 \end{aligned}$$

令 $G_{\pm}(x) = \sum f_n \lambda^n \left(1\mp \frac{\Delta}{2\omega(x+\lambda^2-n)}\right)$ ，它是一个超越函数。

可见 $G_{\pm}(x) $ 的零点就是本征态能级（单位为 $ \omega$）。

{{< figure src="images/v2-303e4a20ba5b4010429158736c8e9049_r.jpg" >}}

$G_{\pm}(x)$ 的零点，图源 [1]

  
  

本征态为：

$$\begin{aligned} &\phantom{=}\sum_n\left[ \sqrt{n!} f_n |n\rangle_B \otimes \frac{|e\rangle + |g\rangle}{\sqrt{2}} + \sqrt{n!} e_n |n\rangle_B \otimes \frac{|e\rangle - |g\rangle}{\sqrt{2}}\right]  \\&=\sum_n \left[ \sqrt{n!/2} (f_n - e_n)\right] |n\rangle_B \otimes |g\rangle + \sum_n \left[ \sqrt{n!/2} (f_n + e_n)\right] |n\rangle_B \otimes |e\rangle \\&=\sum_n \left[ \sqrt{\frac{n!}{2}} f_n \left(1 - \frac{\Delta/2}{n\omega - g\lambda -E}\right)\right] |n\rangle_B \otimes |g\rangle + \sum_n \left[ \sqrt{\frac{n!}{2}} f_n \left(1 + \frac{\Delta/2}{n\omega - g\lambda - E}\right) \right] |n\rangle_B \otimes |e\rangle \end{aligned}$$

到此为止，我们就得到了 QRM 哈密顿量的能级和本征态的解析解。能级随耦合强度变化示意图如下所示：

{{< figure src="images/v2-e31595edaebc43fe39b75a8eddd4197c_r.jpg" >}}

JCM 到 QRM 的过渡。左边标记的是 JCM 的本征态，右边标记的是 QRM 的本征态。图源 [1]

  
  

从图中可以看到，当耦合系数增加时，基态与第一激发态的能级差会降低，这就是兰姆位移。不过我们一般说的兰姆位移是原子与多个模式的真空光场相互作用，而非此处所说的单模光场。

另外，可以看到，随着耦合系数的增加，在 JCM 下本来会相交的能级，在 QRM 下则不会相交，而是先靠近再远离。这就是所谓的 avoided crossing。

## 5. 守恒量与对称性  

JCM 有守恒量 $N = a^\dag a+\sigma_+\sigma_- = a^\dag a + (\mathbb{I} + \sigma_z)/2$ ，其本征值为 $n=0,1,2,\cdots$ ， $N|\pm,n\rangle = \left(n + \frac{1\pm 1}{2}\right)|\pm,n\rangle$ 。这个守恒量的物理意义就是激发数的总和。

守恒量 $N$ 可以生成连续的 $U(1)$ 对称性。这是因为 $[N,H] = 0 \Rightarrow [e^{-\mathrm{i\theta}N},H]=0$ 。也就是说当我们做如下变换之后，哈密顿量不变：

$$a \rightarrow e^{-\mathrm{i}\theta N} a e^{\mathrm{i}\theta N} = a e^{-\mathrm{i}\theta}$$

$$a^\dag   \rightarrow e^{-\mathrm{i}\theta N} a^\dag e^{\mathrm{i}\theta N} = a^\dag e^{\mathrm{i}\theta}$$

$$\sigma_{\pm} \rightarrow e^{-\mathrm{i}\theta N} \sigma_{\pm} e^{\mathrm{i}\theta N} = \sigma_\pm e^{\pm\mathrm{i}\theta}$$

而 QRM 的守恒量是 $\Pi = e^{-\mathrm{i}\pi N} = -\sigma_+\sigma_- \otimes e^{\mathrm{i}\pi a^\dag a}$ ，其本征值为 $\pm 1$ ， $\Pi |\pm,n\rangle = \mp (-1)^n |\pm,n\rangle$ 。

QRM 虽然失去了 $U(1)$ 对称性，但是仍有离散的 $Z_2$ 对称性，这是因为 $[\Pi,H]=0$ 使得当我们做如下变换之后，哈密顿量不变：

$$a \rightarrow \Pi a \Pi^\dag = -a$$

$$a^\dag \rightarrow \Pi a^\dag \Pi^\dag = -a^\dag$$

$$\sigma_\pm \rightarrow \Pi \sigma_\pm \Pi^\dag = -\sigma_\pm$$

$Z_2$ 对称性可以看作是 $U(1)$ 对称性从 $\theta \in [0,2\pi)$ 破缺到 $\theta \in \{0,\pi\}$ 。这一点也可以形象地从哈密顿量中看出来：JCM 只有顺时针旋转项，因此有连续的 $U(1)$ 对称性，而 QRM 既有顺时针旋转项又有逆时针旋转项，这两个项只能在 $\theta \in \{0,\pi\}$ 处汇合，因此只有离散的 $Z_2$ 对称性。

## 参考  

1. ^[a](#ref\_1\_0)[b](#ref\_1\_1)Braak, D. Integrability of the Rabi Model. Phys. Rev. Lett. 2011, 107 (10), 100401. [https://doi.org/10.1103/PhysRevLett.107.100401](https://doi.org/10.1103/PhysRevLett.107.100401)
2. [^](#ref\_2\_0)Chen, Q.-H.; Wang, C.; He, S.; Liu, T.; Wang, K.-L. Exact Solvability of the Quantum Rabi Model Using Bogoliubov Operators. Phys. Rev. A 2012, 86 (2), 023822. [https://doi.org/10.1103/PhysRevA.86.023822](https://doi.org/10.1103/PhysRevA.86.023822)
