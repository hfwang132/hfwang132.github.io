---
title: "哈密顿力学视角下的电动力学【更高更妙的电动力学·5】"
date: 2025-03-22T23:16:56+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/32052863470"
author: "Haifei"
tags: ["电动力学"]
categories: ["数学物理方法"]
---

本系列上一篇文章：

[Godfly：狄拉克磁单极子——陈类与陈数【更高更妙的电动力学·4】](https://zhuanlan.zhihu.com/p/1889370433708609679)

---

在[之前的文章](https://zhuanlan.zhihu.com/p/23958176393)中，我们说到了电磁场和狄拉克场的哈密顿量：

$$\begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi - eA_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \end{aligned} $$

那么它们的哈密顿量是什么呢？为什么量子场论不怎么使用哈密顿量？且看下文分解。

---

## 一、电磁场的哈密顿表述  

已知电磁场的拉格朗日量：

$$\begin{aligned} \mathcal{L}[A_\mu, \partial_\nu A_\mu] &=  -\frac{1}{4\mu_0} F_{\mu\nu} F^{\mu\nu} + A_{\mu} J^{\mu} \\ &= \frac{1}{2}\left(\epsilon_0\mathbf{E^2} -\frac{1}{\mu_0} \mathbf{B^2}\right) -\rho\phi + \mathbf{A} \cdot \mathbf{J} \end{aligned} $$

本节我们试图从它出发，得到哈密顿量，并得到哈密顿正则方程，也就是麦克斯韦方程。

### 1.1 电磁场的哈密顿量  

我们先来试试直接使用勒让德变换：

$$\mathcal{H} = \Pi^i  \dot{A}_i - \mathcal{L}$$

其中 $\Pi^i = \frac{\partial \mathcal{L}}{\partial \dot{ A}_i}$ 是 $\mathbf{A}$ 对应的正则动量。

我们希望从八个哈密顿方程中得到麦克斯韦方程：

$$\boxed{ \dot{A}_i = \frac{\delta \mathcal{H}}{\delta \Pi^i},\quad \dot{\Pi}^i = \frac{\delta \mathcal{H}}{\delta A_i} }$$

其中符号 $\delta$ 是变分。

但是事情没有这么简单。注意到正则动量 $\Pi^0 = \frac{\partial \mathcal{L}}{\partial \dot{\phi}} = 0$ 恒等于零！这说明它是一个约束。

于是

$$\mathcal{H} = \mathbf{\Pi} \cdot \dot{\mathbf{A}} - \mathcal{L}$$

其中 $\mathbf{\Pi}=\frac{\partial \mathcal{L}}{\partial \dot{\mathbf{A}}} = \dot{\mathbf{A}} + \nabla \phi = -\mathbf{E}$ 是 $\mathbf{A}$ 对应的正则动量。

于是

$$\begin{aligned} \mathcal{H} &= (\dot{\mathbf{A}} + \nabla \phi) \cdot \dot{\mathbf{A}} - \left[\frac{1}{2}(\dot{\mathbf{A}}+\nabla \phi)^2 -\frac{1}{2} (\nabla \times \mathbf{A})^2 - \rho \phi + \mathbf{A}\cdot \mathbf{J} \right]  \\ &= \frac{1}{2}\mathbf{\Pi}^2 - \mathbf{\Pi} \cdot \nabla \phi + \frac{1}{2} (\nabla \times \mathbf{A})^2 + \rho \phi - \mathbf{A}\cdot \mathbf{J}  \end{aligned}$$

变分时利用分部积分，可以将 $- \mathbf{\Pi} \cdot \nabla \phi $ 转化为 $+\phi \nabla \cdot \mathbf{\Pi}$ 。于是：

$$\boxed{ \begin{aligned}  \mathcal{H}=\frac{1}{2}\mathbf{\Pi}^2   + \frac{1}{2} (\nabla \times \mathbf{A})^2 - \mathbf{A}\cdot \mathbf{J}+ \phi(\rho +\nabla\cdot \mathbf{\Pi})    \end{aligned} }$$

### 1.2 电磁场的正则方程  

现在我们考虑哈密顿方程 $\dot{\Pi}^0 = -\frac{\delta \mathcal{H}}{\delta A_0} $ 。既然 $\Pi^0$ 恒为零，那么 $\dot{\Pi}^0$ 也应当恒为零，于是根据哈密顿方程有：

$$\dot{\Pi}_0 = -\frac{\delta \mathcal{H}}{\delta A_0} = -\frac{\delta \mathcal{H}}{\delta \phi} = \rho + \nabla \cdot \mathbf{\Pi} = 0\Rightarrow  \boxed{\nabla\cdot \mathbf{E} = \rho}$$

这正是高斯定律。在哈密顿表述中，它是作为约束出现的。而 $\phi$ 就是对应的拉格朗日乘子。

这说明在哈密顿表述中， $\phi$ 不是一个独立的动力学变量。我们不妨取 $\phi =0$ ，这叫做 Weyl 规范。

> Weyl 规范是一个不完全的规范，因为剩下的 $A_1,A_2,A_3$ 仍有规范自由度。

当然，我们也可以取其他规范。例如库仑规范 $\nabla \cdot \mathbf{A} = 0$ ，那么此时 $\phi$ 就依赖于 $\mathbf{A}$ （根据规范变换）。

把约束 $ \rho + \nabla \cdot \mathbf{\Pi} = 0$ 代入 $\mathcal{H}$ 得：

$$\boxed{ \begin{aligned} \mathcal{H} &= \frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 - \mathbf{A}\cdot \mathbf{J}\\ &= \frac{1}{2}\mathbf{E}^2  + \frac{1}{2} \mathbf{B}^2  - \mathbf{A}\cdot \mathbf{J}   \end{aligned} }$$

> 注意到哈密顿量中并没有势能项 $\rho \phi$ ，这与哈密顿量不满足规范不变性有关，见第二节末。  
>   
> 我们来看看为什么哈密顿量不具有规范不变性：  
>   
> 在哈密顿表述中，场 $\varphi$ 的运动方程为 $\partial_t \varphi = \delta \mathcal{H}/\delta \pi_\varphi$ ，其中场 $\pi_\varphi$ 是场 $\varphi$ 对应的正则动量。  
>   
> 注意到，运动方程左边的导数是 $\partial_t$ ，而不是规范不变的协变导数 $D_t = \partial_t + \mathrm{i}eA_t = \partial_t -\mathrm{i}e\phi$ 。所以相应地，方程的右边也不是规范不变的。  
>   
> 这就是哈密顿表述在高能物理中不常用的原因之一。

最后，我们考虑剩下的哈密顿方程：

$$\dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}},\quad \dot{\mathbf{\Pi}} = \frac{\delta \mathcal{H}}{\delta \mathbf{A}}$$

其中前者 $\dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}} = \mathbf{\Pi} - \nabla\phi \Rightarrow \mathbf{E} = -\frac{\partial A}{\partial t} - \nabla \phi$ 是电场的定义式，后者则是安培定律：

$$\begin{aligned} \dot{\mathbf{\Pi}} &= -\frac{\delta \mathcal{H}}{\delta \mathbf{A}} \\ &= -\frac{\delta }{\delta \mathbf{A}} \int\left[\frac{1}{2}(\nabla \times \mathbf{A})^2 - \mathbf{J} \cdot \mathbf{A}\right] \mathrm{d}^3 x  \\&= \int[-\nabla\times(\nabla\times \mathbf{A}) + \mathbf{J}]\mathrm{d}^3x \end{aligned}$$

即

$$\boxed{ \begin{aligned} &\dot{\mathbf{E}}=\nabla\times\mathbf{B} -\mathbf{J} \\ &\Rightarrow   \nabla\times \mathbf{B} = \mathbf{J} + \dot{\mathbf{E}} \end{aligned} }$$

现在我们有了安培定律和高斯定律。但另外两个方程去哪了？实际上，与拉格朗日表述中的 $\mathrm{d}F=\mathrm{d}\mathrm{d}A=0$ 类似，在哈密顿表述中，另外两个无源方程也是定义的一部分。由 $\mathbf{B}:=\nabla\times \mathbf{A}$ 即可得到 $\nabla \cdot \mathbf{B}=0$ ；由 $\mathbf{E} := -\frac{\partial A}{\partial t} - \nabla \varphi$ 即可得到 $\nabla \times \mathbf{E} =-\dot{\mathbf{B}}$ 。

最后，我们来对比一下拉格朗日表述和哈密顿表述：

$$\begin{matrix} \hline & \text{Lagrangian} & \text{Hamiltonian} \\ \hline \text{Field variables} & A_\mu, \partial_\mu A_\nu & A_\mu, \Pi^\mu \\ \hline \text{Eq. of motion} & \text{Euler-Lagrange equations} & \text{Hamiltonian equations} \\ & \partial_\mu F^{\mu\nu}=J^\nu & \dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}},\quad \dot{\mathbf{\Pi}} = \frac{\delta \mathcal{H}}{\delta \mathbf{A}} \\ & \text{Ampere Law, Gauss Law} & \text{Ampere Law} \\ \hline \text{Constraints}  & \text{None} & \Pi^0=\dot{\Pi}^0=0\\ & & \text{Gauss Law} \\ \hline  \end{matrix}$$

### 1.3Dirac-Bergmann 理论  

以上这一套处理有约束的哈密顿系统的理论，叫做 Dirac-Bergmann 理论。其中 $\Pi^0 = \frac{\partial \mathcal{L}}{\partial \dot{A_0}} = 0$ 叫做 Primary constraint， $\dot{\Pi}^0=-\frac{\delta \mathcal{H}}{\delta A_0} =0$ 叫做 Secondary constraint。在 D-B 理论中对这些约束有着更系统和更严格的处理。

### 1.4 为什么场论通常使用拉格朗日表述  

为什么电磁场的哈密顿表述如此不便？

这是因为在拉格朗日力学中，时间 $t=x^0$ 和空间坐标 $x^{1,2,3}$ 的地位是比较平等的，也很容易体现洛伦兹不变性。但在哈密顿力学中，时间 $t$ 拥有特殊地位，难以体现洛伦兹不变性。正是时间 $t=x^0$ 的特殊地位导致了场分量 $A_0$ 及其对应正则动量 $\Pi^0$ 的约束。这也导致了**哈密顿量不具有规范不变性**。

在经典（低速）力学情况下，使用哈密顿力学比较方便。但在狭义相对论情形下，时间 $t$ 被提升为时空坐标 $x^0$ ，可以通过洛伦兹 boost 和其他空间坐标 $x^{1,2,3}$ 混合起来，此时哈密顿力学就显得尴尬了。

之所以在量子力学中我们可以经常使用哈密顿量（以及对应的海森堡/薛定谔表述），正是因为量子力学讨论的是低速情形。而如果进入狭义相对论的范畴，我们就不得不需要用到量子场论，并且使用拉格朗日量以及路径积分表述。

---

## 二、狄拉克场的哈密顿表述  

上面对电磁场 $A_\mu$ 做的一切步骤都可以对狄拉克场 $\psi$ 做一遍。

从狄拉克场的拉格朗日量出发：

$$\mathcal{L}=\bar{\psi}(\mathrm{i}\hbar c \gamma^\mu \partial_\mu  -mc^2)\psi $$

为了方便推导，我们采用自然单位制： $\hbar = c =1$ ，于是

$$\mathcal{L}=\bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi $$

场变量为 $\psi, \bar{\psi}$ ，它们的正则动量为：

$$\pi_\psi = \frac{\partial\mathcal{L}}{\partial (\partial_0\psi)} = \mathrm{i}\bar\psi \gamma^0 = \mathrm{i} \psi^\dagger$$

$\pi_{\bar\psi} = \frac{\partial\mathcal{L}}{\partial (\partial_0\bar\psi)} = 0$ （Primary constraint）

勒让德变换：

$$\begin{aligned} \mathcal{H} &= \pi_\psi \partial_0\psi + \pi_{\bar\psi}\partial_0\bar\psi - \mathcal{L} \\ &=\mathrm{i}\bar\psi \gamma^0 \partial_0\psi-\bar{\psi}(\mathrm{i} \gamma^\mu \partial_\mu  -m)\psi  \\ &= \bar{\psi}(-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi  \end{aligned}$$

哈密顿方程：

$$\begin{aligned} \partial_0{\psi} &= \frac{\delta \mathcal{H}}{\delta\pi_\psi}  \end{aligned}$$

或

$$\begin{aligned} \delta \mathcal{H} &= (\delta\pi_\psi) \partial_0{\psi} \\ &= \delta(\mathrm{i}\bar\psi \gamma^0 ) \partial_0{\psi} \\ &= (\delta \bar\psi) \mathrm{i} \gamma^0  \partial_0{\psi} \end{aligned}$$

于是

$$\begin{aligned} \mathrm{i} \gamma^0  \partial_0{\psi} &= \frac{\delta \mathcal{H}}{\delta \bar\psi} \\ &= (-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi   \end{aligned}$$

移项得：

$$\boxed{ \mathrm{i} \gamma^\mu \partial_\mu \psi - m\psi = 0 }$$

这就是真空中的狄拉克方程。

如果电磁场不为零，即非真空，那么我们需要考虑电磁场和狄拉克场的总拉氏量：

$$\boxed{ \begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi - eA_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \end{aligned} }$$

可以定义 $J^\mu = -e\bar\psi \gamma^\mu\psi$ （注意此处的 $e$ 是正数，而电子 $\psi$ 带负电），于是耦合项 $- eA_\mu \bar{\psi} \gamma^\mu \psi $ 也可以写成 $+A_\mu J^\mu$ ，与之前的定义吻合。

对这个拉格朗日量做勒让德变换得到：

$$\boxed{ \begin{aligned} \mathcal{H} &= \frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 +  \bar{\psi}[-\mathrm{i}\bm\gamma\cdot (\nabla + \mathrm{i}e\mathbf{A} )+ m]\psi \\  &= \underbrace{\frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 }_{\text{free photon field}} + \underbrace{\bar{\psi}(-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi }_{\text{free Dirac field}} +\underbrace{e\bar\psi(\bm\gamma \cdot \mathbf{A})\psi}_{\text{coupling}} \end{aligned} }$$

求对应的哈密顿方程 $\dot{\mathbf{\Pi}} = \delta \mathcal{H}/\delta\mathbf{A}, \ \dot\psi =  \delta\mathcal{H}/\delta \pi_\psi$ 就能得到耦合的麦克斯韦方程和狄拉克方程。

> 注意到，由于缺失了与时间 $t=x^0$ 有关的 $\bar\psi(-\mathrm{i}\gamma^0\partial_0)\psi$ 项和 $e\bar\psi(\gamma^0A_0)\psi=-e\psi^\dagger\psi \phi = \rho\phi$ 项，**哈密顿量不是规范不变的**。  
>   
> 原因我们已经说过：在哈密顿表述中，时间具有特殊地位；在哈密顿运动方程 $\partial_0\varphi = \delta\mathcal{H}/\delta \pi_\varphi$ 中，左边的时间导数 $\partial_0$ 并非规范不变的（ $D_0$ 才是规范不变的），所以右边哈密顿量肯定也不是规范不变的。

---

本系列下一篇文章（完结篇）：

[Godfly：从量子场论到腔量子电动力学【更高更妙的电动力学·6】](https://zhuanlan.zhihu.com/p/1894566826417034044)
