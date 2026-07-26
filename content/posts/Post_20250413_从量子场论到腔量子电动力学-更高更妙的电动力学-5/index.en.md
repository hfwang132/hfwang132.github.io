---
title: "From Quantum Field Theory to Cavity Quantum Electrodynamics [Higher and More Elegant Electrodynamics · 5]"
date: 2025-04-13T01:52:37+08:00
originalURL: "https://zhuanlan.zhihu.com/p/1894566826417034044"
aliases:
  - "/en/gm_5/"
  - "/en/Post_20250406_从量子场论到腔量子电动力学-更高更妙的电动力学-5/"
draft: false
categories: ["Mathematical Methods in Physics"]
tags: ["quantum field theory", "cavity quantum electrodynamics", "electrodynamics", "Jaynes-Cummings"]
---

In this article, we start from the highly complex QED Lagrangian:

$\begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial\_\mu -m)\psi - eA\_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F\_{\mu\nu} F^{\mu\nu} \end{aligned} $

This Lagrangian is highly complex: it not only takes into account the electron's antiparticle—the positron—but the coupling term $- eA\_\mu \bar{\psi} \gamma^\mu \psi$ is also a cubic term, capable of describing multiple processes such as electron-positron pair creation/annihilation. It has no analytical solution and can only be solved using perturbation theory in quantum field theory.

But after a series of simplifications and approximations (the low-energy approximation, the Born-Oppenheimer approximation, the long-wavelength/dipole approximation, the two-level approximation, and the rotating-wave approximation), we unexpectedly arrive at a model with an analytical solution:

$H =  \frac{\omega\_{ab}}{2} \sigma\_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger) $

This is the classic Hamiltonian of cavity quantum electrodynamics: the Jaynes-Cummings Hamiltonian. How is this achieved? Let us break it down below.

---

## I. Hamiltonian Formulation of the Electromagnetic Field  
### 1.1 Hamiltonian of the Electromagnetic Field  

Let us first try applying the Legendre transformation directly:

$\mathcal{H} = \Pi^i  \dot{A}\_i - \mathcal{L}$

where $\Pi^i = \frac{\partial \mathcal{L}}{\partial \dot{ A}\_i}$ is the canonical momentum corresponding to $\mathbf{A}$.

We hope to obtain Maxwell's equations from the eight Hamilton equations:

$\boxed{ \dot{A}\_i = \frac{\delta \mathcal{H}}{\delta \Pi^i},\quad \dot{\Pi}^i = \frac{\delta \mathcal{H}}{\delta A\_i} }$

where the symbol $\delta$ denotes a variation.

But things are not so simple. Notice that the canonical momentum $\Pi^0 = \frac{\partial \mathcal{L}}{\partial \dot{\phi}} = 0$ is identically zero! This indicates that it is a constraint.

Thus,

$\mathcal{H} = \mathbf{\Pi} \cdot \dot{\mathbf{A}} - \mathcal{L}$

where $\mathbf{\Pi}=\frac{\partial \mathcal{L}}{\partial \dot{\mathbf{A}}} = \dot{\mathbf{A}} + \nabla \phi = -\mathbf{E}$ is the canonical momentum corresponding to $\mathbf{A}$.

Therefore,

$\begin{aligned} \mathcal{H} &= (\dot{\mathbf{A}} + \nabla \phi) \cdot \dot{\mathbf{A}} - \left[\frac{1}{2}(\dot{\mathbf{A}}+\nabla \phi)^2 -\frac{1}{2} (\nabla \times \mathbf{A})^2 - \rho \phi + \mathbf{A}\cdot \mathbf{J} \right]  \\\\ &= \frac{1}{2}\mathbf{\Pi}^2 - \mathbf{\Pi} \cdot \nabla \phi + \frac{1}{2} (\nabla \times \mathbf{A})^2 + \rho \phi - \mathbf{A}\cdot \mathbf{J}  \end{aligned}$

Using integration by parts during variation, $- \mathbf{\Pi} \cdot \nabla \phi $ can be transformed into $+\phi \nabla \cdot \mathbf{\Pi}$ . Thus:

$\boxed{ \begin{aligned}  \mathcal{H}=\frac{1}{2}\mathbf{\Pi}^2   + \frac{1}{2} (\nabla \times \mathbf{A})^2 - \mathbf{A}\cdot \mathbf{J}+ \phi(\rho +\nabla\cdot \mathbf{\Pi})    \end{aligned} }$

### 1.2 Canonical Equations of the Electromagnetic Field  

We now consider the Hamilton equation $\dot{\Pi}^0 = -\frac{\delta \mathcal{H}}{\delta A\_0} $ . Since $\Pi^0$ is always zero, $\dot{\Pi}^0$ must also always be zero. Hence, according to the Hamilton equation:

$\dot{\Pi}\_0 = -\frac{\delta \mathcal{H}}{\delta A\_0} = -\frac{\delta \mathcal{H}}{\delta \phi} = \rho + \nabla \cdot \mathbf{\Pi} = 0\Rightarrow  \boxed{\nabla\cdot \mathbf{E} = \rho}$

This is precisely Gauss's law. In the Hamiltonian formulation, it appears as a constraint. And $\phi$ is the corresponding Lagrange multiplier.

This shows that in the Hamiltonian formulation, $\phi$ is not an independent dynamical variable. We may choose $\phi =0$ ; this is called the Weyl gauge.

> The Weyl gauge is an incomplete gauge, because the remaining $A\_1,A\_2,A\_3$ still has gauge freedom.

Of course, we may also choose other gauges. For example, in the Coulomb gauge $\nabla \cdot \mathbf{A} = 0$ , $\phi$ then depends on $\mathbf{A}$ (according to gauge transformations).

Substituting the constraint $ \rho + \nabla \cdot \mathbf{\Pi} = 0$ into $\mathcal{H}$ gives:

$\boxed{ \begin{aligned} \mathcal{H} &= \frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 - \mathbf{A}\cdot \mathbf{J}\\\\ &= \frac{1}{2}\mathbf{E}^2  + \frac{1}{2} \mathbf{B}^2  - \mathbf{A}\cdot \mathbf{J}   \end{aligned} }$

> Note that the Hamiltonian contains no potential-energy term $\rho \phi$ . This is related to the Hamiltonian not being gauge invariant; see the end of Section II.  
>   
> Let us see why the Hamiltonian does not possess gauge invariance:  
>   
> In the Hamiltonian formulation, the equation of motion for the field $\varphi$ is $\partial\_t \varphi = \delta \mathcal{H}/\delta \pi\_\varphi$ , where the field $\pi\_\varphi$ is the canonical momentum corresponding to the field $\varphi$ .  
>   
> Notice that the derivative on the left-hand side of the equation of motion is $\partial\_t$ , rather than the gauge-invariant covariant derivative $D\_t = \partial\_t + \mathrm{i}eA\_t = \partial\_t -\mathrm{i}e\phi$ . Accordingly, the right-hand side of the equation is also not gauge invariant.  
>   
> This is one reason why the Hamiltonian formulation is not commonly used in high-energy physics.

Finally, let us consider the remaining Hamilton equations:

$\dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}},\quad \dot{\mathbf{\Pi}} = \frac{\delta \mathcal{H}}{\delta \mathbf{A}}$

The former $\dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}} = \mathbf{\Pi} - \nabla\phi \Rightarrow \mathbf{E} = -\frac{\partial A}{\partial t} - \nabla \phi$ is the defining equation for the electric field, while the latter is Ampère's law:

$\begin{aligned} \dot{\mathbf{\Pi}} &= -\frac{\delta \mathcal{H}}{\delta \mathbf{A}} \\\\ &= -\frac{\delta }{\delta \mathbf{A}} \int\left[\frac{1}{2}(\nabla \times \mathbf{A})^2 - \mathbf{J} \cdot \mathbf{A}\right] \mathrm{d}^3 x  \\\\&= \int[-\nabla\times(\nabla\times \mathbf{A}) + \mathbf{J}]\mathrm{d}^3x \end{aligned}$

That is,

$\boxed{ \begin{aligned} &\dot{\mathbf{E}}=\nabla\times\mathbf{B} -\mathbf{J} \\\\ &\Rightarrow   \nabla\times \mathbf{B} = \mathbf{J} + \dot{\mathbf{E}} \end{aligned} }$

We now have Ampère's law and Gauss's law. But where are the other two equations? In fact, similarly to $\mathrm{d}F=\mathrm{d}\mathrm{d}A=0$ in the Lagrangian formulation, the other two source-free equations are also part of the definitions in the Hamiltonian formulation. $\mathbf{B}:=\nabla\times \mathbf{A}$ immediately gives $\nabla \cdot \mathbf{B}=0$ ; $\mathbf{E} := -\frac{\partial A}{\partial t} - \nabla \varphi$ immediately gives $\nabla \times \mathbf{E} =-\dot{\mathbf{B}}$ .

Finally, let us compare the Lagrangian and Hamiltonian formulations:

$\begin{matrix} \hline & \text{Lagrangian} & \text{Hamiltonian} \\\\ \hline \text{Field variables} & A\_\mu, \partial\_\mu A\_\nu & A\_\mu, \Pi^\mu \\\\ \hline \text{Eq. of motion} & \text{Euler-Lagrange equations} & \text{Hamiltonian equations} \\\\ & \partial\_\mu F^{\mu\nu}=J^\nu & \dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}},\quad \dot{\mathbf{\Pi}} = \frac{\delta \mathcal{H}}{\delta \mathbf{A}} \\\\ & \text{Ampere Law, Gauss Law} & \text{Ampere Law} \\\\ \hline \text{Constraints}  & \text{None} & \Pi^0=\dot{\Pi}^0=0\\\\ & & \text{Gauss Law} \\\\ \hline  \end{matrix}$

### 1.3Dirac-Bergmann Theory  

The above framework for treating constrained Hamiltonian systems is called Dirac-Bergmann theory. In it, $\Pi^0 = \frac{\partial \mathcal{L}}{\partial \dot{A\_0}} = 0$ is called the Primary constraint, and $\dot{\Pi}^0=-\frac{\delta \mathcal{H}}{\delta A\_0} =0$ is called the Secondary constraint. D-B theory provides a more systematic and rigorous treatment of these constraints.

### 1.4 Why Field Theory Usually Uses the Lagrangian Formulation  

Why is the Hamiltonian formulation of the electromagnetic field so inconvenient?

This is because in Lagrangian mechanics, time $t=x^0$ and spatial coordinates $x^{1,2,3}$ have relatively equal status, and Lorentz invariance is easily manifested. But in Hamiltonian mechanics, time $t$ has a special status, making Lorentz invariance difficult to manifest. It is precisely the special status of time $t=x^0$ that leads to constraints on the field component $A\_0$ and its corresponding canonical momentum $\Pi^0$ . This also causes the **Hamiltonian to lack gauge invariance**.

In classical (low-velocity) mechanics, using Hamiltonian mechanics is relatively convenient. But in the context of special relativity, time $t$ is elevated to the spacetime coordinate $x^0$ and can mix with the other spatial coordinates $x^{1,2,3}$ through Lorentz boosts, making Hamiltonian mechanics awkward.

The reason we can often use the Hamiltonian (and the corresponding Heisenberg/Schrödinger formulations) in quantum mechanics is precisely that quantum mechanics deals with low-velocity situations. But once we enter the domain of special relativity, we have to use quantum field theory, together with the Lagrangian and path-integral formulations.

---

## II. Hamiltonian Formulation of the Dirac Field  

All the steps performed above for the electromagnetic field $A\_\mu$ can also be carried out for the Dirac field $\psi$.

Starting from the Lagrangian of the Dirac field:

$\mathcal{L}=\bar{\psi}(\mathrm{i}\hbar c \gamma^\mu \partial\_\mu  -mc^2)\psi $

For convenience in the derivation, we use natural units: $\hbar = c =1$ , so

$\mathcal{L}=\bar{\psi}(\mathrm{i}\gamma^\mu \partial\_\mu -m)\psi $

The field variables are $\psi, \bar{\psi}$ , and their canonical momenta are:

$\pi\_\psi = \frac{\partial\mathcal{L}}{\partial (\partial\_0\psi)} = \mathrm{i}\bar\psi \gamma^0 = \mathrm{i} \psi^\dagger$

$\pi\_\bar\psi = \frac{\partial\mathcal{L}}{\partial (\partial\_0\bar\psi)} = 0$ （Primary constraint）

Legendre transformation:

$\begin{aligned} \mathcal{H} &= \pi\_\psi \partial\_0\psi + \pi\_{\bar\psi}\partial\_0\bar\psi - \mathcal{L} \\\\ &=\mathrm{i}\bar\psi \gamma^0 \partial\_0\psi-\bar{\psi}(\mathrm{i} \gamma^\mu \partial\_\mu  -m)\psi  \\\\ &= \bar{\psi}(-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi  \end{aligned}$

Hamilton equations:

$\begin{aligned} \partial\_0{\psi} &= \frac{\delta \mathcal{H}}{\delta\pi\_\psi}  \end{aligned}$

or

$\begin{aligned} \delta \mathcal{H} &= (\delta\pi\_\psi) \partial\_0{\psi} \\\\ &= \delta(\mathrm{i}\bar\psi \gamma^0 ) \partial\_0{\psi} \\\\ &= (\delta \bar\psi) \mathrm{i} \gamma^0  \partial\_0{\psi} \end{aligned}$

Thus,

$\begin{aligned} \mathrm{i} \gamma^0  \partial\_0{\psi} &= \frac{\delta \mathcal{H}}{\delta \bar\psi} \\\\ &= (-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi   \end{aligned}$

Rearranging gives:

$\boxed{ \mathrm{i} \gamma^\mu \partial\_\mu \psi - m\psi = 0 }$

This is the Dirac equation in vacuum.

If the electromagnetic field is nonzero, i.e., outside the vacuum, then we need to consider the total Lagrangian of the electromagnetic and Dirac fields:

$\boxed{ \begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial\_\mu -m)\psi - eA\_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F\_{\mu\nu} F^{\mu\nu} \end{aligned} }$

We may define $J^\mu = -e\bar\psi \gamma^\mu\psi$ (note that $e$ here is positive, whereas the electron $\psi$ carries negative charge), so the coupling term $- eA\_\mu \bar{\psi} \gamma^\mu \psi $ can also be written as $+A\_\mu J^\mu$ , consistent with the previous definition.

Applying the Legendre transformation to this Lagrangian gives:

$\boxed{ \begin{aligned} \mathcal{H} &= \frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 +  \bar{\psi}[-\mathrm{i}\bm\gamma\cdot (\nabla + \mathrm{i}e\mathbf{A} )+ m]\psi \\\\  &= \underbrace{\frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 }\_{\text{free photon field}} + \underbrace{\bar{\psi}(-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi }\_{\text{free Dirac field}} +\underbrace{e\bar\psi(\bm\gamma \cdot \mathbf{A})\psi}\_{\text{coupling}} \end{aligned} }$

Solving the corresponding Hamilton equations $\dot{\mathbf{\Pi}} = \delta \mathcal{H}/\delta\mathbf{A}, \ \dot\psi =  \delta\mathcal{H}/\delta \pi\_\psi$ yields the coupled Maxwell and Dirac equations.

> Note that, due to the absence of the $\bar\psi(-\mathrm{i}\gamma^0\partial\_0)\psi$ term and the $e\bar\psi(\gamma^0A\_0)\psi=-e\psi^\dagger\psi \phi = \rho\phi$ term associated with time $t=x^0$ , the **Hamiltonian is not gauge invariant**.  
>   
> We have already explained the reason: in the Hamiltonian formulation, time has a special status; in the Hamilton equation of motion $\partial\_0\varphi = \delta\mathcal{H}/\delta \pi\_\varphi$ , the time derivative $\partial\_0$ on the left-hand side is not gauge invariant ( $D\_0$ is gauge invariant), so the Hamiltonian on the right-hand side is evidently not gauge invariant either.

## III. Canonical Quantization  

If there is only an electromagnetic field or only a Dirac field, then because their Lagrangians/Hamiltonians contain only quadratic terms, the harmonic-oscillator model can be used to obtain analytical solutions directly. For example, the canonical quantization of the electromagnetic field in vacuum uses the harmonic-oscillator model in the Coulomb gauge $ \nabla \cdot \mathbf{A} = 0$ to obtain creation and annihilation operators for plane-wave modes and their evolution. The evolution of these modes is independent (decoupled).

> The analytical solution is $\mathbf{A}(\mathbf{x},t) = \sum\_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega\_\mathbf{k}V}} \left[ a\_{\mathbf{k},\sigma} \bm{\epsilon}\_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}(\mathbf{k}\cdot \mathbf{x}-\omega\_\mathbf{k}t)} + \text{h.c.} \right]$ , where $\epsilon\_{\mathbf{k},\sigma}$ denotes two vectors perpendicular to $\mathbf{k}$ and to each other, $\sigma$ denotes polarization, $\text{h.c.}$ denotes the Hermitian conjugate, and $V$ denotes the cavity volume. If it is not a cavity but all space, replace $\sum\frac{1}{\sqrt{V}}$ with $\int \mathrm{d}^3\mathbf{k} \frac{1}{(2\pi)^{3/2}}$ . Since canonical quantization is standard textbook material in quantum optics, we will not elaborate here; for details, see the appendix chapter of [Atom-Photon Interaction](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197).

In the presence of sources, we cannot impose $\phi=0$ under the condition $\nabla\cdot \mathbf{A}=0$ , which means that there are no longer only transverse modes $\mathbf{E}\_{\perp}(\mathbf{k},t) = -\partial\_t \mathbf{A}(\mathbf{k},t)$ ; there are also source-dependent longitudinal modes $\mathbf{E}\_{\parallel}(\mathbf{k},t) = -\mathrm{i}\mathbf{k} \phi(\mathbf{k},t) = -\mathrm{i}\frac{\mathbf{k}}{k^2} \rho(\mathbf{k},t)$ . The transverse modes $\mathbf{E}\_{\perp}$ can be represented by creation and annihilation operators for plane-wave modes, but the longitudinal modes $\mathbf{E}\_{\parallel}$ depend on the sources.

If we regard the source as a classical object, then the longitudinal modes cannot be quantized. But if we treat the source fully quantum mechanically—that is, treat it as a quantum field like $\mathbf{A}$ (namely $\rho = -e\bar\psi\gamma^0\psi =  -e\psi^\dagger\psi$ )—then the longitudinal modes are coupled to the Dirac field $\psi$ . At this point, the modes that can be decoupled are no longer plane-wave modes, but mixed modes of the electromagnetic and Dirac fields.

If we could solve for these modes, that would be fine. But this is exactly where the problem arises: unlike the free term $\bar{\psi}(-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi , \ \frac{1}{2}(\mathbf{E}^2+\mathbf{B}^2)$ , the coupling term $e\bar\psi A\_\mu\gamma^\mu \psi$ is not quadratic—it is cubic and anharmonic! This prevents us from analytically calculating the mixed modes; in other words, there is no analytical solution. At most, we can write $\mathbf{A}(\mathbf{x})$ rather than $\mathbf{A}(\mathbf{x},t)$ :

$\mathbf{A}(\mathbf{x}) = \sum\_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega\_\mathbf{k}V}} \left[ a\_{\mathbf{k},\sigma} \bm{\epsilon}\_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}\mathbf{k}\cdot \mathbf{x}} + \text{h.c.} \right]$

At this point, we can only solve the system using perturbation theory: treating the coupling term as a perturbation on the basis of the free term. Fortunately, the coupling constant $e = \sqrt{4\pi \alpha} \simeq 0.3$ (in natural units) between the electromagnetic and Dirac fields is not very strong, allowing perturbation theory to work. What follows is quantum field theory—calculating the S-matrix, scattering amplitudes, and so on—which will not be introduced here.

## IV. Low-Energy Approximation and the Schrödinger Equation  

At high energies, we need quantum field theory, but at low energies, we have a good approximate theory: quantum mechanics. In this section, we examine how the Hamiltonian in the high-energy regime reduces to an effective Hamiltonian in the low-energy regime.

### 4.1 High-Energy Physics / Low-Energy Physics  

Let us first review the physical meanings of the operator fields $\psi$ , $\bar\psi$ , and $A$ :

The physical meaning of the field $\psi(\mathbf{x},t)$ is to annihilate an electron or create a positron at the spacetime point $(\mathbf{x},t)$ .

The physical meaning of the field $\bar\psi$ is to create an electron or annihilate a positron.

In the Lagrangian/Hamiltonian, these two fields always appear in pairs because of charge conservation.

The field $A\_\mu$ can both create and annihilate photons, because the photon is its own antiparticle.

Therefore, the coupling term $ e\bar{\psi} \gamma^\mu A\_\mu \psi$ can describe the following various processes:

1. Annihilate an electron, create a photon, and then create an electron.
2. Annihilate an electron, annihilate a photon, and then create an electron.
3. Annihilate a photon and create an electron-positron pair.
4. Annihilate an electron-positron pair and create a photon.
5. ... (other higher-order processes)

Among these, 3 and 4, as well as other higher-order processes, belong to high-energy physics and require quantum field theory to handle.

By contrast, 1 and 2 belong to low-energy physics. They describe an electron transitioning from one state to another by absorbing or emitting a photon.

Considering only the low-energy regime means the following two points:

> 1. The number of electrons remains unchanged. There is no creation or annihilation of electron-positron pairs.  
> 2. The positron term $\psi = \begin{bmatrix}\psi\_1\\\\ \psi\_2\end{bmatrix}$ of the Dirac field is small $\psi \_2\approx 0$ . The electron term $\psi\_1 = \begin{bmatrix}\psi\_{1\uparrow} \\\\ \psi\_{1\downarrow}\end{bmatrix}$ is what concerns us. This is because our universe is filled with electrons, while positrons are scarce.

The theory in the low-energy regime can be greatly simplified; see Section 4.3. Before that, however, let us expand the Dirac equation to become familiar with it.

### 4.2 The Dirac Equation  

The Dirac equation is $\mathrm{i}\gamma^\mu D\_\mu \psi - m\psi=0$ , where

$\gamma^0 = \begin{bmatrix} I & 0 \\\\ 0 &-I \end{bmatrix},\  \gamma^i=\begin{bmatrix} 0 & \sigma^i \\\\ -\sigma^i & 0 \end{bmatrix} \quad(i=1,2,3)$

$\sigma^i $ are the Pauli matrices,

and $\psi = \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix}$ , where $\psi\_1 = \begin{bmatrix}\psi\_{1\uparrow} \\\\ \psi\_{1\downarrow}\end{bmatrix}$ are the two spin components of the electron, and $\psi\_2 = \begin{bmatrix}\psi\_{2\uparrow} \\\\ \psi\_{2\downarrow}\end{bmatrix}$ are the two spin components of the positron.

Substitution into the Dirac equation gives:

$\mathrm{i}\begin{bmatrix} I & 0 \\\\ 0 &-I \end{bmatrix} D\_t \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix} + \mathrm{i} \begin{bmatrix} 0 & \bm\sigma \cdot \mathbf{D} \\\\ -\bm\sigma \cdot \mathbf{D} & 0 \end{bmatrix} \begin{bmatrix}\psi\_1 \\\\ \psi\_2 \end{bmatrix} -m \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix}=0$

where $D\_t =  \partial\_t +\mathrm{i}eA\_0 = \partial\_t - \mathrm{i}e\phi$ , $\mathbf{D} = \nabla +\mathrm{i}e\mathbf{A}$ (using the $(-,+,+,+)$ metric convention).

Simplifying gives

$\mathrm{i} \begin{bmatrix}D\_t\psi\_1 \\\\ -D\_t\psi\_2\end{bmatrix} +\mathrm{i} \begin{bmatrix}\bm\sigma\cdot \mathbf{D} \psi\_2 \\\\ -\bm\sigma\cdot \mathbf{D}\psi\_1\end{bmatrix} -m \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix}=0$

namely,

$\boxed{ \begin{aligned} \mathrm{i} D\_t \psi\_1 + \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi\_2 - m\psi\_1 &= 0 \\\\ -\mathrm{i} D\_t \psi\_2 - \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi\_1 - m\psi\_2 &= 0 \end{aligned}  }\quad (\star)$

This is the expanded form of the Dirac equation: we write the electron term $\psi\_1$ and the positron term $\psi\_2$ as two equations. Originally, they were in the same equation.

We could further expand each of them into two equations corresponding to the two spins. However, since we are more familiar with Pauli operators, there is no need to do so.

Up to this point, we have made no approximations. Starting from the next section, we make a low-energy approximation to the Dirac equation.

### 4.3 Low-Energy Effective Hamiltonian  

In the low-energy regime, we do not consider the phase variation $\mathrm{e}^{-\mathrm{i}mt}$ caused by the electron's rest mass, so we factor it out, namely, replace $\psi = \begin{bmatrix}\psi\_1\\\\ \psi\_2\end{bmatrix}$ with $\psi = \begin{bmatrix}\varphi \mathrm{e}^{-\mathrm{i}mt}\\\\ \chi  \mathrm{e}^{-\mathrm{i}mt}\end{bmatrix}$ . Substituting this into the expanded Dirac equation $(\star)$ gives:

$\begin{aligned} &\mathrm{i} D\_t \varphi + \mathrm{i} \bm\sigma \cdot \mathbf{D} \chi  = 0 &(1)\\\\ -&\mathrm{i} D\_t \chi - \mathrm{i} \bm\sigma \cdot \mathbf{D} \varphi - 2m\chi = 0 &(2) \end{aligned}$

Since the positron term $\chi$ is small in the low-energy regime, $D\_t \chi \approx 0$ . Substituting this into $(2)$ gives:

$\chi \approx - \frac{\mathrm{i}}{2m} \bm\sigma \cdot \mathbf{D} \varphi$

Substituting it into $(1)$ gives:

$\mathrm{i} D\_t \varphi +  \frac{1}{2m}(\bm\sigma \cdot \mathbf{D})^2 \varphi = 0 $

It can be shown (see the appendix) that

$\begin{aligned} (\bm \sigma \cdot \mathbf{D})^2 &=\mathbf{D}^2 - \mathrm{i}e \bm\sigma\cdot \mathbf{B} \\\\ &= (\nabla +\mathrm{i}e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B} \\\\ &= -(\mathbf{p} + e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B}  \end{aligned}$

Therefore,

$\mathrm{i} D\_t \varphi =  \frac{1}{2m}[(\mathbf{p} + e\mathbf{A})^2 + e \bm\sigma\cdot \mathbf{B} ] \varphi$

Substituting $D\_t = \partial\_t - \mathrm{i}e\phi$ gives

$\boxed{ \mathrm{i} \partial\_t \varphi =  \left[\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2+ \frac{e}{2m} \bm\sigma\cdot \mathbf{B}  - e\phi  \right]\varphi }$

This is the Schrödinger equation for an electron with spin, also called the Pauli equation. Note that $e$ here is positive, while the electron $\varphi$ carries negative charge.

We may thus define the effective Hamiltonian of the electron as:

$\boxed{ H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2- \frac{e}{2m} \bm\sigma\cdot \mathbf{B}  - e\phi   }$

Because the magnetic field is much weaker than the electric field $B\sim E/c$ . The order of magnitude of the magnetic-field-related term ($\frac{e}{2m} \bm\sigma\cdot \mathbf{B}$ ) in the Hamiltonian is $\alpha\approx \frac{1}{137}$ times that of the electric-field-related term ($e\phi$ ). Therefore, in the usual Hamiltonian $H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2 - e\phi  $ , we may neglect the spin term $\frac{e}{2m} \bm\sigma\cdot \mathbf{B}$ .

Thus, the **low-energy limit of quantum field theory is quantum mechanics**.

> We know that when solving the spinless Schrödinger equation for the hydrogen atom, the results require fine-structure corrections. There are three such corrections: spin-orbit coupling, relativistic kinetic-energy correction, and the Darwin term. The kinetic-energy correction comes from the mass-energy relation $E^2 = p^2 +m^2$ ; the Darwin term comes from interference between the electron and positron terms (which can also be understood as fluctuations of virtual electron-positron pairs); and spin-orbit coupling, as its name suggests, comes from the electron's spin, which has already been taken into account in the Pauli equation.  
>   
> Therefore, solving the Pauli equation for the hydrogen atom yields the correction due to spin-orbit coupling. But it still does not yield the relativistic kinetic-energy correction or the Darwin term. To obtain all three fine-structure corrections simultaneously, quantum field theory and the Dirac equation are still required.  
>   
> In addition, there is another correction of the same order of magnitude as the fine-structure corrections, called the Lamb shift, which arises from fluctuations of the electromagnetic field (virtual photons), rather than fluctuations of electron-positron pairs.

---

## V. Long-Wavelength Approximation and the Dipole Representation  

We now consider the interaction between a light field and an electron in an atom. The first approximation we must make is the **Born-Oppenheimer approximation**, namely, decoupling the Hamiltonians of the atomic core and the electron so that we need consider only the electron Hamiltonian. This is because electron motion is much faster than atomic-core motion, allowing the force on the atomic core to be treated as an average force; conversely, the electron can be regarded as moving in an unchanging background Coulomb potential. Next, we make a series of other approximations.

### 5.1 Long-Wavelength Approximation (Dipole Approximation)  

Since the Bohr radius (~50pm) is much smaller than an optical wavelength (~500nm), we may neglect electromagnetic-field gradients within the atom, that is, replace $\mathbf{A}(\mathbf{x})$ in the Hamiltonian $H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2 - e\phi  + H\_\text{EM}$ with a field $\mathbf{A}(\mathbf{0})$ that depends only on time. Here, $H\_\text{EM}=\sum\_{\mathbf{k,\sigma}} \omega\_{\mathbf{k,\sigma}}\left(a\_{\mathbf{k,\sigma}}^\dagger a\_{\mathbf{k,\sigma}} + \frac{1}{2}\right)$ is the Hamiltonian of the light field.

Substituting $\mathbf{x}=\mathbf{0}$ into $\mathbf{A}(\mathbf{x}) = \sum\_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega\_\mathbf{k}V}} \left[ a\_{\mathbf{k},\sigma} \bm{\epsilon}\_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}\mathbf{k}\cdot \mathbf{x}} + \text{h.c.} \right]$ gives

$\mathbf{A}(\mathbf{0}) = \sum\_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega\_\mathbf{k}V}} \left(a\_{\mathbf{k},\sigma} + a^\dagger\_{\mathbf{k},\sigma}\right) \bm{\epsilon}\_{\mathbf{k},\sigma} $

This approximation is also called the dipole approximation, because it is equivalent to neglecting higher-order terms (quadrupole, octupole, and so on) in the multipole expansion.

### 5.2 Dipole Representation  

Define the dipole operator as $\mathbf{d}=-e\mathbf{x}$ ( $e$ is positive, and $\mathbf{x}$ is the position of the electron relative to the nucleus), and perform the unitary transformation

$\boxed{U=\exp\left[ -\mathrm{i}\mathbf{d}\cdot \mathbf{A}(\mathbf{0})\right]} = \exp\left[ \sum\_{\mathbf{k},\sigma} (\lambda \_{\mathbf{k,\sigma}} a\_{\mathbf{k,\sigma}}^\dagger - \lambda\_{\mathbf{k,\sigma}}^\* a\_{\mathbf{k,\sigma}} )\right] = \prod\_{\mathbf{k,\sigma}} D\_{\mathbf{k,\sigma}}(\lambda\_{\mathbf{k,\sigma}})$

where $\lambda\_{\mathbf{k,\sigma}} = -\mathrm{i}\mathbf{d}\cdot \epsilon\_{\mathbf{k,\sigma}}$ , and $D\_{\mathbf{k,\sigma}}(\alpha) = \exp( \alpha a^\dagger\_{\mathbf{k,\sigma}} - \alpha a\_{\mathbf{k,\sigma}})$ is the translation operator on the $({\mathbf{k,\sigma}})$ mode.

It can be shown[#ref\\\\_1](#ref\\\\_1) that the Hamiltonian in the new representation is:

$\boxed{ H \mapsto U^\dagger H U = \frac{1}{2m}\mathbf{p}^2 - e\phi  +\mathbf{d}\cdot \mathbf{E}\_\perp(\mathbf{0}) + H\_\text{EM}+ H\_{\text{dip}} } \quad (3)$

where $ \mathbf{E}\_\perp(\mathbf{0}) = \sum\_{\mathbf{k,\sigma}} \mathrm{i} \sqrt{\frac{\omega\_k}{2V}} (a\_{\mathbf{k,\sigma}} - a^\dagger\_{\mathbf{k,\sigma}}) \epsilon\_{\mathbf{k,\sigma}}$ is the transverse component of the electric field, and $H\_{\text{dip}} = \sum\_{\mathbf{k,\sigma}} \frac{1}{2V} (\epsilon\_{\mathbf{k,\sigma}} \cdot \mathbf{d})^2$ is the dipole self-energy, which can usually be neglected.

This representation is called the $\mathbf{d}\cdot\mathbf{E}$ representation, also known as the dipole representation. The original representation is called the $\mathbf{p}\cdot \mathbf{A}$ representation.

### 5.3 Two-Level Approximation  

We now simplify the atom to a two-level system (with only a ground state and an excited state), that is, simplify the atomic Hamiltonian $\frac{1}{2m}\mathbf{p}^2 - e\phi$ to $H\_{\text{atom}} = \frac{\omega\_{ab}}{2} \sigma\_z$ , where $\omega\_{ab}$ is the energy-level separation, $\sigma\_z = |b\rangle\langle b| - |a\rangle\langle a|$ , $|b\rangle$ is the excited state, and $|a\rangle$ is the ground state.

Transitions between the two levels impose requirements on the polarization state of the light field (selection rules). Here, we consider only the corresponding polarization state $\sigma$ , so that $\mathbf{d} \cdot \mathbf{E}\_{\perp}(\mathbf0)$ becomes $dE\_\perp(0)$ .

In addition, the dipole operator must be projected onto the two-level subspace: $d\mapsto (|a\rangle\langle a| + |b\rangle\langle b| ) d = d\_{ab}|a\rangle\langle b| + d\_{ba} |b\rangle \langle a|$ . Here $d\_{ba} = d\_{ab}^\*$ .

> The absence of the $d\_{aa} |a\rangle \langle a|$ term is because $d\_{aa} =-e \int \langle \psi\_a|\mathbf{x}|\psi\_a\rangle =-e\int\psi^\*(\mathbf{x})\ \mathbf{x}\ \psi(\mathbf{x})\mathrm{d}^3\mathbf{x}= 0$ . Similarly, $d\_{bb}=0$ also holds.

We can always choose the phase $d\_{ab} \mapsto d\_{ab}\mathrm{e}^{\mathrm{i}\theta}$ such that $d\_{ab} = d\_{ba}$ is real, because the overall phase is unimportant. Thus, the dipole operator can be written as:

$\boxed{ d=d\_{ab}(\sigma\_+ +\sigma\_-) }$

where $\sigma\_+ = |b\rangle\langle a|,\ \sigma\_-=|a\rangle\langle b|$ .

The electric-field operator can be written as:

$E\_\perp(\mathbf{0}) = \sum\_{\mathbf{k}} \mathrm{i} \sqrt{\frac{\omega\_k}{2V}} (a\_{\mathbf{k}} - a^\dagger\_{\mathbf{k}}) $

We may absorb the imaginary factor $\mathrm{i}$ into the annihilation operator: $a\_{\mathbf{k}} \mapsto \mathrm{i}a\_\mathbf{k}, \ a\_{\mathbf{k}}^\dagger \mapsto -\mathrm{i}a\_{\mathbf{k}}^\dagger$ . Thus,

$\boxed{ E\_\perp(\mathbf{0}) = \sum\_{\mathbf{k}} \sqrt{\frac{\omega\_k}{2V}} (a\_{\mathbf{k}} +a^\dagger\_{\mathbf{k}})  }$

Substituting these relations into the Hamiltonian $(3)$ in the dipole representation, and neglecting the dipole self-energy, yields:

$\boxed{ H =  \frac{\omega\_{ab}}{2} \sigma\_z +\sum\_{\mathbf{k}} g\_{\mathbf{k}}(\sigma\_+ +\sigma\_-)(a\_{\mathbf{k}} +a^\dagger\_{\mathbf{k}}) + H\_\text{EM} }$

where $g\_{\mathbf{k}}=d\_{ab}\sqrt{\frac{\omega\_k}{2V}} $ is the coupling strength between the two-level system and the light field.

### 5.4 Cavity Quantum Electrodynamics (Cavity QED)  

Now consider placing the atom in a very small cavity with cavity length $\sim 100 \mu \text{m}$ . The free spectral range is then $c/(2L)\sim 1.5 \text{THz}$ , meaning that the frequency difference between adjacent modes is $\sim 1.5 \text{THz}$ , much greater than the natural linewidth $\sim 10 \text{MHz}$ and the coupling strength $g\sim 100\text{MHz}$ . This allows us to select a single light-field mode to interact with the two-level atom. Consequently, the detunings $\Delta =\omega\_\mathbf{k}-\omega\_{ab}$ of the other light-field modes are large and can be neglected.

Thus, we obtain the interaction Hamiltonian between a single light field and a single electron in the atom:

$\boxed{ H =  \frac{\omega\_{ab}}{2} \sigma\_z +g(\sigma\_+ +\sigma\_-)(a +a^\dagger) + \omega\left(a^\dagger a +\frac{1}{2}\right) }$

where $g = g\_{\mathbf{k}}$ , and $\omega=\omega\_\mathbf{k}$ are the coupling strength and frequency of the selected light field.

Another advantage of the cavity is that the coupling strength $g\_{\mathbf{k}}=d\_{ab}\sqrt{\frac{\omega\_k}{2V}} $ is relatively strong because the mode volume $V$ is very small.

Since $\sigma\_+ a^\dagger$ represents creating a photon while the electron transitions from the lower energy level to the higher one, its probability is very low $\sim\frac{1}{\omega+\omega\_{ab}}$ and it can be neglected. Similarly, $\sigma\_-a$ can also be neglected. This is called the Rotating Wave Approximation (RWA).

After applying the rotating-wave approximation, we obtain the Jaynes-Cummings Hamiltonian:

$\boxed{ H =  \frac{\omega\_{ab}}{2} \sigma\_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger)  }$

The Jaynes-Cummings model has an [analytical solution](https://zhuanlan.zhihu.com/p/701838204), called dressed states. They will not be introduced here due to space limitations.

## Epilogue: The Charm of Physics  

We started from the highly complex QED Lagrangian:

$\begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial\_\mu -m)\psi - eA\_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F\_{\mu\nu} F^{\mu\nu} \end{aligned} $

This Lagrangian is highly complex: it not only takes into account the electron's antiparticle—the positron—but the coupling term $- eA\_\mu \bar{\psi} \gamma^\mu \psi$ is also a cubic term, capable of describing multiple processes such as electron-positron pair creation/annihilation. It has no analytical solution and can only be solved using perturbation theory in quantum field theory.

But after a series of simplifications and approximations (the low-energy approximation, the Born-Oppenheimer approximation, the long-wavelength/dipole approximation, the two-level approximation, and the rotating-wave approximation), we unexpectedly arrive at a model with an analytical solution!

$H =  \frac{\omega\_{ab}}{2} \sigma\_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger) $

Clearly, according to the situation under consideration, we make a series of appropriate and necessary simplifications, thereby grasping the essence amid the complexity of phenomena and ultimately gaining a better understanding of the world.

This methodology can be applied not only in physics, but also generalized to other disciplines. This is the charm of physics.

---

The [Higher and More Elegant Electrodynamics] series ends here. I hope you enjoyed this journey!

## Appendix  

Prove $(\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B}$ , where $\mathbf{D} = \nabla+ \mathrm{i}e\mathbf{A}$ .

> From the identity $(\bm\sigma \cdot \mathbf{a})(\bm\sigma \cdot \mathbf{b}) = \mathbf{a} \cdot \mathbf{b} + \mathrm{i}\bm\sigma \cdot(\mathbf{a}\times\mathbf{b})$ , we obtain  
>   
>  $(\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D})$   
>   
> Thus, we need to calculate $(\mathbf{D}\times\mathbf{D})$ .  
>   
> First, let us calculate $[D\_i, D\_j]$ :  
>  $\begin{aligned} [D\_i, D\_j] &= [\partial\_i +\mathrm{i}eA\_i, \partial\_j +\mathrm{i}eA\_j] \\\\ &= \cancel{[\partial\_i,\partial\_j]} + \cancel{e^2[A\_i, A\_j]} + \mathrm{i}e[\partial\_i, A\_j] - \mathrm{i}e[\partial\_j,A\_i] \end{aligned}$   
>   
> Thus, we need to calculate $[\partial\_i, A\_j]$ :  
>   
>  $\begin{aligned} [\partial\_i, A\_j] f &= \partial\_i (A\_j f) -A\_j \partial\_i f \\\\ &= (\partial\_i A\_j) f + A\_j \partial\_if - A\_j \partial\_i f \\\\ &= (\partial\_iA\_j)f \end{aligned}$   
>   
> Therefore, $[\partial\_i, A\_j] = (\partial\_i A\_j)$ .  
>   
> Thus,  
>   
>  $\begin{aligned} [D\_i, D\_j] &= \mathrm{i}e[\partial\_i, A\_j] -\mathrm{i}e[\partial\_j,A\_i] \\\\ &= \mathrm{i}e (\partial\_i A\_j - \partial\_j A\_i) \\\\ &= \mathrm{i}e \epsilon\_{ijk}B^k \end{aligned}$   
>   
> Thus,  
>   
>  $\begin{aligned} (\mathbf{D}\times\mathbf{D})^k &=\epsilon^{kij} D\_i D\_j \\\\ &= \frac{1}{2} \epsilon^{kij}[D\_i,D\_j] \\\\ &= \frac{\mathrm{i}e}{2} \epsilon^{kij} \epsilon\_{ijl} B^l \\\\ &= \frac{\mathrm{i}e}{2} (\delta^k\_l \delta^j\_j - \delta^k\_j\delta^j\_l) B^l \\\\ &=\mathrm{i}e \delta^k\_l B^l \\\\ &= \mathrm{i}eB^k \end{aligned}$   
>   
> Therefore, $\mathbf{D}\times \mathbf{D} = \mathrm{i}e\mathbf{B}$ .  
>   
> Thus,  
>  $\begin{aligned} (\bm\sigma \cdot \mathbf{D})^2 &= \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D}) \\\\ &= \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B} \end{aligned}$   
>   
> Q.E.D.

## References  

1. Atom-Photon Interactions by Cohen-Tannoudji [https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197)
