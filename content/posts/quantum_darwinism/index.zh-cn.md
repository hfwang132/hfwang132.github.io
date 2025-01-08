---
title: "量子达尔文主义"
date: 2025-01-08T21:03:37+08:00
draft: false
tags: ["量子达尔文主义"]
categories: ["量子信息"]
---


个人认为在量子力学的诠释中，目前最有趣的是 Zurek 的 **Existential Interpretation（存在主义诠释）**，也被称为**量子达尔文主义（Quantum Darwinism）** [1]。Zurek 本人是退相干理论的奠基人之一。

量子达尔文主义并未直接给出测量过程的动力学，但它做出了几个非常有启发性的观察：

**(1)** 测量结果之所以能成为宏观事实，是因为它的信息被复制（克隆）了很多遍，遍布于环境之中，从而使得不同的观察者可以达成共识。

> 具体的克隆过程:  
>  $|s_k\rangle |\varepsilon_0\rangle \rightarrow |s_k\rangle |\varepsilon_k\rangle$   
> 其中 $|s_k\rangle$ 是系统的状态， $|\varepsilon_k\rangle$ 是环境的状态。  
> 很显然，对于一个特定的 k，存在一个幺正（Unitary）过程 $U$ 使得 $U|s_k\rangle |\varepsilon_0\rangle = |s_k\rangle |\varepsilon_k\rangle$ 。  
> 然而，这个过程 $U$ 不能同时克隆任意其他的 $|s_k\rangle$ ，而是只能克隆一组正交的 $|s_k\rangle$ ，这就是下面第 (2) 点要说的不可克隆定理。

**(2)** 根据 no-cloning theorem（不可克隆定理），一个幺正（Unitary）过程只能克隆一组正交的态。

> **评论：** 根据 (1) (2)，我们可以得出：测量结果之间必须是正交的。或者说测量结果构成希尔伯特空间中的一组完备正交基。  
>   
> 但是，希尔伯特空间中有无穷多组完备正交基，一个具体的测量究竟对应到哪一组呢？  
>   
> 例如，“活猫”和“死猫”是量子态，但“活猫加死猫”和“活猫减死猫”同样也是合法的量子态，为什么我们只能观察到前一对结果，而不是后一对？  
>   
> 下面第 (3) 点给出了解释。

**(3)** 系统和环境的相互作用使得只有某一组正交量子态（偏好基）能存活下来，而其他所有量子态（偏好基的叠加态）的信息最终都会丢失。

> **评论：** 第 (3) 点就是“量子达尔文主义”这个名字的来源。它有严格的动力学模型支撑，也就是退相干模型。但退相干模型只能让叠加态变成一个混态，而不是一个纯态，因此仍然没有给出测量过程的动力学。  
>   
> 那么混态意味着什么？混态有两种物理意义：一是对系综的描述，二是对主观信息的描述。例如，对于一个量子比特的混态 $a|0\rangle\langle0|+b|1\rangle\langle1|$ ，我们有两种解释方式：一是我们有一个量子系综，里面有 $\frac{a}{a+b}$ 比例的量子比特处于 $|0\rangle$ 态， $\frac{b}{a+b}$ 比例的量子比特处于 $|1\rangle$ 态；二是我们只有一个量子比特，我们知道它要么处于 $|0\rangle$ 态，要么处于 $|1\rangle$ 态，但不知道实际是哪种情况。我们只知道它以 $\frac{a}{a+b}$ 的概率处于 $|0\rangle$ 态，以 $\frac{b}{a+b}$ 的概率 $|1\rangle$ 态。如果一个人只接受系综解释，那么他很可能会相信多世界诠释。  
>   
> 可见，到此为止，我们仍然没有解释概率的来源，即测量结果为什么以概率出现。下面第 (4) 点是 Zurek 对概率成因的解释：

**(4)** 概率来源于量子纠缠：如果我们有一个纠缠对 $(A,B)$ ，它处于态 $|a_1\rangle |b_1\rangle + |a_2\rangle|b_2\rangle + \cdots + |a_N\rangle |b_N\rangle$ 上，那么任何在 $B$ 上的置换操作都不会改变物理状态。这是因为任何这样的置换操作都能被 $A$ 上同样的置换操作所抵消。而正因为置换分支对物理状态完全没有影响，所以各个分支一定是等概率出现的。

> **评论：** 等概率的情况可以推广到不等概率的情况。这是因为环境的自由度总比系统的自由度多，即 $B$ 的自由度比 $A$ 的自由度要多。例如，假设系统 $A$ 是量子比特，其希尔伯特空间是二维的，而 $B$ 的希尔伯特空间是 1024 维的（例如，10 个量子比特），那么我们可以想象这样一种态： $|0\rangle (|b_1\rangle + \cdots + |b_k\rangle) + |1\rangle (|b_{k+1}\rangle + \cdots + |b_{1024}\rangle)$ 。此时，根据等概率原理， $|0\rangle$ 的概率为 $\frac{k}{1024}$ ， $|1\rangle$ 的概率为 $\frac{1024-k}{1024}$ 。  
>   
> 实际上，环境的希尔伯特空间的维数是 $2^{10^{23}}$ 量级的，远不止 $2^{10} = 1024$ ，因此从 0 到 1 之间的所有概率都可以用这个模型实现。

以上就是 Zurek 的存在主义诠释的 4 个要点。其中第 (3) 点称为 “**Einselection**”，全称“Environment-Induced Superselection”（环境诱导的超选择），第 (4) 点称为 “**Envariance**”，全称“Environment-assisted Invariance”（环境协助的不变性）。

---

以下是哲学方面的个人评论：

个人认为 Zurek 最精彩的观察其实是第 (1) 点，其奠定了存在主义诠释的哲学基调。这里将其再次陈述一遍：

**测量结果之所以能成为宏观事实，是因为它的信息被复制了很多遍，遍布于环境之中，从而使得不同的观察者可以达成共识。**

这个陈述暗含了一个信息：不同的观察者可以观察到不同的事实。Zurek 的工作中通过互信息（Mutual Information）定量刻画了这一点 [1]。之所以没有发生这种情况，是因为随着泄露到环境中的信息以及观察者所能观察的环境部分的增加，互信息增长的非常快。

“不同的观察者可以观察到不同的事实”这一点在相对论中并不令人惊讶。Carlo Rovelli 的关系型量子力学（Relational Quantum Mechanics）诠释就强调了这一点。

回到第 (1) 点，它暗示了这样一种哲学观点：所知与所在的界限是模糊的。用 Zurek 本人的话说 [2]

> "I strongly suspect that the ultimate message of quantum theory is that the separation between what exists and what is known to exist – between the **epistemic** and the **ontic** – must be abolished."  
>   
> "Surprisingly, as the nascent quantum theory matured, quantum awkwardness did not go away. The lesson of the developments that started with decoherence, and led, through einselection and pointer states to quantum Darwinism and related insights, is that quantum states are **epiontic**. It now appears that the distinction between **what is** and **what is known** about what exists – something we take for granted in our everyday world – is not there at the fundamental level."  
>   
> 翻译：  
>   
> 我强烈怀疑，量子理论最终要传达的信息是：必须消除“存在的事物”与“被认识到存在的事物”之间的区分——即消除认知（epistemic）与本体（ontic）之间的区分。  
>   
> 令人惊讶的是，随着新生的量子理论逐渐成熟，量子的尴尬并没有消失。从退相干（decoherence）开始的研究，通过环境选择（einselection）和指针态（pointer states），最终发展到量子达尔文主义（quantum Darwinism）及相关洞察，这些研究表明量子态是“认知-本体一体化”（epiontic）的。如今看来，在基础层面上，我们在日常世界中所认为的“存在”与“被认识的存在”之间的区分，其实并不存在。

Zurek 调和了本体论诠释（隐变量、多世界）和认识论诠释（量子贝叶斯主义，关系型量子力学）之间的矛盾。他说：量子力学既不是完全认识论（Epistemic）的，也不是完全本体论（Ontic）的，而是“Epiontic”的。换言之：

所知即所在，所在即所知。

## 参考  

1. Zurek, W. H. Quantum Theory of the Classical: Einselection, Envariance, Quantum Darwinism and Extantons. Entropy 2022, 24 (11), 1520. [https://doi.org/10.3390/e24111520](https://doi.org/10.3390/e24111520)
2. Emergence of the Classical from within the Quantum Universe. [https://arxiv.org/abs/2107.03378](https://arxiv.org/abs/2107.03378)
