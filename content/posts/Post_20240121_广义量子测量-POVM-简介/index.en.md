---
title: "Generalized Quantum Measurements: An Introduction to POVMs"
date: 2024-01-21T22:13:57+08:00
originalURL: "https://zhuanlan.zhihu.com/p/679038823"
aliases:
  - "/en/povm/"
  - "/en/Post_20240126_广义量子测量-POVM-简介/"
draft: false
tags: ["quantum measurement theory"]
categories: ["Quantum Information/Quantum Optics"]
math: true
author: "Haifei"
---

## Projective Measurements  

A measurement in the traditional sense (in the Von Neumann sense) is a collection of projection operators. By performing a spectral decomposition of the self-adjoint operator corresponding to an observable $O=\sum_i\lambda_i |\varphi_i\rangle\langle\varphi_i|$ , one obtains these projection operators $|\varphi_i\rangle\langle\varphi_i|$ . Anyone who has studied elementary quantum mechanics should be familiar with this part.

In addition to Von Neumann measurements, there is a more general type of measurement called a generalized measurement (Generalized Measurements), also known as a POVM (Positive Operator Valued Measure).

## Generalized Measurements (Generalized Measurements, POVM)  
> **Definition: POVM**  
>   
> A POVM is a mapping $\mathsf{E}: X \rightarrow \mathcal{L}(\mathcal{H})$ satisfying  
> 1) $\mathsf{E}(x) \ge 0,\quad \forall x\in X$   
> 2) $\sum_{x\in X}\mathsf{E}(x) = \mathbb{I}_{\mathcal{H}}$   
> where $X$ denotes the set of finitely many possible measurement outcomes, and $\mathcal{L}(\mathcal{H})$ denotes the set of all bounded operators on $\mathcal{H}$ .  
>   
> **Born Rule**  
>   
> For a quantum state $\rho$ subjected to the measurement specified by the POVM $\mathsf{E}$ , the probability of obtaining outcome $x$ is $p_{\rho}^{\mathsf{E}}(x) = \operatorname{tr}[\rho \mathsf{E}(x)]$

Note that a measurement in the traditional sense is a projection operator satisfying $\mathsf{E}(x)^2=\mathsf{E}(x),\quad \forall x\in X$ . A general POVM need not satisfy this condition and may be a weighted sum of multiple different projection operators.

In fact, traditional projective measurements are also called PVMs (Projection Valued Measures), which are a special class of POVMs.

The relationship between PVMs and POVMs is analogous to that between pure states and mixed states. That is, the elements of a POVM are statistical mixtures of elements of a PVM, just as mixed states are statistical mixtures of pure states. A mixed state can be purified into a pure state on a larger Hilbert space, while a POVM can likewise be extended by naimark dilation into a PVM on a larger space.

## Measure  

The M in POVM stands for Measure, not Measurement. An ordinary measure maps measurable sets to real numbers. A POVM (a positive-operator-valued measure) maps measurable sets to a positive operator (Positive operator). Therefore, the formal definition of a POVM is in fact:

$\mathsf{E}: \mathcal{A} \rightarrow \mathcal{L}(\mathcal{H})$ satisfying

1) $\mathsf{E}(A) \ge 0,\quad \forall A\in \mathcal{A}$

2) $\mathsf{E}(X) = \mathbb{I}_{\mathcal{H}}$

where $\mathcal{A}$ is a $\sigma$-algebra on $X$ . $(X,\mathcal{A})$ forms a measurable space.

There are two reasons for defining it this way:

First, quantum mechanics is founded on probability theory, and probability theory is founded on measure theory.

Second, when measurement outcomes are continuous, we must use this definition. Examples include position and momentum measurements.

## How to Implement a POVM  

So how can a POVM be implemented? In fact, we can use PVMs and composite systems to implement POVMs.

Consider a system with Hilbert space $\mathcal{H}$ and state $\rho$ .

Next, we couple system $\mathcal{H}$ with another system $\mathcal{K}$ . Suppose the initial state of system $\mathcal{K}$ is $\sigma$ ; then the initial state of the composite system is $\rho \otimes \sigma \in \mathcal{H} \otimes \mathcal{K}$ .

We then let the composite system evolve for some time, so that its state becomes $U(\rho\otimes \sigma) U^\dag$ .

Finally, we perform on subsystem $\mathcal{K}$ the measurement specified by the PVM $\mathsf{Z}$ . According to the Born rule, the probability of obtaining outcome $x$ is $\operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}_{\mathcal{H}}\otimes \mathsf{Z(x)})]$ .

In this way, we implement a POVM $\mathsf{E}$ satisfying $\operatorname{tr}[\rho \mathsf{E(x)}]=\operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}_{\mathcal{H}}\otimes \mathsf{Z(x)})]$ .

## Measurement Model (Measurement Model)  

Let us summarize the physical objects involved in the above implementation of a POVM: the ancillary (ancilla) system $\mathcal{K}$ , the initial state $\sigma$ of system $\mathcal{K}$ , the evolution $U$ of the composite system, and the projective measurement $\mathsf{Z}$ on the ancillary system. These physical objects implement a POVM measurement.

Thus, we can define $\mathfrak{M}=(\mathcal{K},\sigma,U,\mathsf{Z})$ and call it a measurement model (Measurement Model).

In actual experiments, the ancillary (ancilla) system $\mathcal{K}$ can be regarded as the probe of the instrument, while $\mathsf{Z}$ is the readout of the probe.

## Post-Measurement State  

A POVM itself cannot determine the post-measurement state. What actually determines the post-measurement state is the specific implementation of the measurement, namely the measurement model.

For the measurement model $\mathfrak{M}=(\mathcal{K},\sigma,U,\mathsf{Z})$ , the state of system $\mathcal{H}$ after measurement is $\rho_x=\operatorname{tr}_{\mathcal{K}}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}_{\mathcal{H}}\otimes \mathsf{Z(x)})]$ , where $\operatorname{tr}_{\mathcal{K}}[\cdot]$ denotes taking the partial trace.

## Quantum Instruments (Quantum Instruments)  

A POVM gives the probabilities of the various measurement outcomes, but does not give the post-measurement state. We therefore seek a mathematical object that incorporates both measurement probabilities and post-measurement states. This mathematical object is called a Quantum Instrument.

> **Definition: Quantum Instrument**  
>   
> We call $\mathcal{I}_{x}: \mathcal{I}_{x}(\rho) = \rho_x$ a Quantum Instrument if $\operatorname{tr}\left[\sum_{x\in X} \rho_x \right]=\operatorname{tr}[\rho]=1$ .

It can be seen that $\mathcal{I}_x$ not only gives the measurement probability $p_x=\operatorname{tr}[\rho_x]$ , but also gives the post-measurement state $\frac{\rho_x}{\operatorname{tr}[\rho_x]}$ .

Clearly, the same POVM corresponds to infinitely many Quantum Instruments.

So, can we always implement an arbitrary Quantum Instrument? The answer is yes.

> **Theorem**  
>   
> Given any Quantum Instrument, we can always find a Measurement Model to implement it (in fact, there are infinitely many). Proof omitted.
