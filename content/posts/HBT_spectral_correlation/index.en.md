---
title: "Probing the spectral purity with unheralded g2 measurements in HBT experiment"
date: 2024-03-10T02:22:34+08:00
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

In the previous section, we discussed the principle of measuring the quantum second-order correlation function with a non-photon-number-resolving single-photon detector in the HBT experiment.

[https://zhuanlan.zhihu.com/p/679453473](https://zhuanlan.zhihu.com/p/679453473)  
In this section, let's see what the quantum second-order correlation function is used for. In addition to the common uses such as distinguishing between super-Poissonian statistics/Poissonian statistics/sub-Poissonian statistics and distinguishing between photon bunching/anti-bunching, the HBT experiment can also be used to measure the spectral purity of multimode squeezed states.

## Generation of Multimode Squeezed States via SPDC  
SPDC (Spontaneous Parametric Down-Conversion) is an experimental method used to generate correlated photon pairs. By shining a laser onto a nonlinear crystal, spontaneous parametric down-conversion occurs if the phase matching condition is satisfied. In this process, one pump photon is converted into two photons with equal frequencies, known as the signal photon and the idler photon, respectively, satisfying energy conservation and momentum conservation. The Hamiltonian for this process is given by:

$H = i\hbar g\,a^\dag\_s a^\dag\_i a\_p + h.c.$ 

where $g$ represents the interaction strength.

When the pump photon is strong enough that its intensity is almost unaffected, we can focus only on the subspace of signal and idler photons. In this case, the Hamiltonian becomes:

$H = i\hbar g \alpha\_p \,a^\dag\_s a^\dag\_i + h.c.$ 

Without loss of generality, let $\alpha\_p$ be a real number, and let $\chi=g\alpha\_p$. Then,

$H = i\hbar \chi (a^\dag\_s a^\dag\_i - a\_s a\_i)$ 

In reality, due to the finite spatial extent of the pump, there will be uncertainty in momentum, manifested as a finite linewidth in the spectrum. In this case, the Hamiltonian becomes:

$\begin{aligned} H=i\hbar \chi \int d\omega\_s d\omega\_i [f(\omega\_s,\omega\_i) a\_s^\dag(\omega\_s) a\_i^\dag(\omega\_i) -f^\*(\omega\_s,\omega\_i) a\_s(\omega\_s) a\_i(\omega\_i)] \end{aligned}$ 

Now, we expand $f(\omega\_s,\omega\_i)$ using a set of orthogonal basis functions (e.g., Hermite functions) $\{\varphi\_k\}\_{k\in \mathbb{N}}$:

$\begin{aligned} f(\omega\_s,\omega\_i)=\sum\_{k,l} C\_{kl}\varphi\_k(\omega\_s)\varphi\_l(\omega\_i) \end{aligned}$ 

and denote $a\_k^\dag = \int d\omega\_s \,\varphi\_k(\omega\_s)a\_s^\dag(\omega\_s),\quad b\_k^\dag = \int d\omega\_i \,\varphi\_k(\omega\_i) a\_i^\dag(\omega\_i)$ , then we have

$\begin{aligned} H=i\hbar \chi \sum\_{k,l}\left( C\_{kl}a^\dag\_k b^\dag\_l - C^\*\_{kl} a\_kb\_l\right) \end{aligned}$ 

Performing a Schmidt decomposition (singular value decomposition) on it, we get

$\begin{aligned} H=i\hbar \chi \sum\_{k}\left( \lambda\_k A^\dag\_k B^\dag\_k - \lambda\_k A\_k B\_k\right) \end{aligned}$ 

where $\sum\_k\lambda^2\_k=1$.


> Note: Since the spectrum of singular value decomposition is always non-negative real numbers, $\lambda\_k$ is real and greater than zero.

This is actually the Hamiltonian of multimode squeezed states.

> Review of various squeezed states:  
> Single-mode squeezed state: $\begin{aligned} H=i\hbar\left(g^\*\frac{a^2}{2}-g\frac{a^{\dag2}}{2}\right) \end{aligned}$   
> Two-mode squeezed state: $\begin{aligned} H=i\hbar\left(g^\*a b-g a^\dag b^\dag\right) \end{aligned}$   
> Multimode squeezed state: $\begin{aligned} H=i\hbar\sum\_{k}\left(g\_k^\*a\_k b\_k-g\_k a\_k^\dag b\_k^\dag\right) \end{aligned}$ 

Now let's separately look at the system evolution in the Schrödinger picture and the Heisenberg picture.

In the Schrödinger picture,

$\begin{aligned} |\Psi\_{\text{out}}\rangle &=e^{\frac{H\tau}{i\hbar}}|\Psi\_{\text{in}}\rangle \\\\ &= \sum\_{k} \frac{1}{\cosh(r\_k)}\sum\_{n=0}^{\infty}\tanh^n(r\_k)|n\_k,n\_k\rangle \end{aligned}$ 

where $r\_k=\chi \tau \lambda\_k$ . Note that it resembles a thermal light field.

When $r\_k$ is small, we have 

$|\Psi\_{\text{out}}\rangle\approx \sum\_{k} \left(|0\_k,0\_k\rangle + r\_k|1\_k,1\_k\rangle\right)$ 


> This is also the case that most experiments conform to.  
> Conditioned on detecting photons, the conditional state is $|\Psi\_{\text{conditional}}\rangle=\sum\_k\lambda\_k|1\_k,1\_k\rangle$ . This is the principle of heralded single-photon sources.

In the Heisenberg picture,

$\begin{aligned} A\_k &\rightarrow e^{\frac{H\tau}{i\hbar}} A\_k e^{-\frac{H\tau}{i\hbar}} \\\\ &= A\_k + [e^{\frac{H\tau}{i\hbar}},A\_k]+[e^{\frac{H\tau}{i\hbar}},[e^{\frac{H\tau}{i\hbar}},A\_k]] + \cdots \\\\ &=\cosh(r\_k) A\_k - \sinh(r\_k)B\_k^\dag \end{aligned}$ 

$\begin{aligned} B\_k &\rightarrow e^{\frac{H\tau}{i\hbar}} B\_k e^{-\frac{H\tau}{i\hbar}} \\\\ &= B\_k + [e^{\frac{H\tau}{i\hbar}},B\_k]+[e^{\frac{H\tau}{i\hbar}},[e^{\frac{H\tau}{i\hbar}},B\_k]] + \cdots \\\\ &=\cosh(r\_k) B\_k - \sinh(r\_k)A\_k^\dag \end{aligned}$ 

where $r\_k=\chi \tau \lambda\_k$ .

## How to Characterize Spectral Correlation?  
Spectral correlation refers to the correlation between the spectra of the signal photon and the idler photon. An uncorrelated joint spectrum can be written as the product of the spectra of the two photons: $f(\omega\_s,\omega\_i)=\phi(\omega\_s)\psi(\omega\_i)$ . If it cannot be written in this form, it implies spectral correlation.

How to characterize spectral correlation specifically? We can use the Schmidt number to quantify the degree of spectral correlation, defined as follows:

$\begin{aligned} K= \frac{1}{\sum\_k\lambda^4\_k} \end{aligned}$ 


> **Example**  
> For an uncorrelated joint spectrum, $\{\lambda\_k\}=\{1\}$ , $K=1$ .  
> For a joint spectrum with two modes and equal coefficients, $\{\lambda\_k\}=\{\frac{1}{2},\frac{1}{2}\}$ , $K=2$ .  
> For a joint spectrum with n modes and equal coefficients, $K=n$ .  
> For a joint spectrum with n modes and coefficients not completely equal to each other, $1<K<n$ .

Why do we care about spectral correlation? Because it is closely related to the purity of photons:


> **Property**  
> When $r\_k$ is small and photons are detected, the quantum state is $|\Psi\_{\text{conditional}}\rangle=\sum\_k\lambda\_k|1\_k,1\_k\rangle$ .  
> For this quantum state, tracing out one of the two photons (performing partial trace operation), the purity of the remaining photon state is $P=\frac{1}{K}$ . This is because:  
> $\begin{aligned} P &= \operatorname{tr}[\operatorname{tr}\_2[|\psi\rangle\langle\psi|]^2] \\\\  &=  \operatorname{tr}\left[\operatorname{tr}\_B\left(\sum\_{k}\lambda\_k \left| 1\_k, 1\_k\right\rangle\sum\_{l}\lambda\_l \left\langle 1\_l ,1\_l\right|\right)^2\right] \\\\ &= \operatorname{tr}\left[\left(\sum\_{k}\lambda\_k^2 \left|1\_k \right\rangle\left\langle 1\_k\right|\right)^2\right] \\\\ &= \operatorname{tr}\left[\sum\_{k}\left(\lambda\_k^2\left| 1\_k \right\rangle\left\langle 1\_k\right|\right)^2\right] \\\\ &= \operatorname{tr}\left[\sum\_{k}\lambda\_k^4 |1\_k\rangle\langle 1\_k|\right] \\\\ &=\sum\_{k}\lambda\_k^4=\frac{1}{K} \end{aligned}$ 

It can be seen that the purity is inversely proportional to the Schmidt number. That is, the stronger the spectral correlation, the lower the purity of the photons in the frequency domain. This is unfavorable for heralded single-photon sources and various multi-photon interference experiments. For the former, spectral correlation will reduce the frequency-domain indistinguishability of single photons, and for the latter, spectral correlation will reduce the interference contrast.

## Measuring Spectral Correlation with HBT Experiment  
In the previous section, we mentioned that the HBT experiment detects:

$\begin{aligned} \frac{C\_{12}R}{S\_1S\_2}=\frac{\langle n(n-1)\rangle}{\langle n\rangle^2} \end{aligned}$ 

where $C\_{12}$ is the coincidence count rate of two detectors, $S\_1$ and $S\_2$ are the count rates of the first and second detectors, respectively, and $R$ is the photon flux.


> When the frequencies of various modes are the same or similar, $\begin{aligned} \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} \approx g^{(2)}(0) \end{aligned}$ .

The reason why we say that the HBT experiment can measure spectral correlation is because $\begin{aligned} \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} = 1+\frac{1}{K} \end{aligned}$ . The proof is as follows:

$\begin{aligned} \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} &=\frac{\langle n^2\rangle-\langle n\rangle}{\langle n\rangle^2} \\\\ &=\frac{\sum\_{k} \langle n\_k^2 \rangle + 2\sum\_{i>j} \langle n\_i n\_j \rangle - \langle n\rangle}{\langle n\rangle^2} \\\\ &= \frac{ \sum\_{k} \left(\langle n\_k \rangle + 2\langle n\_k\rangle^2 \right) + 2\sum\_{i>j} \langle n\_i \rangle \langle n\_j \rangle  - \langle n\rangle}{\langle n\rangle^2} \\\\ &= \frac{\langle n\rangle + \langle n\rangle^2 +\sum\_{k} \langle n\_k\rangle^2 - \langle n\rangle}{\langle n\rangle^2} \\\\ &= 1+\frac{\sum\_{k} \langle n\_k\rangle^2}{ \left\langle \sum\_{k} n\_k\right\rangle^2} \\\\ &= 1 + \frac{\sum\_k \sinh^4(r\_k)}{\left(\sum\_k \sinh^2(r\_k)\right)^2} \\\\ &\approx 1+\frac{\sum\_k r\_k^4}{\left(\sum\_k r\_k^2\right)^2} \\\\ &= 1 + \frac{\sum\_k \lambda\_k^4}{\left(\sum\_k \lambda\_k^2\right)^2} \\\\ &= 1+\sum\_k \lambda\_k^4 \\\\ &= 1+\frac{1}{K} \\\\ &= 1+P \end{aligned}$ 

where the third equality uses the result: for thermal light fields, $\langle n\_k^2 \rangle =\langle n\_k \rangle + 2\langle n\_k\rangle^2$ , and there is no correlation between different modes $\langle n\_i n\_j\rangle=\langle n\_i\rangle\langle n\_j\rangle$ .

The sixth equality is because in the Heisenberg picture,

$\begin{aligned} \langle n\_k\rangle&=\langle 0|A\_k^\dag A\_k|0\rangle \\\\ &\rightarrow\langle 0| (\cosh(r\_k) A\_k^\dag - \sinh(r\_k)B\_k)(\cosh(r\_k) A\_k - \sinh(r\_k)B\_k^\dag)|0\rangle \\\\ &= \sinh^2(r\_k) \end{aligned}$ 

## Conclusion  
With the help of the HBT experiment, we can measure spectral correlation and purity, which is quite remarkable. Because ordinary methods require tunable filters to measure JSI (Joint Spectral

## Note  
The earliest literature I could find for the derivation above is [1], but the literature [1] skips too many steps, and the logical chain in between was filled in by myself.

The literature on measuring spectral correlation using HBT experiments can be found in [2] and [3], both of which cite literature [1].

## References  
[1] Christ, A., Laiho, K., Eckstein, A., Cassemiro, K. N. & Silberhorn, C. Probing multimode squeezing with correlation functions. *New J. Phys.* **13**, 033027 (2011).

[2] Faruque, I. I. *et al.* Estimating the Indistinguishability of Heralded Single Photons Using Second-Order Correlation. *Phys. Rev. Applied* **12**, 054029 (2019).

[3] Paesani, S. *et al.* Near-ideal spontaneous photon sources in silicon quantum photonics. *Nat Commun* **11**, 2505 (2020).  