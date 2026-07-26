---
title: "Why Does Phase Space Sometimes Look Like a Complex Plane?"
date: 2024-07-01T23:09:03+08:00
originalURL: "https://zhuanlan.zhihu.com/p/706487869"
aliases:
  - "/en/phase_space_complex/"
  - "/en/Post_20240727_相空间为什么有时看起来像一个复平面/"
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

Students who have studied physics all know about phase space, which consists of generalized coordinates $q$ and generalized momenta $p$.


> Example 1: The angle of a simple pendulum constitutes a configuration space $S\_1$ . The angle and angular momentum constitute a phase space $S\_1 \times \mathbb{R}$ .  
>   
> Example 2: Given the Hamiltonian and boundary conditions of a classical electromagnetic field, the electric field strength in a certain mode constitutes a configuration space, while the cosine and sine components of the electric field strength in that mode constitute a phase space.

  
In fact, given a configuration space $M$ , phase space is the **cotangent bundle** $M$ over $T^\*M$ .

However, when solving problems, we physicists often also use the **complex plane**.


> Example 1: Given the Hamilton equations of a harmonic oscillator  
> $\begin{cases} \frac{\mathrm{d}q}{\mathrm{d}t} = \omega p\\\\ \frac{\mathrm{d}p}{\mathrm{d}t} = -\omega q \end{cases}$   
> namely  
> $\frac{\mathrm{d}}{\mathrm{d}t} \begin{bmatrix} q \\\\ p \end{bmatrix} = \begin{bmatrix} 0 & \omega \\\\ -\omega & 0 \end{bmatrix} \begin{bmatrix} q\\\\ p \end{bmatrix}$   
> diagonalization yields the eigenvector $a^{\pm} =  q\pm\mathrm{i}p$ , and thus the derivative of $a^{\pm}$ depends only on itself:  
> $\frac{\mathrm{d}a^{\pm}}{\mathrm{d}t}=\mp\mathrm{i}\omega a^{\pm},\quad a^{\pm}=a\_0^{\pm} \exp (\mp\mathrm{i}\omega t)$   
> Although there are no complex numbers in classical mechanics, it is very natural for complex numbers to appear here as eigenvalues. Quantizing this method gives the creation and annihilation operators.  
>   
> Example 2: A phasor diagram describing a single-mode classical electromagnetic field is defined on the complex plane. Of course, it can also describe quantities such as current and voltage.  
>   
> Example 3: The Wigner function describing a single-mode quantum electromagnetic field is defined on the complex plane.
  
All of these suggest: could a cotangent bundle be a complex plane? After discussing this with students from the mathematics department, the answer is indeed yes, but **provided that the cotangent bundle itself is a vector space**. The argument is as follows:

**(1)** Phase space is the cotangent bundle of configuration space.

**(2)** Every cotangent bundle comes equipped with a canonical symplectic structure.


> In other words, the tangent space at every point of a cotangent bundle comes equipped with a canonical symplectic form.

**(3)** If the cotangent bundle itself also happens to be a vector space, then its tangent space is naturally isomorphic to itself. Therefore, according to (2), this cotangent bundle is also a symplectic vector space.

**(4)** A symplectic vector space $g$ with inner product $(V,\omega)$ comes equipped with a canonical complex structure $J$ [1].


> The complex structure $V$ on $J$ is defined as $J \in \operatorname{End}(V) \quad\text{s.t.} \quad J^2 = -\operatorname{id}$ .

From **(1-4)**, we know that if a phase space happens to be a vector space, then that phase space comes equipped with a complex structure.

Therefore, $T^\*\mathbb{R} = \mathbb{R} \times \mathbb{R}^\*$ and $\mathbb{C}$ have the same mathematical structure. $T^\*(\mathbb{R}^n) = \mathbb{R}^n \times (\mathbb{R}^{n})^\*$ and $\mathbb{C}^n$ have the same mathematical structure. This is why we can use the complex plane in place of phase space.

However, note that not all phase spaces can be regarded as complex planes. Only when the configuration space itself is a vector space is the phase space a vector space, and thus can be regarded as a complex plane. For example, the phase space of a simple pendulum is not a vector space and cannot be regarded as a complex plane.



---

Update: The above (1-4) are somewhat abstract. Here is a concrete construction below.

Consider the configuration space $\mathbb{R}$ and phase space $T^\*(\mathbb{R}) = \mathbb{R} \times \mathbb{R}^\*$ , with global coordinates $(p,q)$.

The canonical symplectic form on $T^\*(\mathbb{R})$ is $\omega= \mathrm{d} p \wedge \mathrm{d} q$ , which is independent of the basis. Its matrix form is $M(\omega)=\begin{pmatrix} 0 & 1\\\\ -1 & 0 \end{pmatrix}$ .

The canonical Euclidean inner product on $T^\*(\mathbb{R})$ is $g = \mathrm{d}q^2 + \mathrm{d}p^2$ , whose matrix form is $M(g)=\begin{pmatrix} 1 & 0\\\\ 0 & 1 \end{pmatrix}$ .

We can use $g(u,v)=\omega(u,Jv)$ to define the complex structure $J\in \text{End}[T^\*(\mathbb{R})]$ . Clearly, its matrix form satisfies $M(g)=M(\omega)M(J)$ , so $M(J)=\begin{pmatrix} 0 & -1\\\\ 1 & 0 \end{pmatrix}$ . Does this matrix look familiar? That is right: it is a two-dimensional matrix representation of the imaginary unit $\mathrm{i}$ .

## References  
1. [https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/resources/lect07/](https://ocw.mit.edu/courses/18-966-geometry-of-manifolds-spring-2007/resources/lect07/)
