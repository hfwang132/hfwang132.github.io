---
title: "Electrodynamics from the Perspective of Differential Geometry [Higher and More Elegant Electrodynamics · 1]"
date: 2025-02-07T22:55:58+08:00
originalURL: "https://zhuanlan.zhihu.com/p/21808352165"
aliases:
  - "/en/gm_1/"
  - "/en/Post_20250406_微分几何视角下的电动力学-更高更妙的电动力学-1/"
draft: false
categories: ["Methods of Mathematical Physics"]
tags: ["Differential Geometry", "Electrodynamics"]
math: true
author: "Haifei"
---

### Preface  

You may have heard that Maxwell's equations have a very simple form:

$$\begin{aligned} \mathrm{d} F&=0 \\ \mathrm{d} \star F &= \mu_0 \star J \end{aligned}$$

Or alternatively,

$$\begin{aligned} \partial_\mu (\star{F})^{\mu \nu}&= 0 \\ \partial_\mu F^{\mu\nu}&= \mu_0 J^\nu  \end{aligned}$$

> Note: Strictly speaking, $\mathrm{d}F=0$ (or $\partial_\mu (\star{F})^{\mu \nu}= 0$) is not part of the dynamical equations of the electromagnetic field, but rather part of the field's own structure. This is because $\mathrm{d}F=0$ follows from the definition of the field strength $F=\mathrm{d}A$.

What exactly is going on here? Does this mean that there is in fact a higher and more profound perspective?

Yes, exactly. This article will derive Maxwell's equations starting from the principle of least action, using the language of differential geometry in the process.

Why use the language of differential geometry? First, it helps us see the mathematical structure of the electromagnetic field more clearly; second, it makes extending Maxwell's equations to curved spacetime very easy.

Before that, we need to make some mathematical preparations. Readers who are good at mathematics may skip this part.

## I. Preliminaries  
### 1.1 Field Theory and Variational Calculus  

The setting of field theory is four-dimensional spacetime equipped with the Minkowski metric, denoted by $M$.

Various physical fields (such as the electromagnetic field) are, mathematically, fields (such as vector fields) on the manifold $M$.

Given a field $\phi$ and a Lagrangian $\mathcal{L}[\phi, \partial_\mu \phi]$ on $M$, where $\partial_\mu \phi := \frac{\partial \phi}{\partial x^\mu}$.

The action is defined as $S[\phi] := \int \mathcal{L}[\phi, \partial_\mu \phi] \mathrm{d}^4x$. Varying $\phi, \partial_\mu \phi$:

$$\begin{aligned} \delta S[\phi] &= \int \delta\mathcal{L}[\phi, \partial_\mu \phi] \mathrm{d}^4x \\  &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} \delta \phi+\frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)}\delta(\partial_\mu \phi)\right]\mathrm{d}^4x \\ &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} \delta \phi+\frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)}\partial_\mu (\delta\phi)\right]\mathrm{d}^4x \\ &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} \delta \phi-\left(\partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)}\right)\delta\phi\right]\mathrm{d}^4x \\ &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} -\partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)}\right] (\delta\phi )\mathrm{d}^4x \end{aligned}$$

Here, the third equality uses $\delta \partial_\mu = \partial_\mu\delta$, and the fourth equality uses integration by parts. Note that the Einstein summation convention is used.

According to the principle of least action, set $\delta S=0$. By the arbitrariness of $\delta \phi$, we obtain

$$\begin{aligned} \frac{\partial \mathcal{L}}{\partial \phi} -\partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu \phi)} = 0 \end{aligned}$$

This is the Euler–Lagrange equation for field variations. It differs slightly from the Euler–Lagrange equation in classical mechanics, because in classical mechanics the object being varied is the one-dimensional trajectory of a particle, whereas here it is every possible configuration of a four-dimensional field.

### 1.2 Differential Geometry  

Since our spacetime is flat, we do not need much knowledge of differential geometry. It is sufficient to know the most basic notions of contravariant vectors (Contravariant), covariant vectors (Covariant), differential forms (Differential Forms), and the exterior derivative (Exterior Derivative).

**1.2.1 Contravariant Vectors**

Before encountering differential geometry, most of the time we use contravariant vector fields rather than covariant vector fields. This is because once we choose a basis, coordinate transformations are the inverse transformations of basis transformations. This is the meaning of “contravariant”: its transformation rule is opposite to that of the basis transformation.

For example, given a vector field $A^\mu = (A^x, A^y, A^z)$, namely $A = A^\mu e_\mu$, where $e_\mu$ is the basis we have chosen. Under the basis transformation $e^\prime_\nu = M^{\mu}_\nu e_{\mu}$, since $A^\mu e_\mu = A^{\prime \mu} e^\prime_\mu$, it is evident that the coordinate transformation should be the inverse transformation: $A^{\prime \mu} = (M^{-1})^{\mu}_{\nu} A^\nu$.

In fact, we may set $e_\mu = \partial_\mu = \frac{\partial}{\partial x^\mu}$. This may seem strange, but in differential geometry, contravariant vectors are defined as partial derivative operators! It is fine if this is not understood for now; it does not affect the subsequent derivation.

Note that the coordinates of contravariant vectors should be written with upper indices, for example $A^\mu$, so that they can be contracted with the lower index of the basis $e_\mu$ (according to the Einstein summation convention).

**1.2.2 Covariant Vectors**

Conversely, “covariant” means that the coordinate transformation and the basis transformation have the same matrix. But how can there be such vectors?

In fact, covariant vectors live in another space, called the dual space of the original space.

A vector $\omega_\mu$ (written with a lower index) in the dual space can be contracted with a vector $v^{\mu}$ (with an upper index) in the original space to form a scalar: $\omega_\mu v^\mu = C$.

The basis dual to $e_\mu = \partial_\mu$ is $\mathrm{d}x^\mu$, satisfying $\mathrm{d}x^\mu \partial_\nu = \delta^\mu_\nu = \begin{cases} 1 & \mu=\nu \\ 0 & \mu\ne \nu\end{cases}$. Using reasoning similar to before, we can conclude that the transformation matrix of the dual basis $\mathrm{d}x^\mu$ is the inverse of the transformation matrix of the basis $\partial_\mu$. Thus, the transformation matrix of the coordinates $\omega_\mu$ of a dual vector is the inverse of the inverse of the transformation matrix of the basis $v^\mu$, which is precisely the basis transformation matrix itself. This is the meaning of “covariant”: its transformation rule is the same as that of the basis transformation.

**1.2.3 Metric**

Covariant and contravariant vectors cannot be directly converted into one another unless we have a metric. A metric is a second-rank symmetric covariant tensor field $g_{\mu\nu} = g_{\nu\mu}$.

A metric is additional structure on a manifold. Not every manifold inherently has a metric. A manifold equipped with a metric is called a Riemannian manifold. If the metric is not positive definite, the manifold is called a pseudo-Riemannian manifold. The manifolds used in physics are pseudo-Riemannian manifolds because the Minkowski metric is not positive definite.

With the metric $g_{\mu\nu}$, we can convert a contravariant vector into a covariant vector $A_\mu = g_{\mu\nu} A^\nu$. We can also use $g^{\mu a}g_{a\mu}=\delta^\mu_\nu$ to define the contravariant metric $g^{\mu\nu}$, thereby converting a covariant vector into a contravariant vector $A^\mu = g^{\mu\nu} A_\nu$.

In special relativity, we use the Minkowski metric:

$$\begin{aligned} &g_{00} = \pm1\\ &g_{11} = g_{22}=g_{33}=\mp1\\ &g_{ij}=0\, (i\ne j) \end{aligned}$$

There are generally two conventions: $(+,-,-,-)$ and $(-,+,+,+)$. The former corresponds to $g_{00}=1$, and the latter corresponds to $g_{00}=-1$.

**1.2.4 Differential Forms**

Differential forms can be regarded as covariant antisymmetric tensor fields. Antisymmetry means that exchanging lower indices changes the sign: $\omega_{\mu \nu} = -\omega_{\nu\mu}$.

For example, a second-rank antisymmetric covariant tensor field $\omega_{\mu\nu}$ is a 2-form.

In particular, a covariant vector field $\omega_\mu$ is a 1-form, and a scalar field is a 0-form.

Two 1-forms can produce a 2-form through the wedge product:

$$\omega = \alpha \wedge \beta = \alpha_\mu \beta_\nu\mathrm{d}x^\mu \wedge  \mathrm{d}x^\nu $$

where $\mathrm{d}x^\mu \wedge  \mathrm{d}x^\nu  = -\mathrm{d}x^\nu \wedge  \mathrm{d}x^\mu$

And so on.

**1.2.5 Exterior Derivative**

Define the exterior derivative operation $\mathrm{d}$, which maps an n-form to an (n+1)-form:

$$\begin{aligned} \mathrm{d} \omega &= \mathrm{d}(\omega_\mu \mathrm{d}x^\mu)\ \\  &= \mathrm{d}(\omega_\mu) \wedge \mathrm{d}x^\mu\\ &=  (\partial_\nu \omega_\mu\mathrm{d}x^\nu)\wedge\mathrm{d}x^\mu  \end{aligned}$$

In a nutshell, the exterior derivative operation takes the total differential of the component in each basis and wedges it with the corresponding basis.

In particular, applying the exterior derivative to a 0-form is simply the total differential of the scalar field itself: $\mathrm{d}f = (\partial_\mu f) \mathrm{d}x^\mu$.

The exterior derivative is canonical: it requires no additional structure on the manifold and does not depend on the definition of a basis.

Lemma: $\alpha \wedge \beta = (-1)^{\deg(\alpha)\deg(\beta)} \beta\wedge \alpha$, where $\deg$ denotes the degree of the differential form.

> Proof: To move $\beta$ in front of $\alpha$, the $\deg(\beta)$ 1-forms in $\beta$ must each be moved forward $\deg(\alpha)$ times, for a total of $\deg(\alpha) \deg(\beta)$ moves, accumulating one minus sign each time.

Theorem: Applying the exterior derivative twice always yields zero: $\mathrm{d}\mathrm{d}=0$. The proof is omitted.

**1.2.6 Hodge Dual**

Interested readers may consult references on the Hodge dual themselves; it will not be introduced in detail here. Simply put, the Hodge dual of a k-form is the “complementary” (n-k)-form. For example, in Euclidean space $\mathbb{R}^3$, given an orthonormal basis $\mathrm{d}x,\mathrm{d}y,\mathrm{d}z$, we have

$$\begin{aligned} \star (1) &=\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z, \quad\star(\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z)= 1\\ \star \mathrm{d}x &= \mathrm{d}y \wedge \mathrm{d}z , \quad\star(\mathrm{d}y \wedge \mathrm{d}z) = \mathrm{d}x\\ \star\mathrm{d}y&=\mathrm{d}z\wedge \mathrm{d}x, \quad\star(\mathrm{d}z\wedge\mathrm{d}x) = \mathrm{d}y \\ \star \mathrm{d}z&=\mathrm{d}x\wedge \mathrm{d}y, \quad\star(\mathrm{d}x\wedge\mathrm{d}y)=\mathrm{d}z \end{aligned}$$

In this example, taking the Hodge dual twice returns the original form: $\star\star = \operatorname{id}$. In general, however, this is not always the case. For example, in Minkowski spacetime:

$$\star(\mathrm{d}t \wedge\mathrm{d}x) = -(\mathrm{d}y \wedge \mathrm{d}z),\quad \star(\mathrm{d}y \wedge \mathrm{d}z) = \mathrm{d}t \wedge\mathrm{d}x$$

$$\star\mathrm{d}t = -\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z, \quad \star(\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z) = -\mathrm{d}t$$

In fact, in Minkowski spacetime, for even-degree forms, $\star\star = -\operatorname{id}$. For odd-degree forms, $\star\star = \operatorname{id}$.

For the general case, see Lemma 3 in the appendix.

## II. 4-Potential, 4-Current, and Field-Strength Tensor  

The 4-potential (4-potential) is defined as $A^\mu = (A^0, A^1, A^2, A^3) = (\phi/c, A^x,A^y,A^z)$

> In more rigorous differential-geometric language, this is $A = A^0\partial_0 + A^1 \partial_1 + A^2 \partial_2 + A^3 \partial_3 = \frac{\phi}{c} \partial_{(ct)} + A^x\partial_x + A^y \partial_y + A^z\partial_z$  
> This is a tangent vector field, with basis $(\partial_0, \partial_1,\partial_2,\partial_3)$

Since only covariant vectors have a natural exterior derivative operation, we use the metric to convert the 4-potential into covariant form:

$$A_{\mu}=g_{\mu\nu}A^{\nu}$$

Hereafter, we adopt the metric convention $(-,+,+,+)$, so that:

$$A_\mu = (A_0, A_1, A_2, A_3) = (-\phi/c, A_x, A_y, A_z)$$

That is,

$$\begin{aligned} A &= A_0 \mathrm{d}x^0 + A_1\mathrm{d}x^1 + A_2\mathrm{d}x^2 + A_3\mathrm{d}x^3 \\&= -\phi/c \mathrm{d}(ct) +A^x\mathrm{d}x + A^y\mathrm{d}y + A^z\mathrm{d}z \\&=  -\phi \mathrm{d}t +A^x\mathrm{d}x +A^y\mathrm{d}y +A^z\mathrm{d}z  \end{aligned}$$

Applying the exterior derivative to the covariant 4-potential $A$ gives the field-strength tensor $F$:

$$\begin{aligned} F &= \mathrm{d}A \\ &= \mathrm{d} (-\phi \mathrm{d}t +A^x\mathrm{d}x +A^y\mathrm{d}y +A^z\mathrm{d}z) \\ &=(\partial_x \phi + \partial_t \mathrm A^x) \,\mathrm{d}t \wedge \mathrm{d}x \\ &+ (\partial_y \phi + \partial_t A^y) \,\mathrm{d}t\wedge \mathrm{d}y \\ &+ (\partial_z\phi + \partial_t A^z)\,\mathrm{d}t \wedge \mathrm{d}z \\ &+ (\partial_y A^z - \partial_z A^y) \mathrm{d}y \wedge \mathrm{d}z \\ & +(\partial_z A^x - \partial_x A^z)\mathrm{d}z \wedge \mathrm{d}x \\ & +(\partial_x A^y - \partial_y A^x)\mathrm{d}x \wedge \mathrm{d}y \\ &= -E^x \mathrm{d}t \wedge \mathrm{d}x - E^y \mathrm{d}t \wedge \mathrm{d}y - E^z \mathrm{d}t \wedge \mathrm{d}z \\ & + B^x \mathrm{d}y \wedge \mathrm{d}z + B^y \mathrm{d}z \wedge \mathrm{d}x + B^z \mathrm{d}x \wedge \mathrm{d}y \end{aligned}$$

It can also be written in matrix form:

$$\begin{bmatrix} 0 & E^x & E^y & E^z \\ -E^x & 0 & -B^z & B^y \\ -E^y & B^z & 0 & -B^x \\ -E^z & -B^y & B^x & 0 \end{bmatrix}$$

To maintain dimensional consistency, we absorb $c$ into $\mathrm{d}t$, and thus

$$\color{red}{F_{\mu\nu}=\begin{bmatrix} 0 & E^x/c & E^y/c & E^z /c\\ -E^x/c & 0 & -B_z & B^y \\ -E^y/c & B^z & 0 & -B^x \\ -E^z /c& -B^y & B^x & 0 \end{bmatrix}}$$

> Note that the first index $\mu$ here represents not the row, but the column; the second index $ \nu$ represents the row. If the other metric signature $(+,-,-,-)$ is chosen, then the first index $\mu$ represents the row.

In fact, $\color{red}{F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu}$. Readers may derive this themselves from the definition $F=\mathrm{d}A$.

The contravariant form of $F_{\mu\nu}$ is $F^{\mu\nu} = g^{\mu \rho} g^{\nu \sigma} F_{\rho \sigma}$:

$$F^{\mu\nu} = \begin{bmatrix} 0 & -E^x/c & -E^y/c & -E^z /c\\ E^x/c & 0 & -B_z & B^y \\ E^y/c & B^z & 0 & -B^x \\ E^z /c& -B^y & B^x & 0 \end{bmatrix}$$

Finally, the 4-current (4-current) is defined as $J^{\mu}=(\rho c, J^x,J^y,J^z)$, and its covariant form is $J_{\mu}=(-\rho c, J^x, J^y, J^z) = -\rho c^2 \mathrm{d}t +J^x \mathrm{d}x + J^y \mathrm{d}y + J^z \mathrm{d}z$.

> In fact, the 4-potential is a connection on a principal bundle. A principal bundle is a fiber bundle whose fiber has the structure of a Lie group, whereas the fibers of vector bundles (such as tangent/cotangent bundles) are vector spaces (such as tangent/cotangent spaces). Thus, principal bundles differ from vector bundles.  
>   
> The definition of a connection on a principal bundle also differs from that of a connection on a vector bundle. A connection on a vector bundle is defined as a covariant derivative, whereas a connection on a principal bundle is a Lie-algebra-valued 1-form. For the electromagnetic field, the fiber of the principal bundle is $U(1)$, and its Lie algebra is $\mathbb{R}$, so it appears no different from an ordinary 1-form. We will discuss the details in the next article of this series.

## III. Lagrangian of the Electromagnetic Field  

We directly state the Lagrangian here:

$$\color{red}{ \begin{aligned} \mathcal{L}[A_\mu, \partial_\nu A_\mu] =  -\frac{1}{4\mu_0} F_{\mu\nu} F^{\mu\nu} + A_{\mu} J^{\mu} \end{aligned} }$$

Note that if the other metric $(+,-,-,-)$ is chosen, the second term in the equation above should be negative.

Expanding it, one finds that it equals:

$$\color{red}{\mathcal{L} = \frac{1}{2}\left(\epsilon_0\mathbf{E^2} -\frac{1}{\mu_0} \mathbf{B^2}\right) -\rho\phi + \mathbf{A} \cdot \mathbf{J}}$$

As for why the Lagrangian takes this form, we will not investigate it further here.

## IV. Maxwell's Equations  

Using the field variation method introduced in the first section, we have:

$$\begin{aligned} \frac{\partial \mathcal{L}}{\partial A_\nu} -\partial_\mu \frac{\partial \mathcal{L}}{\partial(\partial_\mu A_\nu)} = 0 \end{aligned}$$

where

$$\begin{aligned} \frac{\partial \mathcal{L}}{\partial A_\mu} = -J_\mu \end{aligned}$$

$$\begin{aligned} \frac{\partial \mathcal{L}}{\partial(\partial_\mu A_\nu)} &= -\frac{\partial }{\partial(\partial_\mu A_\nu)} \left[\frac{1}{4\mu_0} F_{ab} F^{ab} \right]\\ &= -\frac{1}{4\mu_0}\left[\frac{\partial F_{ab}}{\partial(\partial_\mu A_\nu)} F^{ab} + F_{ab}\frac{\partial F^{ab}}{\partial(\partial_\mu A_\nu)} \right] \\ &= -\frac{1}{4\mu_0}\left[\frac{\partial F_{ab}}{\partial(\partial_\mu A_\nu)} F^{ab} + g_{ai}g_{bj}F^{ij}\frac{\partial (g^{ak}g^{bl}F_{kl})}{\partial(\partial_\mu A_\nu)} \right] \\ &= -\frac{1}{4\mu_0}\left[\frac{\partial F_{ab}}{\partial(\partial_\mu A_\nu)} F^{ab} + \delta_{ki}\delta_{lj}F^{ij}\frac{\partial F_{kl}}{\partial(\partial_\mu A_\nu)} \right] \\ &= -\frac{1}{4\mu_0}\left[\frac{\partial F_{ab}}{\partial(\partial_\mu A_\nu)} F^{ab} + F^{ij}\frac{\partial F_{ij}}{\partial(\partial_\mu A_\nu)} \right] \\ &= -\frac{1}{2\mu_0}\left[\frac{\partial F_{ab}}{\partial(\partial_\mu A_\nu)} F^{ab}  \right] \\ &= -\frac{1}{2\mu_0}\left[\frac{\partial(\partial_a A_b - \partial_b A_a)}{\partial(\partial_\mu A_\nu)} F^{ab}  \right] \\ &= -\frac{1}{2\mu_0}\left[(\delta^\mu_a\delta^\nu_b - \delta^\mu_b\delta^\nu_a  ) F^{ab}  \right]  \\  &= -\frac{1}{2\mu_0} \left( F^{\mu\nu}-F^{\nu\mu} \right) \\ &=-\frac{1}{\mu_0}F^{\mu\nu} \end{aligned}$$

Therefore,

$$\begin{aligned} \color{red}{\partial_\mu F^{\mu\nu} = \mu_0 J^{\nu}} \end{aligned}$$

These are Maxwell's equations.

Next, we rewrite them in the familiar form. Substituting

$$F^{\mu\nu} = \begin{bmatrix} 0 & -E^x/c & -E^y/c & -E^z /c\\ E^x/c & 0 & -B_z & B^y \\ E^y/c & B^z & 0 & -B^x \\ E^z /c& -B^y & B^x & 0 \end{bmatrix}$$

and

$$J^{\mu} = (\rho c^2, J^x,J^y,J^z)$$

into $\begin{aligned} \partial_\mu F^{\mu\nu} = \mu_0 J^{\nu} \end{aligned}$ gives:

$$\begin{aligned} \frac{\partial_i E^i}{c} = \mu_0 \rho c \\ \Rightarrow \color{red}{ \nabla \cdot \mathbf{E} =\frac{\rho}{\epsilon_0} }\end{aligned}$$

as well as

$$\begin{aligned} \varepsilon^{ij}_{k} \partial_{j}B^k - \frac{\partial}{\partial(ct)}E^i/c = \mu_0J^i\\  \color{red}{ \Rightarrow \nabla \times \mathbf{B} = \mu_0 (\mathbf{J}+ \epsilon_0 \partial_t \mathbf{E})} \end{aligned}$$

These are the sourced Maxwell equations.

But where have the other two source-free equations ($\color{red}{ \nabla \cdot\mathbf{B}=0}$ and $\color{red}{ \nabla \times \mathbf{E} = -\partial_t \mathbf{B}}$) gone?

In fact, these two source-free equations are not part of the dynamics of the electromagnetic field, but rather part of its own structure. This is because the source-free equations follow from $\mathrm{d}F=0$, while $\mathrm{d} F=0$ follows from $F = \mathrm{d} A$ (applying the exterior derivative twice to any differential form gives zero). And $F=\mathrm{d}A$ itself is the definition of the field-strength tensor. Thus, the source-free equations follow from the definition of the electromagnetic field and are part of its own structure.

The source-free equations can be written as:

$$\color{red}{\partial_\mu (\star F)^{\mu\nu} = 0}$$

where $(\star F)^{\mu\nu}$ is the Hodge dual of $F^{\mu\nu}$:

$$\color{red}{(\star F)^{\mu\nu} = \begin{bmatrix} 0 & -B^x & -B^y & -B^z \\ B^x & 0 & E^z/c & -E^y/c \\ B^y & -E^z/c & 0 & E^x/c \\ B^z & E^y/c & -E^x/c & 0 \end{bmatrix}}$$

Readers are invited to derive the source-free equations from $\mathrm{d} F=0$.

> If the reader knows differential geometry, the following provides a more elegant derivation:  
>  $\begin{aligned} &\mathrm{d}F=0 \\ &\Rightarrow \mathrm{d} \star \star F = 0 \\ &\Rightarrow \mathrm{d} \star \flat\sharp\star F = 0 \\ &\Rightarrow (\sharp\star\mathrm{d} \star \flat)(\sharp\star F) = 0 \\ &\Rightarrow (\nabla\cdot)(\sharp\star F) = 0 \\ &\Rightarrow \partial_\mu (\star F)^{\mu\nu} = 0 \end{aligned}$  
> where $\sharp$ raises indices, $\flat$ lowers indices, and $(\nabla\cdot)$ is the generalized divergence, defined as $(\nabla\cdot) = \sharp\star\mathrm{d} \star \flat$.

## V. Differential-Geometric Formulation  

Some readers dislike index notation and prefer more canonical abstract notation, so this section rewrites everything once more in the language of differential geometry.

Given the Lagrangian:

$$\begin{aligned} \mathcal{L} &= -\frac{1}{2\mu_0} F \wedge (\star F) + A\wedge (\star J) \\ &= \left[-\frac{1}{2\mu_0} \langle F , F\rangle + \langle A , J \rangle\right] \omega  \end{aligned}$$

Note that if the $(+,-,-,-)$ metric is adopted, the second term above should be $-\langle A, J\rangle \omega$.

The metric volume form $\omega$ is defined as the n-form such that $\langle \omega ,\omega \rangle_g = \pm 1 =: \operatorname{sgn}(g)$ holds, where n is the dimension of the manifold. Its explicit definition is $\omega = \sqrt{|\det(g)|}\,\mathrm{d}x^0 \wedge \mathrm{d}x^1 \wedge \mathrm{d}x^2 \wedge \mathrm{d}x^3 = \mathrm{d}x^0 \wedge \mathrm{d}x^1 \wedge \mathrm{d}x^2 \wedge \mathrm{d}x^3$.

> The Hodge dual $\star \beta$ of the differential form $\beta$ is defined by $\alpha \wedge *\beta = \langle \alpha, \beta\rangle \omega$. Here $\langle \cdot,\cdot\rangle$ is the inner product of differential forms. For n-forms, the inner product is defined by:  
>  $\langle \alpha_1,\cdots\wedge\alpha_n,\,\beta_1\wedge\cdots\wedge\beta_n\rangle = \begin{vmatrix} \langle \alpha_1,\beta_1 \rangle & \cdots & \langle \alpha_1,\beta_n \rangle \\ \vdots & \ddots & \vdots \\ \langle \alpha_n ,\beta_1 \rangle  & \cdots & \langle\alpha_n ,\beta_n \rangle  \end{vmatrix}$

Note that the coefficient here is $-1/(2\mu_0)$ rather than $-1/(4\mu_0)$. This is because the earlier tensor-index notation ($F_{\mu\nu}F^{\mu\nu}$) causes repeated summation when $\mu, \nu$ is exchanged, so previously one had to divide by an additional $1/2$.

It is evident from the form of $\mathcal{L}$ that it is actually a 4-form rather than a scalar field. This is because it must be integrated to form the action $\begin{aligned} S = \int \mathcal{L} \end{aligned}$.

Varying the action gives:

$$\begin{aligned} \delta S&\stackrel{1}{=}\int \delta \mathcal{L} \\ &\stackrel{2}=\int -\frac{1}{2\mu_0} [(\delta F) \wedge (\star F) +F\wedge(\delta\star F)] + (\delta A)\wedge (\star J) \\ &\color{blue}{\stackrel{3}{=}}\int -\frac{1}{2\mu_0} [(\delta F) \wedge (\star F)+(\star \delta F)\wedge F] + (\delta A)\wedge (\star J) \\ & \color{blue}{\stackrel{4}=} \int -\frac{1}{2\mu_0} [(\delta F) \wedge (\star F)+(\delta F)\wedge (\star F)] + (\delta A)\wedge (\star J) \\ &\stackrel{5}=\int -\frac{1}{\mu_0} (\delta F) \wedge (\star F) + (\delta A)\wedge (\star J) \\ &\stackrel{6}= \int -\frac{1}{\mu_0} (\delta \mathrm{d}A) \wedge (\star F) + (\delta A)\wedge (\star J) \\ &\stackrel{7}= \int -\frac{1}{\mu_0} \mathrm{d}(\delta A) \wedge (\star F) + (\delta A)\wedge (\star J) \\ &\color{blue}{\stackrel{8}=} \int -\frac{1}{\mu_0} (\delta A) \wedge (\mathrm{d}\star F) + (\delta A)\wedge (\star J) \\ &\stackrel{9}= \int  (\delta A) \wedge \left(-\frac{1}{\mu_0}\mathrm{d}\star F + \star J\right) \end{aligned}$$

The third equality uses:

$$\begin{aligned} \alpha\wedge\beta &= (-1)^{\deg(\alpha)\deg(\beta)}\end{aligned} \beta \wedge \alpha$$

where $\deg(\alpha)$ denotes the degree of $\alpha$. For example, here $\deg(F)=2$, because $F$ is a 2-form.

The fourth equality uses:

$$\begin{aligned} \star \alpha\wedge\beta &= (-1)^{\deg(\star\alpha)\deg(\beta)}\beta\wedge\star\alpha \\ &= (-1)^{\deg(\star\alpha)\deg(\beta)}\langle\beta,\alpha\rangle \omega \\ &= (-1)^{\deg(\star\alpha)\deg(\beta)}\langle\alpha,\beta\rangle \omega \\ &= (-1)^{\deg(\star\alpha)\deg(\beta)}\alpha \wedge\star\beta \end{aligned}$$

The eighth equality uses integration by parts:

$$\begin{aligned} \int (\mathrm{d}\alpha) \wedge \beta &= \int \left[\cancel{\mathrm{d}(\alpha \wedge \beta)} - (-1)^{\text{deg}(\alpha)} \alpha \wedge \mathrm{d}\beta\right]\end{aligned}$$

The reason $\int_M\mathrm{d}(\alpha \wedge \beta) = 0$ is that, according to Stokes' theorem, $\int_M\mathrm{d}(\alpha \wedge \beta)=\int_{\partial M} \alpha \wedge \beta$, where $\partial M$ is the boundary of $M$. Moreover, $\int_{\partial M} \alpha \wedge \beta =0$ (the boundary condition in the variational method is $\delta A|_{\partial M}=0$).

Since $\delta S =0$ holds for arbitrary $\delta A$, we obtain $-\frac{1}{\mu_0}\mathrm{d}\star F + \star J = 0$, namely Maxwell's equations:

$$\color{red}{\mathrm{d}\star F =\mu_0 \star J}$$

What is the advantage of writing it this way? The answer is that it is easily generalized to curved spacetime. To go from flat spacetime to curved spacetime, we need only replace the metric, which is reflected in the equation above by replacing the Hodge star operator, since the Hodge star operator is defined in terms of the metric.

## VI. Comparison of Covariant/Contravariant Forms  

Finally, let us compare index notation and differential-form notation:

(Contravariant) index notation:

$$\begin{aligned} \partial_\mu (\star{F})^{\mu \nu}&= 0 \\ \partial_\mu F^{\mu\nu}&= \mu_0 J^\nu  \end{aligned}$$

(Covariant) differential-form notation:

$$\begin{aligned} \mathrm{d} F&=0 \\ \mathrm{d} \star F &= \mu_0 \star J \end{aligned}$$

$F$ in index notation becomes the dual $(\star F)$ in differential-form notation, and vice versa. This is because $F^{\mu\nu}$ in index notation is a contravariant tensor, whereas the differential form $F$ is a covariant tensor. According to $(\nabla\cdot) \sharp = \sharp\star\mathrm{d} \star $, we have $\partial_\mu F^{\mu\nu} = \sharp\star \mathrm{d} \star F$. See the figure below:

$$\begin{matrix} k\text{-vector fields} & \stackrel{(\nabla\cdot)}{\longrightarrow}  & (k-1)\text{-vector fields}\\ \uparrow\sharp & & \uparrow\sharp \\  k\text{-form}  & & (k-1)\text{-form}\\ \downarrow\star &  & \uparrow \star \\ (n-k)\text{-form} &  \stackrel{\mathrm{d}}\longrightarrow  & (n-k+1)\text{-form} \end{matrix}$$

> Alternatively, one may use the more common co-differential $\mathrm{d}^\dagger$, defined by $\langle \alpha, \mathrm{d}\beta\rangle = \langle \mathrm{d}^\dagger\alpha, \beta\rangle$.  
>   
> It can be proved (see the appendix) that $\mathrm{d}^\dagger \alpha = (-1)^{k}\star^{-1} \mathrm{d} \star \alpha = (-1)^{nk+n+1} s\star \mathrm{d} \star \alpha$, where $k=\deg(\alpha)$ and $s=\operatorname{sgn}(g) := \operatorname{sgn}(\det (g))$ is the signature of the metric.  
>   
> For the Minkowski metric, $s = -1$. Substituting into $s=-1,\,n=4,\,k=2$ gives $\mathrm{d}^\dagger F=\star \mathrm{d}\star F$.  
>   
> Thus, the figure above can be drawn as:  
>  $\begin{matrix} 2\text{-vector fields} & \stackrel{(\nabla\cdot)}{\longrightarrow}  & 1\text{-vector fields}\\ \uparrow\sharp & & \uparrow\sharp \\  2\text{-form}  & \xrightarrow{\mathrm{d}^\dagger} & 1\text{-form}\\ \downarrow\star &  & \uparrow \star \\ 2\text{-form} &  \stackrel{\mathrm{d}}\longrightarrow  & 3\text{-form} \end{matrix}$

Therefore,

$$\begin{matrix} F^{\mu\nu} & \xrightarrow{(\nabla\cdot)} & \partial_\mu F^{\mu\nu}=\mu_0J^\nu \\ \uparrow \sharp & & \uparrow \sharp \\ F & \xrightarrow{\star \mathrm{d}\star} & \star \mathrm{d} \star F \end{matrix}$$

Thus $\partial_\mu F^{\mu\nu}=\mu_0J^\nu$ is equivalent to $\star \mathrm{d} \star F = \mu_0 J$.

For 1-forms, $\star\star = (-1)^{k(n-k)+s} \operatorname{id} = (-1)^{1(4-1)+1} \operatorname{id} = \operatorname{id}$. Therefore $\star \mathrm{d} \star F = \mu_0 J$ is equivalent to $\mathrm{d} \star F = \mu_0 \star J$.

The derivation for $\mathrm{d} F = 0  \Leftrightarrow \partial_\mu (\star F)^{\mu\nu} = 0$ is similar.

## VII. Appendix  

Lemma 1: $\mathrm{d}(\alpha \wedge \beta) = \mathrm{d}\alpha \wedge \beta + (-1)^{\deg(\alpha)} \alpha \wedge \mathrm{d}\beta$

> Proof:  
> Let  
>  $\begin{aligned} \alpha \wedge \beta &= \sum_{I,J} a_I b_J\mathrm{d} x^I \wedge \mathrm{d}x^J \\ &= \sum_{i_1,\cdots,i_{m},j_1,\cdots,j_n} a_{i_1,\cdots,i_{m}}b_{j_1,\cdots,j_n}\mathrm{d}x^{i_1} \wedge \cdots \wedge \mathrm{d}x^{i_m} \wedge \mathrm{d}x^j_1\wedge \cdots \wedge \mathrm{d}x^{j_n} \end{aligned}$  
> Then  
>  $\begin{aligned} \mathrm{d}(\alpha\wedge \beta) &= \partial_i (a_I b_J) \mathrm{d}x^i\wedge \mathrm{d}x^I \wedge \mathrm{d}x^J \\ &=[(\partial_i a_I)b_J \mathrm{d}x^i \wedge \mathrm{d}x^I] \wedge \mathrm{d}x^J + a_I\partial_i b_J \mathrm{d}x^i \wedge \mathrm{d}x^I \wedge \mathrm{d}x^J \\ &=(\partial_i a_I\mathrm{d}x^i \wedge \mathrm{d}x^I) \wedge (b_J \mathrm{d}x^J) + (-1)^{\deg(\alpha)} (a_I\partial_i  \mathrm{d}x^I \wedge \mathrm{d}x^i) \wedge (b_J\mathrm{d}x^J) \\ &=\mathrm{d}\alpha \wedge \beta + (-1)^{\deg(\alpha)} \alpha \wedge \mathrm{d}\beta \end{aligned}$

Lemma 2: When $\deg(\alpha)=\deg(\beta)$, we have $\star\alpha \wedge \beta = (-1)^{k(n-k)}\alpha\wedge \star\beta$, where $k=\deg(\alpha)$

> Proof:  
>  $\begin{aligned} \star \alpha\wedge\beta &= (-1)^{\deg(\star\alpha)\deg(\beta)} \beta\wedge\star\alpha \\  &= (-1)^{k(n-k)}\langle\beta,\alpha\rangle \omega \\  &= (-1)^{k(n-k)}\langle\alpha,\beta\rangle \omega \\  &= (-1)^{k(n-k)}\alpha \wedge\star\beta \end{aligned}$

Lemma 3: $\star\star \alpha = (-1)^{k(n-k)}s \alpha$, where $k=\deg(\alpha)$ and $s=\operatorname{sgn}(g)$.

> Proof:  
>  $\begin{aligned} \star\alpha \wedge \star\star \alpha &= \langle \star\alpha, \star\alpha \rangle\omega \\ &= s\langle \alpha,\alpha \rangle\omega \\ &= s\alpha \wedge \star \alpha\\ &= (-1)^{k(n-k)}s \star\alpha\wedge \alpha \\ &= \star\alpha\wedge \left[(-1)^{k(n-k)}s  \alpha\right] \end{aligned}$

Lemma 4: $\mathrm{d}^\dagger \alpha = (-1)^{k}\star^{-1} \mathrm{d} \star \alpha$

> Proof:  
>  $\begin{aligned} \langle \beta,\mathrm{d}^\dagger \alpha\rangle&= \langle \mathrm{d}\beta , \alpha\rangle \\ &= \int\mathrm{d}\beta \wedge \star \alpha \\ &= \int -(-1)^{\deg(\beta)} \beta \wedge \mathrm{d}\star \alpha \\ &= \int (-1)^{\deg(\beta)+1} \beta \wedge \mathrm{d}\star \alpha \\ &= \int (-1)^{\deg(\alpha)} \beta \wedge \mathrm{d}\star \alpha \\ &= \int (-1)^{\deg(\alpha)} \beta \wedge \star (\star^{-1}\mathrm{d}\star \alpha) \\ &= (-1)^{k} \langle\beta, \star^{-1}\mathrm{d} \star \alpha \rangle \end{aligned}$

Lemma 5: $\mathrm{d}^\dagger \alpha  = (-1)^{nk+n+1} s\star \mathrm{d} \star \alpha$

> Proof:  
> This follows immediately by combining Lemma 3 and Lemma 4.

Next article in this series:

[Electrodynamics from the Perspective of Gauge Field Theory [Higher and More Elegant Electrodynamics · 2]](https://zhuanlan.zhihu.com/p/23958176393)
