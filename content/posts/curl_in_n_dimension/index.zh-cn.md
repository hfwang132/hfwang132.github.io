---
title: "高维空间中的旋度"
date: 2023-06-10T10:55:38+08:00
draft: false
categories: ["数学"]
tags: ["矢量微积分"]
---

### 1 微分形式

在介绍旋度之前，我们得先介绍一下微分形式和外微分算子。

一个 $n$ 阶形式可以定义为一个交替多重线性映射 $\omega:(T\_pM)^n\rightarrow \mathbb{R}$ 。它把多个向量映射成一个实数。另外，它还满足交替性，即交换两个输入向量，输出多一个负号。

因此可以显式地定义 $n$ 阶形式如下：  
$\omega^1\wedge \omega^2\wedge\cdots\wedge \omega^n(v\_1,v\_2,\cdots,v\_n)= \begin{vmatrix} \omega^1(v\_1) & \cdots & \omega^{1}(v\_n) \\\\ \vdots & \ddots & \vdots \\\\ \omega^n(v\_1) & \cdots & \omega^n(v\_n) \end{vmatrix}\in\mathbb{R}$

$T\_pM$ 上所有 $n$ 阶形式的集合可以写成 $\bigwedge^n(T^\*\_pM)$ 。

至于“微分形式”，它与“形式”的不同之处在于，它是“形式的场”，即流形上每一点都对应一个该点处的形式。换句话说，“形式”是相对于某一点来说的，而“微分形式”是相对于整个流形来说的。

### 2 外微分

外微分算子的定义如下：

外微分算子是一个映射 $\mathrm{d}: \bigwedge^n(T\_p^\*M)\rightarrow \bigwedge^{(n+1)}(T\_p^\*M)$ ，它作用到一个 $n$ 阶微分形式： $\varphi=\sum\_{I}f\_I\mathrm{d}x^{I}=\sum\_{(i\_1,\cdots,i\_n)}f\_{(i\_1,\cdots,i\_n)}\mathrm{d}x^{i\_1}\wedge\cdots\wedge\mathrm{d}x^{i\_n}$ 上，得到一个 $(n+1)$ 阶微分形式：

$\mathrm{d}\varphi=\sum\_{I}\sum\_{i}\frac{\partial f\_I}{\partial x\_i}\mathrm{d}x\_i\wedge x\_I$。


> **评论** 这一堆指标太丑陋了，不如看下面的例子。   
>   
> **例**  对于一个 3 维流形上的二阶微分形式： $ \varphi=z^2\mathrm{d}x\wedge\mathrm{d}y+x\sin y\\,\mathrm{d}y\wedge \mathrm{d}z $ ，其外导数为： $$\begin{aligned} \mathrm{d}\varphi &=\left(\frac{\partial z^2}{\partial x}\mathrm{d}x+\frac{\partial z^2}{\partial y}\mathrm{d}y+\frac{\partial z^2}{\partial z}\mathrm{d}z\right)\wedge\mathrm{d}x\wedge\mathrm{d}y \\\\ & +\left(\frac{\partial (x\sin y)}{\partial x}\mathrm{d}x+\frac{\partial (x\sin y)}{\partial y}\mathrm{d}y+\frac{\partial (x\sin y)}{\partial z}\mathrm{d}z\right)\wedge\mathrm{d}y\wedge\mathrm{d}z \\\\ &=(2z+\sin y)\\,\mathrm{d}x\wedge\mathrm{d}y\wedge\mathrm{d}z \end{aligned} $$

### 3 N 维空间中的旋度

在下面的例子中，我们将会给出旋度与外微分的关系：

例 在三维流形上，外导数算子 \mathrm{d} 作用到一个一阶微分形式后，会得到一个二阶微分形式：   
  
 $$ \begin{aligned} \mathrm{d}(f\_i\mathrm{d}x^i)&=\frac{\partial f\_1}{\partial x^1}\mathrm{d}x^1\wedge\mathrm{d}x^1+\frac{\partial f\_1}{\partial x^2}\mathrm{d}x^2\wedge\mathrm{d}x^1+\frac{\partial f\_1}{\partial x^3}\mathrm{d}x^3\wedge\mathrm{d}x^1 \\\\ &+\frac{\partial f\_2}{\partial x^1}\mathrm{d}x^1\wedge\mathrm{d}x^2+\frac{\partial f\_2}{\partial x^2}\mathrm{d}x^2\wedge\mathrm{d}x^2+\frac{\partial f\_2}{\partial x^3}\mathrm{d}x^3\wedge\mathrm{d}x^2 \\\\ &+\frac{\partial f\_3}{\partial x^1}\mathrm{d}x^1\wedge\mathrm{d}x^3+\frac{\partial f\_3}{\partial x^2}\mathrm{d}x^2\wedge\mathrm{d}x^3+\frac{\partial f\_3}{\partial x^3}\mathrm{d}x^3\wedge\mathrm{d}x^3 \end{aligned} $$  
  
对它使用一次 Hodge 星算子，会得到一个一阶微分形式：   
  
$$ \begin{aligned} \star \mathrm{d}(f\_i\mathrm{d}x^i)&=\phantom{+\frac{\partial f\_1}{\partial x^2}\mathrm{d}x^3}-\frac{\partial f\_1}{\partial x^2}\mathrm{d}x^3+\frac{\partial f\_1}{\partial x^3}\mathrm{d}x^2 \\\\ &\phantom{=}+\frac{\partial f\_2}{\partial x^1}\mathrm{d}x^3 \phantom{\\,\\,\\,\\,-\frac{\partial f\_1}{\partial x^2}\mathrm{d}x^3} -\frac{\partial f\_2}{\partial x^3}\mathrm{d}x^1 \\\\ &\phantom{=}-\frac{\partial f\_3}{\partial x^1}\mathrm{d}x^2+\frac{\partial f\_3}{\partial x^2}\mathrm{d}x^1 \\\\ &=\left(\frac{\partial f\_3}{\partial x^2}-\frac{\partial f\_2}{\partial x^3}\right)\mathrm{d}x^1 + \left(\frac{\partial f\_1}{\partial x^3}-\frac{\partial f\_3}{\partial x^1}\right)\mathrm{d}x^2 + \left(\frac{\partial f\_2}{\partial x^1}-\frac{\partial f\_1}{\partial x^2}\right)\mathrm{d}x^3 \end{aligned} $$
  
它可以写成旋度和切向量的内积： $\star\mathrm{d}f:\star\mathrm{d}f(v)=\langle \nabla \times f^{\sharp}\mid v \rangle$   
  
我们暂时不介绍什么是 Hodge 星算子，现在，你只需要知道，在 3 维流形上，Hodge 算子作用到一个的 $n$ 阶微分形式上会得到一个 $(3-n)$ 阶微分形式。  
  
具体地，如果配备了内积 $\langle\mathrm{d}x^i,\mathrm{d}x^j\rangle=\delta^{j}\_i$ ，则有：   
 $$\star(\mathrm{d}x^i \wedge \mathrm{d}x^j)=\mathrm{d}x^k$$
 $$\star\mathrm{d}x^i =\mathrm{d}x^j\wedge \mathrm{d}x^k$$
 $$\star(f\\,\mathrm{d}x^i \wedge\mathrm{d}x^j\wedge \mathrm{d}x^k)=f$$
 $$\star f=f \\,\mathrm{d}x^i \wedge\mathrm{d}x^j\wedge \mathrm{d}x^k$$   
其中 $(i,j,k)$ 是 $(1,2,3)$ 的一个偶置换。   
  
另外，注意到我们用了一个升号： $\sharp$ 。这是因为旋度是作用在切向量场，而非余切向量场上的。  
  
具体来说，旋度 $\nabla\times$ 把切向量场映射成一个切向量场： $\Gamma(TM)\rightarrow \Gamma(TM)$ 。但是 $f\in \Gamma(T^\*M)$ 是一个余切向量场（一阶微分形式），因此我们先要给将它“升”为切向量场： $f^\sharp\in \Gamma(TM)$ 。 这其实就是物理人喜闻乐见的指标升降： $g^{ij}X\_i=X^j$ 。同理， $\flat$ 代表将切向量场“降”为余切向量场： $g\_{ij}X^i=X\_j$ 。  
  
 回到上面的例子，我们有一个由内积诱导的典范同构：  
  
 $$\sharp:\star \mathrm{d}f\mapsto \nabla\times f^{\sharp}$$
或写成： $$(\star \mathrm{d}f)^\sharp = \nabla\times f^{\sharp}$$
或写成： $$\star \mathrm{d}f(v) = \langle\nabla\times f^{\sharp}\mid v\rangle$$  
  
其中 $f$ 是一个一阶微分形式。   
  
我们还可以写成： $\nabla\times F=(\star \mathrm{d} (F^{\flat}))^{\sharp}$  
  
其中 $F=f^\sharp$ 是一个切向量场， $f$ 是一个余切向量场（一阶微分形式）。

通过上面例子的启发，我们可以将旋度定义为

$$ \begin{aligned} (\nabla\times) :\quad & \Gamma(TM)\rightarrow \Gamma\left(\bigwedge^{n-2}TM\right)\\ &F\mapsto(\star \mathrm{d} (F^{\flat}))^{\sharp} \end{aligned} $$ 

其中 $F$ 是一个切向量场； $F^{\flat}$ 是一个余切向量场（一阶微分形式）；  $\mathrm{d} (F^{\flat})$ 是一个二阶微分形式， $\star \mathrm{d} (F^{\flat})$ 是一个 (n-2) 阶微分形式。

**因此，一个** $n$ **维流形上的切向量场** $F$ **的旋度** $(\star \mathrm{d} (F^{\flat}))^{\sharp}$ **是一个** $(n-2,0)$ **型反对称张量场。或者说是一个 (n-2)-向量场。**

在 3 维流形中，旋度退化为一个切向量场。在 2 维流形中，旋度退化为一个标量场。