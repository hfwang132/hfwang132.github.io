---
title: "How Are Creation and Annihilation Operators Derived?"
date: 2024-05-27T17:47:25+08:00
draft: false
tags: ["Mathematical Methods in Physics"]
categories: ["Quantum Information"]
---

The motivation for defining creation and annihilation operators is simple and can be entirely derived from classical mechanics.

Think about how we solve the classical harmonic oscillator. Since position and momentum are coupled:

$\begin{cases} \frac{\mathrm{d}x}{\mathrm{d}t} = \omega p \\\\ \frac{\mathrm{d}p}{\mathrm{d}t} = -\omega x \end{cases}$

That is,

$\frac{\mathrm{d}}{\mathrm{d}t} \begin{bmatrix} x \\\\ p \end{bmatrix} = \begin{bmatrix} 0 & \omega \\\\ -\omega & 0 \end{bmatrix} \begin{bmatrix} x \\\\ p \end{bmatrix}$

So, we just need to decouple them. By diagonalizing, we obtain the eigenvectors $a^{\pm} = x \pm \mathrm{i} p$, and the derivatives of $a^{\pm}$ only depend on themselves:

$\frac{\mathrm{d}a^{\pm}}{\mathrm{d}t} = \mp \mathrm{i} \omega a^{\pm}, \quad a^{\pm} = a_0^{\pm} \exp (\mp \mathrm{i} \omega t)$

In this procedure, $a^{+}$ and $a^{-}$, when quantized, become the annihilation and creation operators.

> Note that $a^{+} \rightarrow \hat{a}, \quad a^{-} \rightarrow \hat{a}^\dag$, then $[\hat{a}, \hat{a}^\dag] = [\hat{x} + \mathrm{i}\hat{p}, \hat{x} - \mathrm{i}\hat{p}] = -\mathrm{i}[\hat{x}, \hat{p}] = 1$.
>   
> The rest of the story is well known.

The multimode case is also simple. Each time we decouple an eigenvector, we call it a mode, corresponding to the creation and annihilation operators for that mode. This is how quasiparticles (like phonons) originate.

In classical mechanics, $a^{+}$ and $a^{-}$ are just techniques extended to the complex domain for convenience in solving problems. In quantum mechanics, however, they have tangible physical meanings. Hence, quantum mechanics cannot do without complex numbers.
