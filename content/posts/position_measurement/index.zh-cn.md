---
title: "位置测量的塌缩态"
date: 2024-05-27T17:49:27+08:00
draft: false
tags: ["量子测量理论"]
categories: ["量子信息"]
---

一般理性告诉我们，实际的位置测量不会产生 delta 函数，因为 delta 函数本身是病态的。那么实际的位置测量的坍缩态应该长什么样呢？

---

太长不看版：

设待测系统的波函数为 $\varphi(x)$ ，则坍缩后的波函数为：

$\varphi^{(q)}(x) = \mathcal{A}\psi(q-gx) \varphi(x)$ 

其中 $\psi(x)$ 是仪器指针的初态波函数。 $q$ 是仪器指针的读数。 $g$ 是仪器和待测系统之间的耦合强度。$\begin{aligned} \mathcal{A} = \left[\int\_\mathbb{R}\psi(q-gx) \varphi(x)\right]^{-1} \end{aligned}$ 是合适的归一化常数。

## 一、前置知识  
### 1.1 符号约定  
$L^2(\mathbb{R})$ ： $\mathbb{R}$ 上平方可积函数构成的希尔伯特空间。

$\mathcal{L}(\mathcal{H})$ ：希尔伯特空间 $\mathcal{H}$ 上的（有界）算符。

$\mathbb{I}\_{\mathcal{H}}$ ：希尔伯特空间 $\mathcal{H}$ 上的恒等算符。

$\mathcal{E}(\mathcal{H})$ ：希尔伯特空间 $\mathcal{H}$ 上的 effect。定义为 $\mathcal{E}(\mathcal{H}) := \\\\{ E\in \mathcal{L}(\mathcal{H}) | E =E^\*, 0 \le E\le \mathbb{I}\_{\mathcal{H}}\\\\}$ 。

$\text{Leb}(\mathbb{R})$ ： $\mathbb{R}$ 上的 Lebesgue sigma algebra。

### 1.2 量子信息的一些基础知识  
1) PVM（投影测量）与 POVM

2) Quantum channel 及其对偶


> 我不打算在此处详细介绍它们。维基百科或数学教科书已经有详尽的介绍，请自行参阅。也可以看我的文章：[https://zhuanlan.zhihu.com/p/679038823](https://zhuanlan.zhihu.com/p/679038823)

### 1.3 测度、勒贝格积分  
位置和动量算符的谱是连续的。数学上严格 formulate 连续的谱需要测度和勒贝格积分。


> 我不打算在此处详细介绍它们。维基百科或数学教科书已经有详尽的介绍，请自行参阅。

另外，PVM 和 POVM 中的字母 M 指的就是测度（Measure）。量子力学建立在概率论的基础上，概率论建立在测度论的基础上。所以关于测度的知识是必要的。

### 1.4 位置与动量算符的谱分解  
$L^2(\mathbb{R})$ 上的位置算符 $Q \in \mathcal{L}(L^2(\mathbb{R}))$ 有谱分解： $Q = \int\_\mathbb{R} x\mathsf{Q}(\mathrm{d}x)$ 。这是一个勒贝格积分。

其中 $\mathsf{Q}$ 是位置投影测量，即 PVM（Projection Valued Measure，是 POVM，Positive Operator Valued Measure 的特例），它定义为一个 operator-valued 的测度： $\mathsf{Q}: \text{Leb}(\mathbb{R}) \rightarrow \mathcal{E}(L^2(\mathbb{R}))$ ，$\[\mathsf{Q}(A) \varphi\](x):=\chi\_A(x) \varphi(x)$，其中 $\chi\_A(x)=\begin{cases} 1, \quad x\in A \\\\ 0, \quad x \notin A \end{cases}$ 是集合 $A$ 的特征函数。


> 选读：动量 PVM 可以定义为 $\mathsf{P}(A) = F^\* \mathsf{Q}(A) F$ ，其中 $F$ 是 Fourier-Plancherel 算子 $\mathcal{F} \in \mathcal{L}(L^2(\mathbb{R}))$ ，定义为：  
> $(\mathcal{F}\varphi)(p)=\frac{1}{\sqrt{2\pi}}\int\_{\mathbb{R}}\mathrm{e}^{-ipx}\varphi(x)\mathrm{d}x$ 

## 二、测量模型  
本节的整体思路如下：

考虑一个待测系统，其希尔伯特空间为 $\mathcal{H}$ ，状态为 $\rho$ 。接着我们将系统 $\mathcal{H}$ 和另一个系统 $\mathcal{K}$ 耦合到一起。可以将 $\mathcal{K}$ 想象成一个仪器上面的指针，可以给出不同的读数。假设系统 $\mathcal{K}$ 的初态为 $\sigma$ ，于是复合系统的初态为 $\rho \otimes \sigma \in \mathcal{H} \otimes \mathcal{K}$ 。

然后，我们让复合系统演化一段时间，于是系统状态变为 $U(\rho\otimes \sigma) U^\dag$ 。

最后，我们对辅助系统 $\mathcal{K}$ 进行 PVM $\mathsf{Z}$ 所给出的测量，根据玻恩规则，得到结果 $x$ 的概率为 $\operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z(x)})]$ 。

这样，我们就实现了一个 POVM $\mathsf{E}$ ，满足 $\operatorname{tr}[\rho \mathsf{E(x)}]=\operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z(x)})]$ 。

定义 $\mathcal{I}\_x(\rho) :=\operatorname{tr}\_\mathcal{K}[\rho \mathsf{E(x)}]=\operatorname{tr}\_\mathcal{K}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z(x)})]$ ，它是测量过程所诱导的 quantum channel。如果我们找到 quantum channel 的 Kraus operator $K\_i$ 使得 $\mathcal{I}\_x(\rho) :=\sum\_i K\_i \rho K\_i^\*$ ，就可以很容易求出 $\mathcal{I}\_x$ 的对偶 channel $\mathcal{I}\_x^\*: \mathcal{I}\_x^\*(\mathcal{M}) =  \sum\_i K\_i^\* \mathcal{M} K\_i$ ，于是测量后的坍缩态就是 $\mathcal{I}\_x^\*(\mathbb{I\_\mathcal{H}}) =  \sum\_i K\_i^\* K\_i$ 。

以上是整体思路，下面我们给出具体计算过程。

### 2.1 待测系统和仪器的哈密顿量  
考虑待测量的系统 $\mathcal{H}$ 和仪器 $\mathcal{K}$ ，且 $\mathcal{H} \cong \mathcal{K} \cong L^2(\mathbb{R})$ ，即 $\mathcal{H}$ 和 $\mathcal{K}$ 都是 $\mathbb{R}$ 上平方可积函数构成的希尔伯特空间。可以将 $\mathcal{K}$ 想象成一个仪器上面的指针，可以给出不同的读数。

为了测量 $|\psi\rangle\in \mathcal{H}$ 的位置，我们需要仪器与待测系统耦合起来，并演化一段时间。

这个演化过程的哈密顿量为 $U =e^{-\mathrm{i} g Q\otimes P}$ 。其中 $Q$ 是 $\mathcal{H}$ 上的位置算符， $P$ 是 $\mathcal{K}$ 上的动量算符， $g$ 是耦合强度（已经将演化时间 $t$ 吸收进去）。这个哈密顿量不难理解，因为仪器的指针需要在表盘上移动以给出不同的读数，而平移的生成元就是动量算符。因此直观来看， $U$ 可以理解为根据 $|\psi\rangle\in \mathcal{H}$ 的位置生成 $\mathcal{K}$ 上的平移。

### 2.2 演化  
根据谱分解 $Q = \int\_{\mathbb{R}} x\mathsf{Q}(\mathrm{d}x)$ ，我们可以把 $U$ 写成：

$U = \int\_\mathbb{R} \mathsf{Q}(\mathrm{d}x) \otimes e^{-\mathrm{i}g x P}$ 

设 $\mathcal{H}$ 和 $\mathcal{K}$ 的初态分别为 $\rho$ 和 $\sigma = |\psi\rangle\langle\psi|$ ，那么演化后的量子态为：

$\tau = U(\rho \otimes \sigma) U^\*=\int\_{\mathbb{R}^2} \mathsf{Q}(\mathrm{d}x) \rho \mathsf{Q}(\mathrm{d}y) \otimes e^{-\mathrm{i} g x P} |\psi\rangle\langle \psi | e^{-\mathrm{i} g y P}$ 

### 2.3 测量诱导的 Quantum channel 和 POVM  
此时对系统 $\mathcal{K}$ 进行位置测量会给出如下的 quantum channel：

$ \mathcal{I}\_{A}(\rho)  =\text{tr}\_\mathcal{K}[\tau(\mathbb{I}\_\mathcal{H} \otimes \mathsf{Q}(A)) ] $ 

计算得：

$\begin{aligned} \mathcal{I}\_{A}(\rho) &= \text{tr}\_\mathcal{K}[\tau(\mathbb{I}\_\mathcal{H} \otimes \mathsf{Q}(A)) ] \\\\  &=\text{tr}\_\mathcal{K}[U(\rho \otimes \sigma) U^\*(\mathbb{I}\_\mathcal{H} \otimes \mathsf{Q}(A)) ] \\\\ &= \int\_{\mathbb{R}^2} \langle e^{-\mathrm{i}g y P} \psi | \mathsf{Q}(A)|e^{-\mathrm{i}g x P }\psi \rangle \mathsf{Q}(\mathrm{d}x) \rho \mathsf{Q}(\mathrm{d}y) \\\\ &= \int\_A \int\_{\mathrm{R}^2} \psi(q-gy)^\*\psi(q-gx) \mathsf{Q}(\mathrm{d}x) \rho \mathsf{Q}(\mathrm{d}y) \mathrm{d}q \\\\ &= \int\_A K(q) \rho K(q)^\* \mathrm{d}q \end{aligned}$ 

其中 $K(q) := \int\_{\mathrm{R}} \psi(q - gx)\mathsf{Q}(\mathrm{d}x)$ 是 $\mathcal{I}\_A$ 的 Kraus operator，即 $[K(q) \varphi] (x) := \psi(q - gx) \varphi(x)$ 。

这个 quantum channel 诱导了一个 $\mathcal{H}$ 上的 POVM：

$\mathsf{E}(A) = \mathcal{I}\_A^\*(\mathbb{I}\_\mathcal{H}) = \int\_A K(q)^\* K(q) \mathrm{d}q = \int\_A\int\_\mathbb{R} |\psi(q - gx)|^2 \mathsf{Q}(\mathrm{d}x) \mathrm{d}q$ 

可以看出，这个测量并不是将量子态坍缩到一个 delta 函数上，而是将 delta 函数与仪器 $\mathcal{K}$ 的初态做了一个卷积，而仪器的初态 $|\psi\rangle \in\mathcal{K}$ 肯定不是一个 delta 函数。所以此时的 POVM 是一个\*\*“被展宽”的测量\*\*。这个展宽来源于仪器探针态本身的展宽。

### 2.4 坍缩后的态  
此时，在 $\mathcal{I}\_{A}(\rho)$ 中令 $A=\{q\}$ ，得到待测系统 $\mathcal{H}$ 的量子态坍缩为 $\frac{K(q) \rho K(q)^\*}{\text{tr}[K(q) \rho K(q)^\*]}$ ，其中 $q$ 是仪器的读数。

当 $\rho = |\varphi\rangle\langle\varphi|$ 是纯态时，其坍缩后的波函数为：

$\varphi^{(q)}(x) = \mathcal{A}\psi(q-gx) \varphi(x)$ 

其中 $\begin{aligned} \mathcal{A} = \left[\int\_\mathbb{R}\psi(q-gx) \varphi(x)\right]^{-1} \end{aligned}$ 是合适的归一化常数。其中 $q$ 是探针的读数。

如果探针态是一个“展宽”的高斯波包： $\psi(x) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left[-\frac{x^2}{2\sigma^2}\right]$ ，那么

$\varphi^{(q)}(x) = \mathcal{A} \exp\left[-\frac{(gx-q)^2}{2\sigma^2}\right] \varphi(x)$ 

这个几何意义已经非常直观了。


> 特别地，如果探针态本身就是 delta 函数 $\psi(x) = \delta(x)$ ，那么测量后的态坍缩为  
>  $\varphi^{(q)}(x) = \delta(x-\frac{q}{g})$   
> 同样是一个 delta 函数。

### 2.5 测量模型  
以上的分析过程十分有用。我们可以把它抽象为一个测量模型（Measurement model）： $\mathfrak{M}=(\mathcal{K},\sigma,U,\mathsf{Z})$ 。

其中 $\mathcal{K}$ 是辅助系统（可以理解为仪器）， $\sigma$ 是系统 $\mathcal{K}$ 的初态， $U$ 是整体系统 $\mathcal{H} \otimes \mathcal{K}$ 的演化 ， $\mathsf{Z}$ 是对辅助系统的投影测量（PVM）。这些物理对象实现了一个 $\mathcal{H}$ 上的 POVM 测量。

在实际实验中，辅助（ancilla）系统 $\mathcal{K}$ 可以看作是仪器的探针，而 $\mathsf{Z}$ 就是对探针进行读数。

## 三、量子-经典过渡  
最后，你可能想问：测量之后，探针态坍缩成什么态了？这是一个很有趣的问题。

因为我们对于仪器探针位置的测量使用的是 PVM $\mathsf{Q}$ ，所以探针态似乎应该坍缩成 delta 函数。如此一来，以上分析似乎仅仅是把一个问题变成另一个问题。即：把待测系统量子态如何坍缩的问题，变成了仪器探针态如何坍缩的问题。

但在实验上，我们的仪器是宏观的经典系统，而不是一个量子系统，因此实际的情况更加复杂。如果你了解一些 POVM 与量子测量模型的知识，你就会知道：（非 PVM 的）POVM 本身只能给出测量结果的概率。坍缩后的态具体是什么，只能由一个测量模型给出，而这个测量模型必然会涉及到一个辅助系统 $\mathcal{K}$ 。如果你想要知道 $\mathcal{K}$ 的量子态，你就要用另外一个系统 $\mathcal{M}$ 去测量系统 $\mathcal{K}$ ，如此往复下去。这种循环往复的过程就是从量子到经典过渡的过程。从量子到经典的过渡涉及到 measurement problem，是量子力学悬而未决的问题，我不想在这里过多地讨论它。有兴趣的读者可以自行搜索文献深究。

如此一来，测量模型似乎和退相干一样，都是看似解决了 measurement problem，实则没有解决。即便如此，它们还是能为我们提供很多 insight。


> 当然，以上说的只是连续谱的可观测量的问题。对于离散谱的可观测量而言，实验上很好实现 PVM。PVM 可以直接给出测量后的态，且这个态性质良好，不存在 delta 函数那样的不良性质。

## 四、经典仪器  
为了避免上面说到的问题，我们可以定义一个 course-grained 的经典仪器，它只能区分粒子在或不在某一个区间内：

$\mathsf{Z}: \\{0,1\\} \rightarrow \mathcal{E}(L^2(\mathbb{R}))$ 

$\mathsf{Z}(1) = \int\_a^b \mathsf{Q}(\mathrm{d}x)$ 

$\mathsf{Z}(0) = \mathbb{I}\_{L^2(\mathbb{R})} - \int\_a^b \mathsf{Q}(\mathrm{d}x)$ 

又或者是以一定精度 $g$ 区分粒子的位置：

$\mathsf{Z}: \mathbb{Z} \rightarrow \mathcal{E}(L^2(\mathbb{R}))$ 

$\mathsf{Z}(n) =\int\_{gn}^{g(n+1)} \mathsf{Q}(\mathrm{d}x)$ 

注意到它们都是 PVM，因此坍缩后的态也可以确定下来。

这两种情况的计算留给读者作为练习。

