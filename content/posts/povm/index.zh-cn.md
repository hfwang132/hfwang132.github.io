---
title: "广义量子测量：POVM 简介"
date: 2024-01-26T23:36:13+08:00
draft: false
---

## 投影测量  
传统意义上的（Von Neumann 意义上的）测量是一系列投影算符。对可观测量所对应的自伴算子进行谱分解 $O=\sum\_i\lambda\_i |\varphi\_i\rangle\langle\varphi\_i|$ ，即可得到这些投影算符 $|\varphi\_i\rangle\langle\varphi\_i|$ 。这一部分学过初等量子力学的同学都很熟悉。

除了 Von Neumann 测量外，还有一种更加一般的测量，叫做广义测量（Generalized Measurements），或称 POVM（Positive Operator Valued Measure）。

## 广义测量（Generalized Measurements, POVM）  

> **定义：POVM**  
>   
> POVM 是一个映射 $\mathsf{E}: X \rightarrow \mathcal{L}(\mathcal{H})$ ，满足  
> 1) $\mathsf{E}(x) \ge 0,\quad \forall x\in X$   
> 2) $\sum\_{x\in X}\mathsf{E}(x) = \mathbb{I}\_{\mathcal{H}}$   
> 其中 $X$ 代表有限个可能的测量结果的集合， $\mathcal{L}(\mathcal{H})$ 代表 $\mathcal{H}$ 上所有的有界算子的集合。  
>   
> **玻恩规则**  
>   
> 对于一个量子态 $\rho$ 进行 POVM $\mathsf{E}$ 所给出的测量，结果为 $x$ 的概率为 $p\_{\rho}^{\mathsf{E}}(x) = \operatorname{tr}[\rho \mathsf{E}(x)]$ 

当我第一次看到 POVM 的时候，我并不清楚它是如何实现的。因为传统意义上的测量是一个投影算符，满足 $\mathsf{E}(x)^2=\mathsf{E}(x),\quad \forall x\in X$ 。而一般的 POVM 不满足这一条件。

实际上，传统意义上的投影测量也叫做 PVM（Projection Valued Measure），是一类特殊的 POVM。

PVM 之于 POVM，就像纯态之于混合态。也就是说，POVM 是 PVM 的统计混合（statistical mixture），正如混合态是纯态的统计混合。

## 如何实现 POVM  
那么如何实现 POVM 呢？其实我们可以利用 PVM 和复合系统来实现 POVM。

考虑一个系统，其希尔伯特空间为 $\mathcal{H}$ ，状态为 $\rho$ 。

接着我们将系统 $\mathcal{H}$ 和另一个系统 $\mathcal{K}$ 耦合到一起。假设系统 $\mathcal{K}$ 的初态为 $\sigma$ ，于是复合系统的初态为 $\rho \otimes \sigma \in \mathcal{H} \otimes \mathcal{K}$ 。

然后，我们让复合系统演化一段时间，于是系统状态变为 $U(\rho\otimes \sigma) U^\dag$ 。

最后，我们对子系统 $\mathcal{K}$ 进行 PVM $\mathsf{Z}$ 所给出的测量，根据玻恩规则，得到结果 $x$ 的概率为 $\operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z(x)})]$ 。

这样，我们就实现了一个 POVM $\mathsf{E}$ ，满足 $\operatorname{tr}[\rho \mathsf{E(x)}]=\operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z(x)})]$ 。

## 测量模型（Measurement Model）  
我们整理一下上面实现 POVM 所涉及到的物理对象：辅助（ancilla）系统 $\mathcal{K}$ ，系统 $\mathcal{K}$ 的初态 $\sigma$ ，复合系统的演化 $U$ ，以及对辅助系统的投影测量 $\mathsf{Z}$ 。这些物理对象实现了一个 POVM 测量。

于是我们可以定义 $\mathfrak{M}=(\mathcal{K},\sigma,U,\mathsf{Z})$ ，并称之为一个测量模型（Measurement Model）。

在实际实验中，辅助（ancilla）系统 $\mathcal{K}$ 可以看作是仪器的探针，而 $\mathsf{Z}$ 就是对探针进行读数。

## 测量后的状态  
POVM 本身不能决定测量后的状态。真正决定测量后的状态的是测量的具体实现，即测量模型。

对于测量模型 $\mathfrak{M}=(\mathcal{K},\sigma,U,\mathsf{Z})$ ，测量后系统 $\mathcal{H}$ 的状态为 $\rho\_x=\operatorname{tr}\_{\mathcal{K}}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z(x)})]$ ，其中 $\operatorname{tr}\_{\mathcal{K}}[\cdot]$ 表示取偏迹。

## 量子仪器（Quantum Instruments）  
POVM 给出了各个测量结果的概率，却没有给出测量后的状态。于是我们希望找到一个数学对象，能将测量概率和测量后的状态都包括进来。这个数学对象叫做 Quantum Instrument。


> **定义 Quantum Instrument**  
>   
> 称 $\mathcal{I}\_{x}: \mathcal{I}\_{x}(\rho) = \rho\_x$ 为一个 Quantum Instrument，如果 $\operatorname{tr}\left[\sum\_{x\in X} \rho\_x \right]=\operatorname{tr}[\rho]=1$ 。

可以看出， $\mathcal{I}\_x$ 不仅给出了测量的概率 $p\_x=\operatorname{tr}[\rho\_x]$ ，还给出了测量后的状态 $\frac{\rho\_x}{\operatorname{tr}[\rho\_x]}$ 。

显然，同一个 POVM 对应无数个 Quantum Instrument。

那么对于任意一个 Quantum Instrument，我们是否总是可以实现它？答案是肯定的。


> **定理**  
>   
> 给定任意一个 Quantum Instrument，我们总是能找到一个 Measurement Model 来实现它（实际上有无数个）。证略。

