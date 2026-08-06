---
title: "Dirac Magnetic Monopoles—Chern Classes and Chern Numbers [Higher and More Wonderful Electrodynamics · 4]"
date: 2025-03-30T01:13:18+08:00
originalURL: "https://zhuanlan.zhihu.com/p/1889370433708609679"
aliases:
  - "/en/gm_4/"
  - "/en/Post_20250406_狄拉克磁单极子-陈类与陈数-更高更妙的电动力学-4/"
draft: false
categories: ["mathematical physics methods"]
tags: ["differential geometry", "topology", "Chern numbers", "electrodynamics"]
math: true
author: "Haifei"
---

Previous article in this series:

[Godfly: The electromagnetic field is more than just electric and magnetic fields—The AB effect and Berry connection [Higher and More Wonderful Electrodynamics · 3]](https://zhuanlan.zhihu.com/p/32173040413)

---

In the [previous article](https://zhuanlan.zhihu.com/p/32173040413), we mentioned that if a manifold is topologically trivial, then integrating the Berry curvature over a closed surface \(\Sigma\) should yield zero. This is because, according to Stokes' theorem:

\[\int_\Sigma F = \int_{\partial \Sigma } A = 0\]

However, on a topologically nontrivial manifold, the integral \(\int_\Sigma F\) need not be zero. This is because a globally single-valued connection \(A\) cannot be defined in this case, so Stokes' theorem no longer applies. What does this mean?

## I. Cohomology and Chern Classes  

We know that exact forms are all closed forms. This is because \(\mathrm{d}\mathrm{d}=0\) .

> An exact form is a form that is the (exterior) derivative of another form: \(\exists \alpha, \, \omega = \mathrm{d}\alpha\) .  
> A closed form is a form whose (exterior) derivative is zero: \(\mathrm{d}\omega =0\) .

But conversely, are all closed forms exact forms? For topologically trivial manifolds, such as \(\mathbb{R}^n\) , this is indeed true. But for general manifolds, not all closed forms are exact forms. Let us give an example below:

> **Example**  
>   
> Imagine the lateral surface of an infinitely long cylinder (\(\mathbb{R}^1 \times S^1\)), with a uniform electric field \(E= c\,\mathrm{d}\theta\) circulating once around it, where \(c\) is a constant. Such an electric field \(E\) is curl-free ( \(\mathrm{d}E=0\) ); that is, this electric field is a closed form.  
>   
> However, \(E\) is not a conservative field: if an electron travels once around in the direction of the electric field and returns to its original position, its energy decreases.  
>   
> Evidently, we cannot define a globally single-valued electric potential in this case; that is, we cannot find an \(\phi\) such that \(E = \mathrm{d} \phi\) . In other words, \(E\) is not an exact form.

In physics, we usually assume by default that if a form is closed, then it is also exact. This is because in most cases, the manifolds we study have no “holes.” Such manifolds may be called topologically trivial.

However, this does not hold on manifolds with “holes.” In this case, closed forms need not be exact forms.

Cohomology is the study of “non-exact closed forms.” More specifically, it studies how many classes “non-exact closed forms” can be divided into. These equivalence classes form a group called a cohomology group.

A **Chern class** is an element of a cohomology group, namely an equivalence class of “non-exact closed forms.”

Returning to the initial question, we said that a global connection does not necessarily exist. This is because although the curvature 2-form is a closed form, it need not be an exact form. Therefore, a global connection 1-form whose exterior derivative is the curvature 2-form need not exist. The topological equivalence class of such curvature 2-forms is a Chern class. Chern numbers are used to label different equivalence classes.

> **Optional reading**  
>   
> Specifically, the nth-order (de Rham) cohomology group of a manifold \(M\) is defined as all nth-order closed forms on \(M\) modulo all nth-order exact forms (see [this article](https://zhuanlan.zhihu.com/p/629852598)):  
>   
>  \(\boxed{H_{\text{dR}}^n(M) = \frac{\{\omega\mid\mathrm{d}\omega = 0\}}{\{\omega\mid \exists\alpha,\mathrm{d}\alpha = \omega\}}} ​ \)   
>   
> where \(\omega\) is an n-form.  
>   
> In addition to de Rham cohomology, there are other cohomology theories. Singular cohomology uses concepts such as simplices and chains from singular homology to define cohomology groups:  
>   
>  \(\boxed{ H^n(M;\mathbb{F}) = \frac{\{c\mid\delta c = 0\}}{\{c\mid \exists a,\delta a = c\}} } \)   
>   
> where \(c\) is an nth-order co-chain, and \(\delta\) is the co-boundary operator. They are defined using the chain and boundary operators in homology (see [this article](https://zhuanlan.zhihu.com/p/629852598)). In addition, \(\mathbb{F}\) denotes the coefficient ring of the co-chain, which may be \(\mathbb{Z}\) or \(\mathbb{R}\) .  
>   
> The de Rham cohomology group \(H_{\text{dR}}^n(M) \) is isomorphic to the singular cohomology group \(H^n(M;\mathbb{R})\) . The (first) Chern class is essentially an element of the second singular cohomology group \(H^2(M;\mathbb{Z})\) .

## II. Local Connections and Winding Number  

Let us return to the initial question. We said that on a topologically nontrivial manifold, the integral \(\int_\Sigma F\) need not be zero. This is because a globally single-valued connection \(A\) cannot be defined in this case. However, although the connection \(A\) cannot be globally defined, it can still be defined locally—we can patch it together.

Specifically, we define a connection \(A_1\) on the upper half-surface \(\Sigma_1\) and a connection \(A_2\) on the lower half-surface \(\Sigma_2\). These two half-surfaces intersect at the equator in the middle. In the overlap region \(U=\Sigma_1 \cup \Sigma_2 \simeq S^1\), we require \(A_1\) and \(A_2\) to differ only by a gauge transformation: \(A_2  = A_1 + \mathrm{d}\lambda\) .

The overlap region \(U\) is a “circle” ( \(\simeq S^1\) ), and \(e^{i\lambda} \in U(1)\) is also a “circle,” which leads to an important concept: the winding number. Specifically, after going once around \(U\) and returning to the origin, \(\Delta \lambda = \oint_{U} \mathrm{d}\lambda \) need not be zero; differing by an integer multiple of \(2\pi\) is also acceptable, namely:

\[\oint_{U} \mathrm{d}\lambda = \oint_{U} \nabla \lambda \cdot \mathrm{d}\mathbf{l} = 2k\pi \quad(k\in\mathbb{Z})\]

> From the gauge transformation of the wavefunction \(\psi \mapsto e^{i\lambda} \psi\), we can see that after making one circuit and returning to the origin, it is only necessary that \(\Delta \lambda = 2k\pi\).

The \(k\) here is the **winding number**. It represents how many times the gauge transformation at the junction between the two local connections “winds.”

Why need \(\Delta \lambda\) not be zero? Because \(A_1\) and \(A_2\) are not parts of a global connection \(A\), but two entirely different local connections. We merely “glue” them together, and the glue is the gauge transformation. The \(\lambda\) of this gauge transformation need not satisfy the single-valuedness condition \(\oint_{U} \mathrm{d}\lambda  = 0\) .

## III. Chern Number  

Returning to the initial question: on a topologically nontrivial manifold, the integral \(\int_\Sigma F\) of the Berry curvature \(F\) over the closed surface \(\Sigma\) need not be zero. This appears to violate Stokes' theorem, so what is actually happening?

In fact, this does not violate Stokes' theorem. It is simply that we cannot apply it over the entire \(\Sigma\); instead, we must apply it separately on the “patches” \(\Sigma_1\) and \(\Sigma_2\).

In other words, although the global connection \(A\) does not exist, the local connections \(A_1\) and \(A_2\) on \(\Sigma_1\) and \(\Sigma_2\) still exist, so we can apply Stokes' theorem separately on \(\Sigma_1\) and \(\Sigma_2\):

\[\begin{aligned} \int_{\Sigma_1} F &=  \int_{\partial \Sigma_1} A_1 = \int_{U} A_1 \\ \int_{\Sigma_2} F &=  \int_{\partial \Sigma_2} A_2 = \int_{U} A_2 \end{aligned}\]

Thus:

\[\begin{aligned} \int_{\Sigma} F &=  \int_{\partial \Sigma_1} A_1 - \int_{\partial \Sigma_2} A_2\\ &= \int_{U} (A_1-A_2)  \\ &= \int_{U} \nabla \lambda \cdot \mathrm{d}l  \\ &=2k\pi \quad (k\in\mathbb{Z}) \end{aligned}\]

Clearly, \(\int_\Sigma F\) need not be zero precisely because the winding number \(k\) can be nonzero.

We therefore define the **Chern number** as

\[\boxed{ C = \frac{1}{2\pi} \int_\Sigma F }\]

> Clearly, on \(\Sigma \simeq S^2\), the Chern number equals the winding number.  
>   
> Of course, this is only the case for \(\Sigma \simeq S^2\). In condensed matter physics, the more common case is the “doughnut” \(\Sigma \simeq T^2\) . In this case, we can wind in both the x and y directions. It can be proved that the Chern number in this case is the difference between the winding numbers in the two directions.  
>   
> The Chern number defined here is obtained by integration over a two-dimensional closed surface. In fact, integration over a 2n-dimensional closed surface yields the nth Chern number, while what we discuss here is only the first Chern number.  
>   
> In the non-Abelian case, we can calculate the nth Chern numbers, which are defined as:  
>   
>  \(\boxed{ C_n = \frac{1}{n!(2\pi)^n}  \int \operatorname{tr}[\underbrace{F\wedge \cdots \wedge F}_{\text{n } F}] = \frac{1}{n!(2\pi)^n}  \int \operatorname{tr}[F^{\wedge n}] }\)   
>   
> In the Abelian case, \(C_{n\gt 1} =0\) , because \(F \wedge F=0\) .

Different curvature 2-forms may yield the same Chern number when integrated over a closed surface, so we can classify curvature 2-forms according to their Chern numbers. These equivalence classes are called Chern classes.

## IV. Dirac Monopole  

Next, let us apply what we have learned above to a specific example: the Dirac magnetic monopole.

We now assume that there exists a kind of particle that can emit magnetic field lines just as a point charge emits electric field lines. We call this kind of particle a “magnetic monopole.”

\[\nabla \cdot \mathbf{B} = g \delta^3(\mathbf{r})\]

Here \(g\) represents the magnitude of the “magnetic charge.” The magnetic field outside the magnetic monopole is then:

\[\begin{aligned} \mathbf{B} = \frac{g}{4\pi} \frac{\hat{r}}{r^2} \end{aligned}\]

Consider a sphere of radius \(r\) centered on the magnetic monopole. We define two local connections on the upper and lower hemispheres, respectively:

\[\begin{aligned} \mathbf{A}_1 &= \frac{g}{4\pi}\frac{1-\cos \theta}{\sin \theta} \hat{\phi} \\ \mathbf{A}_2 &= -\frac{g}{4\pi}\frac{1+\cos \theta}{\sin \theta} \hat{\phi} \end{aligned}\]

It can be verified that \(\nabla \times \mathbf{A}_1 = \mathbf{B}\) and \(\nabla \times \mathbf{A}_2 = \mathbf{B}\) hold on these two hemispheres.

At the equator, \(\mathbf{A}_1\) and \(\mathbf{A}_2\) can differ only by a gauge transformation: \(\frac{q}{\hbar}(\mathbf{A}_1 -\mathbf{A}_2) = \nabla \lambda\) . Thus \(\lambda = \frac{q}{\hbar}\frac{g}{2\pi r} \phi\), and

\[\begin{aligned} \oint \nabla \lambda \cdot \mathrm{d} \mathbf{l} &= \oint  \frac{q}{\hbar}\frac{g}{2\pi r} \cdot r \mathrm{d} \phi\\ &= \frac{qg}{\hbar} \end{aligned}\]

Setting \(\oint \nabla \lambda \cdot \mathrm{d} \mathbf{l}  = 2k\pi \,\, (k\in\mathbb{Z})\) gives:

\[\boxed{\frac{qg}{2\pi \hbar} = k \in \mathbb{Z} }\]

This is the Dirac quantization condition. It tells us that if magnetic monopoles exist, then magnetic charge must be quantized.

In this example, the Berry connection is the vector potential, the Berry curvature is the magnetic field, and the Chern number \(qg/2\pi \hbar \in \mathbb{Z}\) is proportional to the magnetic charge \(g\) . The magnetic charge \(g\) is one kind of what we commonly call **topological charge**.

Of course, no one has discovered a magnetic monopole to this day. This means that the magnetic field as a Berry curvature is topologically trivial: a global Berry connection, namely a vector potential, can always be found such that the magnetic field is its exterior derivative. In other words, the Chern number of the magnetic field is always zero.

## V. Spin in a Magnetic Field  

In the previous section, we saw that the case in which configuration space is taken as the base manifold is topologically trivial. This is too boring, so let us give a topologically nontrivial example below.

Now consider a spin in a magnetic field, with Hamiltonian:

\[H = - \mu\ \mathbf{B}\cdot \bm\sigma\]

Here \(\bm\sigma = (\sigma_x, \sigma_y,\sigma_z)\) is the vector composed of the three Pauli operators. The energies of the two levels of this spin are \(\pm \mu B \) .

Now keep the magnitude of the magnetic field fixed while changing its direction. In other words, we let all possible directions of the magnetic field \(\mathbf{B}\) form the base manifold of the fiber bundle. This manifold is the two-dimensional sphere \(S^2\) .

When the direction of the magnetic field is \((\theta,\varphi)\) in spherical coordinates, the ground state is \(|\psi\rangle= (\cos \frac{\theta}{2} , \sin \frac{\theta}{2} \mathrm{e}^\mathrm{i\varphi})^T\)

The Berry connection is then:

\[\begin{aligned} A_\theta &= \mathrm{i} \langle \psi | \partial_\theta \psi\rangle \\ &= \mathrm{i}\left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2}\mathrm{e}^\mathrm{-i\varphi} \right) \partial_\theta \left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2} \mathrm{e}^\mathrm{i\varphi}\right)^T \\ &= \mathrm{i}\left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2}\mathrm{e}^\mathrm{-i\varphi} \right) \left(-\sin \frac{\theta}{2} , \cos\frac{\theta}{2}\mathrm{e}^\mathrm{i\varphi} \right)^T \\ &= 0 \end{aligned}\]

\[\begin{aligned} A_\theta &= \mathrm{i} \langle \psi | \partial_\varphi \psi\rangle \\ &= \mathrm{i}\left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2}\mathrm{e}^\mathrm{-i\varphi} \right) \partial_\varphi\left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2} \mathrm{e}^\mathrm{i\varphi}\right)^T \\ &= \mathrm{i}\left(\cos \frac{\theta}{2} , \sin \frac{\theta}{2}\mathrm{e}^\mathrm{-i\varphi} \right) \left(0 , \mathrm{i}\sin\frac{\theta}{2}\mathrm{e}^\mathrm{i\varphi} \right)^T \\ &= -\sin^2 \frac{\theta}{2} \\ &= -\frac{1-\cos\theta}{2} \end{aligned}\]

Similarly, for the excited state, we have

\[\begin{aligned} A_\theta &= 0,\\ A_\varphi&= -\cos^2\frac{\theta}{2} = -\frac{1+\cos\theta}{2} \end{aligned}\]

That is, the \(A_\theta\) of both eigenstates are zero, while their \(A_\varphi\) are respectively \(\frac{\pm \cos\theta - 1}{2}\), where \(+\) corresponds to the ground state and \(-\) corresponds to the excited state.

The Berry curvature is then

\[\Omega_{\theta \varphi} = \partial_\theta A_\varphi - \partial_\varphi A_\theta = \mp \frac{1}{2} \sin \theta\]

and the Chern number is

\[\begin{aligned} C&=\frac{1}{2\pi}\int_{S^2} \Omega_{\theta \varphi} \mathrm{d}\theta\wedge \mathrm{d}\varphi \\ &=\frac{1}{4\pi}\int_{S^2}  \mp  \sin \theta \ \mathrm{d}\theta\wedge \mathrm{d}\varphi \\ &= \mp 1 \end{aligned}\]

Clearly, for spin 1/2, the Chern number of its ground state is \(-1\), while that of its excited state is \(+1\) .

For general spin \(j\), it can be proved that the Chern number of an eigenstate with magnetic quantum number \(m\) is \(C_m = -2m\) .

> **Optional reading**  
>   
> Spins in a magnetic field can also involve **non-Abelian geometric phases**.  
>   
> Consider the magnetic quadrupole Hamiltonian \(H= \mu(\mathbf{B} \cdot \mathbf{J})^2\) [[1]](#ref\_1), where \(\mathbf{J} = (J_x,J_y,J_z)\) is the angular momentum operator for spin 3/2.  
>   
> Clearly, the energy levels of the eigenstates \(m=\pm\frac{1}{2}\) and \(m=\pm\frac{3}{2}\) are each degenerate.  
>   
> If the direction of the magnetic field \(\mathbf{B}\) is slowly varied, there is a **non-Abelian geometric phase** in the eigenspace of \(m=\pm\frac{1}{2}\). However, the eigenspace of \(m=\pm\frac{3}{2}\) does not have one, because of the selection rule \(\Delta m = 0, \pm1\) .  
>   
> For this example, one can calculate the non-Abelian connection and curvature [[1]](#ref\_1), and then calculate the first Chern number. The calculation shows that the first Chern number is zero. But this does not mean that this example is topologically trivial. It has a nontrivial topological invariant: the Stiefel–Whitney class, which will not be introduced here.

---

Next article in this series:

[Electrodynamics from the Perspective of Hamiltonian Mechanics [Higher and More Wonderful Electrodynamics · 5]](https://zhuanlan.zhihu.com/p/32052863470)## References  

1. ^[a](#ref\_1\_0)[b](#ref\_1\_1)A. Zee, Phys. Rev. A 38, 1 (1988).
