---
title: "What is the relationship between Lie derivative and covariant derivative?"
date: 2024-01-26T23:50:58+08:00
draft: false
tags: ["Differential Geometry"]
categories: ["Mathematical Physics"]
---

## I. Differences and Similarities in Properties
Lie derivative $\mathcal{L}\_V$ and covariant derivative $\nabla\_V$ share many common points:

1. Both $\mathcal{L}\_V$ and $\nabla\_V$ preserve the type of tensors, mapping $\mathcal{T}^p\_q(M)$ to $\mathcal{T}^p\_q(M)$. $\mathcal{T}^p\_q(M)$ represents the set of all smooth tensor fields of type (p, q) on $M$.

Particularly, for (0,0) type tensor fields, i.e., scalar fields $f\in \mathcal{F}(M)$, we have $\mathcal{L}\_V f=\nabla\_V f=Vf$.

2. Both satisfy linearity and the Leibniz rule:

$ \begin{aligned} \mathcal{L}\_V(\mu A + \lambda B) &= \mu \mathcal{L}\_V A + \lambda \mathcal{L}\_V B, \\\\ \mathcal{L}\_V (A \otimes B) &= (\mathcal{L}\_V A)\otimes B + A \otimes (\mathcal{L}\_V B) \end{aligned} $ 

$\begin{aligned}  \nabla\_V(\lambda A+\mu B) &= \lambda \nabla\_V A + \mu \nabla\_V B \\\\  \nabla\_V(A\otimes B) &= (\nabla\_V A)\otimes B + A \otimes (\nabla\_V B)  \end{aligned}$ 

3. Both commute with contraction

$ \mathcal{L}\_V \circ C = C \circ \mathcal{L}\_V $ 

$ \nabla\_W \circ C = C \circ \nabla\_W $ 

So, what are their differences? The most important difference is as follows:

**4. Covariant derivative has $\mathcal{F}$-linearity in $V$, while Lie derivative only has ordinary linearity:**

$ \nabla\_{fV+gW} = f\nabla\_V + g\nabla\_W \quad f,g\in\mathcal{F}(M) $ 

$ \mathcal{L}\_{\lambda V+\mu W} = \lambda \mathcal{L}\_V + \mu \mathcal{L}\_W \quad \lambda,\mu\in\mathbb{R}$ 

where $\mathcal{F}(M)$ represents the set of all scalar fields on $M$.

This seems interesting, but what does it mean? With this question in mind, let's look at the next section.

## II. Significance of Lie Derivative and Covariant Derivative
As we all know, a derivative is taking the difference of objects at two points, then taking the limit as these two points approach each other. However, on a manifold, we encounter a problem: **the tangent spaces/cotangent spaces at different points are completely different spaces, that is, tensors at different points are not in the same space, so we cannot compare tensors at different points (cannot take the difference).**

Therefore, to compare tensors at different points, we **must somehow move the tensor at one point to the other point**. There are two ways to perform such a movement, the first is "flow" and the second is "parallel transport". The former corresponds to the Lie derivative, and the latter to the covariant derivative.

### 2.1 Flow—Lie Derivative  

> **Prerequisite Knowledge: Pull Back and Push Forward**  
> Suppose we have a diffeomorphism: $\phi:M\rightarrow N$. Differential geometry tells us that we can pull back tensor fields on $N$ to $M$. Conversely, we can also push forward tensor fields on $M$ to $N$.

An integral curve family (e.g., electric field lines) of a smooth vector field $V$ on $M$ can give a diffeomorphism

$\Phi\_t:M\rightarrow M, \quad \gamma(t\_0)\mapsto \gamma(t\_0+t)$ 

This diffeomorphism can be parameterized by a real number $t$. Intuitively, every point on the manifold "flows" a certain distance downstream along the integral curve it is on. Using the pullback map, we can induce the following map:

$\Phi^\*\_t: \mathcal{T}^p\_q(M) \rightarrow \mathcal{T}^p\_q(M)$ 

This provides a method of "moving a tensor at one point to another point":

1. First, let point $P$ "flow" a certain distance downstream along the integral curve to point $Q$, i.e., $\Phi\_t (P) =Q$,
2. Then pull back the tensor at point $Q$ to point $P$ through $\Phi^\*\_t$.

This gives a method of moving the tensor at point $Q$ to point $P$.

Thus, we can define the Lie derivative as follows:

$ \begin{aligned} \mathcal{L}\_V A &:= \left.\frac{\mathrm{d}}{\mathrm{d}t}\right|\_{t=0} (\Phi^\*\_t A) \\\\ &= \lim\_{t\rightarrow 0}\frac{\Phi^\*\_\epsilon A - A}{\epsilon} \end{aligned} $ 

The idea is: first let a point flow a small distance downstream, then pull the tensor at that point back to the original place and compare it with the original tensor at the point. If the results are the same, the derivative is zero; otherwise, the derivative is non-zero.


> Note: Actually writing $\Phi^\*\_t$ as $(\Phi^{V}\_t)^\*$ would be more explicit, indicating that $\Phi^\*\_t$ is about $V$, but this looks too clunky.

### 2.2 Parallel Transport—Covariant Derivative  
The method of "moving a tensor at one point to another point" by the Lie derivative always feels somewhat awkward. This is because, in order to move a vector at point $Q$ to point $P$ through a certain path, we need to find a vector field such that it has an integral curve coinciding with the path. This is not always convenient.

More fatally, even if two different vector fields have a completely coinciding integral curve—even so, the results of the movement may not be the same.

That is, $(\Phi^{V}\_{Q\rightarrow P})^\*$ and $(\Phi^{W}\_{Q\rightarrow P})^\*$ are generally different, even if the paths are exactly the same.

In other words, the Lie derivative at a certain point about vector field $V$ depends on the properties of $V$ in the neighborhood of that point. This is why we say "the covariant derivative has $\mathcal{F}$-linearity in $V$, while the Lie derivative does not".

Therefore, we prefer a method that allows us to arbitrarily move tensors directly without needing to find an integral curve first, as in the Lie derivative. In this method, we are the rule makers—meaning the rules of tensor movement are determined by us and do not require any local structure of the vector field.

Given a local coordinate system, such an artificial rule can be characterized by a set of data called Christoffel symbols $\Gamma^i\_{jk}$:

$\nabla\_{k} e\_j =: \Gamma^i\_{jk}e\_i, \quad \nabla\_i := \nabla\_{e\_i}$ 

The three subscripts of $\Gamma^i\_{jk}$ mean: $k$ represents the direction along the $k$-th basis vector, $j$ indicates the basis vector we are considering, and $i$ represents the component of the change along the $i$-th basis vector.


> However, such a set of data is too arbitrary: for an n-dimensional manifold, we need $n^3$ numbers to determine the Christoffel symbols.  
>   
> To be specific, we can use an additional structure on the manifold—metric. We hope the covariant derivative is metric-preserving, i.e., satisfies $ \nabla\_k g\_{ij}=0 $, which can give $n^2(n+1)/2$ constraints, leaving $n^3-n^2(n+1)/2=n^2(n-1)/2$ degrees of freedom.  
>   
> We can also obtain the remaining $n^2(n-1)/2$ constraints by requiring the covariant derivative to be torsion-free, thus eliminating arbitrariness and obtaining a unique connection. This is the Riemann / Levi-Civita connection.

Thus, we can use the fact that the covariant derivative is zero to define "parallel transport".

Since the rules of parallel transport are artificially specified, the covariant derivative does not depend on the neighborhood of the vector field, so **the covariant derivative has $\mathcal{F}$-linearity in $V$**.

### 2.3 Back to Lie Derivative
Of course, this does not mean that the Lie derivative is useless. The significance of the Lie derivative lies not in moving tensors but in characterizing the properties of "flows". For example, the divergence can be defined by the action of the Lie derivative on the unit volume form:

$\begin{aligned}  \mathcal{L}\_V \omega\_g =: (\operatorname{div} V)\omega\_g  \end{aligned}$ 

The geometric meaning is also very clear: if we let a small volume on the manifold flow a small distance along the integral curve of the vector field, the scaling ratio of this small volume is the divergence of the vector field at that point.

The Lie derivative provides a more elegant language for defining many concepts. If the divergence is not defined by the Lie derivative, it can only be defined as $\operatorname{div} V = \star\_g \mathrm{d} \star\_g \flat\_g V$, involving the raising and lowering operators, Hodge star operator, exterior differential operator, which at first glance looks like an indescribable object.

Moreover, torsion, curvature, etc., can all be given beautiful (and coordinate-independent) definitions using the Lie derivative, as mentioned in the existing answers and won't be repeated here.

Additionally, as the name suggests, the Lie derivative has deep connections with Lie groups and Lie algebras. The Lie derivative can be used to prove that the Lie bracket of left-invariant vector fields is also a left-invariant vector field, thus inducing a Lie bracket on the tangent space, making the tangent space a Lie algebra.

## III. Explicit Formulas  
Finally, let's compare the explicit formulas of Lie derivative and covariant derivative:

> Lie derivative:  
>   
>  $ \begin{aligned} (\mathcal{L}\_V A)^{i...j}\_{k...l} &= V^m A^{i...j}\_{k...l,m} + \\\\ &+ V^m\_{,k} A^{i...j}\_{m...l} + \cdots + V^m\_{,l} A^{i...j}\_{k...m} \\\\ &- V^i\_{,m}A^{m...j}\_{k...l} + \cdots - V^j\_{,m} A^{i...m}\_{k...l} \end{aligned} $   
>   
>  Covariant derivative:  
>   
> $ \begin{aligned} (\nabla\_V A)^{i...j}\_{k...l} & = V^{m} A^{i...j}\_{k...l,m} \\\\  & - \Gamma^{n}\_{km} V^{m} A^{i...j}\_{n...l} - \cdots - \Gamma^{n}\_{lm} V^m A^{i...j}\_{k...n} \\\\ & + \Gamma^{i}\_{nm} V^{m} A^{n...j}\_{k...l} + \cdots + \Gamma^{j}\_{nm} V^m A^{i...n}\_{k...l} \end{aligned} $  
>   
> In the formula, a comma with a subscript indicates partial differentiation, i.e., $A\_{,k}:=\frac{\partial}{\partial k}A$.

From the formulas, it can be seen that the Lie derivative $\mathcal{L}\_V$ at a point depends on the properties of $V$ in the neighborhood of that point because it involves the partial derivatives of the components of the vector field $V^m\_{,k}$.

In the covariant derivative, only the components of the vector field $V^m$ appear, not the partial derivatives of the components $V^m\_{,k}$. This means that the covariant derivative does not depend on the neighborhood. This is why the covariant derivative has $\mathcal{F}$-linearity, while the Lie derivative does not.
