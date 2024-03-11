---
title: "光子有波函数吗？"
date: 2024-03-09T17:37:15+08:00
draft: false
tags: ["量子光学"]
categories: ["量子信息"]
---

光子有时空表象下的波函数：

$\Psi(\mathbf{r},t)=\langle \mathbf{r},t|\psi\rangle=\langle 0 |E^{+}(\mathbf{r},t)|\psi\rangle$ 

其中 $\begin{aligned} |\mathbf{r},t\rangle = E^{-}(\mathbf{r},t) |0\rangle = \sum\_{\mathbf{k},\lambda} \sqrt{\frac{\hbar \omega}{2 \epsilon\_0 V}} e^{\mathrm{i}(\mathbf{k}\cdot \mathbf{r}-\omega\_{\mathbf{k}} t)} a^\dag\_{\mathbf{k},\lambda} |0\rangle \end{aligned}$ 。

直观来看，就是让场算符 $E^{-}(\mathbf{r},t)$ 在时空点 $(\mathbf{r},t)$ 处创造一个态 $|\mathbf{r},t\rangle$ ，再求这个态和 $|\psi\rangle$ 之间的 overlap。

当我们说到光子的时空模式时，例如高斯脉冲，双曲正割脉冲等等，我们实际上说的就是上述的时空表象下的波函数。

当然，这个波函数不是“薛定谔意义上”的波函数，因为薛定谔方程属于非相对论量子力学，而光子是相对论粒子。



---

当我们说光子没有良定义的波函数时，我们实际上说的是它没有良定义的位置算符。但是我们有场算符 $E^{\pm}(\mathbf{r},t) $ 呀，所以也不需要位置算符。

---

光子波函数的说法在文献中是很常见的，举几个例子：

[1] Xu, Y., Choudhary, S. & Boyd, R. W. Efficient Measurement of the Bi-photon Spatial Mode Entanglement with Stimulated Emission Tomography. Preprint at http://arxiv.org/abs/2403.05036 (2024).

[2] Tian, Z., Liu, Q., Tian, Y. & Gu, Y. Wavepacket interference of two photons: from temporal entanglement to wavepacket shaping. Preprint at http://arxiv.org/abs/2403.04432 (2024).

[3] Moura, A. G. da C. & Monken, C. H. Einstein-Podolsky-Rosen correlations in spontaneous parametric down-conversion: Beyond the Gaussian approximation. Preprint at http://arxiv.org/abs/2403.04561 (2024).