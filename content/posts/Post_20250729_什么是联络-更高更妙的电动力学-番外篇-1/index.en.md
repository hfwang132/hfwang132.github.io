---
title: "Gauge-Field Connections vs. Connections in General Relativity [Higher and More Elegant Electrodynamics · Extra 1]"
date: 2025-07-29T15:08:10+08:00
originalURL: "https://zhuanlan.zhihu.com/p/1933542737275250334"
aliases:
  - "/en/what_is_a_connection/"
  - "/en/Post_20251012_什么是联络-更高更妙的电动力学-番外篇-1/"
draft: false
tags: ["connection", "general relativity", "electrodynamics"]
categories: ["Methods of Mathematical Physics"]
math: true
author: "Haifei"
---

In a [previous article](https://zhuanlan.zhihu.com/p/23958176393), we said that the electromagnetic field is a connection. This led many readers to think of the connection in general relativity. What are the differences and commonalities between these two kinds of connections?

The electromagnetic connection \(A\) is a connection on a principal bundle, whereas the general-relativistic connection \(\Gamma\) is a connection on a vector bundle. Their definitions appear to be quite different. Is there a way to relate them?

The answer is: yes! We can absolutely regard the connection in general relativity as a connection on a principal bundle as well. In this way, the two kinds of connections are unified as the same mathematical object.

In fact, \(\Gamma\) can be regarded as a connection on the frame bundle (a type of principal bundle). Then, the transformation rule for the Christoffel symbols

\[\boxed{ \begin{aligned} \bar{\Gamma}^i_{\mu j} = \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial x^l}{\partial \bar{x}^j} \frac{\partial x^\nu}{\partial \bar{x}^\mu} \Gamma^k_{\nu l}  \color{red}{ + \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial x^\mu \partial \bar{x}^j}} \end{aligned} }\]

is nothing more than a gauge transformation:

\[\boxed{ \bar{A} = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} }\]

The extra inhomogeneous term \( g^{-1} \mathrm{d}g\) is inherently part of a gauge transformation.

> In addition, as mentioned previously, the curvature of a non-Abelian gauge field is \(\boxed{ F=\mathrm{d} A + A \wedge A }\). Where does this extra \(A \wedge A \) come from? After reading this article, you will know the answer as well.

## I. Gauge Transformations  

When performing a gauge transformation \(g\) on a principal bundle, the connection \(A\) transforms as follows:

\[A \mapsto g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g}\]

> As for where this formula comes from, we will explain it in Section V.

For example, the simplest gauge transformation is the gauge transformation \(U(1)\) on a \(g=\mathrm{e}^{\mathrm{i}\lambda}\)-fiber bundle:

\[\begin{aligned} A &\mapsto g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} \\ &= \mathrm{e}^{-\mathrm{i}\lambda} A \mathrm{e}^{\mathrm{i}\lambda} \color{red}{+ \mathrm{e}^{-\mathrm{i}\lambda}\mathrm{d}  \mathrm{e}^{\mathrm{i}\lambda}} \\ &= A \color{red}{+\mathrm{i}\ \mathrm{d}\lambda} \end{aligned}\]

In physics, the imaginary unit \(\mathrm{i}\) is usually factored out of the connection \(A\). Thus, the above equation is written in physics as:

\[A \mapsto A \color{red}{+ \mathrm{d}\lambda}\]

Let \(A^\sharp=(\phi,\mathbf{A})\) and adopt the \((+,-,-,-)\) metric; then the above equation becomes:

\[\boxed{ \begin{aligned} \phi &\mapsto \phi \color{red}{+ \partial_t \lambda} \\ \mathbf{A} &\mapsto \mathbf{A} \color{red}{- \nabla \lambda} \end{aligned} }\]

This is the electromagnetic gauge transformation. Note that \(\nabla\) here denotes the gradient, not the covariant derivative.

The \(A\) above is a Lie-algebra-valued 1-form: \(A\in \Omega^1(M, \mathfrak{u}(1))\), meaning that it takes a tangent vector and returns an element of \(\mathfrak{u}(1) \cong \mathrm{i}\mathbb{R}\).

If \(\mathrm{i}\) is factored out, then it is no different from an ordinary real-valued 1-form.

This is why we regard the electromagnetic potential \(A\) as a vector field.

The same thing happens with the Christoffel symbols.

## II. Connections on the Frame Bundle  

Now, let us directly apply the electromagnetic gauge transformation to the case of the Christoffel symbols. The only difference is that we replace the \(U(1)\)-principal bundle with the frame bundle \(FM\), namely, the \(GL(n)\)-principal bundle.

> A frame is defined as an ordered set of basis vectors \(f:=(e_1, e_2, ...,e_n)\). Transformations between frames are described by \(GL(n)\), and the group action of \(GL(n)\) is free and transitive; therefore, the frame bundle is a \(GL(n)\)-principal bundle.

The connection \(\Gamma\) at this point is a Lie-algebra-valued 1-form on a principal bundle:

\[\Gamma_{\text{global}} \in \Omega^1(FM, \mathfrak{gl}(n))\]

Choosing a local frame \(s\), it can be locally trivialized as \(\Gamma = s^*\Gamma_{\text{global}} \in \Omega^1(M, \mathfrak{gl}(n))\).

Its value, as an element of the Lie algebra \(\mathfrak{gl}(n)\), can act on the frame \(f \) to yield \(\Gamma f \), representing an infinitesimal \(GL(n)\) transformation of the frame.

Note that the 1-form \(\Gamma\) here has not yet taken a vector as its argument. More rigorously, we should write the vector to be taken as a placeholder:

\[\Gamma(\cdot) f \]

We can also write the vector \(X\) it takes as the subscript \(\Gamma_X\) of \(\Gamma\):

\[\Gamma_X f := \Gamma(X)f \]

Written this way, it is very clear: \(\Gamma\) is a Lie-algebra-valued 1-form. Acting on the vector \(X\) gives the Lie-algebra element \(\Gamma_X \in \mathfrak{gl}(n)\), which can further act on \(f\) to give \(\Gamma_X f\).

Up to this point, there is no problem: \(\Gamma\) is a 1-form, that is, a tensor of type (0,1), except that its value after acting on a vector is a matrix in \(\mathfrak{gl}(n)\).

Then why do people always say that the Christoffel symbols \(\Gamma_{\mu i}^j\) are not tensors? Where does the problem lie? The problem arises when we write them in index notation, because we fail to distinguish between the action of \(\Gamma\) as a 1-form and the action of \(\Gamma\) as a Lie-algebra element.

As a 1-form, \(\Gamma\) can be expanded as:

\[\Gamma =\Gamma_\mu\mathrm{d}x^\mu\]

where \(\Gamma_\mu\) is an element of the Lie algebra \(\mathfrak{gl}(n)\). Here, there is no issue in saying that \(\Gamma\) is a tensor of type (0,1). Moreover, the components \(\Gamma_\mu\) indeed transform according to the transformation rule for the components of a tensor field of type (0,1).

But what if we further expand \(\Gamma_\mu \in \mathfrak{gl}(n)\) in a local frame? Then we have

\[\Gamma_\mu = (\Gamma_\mu)_{j}^i\partial_i \otimes \mathrm{d}x^j = :\Gamma_{\mu j}^i \partial_i \otimes \mathrm{d}x^j\]

If we now write \(\Gamma^i_j := (\Gamma_\mu)^i_j \mathrm{d}x^\mu\), then this \(\Gamma^i_j\) is no longer a Lie-algebra-valued 1-form, but a real-valued 1-form. This is equivalent to taking each matrix element \(\Gamma^i_j\) of the \(\mathfrak{gl}(n)\)-valued \(\Gamma\) as a 1-form.

This is where the problem lies: although \(\Gamma^i_j\) has upper and lower indices, it is itself a 1-form rather than a component of any tensor field. Furthermore, the definition of \(\Gamma^i_j\) as a 1-form depends on the choice of coordinate system (\(\partial_i \otimes \mathrm{d}x^j\)). This is why some people say that it is a coordinate-dependent tensor field.

## III. Gauge Transformations on the Frame Bundle  

Finally, starting from the gauge transformation

\[\bar{A}  = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g}\]

we derive the transformation rule for the Christoffel symbols:

\[\begin{aligned} \bar{\Gamma}^i_{\mu j} = \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial x^l}{\partial \bar{x}^j} \frac{\partial x^\nu}{\partial \bar{x}^\mu} \Gamma^k_{\nu l}  \color{red}{ + \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial x^\mu \partial \bar{x}^j}} \end{aligned} \]

> Note that \(g\) here does not refer to the metric tensor, but to a gauge transformation.

First, let us replace \(A\) with \(\Gamma\):

\[\bar{\Gamma} = g^{-1} \Gamma g \color{red}{+ g^{-1} \mathrm{d}g}\]

Then expand the 1-forms \(\bar{\Gamma}\) and \(\mathrm{d}g\) in a local frame as \(\bar{\Gamma}_\mu \mathrm{d}\bar{x}^\mu\) and \((\bar{\partial}_\nu g)\mathrm{d}\bar{x}^\nu\):

\[\begin{aligned} \bar{\Gamma}_\mu \mathrm{d}\bar{x}^\mu &\mapsto g^{-1} (\Gamma_\nu \mathrm{d}x^\nu) g \color{red}{+ g^{-1} (\bar{\partial}_\mu g)\mathrm{d}\bar{x}^\mu} \\ &= g^\nu_\mu \ g^{-1} \left(\Gamma_\nu \mathrm{d}\bar{x}^\mu \right) g \color{red}{+ g^{-1} (\bar{\partial}_\mu g)\mathrm{d}\bar{x}^\mu}  \end{aligned}\]

where \(\bar{\partial}_\mu :=\frac{\partial}{\partial \bar{x}^\mu}\), \(g^\nu_\mu = \frac{\partial x^\nu}{\partial \bar{x}^\mu}\).

Factoring out \(\mathrm{d}\bar{x}^\mu\) gives:

\[\begin{aligned} \bar{\Gamma}_\mu  &= g^\nu_\mu \ g^{-1} \left(\Gamma_\nu \right) g \color{red}{+ g^{-1} (\bar{\partial}_\mu g)}  \end{aligned}\]

Then substitute the gauge transformation

\[\begin{aligned} g = g^i_j  \partial_i \otimes \mathrm{d}x^j= \frac{\partial x^i}{\partial \bar{x}^j} \partial_i \otimes \mathrm{d}x^j \end{aligned}\]

and take components to obtain:

\[\begin{aligned} (\bar{\Gamma}_\mu )^i_j &= g^\nu_\mu(g^{-1})^i_k \left(\Gamma_\nu \right)^k_l g^l_j \color{red}{+ (g^{-1})^i_k (\bar{\partial}_\mu g^k_l)}  \end{aligned}\]

Finally, substituting the components of the gauge transformation

\[\begin{aligned} g^i_j = \frac{\partial x^i}{\partial \bar{x}^j} ,\quad (g^{-1})^i_j = \frac{\partial \bar{x}^i}{\partial x^j} \end{aligned}\]

gives:

\[\begin{aligned} (\bar{\Gamma}_\mu )^i_j &= \frac{\partial x^\nu}{\partial \bar{x}^\mu}\frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial x^l}{\partial \bar{x}^j} \left(\Gamma_\nu \right)^k_l  \color{red}{+ \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial \bar{x}^\mu \partial \bar{x}^j}}  \end{aligned}\]

Let \(\Gamma_{\mu j}^i := (\Gamma_{\mu})^{i}_{j}\); then we obtain the transformation formula for the Christoffel symbols:

\[\boxed{ \begin{aligned} \bar{\Gamma}^i_{\mu j} = \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial x^l}{\partial \bar{x}^j} \frac{\partial x^\nu}{\partial \bar{x}^\mu} \Gamma^k_{\nu l}  \color{red}{ + \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial x^\mu \partial \bar{x}^j}} \end{aligned} }\]

Is it necessary to memorize this formula? No; it is enough to remember \(\boxed{ \bar{A}  = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} }\).

## IV. Gravity  

In particular, spacetime, the base manifold, is equipped with a metric. The frames are then orthonormal bases, so the structure group changes from \(GL(4)\) to the metric-preserving subgroup, namely the Lorentz group \(SO(1,3)\). Thus, the gravitational field can be regarded as the gauge field of the Lorentz group \(SO(1,3)\)[[1]](#ref\_1), just as the electromagnetic field is a \(U(1)\) gauge field and the gluon field is a \(SU(3)\) gauge field, and so on.

## V: Derivation of Gauge Transformations  

So where does the gauge transformation formula \(\boxed{ \bar{A}  = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} }\) come from? It can likewise be derived from a more fundamental relation.

The more fundamental relation referred to here is \(\boxed{ \mathrm{D} = \mathrm{d} + A \ \wedge }\), namely, the covariant exterior derivative equals the exterior derivative plus the connection.

> On the frame bundle, \(\mathrm{D}\) is the covariant derivative \(\nabla\).

Under the gauge transformation \(g\), the field transforms according to \(\bar{\psi} = g^{-1} \psi\). We want the covariant exterior derivative \(\mathrm{D} \psi = \mathrm{d} \psi + A \wedge \psi\) of the field to transform in the same way, namely:

\(\mathrm{\bar{D}}\bar{\psi} = g^{-1}(\mathrm{D}\psi )\).

> This is equivalent to requiring \(\boxed{ \bar{\mathrm{D}} = g^{-1} \mathrm{D} g }\).

Expanding the left-hand side of the above equation:

\[\begin{aligned} \mathrm{\bar{D}}\bar{\psi} &= (\mathrm{\mathrm{d}+\bar{A}}\ \wedge)(g^{-1}\psi) \\ &= \mathrm{d}(g^{-1}\psi) + \bar{A} \wedge (g^{-1}\psi) \\ &= (\mathrm{d} g^{-1})\psi + g^{-1} \mathrm{d}\psi + \bar{A}g^{-1} \wedge \psi \end{aligned}\]

Expanding the right-hand side:

\[\begin{aligned} g^{-1}(\mathrm{D}\psi ) &= g^{-1} (\mathrm{d} + A\ \wedge )\psi\\ &= g^{-1}\mathrm{d} \psi + g^{-1} A \wedge \psi \end{aligned}\]

Comparing both sides gives:

\[\bar{A}g^{-1} \wedge \psi = g^{-1} A \wedge \psi - (\mathrm{d} g^{-1} )\psi\]

Factoring out \(\psi\):

\[ \bar{A} g^{-1}= g^{-1} A - \mathrm{d}g^{-1}\]

Multiplying on the right by \(g\) and using \(\mathrm{d}(g^{-1}g)=0\) gives:

\[\boxed{ \bar{A} = g^{-1} A g + g^{-1} \mathrm{d} g }\]

This yields the transformation formula for the connection under a gauge transformation.

## VI. Curvature Tensor  

The curvature \(F\) on a principal bundle is defined as the square of the covariant exterior derivative \(\mathrm{D}\), and is a 2-form:

\[\boxed{ F =\mathrm{D}^2 }\]

Substituting \(\mathrm{D} = \mathrm{d} + A \ \wedge\) gives:

\[\begin{aligned} \mathrm{D}^2 \psi &= (\mathrm{d} + A\ \wedge)^2 \psi \\ &= \cancel{\mathrm{d}\mathrm{d}} + \mathrm{d} (A \wedge \psi) + A \wedge (\mathrm{d}\psi) + A \wedge A \wedge \psi \\ &=\mathrm{d} A \wedge \psi \cancel{- A \wedge \mathrm{d}\psi} \cancel{+A\wedge \mathrm{d}\psi} + A \wedge A \wedge \psi \\ &= (\mathrm{d} A+ A \wedge A)\wedge  \psi \end{aligned}\]

Therefore:

\[\boxed{ F=\mathrm{d} A + A \wedge A }\]

Expanding \(F\) as \(F = \frac{1}{2}F_{\mu\nu} \mathrm{d}x^\mu \wedge \mathrm{d}x^\nu\) and \(A\) as \(A = A_{\mu} \mathrm{d}x^{\mu}\), then substituting into the above equation, gives:

\[F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + [A_\mu , A_\nu]\]

The derivation above applies to all principal bundles. Now consider the frame bundle as a principal bundle. Its fibers carry a free and transitive \(GL(n)\) action, and its Lie algebra is \(\mathfrak{gl}(n)\). Thus, both sides of the above equation are matrices in \(\mathfrak{gl}(n)\): \(F_{\mu\nu} = \{ (F_{\mu\nu})^i_j\}, \ \ A_{\mu}=\{(A_\mu)^i_j\}\).

Let \(R^i_{j\mu\nu} := (F_{\mu\nu})^i_j\), \(\Gamma^{i}_{\mu j}:= (A_\mu)^i_j\). Substituting into the above equation gives:

\[\boxed{ R^i_{j\mu\nu}= \partial_\mu \Gamma^i_{\nu j} - \partial_\nu \Gamma^i_{\mu j} + \Gamma^{i}_{\mu k} F^{k}_{\nu j} -  \Gamma^{i}_{\nu k} F^{k}_{\mu j} }\]

This is precisely the curvature tensor.

Wait—why is the connection \(\Gamma^i_{\mu j}\) not a component of a tensor field, whereas \(R^i_{j\mu\nu}\) is a component of a tensor field?

This is because, although the connection \(A\) is not gauge-invariant, the curvature \(F\) is gauge-invariant (or, rather, gauge-covariant). As can be seen from the following equation, the transformation law for curvature contains only a homogeneous term:

\[\begin{aligned} \mathrm{\bar{\nabla}} &= g^{-1} \mathrm{\nabla} g \\ \Rightarrow \bar{F} &= \bar{\nabla}^2 = (g^{-1} \nabla g)^2 = \underbrace{g^{-1} F g}_{\text{homogeneous}} \end{aligned}\]

In contrast, the transformation formula for the connection has an inhomogeneous term:

\[A \mapsto \underbrace{g^{-1}A g}_{\text{homogeneous}} \color{red}{+ \underbrace{g^{-1} \mathrm{d}g}_{\text{inhomogeneous}}}\]

## Summary  

This article introduced:

1. How to regard the connection in general relativity (a connection on a vector bundle) as the connection of a gauge field (a connection on a principal bundle):

\[\begin{aligned} &\boxed{ \bar{A} = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} } \\ &\Leftrightarrow \\ &\boxed{ \begin{aligned} \bar{\Gamma}^i_{\mu j} = \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial x^l}{\partial \bar{x}^j} \frac{\partial x^\nu}{\partial \bar{x}^\mu} \Gamma^k_{\nu l}  \color{red}{ + \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial x^\mu \partial \bar{x}^j}} \end{aligned} } \end{aligned}\]

2. How to regard the Riemann curvature tensor as the curvature of a non-Abelian gauge field:

\[\begin{aligned} &\boxed{ F=\mathrm{d} A \color{red}{+ A \wedge A}} \\ &\Leftrightarrow \\ &\boxed{ R^i_{j\mu\nu}= \partial_\mu \Gamma^i_{\nu j} - \partial_\nu \Gamma^i_{\mu j} \color{red}{+ \Gamma^{i}_{\mu k} F^{k}_{\nu j} -  \Gamma^{i}_{\nu k} F^{k}_{\mu j} }} \end{aligned}\]

## References  

1. [^](#ref\_1\_0)Utiyama, Ryoyu. "Invariant theoretical interpretation of interaction." Physical Review 101.5 (1956): 1597. [https://doi.org/10.1103%2FPhysRev.101.1597](https://doi.org/10.1103/PhysRev.101.1597)
