---
title: "A Simple Quantum Description of Lasers"
date: 2024-05-21T00:41:11+08:00
originalURL: "https://zhuanlan.zhihu.com/p/698877224"
aliases:
  - "/en/laser_quantum/"
  - "/en/Post_20240527_激光的一种简单的量子描述/"
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information/Quantum Optics"]
math: true
author: "Haifei"
---

This article aims to derive, using a simple physical picture, the fact that the state output by a laser is a coherent state.

Consider the interaction between a two-level system and a single-mode optical field, with the field frequency equal to the energy-level spacing.

The two-level system initially occupies the excited state $|e\rangle$, while the optical field is in the vacuum state $|0\rangle$.

According to the Jaynes-Cummings model, spontaneous emission occurs even when the optical field is in the vacuum state. After a short time, the quantum state evolves from $|e,0\rangle$ to:

$$|\psi\rangle = a |e,0\rangle + b |g,1\rangle$$

where $|g,1\rangle$ denotes that the two-level system is in the ground state and that there is one photon in the optical field mode coupled to it, namely, the photon emitted through spontaneous emission.

Now consider $N$ two-level systems in the excited state. They are not coupled to one another, but only to the optical field. The photon emitted initially through spontaneous emission induces stimulated emission from the other two-level systems. These states are likewise $|\psi\rangle = a |e,0\rangle + b |g,1\rangle$, so the total quantum state can be written as the tensor product of N such states:

$$|\Psi\rangle = C|\psi\rangle^{\otimes N} =  C\sum_k   \sum_m\mathcal{P}_m[|e,0\rangle^{\otimes (N-k)} \otimes |g,1\rangle^{\otimes k}]$$

where $C$ is a normalization constant to be determined, and $\mathcal{P}_m$ denotes $|e,0\rangle^{\otimes (N-k)} \otimes |g,1\rangle^{\otimes k}$ all possible permutations, of which there are $\frac{N!}{(N-k)!\,k!}$. Note that we have not yet used Fock space here (identical bosons have not yet been symmetrized).

> This step is not very rigorous, because it does not explain from first principles why stimulated emission implies that the total quantum state is the tensor product of spontaneous-emission states $|\psi\rangle = a |e,0\rangle + b |g,1\rangle$. Our basis for obtaining this result comes entirely from the physical picture of stimulated emission.

The quantum state of the optical field is obtained by taking the partial trace of the total quantum state over the two-level systems:

$$\rho = \operatorname{Tr}_{\text{a}}[|\Psi\rangle\langle\Psi|] = C^2 \sum_k  |a^{N-k}b^k |^2  \sum_m\mathcal{P}_m[(|0\rangle\langle 0|)^{\otimes (N-k)} \otimes (|1\rangle\langle 1|)^{\otimes k}]$$

We now symmetrize the tensor product of identical particles and map it to Fock space, namely the well-known $|1\rangle ^{\otimes k} \rightarrow  \sqrt{k!} |k\rangle$, and the above expression becomes

$$\rho = C^2 \sum_k  |a^{N-k}b^k |^2 \left(\frac{N!}{(N-k)!\,k!}\right)^2 k! |k\rangle\langle k |$$

When $k \ll N$, $\frac{N!}{(N-k)!}  \sim N^k$. Let $\alpha = \frac{b}{a}N$; then the above expression can be written as:

$$\rho = C^2 a^N\sum_k \frac{|\alpha|^{2k}}{k!} |k\rangle\langle k |$$

Normalizing it yields:

$$\rho = e^{-|\alpha|^2}\sum_k \frac{|\alpha|^{2k}}{k!} |k\rangle\langle k |$$

This is a Poisson distribution with mean particle number $|\alpha|^2$. In the coherent-state representation, it can be written as:

$$\rho = \int_0^{2\pi} \frac{\mathrm{d}\theta}{2\pi} |\alpha e^{\mathrm{i}\theta}\rangle\langle\alpha e^{\mathrm{i}\theta}|$$

It can be seen that it is in fact a coherent state with a random phase. A coherent state $|\alpha\rangle$ corresponds to a classical electromagnetic wave with highly definite amplitude and phase, whereas here its phase is integrated from $0$ to $2\pi$. This reflects our ignorance of the phase information, which fundamentally originates from our ignorance of the microscopic states of the two-level systems (the gain medium). One may say that this $\rho = \rho_{\text{epistemic}}$ is an epistemic quantum state.

From an ontological perspective, however, the quantum state of the system should collapse into an $\rho_{\text{ontic}} = |\alpha\rangle$ with a definite phase; we simply have no way of knowing which phase it is. This is because, at an optical frequency of $\sim 10^{15} \text{Hz}$, humans cannot observe absolute phase. Relative phase can nevertheless be observed, and thus we can still observe interference phenomena. A simple calculation also shows this: whether one uses the mixed state $\rho = \int_0^{2\pi} \frac{\mathrm{d}\theta}{2\pi} |\alpha e^{\mathrm{i}\theta}\rangle\langle\alpha e^{\mathrm{i}\theta}|$ or the pure state $\rho = |\alpha\rangle\langle \alpha|$ to calculate the correlation function $\langle a^\dag(t)a(0)\rangle = \text{tr}[\rho a^\dag(t)a(0)]$, the result is exactly the same. This once gave rise to discussion about coherence: is coherence an illusion or a physical reality? [[1]](#ref\_1) Supporters of the former view argue that the above interpretation of “phase collapse” has a “preferred basis” problem, whereas supporters of the latter view argue that the preferred basis problem can be explained by spontaneous symmetry breaking.

## References  

1. [^](#ref\_1\_0)Bartlett, S. D., Rudolph, T. & Spekkens, R. W. Dialogue Concerning Two Views on Quantum Coherence: Factist and Fictionist. Int. J. Quantum Inform. 04, 17–43 (2006).
