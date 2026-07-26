---
title: "Dirac Magnetic Monopoles—Chern Classes and Chern Numbers [Higher and More Elegant Electrodynamics · 4]"
date: 2025-03-30T01:13:18+08:00
originalURL: "https://zhuanlan.zhihu.com/p/1889370433708609679"
aliases:
  - "/en/gm_4/"
  - "/en/Post_20250406_狄拉克磁单极子-陈类与陈数-更高更妙的电动力学-4/"
draft: false
categories: ["mathematical physics methods"]
tags: ["differential geometry", "topology", "Chern numbers", "electrodynamics"]
---

In the [previous article](https://zhuanlan.zhihu.com/p/32173040413), we mentioned that if a manifold is topologically trivial, then integrating the Berry curvature over a closed surface $\Sigma$ should yield zero. This is because, according to Stokes' theorem:

$\int\_\Sigma F = \int\_{\partial \Sigma } A = 0$

However, on a topologically nontrivial manifold, the integral $\int\_\Sigma F$ is not necessarily zero. This is because a globally single-valued connection $A$ cannot be defined in this case, so Stokes' theorem no longer applies. What does this mean?

## I. Cohomology and Chern Classes  

We know that exact forms are all closed forms. This is because $\mathrm{d}\mathrm{d}=0$ .

> An exact form is a form that is the (exterior) derivative of another form: $\exists \alpha, \  \omega = \mathrm{d}\alpha$ .  
> A closed form is a form whose (exterior) derivative is zero: $\mathrm{d}\omega =0$ .

But conversely, are all closed forms exact forms? For topologically trivial manifolds, such as $\mathbb{R}^n$ , this is indeed the case. But for general manifolds, not all closed forms are exact forms. Let us give an example below:

> **Example**  
>   
> Imagine the lateral surface of an infinitely long cylinder ($\mathbb{R}^1 \times S^1$), with a uniform electric field $E= c\ \mathrm{d}\theta$ circling around it, where $c$ is a constant. Such an electric field $E$ is curl-free ( $\mathrm{d}E=0$ ), meaning that this electric field is a closed form.  
>   
> However, $E$ is not a conservative field: if an electron travels once around in the direction of the electric field and returns to its original position, its energy decreases.  
>   
> Evidently, we cannot define a globally single-valued electric potential in this case; that is, we cannot find a $\phi$ such that $E = \mathrm{d} \phi$ . In other words, $E$ is not an exact form.

In physics, we usually assume that if a form is closed, then it is also exact. This is because in most cases, the manifolds we study have no “holes.” Such manifolds may be called topologically trivial.

However, this does not hold on manifolds with “holes.” In this case, closed forms are not necessarily exact forms.

Cohomology is the study of “non-exact closed forms.” Specifically, it studies how many classes these “non-exact closed forms” can be divided into. These equivalence classes form a group, called a cohomology group.

A **Chern class** is an element of a cohomology group, namely an equivalence class of “non-exact closed forms.”

Returning to the initial question, we said that a global connection does not necessarily exist. This is because although the curvature 2-form is closed, it is not necessarily exact. Therefore, there need not exist a global connection 1-form whose exterior derivative is the curvature 2-form. The topological equivalence class of such a curvature 2-form is a Chern class. Chern numbers are used to label different equivalence classes.

> **Optional reading**  
>   
> Specifically, the nth-order (de Rham) cohomology group on a manifold $M$ is defined as all nth-order closed forms on $M$ modulo all nth-order exact forms (see [this article](https://zhuanlan.zhihu.com/p/629852598)):  
>   
>  $\boxed{H\_{\text{dR}}^n(M) = \frac{\{\omega\mid\mathrm{d}\omega = 0\}}{\{\omega\mid \exists\alpha,\mathrm{d}\alpha = \omega\}}} ​ $   
>   
> Here $\omega$ is an n-form.  
>   
> In addition to de Rham cohomology, there are other cohomology theories. Singular cohomology uses concepts such as simplices and chains from singular homology to define cohomology groups:  
>   
>  $\boxed{ H^n(M;\mathbb{F}) = \frac{\{c\mid\delta c = 0\}}{\{c\mid \exists a,\delta a = c\}} } $   
>   
> Here $c$ is an nth-order co-chain, and $\delta$ is the co-boundary operator. They are defined with the help of chains and the boundary operator in homology (see [this article](https://zhuanlan.zhihu.com/p/629852598)). In addition, $\mathbb{F}$ denotes the coefficient ring of co-chains, which may be $\mathbb{Z}$ or $\mathbb{R}$ .  
>   
> The de Rham cohomology group $H\_{\text{dR}}^n(M) $ is isomorphic to the singular cohomology group $H^n(M;\mathbb{R})$ . The (first) Chern class is essentially an element of the second-order singular cohomology group $H^2(M;\mathbb{Z})$ .

## II. Local Connections and Winding Number  

Returning to the initial question. We said that on a topologically nontrivial manifold, the integral $\int\_\Sigma F$ is not necessarily zero. This is because a globally single-valued connection $A$ cannot be defined in this case. However, although the connection $A$ cannot be defined globally, it can still be defined locally—we can patch it together.

Specifically, we define a connection $A\_1$ on the upper half-surface $\Sigma\_1$, and a connection $A\_2$ on the lower half-surface $\Sigma\_2$. These two half-surfaces intersect at the equator in the middle. In the overlap region $U=\Sigma\_1 \cup \Sigma\_2 \simeq S^1$, we require $A\_1$ and $A\_2$ to differ only by a gauge transformation: $A\_2  = A\_1 + \mathrm{d}\lambda$ .

The overlap region $U$ is a “circle” ( $\simeq S^1$ ), and $e^{i\lambda} \in U(1)$ is also a “circle,” which leads to an important concept: the winding number. Specifically, after going once around $U$ and returning to the origin, $\Delta \lambda = \oint\_{U} \mathrm{d}\lambda $ need not be zero; differing by an integer multiple of $2\pi$ is also acceptable, namely:

$\oint\_{U} \mathrm{d}\lambda = \oint\_{U} \nabla \lambda \cdot \mathrm{d}\mathbf{l} = 2k\pi \quad(k\in\mathbb{Z})$

> This can be seen from the gauge transformation of the wave function $\psi \mapsto e^{i\lambda} \psi$: after making one circuit and returning to the origin, it is only necessary that $\Delta \lambda = 2k\pi$.

The $k$ here is the **winding number**. It represents how many times the gauge transformation at the junction between the two local connections “winds.”

Why need $\Delta \lambda$ not be zero? Because $A\_1$ and $A\_2$ are not parts of a global connection $A$, but two entirely distinct local connections. We merely “glue” them together, and the glue is the gauge transformation. The $\lambda$ of this gauge transformation need not satisfy the single-valuedness condition $\oint\_{U} \mathrm{d}\lambda  = 0$ .

## III. Chern Number  

Returning to the initial question: on a topologically nontrivial manifold, the integral $\int\_\Sigma F$ of the Berry curvature $F$ over a closed surface $\Sigma$ is not necessarily zero. This appears to violate Stokes' theorem, so what is actually happening?

In fact, this does not violate Stokes' theorem. It is simply that we cannot apply it over the entirety of $\Sigma$; instead, we must apply it separately on the “patches” $\Sigma\_1$ and $\Sigma\_2$.

In other words, although the global connection $A$ does not exist, the local connections $A\_1$ and $A\_2$ on $\Sigma\_1$ and $\Sigma\_2$ still exist, so we can apply Stokes' theorem separately on $\Sigma\_1$ and $\Sigma\_2$:

$\begin{aligned} \int\_{\Sigma\_1} F &=  \int\_{\partial \Sigma\_1} A\_1 = \int\_{U} A\_1 \\\\ \int\_{\Sigma\_2} F &=  \int\_{\partial \Sigma\_2} A\_2 = \int\_{U} A\_2 \end{aligned}$

Thus:

$\begin{aligned} \int\_{\Sigma} F &=  \int\_{\partial \Sigma\_1} A\_1 - \int\_{\partial \Sigma\_2} A\_2\\\\ &= \int\_{U} (A\_1-A\_2)  \\\\ &= \int\_{U} \nabla \lambda \cdot \mathrm{d}l  \\\\ &=2k\pi \quad (k\in\mathbb{Z}) \end{aligned}$

Clearly, $\int\_\Sigma F$ need not be zero precisely because the winding number $k$ can be nonzero.

We therefore define the **Chern number** as

$\boxed{ C = \frac{1}{2\pi} \int\_\Sigma F }$

> Clearly, on $\Sigma \simeq S^2$, the Chern number equals the winding number.  
>   
> Of course, this is only the case for $\Sigma \simeq S^2$. In condensed matter physics, the more common case is the “torus” $\Sigma \simeq T^2$. In this case, we can wind in both the x and y directions. It can be shown that the Chern number in this case is the difference between the winding numbers in the two directions.  
>   
> The Chern number defined here is obtained by integrating over a two-dimensional closed surface. In fact, integrating over a 2n-dimensional closed surface yields the nth Chern number, whereas what we discuss here is only the first Chern number.

Different curvature 2-forms may yield the same Chern number when integrated over a closed surface, so curvature 2-forms can be classified according to their Chern numbers. These equivalence classes are called Chern classes.

## IV. Dirac Magnetic Monopoles  

Next, let us apply what we have learned above to a concrete example: the Dirac magnetic monopole.

Let us now assume that there exists a kind of particle that, just as a point charge emits electric field lines, can emit magnetic field lines. We call this kind of particle a “magnetic monopole.”

$\nabla \cdot \mathbf{B} = g \delta^3(\mathbf{r})$

Here $g$ denotes the magnitude of the “magnetic charge.” The magnetic field outside the magnetic monopole is then:

$\begin{aligned} \mathbf{B} = \frac{g}{4\pi} \frac{\hat{r}}{r^2} \end{aligned}$

Consider a sphere of radius $r$ centered on the magnetic monopole. We define two local connections on the upper and lower hemispheres, respectively:

$\begin{aligned} \mathbf{A}\_1 &= \frac{g}{4\pi}\frac{1-\cos \theta}{\sin \theta} \hat{\phi} \\\\ \mathbf{A}\_2 &= -\frac{g}{4\pi}\frac{1+\cos \theta}{\sin \theta} \hat{\phi} \end{aligned}$

It can be verified that on these two hemispheres, $\nabla \times \mathbf{A}\_1 = \mathbf{B}$ and $\nabla \times \mathbf{A}\_2 = \mathbf{B}$ hold.

On the equator, $\mathbf{A}\_1$ and $\mathbf{A}\_2$ can differ only by a gauge transformation: $\frac{q}{\hbar}(\mathbf{A}\_1 -\mathbf{A}\_2) = \nabla \lambda$ . Thus $\lambda = \frac{q}{\hbar}\frac{g}{2\pi r} \phi$, and

$\begin{aligned} \oint \nabla \lambda \cdot \mathrm{d} \mathbf{l} &= \oint  \frac{q}{\hbar}\frac{g}{2\pi r} \cdot r \mathrm{d} \phi\\\\ &= \frac{qg}{\hbar} \end{aligned}$

Setting $\oint \nabla \lambda \cdot \mathrm{d} \mathbf{l}  = 2k\pi \ \  (k\in\mathbb{Z})$ gives:

$\boxed{\frac{qg}{2\pi \hbar} = k \in \mathbb{Z} }$

This is the Dirac quantization condition. It tells us that if magnetic monopoles exist, then magnetic charge must be quantized.

In this example, the Berry connection is the vector potential, the Berry curvature is the magnetic field, and the Chern number $qg/2\pi \hbar \in \mathbb{Z}$ is proportional to the magnetic charge $g$ . The magnetic charge $g$ is one type of what we commonly call **topological charge**.

Of course, magnetic monopoles have not yet been observed. This means that the magnetic field, as a Berry curvature, is topologically trivial: a global Berry connection, namely a vector potential, can always be found such that the magnetic field is its exterior derivative. In other words, the Chern number of the magnetic field is always zero.
