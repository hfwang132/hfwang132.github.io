---
title: "激光的一种简单的量子描述"
date: 2024-05-21T00:41:11+08:00
originalURL: "https://zhuanlan.zhihu.com/p/698877224"
aliases:
  - "/laser_quantum/"
  - "/Post_20240527_激光的一种简单的量子描述/"
draft: false
tags: ["量子光学"]
categories: ["量子信息/量子光学"]
math: true
author: "Haifei"
---

本文旨在用简单的物理图像导出这样一个事实：激光器所输出的态是相干态。

考虑一个二能级系统和一个单模光场的相互作用，且光场频率等于能级差。

二能级系统一开始处于激发态 $|e\rangle$ ，光场处于真空态 $|0\rangle$ 。

根据 Jaynes-Cummings model，即使光场处于真空态，也会产生自发辐射。经过一小段时间，量子态从 $|e,0\rangle$ 演化为：

$$|\psi\rangle = a |e,0\rangle + b |g,1\rangle$$

其中 $|g,1\rangle$ 表示二能级处于基态，且与其耦合的光场模式中有一个光子，也就是自发辐射所发射的光子。

现在考虑 $N$ 个处于激发态的二能级系统，它们之间没有耦合，而是只和光场耦合。一开始的自发辐射出的光子诱导其他二能级系统的受激辐射，这些态同样也是 $|\psi\rangle = a |e,0\rangle + b |g,1\rangle$ ，那么总体量子态就可以写成 N 个这样的态的张量积：

$$|\Psi\rangle = C|\psi\rangle^{\otimes N} =  C\sum_k   \sum_m\mathcal{P}_m[|e,0\rangle^{\otimes (N-k)} \otimes |g,1\rangle^{\otimes k}]$$

其中 $C$ 是待定的归一化常数， $\mathcal{P}_m$ 表示 $|e,0\rangle^{\otimes (N-k)} \otimes |g,1\rangle^{\otimes k}$ 所有可能的置换方式，共有 $\frac{N!}{(N-k)!\,k!}$ 种置换方式。注意这里我们尚未使用 Fock space（还没有对全同玻色子做对称化）。

> 这一步不是很严格，因为它并没有从第一性原理的角度说明为什么受激辐射意味着总体量子态是自发辐射态 $|\psi\rangle = a |e,0\rangle + b |g,1\rangle$ 的张量积。我们得出这个结果的依据完全来源于受激辐射的物理图像。

光场的量子态就是总体量子态对二能级系统取偏迹：

$$\rho = \operatorname{Tr}_{\text{a}}[|\Psi\rangle\langle\Psi|] = C^2 \sum_k  |a^{N-k}b^k |^2  \sum_m\mathcal{P}_m[(|0\rangle\langle 0|)^{\otimes (N-k)} \otimes (|1\rangle\langle 1|)^{\otimes k}]$$

现在我们将全同粒子的张量积对称化并映射到 Fock space，也就是众所周知的 $|1\rangle ^{\otimes k} \rightarrow  \sqrt{k!} |k\rangle$ ，于是上式变成

$$\rho = C^2 \sum_k  |a^{N-k}b^k |^2 \left(\frac{N!}{(N-k)!\,k!}\right)^2 k! |k\rangle\langle k |$$

当 $k \ll N$ 时， $\frac{N!}{(N-k)!}  \sim N^k$ 。令 $\alpha = \frac{b}{a}N$ ，则上式可以写成：

$$\rho = C^2 a^N\sum_k \frac{|\alpha|^{2k}}{k!} |k\rangle\langle k |$$

对其进行归一化得到：

$$\rho = e^{-|\alpha|^2}\sum_k \frac{|\alpha|^{2k}}{k!} |k\rangle\langle k |$$

这是一个平均粒子数为 $|\alpha|^2$ 的泊松分布。它在相干态表象下可以写成：

$$\rho = \int_0^{2\pi} \frac{\mathrm{d}\theta}{2\pi} |\alpha e^{\mathrm{i}\theta}\rangle\langle\alpha e^{\mathrm{i}\theta}|$$

可见它其实是一个相位随机的相干态。相干态 $|\alpha\rangle$ 对应一个振幅和相位都非常确定的经典电磁波，而这里将它的相位从 $0$ 到 $2\pi$ 积分了，这表现了我们对相位信息的无知，这种无知从根本上来源于我们对二能级系统（增益介质）的微观状态的无知。可以说这个 $\rho = \rho_{\text{epistemic}}$ 是认识论的量子态。

而从本体论的角度而言，系统的量子态应当坍缩为一个有确定相位的 $\rho_{\text{ontic}} = |\alpha\rangle$ ，只是我们没办法知道是哪个相位而已。这是因为在光学频率 $\sim 10^{15} \text{Hz}$ 下，人类无法观测绝对相位。不过相对相位可以观测，因此我们仍能观察到干涉现象。简单的计算也可以看出这一点：无论是用混态 $\rho = \int_0^{2\pi} \frac{\mathrm{d}\theta}{2\pi} |\alpha e^{\mathrm{i}\theta}\rangle\langle\alpha e^{\mathrm{i}\theta}|$ 还是用纯态 $\rho = |\alpha\rangle\langle \alpha|$ 去计算关联函数 $\langle a^\dag(t)a(0)\rangle = \text{tr}[\rho a^\dag(t)a(0)]$ ，计算结果都不会有任何区别。这一度引起了关于相干现象的讨论：相干到底是一种幻觉，还是一种物理实在？ [[1]](#ref\_1)前者的支持者认为上文的“相位坍缩”诠释存在“preferred basis”的问题，而后者的支持者认为 preferred basis 问题可以用自发对称性破缺来解释。

## 参考  

1. [^](#ref\_1\_0)Bartlett, S. D., Rudolph, T. & Spekkens, R. W. Dialogue Concerning Two Views on Quantum Coherence: Factist and Fictionist. Int. J. Quantum Inform. 04, 17–43 (2006).
