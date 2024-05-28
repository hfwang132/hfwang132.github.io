---
title: "Orbital angular momentum of photons"
date: 2024-05-27T17:35:05+08:00
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

## Preface  
A paper published in PRA in 1992 [[1]](#ref_1) pointed out that photons also have orbital angular momentum (OAM). Compared to spin angular momentum (i.e., polarization, SAM) which can only take $\pm \hbar$, orbital angular momentum can take any integer multiple of $\hbar$. Such orbital angular momentum can be carried by helical wavefronts.

You might be surprised: did people only discover this in 1992? In fact, helical wavefronts had been studied before 1992; photons carrying angular momentum greater than $\hbar$ had already been predicted by atomic physics (though they originate from higher-order transition processes, which do not satisfy the selection rules and thus have very low probabilities, making them practically unobservable in experiments). It wasn't until 1992 that Allen et al. pointed out that light beams with helical wavefronts carry quantized orbital angular momentum.

From 1992 to 2001, research on OAM was mostly in the domain of macroscopic electromagnetic waves (coherent states of a large number of photons). In a paper in 2001 [[2]](#ref_2) by Nobel laureate Zeilinger's group, the orbital angular momentum and its entanglement of single photons were studied for the first time. Since then, OAM has also gained the interest of researchers in quantum information and quantum optics. One potential application of OAM in quantum information is quantum precision measurement, as its $e^{\mathrm{i}l\varphi}$ factor helps to increase the precision of angle measurements by a factor of $l$. Additionally, SAM and OAM can interact through a q-plate, which is beneficial for quantum information processing. OAM also has many other classical applications [[3]](#ref_3), which will not be elaborated here.

## 1. Hermite-Gaussian (HG) Beams  
Before introducing Laguerre-Gaussian beams that carry orbital angular momentum, it is best to introduce Hermite-Gaussian beams.

Why introduce Gaussian beams? Because the electromagnetic waves obtainable in experiments are not ideal plane waves but Gaussian beams output by lasers.

{{< figure src="image/gaussian.jpg" title="Waist width w0, Rayleigh length zR, and divergence angle theta of a Gaussian beam, image source Wikipedia" >}}
  
The electric field amplitude of a common Hermite-Gaussian beam is as follows:

$\begin{aligned} E_{m,n}(x,y,z) = & \,E_0 \color{blue}{ \frac{w_0}{w(z)}\exp\left[-\frac{x^2+y^2}{w(z)^2}\right] } \times \\\\ & \color{green}{\exp\left[-\mathrm{i}\frac{k(x^2+y^2)}{2 R(z)}\right]} \color{orange}{\exp\left[\mathrm{i}\psi(z)\right]} \color{gray}{\exp[-\mathrm{i}kz]} \times \\\\ & \color{red}{H_m\left[\sqrt{2}\frac{x}{w(z)}\right]H_n\left[\sqrt{2}\frac{y}{w(z)}\right]} \end{aligned} $ 

where:

$\color{blue}{w(z) = w_0 \sqrt{1+\left(\frac{z}{z_R}\right)^2}}$ represents the beam width at $z$, $z_R = \pi\frac{w_0^2}{\lambda}$ is the Rayleigh length, defined as the $z$ value at which the beam width diverges to $\sqrt{2}$ times the waist width.

$\color{green}{R(z) = \frac{z^2 + z_R^2}{z}}$ represents the curvature radius of the wavefront at $z$.

$\color{orange}{\psi(z)=\arctan\left(\frac{z}{z_R}\right)}$ represents the Gouy phase shift. There is an extra phase shift of $\pi$ from negative infinity to positive infinity.

$\color{red}{H_m(t)}$ is the $m$-th order Hermite polynomial. These are also the energy eigenfunctions of the quantum harmonic oscillator. When $m,n$ are both zero, it degenerates to the fundamental Gaussian beam. Most lasers output fundamental Gaussian beams.

As can be seen, remembering the Gaussian beam is not difficult, just remember three characteristics: $\color{blue}{\text{waist divergence}}$, $\color{green}{\text{curvature radius}}$, $\color{orange}{\text{Gouy phase shift}}$.

Another useful quantity is the divergence angle. From $\color{blue}{w(z) = w_0 \sqrt{1+\left(\frac{z}{z_R}\right)^2}}$, it can be seen that the tangent value of the divergence angle is $\tan \theta=\frac{w_0}{z_R}$, so $w_0 \tan \theta = \frac{\lambda}{\pi}$.

The shape of a Gaussian beam is completely determined by any two of the wavelength, waist radius, and divergence angle. The relationship between these three is given by $w_0 \tan \theta = \frac{\lambda}{\pi}$.


> $E_{m,n}(x,y,z)$ only represents the amplitude of the electric field and does not include polarization information.  
>   
> Adding polarization information is easy: if it is $x$-direction polarized, simply multiply $E_{m,n}(x,y,z)$ by the unit vector in the $x$ direction $\hat{x}$. If it is circularly polarized, multiply by $\hat{x} \pm \mathrm{i}\hat{y}$.  
>   
> Note that $E_{m,n}(x,y,z)$ is a complex number. For classical electromagnetic waves, the real part of this is the actual electric field amplitude. For quantum electromagnetic waves, we can assign an annihilation operator to this mode, which is a linear combination of plane wave annihilation operators, with coefficients obtainable by Fourier analysis.

{{< figure src="image/HG.jpg" title="HG modes, image source Wikipedia" >}}

  
## 2. Laguerre-Gaussian (LG) Beams  
In the solutions of the two-dimensional quantum harmonic oscillator, besides the linear vibrations represented by Hermite polynomials, there are rotational motions represented by Laguerre polynomials.

Below we give the form of the Laguerre-Gaussian beam:

$\begin{aligned} E_{l,p}(r,\varphi,z) = & \,E_0 \color{blue}{ \frac{w_0}{w(z)}\exp\left[-\frac{r^2}{w(z)^2}\right] } \times \\\\ & \color{green}{\exp\left[-\mathrm{i}\frac{kr^2}{2 R(z)}\right]} \color{orange}{\exp\left[\mathrm{i}\psi(z)\right]} \color{gray}{\exp[-\mathrm{i}kz]} \times \\\\ & \color{red}{\left(\sqrt{2}\frac{r}{w(z)}\right)^{|l|} L_p^{|l|} \left(2 \frac{r^2}{w(z)^2}\right) \exp(-\mathrm{i}l\varphi)} \end{aligned} $ 

where $\color{blue}{\text{waist divergence}}$ and $\color{green}{\text{curvature radius}}$ are the same as those of the Hermite-Gaussian beam. There are two differences:

First, the higher-order terms change from Hermite polynomials to Laguerre polynomials $\color{red}{L_p^{|l|} (t)}$. The additional factors $\color{red}{\left(\sqrt{2}\frac{r}{w(z)}\right)^{|l|}}$ and $\color{red}{\exp(-\mathrm{i}l\varphi)}$ represent a singularity at the origin and a helical wavefront (carrying orbital angular momentum $\hbar l$), respectively.

Second, the Gouy phase shift $\color{orange}{\psi(z) = (2p + |l|+ 1)\arctan \frac{z}{z_R}}$ becomes $(2p + |l|+ 1)$ times that of the HG mode.

{{< figure src="image/LG.jpg" title="LG modes, image source Wikipedia" >}}

  
Just as rotation can be decomposed into a linear combination of vibrations, LG modes can also be represented as coherent combinations of HG modes. This is similar to circular polarization being decomposable into a combination of two linear polarizations.

## 3. Manipulating Spin Angular Momentum and Orbital Angular Momentum with a Q-Plate  
A q-plate, proposed in 2006 [[4]](#ref\_4), is essentially a half-wave plate with its optical axis varying with position, and the angle $\alpha$ of the optical axis satisfies $\alpha(r,\varphi) = q \varphi + \alpha_0$. Its Jones matrix is $\begin{bmatrix} \cos 2\alpha & \sin 2\alpha \\\\ \sin 2\alpha & -\cos 2\alpha \end{bmatrix}$.

{{< figure src="image/qplate.jpg" title="Optical axis pattern of a q-plate, image source [4]" >}}
 
  
Consider a q-plate acting on a left-handed polarized fundamental Gaussian beam, resulting in:

$\begin{bmatrix} \cos 2\alpha & \sin 2\alpha \\\\ \sin 2\alpha & -\cos 2\alpha \end{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{2}} \\\\ \frac{\mathrm{i}}{\sqrt{2}} \end{bmatrix} =  e^{\mathrm{i}2q\varphi} \begin{bmatrix} \frac{1}{\sqrt{2}} \\\\ -\frac{\mathrm{i}}{\sqrt{2}} \end{bmatrix}$ 

As can be seen, after passing through the q-plate, the left-handed polarized light becomes right-handed polarized light carrying $2q\hbar$ orbital angular momentum.

Q-plates are currently the most commonly used method for preparing OAM states in experiments. Of course, spatial light modulators (SLM) can also be used.

One reason why OAM attracts the interest of quantum information researchers is that its Hilbert space dimension, like that of a harmonic oscillator, is infinite, unlike polarization (SAM), which only has two states. The interaction between SAM and OAM leads to a straightforward idea: using SAM and OAM to make a CNOT gate, where SAM is the control bit and OAM is the target bit. There are many similar experiments, which are not listed here.

## References  
1. Allen, L.; Beijersbergen, M. W.; Spreeuw, R. J. C.; Woerdman, J. P. Orbital Angular Momentum of Light and the Transformation of Laguerre-Gaussian Laser Modes. Phys. Rev. A 1992, 45 (11), 8185–8189. https://doi.org/10.1103/PhysRevA.45.8185.
2. A. Mair, A. Vaziri, G. Weihs, and A. Zeilinger, “Entanglement of the orbital angular momentum states of photons,” Nature 412(6844), 313–316 (2001).
3. Padgett, M. J. Orbital Angular Momentum 25 Years on [Invited]. Opt. Express 2017, 25 (10), 11265. https://doi.org/10.1364/OE.25.011265.
4. Marrucci, L.; Manzo, C.; Paparo, D. Optical Spin-to-Orbital Angular Momentum Conversion in Inhomogeneous Anisotropic Media. Phys. Rev. Lett. 2006, 96 (16), 163905. https://doi.org/10.1103/PhysRevLett.96.163905.

