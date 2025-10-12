---
title: "当我们做二次量子化的时候，我们究竟在做什么？"
date: 2025-10-12T20:33:12+08:00
draft: false
tags: ["二次量子化"]
categories: ["量子力学"]
---

**一次量子化无法描述粒子数的叠加态，更无法描述粒子数变化情况下的动力学**

一次量子化和二次量子化的说法很容易让人以为它们是等价的，哪个方便就用哪个，就像薛定谔和海森堡表象一样。实则不然。二次量子化的描述能力是严格强于一次量子化的。一次量子化只是二次量子化在粒子数固定情形下的简化描述，本身是有缺陷的。

考虑这样一个量子态，它是以下两种情形的等权相干叠加：

1. 粒子数为 1，且波函数为 $\psi\_1(x\_1)$
2. 粒子数为 2，且波函数为 $\psi\_2(x\_1, x\_2)$

对于这样一个量子态，你是没办法写下它的波函数的。这样写很明显也不对：

$\psi(x\_1,x\_2) = \frac{1}{\sqrt{2}}\psi\_1(x\_1)+\frac{1}{\sqrt{2}}\psi\_2(x\_1,x\_2) \quad (\times)$

实际上，正确的写法只能使用二次量子化的语言：

$\begin{aligned} |\psi\rangle = \frac{1}{\sqrt{2}} \int \mathrm{d}x\_1 \psi\_1(x\_1) \hat{\psi}^\dagger(x\_1) |\text{vac}\rangle + \frac{1}{\sqrt{2}} \iint \frac{1}{2}\mathrm{d}x\_1\mathrm{d}x\_2 \psi\_2(x\_1,x\_2) \hat{\psi}^\dagger(x\_1)\hat{\psi}^\dagger(x\_2) | \text{vac}\rangle \end{aligned}$

其中 $\hat{\psi}^\dagger$ 是场的产生算符， $|\text{vac}\rangle$ 是真空态。

之所以在量子力学中我们大部分时间只需要一次量子化，是因为量子力学处理的主要是非相对论情形，也就是低能标情形，而低能标的电子是近似粒子数守恒的，不守恒的部分可以作为微扰来处理，比如氢原子能级的达尔文项（Darwin term），来源于电子-正电子对的涨落。

另一方面，光子虽然通常粒子数不守恒，但量子力学是将光子场作为经典电磁场来处理，而经典电磁场正好近似刻画了宇宙中最常出现的光场态——相干态：

$\begin{aligned} |\alpha\_\mathbf{k}\rangle &=  \exp(-|\alpha\_\mathbf{k}|^2/2)\exp(\alpha\_\mathbf{k}\hat{a}\_\mathbf{k}) | \text{vac}\rangle \\\\ &= \exp(-|\alpha\_\mathbf{k}|^2/2) \sum\_{n=0}^{\infty} \frac{\alpha^n\_\mathbf{k}}{\sqrt{n!}} |n\_\mathbf{k}\rangle \end{aligned}$

其中 $\mathbf{k}$ 代表空间模式和偏振模式， $\hat{a}\_\mathbf{k}$ 是模式 $\mathbf{k}$ 上的产生算符， $|n\_\mathbf{k}\rangle$ 是模式 $\mathbf{k}$ 上的 $n$ 粒子数态， $\alpha\_\mathbf{k} \in \mathbb{C}$ 描述模式 $\mathbf{k}$ 的振幅和相位。于是电磁场 $A$ 作为不同 $\mathbf{k}$ 模式的叠加，其对应的量子态可以写成：

$\begin{aligned} |A\rangle = \exp\left(-\frac{1}{2}\sum\_{\mathbf{k}}|\alpha\_\mathbf{k}|^2\right)\exp\left(\sum\_{\mathbf{k}}\alpha\_\mathbf{k}\hat{a}\_\mathbf{k}\right) | \text{vac}\rangle \end{aligned}$

可以证明，这是电场算符和磁场算符的最小不确定性态，对应宏观经典电磁波。

光子很容易损耗（散射，吸收），而从损耗动力学中存活下来的态就是相干态，即 Lindblad 算符——湮灭算符的本征态。

处于相干态的光场，其量子性只在粒子数很低，即接近真空时才体现出来，比如氢原子能级的兰姆位移等等。而这些效应通常非常弱，可以在经典电磁波的基础上作修正。这就是为什么光场很难表现出宏观量子性，以及量子力学使用经典电磁场也能如此成功的原因。

然而，一旦光子之间产生纠缠，或者光子和电子产生纠缠，那么光场就没办法用经典电磁场来描述了。

总之，量子力学（一次量子化）只是一种本身有缺陷的近似理论，它没法描述粒子数的叠加态，完整的描述必须要使用量子场论（二次量子化）。

回到问题：当我们在做二次量子化的时候，我们在做什么？答案很简单：我们在做我们应该且必须做的事情。