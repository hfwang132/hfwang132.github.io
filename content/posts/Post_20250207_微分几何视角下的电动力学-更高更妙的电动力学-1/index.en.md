---
title: "Electrodynamics from the Perspective of Differential Geometry [Higher and More Elegant Electrodynamics · 1]"
date: 2025-02-07T22:55:58+08:00
originalURL: "https://zhuanlan.zhihu.com/p/21808352165"
aliases:
  - "/en/gm_1/"
  - "/en/Post_20250406_微分几何视角下的电动力学-更高更妙的电动力学-1/"
draft: false
categories: ["Mathematical Physics Methods"]
tags: ["Differential Geometry", "Electrodynamics"]
---

### Preface  

You may have heard that Maxwell's equations take a very simple form:

$\begin{aligned} \mathrm{d} F&=0 \\\\ \mathrm{d} \star F &= \mu\_0 \star J \end{aligned}$

Or alternatively:

$\begin{aligned} \partial\_\mu (\star{F})^{\mu \nu}&= 0 \\\\ \partial\_\mu F^{\mu\nu}&= \mu\_0 J^\nu  \end{aligned}$

> Note: Strictly speaking, $\mathrm{d}F=0$ (or $\partial\_\mu (\star{F})^{\mu \nu}= 0$) is not a dynamical equation of the electromagnetic field, but rather part of the intrinsic structure of the electromagnetic field itself. This is because $\mathrm{d}F=0$ follows from the definition of the field strength $F=\mathrm{d}A$.

What exactly is going on here? Does this mean that there is in fact a higher and more profound perspective?

Yes, precisely. This article derives Maxwell's equations starting from the principle of least action, using the language of differential geometry throughout.

Why use the language of differential geometry? First, it helps us see the mathematical structure of the electromagnetic field more clearly; second, it makes extending Maxwell's equations to curved spacetime very easy.

Before that, we need to make some mathematical preparations. Readers with a strong mathematical background may skip this part.

## I. Preparations  
### 1.1 Field Theory and Variational Calculus  

The setting of field theory is four-dimensional spacetime equipped with the Minkowski metric, denoted by $M$.

Various physical fields (such as electromagnetic fields) are mathematically fields (such as vector fields) on the manifold $M$.

Given a field $\phi$ and a Lagrangian $\mathcal{L}[\phi, \partial\_\mu \phi]$ on $M$, where $\partial\_\mu \phi := \frac{\partial \phi}{\partial x^\mu}$.

The action is defined as $S[\phi] := \int \mathcal{L}[\phi, \partial\_\mu \phi] \mathrm{d}^4x$. Varying $\phi, \partial\_\mu \phi$:

$\begin{aligned} \delta S[\phi] &= \int \delta\mathcal{L}[\phi, \partial\_\mu \phi] \mathrm{d}^4x \\\\  &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} \delta \phi+\frac{\partial \mathcal{L}}{\partial(\partial\_\mu \phi)}\delta(\partial\_\mu \phi)\right]\mathrm{d}^4x \\\\ &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} \delta \phi+\frac{\partial \mathcal{L}}{\partial(\partial\_\mu \phi)}\partial\_\mu (\delta\phi)\right]\mathrm{d}^4x \\\\ &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} \delta \phi-\left(\partial\_\mu \frac{\partial \mathcal{L}}{\partial(\partial\_\mu \phi)}\right)\delta\phi\right]\mathrm{d}^4x \\\\ &= \int \left[\frac{\partial \mathcal{L}}{\partial \phi} -\partial\_\mu \frac{\partial \mathcal{L}}{\partial(\partial\_\mu \phi)}\right] (\delta\phi )\mathrm{d}^4x \end{aligned}$

Here, the third equality uses $\delta \partial\_\mu = \partial\_\mu\delta$, and the fourth equality uses integration by parts. Note that Einstein summation convention is used.

According to the principle of least action, setting $\delta S=0$, and using the arbitrariness of $\delta \phi$, we obtain

$\begin{aligned} \frac{\partial \mathcal{L}}{\partial \phi} -\partial\_\mu \frac{\partial \mathcal{L}}{\partial(\partial\_\mu \phi)} = 0 \end{aligned}$

This is the Euler–Lagrange equation for field variations. It differs slightly from the Euler–Lagrange equation in classical mechanics, because in classical mechanics the object being varied is a particle's one-dimensional trajectory, whereas here the object being varied is every possible configuration of a four-dimensional field.

### 1.2 Differential Geometry  

Since our spacetime is flat, we do not need much knowledge of differential geometry. It is enough to know the most basic notions of contravariance (Contravariant), covariance (Covariant), differential forms (Differential Forms), and the exterior derivative (Exterior Derivative).

**1.2.1 Contravariant Vectors**

Before encountering differential geometry, most of the time we use contravariant vector fields rather than covariant vector fields. This is because once we choose a basis, a coordinate transformation is the inverse transformation of the basis transformation. This is what “contravariant” means: its transformation rule is opposite to that of the basis transformation.

For example, given a vector field $A^\mu = (A^x, A^y, A^z)$, namely $A = A^\mu e\_\mu$, where $e\_\mu$ is the basis we have chosen. When performing the basis transformation $e^\prime\_\nu = M^{\mu}\_\nu e\_{\mu}$, since $A^\mu e\_\mu = A^{\prime \mu} e^\prime\_\mu$, clearly the coordinate transformation should be the inverse transformation: $A^{\prime \mu} = (M^{-1})^{\mu}\_{\nu} A^\nu$.

In fact, we may set $e\_\mu = \partial\_\mu = \frac{\partial}{\partial x^\mu}$. This may seem strange, but in differential geometry, contravariant vectors are defined to be partial derivative operators! It is fine if this is not understood for the moment; it does not affect the subsequent derivation.

Note that the coordinates of contravariant vectors should be written with superscripts, such as $A^\mu$, so that they can contract with the subscripts of the basis $e\_\mu$ (according to Einstein summation convention).

**1.2.2 Covariant Vectors**

Conversely, “covariant” means that the coordinate transformation and the basis transformation have the same matrix. But how can such vectors exist?

In fact, covariant vectors live in another space, called the dual space of the original space.

A vector $\omega\_\mu$ (written with subscripts) in the dual space can contract with a vector $v^{\mu}$ (written with superscripts) in the original space to form a scalar: $\omega\_\mu v^\mu = C$.

The basis dual to $e\_\mu = \partial\_\mu$ is $\mathrm{d}x^\mu$, satisfying $\mathrm{d}x^\mu \partial\_\nu = \delta^\mu\_\nu = \begin{cases} 1 & \mu=\nu \\\\ 0 & \mu\ne \nu\end{cases}$. Using reasoning similar to that above, we can conclude that the transformation matrix of the dual basis $\mathrm{d}x^\mu$ is the inverse of the transformation matrix of the basis $\partial\_\mu$. Thus, the transformation matrix of the coordinates $\omega\_\mu$ of a dual vector is the inverse of the inverse of the transformation matrix of the basis $v^\mu$, which is exactly the basis transformation matrix itself. This is what “covariant” means: its transformation rule is the same as that of the basis transformation.

**1.2.3 Metric**

Covariant and contravariant vectors cannot be converted directly into one another unless we have a metric. A metric is a symmetric covariant tensor field of rank two $g\_{\mu\nu} = g\_{\nu\mu}$.

A metric is additional structure on a manifold. Not all manifolds naturally possess a metric. A manifold equipped with a metric is called a Riemannian manifold. If the metric is not positive definite, then the manifold is called a pseudo-Riemannian manifold. The manifolds used in physics are pseudo-Riemannian manifolds, because the Minkowski metric is not positive definite.

With the metric $g\_{\mu\nu}$, we can convert a contravariant vector into a covariant vector $A\_\mu = g\_{\mu\nu} A^\nu$. We can also use $g^{\mu a}g\_{a\mu}=\delta^\mu\_\nu$ to define the contravariant metric $g^{\mu\nu}$, thereby converting a covariant vector into a contravariant vector $A^\mu = g^{\mu\nu} A\_\nu$.

In special relativity, we use the Minkowski metric:

$\begin{aligned} &g\_{00} = \pm1\\\\ &g\_{11} = g\_{22}=g\_{33}=\mp1\\\\ &g\_{ij}=0\, (i\ne j) \end{aligned}$

There are generally two conventions: $(+,-,-,-)$ and $(-,+,+,+)$. The former corresponds to $g\_{00}=1$, and the latter to $g\_{00}=-1$.

**1.2.4 Differential Forms**

Differential forms may be regarded as covariant antisymmetric tensor fields. Antisymmetry means that exchanging subscripts changes the sign: $\omega\_{\mu \nu} = -\omega\_{\nu\mu}$.

For example, an antisymmetric covariant tensor field of rank two $\omega\_{\mu\nu}$ is a 2-form.

In particular, a covariant vector field $\omega\_\mu$ is a 1-form, and a scalar field is a 0-form.

Two 1-forms can produce a 2-form through the wedge product:

$\omega = \alpha \wedge \beta = \alpha\_\mu \beta\_\nu\mathrm{d}x^\mu \wedge  \mathrm{d}x^\nu $

where $\mathrm{d}x^\mu \wedge  \mathrm{d}x^\nu  = -\mathrm{d}x^\nu \wedge  \mathrm{d}x^\mu$

And so on.

**1.2.5 Exterior Derivative**

Define the exterior derivative operation $\mathrm{d}$, which maps an n-form to an (n+1)-form:

$\begin{aligned} \mathrm{d} \omega &= \mathrm{d}(\omega\_\mu \mathrm{d}x^\mu)\ \\\\  &= \mathrm{d}(\omega\_\mu) \wedge \mathrm{d}x^\mu\\\\ &=  (\partial\_\nu \omega\_\mu\mathrm{d}x^\nu)\wedge\mathrm{d}x^\mu  \end{aligned}$

In a nutshell, the exterior derivative takes the total differential of the component with respect to each basis element and then wedges it with the corresponding basis element.

In particular, applying the exterior derivative to a 0-form is simply the total differential of the scalar field itself: $\mathrm{d}f = (\partial\_\mu f) \mathrm{d}x^\mu$.

The exterior derivative is canonical: it requires no additional structure on the manifold and does not depend on the definition of the basis.

Lemma: $\alpha \wedge \beta = (-1)^{\deg(\alpha)\deg(\beta)} \beta\wedge \alpha$, where $\deg$ denotes the degree of the differential form.

> Proof: To move $\beta$ in front of $\alpha$, the $\deg(\beta)$ 1-forms in $\beta$ must each be moved forward $\deg(\alpha)$ times, for a total of $\deg(\alpha) \deg(\beta)$ moves, accumulating one minus sign each time.

Theorem: Applying the exterior derivative twice always gives zero: $\mathrm{d}\mathrm{d}=0$. The proof is omitted.

**1.2.6 Hodge Dual**

Interested readers may consult other sources on the Hodge dual; it will not be introduced in detail here. Simply put, the Hodge dual of a k-form is its “complementary” (n-k)-form. For example, in Euclidean space $\mathbb{R}^3$, given the standard orthonormal basis $\mathrm{d}x,\mathrm{d}y,\mathrm{d}z$, we have

$\begin{aligned} \star (1) &=\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z, \quad\star(\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z)= 1\\\\ \star \mathrm{d}x &= \mathrm{d}y \wedge \mathrm{d}z , \quad\star(\mathrm{d}y \wedge \mathrm{d}z) = \mathrm{d}x\\\\ \star\mathrm{d}y&=\mathrm{d}z\wedge \mathrm{d}x, \quad\star(\mathrm{d}z\wedge\mathrm{d}x) = \mathrm{d}y \\\\ \star \mathrm{d}z&=\mathrm{d}x\wedge \mathrm{d}y, \quad\star(\mathrm{d}x\wedge\mathrm{d}y)=\mathrm{d}z \end{aligned}$

In this example, applying the Hodge dual twice returns the original form: $\star\star = \operatorname{id}$. In general, however, this is not always the case. For example, in Minkowski spacetime:

$\star(\mathrm{d}t \wedge\mathrm{d}x) = -(\mathrm{d}y \wedge \mathrm{d}z),\quad \star(\mathrm{d}y \wedge \mathrm{d}z) = \mathrm{d}t \wedge\mathrm{d}x$

$\star\mathrm{d}t = -\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z, \quad \star(\mathrm{d}x\wedge\mathrm{d}y \wedge\mathrm{d}z) = -\mathrm{d}t$

In fact, in Minkowski spacetime, for even-degree forms, $\star\star = -\operatorname{id}$. For odd-degree forms, $\star\star = \operatorname{id}$.

For the general case, see Lemma 3 in the appendix.

## II. 4-Potential, 4-Current, and Field Strength Tensor  

The 4-potential (4-potential) is defined as $A^\mu = (A^0, A^1, A^2, A^3) = (\phi/c, A^x,A^y,A^z)$

> In more rigorous differential-geometric language, this is $A = A^0\partial\_0 + A^1 \partial\_1 + A^2 \partial\_2 + A^3 \partial\_3 = \frac{\phi}{c} \partial\_{(ct)} + A^x\partial\_x + A^y \partial\_y + A^z\partial\_z$  
> This is a tangent vector field, with basis $(\partial\_0, \partial\_1,\partial\_2,\partial\_3)$

Since only covariant vectors have a natural exterior derivative operation, we use the metric to convert the 4-potential into covariant form:

$A\_{\mu}=g\_{\mu\nu}A^{\nu}$

Below, we adopt the metric convention $(-,+,+,+)$. Thus:

$A\_\mu = (A\_0, A\_1, A\_2, A\_3) = (-\phi/c, A\_x, A\_y, A\_z)$

That is,

$\begin{aligned} A &= A\_0 \mathrm{d}x^0 + A\_1\mathrm{d}x^1 + A\_2\mathrm{d}x^2 + A\_3\mathrm{d}x^3 \\\\&= -\phi/c \mathrm{d}(ct) +A^x\mathrm{d}x + A^y\mathrm{d}y + A^z\mathrm{d}z \\\\&=  -\phi \mathrm{d}t +A^x\mathrm{d}x +A^y\mathrm{d}y +A^z\mathrm{d}z  \end{aligned}$

Applying the exterior derivative to the covariant 4-potential $A$ gives the field strength tensor $F$:

$\begin{aligned} F &= \mathrm{d}A \\\\ &= \mathrm{d} (-\phi \mathrm{d}t +A^x\mathrm{d}x +A^y\mathrm{d}y +A^z\mathrm{d}z) \\\\ &=(\partial\_x \phi + \partial\_t \mathrm A^x) \,\mathrm{d}t \wedge \mathrm{d}x \\\\ &+ (\partial\_y \phi + \partial\_t A^y) \,\mathrm{d}t\wedge \mathrm{d}y \\\\ &+ (\partial\_z\phi + \partial\_t A^z)\,\mathrm{d}t \wedge \mathrm{d}z \\\\ &+ (\partial\_y A^z - \partial\_z A^y) \mathrm{d}y \wedge \mathrm{d}z \\\\ & +(\partial\_z A^x - \partial\_x A^z)\mathrm{d}z \wedge \mathrm{d}x \\\\ & +(\partial\_x A^y - \partial\_y A^x)\mathrm{d}x \wedge \mathrm{d}y \\\\ &= -E^x \mathrm{d}t \wedge \mathrm{d}x - E^y \mathrm{d}t \wedge \mathrm{d}y - E^z \mathrm{d}t \wedge \mathrm{d}z \\\\ & + B^x \mathrm{d}y \wedge \mathrm{d}z + B^y \mathrm{d}z \wedge \mathrm{d}x + B^z \mathrm{d}x \wedge \mathrm{d}y \end{aligned}$

It can also be written in matrix form:

$\begin{bmatrix} 0 & E^x & E^y & E^z \\\\ -E^x & 0 & -B^z & B^y \\\\ -E^y & B^z & 0 & -B^x \\\\ -E^z & -B^y & B^x & 0 \end{bmatrix}$

To maintain dimensional consistency, we absorb $c$ into $\mathrm{d}t$, giving

$\color{red}{F\_{\mu\nu}=\begin{bmatrix} 0 & E^x/c & E^y/c & E^z /c\\\\ -E^x/c & 0 & -B\_z & B^y \\\\ -E^y/c & B^z & 0 & -B^x \\\\ -E^z /c& -B^y & B^x & 0 \end{bmatrix}}$

Note that the first index $\mu$ here denotes not the row but the column, while the second index $ \nu$ denotes the row.

In fact, $\color{red}{F\_{\mu\nu} = \partial\_\mu A\_\nu - \partial\_\nu A\_\mu}$; readers may derive this themselves from the definition $F=\mathrm{d}A$.

The contravariant form of $F\_{\mu\nu}$ is $F^{\mu\nu} = g^{\mu \rho} g^{\nu \sigma} F\_{\rho \sigma}$:

$F^{\mu\nu} = \begin{bmatrix} 0 & -E^x/c & -E^y/c & -E^z /c\\\\ E^x/c & 0 & -B\_z & B^y \\\\ E^y/c & B^z & 0 & -B^x \\\\ E^z /c& -B^y & B^x & 0 \end{bmatrix}$

Finally, the 4-current (4-current) is defined as $J^{\mu}=(\rho c, J^x,J^y,J^z)$, and its covariant form is $J\_{\mu}=(-\rho c, J^x, J^y, J^z) = -\rho c^2 \mathrm{d}t +J^x \mathrm{d}x + J^y \mathrm{d}y + J^z \mathrm{d}z$.

> In fact, the 4-potential is a connection on a principal bundle. A principal bundle is a fiber bundle whose fibers have the structure of a Lie group, whereas the fibers of vector bundles (such as tangent/cotangent bundles) are vector spaces (such as tangent/cotangent spaces). Thus, principal bundles differ from vector bundles.  
>   
> The definition of a connection on a principal bundle also differs from that of a connection on a vector bundle. A connection on a vector bundle is defined as a covariant derivative, whereas a connection on a principal bundle is a Lie-algebra-valued 1-form. For the electromagnetic field, the fiber of the principal bundle is $U(1)$, and its Lie algebra is $\mathbb{R}$, so it appears no different from an ordinary 1-form. We will discuss the details in the next article in this series.

## III. Lagrangian of the Electromagnetic Field  

We directly give the Lagrangian here:

$\color{red}{ \begin{aligned} \mathcal{L}[A\_\mu, \partial\_\nu A\_\mu] =  -\frac{1}{4\mu\_0} F\_{\mu\nu} F^{\mu\nu} + A\_{\mu} J^{\mu} \end{aligned} }$

Note that if the other metric $(+,-,-,-)$ is chosen, the second term in the expression above should be negative.

If expanded, it is found to equal:

$\color{red}{\mathcal{L} = \frac{1}{2}\left(\epsilon\_0\mathbf{E^2} -\frac{1}{\mu\_0} \mathbf{B^2}\right) -\rho\phi + \mathbf{A} \cdot \mathbf{J}}$

As for why the Lagrangian has this form, we will not investigate it further here.

## IV. Maxwell's Equations  

Using the field variation method introduced in the first section, we have:

$\begin{aligned} \frac{\partial \mathcal{L}}{\partial A\_\nu} -\partial\_\mu \frac{\partial \mathcal{L}}{\partial(\partial\_\mu A\_\nu)} = 0 \end{aligned}$

where

$\begin{aligned} \frac{\partial \mathcal{L}}{\partial A\_\mu} = -J\_\mu \end{aligned}$

$\begin{aligned} \frac{\partial \mathcal{L}}{\partial(\partial\_\mu A\_\nu)} &= -\frac{\partial }{\partial(\partial\_\mu A\_\nu)} \left[\frac{1}{4\mu\_0} F\_{ab} F^{ab} \right]\\\\ &= -\frac{1}{4\mu\_0}\left[\frac{\partial F\_{ab}}{\partial(\partial\_\mu A\_\nu)} F^{ab} + F\_{ab}\frac{\partial F^{ab}}{\partial(\partial\_\mu A\_\nu)} \right] \\\\ &= -\frac{1}{4\mu\_0}\left[\frac{\partial F\_{ab}}{\partial(\partial\_\mu A\_\nu)} F^{ab} + g\_{ai}g\_{bj}F^{ij}\frac{\partial (g^{ak}g^{bl}F\_{kl})}{\partial(\partial\_\mu A\_\nu)} \right] \\\\ &= -\frac{1}{4\mu\_0}\left[\frac{\partial F\_{ab}}{\partial(\partial\_\mu A\_\nu)} F^{ab} + \delta\_{ki}\delta\_{lj}F^{ij}\frac{\partial F\_{kl}}{\partial(\partial\_\mu A\_\nu)} \right] \\\\ &= -\frac{1}{4\mu\_0}\left[\frac{\partial F\_{ab}}{\partial(\partial\_\mu A\_\nu)} F^{ab} + F^{ij}\frac{\partial F\_{ij}}{\partial(\partial\_\mu A\_\nu)} \right] \\\\ &= -\frac{1}{2\mu\_0}\left[\frac{\partial F\_{ab}}{\partial(\partial\_\mu A\_\nu)} F^{ab}  \right] \\\\ &= -\frac{1}{2\mu\_0}\left[\frac{\partial(\partial\_a A\_b - \partial\_b A\_a)}{\partial(\partial\_\mu A\_\nu)} F^{ab}  \right] \\\\ &= -\frac{1}{2\mu\_0}\left[(\delta^\mu\_a\delta^\nu\_b - \delta^\mu\_b\delta^\nu\_a  ) F^{ab}  \right]  \\\\  &= -\frac{1}{2\mu\_0} \left( F^{\mu\nu}-F^{\nu\mu} \right) \\\\ &=-\frac{1}{\mu\_0}F^{\mu\nu} \end{aligned}$

Therefore,

$\begin{aligned} \color{red}{\partial\_\mu F^{\mu\nu} = \mu\_0 J^{\nu}} \end{aligned}$

These are Maxwell's equations.

Next, we rewrite them in the familiar form. Substituting

$F^{\mu\nu} = \begin{bmatrix} 0 & -E^x/c & -E^y/c & -E^z /c\\\\ E^x/c & 0 & -B\_z & B^y \\\\ E^y/c & B^z & 0 & -B^x \\\\ E^z /c& -B^y & B^x & 0 \end{bmatrix}$

and

$J^{\mu} = (\rho c^2, J^x,J^y,J^z)$

into $\begin{aligned} \partial\_\mu F^{\mu\nu} = \mu\_0 J^{\nu} \end{aligned}$ gives:

$\begin{aligned} \frac{\partial\_i E^i}{c} = \mu\_0 \rho c \\\\ \Rightarrow \color{red}{ \nabla \cdot \mathbf{E} =\frac{\rho}{\epsilon\_0} }\end{aligned}$

and

$\begin{aligned} \varepsilon^{ij}\_{k} \partial\_{j}B^k - \frac{\partial}{\partial(ct)}E^i/c = \mu\_0J^i\\\\  \color{red}{ \Rightarrow \nabla \times \mathbf{B} = \mu\_0 (\mathbf{J}+ \epsilon\_0 \partial\_t \mathbf{E})} \end{aligned}$

These are the sourced Maxwell equations.

But where have the other two source-free equations ($\color{red}{ \nabla \cdot\mathbf{B}=0}$ and $\color{red}{ \nabla \times \mathbf{E} = -\partial\_t \mathbf{B}}$) gone?

In fact, these two source-free equations are not part of electromagnetic field dynamics, but part of the intrinsic structure of the electromagnetic field itself. This is because the source-free equations follow from $\mathrm{d}F=0$, while $\mathrm{d} F=0$ follows from $F = \mathrm{d} A$ (applying the exterior derivative twice to any differential form gives zero). And $F=\mathrm{d}A$ itself is the definition of the field strength tensor. Thus, the source-free equations follow from the definition of the electromagnetic field and are part of its intrinsic structure.

The source-free equations can be written as:

$\color{red}{\partial\_\mu (\star F)^{\mu\nu} = 0}$

where $(\star F)^{\mu\nu}$ is the Hodge dual of $F^{\mu\nu}$:

$\color{red}{(\star F)^{\mu\nu} = \begin{bmatrix} 0 & -B^x & -B^y & -B^z \\\\ B^x & 0 & E^z/c & -E^y/c \\\\ B^y & -E^z/c & 0 & E^x/c \\\\ B^z /c& E^y/c & -E^x/c & 0 \end{bmatrix}}$

Readers may derive the source-free equations from $\mathrm{d} F=0$.

> If readers know differential geometry, the following provides a more elegant derivation:  
>  $\begin{aligned} &\mathrm{d}F=0 \\\\ &\Rightarrow \mathrm{d} \star \star F = 0 \\\\ &\Rightarrow \mathrm{d} \star \flat\sharp\star F = 0 \\\\ &\Rightarrow (\sharp\star\mathrm{d} \star \flat)(\sharp\star F) = 0 \\\\ &\Rightarrow (\nabla\cdot)(\sharp\star F) = 0 \\\\ &\Rightarrow \partial\_\mu (\star F)^{\mu\nu} = 0 \end{aligned}$  
> where $\sharp$ raises indices, $\flat$ lowers indices, and $(\nabla\cdot)$ is the generalized divergence, defined as $(\nabla\cdot) = \sharp\star\mathrm{d} \star \flat$.

## V. Differential-Geometric Formulation  

Some readers dislike index calculations and instead prefer more canonical abstract notation, so this section rewrites the above once more in the language of differential geometry.

Given the Lagrangian:

$\begin{aligned} \mathcal{L} &= -\frac{1}{2\mu\_0} F \wedge (\star F) + A\wedge (\star J) \\\\ &= \left[-\frac{1}{2\mu\_0} \langle F , F\rangle + \langle A , J \rangle\right] \omega  \end{aligned}$

Note that if the $(+,-,-,-)$ metric is adopted, the second term above should be $-\langle A, J\rangle \omega$.

The metric volume form $\omega$ is defined as the n-form such that $\langle \omega ,\omega \rangle\_g = \pm 1 =: \operatorname{sgn}(g)$ holds, where n is the dimension of the manifold. Its explicit definition is $\omega = \sqrt{|\det(g)|}\,\mathrm{d}x^0 \wedge \mathrm{d}x^1 \wedge \mathrm{d}x^2 \wedge \mathrm{d}x^3 = \mathrm{d}x^0 \wedge \mathrm{d}x^1 \wedge \mathrm{d}x^2 \wedge \mathrm{d}x^3$.

> The Hodge dual $\star \beta$ of the differential form $\beta$ is defined by $\alpha \wedge \*\beta = \langle \alpha, \beta\rangle \omega$. Here $\langle \cdot,\cdot\rangle$ is the inner product of differential forms; for n-forms, the inner product is defined as:  
>  $\langle \alpha\_1,\cdots\wedge\alpha\_n,\,\beta\_1\wedge\cdots\wedge\beta\_n\rangle = \begin{vmatrix} \langle \alpha\_1,\beta\_1 \rangle & \cdots & \langle \alpha\_1,\beta\_n \rangle \\\\ \vdots & \ddots & \vdots \\\\ \langle \alpha\_n ,\beta\_1 \rangle  & \cdots & \langle\alpha\_n ,\beta\_n \rangle  \end{vmatrix}$

Note that the coefficient here is $-1/(2\mu\_0)$ rather than $-1/(4\mu\_0)$. This is because the earlier tensor-index notation ($F\_{\mu\nu}F^{\mu\nu}$) causes repeated summation when $\mu, \nu$ is exchanged, so previously one had to divide by an additional $1/2$.

From the form of $\mathcal{L}$, we can see that it is actually a 4-form rather than a scalar field. This is because it must be integrated into the action $\begin{aligned} S = \int \mathcal{L} \end{aligned}$.

Varying the action gives:

$\begin{aligned} \delta S&\stackrel{1}{=}\int \delta \mathcal{L} \\\\ &\stackrel{2}=\int -\frac{1}{2\mu\_0} [(\delta F) \wedge (\star F) +F\wedge(\delta\star F)] + (\delta A)\wedge (\star J) \\\\ &\color{blue}{\stackrel{3}{=}}\int -\frac{1}{2\mu\_0} [(\delta F) \wedge (\star F)+(\star \delta F)\wedge F] + (\delta A)\wedge (\star J) \\\\ & \color{blue}{\stackrel{4}=} \int -\frac{1}{2\mu\_0} [(\delta F) \wedge (\star F)+(\delta F)\wedge (\star F)] + (\delta A)\wedge (\star J) \\\\ &\stackrel{5}=\int -\frac{1}{\mu\_0} (\delta F) \wedge (\star F) + (\delta A)\wedge (\star J) \\\\ &\stackrel{6}= \int -\frac{1}{\mu\_0} (\delta \mathrm{d}A) \wedge (\star F) + (\delta A)\wedge (\star J) \\\\ &\stackrel{7}= \int -\frac{1}{\mu\_0} \mathrm{d}(\delta A) \wedge (\star F) + (\delta A)\wedge (\star J) \\\\ &\color{blue}{\stackrel{8}=} \int -\frac{1}{\mu\_0} (\delta A) \wedge (\mathrm{d}\star F) + (\delta A)\wedge (\star J) \\\\ &\stackrel{9}= \int  (\delta A) \wedge \left(-\frac{1}{\mu\_0}\mathrm{d}\star F + \star J\right) \end{aligned}$

Here, the third equality uses:

$\begin{aligned} \alpha\wedge\beta &= (-1)^{\deg(\alpha)\deg(\beta)}\end{aligned} \beta \wedge \alpha$

where $\deg(\alpha)$ denotes the degree of $\alpha$. For example, here $\deg(F)=2$, because $F$ is a 2-form.

The fourth equality uses:

$\begin{aligned} \star \alpha\wedge\beta &= (-1)^{\deg(\star\alpha)\deg(\beta)}\beta\wedge\star\alpha \\\\ &= (-1)^{\deg(\star\alpha)\deg(\beta)}\langle\beta,\alpha\rangle \omega \\\\ &= (-1)^{\deg(\star\alpha)\deg(\beta)}\langle\alpha,\beta\rangle \omega \\\\ &= (-1)^{\deg(\star\alpha)\deg(\beta)}\alpha \wedge\star\beta \end{aligned}$

The eighth equality uses integration by parts:

$\begin{aligned} \int (\mathrm{d}\alpha) \wedge \beta &= \int \left[\cancel{\mathrm{d}(\alpha \wedge \beta)} - (-1)^{\text{deg}(\alpha)} \alpha \wedge \mathrm{d}\beta\right]\end{aligned}$

The reason $\int\_M\mathrm{d}(\alpha \wedge \beta) = 0$ is that, according to Stokes' theorem, $\int\_M\mathrm{d}(\alpha \wedge \beta)=\int\_{\partial M} \alpha \wedge \beta$, where $\partial M$ is the boundary of $M$. Moreover, $\int\_{\partial M} \alpha \wedge \beta =0$ (the boundary condition in variational calculus is $\delta A|\_{\partial M}=0$).

Since $\delta S =0$ holds for arbitrary $\delta A$, we have $-\frac{1}{\mu\_0}\mathrm{d}\star F + \star J = 0$, namely Maxwell's equations:

$\color{red}{\mathrm{d}\star F =\mu\_0 \star J}$

What is the advantage of writing them this way? The answer is that they can be readily extended to curved spacetime. To go from flat spacetime to curved spacetime, we need only replace the metric, which in the equation above is reflected by replacing the Hodge star operator, since the Hodge star operator is defined in terms of the metric.

## VI. Comparison of Covariant/Contravariant Forms  

Finally, let us compare the index notation and the differential-form notation:

(Contravariant) index notation:

$\begin{aligned} \partial\_\mu (\star{F})^{\mu \nu}&= 0 \\\\ \partial\_\mu F^{\mu\nu}&= \mu\_0 J^\nu  \end{aligned}$

(Covariant) differential-form notation:

$\begin{aligned} \mathrm{d} F&=0 \\\\ \mathrm{d} \star F &= \mu\_0 \star J \end{aligned}$

$F$ in index notation becomes the dual $(\star F)$ in differential-form notation, and vice versa. This is because $F^{\mu\nu}$ in index notation is a contravariant tensor, whereas the differential form $F$ is a covariant tensor. According to $(\nabla\cdot) \sharp = \sharp\star\mathrm{d} \star $, we have $\partial\_\mu F^{\mu\nu} = \sharp\star \mathrm{d} \star F$. See the figure below:

$\begin{matrix} k\text{-vector fields} & \stackrel{(\nabla\cdot)}{\longrightarrow}  & (k-1)\text{-vector fields}\\\\ \uparrow\sharp & & \uparrow\sharp \\\\  k\text{-form}  & & (k-1)\text{-form}\\\\ \downarrow\star &  & \uparrow \star \\\\ (n-k)\text{-form} &  \stackrel{\mathrm{d}}\longrightarrow  & (n-k+1)\text{-form} \end{matrix}$

> Alternatively, one may use the more common co-differential $\mathrm{d}^\dagger$, defined by $\langle \alpha, \mathrm{d}\beta\rangle = \langle \mathrm{d}^\dagger\alpha, \beta\rangle$.  
>   
> It can be proved (see the appendix) that $\mathrm{d}^\dagger \alpha = (-1)^{k}\star^{-1} \mathrm{d} \star \alpha = (-1)^{nk+n+1} s\star \mathrm{d} \star \alpha$, where $k=\deg(\alpha)$ and $s=\operatorname{sgn}(g) := \operatorname{sgn}(\det (g))$ is the signature of the metric.  
>   
> For the Minkowski metric, $s = -1$. Substituting into $s=-1,\,n=4,\,k=2$ gives $\mathrm{d}^\dagger F=\star \mathrm{d}\star F$.  
>   
> Thus, the figure above may be drawn as:  
>  $\begin{matrix} 2\text{-vector fields} & \stackrel{(\nabla\cdot)}{\longrightarrow}  & 1\text{-vector fields}\\\\ \uparrow\sharp & & \uparrow\sharp \\\\  2\text{-form}  & \xrightarrow{\mathrm{d}^\dagger} & 1\text{-form}\\\\ \downarrow\star &  & \uparrow \star \\\\ 2\text{-form} &  \stackrel{\mathrm{d}}\longrightarrow  & 3\text{-form} \end{matrix}$

Thus,

$\begin{matrix} F^{\mu\nu} & \xrightarrow{(\nabla\cdot)} & \partial\_\mu F^{\mu\nu}=\mu\_0J^\nu \\\\ \uparrow \sharp & & \uparrow \sharp \\\\ F & \xrightarrow{\star \mathrm{d}\star} & \star \mathrm{d} \star F \end{matrix}$

It follows that $\partial\_\mu F^{\mu\nu}=\mu\_0J^\nu$ is equivalent to $\star \mathrm{d} \star F = \mu\_0 J$.

For a 1-form, $\star\star = (-1)^{k(n-k)+s} \operatorname{id} = (-1)^{1(4-1)+1} \operatorname{id} = \operatorname{id}$. Therefore, $\star \mathrm{d} \star F = \mu\_0 J$ is equivalent to $\mathrm{d} \star F = \mu\_0 \star J$.

The derivation for $\mathrm{d} F = 0  \Leftrightarrow \partial\_\mu (\star F)^{\mu\nu} = 0$ is similar.

## VII. Appendix  

Lemma 1: $\mathrm{d}(\alpha \wedge \beta) = \mathrm{d}\alpha \wedge \beta + (-1)^{\deg(\alpha)} \alpha \wedge \mathrm{d}\beta$

> Proof:  
> Let  
>  $\begin{aligned} \alpha \wedge \beta &= \sum\_{I,J} a\_I b\_J\mathrm{d} x^I \wedge \mathrm{d}x^J \\\\ &= \sum\_{i\_1,\cdots,i\_{m},j\_1,\cdots,j\_n} a\_{i\_1,\cdots,i\_{m}}b\_{j\_1,\cdots,j\_n}\mathrm{d}x^{i\_1} \wedge \cdots \wedge \mathrm{d}x^{i\_m} \wedge \mathrm{d}x^j\_1\wedge \cdots \wedge \mathrm{d}x^{j\_n} \end{aligned}$  
> Then  
>  $\begin{aligned} \mathrm{d}(\alpha\wedge \beta) &= \partial\_i (a\_I b\_J) \mathrm{d}x^i\wedge \mathrm{d}x^I \wedge \mathrm{d}x^J \\\\ &=[(\partial\_i a\_I)b\_J \mathrm{d}x^i \wedge \mathrm{d}x^I] \wedge \mathrm{d}x^J + a\_I\partial\_i b\_J \mathrm{d}x^i \wedge \mathrm{d}x^I \wedge \mathrm{d}x^J \\\\ &=(\partial\_i a\_I\mathrm{d}x^i \wedge \mathrm{d}x^I) \wedge (b\_J \mathrm{d}x^J) + (-1)^{\deg(\alpha)} (a\_I\partial\_i  \mathrm{d}x^I \wedge \mathrm{d}x^i) \wedge (b\_J\mathrm{d}x^J) \\\\ &=\mathrm{d}\alpha \wedge \beta + (-1)^{\deg(\alpha)} \alpha \wedge \mathrm{d}\beta \end{aligned}$

Lemma 2: When $\deg(\alpha)=\deg(\beta)$, we have $\star\alpha \wedge \beta = (-1)^{k(n-k)}\alpha\wedge \star\beta$, where $k=\deg(\alpha)$

> Proof:  
>  $\begin{aligned} \star \alpha\wedge\beta &= (-1)^{\deg(\star\alpha)\deg(\beta)} \beta\wedge\star\alpha \\\\  &= (-1)^{k(n-k)}\langle\beta,\alpha\rangle \omega \\\\  &= (-1)^{k(n-k)}\langle\alpha,\beta\rangle \omega \\\\  &= (-1)^{k(n-k)}\alpha \wedge\star\beta \end{aligned}$

Lemma 3: $\star\star \alpha = (-1)^{k(n-k)}s \alpha$, where $k=\deg(\alpha)$, $s=\operatorname{sgn}(g)$.

> Proof:  
>  $\begin{aligned} \star\alpha \wedge \star\star \alpha &= \langle \star\alpha, \star\alpha \rangle\omega \\\\ &= s\langle \alpha,\alpha \rangle\omega \\\\ &= s\alpha \wedge \star \alpha\\\\ &= (-1)^{k(n-k)}s \star\alpha\wedge \alpha \\\\ &= \star\alpha\wedge \left[(-1)^{k(n-k)}s  \alpha\right] \end{aligned}$

Lemma 4: $\mathrm{d}^\dagger \alpha = (-1)^{k}\star^{-1} \mathrm{d} \star \alpha$

> Proof:  
>  $\begin{aligned} \langle \beta,\mathrm{d}^\dagger \alpha\rangle&= \langle \mathrm{d}\beta , \alpha\rangle \\\\ &= \int\mathrm{d}\beta \wedge \star \alpha \\\\ &= \int -(-1)^{\deg(\beta)} \beta \wedge \mathrm{d}\star \alpha \\\\ &= \int (-1)^{\deg(\beta)+1} \beta \wedge \mathrm{d}\star \alpha \\\\ &= \int (-1)^{\deg(\alpha)} \beta \wedge \mathrm{d}\star \alpha \\\\ &= \int (-1)^{\deg(\alpha)} \beta \wedge \star (\star^{-1}\mathrm{d}\star \alpha) \\\\ &= (-1)^{k} \langle\beta, \star^{-1}\mathrm{d} \star \alpha \rangle \end{aligned}$

Lemma 5: $\mathrm{d}^\dagger \alpha  = (-1)^{nk+n+1} s\star \mathrm{d} \star \alpha$

> Proof:  
> This follows immediately by combining Lemma 3 and Lemma 4.
