---
title: "微分几何视角下的电动力学【更高更妙的电动力学·1】"
date: 2025-04-06T00:43:40+08:00
draft: false
categories: ["数学物理方法"]
tags: ["微分几何", "电动力学"]
---

### 前言  

你可能听说过麦克斯韦方程有很简单的形式：

$\begin{aligned} \mathrm{d} F&=0 \\\\ \mathrm{d} \star F &= \mu\_0 \star J \end{aligned}$

又或者是

$\begin{aligned} \partial\_\mu (\star{F})^{\mu \nu}&= 0 \\\\ \partial\_\mu F^{\mu\nu}&= \mu\_0 J^\nu  \end{aligned}$

> 注：严格来说，其中 $\mathrm{d}F=0$ （或者 $\partial\_\mu (\star{F})^{\mu \nu}= 0$ ）并不属于电磁场的动力学方程，而是属于电磁场自身结构的一部分。这是因为根据场强的定义 $F=\mathrm{d}A$ 就能得到 $\mathrm{d}F=0$ 。

这究竟是怎么一回事？这是否意味着其实存在更高更深奥的视角？

没错，就是如此。本文将从最小作用量原理出发推导麦克斯韦方程，并且在过程中使用微分几何的语言。

为什么要用微分几何的语言？第一，它帮助我们将电磁场的数学结构看得更加清楚，第二，它使得将麦克斯韦方程推广到弯曲时空中非常容易。

在那之前，我们要先做一些数学上的准备工作。数学不错的读者可以跳过。

## 一、准备工作  
### 1.1 场论和变分法  

场论的背景是配备了闵氏度规的四维时空，记为 $M$ 。

各种物理场（如电磁场）在数学上就是流形 $M$ 上的场（如矢量场）。

给定 $M$ 上的场 $\phi$ 和拉氏量 $\mathcal{L}[\phi, \partial\_\mu \phi]$ ，其中 $\partial\_\mu \phi := \frac{\partial \phi}{\partial x^\mu}$ 。

作用量定义为 $S[\phi] := \int \mathcal{L}[\phi, \partial\_\mu \phi] \mathrm{d}^4x$ 。对 $\phi, \partial\_\mu \phi$ 进行变分：

$\begin{aligned} \delta S[\phi] &= \int \delta\mathcal{L}[\phi, \partial\_\mu \phi] \mathrm{d}^4x \\\\  &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} \delta \phi+\frac{\partial \mathcal{L}}{\partial(\partial\_\mu \phi)}\delta(\partial\_\mu \phi)\right]\mathrm{d}^4x \\\\ &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} \delta \phi+\frac{\partial \mathcal{L}}{\partial(\partial\_\mu \phi)}\partial\_\mu (\delta\phi)\right]\mathrm{d}^4x \\\\ &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} \delta \phi-\left(\partial\_\mu \frac{\partial \mathcal{L}}{\partial(\partial\_\mu \phi)}\right)\delta\phi\right]\mathrm{d}^4x \\\\ &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} -\partial\_\mu \frac{\partial \mathcal{L}}{\partial(\partial\_\mu \phi)}\right] (\delta\phi )\mathrm{d}^4x \end{aligned}$

其中第三个等号用到了 $\delta \partial\_\mu = \partial\_\mu\delta$ ，第四个等号用到了分部积分。注意用到了爱因斯坦求和约定。

根据最小作用量原理，令 $\delta S=0$ ，由 $\delta \phi$ 的任意性，则有

$\begin{aligned} \frac{\partial \mathcal{L}}{\partial \phi} -\partial\_\mu \frac{\partial \mathcal{L}}{\partial(\partial\_\mu \phi)} = 0 \end{aligned}$

这就是场变分的欧拉-拉格朗日方程。这和经典力学中的欧拉-拉格朗日方程略有不同，因为在经典力学中，变分的对象是粒子的一维的运动轨迹，而这里变分的对象是四维场的所有可能配置。

### 1.2 微分几何  

由于我们的时空是平直的，我们不需要太多的微分几何知识。只需要知道最基本的逆变（Contravariant）、协变（Covariant）、微分形式（Differential Forms）和外微分（Exterior Derivative）就差不多了。

**1.2.1 逆变矢量**

在接触微分几何前，我们绝大多数时间都在使用逆变矢量场，而非协变矢量场。这是因为当我们选定一组基之后，坐标变换是基变换的逆变换，这就是“逆变”的意思，即变换规则与基变换相反。

例如，给定一个矢量场 $A^\mu = (A^x, A^y, A^z)$ ，即 $A = A^\mu e\_\mu$ ，其中 $e\_\mu$ 是我们选取的基。当做基变换 $e^\prime\_\nu = M^{\mu}\_\nu e\_{\mu}$ 时，由于 $A^\mu e\_\mu = A^{\prime \mu} e^\prime\_\mu$ ，很显然，坐标变换就应当是逆变换： $A^{\prime \mu} = (M^{-1})^{\mu}\_{\nu} A^\nu$ 。

实际上，可以令 $e\_\mu = \partial\_\mu = \frac{\partial}{\partial x^\mu}$ 。这看起来可能很奇怪，不过在微分几何中，逆变矢量的定义就是偏导算子！这点暂时不理解也没关系，不影响后续的推导。

注意，逆变矢量的坐标都应该写成上标，例如 $A^\mu$ ，以便于和基的下标 $e\_\mu$ 缩并（根据爱因斯坦求和约定）。

**1.2.2 协变矢量**

反过来，“协变”的意思就是坐标变换和基变换的矩阵相同。但怎么会有这样的矢量呢？

实际上，协变矢量生活在另一个空间，叫做原空间的对偶空间。

对偶空间中的矢量 $\omega\_\mu$ （写成下标）可以和原空间中的矢量 $v^{\mu}$ （上标）相互缩并成为一个标量： $\omega\_\mu v^\mu = C$ 。

与 $e\_\mu = \partial\_\mu$ 对偶的基是 $\mathrm{d}x^\mu$ ，满足 $\mathrm{d}x^\mu \partial\_\nu = \delta^\mu\_\nu = \begin{cases} 1 & \mu=\nu \\\\ 0 & \mu\ne \nu\end{cases}$ 。运用和之前相似的推理，我们能够得出，对偶基 $\mathrm{d}x^\mu$ 的变换矩阵是基 $\partial\_\mu$ 变换的逆矩阵。从而，对偶矢量的坐标 $\omega\_\mu$ 变换矩阵是基 $v^\mu$ 变换矩阵的逆的逆，也就是正好等于基变换矩阵本身。这就是“协变”的意思，即变换规则与基变换相同。

**1.2.3 度规**

协变矢量和逆变矢量之间不能直接转换，除非我们有一个度规。度规是一个二阶对称协变张量场 $g\_{\mu\nu} = g\_{\nu\mu}$ 。

度规是流形上的额外结构。不是所有流形都天生拥有度规。配备了度规的流形叫做黎曼流形。如果度规不是正定的，那么该流形就叫做伪黎曼流形。物理中用到的流形是伪黎曼流形，因为闵氏度规不是正定的。

借助度规 $g\_{\mu\nu}$ ，我们可以将逆变矢量转化为协变矢量 $A\_\mu = g\_{\mu\nu} A^\nu$ ，也可以借助 $g^{\mu a}g\_{a\mu}=\delta^\mu\_\nu$ 定义逆变度规 $g^{\mu\nu}$ ，从而将协变矢量转化为逆变矢量 $A^\mu = g^{\mu\nu} A\_\nu$ 。

在狭义相对论中，我们使用闵氏度规：

$\begin{aligned} &g\_{00} = \pm1\\\\ &g\_{11} = g\_{22}=g\_{33}=\mp1\\\\ &g\_{ij}=0\, (i\ne j) \end{aligned}$

一般有两种惯例： $(+,-,-,-)$ 和 $(-,+,+,+)$ ，前者对应 $g\_{00}=1$ ，后者对应 $g\_{00}=-1$ 。

**1.2.4 微分形式**

微分形式可以看做是协变反对称张量场。反对称的意思就是，交换下标会改变符号： $\omega\_{\mu \nu} = -\omega\_{\nu\mu}$ 。

例如，二阶反对称协变张量场 $\omega\_{\mu\nu}$ 是 2-形式。

特别地，协变矢量场 $\omega\_\mu$ 是 1-形式，标量场是 0-形式。

两个 1-形式通过 wedge product 可以得到 2-形式：

$\omega = \alpha \wedge \beta = \alpha\_\mu \beta\_\nu\mathrm{d}x^\mu \wedge  \mathrm{d}x^\nu $

其中 $\mathrm{d}x^\mu \wedge  \mathrm{d}x^\nu  = -\mathrm{d}x^\nu \wedge  \mathrm{d}x^\mu$

以此类推。

**1.2.5 外微分**

定义外微分运算 $\mathrm{d}$ ，它将 n-形式变为 (n+1)-形式：

$\begin{aligned} \mathrm{d} \omega &= \mathrm{d}(\omega\_\mu \mathrm{d}x^\mu)\ \\\\  &= \mathrm{d}(\omega\_\mu) \wedge \mathrm{d}x^\mu\\\\ &=  (\partial\_\nu \omega\_\mu\mathrm{d}x^\nu)\wedge\mathrm{d}x^\mu  \end{aligned}$

一句话概括，外微分运算就是对每个基上的分量取全微分再 wedge 上对应的基。

特别地，对 0-形式做外微分运算，其实就是标量场的全微分本身： $\mathrm{d}f = (\partial\_\mu f) \mathrm{d}x^\mu$ 。

外微分运算是典范的：它不需要借助流形上的额外结构，也不依赖于基的定义。

引理： $\alpha \wedge \beta = (-1)^{\deg(\alpha)\deg(\beta)} \beta\wedge \alpha$ ，其中 $\deg$ 表示微分形式的阶数。

> 证明：为了将 $\beta$ 移动到 $\alpha$ 前面，需要将 $\beta$ 中的 $\deg(\beta)$ 个 1-形式 向前移动 $\deg(\alpha)$ 次，共 $\deg(\alpha) \deg(\beta)$ 次，每次积累一个负号。

定理：做两次外微分运算总是会得到零： $\mathrm{d}\mathrm{d}=0$ ，证明略。

**1.2.6 Hodge 对偶**

关于 Hodge 对偶，有兴趣的读者可以自行查阅，这里就不详细介绍了。简单来说，k-形式 的 Hodge 对偶是与其“互补”的 (n-k)-形式。例如，在欧式空间 $\mathbb{R}^3$ 中，给定标准正交基 $\mathrm{d}x,\mathrm{d}y,\mathrm{d}z$ ，有

$\begin{aligned} \star (1) &=\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z, \quad\star(\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z)= 1\\\\ \star \mathrm{d}x &= \mathrm{d}y \wedge \mathrm{d}z , \quad\star(\mathrm{d}y \wedge \mathrm{d}z) = \mathrm{d}x\\\\ \star\mathrm{d}y&=\mathrm{d}z\wedge \mathrm{d}x, \quad\star(\mathrm{d}z\wedge\mathrm{d}x) = \mathrm{d}y \\\\ \star \mathrm{d}z&=\mathrm{d}x\wedge \mathrm{d}y, \quad\star(\mathrm{d}x\wedge\mathrm{d}y)=\mathrm{d}z \end{aligned}$

在这个例子中，做两次 Hodge 对偶会返回自身： $\star\star = \operatorname{id}$ 。但一般来说，并非总是如此。例如在闵氏时空中：

$\star(\mathrm{d}t \wedge\mathrm{d}x) = -(\mathrm{d}y \wedge \mathrm{d}z),\quad \star(\mathrm{d}y \wedge \mathrm{d}z) = \mathrm{d}t \wedge\mathrm{d}x$

$\star\mathrm{d}t = -\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z, \quad \star(\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z) = -\mathrm{d}t$

实际上，在闵氏时空中，对于偶数阶形式， $\star\star = -\operatorname{id}$ 。对于奇数阶形式， $\star\star = \operatorname{id}$ 。

对于一般的情形，见附录引理 3。

## 二、4-势、4-流、场强张量  

4-势（4-potential）定义为 $A^\mu = (A^0, A^1, A^2, A^3) = (\phi/c, A^x,A^y,A^z)$

> 用更严谨的微分几何语言，就是 $A = A^0\partial\_0 + A^1 \partial\_1 + A^2 \partial\_2 + A^3 \partial\_3 = \frac{\phi}{c} \partial\_{(ct)} + A^x\partial\_x + A^y \partial\_y + A^z\partial\_z$   
> 这是一个切矢量场，基为 $(\partial\_0, \partial\_1,\partial\_2,\partial\_3)$

由于只有协变矢量有自然的外微分运算，我们用度规将 4-势变为协变形式：

$A\_{\mu}=g\_{\mu\nu}A^{\nu}$

以下采用 $(-,+,+,+)$ 的度规惯例，于是：

$A\_\mu = (A\_0, A\_1, A\_2, A\_3) = (-\phi/c, A\_x, A\_y, A\_z)$

也就是

$\begin{aligned} A &= A\_0 \mathrm{d}x^0 + A\_1\mathrm{d}x^1 + A\_2\mathrm{d}x^2 + A\_3\mathrm{d}x^3 \\\\&= -\phi/c \mathrm{d}(ct) +A^x\mathrm{d}x + A^y\mathrm{d}y + A^z\mathrm{d}z \\\\&=  -\phi \mathrm{d}t +A^x\mathrm{d}x +A^y\mathrm{d}y +A^z\mathrm{d}z  \end{aligned}$

对协变 4-势 $A$ 做外微分运算得到场强张量 $F$ ：

$\begin{aligned} F &= \mathrm{d}A \\\\ &= \mathrm{d} (-\phi \mathrm{d}t +A^x\mathrm{d}x +A^y\mathrm{d}y +A^z\mathrm{d}z) \\\\ &=(\partial\_x \phi + \partial\_t \mathrm A^x) \,\mathrm{d}t \wedge \mathrm{d}x \\\\ &+ (\partial\_y \phi + \partial\_t A^y) \,\mathrm{d}t\wedge \mathrm{d}y \\\\ &+ (\partial\_z\phi + \partial\_t A^z)\,\mathrm{d}t \wedge \mathrm{d}z \\\\ &+ (\partial\_y A^z - \partial\_z A^y) \mathrm{d}y \wedge \mathrm{d}z \\\\ & +(\partial\_z A^x - \partial\_x A^z)\mathrm{d}z \wedge \mathrm{d}x \\\\ & +(\partial\_x A^y - \partial\_y A^x)\mathrm{d}x \wedge \mathrm{d}y \\\\ &= -E^x \mathrm{d}t \wedge \mathrm{d}x - E^y \mathrm{d}t \wedge \mathrm{d}y - E^z \mathrm{d}t \wedge \mathrm{d}z \\\\ & + B^x \mathrm{d}y \wedge \mathrm{d}z + B^y \mathrm{d}z \wedge \mathrm{d}x + B^z \mathrm{d}x \wedge \mathrm{d}y \end{aligned}$

也可以写成矩阵形式：

$\begin{bmatrix} 0 & E^x & E^y & E^z \\\\ -E^x & 0 & -B^z & B^y \\\\ -E^y & B^z & 0 & -B^x \\\\ -E^z & -B^y & B^x & 0 \end{bmatrix}$

为了保持量纲一致，我们将 $c$ 吸收进 $\mathrm{d}t$ ，于是

$\color{red}{F\_{\mu\nu}=\begin{bmatrix} 0 & E^x/c & E^y/c & E^z /c\\\\ -E^x/c & 0 & -B\_z & B^y \\\\ -E^y/c & B^z & 0 & -B^x \\\\ -E^z /c& -B^y & B^x & 0 \end{bmatrix}}$

注意这里的第一个指标 $\mu$ 不是代表行，而是代表列，第二个指标 $ \nu$ 代表行。

实际上， $\color{red}{F\_{\mu\nu} = \partial\_\mu A\_\nu - \partial\_\nu A\_\mu}$ ，请读者自行根据定义 $F=\mathrm{d}A$ 推导。

$F\_{\mu\nu}$ 的逆变形式为 $F^{\mu\nu} = g^{\mu \rho} g^{\nu \sigma} F\_{\rho \sigma}$ ：

$F^{\mu\nu} = \begin{bmatrix} 0 & -E^x/c & -E^y/c & -E^z /c\\\\ E^x/c & 0 & -B\_z & B^y \\\\ E^y/c & B^z & 0 & -B^x \\\\ E^z /c& -B^y & B^x & 0 \end{bmatrix}$

最后，4-流（4-current）定义为 $J^{\mu}=(\rho c, J^x,J^y,J^z)$ ，协变形式为 $J\_{\mu}=(-\rho c, J^x, J^y, J^z) = -\rho c^2 \mathrm{d}t +J^x \mathrm{d}x + J^y \mathrm{d}y + J^z \mathrm{d}z$ 。

> 实际上，4-势是主丛上的一个联络。所谓主丛，就是一个纤维丛，其纤维有李群的结构，而向量丛（例如切丛/余切丛）的纤维是向量空间（例如切空间/余切空间）。可见主丛不同于向量丛。  
>   
> 主丛上的联络的定义与向量丛上的联络的定义也是不同的。向量丛上的联络定义为协变导数，而主丛上的联络是一个取值为李代数的 1-形式。对于电磁场而言，主丛的纤维是 $U(1)$ ，其李代数为 $\mathbb{R}$ ，因此看起来与普通的 1-形式没有区别。详情我们在本系列下一篇文章中介绍。

## 三、电磁场的拉氏量  

这里直接给出拉氏量：

$\color{red}{ \begin{aligned} \mathcal{L}[A\_\mu, \partial\_\nu A\_\mu] =  -\frac{1}{4\mu\_0} F\_{\mu\nu} F^{\mu\nu} + A\_{\mu} J^{\mu} \end{aligned} }$

注意，如果选择另一种度规 $(+,-,-,-)$ ，则上式第二项应为负。

如果展开来计算，会发现它等于：

$\color{red}{\mathcal{L} = \frac{1}{2}\left(\epsilon\_0\mathbf{E^2} -\frac{1}{\mu\_0} \mathbf{B^2}\right) -\rho\phi + \mathbf{A} \cdot \mathbf{J}}$

至于为什么拉氏量是这个样子，这里就不深究了。

## 四、麦克斯韦方程  

使用第一节介绍的场变分法，有：

$\begin{aligned} \frac{\partial \mathcal{L}}{\partial A\_\nu} -\partial\_\mu \frac{\partial \mathcal{L}}{\partial(\partial\_\mu A\_\nu)} = 0 \end{aligned}$

其中

$\begin{aligned} \frac{\partial \mathcal{L}}{\partial A\_\mu} = -J\_\mu \end{aligned}$

$\begin{aligned} \frac{\partial \mathcal{L}}{\partial(\partial\_\mu A\_\nu)} &= -\frac{\partial }{\partial(\partial\_\mu A\_\nu)} \left[\frac{1}{4\mu\_0} F\_{ab} F^{ab} \right]\\\\ &= -\frac{1}{4\mu\_0}\left[\frac{\partial F\_{ab}}{\partial(\partial\_\mu A\_\nu)} F^{ab} + F\_{ab}\frac{\partial F^{ab}}{\partial(\partial\_\mu A\_\nu)} \right] \\\\ &= -\frac{1}{4\mu\_0}\left[\frac{\partial F\_{ab}}{\partial(\partial\_\mu A\_\nu)} F^{ab} + g\_{ai}g\_{bj}F^{ij}\frac{\partial (g^{ak}g^{bl}F\_{kl})}{\partial(\partial\_\mu A\_\nu)} \right] \\\\ &= -\frac{1}{4\mu\_0}\left[\frac{\partial F\_{ab}}{\partial(\partial\_\mu A\_\nu)} F^{ab} + \delta\_{ki}\delta\_{lj}F^{ij}\frac{\partial F\_{kl}}{\partial(\partial\_\mu A\_\nu)} \right] \\\\ &= -\frac{1}{4\mu\_0}\left[\frac{\partial F\_{ab}}{\partial(\partial\_\mu A\_\nu)} F^{ab} + F^{ij}\frac{\partial F\_{ij}}{\partial(\partial\_\mu A\_\nu)} \right] \\\\ &= -\frac{1}{2\mu\_0}\left[\frac{\partial F\_{ab}}{\partial(\partial\_\mu A\_\nu)} F^{ab}  \right] \\\\ &= -\frac{1}{2\mu\_0}\left[\frac{\partial(\partial\_a A\_b - \partial\_b A\_a)}{\partial(\partial\_\mu A\_\nu)} F^{ab}  \right] \\\\ &= -\frac{1}{2\mu\_0}\left[(\delta^\mu\_a\delta^\nu\_b - \delta^\mu\_b\delta^\nu\_a  ) F^{ab}  \right]  \\\\  &= -\frac{1}{2\mu\_0} \left( F^{\mu\nu}-F^{\nu\mu} \right) \\\\ &=-\frac{1}{\mu\_0}F^{\mu\nu} \end{aligned}$

因此有

$\begin{aligned} \color{red}{\partial\_\mu F^{\mu\nu} = \mu\_0 J^{\nu}} \end{aligned}$

这就是麦克斯韦方程。

接下来我们将它转写成我们熟悉的形式。把

$F^{\mu\nu} = \begin{bmatrix} 0 & -E^x/c & -E^y/c & -E^z /c\\\\ E^x/c & 0 & -B\_z & B^y \\\\ E^y/c & B^z & 0 & -B^x \\\\ E^z /c& -B^y & B^x & 0 \end{bmatrix}$

和

$J^{\mu} = (\rho c^2, J^x,J^y,J^z)$

代入 $\begin{aligned} \partial\_\mu F^{\mu\nu} = \mu\_0 J^{\nu} \end{aligned}$ 得：

$\begin{aligned} \frac{\partial\_i E^i}{c} = \mu\_0 \rho c \\\\ \Rightarrow \color{red}{ \nabla \cdot \mathbf{E} =\frac{\rho}{\epsilon\_0} }\end{aligned}$

以及

$\begin{aligned} \varepsilon^{ij}\_{k} \partial\_{j}B^k - \frac{\partial}{\partial(ct)}E^i/c = \mu\_0J^i\\\\  \color{red}{ \Rightarrow \nabla \times \mathbf{B} = \mu\_0 (\mathbf{J}+ \epsilon\_0 \partial\_t \mathbf{E})} \end{aligned}$

这就是有源麦克斯韦方程。

但是另外两个无源方程（$\color{red}{ \nabla \cdot\mathbf{B}=0}$ 和 $\color{red}{ \nabla \times \mathbf{E} = -\partial\_t \mathbf{B}}$ ）去哪了？

实际上，这两个无源方程不是电磁场动力学的一部分，而是电磁场自身结构的一部分。这是因为无源方程是由 $\mathrm{d}F=0$ 得到的，而 $\mathrm{d} F=0$ 是由 $F = \mathrm{d} A$ 得到的（对任何微分形式做两次外微分都会得到零）。而 $F=\mathrm{d}A$ 本身就是场强张量的定义。可见，无源方程是根据电磁场的定义得来的，属于自身结构的一部分。

无源方程可以写成：

$\color{red}{\partial\_\mu (\star F)^{\mu\nu} = 0}$

其中 $(\star F)^{\mu\nu}$ 是 $F^{\mu\nu}$ 的 Hodge 对偶：

$\color{red}{(\star F)^{\mu\nu} = \begin{bmatrix} 0 & -B^x & -B^y & -B^z \\\\ B^x & 0 & E^z/c & -E^y/c \\\\ B^y & -E^z/c & 0 & E^x/c \\\\ B^z /c& E^y/c & -E^x/c & 0 \end{bmatrix}}$

请读者从 $\mathrm{d} F=0$ 推导无源方程。

> 如果读者会微分几何，以下提供一个更优雅的推导：  
>  $\begin{aligned} &\mathrm{d}F=0 \\\\ &\Rightarrow \mathrm{d} \star \star F = 0 \\\\ &\Rightarrow \mathrm{d} \star \flat\sharp\star F = 0 \\\\ &\Rightarrow (\sharp\star\mathrm{d} \star \flat)(\sharp\star F) = 0 \\\\ &\Rightarrow (\nabla\cdot)(\sharp\star F) = 0 \\\\ &\Rightarrow \partial\_\mu (\star F)^{\mu\nu} = 0 \end{aligned}$   
> 其中 $\sharp$ 是升指标， $\flat$ 是降指标， $(\nabla\cdot)$ 是广义散度，定义为 $(\nabla\cdot) = \sharp\star\mathrm{d} \star \flat$ 。

## 五、微分几何表述  

有些读者不喜欢指标运算，而是喜欢更典范的抽象符号，因此本节用微分几何的语言再重写一遍。

给定拉氏量：

$\begin{aligned} \mathcal{L} &= -\frac{1}{2\mu\_0} F \wedge (\star F) + A\wedge (\star J) \\\\ &= \left[-\frac{1}{2\mu\_0} \langle F , F\rangle + \langle A , J \rangle\right] \omega  \end{aligned}$

注意，如果采用 $(+,-,-,-)$ 度规，则上式第二项应为 $-\langle A, J\rangle \omega$ 。

其中度规体积形式 $\omega$ 的定义是使得 $\langle \omega ,\omega \rangle\_g = \pm 1 =: \operatorname{sgn}(g)$ 成立的 n-形式，n 为流形的维数。显式定义为 $\omega = \sqrt{|\det(g)|}\,\mathrm{d}x^0 \wedge \mathrm{d}x^1 \wedge \mathrm{d}x^2 \wedge \mathrm{d}x^3 = \mathrm{d}x^0 \wedge \mathrm{d}x^1 \wedge \mathrm{d}x^2 \wedge \mathrm{d}x^3$ 。

> 微分形式 $\beta$ 的 Hodge 对偶 $\star \beta$ 的定义式为 $\alpha \wedge \*\beta = \langle \alpha, \beta\rangle \omega$ 。其中 $\langle \cdot,\cdot\rangle$ 是微分形式的内积，对于 n-形式，内积的定义为：  
>  $\langle \alpha\_1,\cdots\wedge\alpha\_n,\,\beta\_1\wedge\cdots\wedge\beta\_n\rangle = \begin{vmatrix} \langle \alpha\_1,\beta\_1 \rangle & \cdots & \langle \alpha\_1,\beta\_n \rangle \\\\ \vdots & \ddots & \vdots \\\\ \langle \alpha\_n ,\beta\_1 \rangle  & \cdots & \langle\alpha\_n ,\beta\_n \rangle  \end{vmatrix}$

注意此处系数是 $-1/(2\mu\_0)$ 而非 $-1/(4\mu\_0)$ 。这是因为之前的张量指标写法（ $F\_{\mu\nu}F^{\mu\nu}$ ）导致交换 $\mu, \nu$ 会重复求和，所以之前要多除以一个 $1/2$ 。

从 $\mathcal{L}$ 的形式可以看出，它其实是一个 4-形式，而不是一个标量场。这是因为它要被积分成为作用量 $\begin{aligned} S = \int \mathcal{L} \end{aligned}$ 。

对作用量变分得到：

$\begin{aligned} \delta S&\stackrel{1}{=}\int \delta \mathcal{L} \\\\ &\stackrel{2}=\int -\frac{1}{2\mu\_0} [(\delta F) \wedge (\star F) +F\wedge(\delta\star F)] + (\delta A)\wedge (\star J) \\\\ &\color{blue}{\stackrel{3}{=}}\int -\frac{1}{2\mu\_0} [(\delta F) \wedge (\star F)+(\star \delta F)\wedge F] + (\delta A)\wedge (\star J) \\\\ & \color{blue}{\stackrel{4}=} \int -\frac{1}{2\mu\_0} [(\delta F) \wedge (\star F)+(\delta F)\wedge (\star F)] + (\delta A)\wedge (\star J) \\\\ &\stackrel{5}=\int -\frac{1}{\mu\_0} (\delta F) \wedge (\star F) + (\delta A)\wedge (\star J) \\\\ &\stackrel{6}= \int -\frac{1}{\mu\_0} (\delta \mathrm{d}A) \wedge (\star F) + (\delta A)\wedge (\star J) \\\\ &\stackrel{7}= \int -\frac{1}{\mu\_0} \mathrm{d}(\delta A) \wedge (\star F) + (\delta A)\wedge (\star J) \\\\ &\color{blue}{\stackrel{8}=} \int -\frac{1}{\mu\_0} (\delta A) \wedge (\mathrm{d}\star F) + (\delta A)\wedge (\star J) \\\\ &\stackrel{9}= \int  (\delta A) \wedge \left(-\frac{1}{\mu\_0}\mathrm{d}\star F + \star J\right) \end{aligned}$

其中第 3 个等号用到了：

$\begin{aligned} \alpha\wedge\beta &= (-1)^{\deg(\alpha)\deg(\beta)}\end{aligned} \beta \wedge \alpha$

其中 $\deg(\alpha)$ 代表 $\alpha$ 的阶数，例如此处 $\deg(F)=2$ ，因为 $F$ 是 2-form。

第 4 个等号用到了：

$\begin{aligned} \star \alpha\wedge\beta &= (-1)^{\deg(\star\alpha)\deg(\beta)}\beta\wedge\star\alpha \\\\ &= (-1)^{\deg(\star\alpha)\deg(\beta)}\langle\beta,\alpha\rangle \omega \\\\ &= (-1)^{\deg(\star\alpha)\deg(\beta)}\langle\alpha,\beta\rangle \omega \\\\ &= (-1)^{\deg(\star\alpha)\deg(\beta)}\alpha \wedge\star\beta \end{aligned}$

第 8 个等号用到了分部积分：

$\begin{aligned} \int (\mathrm{d}\alpha) \wedge \beta &= \int \left[\cancel{\mathrm{d}(\alpha \wedge \beta)} - (-1)^{\text{deg}(\alpha)} \alpha \wedge \mathrm{d}\beta\right]\end{aligned}$

之所以 $\int\_M\mathrm{d}(\alpha \wedge \beta) = 0$ ，是因为根据斯托克斯定理（Stoke's theorem）， $\int\_M\mathrm{d}(\alpha \wedge \beta)=\int\_{\partial M} \alpha \wedge \beta$ ，其中 $\partial M$ 是 $M$ 的边界。而 $\int\_{\partial M} \alpha \wedge \beta =0$ （变分法的边界条件为 $\delta A|\_{\partial M}=0$ ）。

由于 $\delta S =0$ 对任意 $\delta A$ 成立，于是有 $-\frac{1}{\mu\_0}\mathrm{d}\star F + \star J = 0$ ，即麦克斯韦方程：

$\color{red}{\mathrm{d}\star F =\mu\_0 \star J}$

写成这样有什么好处？答案是它很容易被推广到弯曲时空。从平直时空到弯曲时空，我们只需要替换度规即可，这在上式中反映为替换 Hodge 星算子，因为 Hodge 星算子是依赖度规定义的。

## 六、协变/逆变形式的对比  

最后，我们对比一下指标写法和微分形式写法：

（逆变）指标写法：

$\begin{aligned} \partial\_\mu (\star{F})^{\mu \nu}&= 0 \\\\ \partial\_\mu F^{\mu\nu}&= \mu\_0 J^\nu  \end{aligned}$

（协变）微分形式写法：

$\begin{aligned} \mathrm{d} F&=0 \\\\ \mathrm{d} \star F &= \mu\_0 \star J \end{aligned}$

指标写法中的 $F$ ，到了微分形式写法中却变成了对偶 $(\star F)$ ，反之亦然。这是因为指标写法中的 $F^{\mu\nu}$ 是逆变张量，而微分形式 $F$ 是协变张量。根据 $(\nabla\cdot) \sharp = \sharp\star\mathrm{d} \star $ ，有 $\partial\_\mu F^{\mu\nu} = \sharp\star \mathrm{d} \star F$ 。见下图：

$\begin{matrix} k\text{-vector fields} & \stackrel{(\nabla\cdot)}{\longrightarrow}  & (k-1)\text{-vector fields}\\\\ \uparrow\sharp & & \uparrow\sharp \\\\  k\text{-form}  & & (k-1)\text{-form}\\\\ \downarrow\star &  & \uparrow \star \\\\ (n-k)\text{-form} &  \stackrel{\mathrm{d}}\longrightarrow  & (n-k+1)\text{-form} \end{matrix}$

> 或者也可以使用更常见的 co-differential $\mathrm{d}^\dagger$ ，它的定义式为 $\langle \alpha, \mathrm{d}\beta\rangle = \langle \mathrm{d}^\dagger\alpha, \beta\rangle$ 。  
>   
> 可以证明（见附录）， $\mathrm{d}^\dagger \alpha = (-1)^{k}\star^{-1} \mathrm{d} \star \alpha = (-1)^{nk+n+1} s\star \mathrm{d} \star \alpha$ ，其中 $k=\deg(\alpha)$ ， $s=\operatorname{sgn}(g) := \operatorname{sgn}(\det (g))$ 是度规的符号。  
>   
> 对于闵氏度规， $s = -1$ 。代入 $s=-1,\,n=4,\,k=2$ 得 $\mathrm{d}^\dagger F=\star \mathrm{d}\star F$ 。  
>   
> 所以上图可以画成：  
>  $\begin{matrix} 2\text{-vector fields} & \stackrel{(\nabla\cdot)}{\longrightarrow}  & 1\text{-vector fields}\\\\ \uparrow\sharp & & \uparrow\sharp \\\\  2\text{-form}  & \xrightarrow{\mathrm{d}^\dagger} & 1\text{-form}\\\\ \downarrow\star &  & \uparrow \star \\\\ 2\text{-form} &  \stackrel{\mathrm{d}}\longrightarrow  & 3\text{-form} \end{matrix}$

于是有

$\begin{matrix} F^{\mu\nu} & \xrightarrow{(\nabla\cdot)} & \partial\_\mu F^{\mu\nu}=\mu\_0J^\nu \\\\ \uparrow \sharp & & \uparrow \sharp \\\\ F & \xrightarrow{\star \mathrm{d}\star} & \star \mathrm{d} \star F \end{matrix}$

可见 $\partial\_\mu F^{\mu\nu}=\mu\_0J^\nu$ 等价于 $\star \mathrm{d} \star F = \mu\_0 J$ 。

而对于 1-形式， 有$\star\star = (-1)^{k(n-k)+s} \operatorname{id} = (-1)^{1(4-1)+1} \operatorname{id} = \operatorname{id}$ 。所以 $\star \mathrm{d} \star F = \mu\_0 J$ 等价于 $\mathrm{d} \star F = \mu\_0 \star J$ 。

对于 $\mathrm{d} F = 0  \Leftrightarrow \partial\_\mu (\star F)^{\mu\nu} = 0$ 的推导也是类似的。

## 七、附录  

引理 1： $\mathrm{d}(\alpha \wedge \beta) = \mathrm{d}\alpha \wedge \beta + (-1)^{\deg(\alpha)} \alpha \wedge \mathrm{d}\beta$

> 证明：  
> 记  
>  $\begin{aligned} \alpha \wedge \beta &= \sum\_{I,J} a\_I b\_J\mathrm{d} x^I \wedge \mathrm{d}x^J \\\\ &= \sum\_{i\_1,\cdots,i\_{m},j\_1,\cdots,j\_n} a\_{i\_1,\cdots,i\_{m}}b\_{j\_1,\cdots,j\_n}\mathrm{d}x^{i\_1} \wedge \cdots \wedge \mathrm{d}x^{i\_m} \wedge \mathrm{d}x^j\_1\wedge \cdots \wedge \mathrm{d}x^{j\_n} \end{aligned}$   
> 则  
>  $\begin{aligned} \mathrm{d}(\alpha\wedge \beta) &= \partial\_i (a\_I b\_J) \mathrm{d}x^i\wedge \mathrm{d}x^I \wedge \mathrm{d}x^J \\\\ &=[(\partial\_i a\_I)b\_J \mathrm{d}x^i \wedge \mathrm{d}x^I] \wedge \mathrm{d}x^J + a\_I\partial\_i b\_J \mathrm{d}x^i \wedge \mathrm{d}x^I \wedge \mathrm{d}x^J \\\\ &=(\partial\_i a\_I\mathrm{d}x^i \wedge \mathrm{d}x^I) \wedge (b\_J \mathrm{d}x^J) + (-1)^{\deg(\alpha)} (a\_I\partial\_i  \mathrm{d}x^I \wedge \mathrm{d}x^i) \wedge (b\_J\mathrm{d}x^J) \\\\ &=\mathrm{d}\alpha \wedge \beta + (-1)^{\deg(\alpha)} \alpha \wedge \mathrm{d}\beta \end{aligned}$

引理 2：当 $\deg(\alpha)=\deg(\beta)$ 时，有 $\star\alpha \wedge \beta = (-1)^{k(n-k)}\alpha\wedge \star\beta$ ，其中 $k=\deg(\alpha)$

> 证明：  
>  $\begin{aligned} \star \alpha\wedge\beta &= (-1)^{\deg(\star\alpha)\deg(\beta)} \beta\wedge\star\alpha \\\\  &= (-1)^{k(n-k)}\langle\beta,\alpha\rangle \omega \\\\  &= (-1)^{k(n-k)}\langle\alpha,\beta\rangle \omega \\\\  &= (-1)^{k(n-k)}\alpha \wedge\star\beta \end{aligned}$

引理 3： $\star\star \alpha = (-1)^{k(n-k)}s \alpha$ ，其中 $k=\deg(\alpha)$ ， $s=\operatorname{sgn}(g)$ 。

> 证明：  
>  $\begin{aligned} \star\alpha \wedge \star\star \alpha &= \langle \star\alpha, \star\alpha \rangle\omega \\\\ &= s\langle \alpha,\alpha \rangle\omega \\\\ &= s\alpha \wedge \star \alpha\\\\ &= (-1)^{k(n-k)}s \star\alpha\wedge \alpha \\\\ &= \star\alpha\wedge \left[(-1)^{k(n-k)}s  \alpha\right] \end{aligned}$

引理 4： $\mathrm{d}^\dagger \alpha = (-1)^{k}\star^{-1} \mathrm{d} \star \alpha$

> 证明：  
>  $\begin{aligned} \langle \beta,\mathrm{d}^\dagger \alpha\rangle&= \langle \mathrm{d}\beta , \alpha\rangle \\\\ &= \int\mathrm{d}\beta \wedge \star \alpha \\\\ &= \int -(-1)^{\deg(\beta)} \beta \wedge \mathrm{d}\star \alpha \\\\ &= \int (-1)^{\deg(\beta)+1} \beta \wedge \mathrm{d}\star \alpha \\\\ &= \int (-1)^{\deg(\alpha)} \beta \wedge \mathrm{d}\star \alpha \\\\ &= \int (-1)^{\deg(\alpha)} \beta \wedge \star (\star^{-1}\mathrm{d}\star \alpha) \\\\ &= (-1)^{k} \langle\beta, \star^{-1}\mathrm{d} \star \alpha \rangle \end{aligned}$

引理 5： $\mathrm{d}^\dagger \alpha  = (-1)^{nk+n+1} s\star \mathrm{d} \star \alpha$

> 证明：  
> 结合引理 3 和引理 4 即可证得。