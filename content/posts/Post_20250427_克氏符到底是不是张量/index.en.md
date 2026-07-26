---
title: "Are Christoffel Symbols Tensors After All?"
date: 2025-04-27T23:12:31+08:00
originalURL: "https://www.zhihu.com/question/616788207/answer/1899964144238703076"
aliases:
  - "/en/christoffel/"
  - "/en/Post_20251012_克氏符到底是不是张量/"
draft: false
tags: ["Christoffel symbols", "general relativity"]
categories: ["mathematical physics methods"]
author: "Haifei"
---

My favorite way to understand this is to regard $\Gamma$ as a connection on the frame bundle. Then, the transformation law of the Christoffel symbols

$\boxed{ \begin{aligned} \bar{\Gamma}^i\_{\mu j} = \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial x^l}{\partial \bar{x}^j} \frac{\partial x^\nu}{\partial \bar{x}^\mu} \Gamma^k\_{\nu l}  \color{red}{ + \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial x^\mu \partial \bar{x}^j}} \end{aligned} }$

is nothing more than a gauge transformation:

$\boxed{ \bar{A} = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} }$

The extra inhomogeneous term $ g^{-1} \mathrm{d}g$ is inherently part of a gauge transformation.

But does this mean that $A$ is not a tensor field? Not at all.

A connection $A$ on a principal bundle is defined as a Lie-algebra-valued 1-form.

**The frame bundle is a principal bundle, and the Christoffel symbols correspond to a connection on the frame bundle, so the Christoffel symbols are also a 1-form. Since it is a 1-form, it is of course also a tensor field of type (0,1).**

Wait? Do Christoffel symbols not have two lower indices and one upper index? Why are they said to be a tensor field of type (0,1)? Let me explain.

## I. Gauge transformations  

When performing a gauge transformation $g$ on a principal bundle, the connection $A$ transforms as follows:

$A \mapsto g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g}$

For example, the simplest gauge transformation is the $U(1)$-bundle gauge transformation $g=\mathrm{e}^{\mathrm{i}\lambda}$:

$\begin{aligned} A &\mapsto g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} \\\\ &= \mathrm{e}^{-\mathrm{i}\lambda} A \mathrm{e}^{\mathrm{i}\lambda} \color{red}{+ \mathrm{e}^{-\mathrm{i}\lambda}\mathrm{d}  \mathrm{e}^{\mathrm{i}\lambda}} \\\\ &= A \color{red}{+\mathrm{i}\ \mathrm{d}\lambda} \end{aligned}$

In physics, one usually factors the imaginary unit $\mathrm{i}$ out of the connection $A$. Thus, the above equation is written in physics as:

$A \mapsto A \color{red}{+ \mathrm{d}\lambda}$

Let $A^\sharp=(\phi,\mathbf{A})$ and adopt the $(+,-,-,-)$ metric; then the above equation becomes:

$\boxed{ \begin{aligned} \phi &\mapsto \phi \color{red}{+ \partial\_t \lambda} \\\\ \mathbf{A} &\mapsto \mathbf{A} \color{red}{- \nabla \lambda} \end{aligned} }$

This is the electromagnetic gauge transformation. Note that $\nabla$ here denotes the gradient, not the covariant derivative.

The above $A$ is a Lie-algebra-valued 1-form: $A\in \Omega^1(M, \mathfrak{u}(1))$, meaning that it takes a tangent vector and returns an element of $\mathfrak{u}(1) \cong \mathrm{i}\mathbb{R}$.

If $\mathrm{i}$ is factored out, then there is no difference whatsoever from an ordinary real-valued 1-form.

This is why we regard the electromagnetic potential $A$ as a vector field.

Would anyone conclude that the electromagnetic potential $A$ is not a 1-form merely because the gauge transformation contains an extra term $\mathrm{d}\lambda$? Of course not! The same thing happens with Christoffel symbols.

## II. Connections on the frame bundle  

Now let us directly carry over electromagnetic gauge transformations to the case of Christoffel symbols. The only difference is that we replace the $U(1)$-principal bundle with the frame bundle $FM$, namely, the $GL(n)$-principal bundle.

> A frame is defined as an ordered set of basis vectors $f:=(e\_1, e\_2, ...,e\_n)$. Transformations between frames are described by $GL(n)$, and the group action of $GL(n)$ is free and transitive; therefore, the frame bundle is an $GL(n)$-principal bundle.

The connection $\Gamma$ at this point is a Lie-algebra-valued 1-form on the principal bundle:

$\Gamma\_{\text{global}} \in \Omega^1(FM, \mathfrak{gl}(n))$

Choosing a local frame $s$ locally trivializes it as $\Gamma = s^\*\Gamma\_{\text{global}} \in \Omega^1(M, \mathfrak{gl}(n))$.

Its value, as an element of the Lie algebra $\mathfrak{gl}(n)$, can act on the frame $f $ to yield $\Gamma f $, representing an infinitesimal $GL(n)$ transformation of the frame.

Note that the 1-form $\Gamma$ here has not yet taken a vector as its argument. More rigorously, we should write the vector to be taken as an empty slot:

$\Gamma(\cdot) f $

We may also write the vector $X$ being taken as the subscript $\Gamma\_X$ of $\Gamma$:

$\Gamma\_X f := \Gamma(X)f $

Written this way, it is very clear: $\Gamma$ is a Lie-algebra-valued 1-form; acting on the vector $X$ gives the Lie algebra element $\Gamma\_X \in \mathfrak{gl}(n)$, which can further act on $f$ to yield $\Gamma\_X f$.

So far, there is no issue: $\Gamma$ is a 1-form, that is, a tensor of type (0,1), except that its value after acting on a vector is a matrix in $\mathfrak{gl}(n)$.

Where does the problem arise? It arises when we write it in index notation, without distinguishing the action of $\Gamma$ as a 1-form from the action of $\Gamma$ as a Lie algebra element.

As a 1-form, $\Gamma$ can be expanded as:

$\Gamma =\Gamma\_\mu\mathrm{d}x^\mu$

where $\Gamma\_\mu$ is an element of the Lie algebra $\mathfrak{gl}(n)$. Here, there is no problem in saying that $\Gamma$ is a tensor of type (0,1). And its components $\Gamma\_\mu$ do indeed transform according to the component transformation law for tensor fields of type (0,1).

But what if we further expand $\Gamma\_\mu \in \mathfrak{gl}(n)$ in a local frame? Then we have

$\Gamma\_\mu = (\Gamma\_\mu)\_{j}^i\partial\_i \otimes \mathrm{d}x^j = :\Gamma\_{\mu j}^i \partial\_i \otimes \mathrm{d}x^j$

If we now write $\Gamma^i\_j := (\Gamma\_\mu)^i\_j \mathrm{d}x^\mu$, then this $\Gamma^i\_j$ is no longer a Lie-algebra-valued 1-form, but a real-valued 1-form. This is equivalent to taking every matrix element $\Gamma^i\_j$ of the $\mathfrak{gl}(n)$-valued $\Gamma$ as a 1-form.

This is where the problem lies: although $\Gamma^i\_j$ has upper and lower indices, it is itself a 1-form, not a component of any tensor field. Moreover, the definition of $\Gamma^i\_j$ as a 1-form depends on the choice of coordinate system ($\partial\_i \otimes \mathrm{d}x^j$). This is why some people say that it is a coordinate-dependent tensor field.

## III. Gauge transformations on the frame bundle  

Finally, let us derive the transformation law of the Christoffel symbols from the gauge transformation

$\bar{A}  = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g}$

> Note that $g$ here does not refer to the metric tensor, but to a gauge transformation.

First, let us replace $A$ with $\Gamma$:

$\bar{\Gamma} = g^{-1} \Gamma g \color{red}{+ g^{-1} \mathrm{d}g}$

Then expand the 1-forms $\bar{\Gamma}$ and $\mathrm{d}g$ in the local frame as $\bar{\Gamma}\_\mu \mathrm{d}\bar{x}^\mu$ and $(\bar{\partial}\_\nu g)\mathrm{d}\bar{x}^\nu$:

$\begin{aligned} \bar{\Gamma}\_\mu \mathrm{d}\bar{x}^\mu &\mapsto g^{-1} (\Gamma\_\nu \mathrm{d}x^\nu) g \color{red}{+ g^{-1} (\bar{\partial}\_\mu g)\mathrm{d}\bar{x}^\mu} \\\\ &= g^\nu\_\mu \ g^{-1} \left(\Gamma\_\nu \mathrm{d}\bar{x}^\mu \right) g \color{red}{+ g^{-1} (\bar{\partial}\_\mu g)\mathrm{d}\bar{x}^\mu}  \end{aligned}$

where $\bar{\partial}\_\mu :=\frac{\partial}{\partial \bar{x}^\mu}$, $g^\nu\_\mu = \frac{\partial x^\nu}{\partial \bar{x}^\mu}$.

Factoring out $\mathrm{d}\bar{x}^\mu$ gives:

$\begin{aligned} \bar{\Gamma}\_\mu  &= g^\nu\_\mu \ g^{-1} \left(\Gamma\_\nu \right) g \color{red}{+ g^{-1} (\bar{\partial}\_\mu g)}  \end{aligned}$

Then substitute the gauge transformation

$\begin{aligned} g = g^i\_j  \partial\_i \otimes \mathrm{d}x^j= \frac{\partial x^i}{\partial \bar{x}^j} \partial\_i \otimes \mathrm{d}x^j \end{aligned}$

and take components to obtain:

$\begin{aligned} (\bar{\Gamma}\_\mu )^i\_j &= g^\nu\_\mu(g^{-1})^i\_k \left(\Gamma\_\nu \right)^k\_l g^l\_j \color{red}{+ (g^{-1})^i\_k (\bar{\partial}\_\mu g^k\_l)}  \end{aligned}$

Finally, substituting the components of the gauge transformation

$\begin{aligned} g^i\_j = \frac{\partial x^i}{\partial \bar{x}^j} ,\quad (g^{-1})^i\_j = \frac{\partial \bar{x}^i}{\partial x^j} \end{aligned}$

gives:

$\begin{aligned} (\bar{\Gamma}\_\mu )^i\_j &= \frac{\partial x^\nu}{\partial \bar{x}^\mu}\frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial x^l}{\partial \bar{x}^j} \left(\Gamma\_\nu \right)^k\_l  \color{red}{+ \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial \bar{x}^\mu \partial \bar{x}^j}}  \end{aligned}$

Let $\Gamma\_{\mu j}^i := (\Gamma\_{\mu})^{i}\_{j}$; then we obtain the transformation law of the Christoffel symbols:

$\boxed{ \begin{aligned} \bar{\Gamma}^i\_{\mu j} = \frac{\partial \bar{x}^i}{\partial x^k}\frac{\partial x^l}{\partial \bar{x}^j} \frac{\partial x^\nu}{\partial \bar{x}^\mu} \Gamma^k\_{\nu l}  \color{red}{ + \frac{\partial \bar{x}^i}{\partial x^k} \frac{\partial^2 x^k}{\partial x^\mu \partial \bar{x}^j}} \end{aligned} }$

Is it necessary to memorize this formula? No; it is enough to remember $\boxed{ \bar{A}  = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} }$.

## IV. Gravity  

In particular, when the spacetime base manifold is equipped with a metric, we consider only orthonormal bases as frames. Thus, the structure group changes from $GL(4)$ to the metric-preserving subgroup, namely the Lorentz group $SO(1,3)$. Therefore, the gravitational field can be regarded as a gauge field of the Lorentz group $SO(1,3)$ [1], just as the electromagnetic field is an $U(1)$ gauge field and the gluon field is an $SU(3)$ gauge field, and so on.

## Supplement: Derivation of gauge transformations  

So where does the gauge transformation formula $\boxed{ \bar{A}  = g^{-1}A g \color{red}{+ g^{-1} \mathrm{d}g} }$ come from? It can likewise be derived from a more fundamental relation.

The more fundamental relation referred to here is $\boxed{ \mathrm{D} = \mathrm{d} + A \ \wedge }$, namely that the covariant exterior derivative equals the exterior derivative plus the connection.

> On the frame bundle, $\mathrm{D}$ is the covariant derivative $\nabla$.

Under the gauge transformation $g$, the field transforms according to $\bar{\psi} = g^{-1} \psi$. We want the covariant exterior derivative $\mathrm{D} \psi = \mathrm{d} \psi + A \wedge \psi$ of the field to transform in the same way, namely:

$\mathrm{\bar{D}}\bar{\psi} = g^{-1}(\mathrm{D}\psi )$.

> This is equivalent to requiring $\boxed{ \bar{\mathrm{D}} = g^{-1} \mathrm{D} g }$.

Expanding the left-hand side:

$\begin{aligned} \mathrm{\bar{D}}\bar{\psi} &= (\mathrm{\mathrm{d}+\bar{A}}\ \wedge)(g^{-1}\psi) \\\\ &= \mathrm{d}(g^{-1}\psi) + \bar{A} \wedge (g^{-1}\psi) \\\\ &= (\mathrm{d} g^{-1})\psi + g^{-1} \mathrm{d}\psi + \bar{A}g^{-1} \wedge \psi \end{aligned}$

Expanding the right-hand side:

$\begin{aligned} g^{-1}(\mathrm{D}\psi ) &= g^{-1} (\mathrm{d} + A\ \wedge )\psi\\\\ &= g^{-1}\mathrm{d} \psi + g^{-1} A \wedge \psi \end{aligned}$

Comparing the two sides gives:

$\bar{A}g^{-1} \wedge \psi = g^{-1} A \wedge \psi - (\mathrm{d} g^{-1} )\psi$

Factoring out $\psi$:

$ \bar{A} g^{-1}= g^{-1} A - \mathrm{d}g^{-1}$

Right-multiplying by $g$ and using $\mathrm{d}(g^{-1}g)=0$ gives:

$\boxed{ \bar{A} = g^{-1} A g + g^{-1} \mathrm{d} g }$

Thus we obtain the transformation law of the connection under a gauge transformation.

## Supplement: The curvature tensor  

Since we have said so much, let us also briefly mention curvature.

The curvature $F$ on a principal bundle is defined as the square of the covariant exterior derivative $\mathrm{D}$, and is a 2-form:

$\boxed{ F =\mathrm{D}^2 }$

Substituting $\mathrm{D} = \mathrm{d} + A \ \wedge$ gives:

$\begin{aligned} \mathrm{D}^2 \psi &= (\mathrm{d} + A\ \wedge)^2 \psi \\\\ &= \cancel{\mathrm{d}\mathrm{d}} + \mathrm{d} (A \wedge \psi) + A \wedge (\mathrm{d}\psi) + A \wedge A \wedge \psi \\\\ &=\mathrm{d} A \wedge \psi \cancel{- A \wedge \mathrm{d}\psi} \cancel{+A\wedge \mathrm{d}\psi} + A \wedge A \wedge \psi \\\\ &= (\mathrm{d} A+ A \wedge A)\wedge  \psi \end{aligned}$

Therefore:

$\boxed{ F=\mathrm{d} A + A \wedge A }$

Expanding $F$ as $F = \frac{1}{2}F\_{\mu\nu} \mathrm{d}x^\mu \wedge \mathrm{d}x^\nu$ and $A$ as $A = A\_{\mu} \mathrm{d}x^{\mu}$, then substituting into the above formula, gives:

$F\_{\mu\nu} = \partial\_\mu A\_\nu - \partial\_\nu A\_\mu + [A\_\mu , A\_\nu]$

The above derivation applies to all principal bundles. Now, considering the frame bundle as a principal bundle, its fibers have a free and transitive $GL(n)$ action, and its Lie algebra is $\mathfrak{gl}(n)$. Thus, both sides of the above equation are matrices in $\mathfrak{gl}(n)$: $F\_{\mu\nu} = \{ (F\_{\mu\nu})^i\_j\}, \ \ A\_{\mu}=\{(A\_\mu)^i\_j\}$.

Let $R^i\_{j\mu\nu} := (F\_{\mu\nu})^i\_j$, $\Gamma^{i}\_{\mu j}:= (A\_\mu)^i\_j$; substituting into the above equation gives:

$\boxed{ R^i\_{j\mu\nu}= \partial\_\mu \Gamma^i\_{\nu j} - \partial\_\nu \Gamma^i\_{\mu j} + \Gamma^{i}\_{\mu k} F^{k}\_{\nu j} -  \Gamma^{i}\_{\nu k} F^{k}\_{\mu j} }$

This is precisely the curvature tensor.

Eh? Wait? Why is the connection $\Gamma^i\_{\mu j}$ not a component of a tensor field, while $R^i\_{j\mu\nu}$ is a component of a tensor field?

This is because, although the connection $A$ is not gauge invariant, the curvature $F$ is gauge invariant (or, equivalently, gauge covariant). As can be seen from the following equation, the transformation law of curvature has only a homogeneous term:

$\begin{aligned} \mathrm{\bar{\nabla}} &= g^{-1} \mathrm{\nabla} g \\\\ \Rightarrow \bar{F} &= \bar{\nabla}^2 = (g^{-1} \nabla g)^2 = \underbrace{g^{-1} F g}\_{\text{homogeneous}} \end{aligned}$

In contrast, the transformation law of the connection has an inhomogeneous term:

$A \mapsto \underbrace{g^{-1}A g}\_{\text{homogeneous}} \color{red}{+ \underbrace{g^{-1} \mathrm{d}g}\_{\text{inhomogeneous}}}$

## Supplement: Frame bundles vs. vector bundles  

Someone may ask why use frame bundles rather than the more direct vector bundles. Because frame bundles are principal bundles, whereas vector bundles are not.

Why do we need principal bundles? Because we want gauge groups and gauge transformations.

A principal bundle requires a free and transitive action of a group $G$ on its fibers. Such a fiber is also called an $G$-torsor.

> Free means that for any point $p$ in the fiber, if $pg=p$, then the group element $g$ is the identity element.  
> Transitive means that for any two points $p$ and $q$ in the fiber, one can find a group element $g$ such that $q=pg$.

An $G$-torsor is “almost” isomorphic to the group $G$. **Their only difference is that an $G$-torsor has no canonical identity element; one can only choose a base point as the identity element, and this base point is the so-called gauge.** Once a base point is chosen, the $G$-torsor and $G$ are isomorphic.

Why is a vector bundle not a principal bundle? Because the $GL(n,\mathbb{R})$ group action on the fibers of a vector bundle (that is, the vector space $V\cong \mathbb{R}^n$) is not free and transitive ($V$ is clearly not isomorphic to $GL(n,\mathbb{R})$). In other words, a vector space is not an $GL(n)$-torsor.

> For example, any $GL(n,\mathbb{R})$ group element can only map the zero vector to the zero vector, so the action of $GL(n,\mathbb{R})$ on $V\cong \mathbb{R}^n$ is neither free nor transitive.

However, the set of frames is an $GL(n)$-torsor. Once a reference frame is chosen, the set of all frames is isomorphic to $GL(n,\mathbb{R})$.

## References  

1. Utiyama, Ryoyu. "Invariant theoretical interpretation of interaction." Physical Review 101.5 (1956): 1597. [https://doi.org/10.1103/PhysRev.101.1597](https://doi.org/10.1103/PhysRev.101.1597)
