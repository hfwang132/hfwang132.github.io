---
title: "[Quantum Optics Experiments Miscellany · II] Measuring Spectral Correlations and Purity of SPDC Multimode Squeezed States with an HBT Experiment"
date: 2024-02-05T00:10:15+08:00
originalURL: "https://zhuanlan.zhihu.com/p/679054571"
aliases:
  - "/en/HBT_spectral_correlation/"
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information/Quantum Optics"]
math: true
author: "Haifei"
---

In the previous article, we discussed the principle of using non-photon-number-resolving single-photon detectors to measure the quantum second-order correlation function in an HBT experiment.

[[Quantum Optics Experiments Miscellany · I] The Principle of Measuring the Second-Order Correlation Function (g2) with Single-Photon Detectors](https://zhuanlan.zhihu.com/p/679453473)

In this article, let us look at the uses of the quantum second-order correlation function. In addition to its well-known use for distinguishing [super-Poissonian statistics/Poissonian statistics/sub-Poissonian statistics] and [photon bunching/antibunching], an HBT experiment can also be used to measure the spectral purity of multimode squeezed states.

## SPDC Generates Multimode Squeezed States  

SPDC (Spontaneous Parametric Down-Conversion) is an experimental method for generating correlated photon pairs. When a laser beam is directed onto a nonlinear crystal, spontaneous parametric down-conversion occurs if the phase-matching condition is satisfied. In this process, one pump photon is converted into two photons of equal frequency, called the signal photon and idler photon, respectively, satisfying energy and momentum conservation. Its Hamiltonian is as follows:

$$H = i\hbar g\,a^\dag_s a^\dag_i a_p + h.c.$$

where $g$ represents the interaction strength.

When the pump light is sufficiently strong that its intensity is almost not depleted, we can focus only on the sub-Hilbert space of the signal and idler photons. The Hamiltonian is then:

$$H = i\hbar g \alpha_p \,a^\dag_s a^\dag_i + h.c.$$

Without loss of generality, let $\alpha_p$ be real, and let $\chi=g\alpha_p$ , then

$$H = i\hbar \chi (a^\dag_s a^\dag_i - a_sa_i)$$

In fact, because the spatial extent of the pump interaction is finite, momentum has uncertainty, which manifests as a certain linewidth in the spectrum. The Hamiltonian is then as follows:

$$\begin{aligned} H=i\hbar \chi \int d\omega_s d\omega_i [f(\omega_s,\omega_i) a_s^\dag(\omega_s) a_i^\dag(\omega_i) -f^*(\omega_s,\omega_i) a_s(\omega_s) a_i(\omega_i)] \end{aligned}$$

We now expand $f(\omega_s,\omega_i)$ using a set of orthogonal basis functions $\{\varphi_k\}_{k\in \mathbb{N}}$ of $L^2(\mathbb{R^2})$ (e.g., Hermite functions):

$$\begin{aligned} f(\omega_s,\omega_i)=\sum_{k,l} C_{kl}\varphi_k(\omega_s)\varphi_l(\omega_i) \end{aligned}$$

and define $a_k^\dag = \int d\omega_s \,\varphi_k(\omega_s)a_s^\dag(\omega_s),\quad b_k^\dag = \int d\omega_i \,\varphi_k(\omega_i) a_i^\dag(\omega_i)$ , then

$$\begin{aligned} H=i\hbar \chi \sum_{k,l}\left( C_{kl}a^\dag_k b^\dag_l - C^*_{kl} a_kb_l\right) \end{aligned}$$

Performing a Schmidt decomposition (singular value decomposition) yields

$$\begin{aligned} H=i\hbar \chi \sum_{k}\left( \lambda_k A^\dag_k B^\dag_k - \lambda_k A_k B_k\right) \end{aligned}$$

where $\sum_k\lambda^2_k=1$ .

> Note: Since the spectrum from singular value decomposition is always nonnegative and real, $\lambda_k$ is real and greater than zero.

This is in fact the Hamiltonian of a multimode squeezed state.

> Let us review the various squeezed states:  
> Single-mode squeezed state: $\begin{aligned} H=i\hbar\left(g^*\frac{a^2}{2}-g\frac{a^{\dag2}}{2}\right) \end{aligned}$   
> Two-mode squeezed state: $\begin{aligned} H=i\hbar\left(g^*a b-g a^\dag b^\dag\right) \end{aligned}$   
> Multimode squeezed state: $\begin{aligned} H=i\hbar\sum_{k}\left(g_k^*a_k b_k-g_k a_k^\dag b_k^\dag\right) \end{aligned}$

Now let us examine the system evolution in the Schrödinger and Heisenberg pictures, respectively.

In the Schrödinger picture,

$$\begin{aligned} |\Psi_{\text{out}}\rangle &=e^{\frac{H\tau}{i\hbar}}|\Psi_{\text{in}}\rangle \\ &= \sum_{k} \frac{1}{\cosh(r_k)}\sum_{n=0}^{\infty}\tanh^n(r_k)|n_k,n_k\rangle \end{aligned}$$

where $r_k=\chi \tau \lambda_k$ . Note that it has the form of a thermal optical field.

When $r_k$ is very small, we have

$$|\Psi_{\text{out}}\rangle\approx \sum_{k} \left(|0_k,0_k\rangle + r_k|1_k,1_k\rangle\right)$$

> This is also the case in most experiments.  
> Conditional on detecting a photon, the conditional quantum state (Conditional State) is $|\Psi_\text{conditional}\rangle=\sum_k\lambda_k|1_k,1_k\rangle$ . This is the principle of a heralded single-photon source.

In the Heisenberg picture,

$$\begin{aligned} A_k &\rightarrow e^{\frac{H\tau}{i\hbar}} A_k e^{-\frac{H\tau}{i\hbar}} \\ &= A_k + [e^{\frac{H\tau}{i\hbar}},A_k]+[e^{\frac{H\tau}{i\hbar}},[e^{\frac{H\tau}{i\hbar}},A_k]] + \cdots \\ &=\cosh(r_k) A_k - \sinh(r_k)B_k^\dag \end{aligned}$$

$$\begin{aligned} B_k &\rightarrow e^{\frac{H\tau}{i\hbar}} B_k e^{-\frac{H\tau}{i\hbar}} \\ &= B_k + [e^{\frac{H\tau}{i\hbar}},B_k]+[e^{\frac{H\tau}{i\hbar}},[e^{\frac{H\tau}{i\hbar}},B_k]] + \cdots \\ &=\cosh(r_k) B_k - \sinh(r_k)A_k^\dag \end{aligned}$$

where $r_k=\chi \tau \lambda_k$ .

## How Can Spectral Correlations Be Characterized?  

Spectral correlation refers to the correlation between the spectra of the signal and idler photons. An uncorrelated joint spectrum can be written as the product of the individual spectra of the two photons: $f(\omega_s,\omega_i)=\phi(\omega_s)\psi(\omega_i)$ . If it cannot be written in this form, it means that spectral correlations are present.

How exactly can spectral correlations be characterized? We can use the Schmidt number to characterize the degree of spectral correlation, defined as follows:

$$\begin{aligned} K= \frac{1}{\sum_k\lambda^4_k} \end{aligned}$$

> **Example**  
> For an uncorrelated joint spectrum, $\{\lambda_k\}=\{1\}$ , $K=1$ .  
> For a joint spectrum with two modes and equal coefficients, $\{\lambda_k\}=\{\frac{1}{2},\frac{1}{2}\}$ , $K=2$ .  
> For a joint spectrum with n modes and equal coefficients, $K=n$ .  
> For a joint spectrum with n modes whose coefficients are not all equal, $1\lt K\lt n$ .

Why do we care about spectral correlations? This is because they are closely related to photon purity:

> **Property**  
> When $r_k$ is very small and conditional on detecting a photon, the quantum state is $|\Psi_\text{conditional}\rangle=\sum_k\lambda_k|1_k,1_k\rangle$ .  
> For this quantum state, tracing out one of the two photons (performing a partial trace), the purity of the quantum state of the remaining photon is $P=\frac{1}{K}$ . This is because:  
> $\begin{aligned} P &= \operatorname{tr}[\operatorname{tr}_2[|\psi\rangle\langle\psi|]^2] \\  &=  \operatorname{tr}\left[\operatorname{tr}_B\left(\sum_{k}\lambda_k \left| 1_k, 1_k\right\rangle\sum_{l}\lambda_l \left\langle 1_l ,1_l\right|\right)^2\right] \\ &= \operatorname{tr}\left[\left(\sum_{k}\lambda_k^2 \left|1_k \right\rangle\left\langle 1_k\right|\right)^2\right] \\ &= \operatorname{tr}\left[\sum_{k}\left(\lambda_k^2\left| 1_k \right\rangle\left\langle 1_k\right|\right)^2\right] \\ &= \operatorname{tr}\left[\sum_{k}\lambda_k^4 |1_k\rangle\langle 1_k|\right] \\ &=\sum_{k}\lambda_k^4=\frac{1}{K} \end{aligned}$

It can be seen that purity is inversely proportional to the Schmidt number. In other words, the stronger the spectral correlation, the lower the purity of the photon in the frequency domain. This is detrimental to heralded single-photon sources and various multiphoton interference experiments. For the former, spectral correlations reduce the spectral indistinguishability of single photons; for the latter, spectral correlations reduce interference visibility.

## Measuring Spectral Correlations with an HBT Experiment  

In the previous article, we mentioned that an HBT experiment measures:

$$\begin{aligned} \frac{C_{12}R}{S_1S_2}=\frac{\langle n(n-1)\rangle}{\langle n\rangle^2} \end{aligned}$$

where $C_{12}$ is the coincidence count rate of the two detectors, $S_1$ and $S_2$ are the count rates of the first and second detectors, respectively, and $R$ is the photon flux.

> When the frequencies of the modes are identical or close, $\begin{aligned} \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} \approx g^{(2)}(0) \end{aligned}$ .

We say that spectral correlations can be measured with an HBT experiment because $\begin{aligned} \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} = 1+\frac{1}{K} \end{aligned}$ . The proof is as follows:

$$\begin{aligned} \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} &=\frac{\langle n^2\rangle-\langle n\rangle}{\langle n\rangle^2} \\ &=\frac{\sum_{k} \langle n_k^2 \rangle + 2\sum_{i\gt j} \langle n_i n_j \rangle - \langle n\rangle}{\langle n\rangle^2} \\ &= \frac{ \sum_{k} \left(\langle n_k \rangle + 2\langle n_k\rangle^2 \right) + 2\sum_{i\gt j} \langle n_i \rangle \langle n_j \rangle  - \langle n\rangle}{\langle n\rangle^2} \\ &= \frac{\langle n\rangle + \langle n\rangle^2 +\sum_{k} \langle n_k\rangle^2 - \langle n\rangle}{\langle n\rangle^2} \\ &= 1+\frac{\sum_{k} \langle n_k\rangle^2}{ \left\langle \sum_{k} n_k\right\rangle^2} \\ &= 1 + \frac{\sum_k \sinh^4(r_k)}{\left(\sum_k \sinh^2(r_k)\right)^2} \\ &\approx 1+\frac{\sum_k r_k^4}{\left(\sum_k r_k^2\right)^2} \\ &= 1 + \frac{\sum_k \lambda_k^4}{\left(\sum_k \lambda_k^2\right)^2} \\ &= 1+\sum_k \lambda_k^4 \\ &= 1+\frac{1}{K} \\ &= 1+P \end{aligned}$$

In the third equality, we used the result that for a thermal optical field, $ \langle n_k^2 \rangle =\langle n_k \rangle + 2\langle n_k\rangle^2$ , and that there is no correlation between the modes, $\langle n_i n_j\rangle=\langle n_i\rangle\langle n_j\rangle$ .

The sixth equality follows because, in the Heisenberg picture:

$$\begin{aligned} \langle n_k\rangle&=\langle 0|A_k^\dag A_k|0\rangle \\ &\rightarrow\langle 0| (\cosh(r_k) A_k^\dag - \sinh(r_k)B_k)(\cosh(r_k) A_k - \sinh(r_k)B_k^\dag)|0\rangle \\ &= \sinh^2(r_k) \end{aligned}$$

## Conclusion  

With the help of an HBT experiment, we can measure spectral correlations and purity, which is quite remarkable. Ordinary methods require a tunable filter to measure the JSI (Joint Spectral Intensity), and then use the JSI to calculate spectral correlations and purity. An HBT experiment, however, does not even require a filter, demonstrating the advantages of the HBT experiment.

## Notes  

The earliest reference I could find for the above derivation is [1], but reference [1] skips too many steps; I filled in the intermediate logical chain bit by bit myself.

References on measuring spectral correlations using an HBT experiment are [2] and [3], both of which cite reference [1].

## References  

[1] Christ, A., Laiho, K., Eckstein, A., Cassemiro, K. N. & Silberhorn, C. Probing multimode squeezing with correlation functions. *New J. Phys.* **13**, 033027 (2011).

[2] Faruque, I. I. *et al.* Estimating the Indistinguishability of Heralded Single Photons Using Second-Order Correlation. *Phys. Rev. Applied* **12**, 054029 (2019).

[3] Paesani, S. *et al.* Near-ideal spontaneous photon sources in silicon quantum photonics. *Nat Commun* **11**, 2505 (2020).
