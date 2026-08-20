---
title: "What is the significance of complex numbers in describing EM waves?"
date: 2024-02-15T23:46:31+08:00
originalURL: "https://www.zhihu.com/question/614307607/answer/3397335289"
aliases:
  - "/en/complex_numbers_in_em/"
  - "/en/Post_20240216_复数对于描述电磁波有什么重要性/"
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information/Quantum Optics"]
author: "Haifei"
---

In classical mechanics, complex numbers are merely a mathematical tool used to simplify calculations.

In quantum mechanics, complex numbers are not just a mathematical trick, but have a certain physical significance. Consider the classical vector potential:

$\begin{aligned} \mathbf{A}(\mathbf{r},t)=\sum_{\mathbf{k}\lambda} \left( A_{\mathbf{k}\lambda}e^{i(\mathbf{k}\cdot\mathbf{r}-\omega_{\mathbf{k}}t)} + \text{c.c.}\right)\mathbf{e}_{\mathbf{k}\lambda} \end{aligned}$ 

> where $\mathbf{k}$ and $\lambda$ represent the spatial and polarization modes respectively

Quantizing it yields the vector potential operator in the Heisenberg picture:

$\begin{aligned} \mathbf{A}(\mathbf{r},t)=\sum_{\mathbf{k}\lambda} \left( C_{\mathbf{k}\lambda}\hat{a}_{\mathbf{k}\lambda}e^{i(\mathbf{k}\cdot\mathbf{r}-\omega_{\mathbf{k}}t)} + C_{\mathbf{k}\lambda}^{*}\hat{a}^{\dag}_{\mathbf{k}\lambda} e^{i(\mathbf{k}\cdot\mathbf{r}+\omega_{\mathbf{k}}t)}\right)\mathbf{e}_{\mathbf{k}\lambda} \end{aligned}$ 

It can be seen that the part rotating clockwise corresponds to the annihilation operator $\hat{a}_{\mathbf{k}\lambda}$, while the counterclockwise rotating part corresponds to the creation operator $\hat{a}_{\mathbf{k}\lambda}^{\dag}$. Since these two operators do not commute ( $[\hat{a}_{\mathbf{k}\lambda},\hat{a}_{\mathbf{k}\lambda}^{\dag}]=1$ ), the vacuum is no longer "vacuum", but filled with fluctuations of the electromagnetic field.

> Specifically, the Hamiltonian of the electromagnetic field is:  
>  $\begin{aligned} \hat{H}&=\hbar\sum_{\mathbf{k}\lambda}\frac{\omega_\mathbf{k}}{2}\left\{\hat{a}_{\mathbf{k}\lambda},\hat{a}_{\mathbf{k}\lambda}^{\dag}\right\} \\\\ &= \hbar \sum_{\mathbf{k}\lambda}\frac{\omega_{\mathbf{k}}}{2}\left(\hat{a}_{\mathbf{k}\lambda}^{\dag}\hat{a}_{\mathbf{k}\lambda}+\hat{a}_{\mathbf{k}\lambda}\hat{a}_{\mathbf{k}\lambda}^{\dag}\right) \\\\ &= \hbar \sum_{\mathbf{k}\lambda}\frac{\omega_{\mathbf{k}}}{2}\left(\hat{a}_{\mathbf{k}\lambda}^{\dag}\hat{a}_{\mathbf{k}\lambda}+\hat{a}_{\mathbf{k}\lambda}^{\dag}\hat{a}_{\mathbf{k}\lambda} + [\hat{a}_{\mathbf{k}\lambda},\hat{a}_{\mathbf{k}\lambda}^{\dag}]\right) \\\\ &=\hbar \sum_{\mathbf{k}\lambda}\omega_{\mathbf{k}}\left(\hat{a}_{\mathbf{k}\lambda}^{\dag}\hat{a}_{\mathbf{k}\lambda} + \frac{1}{2}\right) \\\\ &= \hbar \sum_{\mathbf{k}\lambda} \omega_{\mathbf{k}}\left(\hat{n}_{\mathbf{k}\lambda}+\frac{1}{2}\right) \end{aligned}$   
> When the excitation numbers of all modes are zero, which is the vacuum state, the energy of the electromagnetic field is not zero. This is caused by vacuum fluctuations.
