---
title: "The Electromagnetic Field Is More Than Just Electric and Magnetic Fields—The AB Effect and Berry Connection [Higher and More Elegant Electrodynamics · 3]"
date: 2025-03-23T20:20:44+08:00
originalURL: "https://zhuanlan.zhihu.com/p/32173040413"
aliases:
  - "/en/gm_3/"
  - "/en/Post_20250406_电磁场不只是电场和磁场-AB效应与Berry联络-更高更妙的电动力学-3/"
draft: false
categories: ["mathematical physics methods"]
tags: ["differential geometry", "Berry connection", "electrodynamics"]
---

The electromagnetic field is not merely the electric and magnetic fields.

In other words, the electromagnetic field is more than just the electric and magnetic fields.

What does this mean?

## I. Electromagnetic Potentials Have a Higher Status Than Field Strengths  

In the [previous article](https://zhuanlan.zhihu.com/p/23958176393), we left a question unresolved:

> $\boxed{\begin{aligned} \phi &\mapsto \phi - \partial\_t \lambda \\\\ \mathbf{A} &\mapsto \mathbf{A} + \nabla \lambda \end{aligned}}$  
>   
> Students who have studied classical electrodynamics all know that this is an electromagnetic gauge transformation, and that the physics is unaffected before and after the transformation.  
>   
> In classical electrodynamics, we always regard Maxwell's equations as first principles and gauge transformations as a derivative concept; we regard electric and magnetic fields as fundamental entities, while treating the scalar and vector potentials as convenient mathematical tools with no actual physical effect. It is precisely because gauge transformations do not affect the electric and magnetic fields that we derive gauge transformations.  
>   
> But is field strength really the whole story?  
>   
> No! From a higher perspective, the electromagnetic potential $A = (\phi, \mathbf{A})$ is the fundamental physical entity, while the field strength is derivative.

You may have many questions: in electrodynamics, are field strengths $\mathbf{E}$ and $\mathbf{B}$ not the entirety of the electromagnetic field? Do Maxwell's equations not describe the evolution of field strengths? Are observables not limited to field strengths? Given the existence of gauge freedom, is the electromagnetic potential $A = (\phi, \mathbf{A})$ not unobservable?

Indeed, in classical electrodynamics, the views above are entirely correct.

However, upon entering the quantum realm, people gradually discovered that field strengths $\mathbf{E}$ and $\mathbf{B}$ are not the whole story: some phenomena cannot be explained using only $\mathbf{E}$ and $\mathbf{B}$, but can only be explained using the electromagnetic potential $A$.

This phenomenon is the Aharonov–Bohm effect (AB effect for short). It was not until the discovery of the AB effect that people formally established the ontological status of $A$, regarding field strengths $\mathbf{E}$ and $\mathbf{B}$ as derivatives.

In quantum electrodynamics, you will hardly see $\mathbf{E}$ and $\mathbf{B}$. They are replaced by the electromagnetic potential $A$.

## II. The Aharonov-Bohm Effect  

Let us now briefly derive the AB effect.

In the [previous article](https://zhuanlan.zhihu.com/p/23958176393), we stated that the covariant derivative is $D\_\mu=\partial\_\mu + \mathrm{i}\frac{e}{h}A\_\mu$.

Now, let an electron move slowly along a path. Its covariant derivative should then vanish:

$D\_\mu \psi = 0$

> This is just as in general relativity: when we parallel-transport a vector, we set its covariant derivative to zero.

Thus,

$\begin{aligned} &D\_\mu\psi=0\\\\ &\Rightarrow\left(\partial\_\mu + \mathrm{i}\frac{e}{h}A\_\mu\right) \psi =0 \\\\ &\Rightarrow  \partial\_\mu \psi = -\mathrm{i}\frac{e}{\hbar} A\_\mu \psi \\\\ &\Rightarrow \psi(x) = \psi(x\_0) \exp\left( -\mathrm{i}\frac{e}{\hbar}\int A\_\mu \mathrm{d}x^\mu\right) \end{aligned}$

Clearly, in addition to the dynamical phase $\int\frac{e}{\hbar}A\_0 \mathrm{d}x^0 = \int\frac{1}{\hbar} E \mathrm{d}t$, the electron acquires an extra phase $\color{red}{\int \frac{e}{\hbar} \mathbf{A} \cdot \mathrm{d}\mathbf{l}}$. This is the Aharonov-Bohm phase.

Consider a very long solenoid, with a magnetic field inside it but zero magnetic field outside. Now let an electron slowly circle it once. Compared with the case in which no current flows through the solenoid, the phase accumulated by the electron changes by

$\boxed{\begin{aligned} \Delta \theta = \frac{e}{\hbar}\oint \mathbf{A} \cdot \mathrm{d}\mathbf{l} = \frac{e}{\hbar}\int \mathbf{B} \cdot \mathrm{d}\mathbf{S} = \frac{e }{\hbar}\Phi \end{aligned}}$

where $\Phi$ is the magnetic flux inside the solenoid.

People were astonished to discover that the electron did not pass through any $\mathbf{E},\mathbf{B}$. In other words, along the electron's path, $\mathbf{E}=\mathbf{B}=\mathbf{0}$, yet the electron was still affected by the electromagnetic field! This is because, along the electron's path, although $\mathbf{E}=\mathbf{B}=\mathbf{0}$, the electromagnetic vector potential $\mathbf{A}\ne 0$.

This tells us that $\mathbf{A}$ is the fundamental entity, while $\mathbf{E}$ and $\mathbf{B}$ are merely derivatives.

Indeed, in the [previous article](https://zhuanlan.zhihu.com/p/23958176393), we mentioned that $A$, as a connection on a principal bundle, is primary. $\mathbf{E}$ and $\mathbf{B}$ (or the electromagnetic tensor $F = \mathrm{d}A$), as the curvature of the connection $A$, are secondary.

> Note that $\Delta \theta = \frac{e}{\hbar}\oint \mathbf{A} \cdot \mathrm{d}\mathbf{l}$ is gauge-invariant: setting $\mathbf{A} \rightarrow \mathbf{A} + \nabla\lambda$, we have $\oint \nabla \lambda\cdot \mathrm{d}\mathbf{l} = 0$. Clearly, only the AB phase along a closed path is gauge-invariant.

## III. Holonomy  

The phenomenon in which one travels around a loop on the base manifold of a fiber bundle and returns to the starting point, causing the value in the fiber to change, is called holonomy. For our $U(1)$ principal bundle, whose fiber is $U(1)$, it is an element of $U(1)$ ( $\mathrm{e}^{\mathrm{i}\theta}$ ) that changes.

This is just like a tangent vector that changes after traveling around a loop on a sphere and returning to its starting point, because a tangent vector is an element of the fiber (the tangent space) of the tangent bundle.

{{< figure src="image/holonomy.jpg" title="Holonomy on the tangent bundle" >}}
  

In physics, holonomy on a $U(1)$ fiber bundle has a special name: the geometric phase, or Berry phase. The corresponding connection is called the Berry connection, and the corresponding curvature is called the Berry curvature.

In the AB effect, the Berry connection $\mathcal{A}$ is nothing other than the electromagnetic 1-form $A$ (in fact, it must also be multiplied by the constant $e/\hbar$: $\mathcal{A} = \frac{e}{\hbar} A$), while the Berry curvature $F$ is the magnetic field $B$ (in fact, it must also be multiplied by the constant $e/\hbar$: $F = \frac{e}{\hbar} B$).

> More precisely, the Berry curvature should be the exterior derivative $F = \mathrm{d}A$ of $A$, and is a 2-form.  
>   
> Through the Hodge duality of three-dimensional Euclidean space, we can dualize a 2-form into a 1-form, namely the magnetic-field 1-form. Taking the exterior derivative of the 1-form $A$ and then taking the Hodge dual is equivalent to taking its curl: $\nabla \times A^\sharp = \star\mathrm{d}A$.  
>   
> The reason the magnetic field is called a pseudovector is also that the magnetic field is essentially a 2-form rather than a 1-form. What we commonly call the magnetic field is actually the Hodge dual of this 2-form.

The electromagnetic potential $\mathbf{A}$ is merely a connection on a particular $U(1)$ fiber bundle, whose base manifold is configuration space itself.

There are many other $U(1)$ fiber bundles whose base manifolds are not configuration space but abstract parameter spaces, such as momentum space. The analysis of the **quantum Hall effect** is carried out on a $U(1)$ fiber bundle in momentum space, where we can likewise derive the Berry connection and Berry curvature. These concepts have become central to modern condensed matter physics.

> The geometric phase on a $U(1)$ fiber bundle is called the Berry phase, while the geometric phase on a $SU(n)$ fiber bundle is called the non-Abelian geometric phase; both have applications in non-Hermitian systems, topological quantum computing, and so on.

## IV. Berry Connection/Curvature  

Next, let us derive the formula for the Berry connection.

Consider an abstract base manifold $M$. A point $s \in M$ on $M$ is a parameter of the Hamiltonian $H(s)$ rather than a spacetime point. Let an eigenstate of the Hamiltonian be denoted by $\psi$.

Starting from parallel transport:

$\begin{aligned} &D\_\mu\psi=0\\\\ &\Rightarrow\left(\partial\_\mu + \mathrm{i}A\_\mu\right) \psi =0 \\\\ &\Rightarrow  \partial\_\mu \psi = -\mathrm{i}A\_\mu \psi  \end{aligned}$

Taking the inner product of both sides of the above equation with $\psi$ gives:

$\langle\psi | \partial\_\mu \psi \rangle = -\mathrm{i} A\_\mu \langle\psi | \psi\rangle$

That is:

$\boxed{A\_\mu = \mathrm{i} \langle \psi | \partial\_\mu \psi\rangle}$

This is the expression for the Berry connection. It can also be written as:

$\boxed{\mathbf{A} = \mathrm{i} \langle \psi|\nabla \psi\rangle}$

The Berry curvature is the exterior derivative of the Berry connection:

$F = \mathrm{d}A$

In index notation, this becomes

$ \begin{aligned} F\_{\mu\nu} &= \partial\_\mu A\_\nu - \partial\_\nu A\_\mu \\\\ &= \mathrm{i} \left[\partial\_\mu \langle \psi | \partial\_\nu \psi\rangle   -\partial\_\nu \langle \psi | \partial\_\mu \psi\rangle \right] \\\\ &= \mathrm{i} [\langle \partial\_\mu \psi| \partial\_\nu \psi \rangle - \langle \partial\_\nu \psi| \partial\_\mu \psi \rangle] \end{aligned} $

namely,

$\boxed{F\_{\mu\nu}=\mathrm{i} [\langle \partial\_\mu \psi| \partial\_\nu \psi \rangle - \langle \partial\_\nu \psi| \partial\_\mu \psi \rangle]}$

The geometric phase is the integral of the connection 1-form $A$ along the closed curve $\gamma$:

$\boxed{ \Delta \theta = \int\_\gamma A }$

If there exists a surface $\Sigma$ such that the curve $\gamma$ is the boundary of $\Sigma$, then by Stokes' theorem,

$\begin{aligned} \Delta \theta  = \int\_{\partial \Sigma} A = \int\_{\Sigma} \mathrm{d}A = \int\_\Sigma F \end{aligned}$

where $\partial \Sigma$ denotes the boundary of $\Sigma$.

Therefore, the geometric phase can also be obtained by integrating the curvature 2-form $F$ over the surface $\Sigma$:

$\boxed{ \Delta \theta = \int\_\Sigma F}$

If we take $\Sigma$ to be a closed surface, then $\partial \Sigma=0$, and thus

$\Delta \theta = \int\_\Sigma F = \int\_{\partial \Sigma} A = 0$

However, on a topologically nontrivial manifold, this integral need not vanish. This is because a global connection $A$ cannot be defined in this case, so Stokes' theorem no longer applies. We will discuss the details in the next article.

> Note that the geometric phase $\Delta \theta$ is not an element of $U(1)$, but an element of the Lie algebra of $U(1)$. In other words, the geometric phase does not take values in $U(1) = \{ e^{\mathrm{i}\theta} \mid \theta \in [0,2\pi) \}$, but in $\mathbb{R}$. It represents the change in phase rather than the phase itself. That is, the geometric phase can take values such as $2\pi, 4\pi$, and these are not equivalent to $0$.

In a two-dimensional lattice, due to periodic boundary conditions, the electron momentum space $M$ is a torus, namely $M=T^2$. Integrating the Berry curvature $F$ over $T^2$ then yields the Chern number, which need not be zero:

$\int\_{M} F = 2 k\pi \quad (k\in\mathbb{Z})$

where $k$ is the Chern number, defined as $k = \frac{1}{2\pi}\int\_{M} F$.
