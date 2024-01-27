---
title: "傅里叶变换的Parseval定理既然表示了一种守恒律，那么与之对应的对称性是什么？"
date: 2024-01-26T23:49:29+08:00
draft: false
tags: ["对称性"]
categories: ["数学物理方法"]
---

**Link:** [https://www.zhihu.com/question/640869828/answer/3373753127]

抛砖引玉一下。

## Fourier-Plancherel 算子  
定义 Fourier-Plancherel 算子 $\mathcal{F} \in \mathcal{L}(L^2(\mathbb{R}))$ 为：

$(\mathcal{F}\varphi)(p)=\frac{1}{\sqrt{2\pi}}\int\_{\mathbb{R}}\mathrm{e}^{-ipx}\varphi(x)\mathrm{d}x$ 

它实际上是个酉算子：

$\mathcal{F}^\dag\mathcal{F}=\mathbb{I}\_{L^2(\mathbb{R})}$ 

而 Parseval 定理无非就是这一事实的重新表述：

$\langle\varphi \mathcal{F}^\dag|\mathcal{F\varphi}\rangle=\langle\varphi|\mathcal{F}^\dag\mathcal{F}|\varphi\rangle=\langle\varphi|\varphi\rangle=1$ 

这个定理似乎并未涉及到任何物理量的守恒？

当然，我也可以说“恒等算子”对应的物理量守恒（也就是概率守恒）。

$\langle\varphi|\mathcal{F}^\dag\mathbb{I}\_{L^2(\mathbb{R})}\mathcal{F}|\varphi\rangle=\langle\varphi|\mathbb{I}\_{L^2(\mathbb{R})}|\varphi\rangle=1$ 

这是因为 $[\mathcal{F},\mathbb{I}\_{L^2(\mathbb{R})}]=0$ 。

但是所有算子都和恒等算子对易，所以这没有什么特别的。

## Fourier-Plancherel 算子的一些性质  
**性质 1：** $\mathcal{F}^\dag Q\mathcal{F} = P$ ， $\mathcal{F}P\mathcal{F}^\dag  = Q$

其中 $Q$ 和 $P$ 分别是位置和动量算子，定义为：

$(Q\varphi)(x)=x\varphi(x)$ 

$(P\varphi)(x) = -\mathrm{i}\varphi^\prime(x)$ 

**性质 2：** $\mathcal{F}^2=(\mathcal{F}^*)^2=\mathcal{P}$ 

其中 $\mathcal{P}$ 是宇称算子，定义为：

$(\mathcal{P}\varphi)(x)=\varphi(-x)$ 

**性质 3：** $\mathcal{F}^4=\mathbb{I}\_{L^2(\mathbb{R})}$ 

这是因为 $\mathcal{P}^2=\mathbb{I}\_{L^2(\mathbb{R})}$ 

## 守恒量  
我们知道宇称守恒所对应的对称性是宇称对称，即哈密顿量在宇称变换下不变。

作为复习，下面简单推导一下宇称守恒。

宇称变换用宇称算子 $\mathcal{P}$ 来表示。

哈密顿量在宇称变换下不变，用公式写出来就是：

$\mathcal{P}\mathcal{H}\mathcal{P}^\dag=\mathcal{H}$ 

或

$[\mathcal{H},\mathcal{P}]=0$ 

此时有：

$\frac{\mathrm{d}}{\mathrm{d}t}\langle \mathcal{P} \rangle = \frac{\mathrm{i}}{\hbar}\langle[\mathcal{H},\mathcal{P}]\rangle = 0$ 

即宇称守恒。

那么 Fourier-Plancherel 算子 $\mathcal{F}$ 有没有对应的守恒量呢？很遗憾， $\mathcal{F}$ 并非一个可观测量，因为它不是一个自伴算子。


> 不过我们可以定义 $\mathcal{G} = \frac{\mathcal{F}+\mathcal{F}^\dag}{2}$ ，这样 $\mathcal{G}$ 就是一个自伴算子了。它对应傅里叶余弦变换。   
>   
> 话说回来，虽然 $\mathcal{F}$ 不是自伴算子，但是它是一个正规算子，也就是说它可以被正交对角化，只不过特征值不一定是实数。   
>   
> 有些作者将可观测量定义为正规算子而非自伴算子。在这个意义下， $\mathcal{F}$ 可以是可观测量。

如果硬要守恒量貌似也不是不可以。假设有一个哈密顿量在 Fourier-Plancherel 变换下不变：

$\mathcal{F}^\dag\mathcal{H}\mathcal{F} = \mathcal{H}$ 

即

$[\mathcal{H},\mathcal{F}]=0$ 

则有：

$\frac{\mathrm{d}}{\mathrm{d}t}\langle \mathcal{F} \rangle = \frac{\mathrm{i}}{\hbar}\langle[\mathcal{H},\mathcal{F}]\rangle = 0$ 

此时 $\langle\mathcal{F}\rangle$ 是守恒量。不过我暂时不清楚这个守恒量有什么意义。

你可能想问满足 $\mathcal{F}^\dag\mathcal{H}\mathcal{F} = \mathcal{H}$ 的哈密顿量是否存在。当然！我们喜闻乐见的谐振子哈密顿量 $\mathcal{H}=P^2+Q^2$ 就满足这一条件，这是因为

$$
\begin{aligned} \mathcal{F}^\dag\mathcal{H}\mathcal{F}&=\mathcal{F}^\dag(P^2+Q^2)\mathcal{F} \\\\ 
&=(\mathcal{F}^\dag P\mathcal{F})^2+(\mathcal{F}^\dag Q\mathcal{F})^2 \\\\
&=(\mathcal{P}^\dag Q\mathcal{P})^2+P^2 \\\\
&=(-Q)^2+P^2 \\\\
&=\mathcal{H} \end{aligned}
$$ 


