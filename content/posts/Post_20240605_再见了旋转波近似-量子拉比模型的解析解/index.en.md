---
title: "Goodbye, Rotating-Wave Approximation: The Analytical Solution of the Quantum Rabi Model"
date: 2024-06-05T20:52:29+08:00
originalURL: "https://zhuanlan.zhihu.com/p/701838204"
aliases:
  - "/en/rabi/"
  - "/en/Post_20240727_再见了旋转波近似-量子拉比模型的解析解/"
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

## 1. Introduction  
In the early days of quantum mechanics, Rabi proposed the Rabi model to treat the interaction between an electromagnetic field and an atom. Since this model quantized only the atom, but not the electromagnetic wave, although it could explain many phenomena (such as Rabi oscillations), it could not explain phenomena involving the quantization of the electromagnetic field, such as spontaneous emission.

To explain spontaneous emission and other phenomena involving the quantization of the electromagnetic field, Jaynes and Cummings proposed the Quantum Rabi Model (**QRM**) in 1962. This model also quantizes the electromagnetic field, so that the vacuum fluctuations of the electromagnetic field cannot be neglected. Thus, spontaneous emission is simply “stimulated emission” “excited” by the vacuum fluctuations of the electromagnetic field.

However, for quite a long time after the QRM was proposed, people believed that it had no analytical solution, and that an analytical solution existed only after applying the rotating-wave approximation (RWA). The model after applying the rotating-wave approximation is called the Jaynes-Cummings model (**JCM**).

The JCM successfully explains phenomena such as spontaneous emission and vacuum Rabi oscillations, but because it uses the rotating-wave approximation, it still cannot explain phenomena such as the Lamb shift. Moreover, strong coupling can now be realized in Circuit QED systems, and when the coupling is very strong, the rotating-wave approximation fails; in this case, the JCM deviates substantially from experimental results. Clearly, the QRM is still needed in some situations.

Surprisingly, the analytical solution of the QRM was not discovered until 2011 [1]. Since then, people have also become interested in analytical solutions of various generalized quantum Rabi models, such as extensions to multiple atoms (the Dicke model) and multiple field modes.

This article will derive the analytical solution of the QRM, with the following structure:

Section 2: Introduces the Hamiltonians of the QRM and JCM

Section 3: Briefly derives the analytical solution of the JCM

Section 4: Derives the analytical solution of the QRM

Section 5: Introduces the conserved quantities and symmetries of the JCM and QRM

## 2. Hamiltonians of the QRM and JCM  
The Quantum Rabi Model (QRM) describes the interaction between a single-mode optical field and a two-level system.

Let the Hilbert space of the single-mode optical field be $\mathcal{H} \cong L^{2}(\mathbb{R})$, and the Hilbert space of the two-level system be $\mathcal{K} \cong \mathbb{C}^2$. Then the QRM Hamiltonian $H\in \mathcal{L}(\mathcal{H}\otimes \mathcal{K})$ is as follows:

$\begin{aligned} H&= \underbrace{\omega \left(a^\dag a+\frac{1}{2}\right)}\_{\text{field}}+ \underbrace{ \frac{\Delta}{2} \sigma\_z}\_{\text{atom}} +  \underbrace{g\sigma\_x(a+a^\dag)}\_{\text{atom-field coupling}} \\\\&= \underbrace{\omega \left(a^\dag a+\frac{1}{2}\right)}\_{\text{field}}+ \underbrace{ \frac{\Delta}{2} \sigma\_z}\_{\text{atom}} +  \underbrace{g(\sigma\_++\sigma\_-)(a+a^\dag)}\_{\text{atom-field coupling}} \end{aligned}$ 

Here, $a^\dag , a$ are the creation and annihilation operators on $\mathcal{H} $, and $\sigma\_z, \sigma\_{\pm}$ are the Pauli Z operator and raising and lowering operators on $\mathcal{K}$. $g$ is called the Rabi frequency, and it measures the coupling strength between the optical field and the two-level system.

If we discard the terms $\sigma\_- a$ and $\sigma\_+ a^\dag$, which have large energy differences, we obtain the Hamiltonian of the Jaynes-Cummings model (JCM):

$\begin{aligned} H&= \underbrace{\omega \left(a^\dag a+\frac{1}{2}\right)}\_{\text{field}}+ \underbrace{ \frac{\Delta}{2} \sigma\_z}\_{\text{atom}} +  \underbrace{g(\sigma\_+ a + \sigma\_- a^{\dag})}\_{\text{atom-field coupling}}\end{aligned}$ 

This is the rotating-wave approximation. The discarded terms are called the counter-rotating terms, while the retained terms are called the co-rotating terms.


> The rotating-wave approximation is justified because the energy difference between the two levels involved in the counter-rotating terms is $\omega + \Delta$, much larger than the energy difference $|\omega - \Delta|$ for the co-rotating terms. The exponential factor involved in the former is $e^{\pm\mathrm{i} (\omega + \Delta) t}$, while that in the latter is $e^{\pm\mathrm{i}(\omega-\Delta)}t$. Since $e^{\pm\mathrm{i} (\omega + \Delta) t}$ varies too rapidly, it can be regarded as averaging to zero and thus eliminated.  
>   
> In addition, this can also be seen from perturbative calculations: the terms obtained after perturbative calculation are proportional to the reciprocal of the energy difference, namely $\frac{1}{\omega +\Delta}$ for the former and $\frac{1}{|\omega - \Delta|}$ for the latter. Since $\frac{1}{\omega + \Delta}$ is much smaller than $\frac{1}{|\omega - \Delta|}$, the former can be neglected.

  


## 2. Analytical Solution of the JCM  
We can expand $H$ in the photon-number basis:

$\begin{aligned} H &= \color{gray}{ \begin{matrix} |g,0\rangle \\\\ |e,0\rangle \\\\ |g,1\rangle \\\\ |e,1\rangle \\\\ |g,2\rangle \\\\ \vdots \end{matrix} } \begin{bmatrix} 1 & 0 & 0 & 0 & 0 & \cdots \\\\ 0 & 1 & 0 & 0 & 0 & \cdots \\\\ 0 & 0 & 3 & 0 & 0 & \cdots \\\\ 0 & 0 & 0 & 3& 0 & \cdots \\\\ 0 & 0 & 0 & 0 & 5& \cdots \\\\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix} \frac{\omega}{2}+\begin{bmatrix} -1 & 0 & 0 & 0 & 0 & \cdots \\\\ 0 & 1 & 0 & 0 & 0 & \cdots \\\\ 0 & 0 & -1 & 0 & 0 & \cdots \\\\ 0 & 0 & 0 & 1 & 0 & \cdots \\\\ 0 & 0 & 0 & 0 & -1 & \cdots \\\\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix} \frac{\Delta}{2} +\begin{bmatrix} 0 & 0 & 0 & 0 & 0 & \cdots \\\\ 0 & 0 & 1 & 0 & 0 & \cdots \\\\ 0 & 1 & 0 & 0 & 0 & \cdots \\\\ 0 & 0 & 0 & 0 & \sqrt{2} & \cdots \\\\ 0 & 0 & 0 & \sqrt{2} & 0 & \cdots \\\\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix} g \end{aligned} $ 

Here, $g,e$ respectively denote the ground state and excited state of the two-level system, and $0,1,2,\cdots$ denotes the excitation number of the optical field (i.e., the photon number).

It can be further written as:

$\begin{aligned} H = \bigoplus\_{n=1}^\infty  \begin{bmatrix} n\omega+\frac{\Delta}{2} & g\sqrt{n} \\\\ g\sqrt{n} & (n+1)\omega -\frac{\Delta}{2} \end{bmatrix} \end{aligned}$ 

Here, $n$ denotes the total excitation number, namely the sum of the excitation number of the two-level system and the excitation number of the optical field (i.e., the photon number).

This matrix can obviously be diagonalized exactly, with eigenvalues $\left(n+ \frac{1}{2}\right)\omega \pm \sqrt{\left(\frac{\omega - \Delta}{2}\right)^2 + ng^2}$. Let $\Delta\_n =  \sqrt{\left(\frac{\omega - \Delta}{2}\right)^2 + ng^2}$; then the energy levels are $E\_{\pm,n} =   \left(n + \frac{1}{2}\right)\omega \pm \frac{\Delta\_n}{2}$.

The eigenstates at these energy levels are called dressed states:

$\begin{aligned} |-,n\rangle &= \cos \theta\_n |e,n-1\rangle - \sin \theta\_n |g,n\rangle \\\\ |+,n\rangle &= \sin \theta\_n |e,n-1\rangle + \cos \theta\_n |g,n\rangle  \end{aligned}$ 

where

$\begin{aligned} \cos \theta\_n &= \frac{2\sqrt{n}g}{\sqrt{(\Delta\_n-\Delta\_0)^2 + 4ng^2}} \\\\ \sin \theta\_n &= \frac{\Delta\_n-\Delta\_0}{\sqrt{(\Delta\_n-\Delta\_0)^2 + 4ng^2}} \end{aligned}$ 

and $\Delta \_0 := \Delta - \omega$.

  
## 4. Analytical Solution of the QRM  
Next, we derive the analytical solution of the QRM following the method of a 2012 paper\[#ref\\\\_2](#ref\\\\_2\). Compared with the earliest method in the 2011 paper\[#ref\\\\_1](#ref\\\\_1\), it is more suitable for physicists rather than mathematicians.

Expanding the QRM Hamiltonian in the basis $\{|+\rangle, |-\rangle\} =\left\{\frac{|e\rangle + |g\rangle}{\sqrt{2}} ,\frac{|e\rangle - |g\rangle}{\sqrt{2}}\right\}$ gives:

$H =  \begin{bmatrix} \omega a^\dag a + g(a+a^\dag) & \Delta/2 \\\\ \Delta/2 & \omega a^\dag a + g(a-a^\dag) \end{bmatrix}$ 


> It can be verified that $H = [\omega a^\dag a + g(a+a^\dag)] |+\rangle\langle+| + [\omega a^\dag a - g(a+a^\dag)] |-\rangle\langle-|  + \frac{\Delta}{2}(|+\rangle\langle-| + |-\rangle\langle+|)$

Perform the Bogoliubov transformation $A = a +g/\omega,\,B=a-g/\omega$, and define the Extended Fock states:

$|0\rangle\_A=e^{-\frac{g}{\omega}(a^\dag - a)} |0\rangle = |\frac{-\omega}{g}\rangle$ 

$|n\rangle\_A = \frac{A^{\dag n}}{\sqrt{n!}} |0\rangle\_A$ 

Note that $|0\rangle\_A$ is a coherent state with parameter $-\frac{\omega}{g}$.

It can be verified that $[A,A^\dag]=1$. Therefore, the relations that hold for ordinary Fock states also hold for Extended Fock states:

$A|n\rangle\_A = \sqrt{n} |n-1\rangle\_A$ 

$A^\dag |n\rangle\_A = \sqrt{n+1} |n + 1\rangle\_A$ 

At this point, we have

$H =  \begin{bmatrix} \omega A^\dag A - g^2 /\omega& \Delta/2 \\\\ \Delta/2 & \omega A^\dag A - 2g(A+A^\dag) + 3g^2/\omega \end{bmatrix}$ 

Let the eigenstate be:

$|\psi\rangle=\begin{bmatrix} \sum \sqrt{n!} e\_n |n\rangle\_A \\\\ \sum \sqrt{n!} f\_n |n\rangle\_A \end{bmatrix}$ 

Substituting into $H|\psi\rangle = E|\psi\rangle$ gives:

$\begin{cases} e\_n = -\frac{\Delta/2}{ n\omega -g^2/\omega - E} f\_n \\\\ nf\_n = \Omega(n-1) f\_{n-1} - f\_{n-2} \end{cases}$ 

where $\Omega(n) = \frac{2g}{\omega}+\frac{1}{2g}\left[ n\omega - g^2/\omega -E - \frac{(\Delta/2)^2}{n\omega  - g^2/\omega - E}\right]$ 

Similarly, the Hamiltonian can also be written as:

$H =  \begin{bmatrix} \omega B^\dag B -2g(B + B^\dag) + 3g^2 & \Delta/2 \\\\ \Delta/2 & \omega  B^\dag B - g^2/\omega \end{bmatrix}$ 

Let the eigenstate be

$|\psi^\prime\rangle=\begin{bmatrix} \sum \sqrt{n!} (-1)^nf\_n^\prime |n\rangle\_B \\\\ \sum \sqrt{n!} (-1)^ne\_n^\prime |n\rangle\_B \end{bmatrix}$ 

Substituting into $H|\psi\rangle = E|\psi\rangle$ gives:

$\begin{cases} e\_n^\prime = -\frac{\Delta/2}{n\omega - g^2/\omega -E} f^\prime\_n \\\\ nf^\prime\_n  = \Omega(n-1)f^\prime\_{n-1} - f\_{n-2} \end{cases}$ 

It can be seen that $f\_n$ and $f\_n^\prime$, as well as $e\_n$ and $e\_n^\prime$, all satisfy the same recurrence relation. Let $f\_0 = f\_0^\prime = 1$; then $f\_n = f\_n^\prime$, $e\_n = e\_n^\prime$.

Since the two eigenstates $|\psi \rangle, |\psi^\prime\rangle$ must be proportional, $|\psi^\prime\rangle = \kappa |\psi\rangle$, where $\kappa \in \mathbb{C}$, we have:

$\begin{cases} \sum \sqrt{n!} (-1)^nf\_n |n\rangle\_B = \kappa \sum \sqrt{n!} e\_n |n\rangle\_A \\\\ \sum \sqrt{n!} (-1)^ne\_n |n\rangle\_B = \kappa\sum \sqrt{n!} f\_n |n\rangle\_A \end{cases}$ 

Multiplying both sides on the left by the vacuum state $\langle0|$, since

$\begin{aligned} \sqrt{n!}\langle 0 | n\rangle\_A &= \langle 0 |A^{\dag n}|0\rangle\_A \\\\&= \langle 0|(a+\lambda)^\dag | 0 \rangle\_A \\\\&= \lambda^n\langle 0|0\rangle\_A \\\\&= \lambda^n e^{-\lambda^2/2} \end{aligned}$ 

$\sqrt{n!} \langle 0|n\rangle\_B = (-\lambda)^n e^{-\lambda^2/2}$ 

where $\lambda = g/\omega$.

Thus:

$\begin{cases} \sum \lambda^n e^{-\lambda^2/2} f\_n = \kappa \sum \lambda^n e^{-\lambda^2/2} e\_n \\\\ \sum\lambda^n e^{-\lambda^2/2}e\_n  = \kappa\sum \lambda^n e^{-\lambda^2/2} f\_n  \end{cases}$ 

$\Rightarrow \left(\sum \lambda^n e^{-\lambda^2/2} f\_n\right)^2 = \left(\sum\lambda^n e^{-\lambda^2/2} e\_n \right)^2 $ 

$\Rightarrow \sum \lambda^n e^{-\lambda^2/2} (f\_n \pm e\_n )= 0$ 

$\begin{aligned} \Rightarrow \sum \lambda^n e^{-\lambda^2/2} f\_n \left(1\pm \frac{\Delta/2}{n\omega - g\lambda -E}\right) = 0 \end{aligned}$ 

Let $G\_{\pm}(x) = \sum f\_n \lambda^n \left(1\mp \frac{\Delta}{2\omega(x+\lambda^2-n)}\right)$, which is a transcendental function.

It can be seen that the zeros of $G\_{\pm}(x) $ are the eigenenergy levels (in units of $ \omega$).

  
The eigenstates are:

$\begin{aligned} &\phantom{=}\sum\_n\left[ \sqrt{n!} f\_n |n\rangle\_B \otimes \frac{|e\rangle + |g\rangle}{\sqrt{2}} + \sqrt{n!} e\_n |n\rangle\_B \otimes \frac{|e\rangle - |g\rangle}{\sqrt{2}}\right]  \\\\&=\sum\_n \left[ \sqrt{n!/2} (f\_n - e\_n)\right] |n\rangle\_B \otimes |g\rangle + \sum\_n \left[ \sqrt{n!/2} (f\_n + e\_n)\right] |n\rangle\_B \otimes |e\rangle \\\\&=\sum\_n \left[ \sqrt{\frac{n!}{2}} f\_n \left(1 - \frac{\Delta/2}{n\omega - g\lambda -E}\right)\right] |n\rangle\_B \otimes |g\rangle + \sum\_n \left[ \sqrt{\frac{n!}{2}} f\_n \left(1 + \frac{\Delta/2}{n\omega - g\lambda - E}\right) \right] |n\rangle\_B \otimes |e\rangle \end{aligned}$ 

At this point, we have obtained the analytical solution for the energy levels and eigenstates of the QRM Hamiltonian.
  
As can be seen from the figure, as the coupling coefficient increases, the energy gap between the ground state and the first excited state decreases. This is the Lamb shift. However, the Lamb shift we generally refer to involves the interaction of an atom with a vacuum optical field containing multiple modes, rather than the single-mode optical field discussed here.

In addition, it can be seen that as the coupling coefficient increases, energy levels that would originally cross in the JCM do not cross in the QRM; instead, they first approach and then move apart. This is the so-called avoided crossing.

## 5. Conserved Quantities and Symmetries  
The JCM has the conserved quantity $N = a^\dag a+\sigma\_+\sigma\_- = a^\dag a + (\mathbb{I} + \sigma\_z)/2$, whose eigenvalues are $n=0,1,2,\cdots$, $N|\pm,n\rangle = \left(n + \frac{1\pm 1}{2}\right)|\pm,n\rangle$. The physical meaning of this conserved quantity is the total number of excitations.

The conserved quantity $N$ generates a continuous $U(1)$ symmetry. This is because $[N,H] = 0 \Rightarrow [e^{-\mathrm{i\theta}N},H]=0$. That is, after performing the following transformation, the Hamiltonian remains unchanged:

$a \rightarrow e^{-\mathrm{i}\theta N} a e^{\mathrm{i}\theta N} = a e^{-\mathrm{i}\theta}$ 

$a^\dag   \rightarrow e^{-\mathrm{i}\theta N} a^\dag e^{\mathrm{i}\theta N} = a^\dag e^{\mathrm{i}\theta}$ 

$\sigma\_{\pm} \rightarrow e^{-\mathrm{i}\theta N} \sigma\_{\pm} e^{\mathrm{i}\theta N} = \sigma\_\pm e^{\pm\mathrm{i}\theta}$ 

The conserved quantity of the QRM is $\Pi = e^{-\mathrm{i}\pi N} = -\sigma\_+\sigma\_- \otimes e^{\mathrm{i}\pi a^\dag a}$, whose eigenvalues are $\pm 1$, $\Pi |\pm,n\rangle = \mp (-1)^n |\pm,n\rangle$.

Although the QRM loses the $U(1)$ symmetry, it still has a discrete $Z\_2$ symmetry, because $[\Pi,H]=0$ ensures that the Hamiltonian remains unchanged after performing the following transformation:

$a \rightarrow \Pi a \Pi^\dag = -a$ 

$a^\dag \rightarrow \Pi a^\dag \Pi^\dag = -a^\dag$ 

$\sigma\_\pm \rightarrow \Pi \sigma\_\pm \Pi^\dag = -\sigma\_\pm$ 

The $Z\_2$ symmetry can be regarded as the breaking of the $U(1)$ symmetry from $\theta \in [0,2\pi)$ to $\theta \in \{0,\pi\}$. This can also be seen intuitively from the Hamiltonian: the JCM has only co-rotating terms and therefore has a continuous $U(1)$ symmetry, whereas the QRM has both co-rotating and counter-rotating terms. These two terms can meet only at $\theta \in \{0,\pi\}$, and therefore there is only a discrete $Z\_2$ symmetry.

## References  
1. Braak, D. Integrability of the Rabi Model. Phys. Rev. Lett. 2011, 107 (10), 100401. [https://doi.org/10.1103/PhysRevLett.107.100401](https://doi.org/10.1103/PhysRevLett.107.100401\)
2. Chen, Q.-H.; Wang, C.; He, S.; Liu, T.; Wang, K.-L. Exact Solvability of the Quantum Rabi Model Using Bogoliubov Operators. Phys. Rev. A 2012, 86 (2), 023822. [https://doi.org/10.1103/PhysRevA.86.023822](https://doi.org/10.1103/PhysRevA.86.023822)
