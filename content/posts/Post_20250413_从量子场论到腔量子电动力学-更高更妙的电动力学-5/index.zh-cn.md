---
title: "从量子场论到腔量子电动力学【更高更妙的电动力学·6】"
date: 2025-04-13T01:52:37+08:00
originalURL: "https://zhuanlan.zhihu.com/p/1894566826417034044"
aliases:
  - "/gm_5/"
  - "/Post_20250406_从量子场论到腔量子电动力学-更高更妙的电动力学-5/"
draft: false
categories: ["数学物理方法"]
tags: ["量子场论", "腔量子电动力学", "电动力学", "Jaynes-Cummings"]
math: true
author: "Haifei"
---

在本篇文章中，我们将从 QED 的拉氏量出发：

\[\begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi - eA_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \end{aligned} \]

这个拉氏量非常复杂：它不仅考虑了电子的反粒子——正电子，并且耦合项 \(- eA_\mu \bar{\psi} \gamma^\mu \psi\) 还是一个三次项，可以描述电子-正电子对产生/湮灭等多种过程。由于三次项的存在，这个拉氏量没有解析解，只能用量子场论的微扰法求解。

但经过一系列简化和近似（低能近似、玻恩-奥本海默近似，长波/偶极子近似、二能级近似、旋转波近似）之后，我们竟然得到了一个有解析解的模型：

\[H =  \frac{\omega_{ab}}{2} \sigma_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger) \]

这就是腔量子电动力学的经典哈密顿量：Jaynes-Cummings 哈密顿量。这是如何做到的？且看下文分解。

---

## 一、正则量子化  

如果只存在电磁场或只存在狄拉克场，由于它们的拉氏量/哈密顿量都只有二次项，那么就使用谐振子模型直接得到解析解。

例如，真空中电磁场的正则量子化，就是在库仑规范 \( \nabla \cdot \mathbf{A} = 0\) 下利用谐振子模型得到平面波模式上的产生和湮灭算符以及解析解。这些模式的演化是彼此独立（解耦）的。

> 解析解为 \(\mathbf{A}(\mathbf{x},t) = \sum_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega_\mathbf{k}V}} \left[ a_{\mathbf{k},\sigma} \bm{\epsilon}_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}(\mathbf{k}\cdot \mathbf{x}-\omega_\mathbf{k}t)} + \text{h.c.} \right]\) ，其中 \(\epsilon_{\mathbf{k},\sigma}\) 表示与 \(\mathbf{k}\) 垂直且彼此垂直的两个向量，\(\sigma\) 表示偏振， \(\text{h.c.}\) 表示厄米共轭（hermitian conjugate）， \(V\) 表示腔内体积。如果不是腔而是全空间，则把 \(\sum\frac{1}{\sqrt{V}}\) 换成 \(\int \mathrm{d}^3\mathbf{k} \frac{1}{(2\pi)^{3/2}}\) 。  
>   
> 由于正则量子化是量子光学的标准教科书内容，此处不再赘述，具体可参考 [Atom-Photon Interactions by Cohen-Tannoudji](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197)[[1]](#ref\_1) 的附录章节。

在有源的情况下，我们无法在 \(\nabla\cdot \mathbf{A}=0\) 的前提下取到 \(\phi=0\) ，这导致此时不再只有横模 \(\mathbf{E}_{\perp}(\mathbf{k},t) = -\partial_t \mathbf{A}(\mathbf{k},t)\) ，而是存在与源有关的纵模 \(\mathbf{E}_{\parallel}(\mathbf{k},t) = -\mathrm{i}\mathbf{k} \phi(\mathbf{k},t) = -\mathrm{i}\frac{\mathbf{k}}{k^2} \rho(\mathbf{k},t)\) 。

横模 \(\mathbf{E}_{\perp}\) 能用平面波模式上的产生和湮灭算符表示，但纵模 \(\mathbf{E}_{\parallel}\) 是与源有关的。

如果我们把源看成经典对象，那么纵模就无法量子化。

而如果我们对源进行全量子处理，也就是把源当作和 \(\mathbf{A}\) 一样的量子场来处理（即 \(\rho = -e\bar\psi\gamma^0\psi =  -e\psi^\dagger\psi\) ），那么纵模就是与狄拉克场 \(\psi\) 耦合起来的。此时，能够解耦的模式不再是平面波模式，而是电磁场和狄拉克场的混合模式。

如果我们能够解出这些模式，那也还好。但问题就出在这了：耦合项 \(e\bar\psi A_\mu\gamma^\mu \psi\) 不像自由项 \(\bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi \) ， \(-\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \) 那样是二次项——它是三次项，是非简谐的！这导致我们无法解析地算出混合模式，也就是说，没有解析解。此时，我们最多只能写出 \(\mathbf{A}(\mathbf{x})\) 而不是 \(\mathbf{A}(\mathbf{x},t)\) ：

\[\mathbf{A}(\mathbf{x}) = \sum_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega_\mathbf{k}V}} \left[ a_{\mathbf{k},\sigma} \bm{\epsilon}_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}\mathbf{k}\cdot \mathbf{x}} + \text{h.c.} \right]\]

这个场 \(\mathbf{A}(\mathbf{x})\) 随时间的变化是写不出解析形式的。对于狄拉克场 \(\psi\) 也是如此。

此时我们只能使用微扰论对系统进行求解，也就是在自由项的基础上，将耦合项作为微扰来处理。

幸亏，电磁场和狄拉克场的耦合常数 \(e = \sqrt{4\pi \alpha} \simeq 0.3\) （自然单位制）不算很强，使得微扰论可以成立。这之后就是量子场论的内容了——计算 S 矩阵、散射振幅等等，此处暂不作介绍。

## 二、低能近似  

在高能的情形下，我们需要使用量子场论，但在低能情形下，我们有一个良好的近似理论，这个理论就是量子力学。在本节中，我们看看高能情形下的拉氏量如何退化成低能情形的有效哈密顿量。

### 2.1高能物理/低能物理  

我们先来回顾一下算符场 \(\psi\) 、 \(\bar\psi\) 、 \(A\) 的物理意义：

场 \(\psi(\mathbf{x},t)\) 的物理意义是在时空点 \((\mathbf{x},t)\) 处湮灭一个电子，或者产生一个正电子。

场 \(\bar\psi\) 的物理意义则是产生一个电子，或者湮灭一个正电子。

在拉氏量中，这两个场总是成对出现，因为电荷守恒。

场 \(A_\mu\) 既可以产生光子，也可以湮灭光子。因为光子的反粒子就是它自己。

所以耦合项 \( e\bar{\psi} \gamma^\mu A_\mu \psi\) 可以描述以下多种过程：

1. 湮灭一个电子，产生一个光子，再产生一个电子。
2. 湮灭一个电子，湮灭一个光子，再产生一个电子。
3. 湮灭一个光子，产生电子-正电子对。
4. 湮灭电子-正电子对，产生一个光子。
5. ... （其他高阶过程）

其中 3 和 4 以及其他高阶过程属于高能物理，处理它们需要使用量子场论。

而 1 和 2 属于低能物理。它们表示一个电子通过吸收或发射一个光子，从一个态跃迁到另一个态。

只考虑低能情形，意味着以下两点：

> 1. 电子数是不变的。忽略电子-正电子对的产生和湮灭。  
>   
> 2. 狄拉克场 \(\psi = \begin{bmatrix}\psi_1\\ \psi_2\end{bmatrix}\) 的正电子项很小 \(\psi _2\approx 0\) 。电子项 \(\psi_1 = \begin{bmatrix}\psi_{1\uparrow} \\ \psi_{1\downarrow}\end{bmatrix}\) 才是我们关心的。这是因为我们的宇宙充斥着电子，而正电子很少。

低能情形的理论可以被大大地简化，见 4.3 节。不过在那之前，我们先把狄拉克方程展开熟悉一下。

### 2.2 狄拉克方程  

对 QED 拉氏量做变分可以得到狄拉克方程

\(\mathrm{i}\gamma^\mu D_\mu \psi - m\psi=0\) ，

其中

\[\gamma^0 = \begin{bmatrix} I & 0 \\ 0 &-I \end{bmatrix},\  \gamma^i=\begin{bmatrix} 0 & \sigma^i \\ -\sigma^i & 0 \end{bmatrix} \quad(i=1,2,3)\]

\(\sigma^i \) 是泡利矩阵，

以及 \(\psi = \begin{bmatrix}\psi_1 \\ \psi_2\end{bmatrix}\) ，其中 \(\psi_1 = \begin{bmatrix}\psi_{1\uparrow} \\ \psi_{1\downarrow}\end{bmatrix}\) 是电子的两个自旋分量， \(\psi_2 = \begin{bmatrix}\psi_{2\uparrow} \\ \psi_{2\downarrow}\end{bmatrix}\) 是正电子的两个自旋分量。

代入狄拉克方程得：

\[\mathrm{i}\begin{bmatrix} I & 0 \\ 0 &-I \end{bmatrix} D_t \begin{bmatrix}\psi_1 \\ \psi_2\end{bmatrix} + \mathrm{i} \begin{bmatrix} 0 & \bm\sigma \cdot \mathbf{D} \\ -\bm\sigma \cdot \mathbf{D} & 0 \end{bmatrix} \begin{bmatrix}\psi_1 \\ \psi_2 \end{bmatrix} -m \begin{bmatrix}\psi_1 \\ \psi_2\end{bmatrix}=0\]

其中 \(D_t =  \partial_t +\mathrm{i}eA_0 = \partial_t - \mathrm{i}e\phi\) ， \(\mathbf{D} = \nabla +\mathrm{i}e\mathbf{A}\) （使用 \((-,+,+,+)\) 度规约定）。

化简得

\[\mathrm{i} \begin{bmatrix}D_t\psi_1 \\ -D_t\psi_2\end{bmatrix} +\mathrm{i} \begin{bmatrix}\bm\sigma\cdot \mathbf{D} \psi_2 \\ -\bm\sigma\cdot \mathbf{D}\psi_1\end{bmatrix} -m \begin{bmatrix}\psi_1 \\ \psi_2\end{bmatrix}=0\]

即

\[\boxed{ \begin{aligned} \mathrm{i} D_t \psi_1 + \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi_2 - m\psi_1 &= 0 \\ -\mathrm{i} D_t \psi_2 - \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi_1 - m\psi_2 &= 0 \end{aligned}  }\quad (\star)\]

这就是狄拉克方程的展开形式：我们把电子项 \(\psi_1\) 和正电子项 \(\psi_2\) 写成两个方程。原来它们在同一个方程里。

我们还可以进一步把它们分别展开成两个方程，对应两种自旋。不过由于我们比较熟悉泡利算符，所以就没必要这么做了。

到此为止，我们还没有做任何近似。从下一节开始，我们对狄拉克方程做低能近似。

### 2.3 低能有效哈密顿量  

在低能情形下，我们不考虑电子静质量带来的相位变化 \(\mathrm{e}^{-\mathrm{i}mt}\) ，因此我们把它分离出来，也就是把 \(\psi = \begin{bmatrix}\psi_1\\ \psi_2\end{bmatrix}\) 换成 \(\psi = \begin{bmatrix}\varphi \mathrm{e}^{-\mathrm{i}mt}\\ \chi  \mathrm{e}^{-\mathrm{i}mt}\end{bmatrix}\) ，代入展开后的狄拉克方程 \((\star)\) 得：

\[\begin{aligned} &\mathrm{i} D_t \varphi + \mathrm{i} \bm\sigma \cdot \mathbf{D} \chi  = 0 &(1)\\ -&\mathrm{i} D_t \chi - \mathrm{i} \bm\sigma \cdot \mathbf{D} \varphi - 2m\chi = 0 &(2) \end{aligned}\]

由于低能情形下正电子项 \(\chi\) 很小，所以 \(D_t \chi \approx 0\) ，代入 \((2)\) 得：

\[\chi \approx - \frac{\mathrm{i}}{2m} \bm\sigma \cdot \mathbf{D} \varphi\]

将其再代入 \((1)\) 得：

\[\mathrm{i} D_t \varphi +  \frac{1}{2m}(\bm\sigma \cdot \mathbf{D})^2 \varphi = 0 \]

可以证明（见附录）

\[\begin{aligned} (\bm \sigma \cdot \mathbf{D})^2 &=\mathbf{D}^2 - \mathrm{i}e \bm\sigma\cdot \mathbf{B} \\ &= (\nabla +\mathrm{i}e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B} \\ &= -(\mathbf{p} + e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B}  \end{aligned}\]

所以

\[\mathrm{i} D_t \varphi =  \frac{1}{2m}[(\mathbf{p} + e\mathbf{A})^2 + e \bm\sigma\cdot \mathbf{B} ] \varphi\]

把 \(D_t = \partial_t - \mathrm{i}e\phi\) 代入得

\[\boxed{ \mathrm{i} \partial_t \varphi =  \left[\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2+ \frac{e}{2m} \bm\sigma\cdot \mathbf{B}  - e\phi  \right]\varphi }\]

这就是（带自旋的）电子的薛定谔方程，也叫做泡利方程。注意此处 \(e\) 是正数，而电子 \(\varphi\) 带负电荷。

于是我们可以定义电子的有效哈密顿量为：

\[\boxed{ H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2- \frac{e}{2m} \bm\sigma\cdot \mathbf{B}  - e\phi   }\]

由于磁场比电场弱很多 \(B\sim E/c\) 。哈密顿量中与磁场有关的项 （ \(\frac{e}{2m} \bm\sigma\cdot \mathbf{B}\) ）的数量级是电场有关项（ \(e\phi\) ）的 \(\alpha\approx \frac{1}{137}\) 倍。所以在通常的哈密顿量 \(H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2 - e\phi  \) 中我们可以忽略自旋项 \(\frac{e}{2m} \bm\sigma\cdot \mathbf{B}\) 。

可见，**量子场论的低能极限就是量子力学**。

> 我们知道，在氢原子中解无自旋的薛定谔方程，得到的结果需要精细结构修正。这些修正一共有三项：自旋-轨道耦合、相对论动能修正、以及 Darwin 项。其中动能修正项来自于质能关系 \(E^2 = p^2 +m^2\) ，Darwin 项来自于电子项和正电子项之间的干涉（也可以理解成虚电子-正电子对的涨落），自旋-轨道耦合，顾名思义，来自于电子的自旋，而这已经被泡利方程考虑进来了。   
>   
> 因此，在氢原子中解泡利方程，可以得到自旋-轨道耦合的更正项。但仍然得不到相对论动能修正项和 Darwin 项。如果想要同时得到这三个精细结构更正项，还是需要量子场论和狄拉克方程才可以。   
>   
> 另外，还有一个修正项与精细结构修正的数量级相同，它叫做 Lamb shift（兰姆位移），来自于电磁场（虚光子）的涨落，而非电子-正电子对的涨落。

---

## 三、长波近似、偶极子表象  

现在我们考虑光场与原子内电子的相互作用。我们首先要做的近似是**玻恩-奥本海默近似**，也就是把原子实和电子的哈密顿量解耦，从而可以只考虑电子的哈密顿量。这是因为电子运动比原子实快得多，导致我们可以把原子实受到的力看做一个平均作用力；反过来，我们可以把电子看成在一个不变的背景库仑势中运动。接下来，我们做一系列其他近似。

### 3.1 长波近似（偶极子近似）  

由于玻尔半径（~50pm）远小于光学波长（~500nm），我们可以不考虑原子内光场的横场的梯度，也就是将哈密顿量 \(H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2 - e\phi  + H_\text{EM}\) 中的 \(\mathbf{A}(\mathbf{x})\) 换成只与时间有关的场 \(\mathbf{A}(\mathbf{0})\) 。其中 \(H_\text{EM}=\sum_{\mathbf{k,\sigma}} \omega_{\mathbf{k,\sigma}}\left(a_{\mathbf{k,\sigma}}^\dagger a_{\mathbf{k,\sigma}} + \frac{1}{2}\right)\) 是光场的横场的哈密顿量。

把 \(\mathbf{x}=\mathbf{0}\) 代入

\[\mathbf{A}(\mathbf{x}) = \sum_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega_\mathbf{k}V}} \left[ a_{\mathbf{k},\sigma} \bm{\epsilon}_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}\mathbf{k}\cdot \mathbf{x}} + \text{h.c.} \right]\]

得

\[\mathbf{A}(\mathbf{0}) = \sum_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega_\mathbf{k}V}} \left(a_{\mathbf{k},\sigma} + a^\dagger_{\mathbf{k},\sigma}\right) \bm{\epsilon}_{\mathbf{k},\sigma} \]

这个近似也叫偶极子近似，因为这个近似也等价于在多极近似（multipole expansion）中忽略高阶项（四极子、八极子等等）。

### 3.2 偶极子表象  

定义偶极子（dipole）算符为 \(\mathbf{d}=-e\mathbf{x}\) （ \(e\) 为正数， \(\mathbf{x}\) 为电子相对于原子核的位置），并且做幺正变换

\[\boxed{U=\exp\left[ -\mathrm{i}\mathbf{d}\cdot \mathbf{A}(\mathbf{0})\right]} = \exp\left[ \sum_{\mathbf{k},\sigma} (\lambda _{\mathbf{k,\sigma}} a_{\mathbf{k,\sigma}}^\dagger - \lambda_{\mathbf{k,\sigma}}^* a_{\mathbf{k,\sigma}} )\right] = \prod_{\mathbf{k,\sigma}} D_{\mathbf{k,\sigma}}(\lambda_{\mathbf{k,\sigma}})\]

其中 \(\lambda_{\mathbf{k,\sigma}} = -\mathrm{i}\mathbf{d}\cdot \epsilon_{\mathbf{k,\sigma}}\) ， \(D_{\mathbf{k,\sigma}}(\alpha) = \exp( \alpha a^\dagger_{\mathbf{k,\sigma}} - \alpha a_{\mathbf{k,\sigma}})\) 为 \(({\mathbf{k,\sigma}})\) 模式上的平移算符。

可以证明[[1]](#ref\_1)，新表象下的哈密顿量为：

\[\boxed{ H \mapsto U^\dagger H U = \frac{1}{2m}\mathbf{p}^2 - e\phi  +\mathbf{d}\cdot \mathbf{E}_\perp(\mathbf{0}) + H_\text{EM}+ H_{\text{dip}} } \quad (3)\]

其中 \( \mathbf{E}_\perp(\mathbf{0}) = \sum_{\mathbf{k,\sigma}} \mathrm{i} \sqrt{\frac{\omega_k}{2V}} (a_{\mathbf{k,\sigma}} - a^\dagger_{\mathbf{k,\sigma}}) \epsilon_{\mathbf{k,\sigma}}\) 是电场的横场部分， \(H_{\text{dip}} = \sum_{\mathbf{k,\sigma}} \frac{1}{2V} (\epsilon_{\mathbf{k,\sigma}} \cdot \mathbf{d})^2\) 为偶极子的自能，通常可以忽略。

这个表象叫做 \(\mathbf{d}\cdot\mathbf{E}\) 表象，也叫偶极子表象。而原来的表象叫做 \(\mathbf{p}\cdot \mathbf{A}\) 表象。

### 3.3 二能级近似  

现在我们将原子简化为一个二能级系统（只有基态和激发态），也就是将原子的哈密顿量 \(\frac{1}{2m}\mathbf{p}^2 - e\phi\) 简化为 \(H_{\text{atom}} = \frac{\omega_{ab}}{2} \sigma_z\) ，其中 \(\omega_{ab}\) 是能级差， \(\sigma_z = |b\rangle\langle b| - |a\rangle\langle a|\) ， \(|b\rangle\) 是激发态， \(|a\rangle\) 是基态。

二能级之间的跃迁对光场的偏振态有要求（选择定则），于是我们可以只考察对应的偏振态 \(\sigma\) 。这使得我们可以把 \(\mathbf{d} \cdot \mathbf{E}_{\perp}(\mathbf0)\) 写成 \(dE_\perp(0)\) 。

另外，还需要将偶极子算符投影到二能级子空间里： \(d\mapsto (|a\rangle\langle a| + |b\rangle\langle b| ) d = d_{ab}|a\rangle\langle b| + d_{ba} |b\rangle \langle a|\) 。其中 \(d_{ba} = d_{ab}^*\) 。

> 之所以没有 \(d_{aa} |a\rangle \langle a|\) 项是因为 \(d_{aa} =-e \int \langle \psi_a|\mathbf{x}|\psi_a\rangle =-e\int\psi^*(\mathbf{x})\ \mathbf{x}\ \psi(\mathbf{x})\mathrm{d}^3\mathbf{x}= 0\) 。类似也有 \(d_{bb}=0\) 。

我们总是可以选取相位 \(d_{ab} \mapsto d_{ab}\mathrm{e}^{\mathrm{i}\theta}\) 使得 \(d_{ab} = d_{ba}\) 是实数。于是偶极子算符可以写成：

\[\boxed{ d=d_{ab}(\sigma_+ +\sigma_-) }\]

其中 \(\sigma_+ = |b\rangle\langle a|,\ \sigma_-=|a\rangle\langle b|\) 。

而电场算符可以写成：

\[E_\perp(\mathbf{0}) = \sum_{\mathbf{k}} \mathrm{i} \sqrt{\frac{\omega_k}{2V}} (a_{\mathbf{k}} - a^\dagger_{\mathbf{k}}) \]

我们可以把虚数因子 \(\mathrm{i}\) 吸收进湮灭/产生算符中： \(a_{\mathbf{k}} \mapsto \mathrm{i}a_\mathbf{k}, \ a_{\mathbf{k}}^\dagger \mapsto -\mathrm{i}a_{\mathbf{k}}^\dagger\) 。于是有

\[\boxed{ E_\perp(\mathbf{0}) = \sum_{\mathbf{k}} \sqrt{\frac{\omega_k}{2V}} (a_{\mathbf{k}} +a^\dagger_{\mathbf{k}})  }\]

将这些关系代入偶极子表象的哈密顿量 \((3)\) ，并且忽略偶极子自能，得到：

\[\boxed{ H =  \frac{\omega_{ab}}{2} \sigma_z +\sum_{\mathbf{k}} g_{\mathbf{k}}(\sigma_+ +\sigma_-)(a_{\mathbf{k}} +a^\dagger_{\mathbf{k}}) + H_\text{EM} }\]

其中 \(g_{\mathbf{k}}=d_{ab}\sqrt{\frac{\omega_k}{2V}} \) 是二能级系统与光场的耦合强度。

### 3.4 腔量子电动力学（Cavity QED）  

现在考虑把原子放在一个很小的腔里，腔长 \(\sim 100 \mu \text{m}\) ，则自由光谱区为 \(c/(2L)\sim 1.5 \text{THz}\) ，也就是说相邻模式的频率差为 \(\sim 1.5 \text{THz}\) ，远大于自然线宽 \(\sim 10 \text{MHz}\) 和耦合强度 \(g\sim 100\text{MHz}\) 。这使得我们可以选择出单个光场模式与二能级原子相互作用。这样一来，其他光场模式的失谐量 \(\Delta =\omega_\mathbf{k}-\omega_{ab}\) 就很大，可以忽略。

于是我们就得到了单个光场与原子中单个电子的相互作用哈密顿量：

\[\boxed{ H =  \frac{\omega_{ab}}{2} \sigma_z +g(\sigma_+ +\sigma_-)(a +a^\dagger) + \omega\left(a^\dagger a +\frac{1}{2}\right) }\]

其中 \(g = g_{\mathbf{k}}\) ， \(\omega=\omega_\mathbf{k}\) 是选择出来的光场的耦合强度和频率。

在腔中还有一个好处，就是耦合强度 \(g_{\mathbf{k}}=d_{ab}\sqrt{\frac{\omega_k}{2V}} \) 比较强，因为模式体积 \(V\) 很小。

由于 \(\sigma_+ a^\dagger\) 代表产生一个光子，并且电子从低能级跃迁到高能级，所以它的概率很低 \(\sim\frac{1}{\omega+\omega_{ab}}\) ，可以忽略。类似地， \(\sigma_-a\) 也可以忽略。这叫做旋转波近似（Rotating Wave Approximation，RWA）。

做旋转波近似之后，我们就得到了 Jaynes-Cummings 哈密顿量：

\[\boxed{ H =  \frac{\omega_{ab}}{2} \sigma_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger)  }\]

Jaynes-Cummings 模型有[解析解](https://zhuanlan.zhihu.com/p/701838204)，这些解叫做缀饰态（dressed states）。由于篇幅所限不作介绍。

## 尾声：物理的魅力  

我们从 QED 拉氏量出发：

\[\begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi - eA_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \end{aligned} \]

这个拉氏量非常复杂：它不仅考虑了电子的反粒子——正电子，并且耦合项 \(- eA_\mu \bar{\psi} \gamma^\mu \psi\) 还是一个三次项，可以描述电子-正电子对产生/湮灭等多种过程。三次项的存在导致它没有解析解，只能用量子场论的微扰法求解。

但经过一系列简化和近似（低能近似、玻恩-奥本海默近似，长波/偶极子近似、二能级近似、旋转波近似）之后，我们竟然得到了一个有解析解的模型！

\[H =  \frac{\omega_{ab}}{2} \sigma_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger) \]

可见，根据所考虑的情况，我们做出了一系列适当和必要的简化，从而在纷复繁杂的现象中抓住本质，最终能够更好地认识世界。

这样的方法论不仅可以用到物理中，而且可以泛化到其他学科。

这就是物理的魅力。

---

【更高更妙的电动力学】系列到此结束。希望你觉得这趟旅途愉快！

## 附录  

证明 \((\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B}\) ，其中 \(\mathbf{D} = \nabla+ \mathrm{i}e\mathbf{A}\) 。

> 根据恒等式  
>   
>  \((\bm\sigma \cdot \mathbf{a})(\bm\sigma \cdot \mathbf{b}) = \mathbf{a} \cdot \mathbf{b} + \mathrm{i}\bm\sigma \cdot(\mathbf{a}\times\mathbf{b})\)   
>   
> 得  
>   
>  \((\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D})\)   
>   
> 于是我们需要计算 \((\mathbf{D}\times\mathbf{D})\) 。   
>   
> 我们先计算 \([D_i, D_j]\) ：   
>   
>  \(\begin{align} [D_i, D_j] &= [\partial_i +\mathrm{i}eA_i, \partial_j +\mathrm{i}eA_j] \\ &= \cancel{[\partial_i,\partial_j]} + \cancel{e^2[A_i, A_j]} + \mathrm{i}e[\partial_i, A_j] - \mathrm{i}e[\partial_j,A_i] \end{align}\)   
>   
> 于是我们需要计算 \([\partial_i, A_j]\) ：  
>   
>  \(\begin{align} [\partial_i, A_j] f &= \partial_i (A_j f) -A_j \partial_i f \\ &= (\partial_i A_j) f + A_j \partial_if - A_j \partial_i f \\ &= (\partial_iA_j)f \end{align}\)   
>   
> 所以 \([\partial_i, A_j] = (\partial_i A_j)\) 。   
>   
> 于是  
>   
>  \(\begin{align} [D_i, D_j] &= \mathrm{i}e[\partial_i, A_j] -\mathrm{i}e[\partial_j,A_i] \\ &= \mathrm{i}e (\partial_i A_j - \partial_j A_i) \\ &= \mathrm{i}e \epsilon_{ijk}B^k \end{align}\)   
>   
> 于是  
>   
>  \(\begin{aligned} (\mathbf{D}\times\mathbf{D})^k &=\epsilon^{kij} D_i D_j \\ &= \frac{1}{2} \epsilon^{kij}[D_i,D_j] \\ &= \frac{\mathrm{i}e}{2} \epsilon^{kij} \epsilon_{ijl} B^l \\ &= \frac{\mathrm{i}e}{2} (\delta^k_l \delta^j_j - \delta^k_j\delta^j_l) B^l \\ &=\mathrm{i}e \delta^k_l B^l \\ &= \mathrm{i}eB^k \end{aligned}\)   
>   
> 所以 \(\mathbf{D}\times \mathbf{D} = \mathrm{i}e\mathbf{B}\) 。   
>   
> 于是  
>   
>  \(\begin{aligned} (\bm\sigma \cdot \mathbf{D})^2 &= \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D}) \\ &= \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B} \end{aligned}\)   
>   
> 证毕。

## 参考  

1. ^[a](#ref\_1\_0)[b](#ref\_1\_1)Atom-Photon Interactions by Cohen-Tannoudji [https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197)
