---
title: "激光的一种简单的量子描述"
date: 2024-05-27T17:42:31+08:00
draft: false
tags: ["量子光学"]
categories: ["量子信息"]
---

本文旨在从基本量子动力学出发，推导出激光的相干态。

考虑一个二能级系统和一个单模光场的相互作用，且光场频率等于能级差。

二能级系统一开始处于激发态 $|e\rangle$ ，光场处于真空态 $|0\rangle$ 。

根据 Jaynes-Cummings model，即使光场处于真空态，也会产生自发辐射。经过一小段时间，量子态从 $|e,0\rangle$ 演化为：

$|\psi\rangle = a |e,0\rangle + b |g,1\rangle$ 

其中 $|g,1\rangle$ 表示二能级处于基态，且与其耦合的光场模式中有一个光子，也就是自发辐射所发射的光子。

现在考虑 $N$ 个处于激发态的二能级系统，它们之间没有耦合，而是只和光场耦合。一开始的自发辐射光子诱导其他二能级系统的受激辐射，那么总体量子态可以写成：

$|\Psi\rangle = C|\psi\rangle^{\otimes N} =  C\sum_k   \sum_m\mathcal{P}_m[|e,0\rangle^{\otimes (N-k)} \otimes |g,1\rangle^{\otimes k}]$ 

其中 $C$ 是待定的归一化常数， $\mathcal{P}_m$ 表示 $|e,0\rangle^{\otimes (N-k)} \otimes |g,1\rangle^{\otimes k}$ 所有可能的置换方式，共有 $\frac{N!}{(N-k)!\,k!}$ 种置换方式。注意这里我们尚未使用 Fock space（还没有对全同玻色子做对称化）。


> 这一步非常不严谨，甚至可能是错误的，因为它没有说明为什么受激辐射意味着总体量子态是自发辐射态 $|\psi\rangle = a |e,0\rangle + b |g,1\rangle$ 的张量积。但是后面会看到它给出了正确的结果。因此这种推导一定包含了某种 insight，只是我现在还没有看出来。

光场的量子态就是总体量子态 trace 掉二能级系统的量子态：

$\rho = \operatorname{Tr}_{\text{a}}[|\Psi\rangle\langle\Psi|] = C^2 \sum_k  |a^{N-k}b^k |^2  \sum_m\mathcal{P}_m[(|0\rangle\langle 0|)^{\otimes (N-k)} \otimes (|1\rangle\langle 1|)^{\otimes k}]$ 

现在我们将全同粒子的张量积对称化并映射到Fock space，也就是众所周知的 $|1\rangle ^{\otimes k} \rightarrow  \sqrt{k!} |k\rangle$ ，于是上式变成

$\rho = C^2 \sum_k  |a^{N-k}b^k |^2 \left(\frac{N!}{(N-k)!\,k!}\right)^2 k! |k\rangle\langle k |$ 

当 $k \ll N$ 时， $\frac{N!}{(N-k)!}  \sim \left(\frac{N}{e}\right)^k$ 。令 $\alpha = \frac{b}{a}\cdot\frac{N}{e}$ ，则上式可以写成：

$\rho = C^2 a^N\sum_k \frac{|\alpha|^{2k}}{k!} |k\rangle\langle k |$ 

对其进行归一化得到：

$\rho = e^{-|\alpha|^2}\sum_k \frac{|\alpha|^{2k}}{k!} |k\rangle\langle k |$ 

这是一个平均粒子数为 $|\alpha|^2$ 的泊松分布。它在相干态表象下可以写成：

$\rho = \int_0^{2\pi} \frac{\mathrm{d}\theta}{2\pi} |\alpha e^{\mathrm{i}\theta}\rangle\langle\alpha e^{\mathrm{i}\theta}|$ 

可见它其实是一个相位随机的相干态。相干态 $|\alpha\rangle$ 对应一个振幅和相位都非常确定的经典电磁波，但是这里将它的相位从 $0$ 到 $2\pi$ 积分了。这表现了我们对相位信息的无知，这种无知从根本上来源于我们对二能级系统（增益介质）的微观状态的无知。因此可以说这个 $\rho = \rho_{\text{epistemic}}$ 是认识论的量子态。

而从本体论量子态的角度而言，系统的量子态应当坍缩为一个有确定相位的 $\rho_{\text{ontic}} = |\alpha\rangle$ ，只是我们没办法知道是哪个相位而已。这是因为在光学频率 $\sim 10^{15} \text{Hz}$ 下，人类是无法观测绝对相位的。不过相对相位可以观测，因此我们仍能观察到干涉现象。如果读者对此好奇，可以进一步阅读这篇文章 [[1]](#ref_1)。

## 参考  
1. Bartlett, S. D., Rudolph, T. & Spekkens, R. W. Dialogue Concerning Two Views on Quantum Coherence: Factist and Fictionist. Int. J. Quantum Inform. 04, 17–43 (2006).
