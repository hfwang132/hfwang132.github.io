---
title: "Wave Function of Photons"
date: 2024-03-10T02:21:37+08:00
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---


The wave function of a photon in the spacetime representation is:

$\Psi(\mathbf{r},t)=\langle \mathbf{r},t|\psi\rangle=\langle 0 |E^{+}(\mathbf{r},t)|\psi\rangle$

Where $\begin{aligned} |\mathbf{r},t\rangle = E^{-}(\mathbf{r},t) |0\rangle = \sum_{\mathbf{k},\lambda} \sqrt{\frac{\hbar \omega}{2 \epsilon_0 V}} e^{\mathrm{i}(\mathbf{k}\cdot \mathbf{r}-\omega_{\mathbf{k}} t)} a^\dag_{\mathbf{k},\lambda} |0\rangle \end{aligned}$.

Intuitively, this is to let the field operator $E^{-}(\mathbf{r},t)$ create a state $|\mathbf{r},t\rangle$ at the spacetime point $(\mathbf{r},t)$, and then calculate the overlap between this state and $|\psi\rangle$.

When we talk about the spacetime modes of photons, such as Gaussian pulses, hyperbolic secant pulses, etc., we are actually referring to the wave function in the spacetime representation described above.

Of course, this wave function is not in the "Schrödinger sense" because the Schrödinger equation belongs to non-relativistic quantum mechanics, while photons are relativistic particles.

When we say that photons do not have a well-defined wave function, we are actually saying that they do not have a well-defined position operator. But we do have field operators $E^{\pm}(\mathbf{r},t)$, so we don't need a position operator either.