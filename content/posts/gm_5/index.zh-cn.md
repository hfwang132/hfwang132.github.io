---
title: "从量子场论到腔量子电动力学【更高更妙的电动力学·5】"
date: 2025-04-06T01:14:26+08:00
draft: false
categories: ["数学物理方法"]
tags: ["量子场论", "腔量子电动力学", "电动力学", "Jaynes-Cummings"]
---


在本篇文章中，我们将从非常复杂的 QED 拉氏量出发：

$\begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial\_\mu -m)\psi - eA\_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F\_{\mu\nu} F^{\mu\nu} \end{aligned} $

这个拉氏量非常复杂：它不仅考虑了电子的反粒子——正电子，并且耦合项 $- eA\_\mu \bar{\psi} \gamma^\mu \psi$ 还是一个三次项，可以描述电子-正电子对产生/湮灭等多种过程。它没有解析解，只能用量子场论的微扰法求解。

但经过一系列简化和近似（低能近似、玻恩-奥本海默近似，长波/偶极子近似、二能级近似、旋转波近似）之后，我们竟然得到了一个有解析解的模型：

$H =  \frac{\omega\_{ab}}{2} \sigma\_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger) $

这就是腔量子电动力学的经典哈密顿量：Jaynes-Cummings 哈密顿量。这是如何做到的？且看下文分解。

---

## 一、电磁场的哈密顿表述  
### 1.1 电磁场的哈密顿量  

我们先来试试直接使用勒让德变换：

$\mathcal{H} = \Pi^i  \dot{A}\_i - \mathcal{L}$

其中 $\Pi^i = \frac{\partial \mathcal{L}}{\partial \dot{ A}\_i}$ 是 $\mathbf{A}$ 对应的正则动量。

我们希望从八个哈密顿方程中得到麦克斯韦方程：

$\boxed{ \dot{A}\_i = \frac{\delta \mathcal{H}}{\delta \Pi^i},\quad \dot{\Pi}^i = \frac{\delta \mathcal{H}}{\delta A\_i} }$

其中符号 $\delta$ 是变分。

但是事情没有这么简单。注意到正则动量 $\Pi^0 = \frac{\partial \mathcal{L}}{\partial \dot{\phi}} = 0$ 恒等于零！这说明它是一个约束。

于是

$\mathcal{H} = \mathbf{\Pi} \cdot \dot{\mathbf{A}} - \mathcal{L}$

其中 $\mathbf{\Pi}=\frac{\partial \mathcal{L}}{\partial \dot{\mathbf{A}}} = \dot{\mathbf{A}} + \nabla \phi = -\mathbf{E}$ 是 $\mathbf{A}$ 对应的正则动量。

于是

$\begin{aligned} \mathcal{H} &= (\dot{\mathbf{A}} + \nabla \phi) \cdot \dot{\mathbf{A}} - \left[\frac{1}{2}(\dot{\mathbf{A}}+\nabla \phi)^2 -\frac{1}{2} (\nabla \times \mathbf{A})^2 - \rho \phi + \mathbf{A}\cdot \mathbf{J} \right]  \\\\ &= \frac{1}{2}\mathbf{\Pi}^2 - \mathbf{\Pi} \cdot \nabla \phi + \frac{1}{2} (\nabla \times \mathbf{A})^2 + \rho \phi - \mathbf{A}\cdot \mathbf{J}  \end{aligned}$

变分时利用分部积分，可以将 $- \mathbf{\Pi} \cdot \nabla \phi $ 转化为 $+\phi \nabla \cdot \mathbf{\Pi}$ 。于是：

$\boxed{ \begin{aligned}  \mathcal{H}=\frac{1}{2}\mathbf{\Pi}^2   + \frac{1}{2} (\nabla \times \mathbf{A})^2 - \mathbf{A}\cdot \mathbf{J}+ \phi(\rho +\nabla\cdot \mathbf{\Pi})    \end{aligned} }$

### 1.2 电磁场的正则方程  

现在我们考虑哈密顿方程 $\dot{\Pi}^0 = -\frac{\delta \mathcal{H}}{\delta A\_0} $ 。既然 $\Pi^0$ 恒为零，那么 $\dot{\Pi}^0$ 也应当恒为零，于是根据哈密顿方程有：

$\dot{\Pi}\_0 = -\frac{\delta \mathcal{H}}{\delta A\_0} = -\frac{\delta \mathcal{H}}{\delta \phi} = \rho + \nabla \cdot \mathbf{\Pi} = 0\Rightarrow  \boxed{\nabla\cdot \mathbf{E} = \rho}$

这正是高斯定律。在哈密顿表述中，它是作为约束出现的。而 $\phi$ 就是对应的拉格朗日乘子。

这说明在哈密顿表述中， $\phi$ 不是一个独立的动力学变量。我们不妨取 $\phi =0$ ，这叫做 Weyl 规范。

> Weyl 规范是一个不完全的规范，因为剩下的 $A\_1,A\_2,A\_3$ 仍有规范自由度。

当然，我们也可以取其他规范。例如库仑规范 $\nabla \cdot \mathbf{A} = 0$ ，那么此时 $\phi$ 就依赖于 $\mathbf{A}$ （根据规范变换）。

把约束 $ \rho + \nabla \cdot \mathbf{\Pi} = 0$ 代入 $\mathcal{H}$ 得：

$\boxed{ \begin{aligned} \mathcal{H} &= \frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 - \mathbf{A}\cdot \mathbf{J}\\\\ &= \frac{1}{2}\mathbf{E}^2  + \frac{1}{2} \mathbf{B}^2  - \mathbf{A}\cdot \mathbf{J}   \end{aligned} }$

> 注意到哈密顿量中并没有势能项 $\rho \phi$ ，这与哈密顿量不满足规范不变性有关，见第二节末。  
>   
> 我们来看看为什么哈密顿量不具有规范不变性：  
>   
> 在哈密顿表述中，场 $\varphi$ 的运动方程为 $\partial\_t \varphi = \delta \mathcal{H}/\delta \pi\_\varphi$ ，其中场 $\pi\_\varphi$ 是场 $\varphi$ 对应的正则动量。  
>   
> 注意到，运动方程左边的导数是 $\partial\_t$ ，而不是规范不变的协变导数 $D\_t = \partial\_t + \mathrm{i}eA\_t = \partial\_t -\mathrm{i}e\phi$ 。所以相应地，方程的右边也不是规范不变的。  
>   
> 这就是哈密顿表述在高能物理中不常用的原因之一。

最后，我们考虑剩下的哈密顿方程：

$\dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}},\quad \dot{\mathbf{\Pi}} = \frac{\delta \mathcal{H}}{\delta \mathbf{A}}$

其中前者 $\dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}} = \mathbf{\Pi} - \nabla\phi \Rightarrow \mathbf{E} = -\frac{\partial A}{\partial t} - \nabla \phi$ 是电场的定义式，后者则是安培定律：

$\begin{aligned} \dot{\mathbf{\Pi}} &= -\frac{\delta \mathcal{H}}{\delta \mathbf{A}} \\\\ &= -\frac{\delta }{\delta \mathbf{A}} \int\left[\frac{1}{2}(\nabla \times \mathbf{A})^2 - \mathbf{J} \cdot \mathbf{A}\right] \mathrm{d}^3 x  \\\\&= \int[-\nabla\times(\nabla\times \mathbf{A}) + \mathbf{J}]\mathrm{d}^3x \end{aligned}$

即

$\boxed{ \begin{aligned} &\dot{\mathbf{E}}=\nabla\times\mathbf{B} -\mathbf{J} \\\\ &\Rightarrow   \nabla\times \mathbf{B} = \mathbf{J} + \dot{\mathbf{E}} \end{aligned} }$

现在我们有了安培定律和高斯定律。但另外两个方程去哪了？实际上，与拉格朗日表述中的 $\mathrm{d}F=\mathrm{d}\mathrm{d}A=0$ 类似，在哈密顿表述中，另外两个无源方程也是定义的一部分。由 $\mathbf{B}:=\nabla\times \mathbf{A}$ 即可得到 $\nabla \cdot \mathbf{B}=0$ ；由 $\mathbf{E} := -\frac{\partial A}{\partial t} - \nabla \varphi$ 即可得到 $\nabla \times \mathbf{E} =-\dot{\mathbf{B}}$ 。

最后，我们来对比一下拉格朗日表述和哈密顿表述：

$\begin{matrix} \hline & \text{Lagrangian} & \text{Hamiltonian} \\\\ \hline \text{Field variables} & A\_\mu, \partial\_\mu A\_\nu & A\_\mu, \Pi^\mu \\\\ \hline \text{Eq. of motion} & \text{Euler-Lagrange equations} & \text{Hamiltonian equations} \\\\ & \partial\_\mu F^{\mu\nu}=J^\nu & \dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}},\quad \dot{\mathbf{\Pi}} = \frac{\delta \mathcal{H}}{\delta \mathbf{A}} \\\\ & \text{Ampere Law, Gauss Law} & \text{Ampere Law} \\\\ \hline \text{Constraints}  & \text{None} & \Pi^0=\dot{\Pi}^0=0\\\\ & & \text{Gauss Law} \\\\ \hline  \end{matrix}$

### 1.3Dirac-Bergmann 理论  

以上这一套处理有约束的哈密顿系统的理论，叫做 Dirac-Bergmann 理论。其中 $\Pi^0 = \frac{\partial \mathcal{L}}{\partial \dot{A\_0}} = 0$ 叫做 Primary constraint， $\dot{\Pi}^0=-\frac{\delta \mathcal{H}}{\delta A\_0} =0$ 叫做 Secondary constraint。在 D-B 理论中对这些约束有着更系统和更严格的处理。

### 1.4 为什么场论通常使用拉格朗日表述  

为什么电磁场的哈密顿表述如此不便？

这是因为在拉格朗日力学中，时间 $t=x^0$ 和空间坐标 $x^{1,2,3}$ 的地位是比较平等的，也很容易体现洛伦兹不变性。但在哈密顿力学中，时间 $t$ 拥有特殊地位，难以体现洛伦兹不变性。正是时间 $t=x^0$ 的特殊地位导致了场分量 $A\_0$ 及其对应正则动量 $\Pi^0$ 的约束。这也导致了**哈密顿量不具有规范不变性**。

在经典（低速）力学情况下，使用哈密顿力学比较方便。但在狭义相对论情形下，时间 $t$ 被提升为时空坐标 $x^0$ ，可以通过洛伦兹 boost 和其他空间坐标 $x^{1,2,3}$ 混合起来，此时哈密顿力学就显得尴尬了。

之所以在量子力学中我们可以经常使用哈密顿量（以及对应的海森堡/薛定谔表述），正是因为量子力学讨论的是低速情形。而如果进入狭义相对论的范畴，我们就不得不需要用到量子场论，并且使用拉格朗日量以及路径积分表述。

---

## 二、狄拉克场的哈密顿表述  

上面对电磁场 $A\_\mu$ 做的一切步骤都可以对狄拉克场 $\psi$ 做一遍。

从狄拉克场的拉格朗日量出发：

$\mathcal{L}=\bar{\psi}(\mathrm{i}\hbar c \gamma^\mu \partial\_\mu  -mc^2)\psi $

为了方便推导，我们采用自然单位制： $\hbar = c =1$ ，于是

$\mathcal{L}=\bar{\psi}(\mathrm{i}\gamma^\mu \partial\_\mu -m)\psi $

场变量为 $\psi, \bar{\psi}$ ，它们的正则动量为：

$\pi\_\psi = \frac{\partial\mathcal{L}}{\partial (\partial\_0\psi)} = \mathrm{i}\bar\psi \gamma^0 = \mathrm{i} \psi^\dagger$

$\pi\_\bar\psi = \frac{\partial\mathcal{L}}{\partial (\partial\_0\bar\psi)} = 0$ （Primary constraint）

勒让德变换：

$\begin{aligned} \mathcal{H} &= \pi\_\psi \partial\_0\psi + \pi\_{\bar\psi}\partial\_0\bar\psi - \mathcal{L} \\\\ &=\mathrm{i}\bar\psi \gamma^0 \partial\_0\psi-\bar{\psi}(\mathrm{i} \gamma^\mu \partial\_\mu  -m)\psi  \\\\ &= \bar{\psi}(-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi  \end{aligned}$

哈密顿方程：

$\begin{aligned} \partial\_0{\psi} &= \frac{\delta \mathcal{H}}{\delta\pi\_\psi}  \end{aligned}$

或

$\begin{aligned} \delta \mathcal{H} &= (\delta\pi\_\psi) \partial\_0{\psi} \\\\ &= \delta(\mathrm{i}\bar\psi \gamma^0 ) \partial\_0{\psi} \\\\ &= (\delta \bar\psi) \mathrm{i} \gamma^0  \partial\_0{\psi} \end{aligned}$

于是

$\begin{aligned} \mathrm{i} \gamma^0  \partial\_0{\psi} &= \frac{\delta \mathcal{H}}{\delta \bar\psi} \\\\ &= (-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi   \end{aligned}$

移项得：

$\boxed{ \mathrm{i} \gamma^\mu \partial\_\mu \psi - m\psi = 0 }$

这就是真空中的狄拉克方程。

如果电磁场不为零，即非真空，那么我们需要考虑电磁场和狄拉克场的总拉氏量：

$\boxed{ \begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial\_\mu -m)\psi - eA\_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F\_{\mu\nu} F^{\mu\nu} \end{aligned} }$

可以定义 $J^\mu = -e\bar\psi \gamma^\mu\psi$ （注意此处的 $e$ 是正数，而电子 $\psi$ 带负电），于是耦合项 $- eA\_\mu \bar{\psi} \gamma^\mu \psi $ 也可以写成 $+A\_\mu J^\mu$ ，与之前的定义吻合。

对这个拉格朗日量做勒让德变换得到：

$\boxed{ \begin{aligned} \mathcal{H} &= \frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 +  \bar{\psi}[-\mathrm{i}\bm\gamma\cdot (\nabla + \mathrm{i}e\mathbf{A} )+ m]\psi \\\\  &= \underbrace{\frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 }\_{\text{free photon field}} + \underbrace{\bar{\psi}(-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi }\_{\text{free Dirac field}} +\underbrace{e\bar\psi(\bm\gamma \cdot \mathbf{A})\psi}\_{\text{coupling}} \end{aligned} }$

求对应的哈密顿方程 $\dot{\mathbf{\Pi}} = \delta \mathcal{H}/\delta\mathbf{A}, \ \dot\psi =  \delta\mathcal{H}/\delta \pi\_\psi$ 就能得到耦合的麦克斯韦方程和狄拉克方程。

> 注意到，由于缺失了与时间 $t=x^0$ 有关的 $\bar\psi(-\mathrm{i}\gamma^0\partial\_0)\psi$ 项和 $e\bar\psi(\gamma^0A\_0)\psi=-e\psi^\dagger\psi \phi = \rho\phi$ 项，**哈密顿量不是规范不变的**。  
>   
> 原因我们已经说过：在哈密顿表述中，时间具有特殊地位；在哈密顿运动方程 $\partial\_0\varphi = \delta\mathcal{H}/\delta \pi\_\varphi$ 中，左边的时间导数 $\partial\_0$ 并非规范不变的（ $D\_0$ 才是规范不变的），所以右边哈密顿量显然也不是规范不变的。

## 三、正则量子化  

如果只有电磁场或只有狄拉克场，由于它们的拉氏量/哈密顿量都只有二次项，所以使用谐振子模型就可以直接得到解析解。例如，真空中电磁场的正则量子化就是在库仑规范 $ \nabla \cdot \mathbf{A} = 0$ 下利用谐振子模型得到平面波模式上的产生和湮灭算符及其演化。这些模式的演化是彼此独立（解耦）的。

> 解析解为 $\mathbf{A}(\mathbf{x},t) = \sum\_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega\_\mathbf{k}V}} \left[ a\_{\mathbf{k},\sigma} \bm{\epsilon}\_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}(\mathbf{k}\cdot \mathbf{x}-\omega\_\mathbf{k}t)} + \text{h.c.} \right]$ ，其中 $\epsilon\_{\mathbf{k},\sigma}$ 表示与 $\mathbf{k}$ 垂直且彼此垂直的两个向量，$\sigma$ 表示偏振， $\text{h.c.}$ 表示厄米共轭（hermitian conjugate）， $V$ 表示腔内体积。如果不是腔而是全空间，则把 $\sum\frac{1}{\sqrt{V}}$ 换成 $\int \mathrm{d}^3\mathbf{k} \frac{1}{(2\pi)^{3/2}}$ 。由于正则量子化是量子光学的标准教科书内容，此处不再赘述，具体可参考 [Atom-Photon Interaction](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197) 的附录章节。

在有源的情况下，我们无法在 $\nabla\cdot \mathbf{A}=0$ 的前提下取到 $\phi=0$ ，这导致此时不再只有横模 $\mathbf{E}\_{\perp}(\mathbf{k},t) = -\partial\_t \mathbf{A}(\mathbf{k},t)$ ，而是存在与源有关的纵模 $\mathbf{E}\_{\parallel}(\mathbf{k},t) = -\mathrm{i}\mathbf{k} \phi(\mathbf{k},t) = -\mathrm{i}\frac{\mathbf{k}}{k^2} \rho(\mathbf{k},t)$ 。横模 $\mathbf{E}\_{\perp}$ 能用平面波模式上的产生和湮灭算符表示，但纵模 $\mathbf{E}\_{\parallel}$ 是与源有关的。

如果我们把源看成经典对象，那么纵模就无法量子化。而如果我们对源进行全量子处理，也就是把源当作和 $\mathbf{A}$ 一样的量子场来处理（也就是 $\rho = -e\bar\psi\gamma^0\psi =  -e\psi^\dagger\psi$ ），那么纵模就是与狄拉克场 $\psi$ 耦合起来的。此时，能够解耦的模式不再是平面波模式，而是电磁场和狄拉克场的混合模式。

如果我们能够解出这些模式，那也还好。但问题就出在这了：耦合项 $e\bar\psi A\_\mu\gamma^\mu \psi$ 不像自由项 $\bar{\psi}(-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi , \ \frac{1}{2}(\mathbf{E}^2+\mathbf{B}^2)$ 那样是二次项——它是三次项，是非简谐的！这导致我们无法解析地算出混合模式，也就是说，没有解析解。此时，我们最多只能写出 $\mathbf{A}(\mathbf{x})$ 而不是 $\mathbf{A}(\mathbf{x},t)$ ：

$\mathbf{A}(\mathbf{x}) = \sum\_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega\_\mathbf{k}V}} \left[ a\_{\mathbf{k},\sigma} \bm{\epsilon}\_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}\mathbf{k}\cdot \mathbf{x}} + \text{h.c.} \right]$

此时我们只能使用微扰论对系统进行求解，也就是在自由项的基础上，将耦合项作为微扰来处理。幸亏，电磁场和狄拉克场的耦合常数 $e = \sqrt{4\pi \alpha} \simeq 0.3$ （自然单位制）不算很强，使得微扰论可以成立。这之后就是量子场论的内容了——计算 S 矩阵、散射振幅等等，此处暂不作介绍。

## 四、低能近似、薛定谔方程  

在高能的情形下，我们需要使用量子场论，但在低能情形下，我们有一个良好的近似理论，这个理论就是量子力学。在本节中，我们看看高能情形下的哈密顿量如何退化成低能情形的有效哈密顿量。

### 4.1 高能物理/低能物理  

我们先来回顾一下算符场 $\psi$ 、 $\bar\psi$ 、 $A$ 的物理意义：

场 $\psi(\mathbf{x},t)$ 的物理意义是在时空点 $(\mathbf{x},t)$ 处湮灭一个电子，或者产生一个正电子。

场 $\bar\psi$ 的物理意义则是产生一个电子，或者湮灭一个正电子。

在拉氏量/哈密顿量中，这两个场总是成对出现，因为电荷守恒。

场 $A\_\mu$ 既可以产生光子，也可以湮灭光子。因为光子的反粒子就是它自己。

所以耦合项 $ e\bar{\psi} \gamma^\mu A\_\mu \psi$ 可以描述以下多种过程：

1. 湮灭一个电子，产生一个光子，再产生一个电子。
2. 湮灭一个电子，湮灭一个光子，再产生一个电子。
3. 湮灭一个光子，产生电子-正电子对。
4. 湮灭电子-正电子对，产生一个光子。
5. ... （其他高阶过程）

其中 3 和 4 以及其他高阶过程属于高能物理，处理它们需要使用量子场论。

而 1 和 2 属于低能物理。它们表示一个电子通过吸收或发射一个光子，从一个态跃迁到另一个态。

只考虑低能情形，意味着以下两点：

> 1. 电子数是不变的。没有电子-正电子对的产生和湮灭。  
> 2. 狄拉克场 $\psi = \begin{bmatrix}\psi\_1\\\\ \psi\_2\end{bmatrix}$ 的正电子项很小 $\psi \_2\approx 0$ 。电子项 $\psi\_1 = \begin{bmatrix}\psi\_{1\uparrow} \\\\ \psi\_{1\downarrow}\end{bmatrix}$ 才是我们关心的。这是因为我们的宇宙充斥着电子，而正电子很少。

低能情形的理论可以被大大地简化，见 4.3 节。不过在那之前，我们先把狄拉克方程展开熟悉一下。

### 4.2 狄拉克方程  

狄拉克方程为 $\mathrm{i}\gamma^\mu D\_\mu \psi - m\psi=0$ ，其中

$\gamma^0 = \begin{bmatrix} I & 0 \\\\ 0 &-I \end{bmatrix},\  \gamma^i=\begin{bmatrix} 0 & \sigma^i \\\\ -\sigma^i & 0 \end{bmatrix} \quad(i=1,2,3)$

$\sigma^i $ 是泡利矩阵，

以及 $\psi = \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix}$ ，其中 $\psi\_1 = \begin{bmatrix}\psi\_{1\uparrow} \\\\ \psi\_{1\downarrow}\end{bmatrix}$ 是电子的两个自旋分量， $\psi\_2 = \begin{bmatrix}\psi\_{2\uparrow} \\\\ \psi\_{2\downarrow}\end{bmatrix}$ 是正电子的两个自旋分量。

代入狄拉克方程得：

$\mathrm{i}\begin{bmatrix} I & 0 \\\\ 0 &-I \end{bmatrix} D\_t \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix} + \mathrm{i} \begin{bmatrix} 0 & \bm\sigma \cdot \mathbf{D} \\\\ -\bm\sigma \cdot \mathbf{D} & 0 \end{bmatrix} \begin{bmatrix}\psi\_1 \\\\ \psi\_2 \end{bmatrix} -m \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix}=0$

其中 $D\_t =  \partial\_t +\mathrm{i}eA\_0 = \partial\_t - \mathrm{i}e\phi$ ， $\mathbf{D} = \nabla +\mathrm{i}e\mathbf{A}$ （使用 $(-,+,+,+)$ 度规约定）。

化简得

$\mathrm{i} \begin{bmatrix}D\_t\psi\_1 \\\\ -D\_t\psi\_2\end{bmatrix} +\mathrm{i} \begin{bmatrix}\bm\sigma\cdot \mathbf{D} \psi\_2 \\\\ -\bm\sigma\cdot \mathbf{D}\psi\_1\end{bmatrix} -m \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix}=0$

即

$\boxed{ \begin{aligned} \mathrm{i} D\_t \psi\_1 + \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi\_2 - m\psi\_1 &= 0 \\\\ -\mathrm{i} D\_t \psi\_2 - \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi\_1 - m\psi\_2 &= 0 \end{aligned}  }\quad (\star)$

这就是狄拉克方程的展开形式：我们把电子项 $\psi\_1$ 和正电子项 $\psi\_2$ 写成两个方程。原来它们在同一个方程里。

我们还可以进一步把它们分别展开成两个方程，对应两种自旋。不过由于我们比较熟悉泡利算符，所以就没必要这么做了。

到此为止，我们还没有做任何近似。从下一节开始，我们对狄拉克方程做低能近似。

### 4.3 低能有效哈密顿量  

在低能情形下，我们不考虑电子静质量带来的相位变化 $\mathrm{e}^{-\mathrm{i}mt}$ ，因此我们把它分离出来，也就是把 $\psi = \begin{bmatrix}\psi\_1\\\\ \psi\_2\end{bmatrix}$ 换成 $\psi = \begin{bmatrix}\varphi \mathrm{e}^{-\mathrm{i}mt}\\\\ \chi  \mathrm{e}^{-\mathrm{i}mt}\end{bmatrix}$ ，代入展开后的狄拉克方程 $(\star)$ 得：

$\begin{aligned} &\mathrm{i} D\_t \varphi + \mathrm{i} \bm\sigma \cdot \mathbf{D} \chi  = 0 &(1)\\\\ -&\mathrm{i} D\_t \chi - \mathrm{i} \bm\sigma \cdot \mathbf{D} \varphi - 2m\chi = 0 &(2) \end{aligned}$

由于低能情形下正电子项 $\chi$ 很小，所以 $D\_t \chi \approx 0$ ，代入 $(2)$ 得：

$\chi \approx - \frac{\mathrm{i}}{2m} \bm\sigma \cdot \mathbf{D} \varphi$

将其代入 $(1)$ 得：

$\mathrm{i} D\_t \varphi +  \frac{1}{2m}(\bm\sigma \cdot \mathbf{D})^2 \varphi = 0 $

可以证明（见附录）

$\begin{aligned} (\bm \sigma \cdot \mathbf{D})^2 &=\mathbf{D}^2 - \mathrm{i}e \bm\sigma\cdot \mathbf{B} \\\\ &= (\nabla +\mathrm{i}e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B} \\\\ &= -(\mathbf{p} + e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B}  \end{aligned}$

所以

$\mathrm{i} D\_t \varphi =  \frac{1}{2m}[(\mathbf{p} + e\mathbf{A})^2 + e \bm\sigma\cdot \mathbf{B} ] \varphi$

把 $D\_t = \partial\_t - \mathrm{i}e\phi$ 代入得

$\boxed{ \mathrm{i} \partial\_t \varphi =  \left[\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2+ \frac{e}{2m} \bm\sigma\cdot \mathbf{B}  - e\phi  \right]\varphi }$

这就是（带自旋的）电子的薛定谔方程，也叫做泡利方程。注意此处 $e$ 是正数，而电子 $\varphi$ 带负电荷。

于是我们可以定义电子的有效哈密顿量为：

$\boxed{ H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2- \frac{e}{2m} \bm\sigma\cdot \mathbf{B}  - e\phi   }$

由于磁场比电场弱很多 $B\sim E/c$ 。哈密顿量中与磁场有关的项 （ $\frac{e}{2m} \bm\sigma\cdot \mathbf{B}$ ）的数量级是电场有关项（ $e\phi$ ）的 $\alpha\approx \frac{1}{137}$ 倍。所以在通常的哈密顿量 $H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2 - e\phi  $ 中我们可以忽略自旋项 $\frac{e}{2m} \bm\sigma\cdot \mathbf{B}$ 。

可见，**量子场论的低能极限就是量子力学**。

> 我们知道，在氢原子中解无自旋的薛定谔方程，得到的结果需要精细结构修正。这些修正一共有三项：自旋-轨道耦合、相对论动能修正、以及 Darwin 项。其中动能修正项来自于质能关系 $E^2 = p^2 +m^2$ ，Darwin 项来自于电子项和正电子项之间的干涉（也可以理解成虚电子-正电子对的涨落），自旋-轨道耦合，顾名思义，来自于电子的自旋，而这已经被泡利方程考虑进来了。  
>   
> 因此，在氢原子中解泡利方程，可以得到自旋-轨道耦合的更正项。但仍然得不到相对论动能修正项和 Darwin 项。如果想要同时得到这三个精细结构更正项，就还是需要量子场论和狄拉克方程。  
>   
> 另外，还有一个修正项与精细结构修正的数量级相同，它叫做 Lamb shift（兰姆位移），来自于电磁场（虚光子）的涨落，而非电子-正电子对的涨落。

---

## 五、长波近似、偶极子表象  

现在我们考虑光场与原子内电子的相互作用。我们首先要做的近似是**玻恩-奥本海默近似**，也就是把原子实和电子的哈密顿量解耦，从而可以只考虑电子的哈密顿量。这是因为电子运动比原子实快得多，导致我们可以把原子实受到的力看做一个平均作用力；反过来，我们可以把电子看成在一个不变的背景库仑势中运动。接下来，我们做一系列其他近似。

### 5.1 长波近似（偶极子近似）  

由于玻尔半径（~50pm）远小于光学波长（~500nm），我们可以不考虑原子内的电磁场梯度，也就是将哈密顿量 $H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2 - e\phi  + H\_\text{EM}$ 中的 $\mathbf{A}(\mathbf{x})$ 换成只与时间有关的场 $\mathbf{A}(\mathbf{0})$ 。其中 $H\_\text{EM}=\sum\_{\mathbf{k,\sigma}} \omega\_{\mathbf{k,\sigma}}\left(a\_{\mathbf{k,\sigma}}^\dagger a\_{\mathbf{k,\sigma}} + \frac{1}{2}\right)$ 是光场的哈密顿量。

把 $\mathbf{x}=\mathbf{0}$ 代入 $\mathbf{A}(\mathbf{x}) = \sum\_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega\_\mathbf{k}V}} \left[ a\_{\mathbf{k},\sigma} \bm{\epsilon}\_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}\mathbf{k}\cdot \mathbf{x}} + \text{h.c.} \right]$ 得

$\mathbf{A}(\mathbf{0}) = \sum\_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega\_\mathbf{k}V}} \left(a\_{\mathbf{k},\sigma} + a^\dagger\_{\mathbf{k},\sigma}\right) \bm{\epsilon}\_{\mathbf{k},\sigma} $

这个近似也叫偶极子近似，因为这个近似等价于在多极近似（multipole expansion）中忽略高阶项（四极子、八极子等等）。

### 5.2 偶极子表象  

定义偶极子（dipole）算符为 $\mathbf{d}=-e\mathbf{x}$ （ $e$ 为正数， $\mathbf{x}$ 为电子相对于原子核的位置），并且做幺正变换

$\boxed{U=\exp\left[ -\mathrm{i}\mathbf{d}\cdot \mathbf{A}(\mathbf{0})\right]} = \exp\left[ \sum\_{\mathbf{k},\sigma} (\lambda \_{\mathbf{k,\sigma}} a\_{\mathbf{k,\sigma}}^\dagger - \lambda\_{\mathbf{k,\sigma}}^\* a\_{\mathbf{k,\sigma}} )\right] = \prod\_{\mathbf{k,\sigma}} D\_{\mathbf{k,\sigma}}(\lambda\_{\mathbf{k,\sigma}})$

其中 $\lambda\_{\mathbf{k,\sigma}} = -\mathrm{i}\mathbf{d}\cdot \epsilon\_{\mathbf{k,\sigma}}$ ， $D\_{\mathbf{k,\sigma}}(\alpha) = \exp( \alpha a^\dagger\_{\mathbf{k,\sigma}} - \alpha a\_{\mathbf{k,\sigma}})$ 为 $({\mathbf{k,\sigma}})$ 模式上的平移算符。

可以证明[#ref\\\\_1](#ref\\\\_1)，新表象下的哈密顿量为：

$\boxed{ H \mapsto U^\dagger H U = \frac{1}{2m}\mathbf{p}^2 - e\phi  +\mathbf{d}\cdot \mathbf{E}\_\perp(\mathbf{0}) + H\_\text{EM}+ H\_{\text{dip}} } \quad (3)$

其中 $ \mathbf{E}\_\perp(\mathbf{0}) = \sum\_{\mathbf{k,\sigma}} \mathrm{i} \sqrt{\frac{\omega\_k}{2V}} (a\_{\mathbf{k,\sigma}} - a^\dagger\_{\mathbf{k,\sigma}}) \epsilon\_{\mathbf{k,\sigma}}$ 是电场的横场部分， $H\_{\text{dip}} = \sum\_{\mathbf{k,\sigma}} \frac{1}{2V} (\epsilon\_{\mathbf{k,\sigma}} \cdot \mathbf{d})^2$ 为偶极子的自能，通常可以忽略。

这个表象叫做 $\mathbf{d}\cdot\mathbf{E}$ 表象，也叫偶极子表象。而原来的表象叫做 $\mathbf{p}\cdot \mathbf{A}$ 表象。

### 5.3 二能级近似  

现在我们将原子简化为一个二能级系统（只有基态和激发态），也就是将原子的哈密顿量 $\frac{1}{2m}\mathbf{p}^2 - e\phi$ 简化为 $H\_{\text{atom}} = \frac{\omega\_{ab}}{2} \sigma\_z$ ，其中 $\omega\_{ab}$ 是能级差， $\sigma\_z = |b\rangle\langle b| - |a\rangle\langle a|$ ， $|b\rangle$ 是激发态， $|a\rangle$ 是基态。

二能级之间的跃迁对光场的偏振态有要求（选择定则），此时我们只考察对应的偏振态 $\sigma$ ，使得 $\mathbf{d} \cdot \mathbf{E}\_{\perp}(\mathbf0)$ 变为 $dE\_\perp(0)$ 。

另外，还需要将偶极子算符投影到二能级子空间里： $d\mapsto (|a\rangle\langle a| + |b\rangle\langle b| ) d = d\_{ab}|a\rangle\langle b| + d\_{ba} |b\rangle \langle a|$ 。其中 $d\_{ba} = d\_{ab}^\*$ 。

> 之所以没有 $d\_{aa} |a\rangle \langle a|$ 项是因为 $d\_{aa} =-e \int \langle \psi\_a|\mathbf{x}|\psi\_a\rangle =-e\int\psi^\*(\mathbf{x})\ \mathbf{x}\ \psi(\mathbf{x})\mathrm{d}^3\mathbf{x}= 0$ 。类似也有 $d\_{bb}=0$ 。

我们总是可以选取相位 $d\_{ab} \mapsto d\_{ab}\mathrm{e}^{\mathrm{i}\theta}$ 使得 $d\_{ab} = d\_{ba}$ 是实数，因为总体相位不重要。于是偶极子算符可以写成：

$\boxed{ d=d\_{ab}(\sigma\_+ +\sigma\_-) }$

其中 $\sigma\_+ = |b\rangle\langle a|,\ \sigma\_-=|a\rangle\langle b|$ 。

而电场算符可以写成：

$E\_\perp(\mathbf{0}) = \sum\_{\mathbf{k}} \mathrm{i} \sqrt{\frac{\omega\_k}{2V}} (a\_{\mathbf{k}} - a^\dagger\_{\mathbf{k}}) $

我们可以把虚数因子 $\mathrm{i}$ 吸收进湮灭算符中： $a\_{\mathbf{k}} \mapsto \mathrm{i}a\_\mathbf{k}, \ a\_{\mathbf{k}}^\dagger \mapsto -\mathrm{i}a\_{\mathbf{k}}^\dagger$ 。于是有

$\boxed{ E\_\perp(\mathbf{0}) = \sum\_{\mathbf{k}} \sqrt{\frac{\omega\_k}{2V}} (a\_{\mathbf{k}} +a^\dagger\_{\mathbf{k}})  }$

将这些关系代入偶极子表象的哈密顿量 $(3)$ ，并且忽略偶极子自能，得到：

$\boxed{ H =  \frac{\omega\_{ab}}{2} \sigma\_z +\sum\_{\mathbf{k}} g\_{\mathbf{k}}(\sigma\_+ +\sigma\_-)(a\_{\mathbf{k}} +a^\dagger\_{\mathbf{k}}) + H\_\text{EM} }$

其中 $g\_{\mathbf{k}}=d\_{ab}\sqrt{\frac{\omega\_k}{2V}} $ 是二能级系统与光场的耦合强度。

### 5.4 腔量子电动力学（Cavity QED）  

现在考虑把原子放在一个很小的腔里，腔长 $\sim 100 \mu \text{m}$ ，则自由光谱区为 $c/(2L)\sim 1.5 \text{THz}$ ，也就是说相邻模式的频率差为 $\sim 1.5 \text{THz}$ ，远大于自然线宽 $\sim 10 \text{MHz}$ 和耦合强度 $g\sim 100\text{MHz}$ 。这使得我们可以选择出单个光场模式与二能级原子相互作用。这样一来，其他光场模式的失谐量 $\Delta =\omega\_\mathbf{k}-\omega\_{ab}$ 就很大，可以忽略。

于是我们就得到了单个光场与原子中单个电子的相互作用哈密顿量：

$\boxed{ H =  \frac{\omega\_{ab}}{2} \sigma\_z +g(\sigma\_+ +\sigma\_-)(a +a^\dagger) + \omega\left(a^\dagger a +\frac{1}{2}\right) }$

其中 $g = g\_{\mathbf{k}}$ ， $\omega=\omega\_\mathbf{k}$ 是选择出来的光场的耦合强度和频率。

在腔中还有一个好处，就是耦合强度 $g\_{\mathbf{k}}=d\_{ab}\sqrt{\frac{\omega\_k}{2V}} $ 比较强，因为模式体积 $V$ 很小。

由于 $\sigma\_+ a^\dagger$ 代表产生一个光子，并且电子从低能级跃迁到高能级，所以它的概率很低 $\sim\frac{1}{\omega+\omega\_{ab}}$ ，可以忽略。类似地， $\sigma\_-a$ 也可以忽略。这叫做旋转波近似（Rotating Wave Approximation，RWA）。

做旋转波近似之后，我们就得到了 Jaynes-Cummings 哈密顿量：

$\boxed{ H =  \frac{\omega\_{ab}}{2} \sigma\_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger)  }$

Jaynes-Cummings 模型有[解析解](https://zhuanlan.zhihu.com/p/701838204)，这些解叫做缀饰态（dressed states）。由于篇幅所限不作介绍。

## 尾声：物理的魅力  

我们从非常复杂的 QED 拉氏量出发：

$\begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial\_\mu -m)\psi - eA\_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F\_{\mu\nu} F^{\mu\nu} \end{aligned} $

这个拉氏量非常复杂：它不仅考虑了电子的反粒子——正电子，并且耦合项 $- eA\_\mu \bar{\psi} \gamma^\mu \psi$ 还是一个三次项，可以描述电子-正电子对产生/湮灭等多种过程。它没有解析解，只能用量子场论的微扰法求解。

但经过一系列简化和近似（低能近似、玻恩-奥本海默近似，长波/偶极子近似、二能级近似、旋转波近似）之后，我们竟然得到了一个有解析解的模型！

$H =  \frac{\omega\_{ab}}{2} \sigma\_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger) $

可见，根据所考虑的情况，我们做出了一系列适当和必要的简化，从而在纷复繁杂的现象中抓住本质，最终能够更好地认识世界。

这样的方法论不仅可以用到物理中，而且可以泛化到其他学科。这就是物理的魅力。

---

【更高更妙的电动力学】系列到此结束。希望你觉得这趟旅途愉快！

## 附录  

证明 $(\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B}$ ，其中 $\mathbf{D} = \nabla+ \mathrm{i}e\mathbf{A}$ 。

> 根据恒等式 $(\bm\sigma \cdot \mathbf{a})(\bm\sigma \cdot \mathbf{b}) = \mathbf{a} \cdot \mathbf{b} + \mathrm{i}\bm\sigma \cdot(\mathbf{a}\times\mathbf{b})$ 得  
>   
>  $(\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D})$   
>   
> 于是我们需要计算 $(\mathbf{D}\times\mathbf{D})$ 。  
>   
> 我们先计算 $[D\_i, D\_j]$ ：  
>  $\begin{aligned} [D\_i, D\_j] &= [\partial\_i +\mathrm{i}eA\_i, \partial\_j +\mathrm{i}eA\_j] \\\\ &= \cancel{[\partial\_i,\partial\_j]} + \cancel{e^2[A\_i, A\_j]} + \mathrm{i}e[\partial\_i, A\_j] - \mathrm{i}e[\partial\_j,A\_i] \end{aligned}$   
>   
> 于是我们需要计算 $[\partial\_i, A\_j]$ ：  
>   
>  $\begin{aligned} [\partial\_i, A\_j] f &= \partial\_i (A\_j f) -A\_j \partial\_i f \\\\ &= (\partial\_i A\_j) f + A\_j \partial\_if - A\_j \partial\_i f \\\\ &= (\partial\_iA\_j)f \end{aligned}$   
>   
> 所以 $[\partial\_i, A\_j] = (\partial\_i A\_j)$ 。  
>   
> 于是  
>   
>  $\begin{aligned} [D\_i, D\_j] &= \mathrm{i}e[\partial\_i, A\_j] -\mathrm{i}e[\partial\_j,A\_i] \\\\ &= \mathrm{i}e (\partial\_i A\_j - \partial\_j A\_i) \\\\ &= \mathrm{i}e \epsilon\_{ijk}B^k \end{aligned}$   
>   
> 于是  
>   
>  $\begin{aligned} (\mathbf{D}\times\mathbf{D})^k &=\epsilon^{kij} D\_i D\_j \\\\ &= \frac{1}{2} \epsilon^{kij}[D\_i,D\_j] \\\\ &= \frac{\mathrm{i}e}{2} \epsilon^{kij} \epsilon\_{ijl} B^l \\\\ &= \frac{\mathrm{i}e}{2} (\delta^k\_l \delta^j\_j - \delta^k\_j\delta^j\_l) B^l \\\\ &=\mathrm{i}e \delta^k\_l B^l \\\\ &= \mathrm{i}eB^k \end{aligned}$   
>   
> 所以 $\mathbf{D}\times \mathbf{D} = \mathrm{i}e\mathbf{B}$ 。  
>   
> 于是  
>  $\begin{aligned} (\bm\sigma \cdot \mathbf{D})^2 &= \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D}) \\\\ &= \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B} \end{aligned}$   
>   
> 证毕。

## 参考  

1. Atom-Photon Interactions by Cohen-Tannoudji [https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197)
