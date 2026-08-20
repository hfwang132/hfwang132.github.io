---
title: "Electrodynamics from the Perspective of Hamiltonian Mechanics [Higher and More Elegant Electrodynamics · 5]"
date: 2025-03-22T23:16:56+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/32052863470"
author: "Haifei"
tags: ["Electrodynamics"]
categories: ["Mathematical Methods in Physics"]
---

Previous article in this series:

[Godfly: Dirac Magnetic Monopoles—Chern Classes and Chern Numbers [Higher and More Elegant Electrodynamics · 4]](https://zhuanlan.zhihu.com/p/1889370433708609679)

---

In a [previous article](https://zhuanlan.zhihu.com/p/23958176393), we discussed the Hamiltonians of the electromagnetic field and the Dirac field:

$$\begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi - eA_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \end{aligned} $$

So what are their Hamiltonians? Why does quantum field theory not make much use of Hamiltonians? Read on for the answer.

---

## I. Hamiltonian Formulation of the Electromagnetic Field  

The Lagrangian of the electromagnetic field is known to be:

$$\begin{aligned} \mathcal{L}[A_\mu, \partial_\nu A_\mu] &=  -\frac{1}{4\mu_0} F_{\mu\nu} F^{\mu\nu} + A_{\mu} J^{\mu} \\ &= \frac{1}{2}\left(\epsilon_0\mathbf{E^2} -\frac{1}{\mu_0} \mathbf{B^2}\right) -\rho\phi + \mathbf{A} \cdot \mathbf{J} \end{aligned} $$

In this section, we attempt to start from it, derive the Hamiltonian, and obtain the Hamiltonian canonical equations, namely Maxwell's equations.

### 1.1 Hamiltonian of the Electromagnetic Field  

Let us first try directly using the Legendre transformation:

$$\mathcal{H} = \Pi^i  \dot{A}_i - \mathcal{L}$$

where $\Pi^i = \frac{\partial \mathcal{L}}{\partial \dot{ A}_i}$ is the canonical momentum corresponding to $\mathbf{A}$.

We hope to obtain Maxwell's equations from the eight Hamiltonian equations:

$$\boxed{ \dot{A}_i = \frac{\delta \mathcal{H}}{\delta \Pi^i},\quad \dot{\Pi}^i = \frac{\delta \mathcal{H}}{\delta A_i} }$$

where the symbol $\delta$ denotes variation.

However, things are not so simple. Notice that the canonical momentum $\Pi^0 = \frac{\partial \mathcal{L}}{\partial \dot{\phi}} = 0$ is identically zero! This indicates that it is a constraint.

Thus,

$$\mathcal{H} = \mathbf{\Pi} \cdot \dot{\mathbf{A}} - \mathcal{L}$$

where $\mathbf{\Pi}=\frac{\partial \mathcal{L}}{\partial \dot{\mathbf{A}}} = \dot{\mathbf{A}} + \nabla \phi = -\mathbf{E}$ is the canonical momentum corresponding to $\mathbf{A}$.

Thus,

$$\begin{aligned} \mathcal{H} &= (\dot{\mathbf{A}} + \nabla \phi) \cdot \dot{\mathbf{A}} - \left[\frac{1}{2}(\dot{\mathbf{A}}+\nabla \phi)^2 -\frac{1}{2} (\nabla \times \mathbf{A})^2 - \rho \phi + \mathbf{A}\cdot \mathbf{J} \right]  \\ &= \frac{1}{2}\mathbf{\Pi}^2 - \mathbf{\Pi} \cdot \nabla \phi + \frac{1}{2} (\nabla \times \mathbf{A})^2 + \rho \phi - \mathbf{A}\cdot \mathbf{J}  \end{aligned}$$

Using integration by parts during variation, $- \mathbf{\Pi} \cdot \nabla \phi $ can be converted into $+\phi \nabla \cdot \mathbf{\Pi}$. Thus:

$$\boxed{ \begin{aligned}  \mathcal{H}=\frac{1}{2}\mathbf{\Pi}^2   + \frac{1}{2} (\nabla \times \mathbf{A})^2 - \mathbf{A}\cdot \mathbf{J}+ \phi(\rho +\nabla\cdot \mathbf{\Pi})    \end{aligned} }$$

### 1.2 Canonical Equations of the Electromagnetic Field  

We now consider the Hamilton equations $\dot{\Pi}^0 = -\frac{\delta \mathcal{H}}{\delta A_0} $. Since $\Pi^0$ is always zero, $\dot{\Pi}^0$ should likewise always be zero. Thus, according to the Hamilton equations:

$$\dot{\Pi}_0 = -\frac{\delta \mathcal{H}}{\delta A_0} = -\frac{\delta \mathcal{H}}{\delta \phi} = \rho + \nabla \cdot \mathbf{\Pi} = 0\Rightarrow  \boxed{\nabla\cdot \mathbf{E} = \rho}$$

This is precisely Gauss's law. In the Hamiltonian formulation, it appears as a constraint. And $\phi$ is the corresponding Lagrange multiplier.

This shows that, in the Hamiltonian formulation, $\phi$ is not an independent dynamical variable. We may as well take $\phi =0$; this is called the Weyl gauge.

> The Weyl gauge is an incomplete gauge, because the remaining $A_1,A_2,A_3$ still has gauge freedom.

Of course, we may also choose other gauges. For example, in the Coulomb gauge $\nabla \cdot \mathbf{A} = 0$, $\phi$ then depends on $\mathbf{A}$ (according to gauge transformations).

Substituting the constraint $ \rho + \nabla \cdot \mathbf{\Pi} = 0$ into $\mathcal{H}$ yields:

$$\boxed{ \begin{aligned} \mathcal{H} &= \frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 - \mathbf{A}\cdot \mathbf{J}\\ &= \frac{1}{2}\mathbf{E}^2  + \frac{1}{2} \mathbf{B}^2  - \mathbf{A}\cdot \mathbf{J}   \end{aligned} }$$

> Notice that the Hamiltonian contains no potential-energy term $\rho \phi$. This is related to the Hamiltonian not being gauge invariant; see the end of Section II.  
>   
> Let us see why the Hamiltonian is not gauge invariant:  
>   
> In the Hamiltonian formulation, the equation of motion for the field $\varphi$ is $\partial_t \varphi = \delta \mathcal{H}/\delta \pi_\varphi$, where the field $\pi_\varphi$ is the canonical momentum corresponding to the field $\varphi$.  
>   
> Notice that the derivative on the left-hand side of the equation of motion is $\partial_t$, rather than the gauge-invariant covariant derivative $D_t = \partial_t + \mathrm{i}eA_t = \partial_t -\mathrm{i}e\phi$. Accordingly, the right-hand side of the equation is also not gauge invariant.  
>   
> This is one reason why the Hamiltonian formulation is not commonly used in high-energy physics.

Finally, let us consider the remaining Hamilton equations:

$$\dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}},\quad \dot{\mathbf{\Pi}} = \frac{\delta \mathcal{H}}{\delta \mathbf{A}}$$

The former $\dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}} = \mathbf{\Pi} - \nabla\phi \Rightarrow \mathbf{E} = -\frac{\partial A}{\partial t} - \nabla \phi$ is the defining equation of the electric field, while the latter is Ampère's law:

$$\begin{aligned} \dot{\mathbf{\Pi}} &= -\frac{\delta \mathcal{H}}{\delta \mathbf{A}} \\ &= -\frac{\delta }{\delta \mathbf{A}} \int\left[\frac{1}{2}(\nabla \times \mathbf{A})^2 - \mathbf{J} \cdot \mathbf{A}\right] \mathrm{d}^3 x  \\&= \int[-\nabla\times(\nabla\times \mathbf{A}) + \mathbf{J}]\mathrm{d}^3x \end{aligned}$$

namely,

$$\boxed{ \begin{aligned} &\dot{\mathbf{E}}=\nabla\times\mathbf{B} -\mathbf{J} \\ &\Rightarrow   \nabla\times \mathbf{B} = \mathbf{J} + \dot{\mathbf{E}} \end{aligned} }$$

We now have Ampère's law and Gauss's law. But where have the other two equations gone? In fact, similar to $\mathrm{d}F=\mathrm{d}\mathrm{d}A=0$ in the Lagrangian formulation, in the Hamiltonian formulation the other two source-free equations are also part of the definitions. From $\mathbf{B}:=\nabla\times \mathbf{A}$, one obtains $\nabla \cdot \mathbf{B}=0$; from $\mathbf{E} := -\frac{\partial A}{\partial t} - \nabla \varphi$, one obtains $\nabla \times \mathbf{E} =-\dot{\mathbf{B}}$.

Finally, let us compare the Lagrangian and Hamiltonian formulations:

$$\begin{matrix} \hline & \text{Lagrangian} & \text{Hamiltonian} \\ \hline \text{Field variables} & A_\mu, \partial_\mu A_\nu & A_\mu, \Pi^\mu \\ \hline \text{Eq. of motion} & \text{Euler-Lagrange equations} & \text{Hamiltonian equations} \\ & \partial_\mu F^{\mu\nu}=J^\nu & \dot{\mathbf{A}} = \frac{\delta \mathcal{H}}{\delta \mathbf{\Pi}},\quad \dot{\mathbf{\Pi}} = \frac{\delta \mathcal{H}}{\delta \mathbf{A}} \\ & \text{Ampere Law, Gauss Law} & \text{Ampere Law} \\ \hline \text{Constraints}  & \text{None} & \Pi^0=\dot{\Pi}^0=0\\ & & \text{Gauss Law} \\ \hline  \end{matrix}$$

### 1.3 Dirac-Bergmann Theory  

The above set of methods for handling constrained Hamiltonian systems is called Dirac-Bergmann theory. Here $\Pi^0 = \frac{\partial \mathcal{L}}{\partial \dot{A_0}} = 0$ is called the Primary constraint, and $\dot{\Pi}^0=-\frac{\delta \mathcal{H}}{\delta A_0} =0$ is called the Secondary constraint. D-B theory provides a more systematic and rigorous treatment of these constraints.

### 1.4 Why Field Theory Usually Uses the Lagrangian Formulation  

Why is the Hamiltonian formulation of the electromagnetic field so inconvenient?

This is because, in Lagrangian mechanics, time $t=x^0$ and spatial coordinates $x^{1,2,3}$ have relatively equal status, and Lorentz invariance is easily manifested. But in Hamiltonian mechanics, time $t$ has a special status, making Lorentz invariance difficult to manifest. It is precisely the special status of time $t=x^0$ that leads to the constraints on the field component $A_0$ and its corresponding canonical momentum $\Pi^0$. This also causes the **Hamiltonian not to be gauge invariant**.

In classical (low-velocity) mechanics, Hamiltonian mechanics is relatively convenient to use. But in the context of special relativity, time $t$ is elevated to the spacetime coordinate $x^0$, which can mix with the other spatial coordinates $x^{1,2,3}$ through Lorentz boosts; Hamiltonian mechanics then becomes awkward.

The reason we can often use Hamiltonians in quantum mechanics (as well as the corresponding Heisenberg/Schrödinger formulations) is precisely that quantum mechanics deals with low-velocity situations. But upon entering the realm of special relativity, we must use quantum field theory, together with the Lagrangian and path-integral formulation.

---

## II. Hamiltonian Formulation of the Dirac Field  

All the steps performed above for the electromagnetic field $A_\mu$ can also be performed for the Dirac field $\psi$.

Starting from the Lagrangian of the Dirac field:

$$\mathcal{L}=\bar{\psi}(\mathrm{i}\hbar c \gamma^\mu \partial_\mu  -mc^2)\psi $$

For convenience in the derivation, we adopt natural units: $\hbar = c =1$, so that

$$\mathcal{L}=\bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi $$

The field variables are $\psi, \bar{\psi}$, and their canonical momenta are:

$$\pi_\psi = \frac{\partial\mathcal{L}}{\partial (\partial_0\psi)} = \mathrm{i}\bar\psi \gamma^0 = \mathrm{i} \psi^\dagger$$

$\pi_{\bar\psi} = \frac{\partial\mathcal{L}}{\partial (\partial_0\bar\psi)} = 0$ (Primary constraint)

Legendre transformation:

$$\begin{aligned} \mathcal{H} &= \pi_\psi \partial_0\psi + \pi_{\bar\psi}\partial_0\bar\psi - \mathcal{L} \\ &=\mathrm{i}\bar\psi \gamma^0 \partial_0\psi-\bar{\psi}(\mathrm{i} \gamma^\mu \partial_\mu  -m)\psi  \\ &= \bar{\psi}(-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi  \end{aligned}$$

Hamilton equations:

$$\begin{aligned} \partial_0{\psi} &= \frac{\delta \mathcal{H}}{\delta\pi_\psi}  \end{aligned}$$

or

$$\begin{aligned} \delta \mathcal{H} &= (\delta\pi_\psi) \partial_0{\psi} \\ &= \delta(\mathrm{i}\bar\psi \gamma^0 ) \partial_0{\psi} \\ &= (\delta \bar\psi) \mathrm{i} \gamma^0  \partial_0{\psi} \end{aligned}$$

Thus,

$$\begin{aligned} \mathrm{i} \gamma^0  \partial_0{\psi} &= \frac{\delta \mathcal{H}}{\delta \bar\psi} \\ &= (-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi   \end{aligned}$$

Rearranging gives:

$$\boxed{ \mathrm{i} \gamma^\mu \partial_\mu \psi - m\psi = 0 }$$

This is the Dirac equation in vacuum.

If the electromagnetic field is nonzero, i.e., outside the vacuum, then we need to consider the total Lagrangian of the electromagnetic and Dirac fields:

$$\boxed{ \begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi - eA_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \end{aligned} }$$

We may define $J^\mu = -e\bar\psi \gamma^\mu\psi$ (note that $e$ here is positive, whereas the electron $\psi$ carries negative charge), so the coupling term $- eA_\mu \bar{\psi} \gamma^\mu \psi $ can also be written as $+A_\mu J^\mu$, consistent with the previous definition.

Applying the Legendre transformation to this Lagrangian yields:

$$\boxed{ \begin{aligned} \mathcal{H} &= \frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 +  \bar{\psi}[-\mathrm{i}\bm\gamma\cdot (\nabla + \mathrm{i}e\mathbf{A} )+ m]\psi \\  &= \underbrace{\frac{1}{2}\mathbf{\Pi}^2  + \frac{1}{2} (\nabla \times \mathbf{A})^2 }_{\text{free photon field}} + \underbrace{\bar{\psi}(-\mathrm{i}\bm\gamma\cdot \nabla + m)\psi }_{\text{free Dirac field}} +\underbrace{e\bar\psi(\bm\gamma \cdot \mathbf{A})\psi}_{\text{coupling}} \end{aligned} }$$

Solving the corresponding Hamilton equations $\dot{\mathbf{\Pi}} = \delta \mathcal{H}/\delta\mathbf{A}, \ \dot\psi =  \delta\mathcal{H}/\delta \pi_\psi$ yields the coupled Maxwell and Dirac equations.

> Notice that, due to the absence of the $\bar\psi(-\mathrm{i}\gamma^0\partial_0)\psi$ term and the $e\bar\psi(\gamma^0A_0)\psi=-e\psi^\dagger\psi \phi = \rho\phi$ term involving time $t=x^0$, the **Hamiltonian is not gauge invariant**.  
>   
> We have already explained the reason: in the Hamiltonian formulation, time has a special status; in the Hamiltonian equation of motion $\partial_0\varphi = \delta\mathcal{H}/\delta \pi_\varphi$, the time derivative $\partial_0$ on the left-hand side is not gauge invariant ($D_0$ is gauge invariant), so the Hamiltonian on the right-hand side certainly is not gauge invariant either.

---

Next article in this series (the final article):

[Godfly: From Quantum Field Theory to Cavity Quantum Electrodynamics [Higher and More Elegant Electrodynamics · 6]](https://zhuanlan.zhihu.com/p/1894566826417034044)
