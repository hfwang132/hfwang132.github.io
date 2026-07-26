---
title: "A Fully Quantum Theory of Lasers"
date: 2024-05-31T21:45:30+08:00
originalURL: "https://zhuanlan.zhihu.com/p/700952618"
aliases:
  - "/en/laser_quantum2/"
  - "/en/Post_20240719_激光的全量子理论/"
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

> Most materials introducing lasers derive them in a classical or semiclassical framework. What, then, does a fully quantum theory of lasers look like? And what is it useful for?

This article briefly introduces the Scully\-Lamb theory of lasers. It is a fully quantum theory. Since it is generally introduced only in the final chapters of quantum optics textbooks, and since the (semi-)classical theory also works well in most cases, not many people are familiar with the Scully\-Lamb theory.

The Scully\-Lamb theory makes more accurate predictions for the photon-number distribution when the pump strength is below or near threshold, something that (semi-)classical theories cannot do.

The structure of this article is as follows:

Section 1 introduces the Jaynes\-Cummings model, which handles the interaction between an optical field and a two-level system.

Section 2 introduces the Lindblad master equation, which handles the interaction between an optical field and a thermal reservoir.

Section 3 derives the Scully\-Lamb theory. It is simply the result of the Jaynes\-Cummings model and the Lindblad master equation acting together.

For simplicity, this article sets $\hbar = 1$ .

## 1. Jaynes\-Cummings Model (JCM)  
(Readers familiar with the JCM may skip this section)


> The JCM describes the coupling between a single-mode optical field and a two-level system. Since it also quantizes the optical field, it is a fully quantum model.  
>   
> In addition to quantizing the optical field, the JCM also makes the dipole approximation (Dipole Approximation) and the rotating-wave approximation (Rotating\-Wave Approximation, RWA) to facilitate its solution. This process is beyond the scope of this article; interested readers may consult textbooks and online resources.

Let the Hilbert space of the single-mode optical field be $\mathcal{H} \cong L^{2}(\mathbb{R})$ and that of the two-level system be $\mathcal{K} \cong \mathbb{C}^2$ . Then the Jaynes\-Cumming Hamiltonian $H \in \mathcal{L}(\mathcal{H}\otimes \mathcal{K})$ is as follows:

$\begin{aligned} H&= \underbrace{\omega \left(a^\dag a+\frac{1}{2}\right)}\_{\text{field}}+ \underbrace{\omega\_a \frac{\sigma\_z}{2}}\_{\text{atom}} +  \underbrace{\Omega(\sigma\_+ a + \sigma\_- a^{\dag})}\_{\text{atom-field coupling}} \\\\ &= \underbrace{\omega \left(a^\dag a+\frac{1}{2}+\frac{\sigma\_z}{2}\right)}\_{H\_0} + \underbrace{\frac{\Delta}{2} \sigma\_z + \Omega(\sigma\_+ a + \sigma\_- a^{\dag})}\_{H\_\text{I}} \end{aligned}$ 

Here, $a^\dag , a$ are the creation and annihilation operators on $\mathcal{H}$ , while $\sigma\_z, \sigma\_{\pm}$ are the Pauli Z operator and raising and lowering operators on $\mathcal{K}$ . $\Omega$ is called the Rabi frequency, and it measures the coupling strength between the optical field and the two-level system.

### 1.1 Diagonalization of the JCM  
Since $H\_0$ has only diagonal terms, we can separate it from the solution: let $|\psi\rangle = e^{-\mathrm{i}H\_0t} |\psi\_\text{I}\rangle$ , then $\mathrm{i} \frac{\mathrm{d}}{\mathrm{d}t}|\psi\_\text{I}\rangle = H\_\text{I}|\psi\_\text{I}\rangle$ . Therefore, we need only study $H\_\text{I}$ . This method is called the interaction picture (Interaction Picture).

We can expand $H\_\text{I}$ in the photon-number representation:

$\begin{aligned} H\_\text{I} &= \color{gray}{  \begin{matrix} |g,0\rangle \\\\ |e,0\rangle \\\\ |g,1\rangle \\\\ |e,1\rangle \\\\ |g,2\rangle \\\\ \vdots \end{matrix} } \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & \cdots \\\\ 0 & 0 & 1 & 0 & 0 & \cdots \\\\ 0 & 1 & 0 & 0 & 0 & \cdots \\\\ 0 & 0 & 0 & 0 & \sqrt{2} & \cdots \\\\ 0 & 0 & 0 & \sqrt{2} & 0 & \cdots \\\\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix}\Omega+ \begin{bmatrix} -1 & 0 & 0 & 0 & 0 & \cdots \\\\ 0 & 1 & 0 & 0 & 0 & \cdots \\\\ 0 & 0 & -1 & 0 & 0 & \cdots \\\\ 0 & 0 & 0 & 1 & 0 & \cdots \\\\ 0 & 0 & 0 & 0 & -1 & \cdots \\\\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix} \frac{\Delta}{2} \end{aligned} $ 

Here, $g,e$ represent the ground state and excited state of the two-level system, respectively, and $0,1,2,\cdots$ represents the excitation number of the optical field (i.e., the photon number).

It can be further written as:

$\begin{aligned} H\_\text{I} = \bigoplus\_{n=1}^\infty  \begin{bmatrix} \frac{\Delta}{2} & \Omega\sqrt{n} \\\\ \Omega\sqrt{n} & -\frac{\Delta}{2} \end{bmatrix} \end{aligned}$ 

Here, $n$ represents the total excitation number, namely the sum of the excitation number of the two-level system and that of the optical field (i.e., the photon number).

This matrix can clearly be diagonalized exactly, with eigenvalues $\pm \sqrt{\left(\frac{\Delta}{2}\right)^2 + n\Omega^2}$ . Let $\Delta\_n =  \sqrt{\Delta^2 + 4n\Omega^2}$; then the energy levels in the original picture (the non-interaction picture) are $E\_{\pm,n} =  \omega \left(n + \frac{1}{2}\right) \pm \frac{\Delta\_n}{2}$ .

The eigenstates of these energy levels are called dressed states:

$\begin{aligned} |-,n\rangle &= \cos \theta\_n |e,n-1\rangle - \sin \theta\_n |g,n\rangle \\\\ |+,n\rangle &= \sin \theta\_n |e,n-1\rangle + \cos \theta\_n |g,n\rangle  \end{aligned}$ 

where

$\begin{aligned} \cos \theta\_n &= \frac{2\sqrt{n}\Omega}{\sqrt{(\Delta\_n-\Delta)^2 + 4n\Omega^2}} \\\\ \sin \theta\_n &= \frac{\Delta\_n-\Delta}{\sqrt{(\Delta\_n-\Delta)^2 + 4n\Omega^2} }\end{aligned}$ 
  
  
### 1.2 Evolution of the Optical Field under the JCM  
Since we are ultimately concerned only with the quantum state of the optical field, we take the partial trace over the atomic part. Suppose the initial atomic state is $|e\rangle\langle e|$ . Then after time $\tau$ , the optical field evolves into

$\rho \rightarrow F(\tau) \rho := \text{tr}\_\text{a}[e^{-\mathrm{i}H \tau} (|e\rangle\langle e|\otimes \rho) e^{\mathrm{i}H\tau}]$ 

where $H$ is the JCM Hamiltonian and $\text{tr}\_\text{a}$ denotes the partial trace over the atomic system.

Let us first examine how $|n\rangle$ evolves under $F(\tau)$ , i.e., calculate $F(\tau)(|n\rangle\langle n|)$ :

$\begin{aligned} |e,n\rangle &= \cos \theta\_n | -,n+1\rangle + \sin \theta\_n |+,n+1\rangle \\\\  e^{-\mathrm{i}H\tau} |e,n\rangle &= \cos \theta\_n e^{-\mathrm{i} \frac{\Delta\_{n+1}}{2}\tau} |-,n+1\rangle +  \sin \theta\_n e^{\mathrm{i} \frac{\Delta\_{n+1}}{2}\tau}|+,n+1\rangle \\\\ &= \cos \theta\_n e^{-\mathrm{i} \frac{\Delta\_{n+1}}{2}\tau}  (\cos \theta\_n |e,n\rangle - \sin \theta\_n |g,n + 1\rangle)\\\\&\phantom{=}+  \sin \theta\_n e^{\mathrm{i} \frac{\Delta\_{n+1}}{2}\tau}(\sin \theta\_n |e,n\rangle + \cos \theta\_n |g,n+1\rangle)  \\\\ &= C\_{e,n} |e,n\rangle + C\_{g, n+1} | g, n+1\rangle \\\\  \text{tr}\_\text{atom}[e^{-\mathrm{i}H\tau}|e,n\rangle\langle e,n|e^{\mathrm{i}H\tau}] &=|C\_{e,n}|^2 |n\rangle\langle n| + |C\_{g,n+1}|^2 |n+1\rangle\langle n+1| \end{aligned}$ 

where

$\begin{aligned} C\_{e,n} &= \cos(\Delta\_{n+1} \tau /2) + \mathrm{i} \cos(2\theta\_n)\sin(\Delta\_{n+1} \tau/2)\\\\ C\_{g,n+1} &= \mathrm{i} \sin (2\theta\_n) \sin (\Delta\_{n+1} \tau/2) \end{aligned}$ 

Suppose the initial state of the optical field is a photon-number mixed state $\rho = \sum\_n p\_n |n\rangle\langle n|$ . Then

$\begin{aligned} F(\tau) \rho &= \sum\_n p\_n F(\tau)(|n\rangle\langle n|)\\\\ &= \sum\_n p\_n [|C\_{e,n}|^2 |n\rangle\langle n | + |C\_{g,n+1}|^2 |n+1\rangle\langle n+1|] \\\\ &= \sum\_n p\_n |C\_{e,n}|^2 |n\rangle\langle n | + \sum\_{n=1} p\_{n-1} |C\_{g,n}|^2 |n\rangle\langle n| \end{aligned}$ 

Thus, the new $p\_n^\prime = \langle n|F(\tau) \rho |n\rangle$ is

$\begin{aligned} \langle n|F(\tau) \rho |n\rangle &= |C\_{e,n}|^2 p\_n + |C\_{g,n}|^2 p\_{n-1} \\\\ &=: (1-C\_n) p\_n + C\_{n-1} p\_{n-1} \end{aligned}$ 

where $C\_n := |C\_{g,n+1}|^2 \Rightarrow 1-C\_n = |C\_{e,n}|^2$ .

We will use the expression for $\langle n|F(\tau) \rho |n\rangle$ later.

There is also $C\_{n-1} = |C\_{g,n}|^2=\sin^2 (2\theta\_n) \sin^2 \left(\frac{\Delta\_{n}}{2} \tau\right) = \frac{4n\Omega^2}{4n\Omega^2+\Delta\_n^2} \sin^2 \left(\frac{\Delta\_{n}}{2}  \tau\right)$ , and this result will also be useful later.


> Summary: This section obtained the analytical solution of the Jaynes\-Cummings model. Given a coupled system consisting of a two-level atom and an optical field, with initial state $\rho$ , we can determine its state $F(\tau) \rho$ at any later time. In particular, we wrote down the diagonal terms $\langle n|F(\tau) \rho |n\rangle$ of the optical-field density matrix, namely the evolved photon-number distribution.

## 2. Lindblad Master Equation  
For a closed system, the evolution of the quantum state $\rho$ follows the Heisenberg equation: $\frac{\mathrm{d}}{\mathrm{d}t} \rho = -\mathrm{i}[H,\rho]$ . It is in fact the statistical superposition of the Schrödinger equation $\frac{\mathrm{d}}{\mathrm{d}t}|\psi\rangle = -\mathrm{i}H|\psi\rangle$ . This is a unitary (Unitary) process.

For an open system, the evolution of the quantum state $\rho$ is no longer a unitary process. When the environment is sufficiently large that it has no memory, i.e., when the environment satisfies the Markovian approximation, the evolution of the quantum state is a trace-preserving (trace preserving) and completely positive (complete positive) quantum channel (quantum channel). It can be shown that the general form of $\frac{\mathrm{d}}{\mathrm{d}t} \rho$ is then:

$\begin{aligned} \frac{\mathrm{d}}{\mathrm{d}t} \rho = \mathcal{L}[\rho]= -\mathrm{i}[H,\rho] - \sum\_k \gamma\_k \left(\frac{1}{2} L\_k^\dag L\_k \rho - L\_k \rho L\_k^\dag + \frac{1}{2} \rho L\_k^\dag L\_k\right) \end{aligned}$ 


> Clearly, $\frac{\mathrm{d}}{\mathrm{d} t} \text{tr}[\rho]=0$ , so it is trace-preserving.

This is the Lindblad master equation, in which $\mathcal{L}$ is called the Lindbladian and may be regarded as the extension of the Hamiltonian to open systems.


> It is sometimes also called the Liouvillian, but Liouvillian is somewhat more general; for example, it does not require complete positivity.  
>   
> In the literature, Liouvillian refers to the superoperator $\mathcal{B}(\mathcal{B}(\mathcal{H}))$ , where $\mathcal{B}(\cdot)$ represents all linear operators on $\cdot$ . A superoperator is an “operator on operators.”  
>   
> In the literature, Liouvillian and Lindbladian are sometimes used interchangeably.

When an optical field is coupled to a thermal reservoir with mean photon number $\lambda$ , the Lindblad master equation it obeys is:

$\begin{aligned} \dot{\rho}=\mathcal{L}[\rho] = -\frac{\omega}{2Q}(\lambda +1)&(a^\dag a \rho - 2 a \rho a^\dag + \rho a^\dag a) \\\\ - \frac{\omega}{2Q}\lambda &(a a^\dag \rho - 2a^\dag \rho a+\rho a a^\dag) \end{aligned}$ 

In the optical band, blackbody radiation gives $\lambda \approx 0$ , so the above equation simplifies to:

$\begin{aligned} \dot{\rho}=\mathcal{L}[\rho] = -\frac{\omega}{2Q}&(a^\dag a \rho - 2 a \rho a^\dag + \rho a^\dag a) \end{aligned}$ 

Its diagonal terms are

$\dot{p}\_n=\langle n | \mathcal{L}[\rho] | n \rangle = -\frac{\omega}{Q}(np\_n - (n+1)p\_{n+1}) $ 

The physical meaning of this expression is quite clear: the probability of energy level $|n\rangle\langle n|$ relaxing to $|n - 1\rangle\langle n -1|$ is proportional to $np\_n$ .

## 3. Scully\-Lamb Laser Theory  
Using the JCM and Lindbladian above, we can treat a laser system in a fully quantum manner.


> There are many atoms in a laser, so why use the single-atom JCM rather than the multi-atom TCM (Tavis\-Cummings model)? This is because the TCM is used to describe collective atomic behavior: when the wavelength lies in the microwave range, since the wavelength and the length of the resonant cavity are comparable, all atoms experience the same electromagnetic field, leading to phenomena such as superradiance (Superradiance). However, in the optical band ($10^{14} \sim 10^{15} \text{Hz}$), the resonant-cavity length is much greater than the coherence length, causing individual atoms to interact independently with the optical field. In this case, the single-atom JCM is sufficient; we need only average the JCM solution over the individual atoms.

There are two main physical processes in a laser: one is the stimulated-emission process described by the JCM Hamiltonian, and the other is the relaxation process described by the Lindbladian. Combining these two processes gives the evolution equation for the optical field $\rho$ :

$\dot{\rho} = -\mathrm{i}\,\text{tr}\_\text{a}[H,\rho\_\text{af}] + \mathcal{L}[\rho]$ 

where $H$ is the JCM Hamiltonian, $\rho\_\text{af}$ is the joint quantum state of the atom and optical field, and $\text{tr}\_\text{a}$ denotes the partial trace over the atomic system.

Directly calculating this equation [1] can of course yield the result, but to simplify the calculation [2], we may first consider the relative time scales of these two processes.

### 3.1 Time-Scale Analysis  
1. \*\*Stimulated emission\*\*: Atoms in both the upper and lower energy levels can de-excite through spontaneous emission, with an average lifetime on the order of nanoseconds (or even picoseconds). That is, the coherent process described by the JCM lasts on the order of \*\*nanoseconds to picoseconds\*\*. In other words, in the evolution $\rho \rightarrow F(\tau) \rho := \text{tr}\_\text{a}[e^{-\mathrm{i}H \tau} (|e\rangle\langle e|\otimes \rho) e^{\mathrm{i}H\tau}]$ of the optical field, the mean value of $\tau$ is on the order of nanoseconds to picoseconds.
2. \*\*Relaxation\*\*: Photons reflect back and forth inside the cavity, with a certain probability of being lost at each reflection. Let the reflectivity be $99.9\%$ and the cavity length be 30 cm; then the characteristic relaxation time is $1\text{ns}  \cdot \frac{\log 37 \%}{\log 99.9 \%} \approx 10^3 \text{ns}$ , on the order of \*\*microseconds\*\*. In other words, in the evolution $\rho \rightarrow e^{t\_p \mathcal{L}} \rho$ of the optical field, the mean value of $t\_p$ is on the order of microseconds.

Clearly, the duration of the Lindbladian's action is much greater than that of the JCM Hamiltonian. Therefore, we can perform a \*\*coarse-grained\*\* analysis and discuss the two processes separately.

Let $\rho(t\_{i+1}) = e^{t\_p \mathcal{L}} F(\tau) \rho(t\_i)$ , where $\tau \ll t\_p = t\_{i+1} - (t\_i + \tau) \approx t\_{i+1} - t\_i$ . It means that during $(t\_i,t\_i +\tau)$ , the optical field evolves according to the JCM; during $(t\_i+\tau,t\_{i+1})$ , it evolves according to the Lindbladian.

### 3.2 Random Matrix Theory  
Note that both $t\_p$ and $\tau$ are random variables, so we must also average the expression $\rho(t\_{i+1}) = e^{t\_p \mathcal{L}} F(\tau) \rho(t\_i)$ .


> A rigorous treatment requires random matrix theory, but here we need not be overly concerned with rigor.

Let us first discuss the probability distributions obeyed by $t\_p$ and $\tau$ :

1. Since individual atoms interact independently with the pump light, the times at which atoms are pumped into the excited state are completely random. This causes the number of excitations per unit time to follow a Poisson distribution, and the time interval between two adjacent excitations to follow an exponential distribution, i.e., $p(t\_p) =R e^{-R t\_p}$ , where $R$ is the pumping rate.
2. Since the time at which spontaneous emission occurs is also completely random, $\tau$ likewise follows an exponential distribution, i.e., $p(\tau) = \gamma e^{-\gamma \tau}$ , where $\gamma^{-1}$ is the mean lifetime of the excited state.

We first average over $t\_p$ :

$\begin{aligned} {\rho}(t\_{i+1}) &= \left[\int \mathrm{d}t\_pe^{-t\_pR}e^{t\_p \mathcal{L}} \right]F(\tau) \bar{\rho}(t\_i) \\\\ &= \ \frac{R}{R-\mathcal{L}} F(\tau) {\rho}(t\_i) \end{aligned}$ 

Thus, the steady-state solution should satisfy:

$R[1-F(\tau)] {\rho} = \mathcal{L} \rho$ 

Considering the diagonal terms of the above equation and substituting $\langle n|F(\tau) \bar\rho | n\rangle$ and $\langle n | \mathcal{L} \bar\rho | n \rangle$ obtained in Sections 1 and 2, we have:

$R[C\_n p\_n - C\_{n-1} p\_{n-1}] = -\frac{\omega}{Q}(np\_n - (n+1)p\_{n+1}) $ 

Let $S\_n = \frac{\omega}{Q}np\_n - RC\_{n-1} p\_{n-1}$ . Then $S\_n =S\_{n+1}$ ; in order for $p\_n$ to converge, we require $S\_n=0$ , and hence:

$p\_n = \frac{RQ}{n\omega}C\_{n-1} p\_{n-1} =\frac{RQ}{\omega} \frac{4\Omega^2}{4n\Omega^2+\Delta\_n^2} \sin^2 \left(\frac{\Delta\_{n}}{2}  \tau\right)p\_{n-1} $ 

Now let us average over $\tau$

$\begin{aligned} {p}\_n &=\frac{RQ}{\omega} \frac{4\Omega^2}{4n\Omega^2+\Delta\_n^2}\left[ \gamma\int\mathrm{d}\tau e^{-\gamma \tau} \sin^2 \left(\frac{\Delta\_{n}}{2}  \tau\right) \right] \bar{p}\_{n-1} \\\\ &= \frac{A}{B +k} {p}\_{n-1} \end{aligned}$ 

where $A = \frac{RQ}{2\omega}$ , $B=\frac{\Delta^2 + \gamma^2}{4\Omega^2}$ .

Thus $\begin{aligned} {p}\_n = {p}\_0 \prod\_{k=1}^n\frac{A}{B+k} \end{aligned}$ .

In an actual laser, $\Delta$ and $\Omega$ are of comparable order of magnitude, both being MHz. As mentioned earlier, $\gamma^{-1}$ is on the order of nanoseconds to picoseconds, i.e., $\gamma$ is on the order of GHz to THz. Therefore, $B$ is a constant on the order of $10^6 \sim 10^{12}$ . The constant $A$ depends on the pump strength and the quality of the resonant cavity.


> We solve only for the steady-state solution of the diagonal terms of $\rho$ because the steady-state solutions of all off-diagonal terms are zero. Thus, after obtaining $p\_n$ , we can directly write the quantum state as $\rho = \sum\_n p\_n |n\rangle\langle n|$ .

### 3.3 Analysis of Results: Photon-Number Distribution  
When the pump is very weak, $A\ll B$ . In this case, ${p}\_n \approx {p}\_0 \left(\frac{A}{B}\right)^n$ , which is a thermal distribution with temperature $T=\omega \left[\log\left(\frac{2\omega B}{RQ}\right)\right]^{-1}$ .

When the pump is very strong, $A \gg B$ . In this case, ${p}\_n \approx {p}\_0 \frac{A^n}{n!}$ , which is a Poisson distribution. The quantum state is then:

$\rho = e^{-A}\sum\_k \frac{A^{k}}{k!} |k\rangle\langle k |$ 

This is a Poisson distribution with mean particle number $A$ .


> In the coherent-state representation, $\rho$ can be written as:  
>   
> $\rho = \int\_0^{2\pi} \frac{\mathrm{d}\theta}{2\pi} |\alpha e^{\mathrm{i}\theta}\rangle\langle\alpha e^{\mathrm{i}\theta}|,\quad A=|\alpha|^2$   
>   
> Clearly, it is actually a coherent state with random phase. A coherent state $|\alpha\rangle$ corresponds to a classical electromagnetic wave with highly definite amplitude and phase, whereas here its phase has been integrated from $0$ to $2\pi$ . This reflects our ignorance of the phase information, an ignorance that fundamentally originates from our ignorance of the microscopic state of the two-level system (the gain medium). One may say that this $\rho = \rho\_{\text{epistemic}}$ is an epistemic quantum state.  
>   
> From an ontological perspective, however, the quantum state of the system should collapse into an $\rho\_{\text{ontic}} = |\alpha\rangle$ with a definite phase; we simply have no way of knowing which phase it is. This is because, at the optical frequency $\sim 10^{15} \text{Hz}$ , humans cannot observe absolute phase. Relative phase, however, is observable, so we can still observe interference phenomena. A simple calculation also shows this: whether using the mixed state $\rho = \int\_0^{2\pi} \frac{\mathrm{d}\theta}{2\pi} |\alpha e^{\mathrm{i}\theta}\rangle\langle\alpha e^{\mathrm{i}\theta}|$ or the pure state $\rho = |\alpha\rangle\langle \alpha|$ to calculate the correlation function $\langle a^\dag(t)a(0)\rangle = \text{tr}[\rho a^\dag(t)a(0)]$ , the result is no different. This once prompted discussion about coherence: is coherence an illusion or a physical reality? [3] Supporters of the former view argue that the “phase-collapse” interpretation above has a “preferred basis” problem, but this problem may be considered resolved: coherent states are the longest-lived states in the open-system setting of a laser cavity.

When the pump magnitude is comparable to the threshold, there is an exact solution ${p}\_n = p\_0 \frac{B! A^n}{(n+B)!}$ . Let us now examine whether it is a super-Poissonian or sub-Poissonian distribution.

$\langle n \rangle = \sum\_n np\_n = A - B + Bp\_0$ 

$\langle n^2\rangle = \langle n \rangle^2 + A$ 

At this point, $g^{(2)}(0) = \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} = 1 + \frac{B(1-p\_0)}{[A-B(1-p\_0)]^2} > 1$ 

It can be seen that when the pump is not strong, the photon-number distribution is in fact super-Poissonian. As the pump becomes increasingly strong, $g^{(2)}(0) \rightarrow 1$ , approaching a Poisson distribution. Such refined predictions are beyond the reach of semiclassical theory.

### 3.4 Analysis of Results: Natural Linewidth  
In the Schrödinger picture, the quantum state $\rho$ evolves as $\mathrm{d}\rho = -\mathrm{i}\,\text{tr}\_\text{a}[H,\rho\_\text{af}]\mathrm{d}\tau+ \mathcal{L}[\rho]\mathrm{d}t\_p$ , while in the Heisenberg picture, the evolution of an operator is its dual channel:

$ \mathrm{d}{R} = \mathrm{i}\,\text{tr}\_\text{a}[H,R]\mathrm{d}\tau + \mathcal{L}^\*[R] \mathrm{d}t\_p$ 

where $\begin{aligned} \mathcal{L}^\*[R]= -\frac{\omega}{2Q}&(a^\dag a R- 2 a^\dag R a + R a^\dag a) \end{aligned}$ .

Setting $R = a$ yields:

$\begin{aligned} \mathrm{d}{a} &= -\mathrm{i} \omega a \mathrm{d}\tau - \frac{\omega}{2Q} a \mathrm{d}t\_p \end{aligned}$ 

From $\gamma \mathrm{d}\tau = R\mathrm{d}t\_p$ , we obtain

$\begin{aligned} \dot{a} &= \frac{\mathrm{d}a}{\mathrm{d}\tau} = -\mathrm{i} \omega a - \frac{\omega}{2Q} \frac{\gamma}{R}a\end{aligned}$ 

Solving gives $a(t ) =a(0) e^{-\mathrm{i}\omega t} e^{-\frac{\omega\gamma}{2RQ}t}, \quad a>0$ .

Its first-order correlation function is:

$\begin{aligned} g^{(1)}(t>0)&=\langle a^\dag(t) a(0)\rangle / \langle a^\dag(0) a(0)\rangle \\\\ &= \text{tr}[a(0) \rho a^\dag(t)] / \text{tr}[a(0) \rho a^\dag(0)] \\\\ &= e^{-\mathrm{i}\omega t} e^{-\frac{\omega\gamma}{2RQ}t} \end{aligned}$ 

Time-translation invariance requires $g^{(1)}(t) = g^{(1)}(-t)$ , so

$\begin{aligned} g^{(1)}(t)= e^{-\mathrm{i}\omega t} e^{-\frac{\omega\gamma}{2RQ}|t|} \end{aligned}$ 

Taking its Fourier transform yields the spectrum:

$\begin{aligned} F(\omega^\prime) = \frac{\frac{\omega\gamma}{2RQ}}{(\omega^\prime-\omega)^2 + \left(\frac{\omega\gamma}{2RQ}\right)^2} \end{aligned}$ 

This is a Lorentzian line shape, with full width at half maximum (FWHM) $\Delta \omega = \frac{\omega\gamma}{RQ} = \frac{2\gamma}{A}$ .


> Clearly, the natural linewidth depends on the mean lifetimes $\gamma^{-1}$ of the upper and lower energy levels. This is very intuitive, since the lifetimes of the upper and lower levels determine the coherence time of stimulated emission.  
> Moreover, the stronger the pump, the narrower the natural linewidth. This is also intuitive: the stronger the pump, the shorter the interval between two stimulated-emission processes, and hence the shorter the time over which relaxation acts.

## References  
1. Marlan O. Scully \& M. Suhail Zubairy, Quantum Optics
2. Pierre Meystre \& Murray Sargent, Elements of Quantum Optics
3. Bartlett, S. D., Rudolph, T. \& Spekkens, R. W. Dialogue Concerning Two Views on Quantum Coherence: Factist and Fictionist. Int. J. Quantum Inform. 04, 17–43 (2006\).
