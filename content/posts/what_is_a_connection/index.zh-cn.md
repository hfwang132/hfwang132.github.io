---
title: "什么是联络【更高更妙的电动力学·番外篇 1】"
date: 2025-10-12T20:22:53+08:00
draft: draft
tags: ["联络", "广义相对论", "电动力学"]
categories: ["数学物理方法"]
---

在前面的文章中，我们说电磁场是联络。这让很多同学想到广义相对论里的联络。这两种联络有什么区别和共同点？

电磁场联络 $A$ 是主丛上的联络，而广义相对论联络 $\Gamma$ 是矢量丛上的联络，它们的定义方式看似很不同。有没有办法将它们联系起来呢？

有的！兄弟有的！我们完全可以将广相的联络也看成是主丛上的联络。

实际上，可以把 $\Gamma$ 看成标架丛上的联络，这样一来，克氏符的变换规则

$\boxed{ \begin{aligned} \bar{\Gamma}^i\_{\mu j} = \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial x^l}{\partial \bar{x}^j} \frac{\partial x^\nu}{\partial \bar{x}^\mu} \Gamma^k\_{\nu l}  \color{red}{ + \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial x^\mu \partial \bar{x}^j}} \end{aligned} }$

就只不过是一个规范变换：

$\boxed{ \bar{A} = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} }$

多出来的非齐次项 $ g^{-1} \mathrm{d}g$ 是规范变换天生自带的。

## 一、规范变换  

在主丛上做规范变换 $g$ 的时候，联络 $A$ 的变换式如下：

$A \mapsto g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g}$

举个例子，最简单的规范变换就是 $U(1)$ -纤维丛上的规范变换 $g=\mathrm{e}^{\mathrm{i}\lambda}$ ：

$\begin{aligned} A &\mapsto g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} \\\\ &= \mathrm{e}^{-\mathrm{i}\lambda} A \mathrm{e}^{\mathrm{i}\lambda} \color{red}{+ \mathrm{e}^{-\mathrm{i}\lambda}\mathrm{d}  \mathrm{e}^{\mathrm{i}\lambda}} \\\\ &= A \color{red}{+\mathrm{i}\ \mathrm{d}\lambda} \end{aligned}$

在物理中，通常将虚数单位 $\mathrm{i}$ 从联络 $A$ 中提取出来。所以上式在物理中写成：

$A \mapsto A \color{red}{+ \mathrm{d}\lambda}$

记 $A^\sharp=(\phi,\mathbf{A})$ 并采用 $(+,-,-,-)$ 度规，那么上式就是：

$\boxed{ \begin{aligned} \phi &\mapsto \phi \color{red}{+ \partial\_t \lambda} \\\\ \mathbf{A} &\mapsto \mathbf{A} \color{red}{- \nabla \lambda} \end{aligned} }$

这就是电磁规范变换。注意此处的 $\nabla$ 代表梯度，而非协变导数。

以上的 $A$ 是一个李代数取值的 1-形式： $A\in \Omega^1(M, \mathfrak{u}(1))$ ，意思就是它接受一个切向量，返回一个 $\mathfrak{u}(1) \cong \mathrm{i}\mathbb{R}$ 中的元素。

如果把 $\mathrm{i}$ 提取出来，那么就和普通的实数取值的 1-形式没有任何区别了。

我们之所以认为电磁势 $A$ 是向量场，原因就在于此。

同样的事情也发生在克氏符身上。

## 二、标架丛上的联络  

现在，我们把电磁规范变换照搬到克氏符的情况。唯一的区别就是把 $U(1)$ -主丛换成标架丛 $FM$ ，也就是 $GL(n)$ -主丛。

> 标架（frame）定义为基向量的有序组 $f:=(e\_1, e\_2, ...,e\_n)$ 。标架之间的变换用 $GL(n)$ 来描述，并且 $GL(n)$ 的群作用是自由且传递的，因此标架丛是一个 $GL(n)$ -主丛。

此时的联络 $\Gamma$ 是一个主丛上的李代数取值的 1-形式：

$\Gamma\_{\text{global}} \in \Omega^1(FM, \mathfrak{gl}(n))$

选取一组局部标架 $s$ ，可以将其局部平凡化为 $\Gamma = s^\*\Gamma\_{\text{global}} \in \Omega^1(M, \mathfrak{gl}(n))$ 。

它的取值作为李代数 $\mathfrak{gl}(n)$ 的元素，可以作用到标架 $f $ 上得到 $\Gamma f $ ，表示标架的无穷小 $GL(n)$ 变换。

注意这里的 1-形式 $\Gamma$ 还没有接受一个向量。严谨一些的话，应该把待接受的向量作为空位写出来，就是：

$\Gamma(\cdot) f $

也可以把接受的向量 $X$ 写成 $\Gamma$ 的下标 $\Gamma\_X$ ：

$\Gamma\_X f := \Gamma(X)f $

这样写出来就很清晰了： $\Gamma$ 是李代数取值的 1-形式，它作用到向量 $X$ 上得到李代数的元素 $\Gamma\_X \in \mathfrak{gl}(n)$ ，而它可以进一步作用到 $f$ 身上得到 $\Gamma\_X f$ 。

到此为止，没有任何问题， $\Gamma$ 是一个 1-形式，也就是一个 (0,1)-型张量，只不过它作用到向量后的取值是 $\mathfrak{gl}(n)$ 里的一个矩阵。

问题出在哪呢？问题出在我们把它写成指标形式的时候，没有区分 $\Gamma$ 作为 1-形式的作用，和 $\Gamma$ 作为李代数的作用。

作为 1-形式时， $\Gamma$ 可以展开写成：

$\Gamma =\Gamma\_\mu\mathrm{d}x^\mu$

其中 $\Gamma\_\mu$ 是李代数 $\mathfrak{gl}(n)$ 中的元素。这里我们说 $\Gamma$ 是 (0,1)-型张量，没有任何问题。而 $\Gamma\_\mu$ 作为分量也的确是按照 (0,1)-型张量场的分量变换规则来变换的。

但如果我们要把 $\Gamma\_\mu \in \mathfrak{gl}(n)$ 在局部标架下进一步展开呢？此时有

$\Gamma\_\mu = (\Gamma\_\mu)\_{j}^i\partial\_i \otimes \mathrm{d}x^j = :\Gamma\_{\mu j}^i \partial\_i \otimes \mathrm{d}x^j$

此时如果我们写下 $\Gamma^i\_j := (\Gamma\_\mu)^i\_j \mathrm{d}x^\mu$ ，那么这个 $\Gamma^i\_j$ 就不是李代数取值的 1-形式了，而是实数取值的 1-形式，相当于我们把 $\Gamma$ 的 $\mathfrak{gl}(n)$ 取值的每一个矩阵元 $\Gamma^i\_j$ 拿出来作为 1-形式。

问题就出在这里： $\Gamma^i\_j$ 虽然有上下标，但它本身就是一个 1-形式，而不是任何张量场的分量。而 $\Gamma^i\_j$ 作为 1-形式的定义是依赖于坐标系（ $\partial\_i \otimes \mathrm{d}x^j$ ）的选取的。之所以有些人说它是坐标系依赖的张量场，原因就在于此了。

## 三、标架丛上的规范变换  

最后，我们从规范变换

$\bar{A}  = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g}$

导出克氏符的变换规则。

> 注意这里的 $g$ 不是指度规张量，而是规范变换。

首先，让我们把 $A$ 换成 $\Gamma$ ：

$\bar{\Gamma} = g^{-1} \Gamma g \color{red}{+ g^{-1} \mathrm{d}g}$

然后，将 1-形式 $\bar{\Gamma}$ 和 $\mathrm{d}g$ 在局部标架下展开成 $\bar{\Gamma}\_\mu \mathrm{d}\bar{x}^\mu$ 和 $(\bar{\partial}\_\nu g)\mathrm{d}\bar{x}^\nu$ ：

$\begin{aligned} \bar{\Gamma}\_\mu \mathrm{d}\bar{x}^\mu &\mapsto g^{-1} (\Gamma\_\nu \mathrm{d}x^\nu) g \color{red}{+ g^{-1} (\bar{\partial}\_\mu g)\mathrm{d}\bar{x}^\mu} \\\\ &= g^\nu\_\mu \ g^{-1} \left(\Gamma\_\nu \mathrm{d}\bar{x}^\mu \right) g \color{red}{+ g^{-1} (\bar{\partial}\_\mu g)\mathrm{d}\bar{x}^\mu}  \end{aligned}$

其中 $\bar{\partial}\_\mu :=\frac{\partial}{\partial \bar{x}^\mu}$ ， $g^\nu\_\mu = \frac{\partial x^\nu}{\partial \bar{x}^\mu}$ 。

将 $\mathrm{d}\bar{x}^\mu$ 拿出来，得到：

$\begin{aligned} \bar{\Gamma}\_\mu  &= g^\nu\_\mu \ g^{-1} \left(\Gamma\_\nu \right) g \color{red}{+ g^{-1} (\bar{\partial}\_\mu g)}  \end{aligned}$

然后，将规范变换

$\begin{aligned} g = g^i\_j  \partial\_i \otimes \mathrm{d}x^j= \frac{\partial x^i}{\partial \bar{x}^j} \partial\_i \otimes \mathrm{d}x^j \end{aligned}$

代入，并取分量得：

$\begin{aligned} (\bar{\Gamma}\_\mu )^i\_j &= g^\nu\_\mu(g^{-1})^i\_k \left(\Gamma\_\nu \right)^k\_l g^l\_j \color{red}{+ (g^{-1})^i\_k (\bar{\partial}\_\mu g^k\_l)}  \end{aligned}$

最后，将规范变换的分量

$\begin{aligned} g^i\_j = \frac{\partial x^i}{\partial \bar{x}^j} ,\quad (g^{-1})^i\_j = \frac{\partial \bar{x}^i}{\partial x^j} \end{aligned}$

代入得：

$\begin{aligned} (\bar{\Gamma}\_\mu )^i\_j &= \frac{\partial x^\nu}{\partial \bar{x}^\mu}\frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial x^l}{\partial \bar{x}^j} \left(\Gamma\_\nu \right)^k\_l  \color{red}{+ \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial \bar{x}^\mu \partial \bar{x}^j}}  \end{aligned}$

记 $\Gamma\_{\mu j}^i := (\Gamma\_{\mu})^{i}\_{j}$ ，就得到了克氏符的变换式：

$\boxed{ \begin{aligned} \bar{\Gamma}^i\_{\mu j} = \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial x^l}{\partial \bar{x}^j} \frac{\partial x^\nu}{\partial \bar{x}^\mu} \Gamma^k\_{\nu l}  \color{red}{ + \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial x^\mu \partial \bar{x}^j}} \end{aligned} }$

有必要记住这个式子吗？没必要，只要记住 $\boxed{ \bar{A}  = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} }$ 就可以了。

## 四、引力  

特别地，时空底流形上配备了度规，此时我们只考虑标准正交基作为标架，因此结构群从 $GL(4)$ 变成保度规的子群，即洛伦兹群 $SO(1,3)$ 。于是，引力场就可以看作是洛伦兹群 $SO(1,3)$ 的规范场[#ref\\\\_1](#ref\\\\_1)，正如电磁场是 $U(1)$ 规范场，胶子场是 $SU(3)$ 规范场，等等。

## 补充：规范变换的推导  

那么，规范变换式 $\boxed{ \bar{A}  = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} }$ 是怎么来的呢？它同样可以从更基本的关系中的得到。

这里说的更基本的关系就是 $\boxed{ \mathrm{D} = \mathrm{d} + A \ \wedge }$ ，即协变外微分等于外微分加联络。

> 在标架丛上， $\mathrm{D}$ 就是协变导数 $\nabla$ 。

在规范变换 $g$ 下，场按照 $\bar{\psi} = g^{-1} \psi$ 变化。我们希望场的协变外微分 $\mathrm{D} \psi = \mathrm{d} \psi + A \wedge \psi$ 也按照同样的方式变化，即：

$\mathrm{\bar{D}}\bar{\psi} = g^{-1}(\mathrm{D}\psi )$ 。

> 这相当于要求 $\boxed{ \bar{\mathrm{D}} = g^{-1} \mathrm{D} g }$ 。

将上式左边展开：

$\begin{aligned} \mathrm{\bar{D}}\bar{\psi} &= (\mathrm{\mathrm{d}+\bar{A}}\ \wedge)(g^{-1}\psi) \\\\ &= \mathrm{d}(g^{-1}\psi) + \bar{A} \wedge (g^{-1}\psi) \\\\ &= (\mathrm{d} g^{-1})\psi + g^{-1} \mathrm{d}\psi + \bar{A}g^{-1} \wedge \psi \end{aligned}$

右边展开：

$\begin{aligned} g^{-1}(\mathrm{D}\psi ) &= g^{-1} (\mathrm{d} + A\ \wedge )\psi\\\\ &= g^{-1}\mathrm{d} \psi + g^{-1} A \wedge \psi \end{aligned}$

比较两边得：

$\bar{A}g^{-1} \wedge \psi = g^{-1} A \wedge \psi - (\mathrm{d} g^{-1} )\psi$

将 $\psi$ 拿出来：

$ \bar{A} g^{-1}= g^{-1} A - \mathrm{d}g^{-1}$

右乘 $g$ ，并利用 $\mathrm{d}(g^{-1}g)=0$ 得：

$\boxed{ \bar{A} = g^{-1} A g + g^{-1} \mathrm{d} g }$

这样就得到了联络在规范变换下的变换式。

## 曲率张量  

主丛上的曲率 $F$ 定义为协变外微分 $\mathrm{D}$ 的平方，是一个 2-形式：

$\boxed{ F =\mathrm{D}^2 }$

代入 $\mathrm{D} = \mathrm{d} + A \ \wedge$ 得：

$\begin{aligned} \mathrm{D}^2 \psi &= (\mathrm{d} + A\ \wedge)^2 \psi \\\\ &= \cancel{\mathrm{d}\mathrm{d}} + \mathrm{d} (A \wedge \psi) + A \wedge (\mathrm{d}\psi) + A \wedge A \wedge \psi \\\\ &=\mathrm{d} A \wedge \psi \cancel{- A \wedge \mathrm{d}\psi} \cancel{+A\wedge \mathrm{d}\psi} + A \wedge A \wedge \psi \\\\ &= (\mathrm{d} A+ A \wedge A)\wedge  \psi \end{aligned}$

所以有：

$\boxed{ F=\mathrm{d} A + A \wedge A }$

将 $F$ 展开成 $F = \frac{1}{2}F\_{\mu\nu} \mathrm{d}x^\mu \wedge \mathrm{d}x^\nu$ ， $A$ 展开成 $A = A\_{\mu} \mathrm{d}x^{\mu}$ ，代入上式得：

$F\_{\mu\nu} = \partial\_\mu A\_\nu - \partial\_\nu A\_\mu + [A\_\mu , A\_\nu]$

以上推导适用于一切主丛。现在，我们考虑标架丛作为主丛，其纤维上有自由且传递的 $GL(n)$ 作用，李代数为 $\mathfrak{gl}(n)$ ，于是上式的左右两边都是 $\mathfrak{gl}(n)$ 中的矩阵： $F\_{\mu\nu} = \{ (F\_{\mu\nu})^i\_j\}, \ \ A\_{\mu}=\{(A\_\mu)^i\_j\}$ 。

记 $R^i\_{j\mu\nu} := (F\_{\mu\nu})^i\_j$ ， $\Gamma^{i}\_{\mu j}:= (A\_\mu)^i\_j$ ，代入上式得：

$\boxed{ R^i\_{j\mu\nu}= \partial\_\mu \Gamma^i\_{\nu j} - \partial\_\nu \Gamma^i\_{\mu j} + \Gamma^{i}\_{\mu k} F^{k}\_{\nu j} -  \Gamma^{i}\_{\nu k} F^{k}\_{\mu j} }$

这正是曲率张量。

诶？等等？为什么联络 $\Gamma^i\_{\mu j}$ 不是张量场的分量，但 $R^i\_{j\mu\nu}$ 却是张量场的分量呢？

这是因为，虽然联络 $A$ 不是规范不变的，但曲率 $F$ 是规范不变（或者说规范协变）的。从下式可以看出，曲率的变换式只有齐次项：

$\begin{aligned} \mathrm{\bar{\nabla}} &= g^{-1} \mathrm{\nabla} g \\\\ \Rightarrow \bar{F} &= \bar{\nabla}^2 = (g^{-1} \nabla g)^2 = \underbrace{g^{-1} F g}\_{\text{homogeneous}} \end{aligned}$

对比联络的变换式，它有非齐次项：

$A \mapsto \underbrace{g^{-1}A g}\_{\text{homogeneous}} \color{red}{+ \underbrace{g^{-1} \mathrm{d}g}\_{\text{inhomogeneous}}}$

## 参考  

1. [#ref\\\\_1\\\\_0](#ref\\\\_1\\\\_0)Utiyama, Ryoyu. "Invariant theoretical interpretation of interaction." Physical Review 101.5 (1956): 1597. [https://doi.org/10.1103/PhysRev.101.1597](https://doi.org/10.1103/PhysRev.101.1597)