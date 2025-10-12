---
title: "量子态的经典阴影（Classical Shadows）"
date: 2025-10-12T20:25:11+08:00
draft: false
tags: ["经典阴影", "Harr 测度"]
categories: ["量子信息"]
---


## 一、量子态层析（Quantum State Tomography）  

目前，人们已经可以制备由成百上千个量子比特所构成的量子态（此处省略二十个参考文献）。

但是我们如何知道制备的量子态 $\rho$ 的确是我们想要的 $\rho$ ？或者更宽泛地说：如何学习一个量子态 $\rho$ 的（部分或者所有）信息？

为了学习量子态 $\rho$ ，我们需要先制备 $\rho$ ，然后在不同的测量基下对其进行测量，得到概率分布函数，最后通过这些概率分布函数去学习 $\rho$ 。这个过程就叫做**量子态层析**。

## 二、全量子态层析  

如果我们的目标是完全重建 $\rho$ ，即学习到 $\rho$ 的全部信息，那么这个过程就叫做**全量子态层析（Full State Tomography，简称 FST）**。

以 $n$ 个 qubit 构成的系统为例，其量子态 $\rho$ 可以写成：

$\begin{aligned} \rho &= \frac{1}{2^n}\sum\_i c\_i P\_i \\\\ &\phantom{==}  P\_i = \sigma\_{i\_1}\otimes \cdots \otimes \sigma\_{i\_n}, \quad i=(i\_1,...,i\_n), \quad i\_k= 0,1,2,3 \\\\ &\phantom{==} \sigma\_0=\mathbb{I},\  \sigma\_1=X,\ \sigma\_2 = Y,\ \sigma\_3=Z  \end{aligned}$

其中 $\sigma\_0=\mathbb{I},\  \sigma\_1=X,\ \sigma\_2 = Y,\ \sigma\_3=Z$ 为单比特的泡利矩阵，并且 $c\_i = \operatorname{tr}[\rho P\_i]$ 。

可见，我们只要测量算符 $P\_i$ 的期望值 $c\_i = \operatorname{tr}[\rho P\_i]$ ，就可以对量子态 $\rho$ 进行 FST。这些 $c\_i$ 叫做泡利系数。

一共有 $4^n - 1$ 个泡利系数要测量，因为 $P\_0 = \mathbb{I}^{\otimes n}$ 为单位矩阵，导致 $c\_{0}$ 总是等于 1。

这种测量方法叫做泡利测量（Pauli Measurements），是人们最常用的方法。

> 注意到实际上只需要 $3^n$ 个测量基，因为其余 $(4^n-3^n-1)$ 个 $P\_i$ 的测量结果是这 $3^n$ 个 $P\_j$ 的测量结果的边缘分布（marginal distribution）。  
>   
> 例如， $\mathbb{I}\otimes Y$ 的测量结果完全可以由 $X \otimes Y$ 的测量结果得到——因为前者的概率分布是后者的概率分布的边缘分布。

本文主要以 $n$ 个 qubit 构成的系统为例，但推广到 qudit 也是很直接的。但本文暂不涉及连续变量系统。

### 2.1 样本复杂度  

前面说过，为了学习量子态 $\rho$ ，我们需要先制备 $\rho$ 的多个样本，然后在不同的测量基下对它们进行测量。于是，一个很直接的问题由之而来：

**对于一个** $d$ **维量子态** $\rho$ **，我们需要多少个样本才能在误差范围** $\epsilon$ **内估计** $\rho$ **？**

> 一个 $d$ 维量子态 $\rho$ 定义为 $d$ 维希尔伯特空间上迹为 1 的半正定算子，通常也叫密度矩阵，由 $D^2-1$ 个实参数刻画。

为了更好理解和阐述这个问题，我们先引入一些术语。我们定义**样本复杂度（sample complexity）**：随着维数 $d$ 增加和误差 $\epsilon$ 降低，所需要样本数 $N$ 也会增长。增长速度 $N \sim O(f(d,\epsilon))$ 就是样本复杂度。

对于单个量子比特（Qubit）而言， $d=2$ ，但对于 $n$ 个量子比特所组成的系统，则是 $d=2^n$ 。对于 $n$ 个 k 维的 qudit，则是 $d=k^n$ 。可见，希尔伯特空间维数是随粒子数的增加而指数级增长的。

接下来我们来看看误差 $\epsilon$ 。刻画两个量子态 $\rho$ 和 $\sigma$ 之间的误差最常用的两个函数是**保真度（Fidelity）** $F(\rho,\sigma)$ 和**迹距离（Trace Distance）** $T(\rho,\sigma)$ ：

$F(\rho,\sigma):=\operatorname{tr}\left[\sqrt{\sqrt{\sigma}\rho\sqrt{\sigma}}\right]^2$   
 $T(\rho,\sigma):=\frac{1}{2}||\rho-\sigma||\_1$

其中 $||\cdot||\_1$ 是 trace norm / 1-norm，定义为 $|| A||\_1 =\operatorname{tr}\left[\sqrt{A^\dagger A}\right]$ 。

保真度越接近 1，迹距离越接近 0，误差就越小。它们满足 ：

$1-\sqrt{F} \le T \le \sqrt{1-F}$

如果以迹距离 $T(\rho,\sigma)$ 作为误差 $\epsilon$ ，那么以保真度计算的误差 $\delta:=1-F$ 则满足 $\delta\ge \epsilon^2$ 。

本文主要使用 $||\rho - \sigma||\_1$ 作为误差。

### 2.2 样本复杂度的上界  

直觉上来看，为了重建量子态 $\rho$ ，样本复杂度随 $d$ 的变化至少是 $\sim d^2$ ，或写成 $\Omega(d^2)$ ，这是因为我们至少需要 $\sim d^2$ 个测量基（POVM）元素，才能使测量基是信息完全（informationally complete）的。另一方面，我们要多次测量从而使估计量逼近真实值。为了使两者的误差小于 $\epsilon$ ，样本复杂度与误差 $\epsilon$ 之间应当是类似于反比的关系 $\sim O(\epsilon^{-m})$ 。

因此，我们猜想，样本复杂度为 $\boxed{ N = O(d^l/\epsilon^m) }$ ，其中 $l \ge 2$ 。接下来，我们来研究不同测量方式下的样本复杂度。

### 2.3 泡利测量的复杂度  

接下来我们给出样本复杂度的一个较为宽松的上界 [1]，它是由前文提到，也是人们最常用的泡利测量（Pauli measurements）给出的。

我们先介绍霍夫丁不等式（Hoeffding's inequality），后面会用到：

> **Hoeffding 不等式**  
> 给定 $N$ 个独立随机变量 $X\_i,\ i=1,...,N$ ，取值范围分别为 $[a\_i,b\_i]$ ，那么它们的和 $S=\sum\_iX\_i$ 满足  
> $\begin{aligned} P(|S-\mathbb{E}(S)| \ge \epsilon) < 2\exp \left[-\frac{2 N^2 \epsilon^2}{\sum\_{i}(b\_i-a\_i)^2}  \right] \end{aligned}$   
> 如果 $X\_1,...,X\_N$ 的分布相同，取值范围为 $[a,b]$ ，并且记均值为 $Y = S/N=\sum\_iX\_i /N$ ，则有  
>  $\begin{aligned} P(|Y-\mathbb{E}(Y)| \ge \epsilon) < 2\exp \left[ -\frac{2 N \epsilon^2}{(b-a)^2} \right] \end{aligned}$

接下来我们运用 Hoeffding 不等式。

> 对于量子态 $\rho = \frac{1}{2^n}\sum\_i c\_i P\_i $ ，我们反复测量算符 $P\_i$ ，取结果的平均值为 $c\_i = \operatorname{tr}[\rho P\_i]$ 的估计量 $\hat{c}\_i$ 。  
>   
> 对 $\hat{c}\_i$ 运用 Hoeffding 不等式，并注意到 $\hat{c}\_i$ 的取值为 $\pm1$ ，有：  
>   
> $P[|\hat{c}\_i-c\_i| > \epsilon\_i] \le 2 \exp \left[-N\epsilon\_i^2/2\right]$   
>   
> 其中 $N$ 为重复测量 $P\_i$ 的次数。  
>   
> 于是根据 union bound，在 $(4^n-1)$ 个 $c\_i$ 中，任意一个 $|\hat{c}\_i-c\_i| > \epsilon\_i$ 的概率为：  
>   
> $P[|\hat{c}\_i-c\_i| > \epsilon\_i, \ \exists \  i] \le (4^n - 1) \cdot 2 \exp \left[-N\delta^2/2\right]$   
>   
> 现在，我们希望所有的 $|\hat{c}\_i-c\_i|$ 都大概率小于 $\epsilon\_1$ 。也就是说，误差大于 $\epsilon\_1$ 的概率为一个很小的数 $\delta \ll 1$ 。令上式右边为 $\delta$ 得到：  
>   
> $N= \frac{2}{\epsilon\_1^2}\log \frac{2\cdot (4^n-1)}{\delta}= O\left(\frac{n -\log \delta}{\epsilon\_1^2}\right) $   
>   
> 代入 $d=2^n$ 得：  
>   
> $\boxed{ N= O(\log(d/\delta)/\epsilon^2\_1)  }$

这就是在误差 $\epsilon\_1$ 内以低于失败率 $\delta$ 估计所有泡利系数所需要的样本复杂度。

---

注意！这里的 $\epsilon\_1$ 只是单个泡利系数 $c\_i$ 的测量误差，而我们希望得到的是密度矩阵 $\rho = \frac{1}{2^n}\sum\_i c\_i P\_i $ 的误差 $\epsilon$ 。

> 为此，我们定义误差矩阵：  
>   
> $\Delta = \hat{\rho}-\rho = \sum\_i(\hat{c}\_i-c\_i)P\_i$   
>   
> 并且要求它的 trace norm 小于 $\epsilon$ ：  
>   
> $||\Delta||\_1<\epsilon$   
>   
> 注意到 Hilbert-Schmidt norm 更好计算： $||\Delta||\_2^2 := \operatorname{tr}[A^\dagger A] = \frac{1}{2^n}\sum\_i |\hat{c}\_i-c\_i|^2$ ，因为   
> $\operatorname{tr}[P\_i^\dagger P\_j]=\operatorname{tr}[P\_iP\_j]=\delta\_{ij}$ 。  
>   
> 于是我们可以使用柯西不等式 $||A||\_1 \le \sqrt{d}||A||\_2$ ，其中 $d = 2^n$ 为矩阵的阶数：  
>   
> $||\Delta||\_1 \le \sqrt{2^n}||\Delta||\_2 = (\sum\_i |\hat{c}\_i-c\_i|^2)^{1/2} \le (\sum\_i \epsilon\_1^2)^{1/2} = (4^n-1)^{1/2} \ \epsilon\_1$   
>   
> 令 $||\Delta||\_1 \le \epsilon$ ，于是 $\epsilon \sim(4^n-1)^{1/2} \ \epsilon\_1\sim 2^n \epsilon\_1$ ，所以  
>   
> $N \sim (n - \log \delta)/\epsilon\_1^2 \sim (n - \log \delta)4^n /\epsilon^2 = \log \frac{d}{\delta} \cdot d^2/\epsilon^{2}$   
>   
> 最后，考虑到有 $3^n$ 个测量基，在每个测量基下都需要测量 $N$ 次。因此：  
>   
> $N \mapsto 3^n \cdot N \sim \log \frac{d}{\delta}  \cdot d^{3.585} /\epsilon^{2}$

通常不将失败率 $\delta$ 考虑在样本复杂度范围内，于是：

$\boxed{ N = O(\log d  \cdot d^{3.585} /\epsilon^{2}) = O(N \cdot 12^N/\epsilon^2)} $

update: 2025 年 2 月，上界的记录已经被刷新了，是 $\boxed{ N = O(\log d  \cdot d^{3.322} /\epsilon^{2}) = O(N \cdot 10^N/\epsilon^2)} $ ，而下界则被证明是 $\Omega(d^{3.188}\log (d)/\epsilon^2)=\Omega(N \cdot 9.118^N /\epsilon^2)$ [2]。

### 2.3 单样本测量的样本复杂度  

实际上，我们可以做得更好：上述上界可以降低到 $\boxed{O(\log d \cdot d^3 / \epsilon^{2})}$ 。

这是因为 $3^n$ 个测量基（measuremet settings）给出了 $3^n \cdot 2^n = 6^n = d^{2.585}$ 个 POVM 元素，但保证 informationally complete 所需要的最少的 POVM 元素数量是 $4^n = d^2$ 个。可见，我们可以使用正好拥有 $d^2$ 个元素的 SIC-POVM，或者使用 MUB (Mutually Unbiased Bases)，它包含 $(d+1)$ 个测量基，每个测量基有 $d$ 个元素，共 $d(d+1)$ 个 POVM 元素。不管用哪种方法，都可以将样本复杂度上界降低到 $O(\log d \cdot d^3 /\epsilon^{2})$ 。

下界则被证明是 $\Omega(d^3 /\epsilon^{2})$ [3]，但尚未发现具体的测量方法。与上界相比，下界去除了 $\log(d)$ 的依赖，对于一般实验来说影响并不大。

### 2.4 多样本测量的样本复杂度  

以上的测量方法都属于单样本测量（Single-copy measurements），因为我们一次只测量一个样本。我们可以考虑更一般的情况——通过纠缠多个样本 $\rho^{\otimes n}$ 进行联合测量，这叫做多样本测量（Multi-copy measurements）。这样的测量需要量子存储器（quantum memory），在目前的量子硬件中基本很难实现。

人们已经证明，对于这种最一般的测量方式，样本复杂度的确界为 $\boxed{\Theta(d^2 / \epsilon^{2})}$[4,5]。这一点直到 2016 年才被证明。

总结：

$\begin{aligned} \hline & \text{POVM} & \quad & \text{Sample Complexity}\ (d=2^n)\\\\ \hline  & \text{Pauli Measurements} & \quad & O(d^{3.322}\log (d)/\epsilon^2), \  \Omega(d^{3.188}\log (d)/\epsilon^2) \\\\ & \text{Single-copy measurements} & \quad & O(d^{3}\log (d)/\epsilon^2)^\dagger \\\\ & \text{Multi-copy measurements} & \quad & \Theta(d^2/\epsilon^2)\\\\ \hline \end{aligned}$

$\dagger$ 下界被证明是 $\Omega(d^3 / \epsilon^2)$ [3]，但没有具体对应的测量方法。

## 三、经典阴影（Classical Shadows）  

在上一节中我们提到，如果要测量所有泡利系数（泡利算符的期望值），并要求所有结果的误差都不大于 $\epsilon$ ，且失败率不高于 $\delta$ ，那么样本复杂度为：

$\boxed{ N = O\left(\frac{n-\log\delta}{\epsilon^2}\right)=O\left(\log \left(\frac{d}{\delta}\right) \cdot \epsilon^{-2}\right) }$

这揭示了一个似乎惊人的事实：如果我们只关注算符的期望值，而不是量子态本身，那么样本复杂度可以大大降低到对数级别。

实际上，对于任何 $M$ 个算符 $O\_1,...,O\_M$ ，如果希望在误差 $\epsilon$ 内以低于 $\delta$ 的失败率估计它们的期望值，那么只需要样本复杂度为：

$\boxed{ N \sim \log(M/\delta)\cdot \epsilon^{-2} \cdot (\max\_i||O\_i||^2\_{\text{shadow}}) }$

其中 $||\cdot||\_{\text{shadow}}$ 的具体形式取决于测量手段。这个结果来自于 2020 年 Huang et al. 的著名的“经典阴影”（Classical Shadows）[6]。

从第二节的分析可以看出，这一复杂度并不令人意外。那么，为什么“经典阴影”在近年来会变得如此热门呢？

这是因为：以往关于样本复杂度的研究，动机多在于缩小理论上的上界，而不是物理应用；即便存在测量方法，在实验中也难以实现，更多属于数学家口中的“理论上存在”。而经典阴影提供了一种简单、具体且有效的测量方法：实现步骤十分明确，实验物理学家可以开箱即用。另外，对数复杂度本身就是一个很大的噱头，即便它并不像初看上去那样令人惊讶。

实际上，早在 2017 年，Scott Aaronson 就提出了阴影层析（Shadow Tomography）[7]，也指出了对数复杂度 $\log(M)$ 。只不过他考虑的是 $M$ 个 two-outcome POVM 的概率 $\operatorname{tr}[\rho E\_i]$ ，而不是 $M$ 个一般的物理量算符 $\langle O\_i \rangle = \operatorname{tr}[\rho O\_i]$ 。之所以 Shadow Tomography 的工作没有 Classical Shadows 那么受关注，也是因为它给出的测量手段比较复杂。

> 趣事：Scott Aaronson 后来去 OpenAI 工作了，但最近又离开了。

### 3.1 经典阴影的具体实现  

现在我们来看看 Classical Shadows 具体是怎么执行的。

粗略来看，执行步骤分为两步：

**1.** 测量量子态得到 Classical Shadows，存储到经典计算机中

**2.** 从存储的 Classical Shadows 通过一定的算法估计 $M$ 个算符的期望值。

我们先来看 **1**，做法如下：

**1.1** 从 Clifford 算符中随机选出一个 $U$ ，作用到量子态 $\rho$ 上，得到 $U\rho U^\dagger$ 。

**1.2** 对 $U\rho U^\dagger$ （在 computational basis 下）进行测量，得到结果 $|b\rangle \in \{0,1\}^n$

**1.3** 将 $U | b\rangle \langle b| U^\dagger$ 存储到经典计算机的内存中

现在我们来看看 $U | b\rangle \langle b| U^\dagger$ 的期望值是什么。注意到这里有两个随机变量， $U$ 和 $|b\rangle$ 。我们所说的期望值是对于这两个随机变量而言的，也就是：

$\begin{aligned} &\mathbb{E}\_{U,b}[U^\dagger |b\rangle\langle b| U^\dagger] \\\\ &:= \mathbb{E}\_U\left[\sum\_{b=0,1} \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right] \end{aligned}$

可以证明这是一个量子信道（Quantum channel），记为：

$\mathcal{M}(\rho):=\mathbb{E}\_{U\sim \nu}\left[\sum\_{b=1}^d \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right]$

其中 $\nu$ 是 $U$ 服从的分布，它是一个均匀分布。它的概率空间不是通常的数轴，而是一个群，在此处是 Clifford 群。

可以证明（证明见下一节）， $\mathcal{M}(\rho)$ 可以解析地写成：

$\boxed{ \mathcal{M}(\rho)= \frac{\rho + \operatorname{tr}[\rho] \mathbb{I}}{d+1} }$

其中 $d=2^n$ 为希尔伯特空间的维数。这是一个 depolarizing channel。

于是 $\mathcal{M}$ 的逆为：

$\boxed{ \mathcal{M}^{-1}(X)=(d+1) X - \operatorname{tr}[X]\mathbb{I} }$

于是我们可以把 $\mathcal{M}(U|b\rangle\langle b| U^\dagger)$ 作为 $\rho$ 的估计量：

$\boxed{ \begin{aligned} \hat{\rho}&=\mathcal{M}^{-1}(U|b\rangle\langle b| U^\dagger)\\\\ &=(d+1) U|b\rangle\langle b| U^\dagger - \mathbb{I} \end{aligned} }$

这个估计量无偏，因为

$\boxed{ \mathbb{E}[\hat{\rho}]=\rho }$

现在，重复 $N$ 次步骤 1，我们可以得到 $N$ 个 $\hat{\rho}$ ：

$\boxed{ S(\rho,N)=\{\hat{\rho}\_1,\hat{\rho\_2},...,\hat{\rho}\_N\} }$

这个 $S(\rho,N)$ 就是 $\rho$ 的经典阴影。

于是第二步（估计 $\{O\_1,...,O\_M\}$ 的期望值 $\{o\_1,..., o\_M\}$ ）就很直接了：

$\hat{o\_i}=\operatorname{tr}[\hat{\rho} O\_i] = \operatorname{tr}[\sum\_{k}\hat{\rho}\_k O\_i]$

为了避免离群值的影响，提高成功率，实际需要使用平均数中位数（Median of means）法，将 $S(\rho,N)$ 分成 $K$ 份，对每一份求 $\hat{o\_i}$ ，然后取 $K$ 个结果的中位数。

### 3.2Haar 测度与 Unitary t-design  

很明显，上一节描述的步骤之所以成立，关键在于下式：

$\boxed{ \mathcal{M}(\rho)= \frac{\rho + \operatorname{tr}[\rho] \mathbb{I}}{d+1} }$

如何证明这个式子呢？我们需要用到一些 Haar 测度与 t-design 的知识。

直观来看，Haar 测度就是群上的“均匀”分布。由于我们考虑的概率分布（测度）是在幺正算符（也就是 $U(d)$ 群）构成的空间上，而不是普通的数轴上，所以像“均匀”分布这样的概念需要特别的刻画。

> **Haar 测度（Haar Measure）**  
>   
> 给定群 $U(d)$ 以及它的一个 Borel 子集 $S$ ，如果对于所有 $g\in U(d)$ ，测度 $\mu$ 满足：  
>  $\mu(g S)=\mu(S)=\mu(Sg)$   
> 那么称 $\mu$ 是一个 Haar 测度。  
>   
> 这里 $U(d)$ 指的是 $d$ 维幺正群，也就是 $d$ 维希尔伯特空间上所有幺正算符构成的群。所谓 Borel 子集，可以理解为最简单的一种 $\sigma$ -代数，也就是可测集的集合。

可见，Haar 测度利用平移不变性来定义“均匀”。

直观来看，如果我们希望量子态层析的误差是均匀的，那么我们就希望按照 Haar 测度从 $U(d)$ 中随机选取量子门。

然而，在实际的量子硬件中，为了操作简便或者由于硬件的限制，我们一般不会从连续的 $U(d)$ 中选取量子门。通常的做法是从有限个量子门的集合中均匀随机选取。一般选取 Clifford 群作为这个集合。

于是，一个直接的问题由之而来：有限群的均匀分布能够“逼近”或者“模拟”连续群的均匀分布吗？

更具体地，给定 $U(d)$ 上的 Haar 测度 $\mu$ ，及其（有限元素的）子集 $S \subsetneq U(d)$ 上的测度 $\nu$ ， $\nu$ 是否能满足

$\mathbb{E}\_{V\sim \nu}[V^{\otimes t}O V^{\dagger \otimes t}] = \mathbb{E}\_{U \sim \mu}[U^{\otimes t}O U^{\dagger \otimes t}]$

对于希尔伯特空间 $\mathcal{H}^{\otimes t}:= (\mathbb{C}^d)^{\otimes t}$ 上的任意算符 $O \in \mathcal{L}({\mathcal{H}^{\otimes t}})$ 成立？

如果成立，那么称 $\nu$ 为一个 **unitary t-design**。以下简称 t-design。

为了方便起见，定义算符 $A\in \mathcal{L}({\mathcal{H}^{\otimes t}})$ 的矩 $M^{(t)}(A)$ 为：

$M^{(t)}(A):=\mathbb{E}\_{U \sim \mu}[U^{\otimes t}A U^{\dagger \otimes t}]$

于是我们可以用一句话概括 t-design 的定义：

> **Unitary t-design**  
>   
>  $U(d)$ 的有限子集上的测度 $\nu$ 被称为 unitary t-design，如果它的 t 阶矩与 Haar 测度的 t 阶矩相同。

### 3.3 Schur-Weyl Duality  

现在我们来看看 Haar 测度的 t 阶矩 $M^{(t)}$ ，它有许多有用的性质，我们接下来会不加证明地给出这些性质。

我们先把 $\mathcal{L}(\mathcal{H}^{\otimes t})$ 通过 Hilbert-Schmidt 内积（HS 内积）变成一个内积空间。HS 内积定义为：

$\langle A ,B\rangle := \operatorname{tr}[A^\dagger B], \quad A,B \in \mathcal{L}(\mathcal{H^{\otimes t}})$

有了内积之后，我们就能定义投影了。而 t 阶矩正是这个内积空间上的一个投影算子。

> **t 阶矩** $M^{(t)}$ **是投影到 commutant 上的投影算子**  
>   
>  $M^{(t)} \in \mathcal{L}(\mathcal{L}(\mathcal{H}^{\otimes t}))$ 是 HS 内积空间 $\mathcal{L}(\mathcal{H}^{\otimes t})$ 上的一个投影算子，它将算子 $A$ 投影到子空间 $\text{Comm}^{(t)}(U(d))$ 上，其中 $\text{Comm}^{(t)}(U(d))$ 是 $U(d)$ 的 **commutant**，定义为所有与 $B^{\otimes t}$ 可交换的算符的集合：  
>   
>  $\text{Comm}^{(t)}(S) :=\{A \in \mathcal{L}(\mathcal{H}^{\otimes t}) \mid [A,B^{\otimes t}] = 0\quad\forall B\in S\}$   
>   
> 可以证明， $\text{Comm}^{(t)}(U(d))$ 是 $\mathcal{L}(\mathcal{H}^{\otimes t})$ 的一个子空间。  
>   
> Commutant 在群论中也叫 Centralizer。

换句话说，任何算子的 t 阶矩 $M^{(t)}(A)$ 总是在 Commutant 中。

那么，这个 Commutant 有什么性质呢？

> **Schur-Weyl 对偶：Commutant 是所有置换算子张成的空间**  
>   
>  $\text{Comm}^{(t)}(U(d)) = \operatorname{span}(V\_d(\pi): \pi \in S\_t)$   
>   
> 其中置换算子 $V\_d(\pi) \in \mathcal{L}(\mathcal{H}^{\otimes t})$ 定义为：  
>   
>  $V\_d(\pi) |\psi\_1\rangle \otimes \cdots \otimes |\psi\_t\rangle := |\psi\_{\pi^{-1}(1)}\rangle \otimes \cdots \otimes |\psi\_{\pi^{(-1)}(t)}\rangle$

有了 Schur-Weyl 对偶，我们就可以将置换算子 $V\_{d}(\pi)$ 作为 Commutant 的一组基了。

> 不过，置换算符作为 Commutant 的基并不是彼此正交的，因为 $\langle V\_d(\pi), V\_{d}(\sigma)\rangle \ne \delta\_{\pi,\sigma}$ 。  
>   
> 实际上： $\langle V\_d(\pi), V\_{d}(\sigma)\rangle = \operatorname{tr}[V\_d(\pi)^{\dagger} V\_{d}(\sigma)] = \operatorname{tr}[V\_d(\pi^{-1}\sigma)]=d^{# \text{cycle}(\pi^{-1}\sigma)}$   
> 其中 $#\text{cycle}(\pi)$ 是置换 $\pi$ 的循环数（置换图中有多少个闭合的圈）。

于是，任何算子的 t 阶矩 $M^{(t)}(A)$ 都可以写成 t 阶置换群对应的置换算子的线性组合。

利用这一点，我们可以轻松地计算一阶和二阶矩，因为一阶置换群是平凡的，只有单位算子 $\mathbb{I}$ ，二阶置换群只有单位算子 $\mathbb{I}\_2 = \mathbb{I}^{\otimes2}$ 和 SWAP 算子，记为 $F := \mathsf{SWAP}$ 。

> **算子的一阶矩和二阶矩**：  
> $\boxed{ M^{(1)}(A):=\mathbb{E}\_{U \sim \mu}[UA U^\dagger]=\operatorname{tr}[A] \frac{\mathbb{I}}{d}  }$   
> $\boxed{ M^{(2)}(A):=\mathbb{E}\_{U \sim \mu}[U^{\otimes 2}A U^{\dagger \otimes 2}] = \alpha\ \mathbb{I}\_2+ \beta\ F}$   
> 其中  
>  $\alpha = \frac{\operatorname{tr}(O)-d^{-1}\operatorname{tr}(FO)}{d^2-1}, \quad \beta = \frac{\operatorname{tr}(FO)-d^{-1}\operatorname{tr}(O)}{d^2-1}$   
> 证明提示：将矩写成置换算子的线性组合，然后对左右两边取迹，就可以解出系数。

特别地，纯态的二阶矩为：

> **纯态的二阶矩**  
>  $\boxed{ M^{(2)}(|\psi\rangle\langle\psi|)=\frac{\mathbb{I}\_2+ F}{d(d+1)} }$   
> 其中 $|\psi\rangle \in \mathcal{H}^{\otimes 2}$ 。  
> 证明提示：直接根据公式计算即可。  
> 实际上，纯态的 t 阶矩是所有 t 阶置换群的置换算子的等权线性组合。

最后，我们不加证明地指出，Clifford 群上的均匀分布构成一个 3-design。并且，一个 (t+1)-design 也是一个 t-design。因此 Clifford 群上的均匀分布也是一个 2-design。这些事实我们在下节会用到。

### 3.4 测量信道  

有了 Haar measure 和 t-design 的铺垫之后，我们这节就可以来证明测量信道可以写成以下解析形式了：

$\begin{aligned} \mathcal{M}(\rho)&:=\mathbb{E}\_{U\sim \nu}\left[\sum\_{b=1}^d \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right] \\\\ &= \frac{\operatorname{tr}(\rho) \mathbb{I} + \rho}{d+1} \end{aligned}$

> 证明：  
> 根据偏迹的性质，有  
>  $\begin{aligned} \mathcal{M}(\rho)&:=\mathbb{E}\_{U\sim \nu}\left[\sum\_{b=1}^d \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right] \\\\ &= \sum\_{b=1}^d \operatorname{tr}\_1\left( (\rho \otimes \mathbb{I}) \mathbb{E}\_{U\sim \nu} [U^{\otimes 2} |b\rangle\langle b|^{\otimes 2}U^{\dagger\otimes 2}]\right) \end{aligned}$   
> 由于 $\nu$ 是一个 2-design，所以它的二阶矩与 Haar 测度的二阶矩相同：  
>  $\begin{aligned} \mathbb{E}\_{U\sim \nu} [U^{\otimes 2} |b\rangle\langle b|^{\otimes 2}U^{\dagger\otimes 2}] &= \frac{\mathbb{I} \otimes \mathbb{I}+ F}{d(d+1)} \end{aligned}$   
> 于是  
>  $\begin{aligned} \mathcal{M}(\rho)&= \sum\_{b=1}^d \operatorname{tr}\_1\left( (\rho \otimes \mathbb{I}) \frac{\mathbb{I} \otimes\ \mathbb{I}+ F}{d(d+1)}\right) \\\\ &= \frac{d}{d(d+1)}\operatorname{tr}\_1\left( (\rho \otimes \mathbb{I}) + F(\rho \otimes \mathbb{I})\right) \\\\ &= \frac{1}{d+1}(\operatorname{tr}(\rho)\mathbb{I}+ \rho) \end{aligned}$   
> 证毕

### 3.5 估计量方差的上界  

我们在上一节证明了

$\boxed{ \mathcal{M}(\rho)= \frac{\rho + \operatorname{tr}[\rho] \mathbb{I}}{d+1} }$

也就是证明了

$\boxed{ \begin{aligned} \hat{\rho}&=\mathcal{M}^{-1}(U|b\rangle\langle b| U^\dagger)\\\\ &=(d+1) U|b\rangle\langle b| U^\dagger - \mathbb{I} \end{aligned} }$

是无偏的。换句话说，算符的估计量 $\hat{o\_i}:= \operatorname{tr}(O\_i \hat{\rho})$ 的期望值等于真实值 $\mathbb{E}[\hat{o}\_i] = \operatorname{tr}[\rho O\_i]$ 。

然而仅此还不够，我们没有给出估计量的方差的上界，从而求出样本复杂度。

我们接下来证明估计量的方差的上界为 $\boxed{\operatorname{Var}(\hat{o}\_i) \le 3 \operatorname{tr}(O\_i^2)}$ 。

> **估计量的方差的上界**  
> 估计量的方差为：  
>  $\operatorname{Var}(\hat{o\_i})=\mathbb{E}[\hat{o}\_i^2]-\mathbb{E}[\hat{o}\_i]^2$   
> 其中  
>  $\mathbb{E}\left(\hat{\sigma}\_i^2\right):=\sum\_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\langle b| U \rho U^{\dagger}|b\rangle \operatorname{tr}\left(O\_i \mathcal{M}^{-1}\left(U^{\dagger}|b\rangle\langle b| U\right)\right)^2\right]$   
> 首先，注意到  
>  $\operatorname{tr}(A \mathcal{M}(B))=\sum\_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\langle b| U B U^{\dagger}|b\rangle\langle b| U A U^{\dagger}|b\rangle\right]=\operatorname{tr}(\mathcal{M}(A) B)$   
> 所以 $\operatorname{tr}(A \mathcal{M}^{-1}(B))=\operatorname{tr}(\mathcal{M}^{-1}(A) B)$   
> 所以  
>  $\begin{aligned} \mathbb{E}\left(\hat{o}\_i^2\right) & =\sum\_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\langle b| U \rho U^{\dagger}|b\rangle \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right) U^{\dagger}|b\rangle\langle b| U\right)^2\right] \\\\ & =\sum\_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\operatorname{tr}\left(\rho U^{\dagger}|b\rangle\langle b| U\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right) U^{\dagger}|b\rangle\langle b| U\right)^2\right] \\\\ & =\operatorname{tr}\left(\left(\rho \otimes \mathcal{M}^{-1}\left(O\_i\right) \otimes \mathcal{M}^{-1}\left(O\_i\right)\right)\left(\sum\_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[U^{\dagger \otimes 3}|b\rangle\left\langle b\right|^{\otimes 3} U^{\otimes 3}\right]\right)\right) \end{aligned}$   
> 其中最后一步用到了 $\operatorname{tr}(A \otimes B) = \operatorname{tr}(A) \operatorname{tr}(B)$ 。  
> 由于 $\nu$ 是一个 3-design，所以  
>  $\begin{aligned} \underset{U \sim \nu}{\mathbb{E}}\left[U^{\dagger \otimes 3}|b\rangle\left\langle b\right|^{\otimes 3} U^{\otimes 3}\right] = \frac{1}{d(d+1)(d+1)}\underset{\pi \in S\_3}{\sum}V\_d(\pi) \end{aligned}$   
> 于是  
>  $\begin{aligned} &\operatorname{tr}\left(\left(\rho \otimes \mathcal{M}^{-1}\left(O\_i\right) \otimes \mathcal{M}^{-1}\left(O\_i\right)\right)\left(\sum\_{\pi \in S\_3} V\_d(\pi)\right)\right) \\\\ & =\operatorname{tr}(\rho) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right)\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right)\right)+\operatorname{tr}(\rho) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right)^2\right)\\\\ & \quad+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i\right)\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right)\right) +\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i\right)^2\right)\\\\ & \quad+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i\right)^2\right)+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i\right)\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right)\right)   \end{aligned}$ （\\*）  
> 现在我们要用一个技巧：方差 $\operatorname{Var}\left(\hat{o}\_i\right)=\mathbb{E}\left[\left(\hat{o}\_i-\operatorname{Tr}\left(O\_i \rho\right)\right)^2\right]$ 只取决于 $O\_i$ 的无迹部分 $O\_i^{(0)} := O\_i - \operatorname{tr}(O\_i) \frac{\mathbb{I}}{d}$ 。这是因为  
>  $\hat{o}\_i-\operatorname{Tr}\left(O\_i \rho\right)=\operatorname{Tr}\left(O\_i \hat{\rho}\right)-\operatorname{Tr}\left(O\_i \rho\right)=\operatorname{Tr}\left(O\_i^{(0)} \hat{\rho}\right)-\operatorname{Tr}\left(O\_i^{(0)} \rho\right)$   
> 注意到 $\mathcal{M}$ 是保迹的。  
> 所以可以把方差的表达式中将所有 $O\_i$ 换成 $O\_i^{(0)}$ ：  
>  $\begin{aligned} & \operatorname{tr}\left(\left(\rho \otimes \mathcal{M}^{-1}\left(O\_i^{(0)}\right) \otimes \mathcal{M}^{-1}\left(O\_i^{(0)}\right)\right)\left(\sum\_{\pi \in S\_3} V\_d(\pi)\right)\right) \\\\ & =0+\operatorname{tr}(\rho) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i^{(0)}\right)^2\right)+0+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i^{(0)}\right)^2\right)+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i^{(0)}\right)^2\right)+0 \\\\ & =(d+1)^2 \operatorname{tr}\left(O\_i^{(0) 2}\right)+2(d+1)^2 \operatorname{tr}\left(\rho O\_i^{(0) 2}\right) \end{aligned}$   
> 于是  
>  $\begin{aligned} \operatorname{Var}\left(\hat{o}\_i\right) & =\frac{(d+1)^2}{(d+1)(d+2)}\left(\operatorname{tr}\left(O\_i^{(0) 2}\right)+2 \operatorname{tr}\left(\rho O\_i^{(0) 2}\right)\right)-\operatorname{tr}\left(O\_i^{(0)} \rho\right)^2 \\\\ & \leq \operatorname{tr}\left(O\_i^{(0) 2}\right)+2 \operatorname{tr}\left(\rho O\_i^{(0) 2}\right) \\\\ & \leq 3 \operatorname{tr}\left(O\_i^{(0) 2}\right) \\\\ & \leq 3 \operatorname{tr}\left( O\_i^2\right) \end{aligned}$   
> 证毕。

### 3.6 样本复杂度  

在第二节中，我们使用了 Hoeffding 不等式给出样本复杂度的宽松上界。这里，我们使用平均数中位数估计（Median of means estimation）来证明样本复杂度的宽松上界。

> **平均数中位数估计（Median of means estimation）**  
> 给定 $N$ 个独立同分布随机变量 $X\_i,\ i=1,...,N$ ，期望值为 $\mu$ ，方差为 $\sigma^2$ 。将它们分成 $k$ 组，每组 $m=N/k$ 个随机变量。那么其中一组的平均值 $\hat{\mu}\_j = \sum\_{i=j}^{j+m-1} X\_i$ 的方差为 $\sigma^2/m$ 。根据 **Chebyshev 不等式**，有：  
>  $\begin{aligned} P(|\hat{\mu}\_j - \mu| > \epsilon ) \le \frac{\sigma^2}{m \epsilon^2} \end{aligned}$   
> 令右边等于 $p$ ，那么 $m= \sigma^2/(p\epsilon^2)$ 。  
> 定义随机变量：  
>  $Z\_j = \begin{cases} 1,& |\hat{\mu}\_j - \mu| > \epsilon \\\\ 0,& |\hat{\mu}\_j - \mu| \le \epsilon \end{cases}$   
> 由于我们最终取 $\hat{\mu}\_1,...,\hat{\mu}\_k$ 的中位数，我们希望一半以上的 $\hat{\mu}\_j$ 误差大于 $\epsilon$ 的概率 $P\left(\sum\_{j=1}^k Z\_j > \frac{k}{2}\right)$ 足够小。  
> 记 $S=\sum\_{j=1}^k Z\_j$ ，根据 **Hoeffding 不等式**有：  
>  $P(S-\mathbb{E}(S)>t)\le \exp\left(-\frac{2t^2}{k}\right)$   
> 其中 $\mathbb{E}(S) \le kp$ 。令 $t = k/2 - kp$ ，于是：  
>  $P\left(S>\frac{k}{2}\right) \le P(S-\mathbb{E}(S)>t)\le \exp\left(-2k\left(\frac{1}{2}-p\right)^2\right)$   
> 不妨令 $p = 1/4$ ，于是  
>  $P\left(\sum\_{j=1}^k Z\_j > \frac{k}{2}\right) \le \exp\left( - \frac{k}{8}\right)$   
>  令右边等于 $\delta$ 得 $k =8 \log (1/\delta)$ 。  
> 又因为 $m=\sigma^2/(p\epsilon^2) =4\sigma^2/\epsilon^2$ ，所以  
>  $\boxed{ N = km =32 \sigma^2 \log(1/\delta)/\epsilon^2 }$   
> 这就是以低于失败率 $\delta$ 在误差 $\epsilon$ 内估计 $\hat{\mu}$ 所需要的样本数。

现在把 Median of means 用到我们的问题中。 $X\_i:= \hat{o}\_i$ 的方差 $\sigma^2$ 满足 $\sigma^2 \le 3 \operatorname{tr}(O\_i^2) = 3||O\_i||^2$ ，代入得

$N  = 96 ||O\_i||^2\log(1/\delta)/\epsilon^2$

现在我们要同时估计 $M$ 个 $\hat{o}\_i$ ，即 $\hat{o}\_1,...,\hat{o}\_M$ 。

在运用 Hoeffding 不等式的时候：

$P(S-\mathbb{E}(S)>t)\le \exp\left(-\frac{2t^2}{k}\right)$

我们可以选取 $M$ 个 $S\_i$ ，即 $S\_1, ..., S\_M$ ，并取 union bound：

$P(S\_i-\mathbb{E}(S\_i)>t,\ \exists S\_i \in\{S\_1,...,S\_M\})\le M\exp\left(-\frac{2t^2}{k}\right)$

对数复杂度的关键就在这里：取 union bound 的时候， $M$ 出现在指数的外面。因此反过来求 $N$ 的时候， $M$ 会出现在对数里面。

因此，我们可以证明样本复杂度为：

$\boxed{ N  = O\left( \log(M/\delta)\max\_i||O\_i||^2 /\epsilon^2 \right) }$

### 3.7 泡利测量  

前面介绍的一切推导都基于 Clifford 测量。但 Clifford 测量是一种全局测量，需要将各个 qubit 进行纠缠门操作，再在计算基下测量。

实践中更常用的是局部测量，即对各个 qubit 分别进行单比特门操作，然后在计算基下测量。通常这些门被选取为单比特的 Clifford 群，它们能够实现泡利基（也就是 $X, Y, Z$ ）下的测量。

(未完待续)

### 3.8 去随机化（Derandomization）  

经典阴影与传统的 FST 非常不同。在传统的 FST 中，我们在每个测量基下都测量一样多的样本，这样能够保证误差在某种程度上更加均匀。而在经典阴影中，由于测量基是随机选取的，所以不同测量基下的样本数也不同。

于是问题由之而来：与随机选基相比，设定不同测量基下的样本数相同是否更好？这就是所谓的去随机化（Derandomization）。

(未完待续)

## 参考  

1. Cotler, J. & Wilczek, F. Quantum Overlapping Tomography. Phys. Rev. Lett. 124, 100401 (2020).
2. Acharya, Jayadev, et al. "Pauli measurements are not optimal for single-copy tomography." Proceedings of the 57th Annual ACM Symposium on Theory of Computing. 2025.
3. Nayak, A., & Lowe, A. (2025). Lower bounds for learning quantum states with single-copy measurements. ACM Transactions on Computation Theory.
4. O’Donnell, R. & Wright, J. Efficient quantum tomography. in Proceedings of the forty-eighth annual ACM symposium on Theory of Computing 899–912 (ACM, Cambridge MA USA, 2016). doi:10.1145/2897518.2897544.
5. Haah, J., Harrow, A. W., Ji, Z., Wu, X. & Yu, N. Sample-optimal tomography of quantum states. in Proceedings of the forty-eighth annual ACM symposium on Theory of Computing 913–925 (ACM, Cambridge MA USA, 2016). doi:10.1145/2897518.2897585.
6. Huang, H.-Y., Kueng, R. & Preskill, J. Predicting many properties of a quantum system from very few measurements. Nat. Phys. 16, 1050–1057 (2020).
7. Aaronson, Scott. "Shadow tomography of quantum states." Proceedings of the 50th annual ACM SIGACT symposium on theory of computing. 2018.