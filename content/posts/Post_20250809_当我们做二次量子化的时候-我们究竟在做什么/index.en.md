---
title: "What Are We Actually Doing When We Perform Second Quantization?"
date: 2025-08-09T14:16:03+08:00
originalURL: "https://www.zhihu.com/question/302491973/answer/1937517474997309454"
aliases:
  - "/en/second_quantization/"
  - "/en/Post_20251012_当我们做二次量子化的时候-我们究竟在做什么/"
draft: false
tags: ["Second Quantization"]
categories: ["Quantum Information/Quantum Optics"]
author: "Haifei"
---

**First quantization cannot describe superpositions of particle number, let alone dynamics in which particle number changes.**

The terms first quantization and second quantization can easily lead one to believe that they are equivalent, and that one can use whichever is more convenient, much like the Schrödinger and Heisenberg pictures. This is not the case. The descriptive power of second quantization is strictly greater than that of first quantization. First quantization is merely a simplified description of second quantization for situations with a fixed particle number, and is intrinsically deficient.

Consider a quantum state that is an equal-weight coherent superposition of the following two cases:

1. The particle number is 1, and the wavefunction is $\psi\_1(x\_1)$
2. The particle number is 2, and the wavefunction is $\psi\_2(x\_1, x\_2)$

For such a quantum state, there is no way to write down its wavefunction. Writing it this way is clearly also incorrect:

$\psi(x\_1,x\_2) = \frac{1}{\sqrt{2}}\psi\_1(x\_1)+\frac{1}{\sqrt{2}}\psi\_2(x\_1,x\_2) \quad (\times)$

In fact, the correct expression can only be written in the language of second quantization:

$\begin{aligned} |\psi\rangle = \frac{1}{\sqrt{2}} \int \mathrm{d}x\_1 \psi\_1(x\_1) \hat{\psi}^\dagger(x\_1) |\text{vac}\rangle + \frac{1}{\sqrt{2}} \iint \frac{1}{2}\mathrm{d}x\_1\mathrm{d}x\_2 \psi\_2(x\_1,x\_2) \hat{\psi}^\dagger(x\_1)\hat{\psi}^\dagger(x\_2) | \text{vac}\rangle \end{aligned}$

Here, $\hat{\psi}^\dagger$ is the field creation operator, and $|\text{vac}\rangle$ is the vacuum state.

The reason we need only first quantization most of the time in quantum mechanics is that quantum mechanics mainly deals with nonrelativistic situations, namely low-energy-scale situations. Electrons at low energy approximately conserve particle number, and the nonconserving part can be treated as a perturbation, such as the Darwin term in hydrogen energy levels, which originates from electron-positron pair fluctuations.

On the other hand, although photon number is usually not conserved, quantum mechanics treats the photon field as a classical electromagnetic field. The classical electromagnetic field happens to approximately characterize the most commonly occurring state of light in the universe—the coherent state:

$\begin{aligned} |\alpha\_\mathbf{k}\rangle &=  \exp(-|\alpha\_\mathbf{k}|^2/2)\exp(\alpha\_\mathbf{k}\hat{a}\_\mathbf{k}) | \text{vac}\rangle \\\\ &= \exp(-|\alpha\_\mathbf{k}|^2/2) \sum\_{n=0}^{\infty} \frac{\alpha^n\_\mathbf{k}}{\sqrt{n!}} |n\_\mathbf{k}\rangle \end{aligned}$

Here, $\mathbf{k}$ denotes the spatial and polarization modes, $\hat{a}\_\mathbf{k}$ is the creation operator for mode $\mathbf{k}$, $|n\_\mathbf{k}\rangle$ is the $n$-particle number state of mode $\mathbf{k}$, and $\alpha\_\mathbf{k} \in \mathbb{C}$ describes the amplitude and phase of mode $\mathbf{k}$. Thus, with the electromagnetic field $A$ as a superposition of different $\mathbf{k}$ modes, its corresponding quantum state can be written as:

$\begin{aligned} |A\rangle = \exp\left(-\frac{1}{2}\sum\_{\mathbf{k}}|\alpha\_\mathbf{k}|^2\right)\exp\left(\sum\_{\mathbf{k}}\alpha\_\mathbf{k}\hat{a}\_\mathbf{k}\right) | \text{vac}\rangle \end{aligned}$

It can be shown that this is a minimum-uncertainty state for the electric-field and magnetic-field operators, corresponding to a macroscopic classical electromagnetic wave.

Photons are easily lost through scattering and absorption, and the states that survive the loss dynamics are coherent states, namely eigenstates of the Lindblad operator—the annihilation operator.

For a light field in a coherent state, its quantumness manifests itself only when the particle number is very low, that is, close to the vacuum, as in the Lamb shift of hydrogen energy levels and so on. Such effects are usually very weak and can be treated as corrections based on classical electromagnetic waves. This is why light fields have difficulty exhibiting macroscopic quantumness, and why quantum mechanics can be so successful even when using classical electromagnetic fields.

However, once photons become entangled with one another, or photons become entangled with electrons, the light field can no longer be described by a classical electromagnetic field.

In short, quantum mechanics (first quantization) is only an approximate theory with inherent deficiencies: it cannot describe superpositions of particle number, and a complete description must use quantum field theory (second quantization).

Returning to the question: when we perform second quantization, what are we doing? The answer is simple: we are doing what we should and must do.
