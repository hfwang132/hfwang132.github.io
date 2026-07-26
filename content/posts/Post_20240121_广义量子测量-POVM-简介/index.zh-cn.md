---
title: "广义量子测量：POVM 简介"
date: 2024-01-21T22:13:57+08:00
originalURL: "https://zhuanlan.zhihu.com/p/679038823"
aliases:
  - "/povm/"
  - "/Post_20240126_广义量子测量-POVM-简介/"
draft: false
tags: ["量子测量理论"]
categories: ["量子信息"]
math: true
author: "Haifei"
---

## 投影测量  

传统意义上的（Von Neumann 意义上的）测量是一系列投影算符。对可观测量所对应的自伴算子进行谱分解 \(O=\sum_i\lambda_i |\varphi_i\rangle\langle\varphi_i|\) ，即可得到这些投影算符 \(|\varphi_i\rangle\langle\varphi_i|\) 。这一部分学过初等量子力学的同学都很熟悉。

除了 Von Neumann 测量外，还有一种更加一般的测量，叫做广义测量（Generalized Measurements），或称 POVM（Positive Operator Valued Measure）。

## 广义测量（Generalized Measurements, POVM）  
> **定义：POVM**  
>   
> POVM 是一个映射 \(\mathsf{E}: X \rightarrow \mathcal{L}(\mathcal{H})\) ，满足  
> 1) \(\mathsf{E}(x) \ge 0,\quad \forall x\in X\)   
> 2) \(\sum_{x\in X}\mathsf{E}(x) = \mathbb{I}_{\mathcal{H}}\)   
> 其中 \(X\) 代表有限个可能的测量结果的集合， \(\mathcal{L}(\mathcal{H})\) 代表 \(\mathcal{H}\) 上所有的有界算子的集合。  
>   
> **玻恩规则**  
>   
> 对于一个量子态 \(\rho\) 进行 POVM \(\mathsf{E}\) 所给出的测量，结果为 \(x\) 的概率为 \(p_{\rho}^{\mathsf{E}}(x) = \operatorname{tr}[\rho \mathsf{E}(x)]\)

注意，传统意义上的测量是一个投影算符，满足 \(\mathsf{E}(x)^2=\mathsf{E}(x),\quad \forall x\in X\) 。而一般的 POVM 不一定满足这一条件，可能是多个不同投影算符的加权和。

实际上，传统意义上的投影测量也叫做 PVM（Projection Valued Measure），是一类特殊的 POVM。

PVM 之于 POVM，类似于纯态之于混合态。也就是说，POVM 的元素是 PVM 的元素的统计混合（statistical mixture），正如混合态是纯态的统计混合。混合态可以被纯化为一个更大的希尔伯特空间上的纯态，而 POVM 也可以由 naimark dilation 扩张为一个更大空间上的 PVM。

## 测度  

POVM 里的 M 表示测度（Measure），而不是测量（Measurement）。普通的测度将可测集映射成实数。而 POVM（值为正算符的测度）将可测集映射成一个正算符（Positive operator）。因此 POVM 的正式定义其实是：

\(\mathsf{E}: \mathcal{A} \rightarrow \mathcal{L}(\mathcal{H})\) 满足

1) \(\mathsf{E}(A) \ge 0,\quad \forall A\in \mathcal{A}\)

2) \(\mathsf{E}(X) = \mathbb{I}_{\mathcal{H}}\)

其中 \(\mathcal{A}\) 是 \(X\) 上的一个 \(\sigma\) -代数。 \((X,\mathcal{A})\) 构成一个可测空间。

之所以要这么定义，有两方面原因：

一是量子力学建立在概率论的基础上，而概率论建立在测度论的基础上。

二是当测量结果连续时，我们必须采用这种定义。例如位置和动量测量。

## 如何实现 POVM  

那么如何实现 POVM 呢？其实我们可以利用 PVM 和复合系统来实现 POVM。

考虑一个系统，其希尔伯特空间为 \(\mathcal{H}\) ，状态为 \(\rho\) 。

接着我们将系统 \(\mathcal{H}\) 和另一个系统 \(\mathcal{K}\) 耦合到一起。假设系统 \(\mathcal{K}\) 的初态为 \(\sigma\) ，于是复合系统的初态为 \(\rho \otimes \sigma \in \mathcal{H} \otimes \mathcal{K}\) 。

然后，我们让复合系统演化一段时间，于是系统状态变为 \(U(\rho\otimes \sigma) U^\dag\) 。

最后，我们对子系统 \(\mathcal{K}\) 进行 PVM \(\mathsf{Z}\) 所给出的测量，根据玻恩规则，得到结果 \(x\) 的概率为 \(\operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}_{\mathcal{H}}\otimes \mathsf{Z(x)})]\) 。

这样，我们就实现了一个 POVM \(\mathsf{E}\) ，满足 \(\operatorname{tr}[\rho \mathsf{E(x)}]=\operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}_{\mathcal{H}}\otimes \mathsf{Z(x)})]\) 。

## 测量模型（Measurement Model）  

我们整理一下上面实现 POVM 所涉及到的物理对象：辅助（ancilla）系统 \(\mathcal{K}\) ，系统 \(\mathcal{K}\) 的初态 \(\sigma\) ，复合系统的演化 \(U\) ，以及对辅助系统的投影测量 \(\mathsf{Z}\) 。这些物理对象实现了一个 POVM 测量。

于是我们可以定义 \(\mathfrak{M}=(\mathcal{K},\sigma,U,\mathsf{Z})\) ，并称之为一个测量模型（Measurement Model）。

在实际实验中，辅助（ancilla）系统 \(\mathcal{K}\) 可以看作是仪器的探针，而 \(\mathsf{Z}\) 就是对探针进行读数。

## 测量后的状态  

POVM 本身不能决定测量后的状态。真正决定测量后的状态的是测量的具体实现，即测量模型。

对于测量模型 \(\mathfrak{M}=(\mathcal{K},\sigma,U,\mathsf{Z})\) ，测量后系统 \(\mathcal{H}\) 的状态为 \(\rho_x=\operatorname{tr}_{\mathcal{K}}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}_{\mathcal{H}}\otimes \mathsf{Z(x)})]\) ，其中 \(\operatorname{tr}_{\mathcal{K}}[\cdot]\) 表示取偏迹。

## 量子仪器（Quantum Instruments）  

POVM 给出了各个测量结果的概率，却没有给出测量后的状态。于是我们希望找到一个数学对象，能将测量概率和测量后的状态都包括进来。这个数学对象叫做 Quantum Instrument。

> **定义 Quantum Instrument**  
>   
> 称 \(\mathcal{I}_{x}: \mathcal{I}_{x}(\rho) = \rho_x\) 为一个 Quantum Instrument，如果 \(\operatorname{tr}\left[\sum_{x\in X} \rho_x \right]=\operatorname{tr}[\rho]=1\) 。

可以看出， \(\mathcal{I}_x\) 不仅给出了测量的概率 \(p_x=\operatorname{tr}[\rho_x]\) ，还给出了测量后的状态 \(\frac{\rho_x}{\operatorname{tr}[\rho_x]}\) 。

显然，同一个 POVM 对应无数个 Quantum Instrument。

那么对于任意一个 Quantum Instrument，我们是否总是可以实现它？答案是肯定的。

> **定理**  
>   
> 给定任意一个 Quantum Instrument，我们总是能找到一个 Measurement Model 来实现它（实际上有无数个）。证略。
