---
title: "波包、群速度与色散关系"
date: 2022-05-04T15:39:54+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/509148630"
author: "Haifei"
tags: ["波包"]
categories: ["数学物理方法"]
---

## 前言  

初学物理的时候，对波包和群速度的概念有些困惑。现在回头看来，其实非常简单，只是有些教科书没有讲清楚。本文梳理一下群速度的概念，以及色散关系的几个例子。

## 动量本征态和傅里叶变换  

平面波的波函数

$$|\bm p\rangle=\frac{1}{(2\pi\hbar)^{3/2}}\exp(\mathrm{i}\frac{\bm{p}}{\hbar}\cdot\bm{x})$$

是无法归一化的。

而根据量子力学的公设，所有实际存在的波函数都是可以归一化的。因此动量的本征态 $|p\rangle$ 不代表实际存在的状态。换言之，动量是不可能完全测准的。

> 假设动量可以测准，那么在测量之后，系统就会落到一个动量算子的本征态上，而这样的本征态在现实中是不可能存在的，因此动量不可能测准。

但是，平面波作为一种抽象的数学存在，对分析是很有用的。即，我们可以把一个实际存在的波分解为单色波的叠加：

$$|\psi\rangle=\sum_{\bm p}\langle \bm p|\psi \rangle |\bm p\rangle=\int\langle \bm p|\psi \rangle |\bm p\rangle\mathrm{d}^3\bm p$$

这其实就是傅里叶变换。

也可以用波矢来表述以上关系：

$$|\bm k\rangle=\frac{1}{(2\pi)^{3/2}}\exp(\mathrm{i}\bm{k}\cdot \bm{x})$$

$$|\psi\rangle=\sum_{\bm k}\langle \bm k|\psi \rangle |\bm k\rangle=\int\langle \bm k|\psi \rangle |\bm k\rangle\mathrm{d}^3\bm k$$

上述过程不仅适用于量子力学中的波函数，而是适用于一切平方可积的函数。

---

## 群速度与相速度  

实际存在的波函数大部分都是 localized（定域）的，即大部分能量限制在一定区域内，这就是波包。

波包运动的速度叫做群速度，它是对波包运动的一阶近似：

$\bm v_g=\nabla_{\bm k}\omega(\bm k)$ （\*）

与群速度概念相对的是相速度，其定义为

$$\bm v_p=\frac{\omega}{k}\hat{\bm k}$$

之所以说群速度只是波包运动的近似，是因为波包在前进的过程中不一定能保持其形状不变。也就是说，仅仅用群速度是无法完全描述波包的演化的。

实际上，由于波包中不同单色波的成分的相速度不同，波包在运动过程中会扩散开来。如果波包扩散得太开，群速度的定义是不良的。

> 波包形状不变的条件是不同单色波的相速度大小相同，即 $\omega=Ck$ ， $C$ 为常数。此时群速度等于相速度。

从（\*）式中可以看出，群速度取决于 $\omega(\bm k)$ 的形式。 $\omega(\bm k)$ 就是所谓的色散关系。

> **例 1** 对于自由空间中的电子，有 $\omega=\frac{\hbar k^2}{2m}$ 以及 $\bm v_g=\frac{\hbar \bm k}{m}$ 。而相速度为 $\bm v_p=\frac{\hbar \bm k}{2m}$ 。可见，对于自由空间中的电子波包而言，其群速度是相速度的两倍。  
>   
>  对于晶格中的电子，由于有周期性势场的存在，情况更为复杂。此时 $\omega(k)$ 不再是按照二次方变化，而是像下图这样：

{{< figure src="images/v2-8aea71f10bb47fb2be2fb39a0e8de742_1440w.jpg" >}}

注意能量正比于频率

  
  
> 可以看到，在布里渊区的边界，色散关系是不连续的，于是会形成“禁带”。  
>   
> 禁带的存在是半导体物理的基础。计算机中的晶体管开关，实际上就是用电压控制禁带中费米能级的位置，从而控制导带中的电子浓度。

相速度和群速度的概念不仅仅适用于波函数，而是适用于一切波。

> **例 2** 对于真空中的电磁波而言，有 $\omega=ck$ ，因此其相速度等于群速度等于真空中的光速，即 $v_p=v_g=c$ 。   
>   
> 对于介质中的电磁波，情况更加复杂。由于折射率 $n$ 不为 $1$ 且与 $\omega$ 有关，有 $\omega=\frac{c}{n(\omega)}k$ ， $\bm v_p=\frac{c}{n(\omega)}$ ，于是  
>  $\begin{aligned} \nabla_{\bm k}\omega&=\nabla_{\bm k}(v_p k)=\bm v_p+k\nabla_{\bm k}v_p\\&=\bm v_p-k\frac{c}{[n(\omega)]^2}\frac{\mathrm{d} n(\omega)}{\mathrm{d} \omega}\nabla_{\bm k}\omega\\ &=\bm v_p-k\frac{v_p}{n(\omega)}\frac{\mathrm{d} n(\omega)}{\mathrm{d} \omega}\nabla_{\bm k}\omega \end{aligned}$   
> 从而 $\bm v_g=\nabla_{\bm k}\omega=\frac{\bm v_p}{1+k\frac{v_p}{n}\frac{\mathrm{d}n}{\mathrm{d}\omega}}$   
>   
> 对于正常色散区， $\frac{\mathrm{d}n}{\mathrm{d}\omega}\gt 0$ ，群速度 $v_g$ 小于相速度 $v_p$ 小于光速；对于反常色散区， $\frac{\mathrm{d}n}{\mathrm{d}\omega}\lt 0$ ，群速度大于相速度，甚至可以大于光速。然而，在反常色散区中，不同波长的单色光的相速度相差很大，波包很快发散开来，此时群速度的定义是不良的。  
>   
> 有些科普说群速度是能量传播的速度。这是错误的。要记住，群速度只是波包运动的一阶近似而已，并不能完全表述波包的演化。群速度超过光速，并不说明能量/信息超光速，而是在这种情况下，群速度已经失去了意义。

> **例 3** 在声子的色散曲线中，经过原点的分支叫做声学支，在长波极限下（即 $k\rightarrow0$ ）， $\omega(k)$ 近似是线性的， $\omega(k)=v_sk$ ，此时群速度等于相速度等于声速，即 $v_p=v_g=v_s$ 。  
>   
> 对于长波极限下的光学支，有 $\mathrm{d}\omega/\mathrm{d}k=0$ ，此时群速度等于零，这就是驻波，但是此时相速度趋于无穷大。

{{< figure src="images/v2-51f6b5426e62e392e1e66d6f23b6f4c3_1440w.jpg" >}}

一维双原子链的声子色散关系

  
  

从上面的例子中可以看出，相速度和群速度都是可以超过光速的。

## 群速度公式的推导  

那么，（\*）式是怎么来的？为什么群速度是角频率对波矢的梯度？下面推导一下一维情形。

首先，可以将波包分解为平面波的叠加：

$$f(x,t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(k)\exp[\mathrm{i}(kx-\omega t)]\mathrm{d}k$$

这就是傅里叶积分（或傅里叶变换）。

现在考虑一个波包，它的平面波诸分量 $F(k)$ 分布在一个较小的范围内，否则它会很快发散开来。即 $F(k)$ 只在 $k=k_0$ 附近不为零。

因此，可以将色散关系近似为：

$$\omega(k)\approx \omega(k_0)+\left.\frac{\mathrm{d}\omega}{\mathrm{d}k}\right|_{k=k_0}\cdot(k-k_0)$$

将符号简化一下：

$$\omega=\omega_0+\omega_0^{\prime}\cdot \widetilde{k}$$

其中

$\omega_0=\omega(k_0)$ ， $\omega^\prime=\left.\frac{\mathrm{d}\omega}{\mathrm{d}k}\right|_{k=k_0}$ ， $\widetilde{k}=k-k_0$ 。

代入傅里叶积分得：

$$\begin{aligned} f(x,t)&=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(k)\exp[\mathrm{i}(kx-\omega t)]\mathrm{d}k\\ &=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(k)\exp\left\{\mathrm{i}\left[(k_0+\widetilde{k})x-(\omega_0+\omega_0^\prime\widetilde{k}) t\right]\right\}\mathrm{d}\widetilde{k}\\ &=\frac{1}{2\pi}\int_{-\infty}^{\infty}F(k)\exp\left\{\mathrm{i}\left[(k_0+\widetilde{k})x-(\omega_0+\omega_0^\prime (k_0+\widetilde{k})) t+\omega_0^\prime k_0t\right]\right\}\mathrm{d}\widetilde{k}\\ &=\exp{[-\mathrm{i}(\omega_0-\omega_0^\prime k_0)t]}\cdot\frac{1}{2\pi}\int_{-\infty}^{\infty}F(k_0+\widetilde{k})\exp{[\mathrm{i}(k_0+\widetilde{k})(x-\omega_0^\prime t)]}\mathrm{d}\widetilde{k}\\ &=\exp{[-\mathrm{i}(\omega_0-\omega_0^\prime k_0)t]}\cdot f(x-\omega_0^\prime t,0) \end{aligned}$$

可见，除了多了一个相位因子，波包整体以群速度 $\omega_0^\prime=\left.\frac{\mathrm{d}\omega}{\mathrm{d}k}\right|_{k=k_0}$ 移动。

特别地，如果色散关系是线性的，那么相位因子等于1，即不产生额外的相位变化。
