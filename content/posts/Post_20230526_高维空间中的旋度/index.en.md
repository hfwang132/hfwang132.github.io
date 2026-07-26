---
title: "What Is Curl in Higher-Dimensional Spaces?"
date: 2023-05-26T21:00:37+08:00
originalURL: "https://zhuanlan.zhihu.com/p/632513066"
aliases:
  - "/en/curl_in_n_dimension/"
  - "/en/Post_20230610_高维空间中的旋度/"
draft: false
categories: ["Mathematical methods of physics"]
tags: ["Vector calculus"]
math: true
author: "Haifei"
---

### Differential Forms  

Before introducing curl, we must first introduce differential forms and the exterior derivative operator.

An n-form can be defined as an alternating multilinear map \(\omega:(T_pM)^n\rightarrow \mathbb{R}\) . It maps multiple vectors to a real number. Moreover, it satisfies alternation: exchanging two input vectors introduces an additional minus sign in the output.

Thus, an n-form can be explicitly defined as follows:  
\[\omega^1\wedge \omega^2\wedge\cdots\wedge \omega^n(v_1,v_2,\cdots,v_n)= \begin{vmatrix} \omega^1(v_1) & \cdots & \omega^{1}(v_n) \\ \vdots & \ddots & \vdots \\ \omega^n(v_1) & \cdots  & \omega^n(v_n) \end{vmatrix}\in\mathbb{R}\]

The set of all n-forms on \(T_pM\) can be written as \(\bigwedge^n(T^*_pM)\) .

As for “differential forms,” the difference between them and “forms” is that they are “fields of forms”: every point on the manifold corresponds to a form at that point. In other words, a “form” is relative to a particular point, whereas a “differential form” is relative to the entire manifold.

### Exterior Derivative  

The exterior derivative operator is defined as follows:

The exterior derivative operator is a map \(\mathrm{d}: \bigwedge^n(T_p^*M)\rightarrow \bigwedge^{n+1}(T_p^*M)\) that acts on an n-form: \(\varphi=\sum_{I}f_I\mathrm{d}x^{I}=\sum_{(i_1,\cdots,i_n)}f_{(i_1,\cdots,i_n)}\mathrm{d}x^{i_1}\wedge\cdots\wedge\mathrm{d}x^{i_n}\), yielding an (n+1)-form:

\(\mathrm{d}\varphi=\sum_{I}\sum_{i}\frac{\partial f_I}{\partial x_i}\mathrm{d}x_i\wedge x_I\).

> **Comment** This pile of indices is far too ugly; it is better to look at the example below.   
>   
> **Example**  For a 2-form on a 3-dimensional manifold: \(\varphi=z^2\mathrm{d}x\wedge\mathrm{d}y+x\sin y\,\mathrm{d}y\wedge \mathrm{d}z\), its exterior derivative is: \[\begin{aligned} \mathrm{d}\varphi   &=\left(\frac{\partial z^2}{\partial x}\mathrm{d}x+\frac{\partial z^2}{\partial y}\mathrm{d}y+\frac{\partial z^2}{\partial z}\mathrm{d}z\right)\wedge\mathrm{d}x\wedge\mathrm{d}y  \\&  +\left(\frac{\partial (x\sin y)}{\partial x}\mathrm{d}x+\frac{\partial (x\sin y)}{\partial y}\mathrm{d}y+\frac{\partial (x\sin y)}{\partial z}\mathrm{d}z\right)\wedge\mathrm{d}y\wedge\mathrm{d}z  \\&=(2z+\sin y)\,\mathrm{d}x\wedge\mathrm{d}y\wedge\mathrm{d}z  \end{aligned}\]

### Curl  

In the following example, we will show the relationship between curl and the exterior derivative:

Example: On a three-dimensional manifold, after the exterior derivative operator \(\mathrm{d}\) acts on a 1-form, it yields a 2-form:   
  
 \[\begin{aligned} \mathrm{d}(f_i\mathrm{d}x^i)&=\frac{\partial f_1}{\partial x^1}\mathrm{d}x^1\wedge\mathrm{d}x^1+\frac{\partial f_1}{\partial x^2}\mathrm{d}x^2\wedge\mathrm{d}x^1+\frac{\partial f_1}{\partial x^3}\mathrm{d}x^3\wedge\mathrm{d}x^1 \\&+\frac{\partial f_2}{\partial x^1}\mathrm{d}x^1\wedge\mathrm{d}x^2+\frac{\partial f_2}{\partial x^2}\mathrm{d}x^2\wedge\mathrm{d}x^2+\frac{\partial f_2}{\partial x^3}\mathrm{d}x^3\wedge\mathrm{d}x^2 \\&+\frac{\partial f_3}{\partial x^1}\mathrm{d}x^1\wedge\mathrm{d}x^3+\frac{\partial f_3}{\partial x^2}\mathrm{d}x^2\wedge\mathrm{d}x^3+\frac{\partial f_3}{\partial x^3}\mathrm{d}x^3\wedge\mathrm{d}x^3 \end{aligned}\]   
  
Applying the Hodge star operator once to it yields a 1-form:   
  
\[\begin{aligned} \star \mathrm{d}(f_i\mathrm{d}x^i)&=\phantom{+\frac{\partial f_1}{\partial x^2}\mathrm{d}x^3}-\frac{\partial f_1}{\partial x^2}\mathrm{d}x^3+\frac{\partial f_1}{\partial x^3}\mathrm{d}x^2 \\&\phantom{=}+\frac{\partial f_2}{\partial x^1}\mathrm{d}x^3 \phantom{\,\,\,\,-\frac{\partial f_1}{\partial x^2}\mathrm{d}x^3}  -\frac{\partial f_2}{\partial x^3}\mathrm{d}x^1 \\&\phantom{=}-\frac{\partial f_3}{\partial x^1}\mathrm{d}x^2+\frac{\partial f_3}{\partial x^2}\mathrm{d}x^1  \\&=\left(\frac{\partial f_3}{\partial x^2}-\frac{\partial f_2}{\partial x^3}\right)\mathrm{d}x^1 + \left(\frac{\partial f_1}{\partial x^3}-\frac{\partial f_3}{\partial x^1}\right)\mathrm{d}x^2 + \left(\frac{\partial f_2}{\partial x^1}-\frac{\partial f_1}{\partial x^2}\right)\mathrm{d}x^3  \end{aligned}\]   
  
It can be written as the inner product of the curl and a tangent vector: \(\star\mathrm{d}f:\star\mathrm{d}f(v)=\langle \nabla \times f^{\sharp}\mid v \rangle\)   
  
We will not introduce the Hodge star operator for now. At present, you only need to know that on a 3-dimensional manifold, the Hodge operator maps an n-form to a (3-n)-form.  
  
Specifically, if equipped with an inner product \(\langle\mathrm{d}x^i,\mathrm{d}x^j\rangle=\delta^{j}_i\), then:   
 \(\star(\mathrm{d}x^i \wedge \mathrm{d}x^j)=\mathrm{d}x^k\) ,  
 \(\star\mathrm{d}x^i =\mathrm{d}x^j\wedge \mathrm{d}x^k\) ,   
 \(\star(f\,\mathrm{d}x^i \wedge\mathrm{d}x^j\wedge \mathrm{d}x^k)=f\) ,  
 \[\star f=f \,\mathrm{d}x^i \wedge\mathrm{d}x^j\wedge \mathrm{d}x^k\]   
where \((i,j,k)\) is an even permutation of \((1,2,3)\).   
  
In addition, note that we used a superscript: \(\sharp\) . This is because curl acts on tangent vector fields rather than cotangent vector fields.  
  
Specifically, curl \(\nabla\times\) maps a tangent vector field to a tangent vector field: \(\Gamma(TM)\rightarrow \Gamma(TM)\) . However, \(f\in \Gamma(T^*M)\) is a cotangent vector field (a 1-form), so we must first “raise” it to a tangent vector field: \(f^\sharp\in \Gamma(TM)\) . This is precisely the raising and lowering of indices beloved by physicists: \(g^{ij}X_i=X^j\) . Likewise, \(\flat\) denotes “lowering” a tangent vector field to a cotangent vector field: \(g_{ij}X^i=X_j\) .  
  
 Returning to the example above, we have a canonical isomorphism induced by the inner product:  
  
 \[\sharp:\star \mathrm{d}f\mapsto \nabla\times f^{\sharp}\]   
or equivalently: \((\star \mathrm{d}f)^\sharp = \nabla\times f^{\sharp}\)   
or equivalently: \(\star \mathrm{d}f(v) = \langle\nabla\times f^{\sharp}\mid v\rangle\)   
  
where \( f\) is a 1-form.   
  
We can also write: \(\nabla\times F=(\star \mathrm{d} (F^{\flat}))^{\sharp}\)   
  
where \(F=f^\sharp\) is a tangent vector field, and \(f\) is a cotangent vector field (a 1-form).

Inspired by the example above, we can define curl as

\[\begin{aligned} (\nabla\times) :\quad & \Gamma(TM)\rightarrow \Gamma\left(\bigwedge^{n-2}TM\right)\\ &F\mapsto(\star \mathrm{d} (F^{\flat}))^{\sharp} \end{aligned}\]

where \(F\) is a tangent vector field; \(F^{\flat}\) is a cotangent vector field (a 1-form); \( \mathrm{d} (F^{\flat})\) is a 2-form, and \(\star \mathrm{d} (F^{\flat})\) is an \((n-2)\)-form.

**Therefore, the curl** \(n\) **of a tangent vector field** \(F\) **on an** \((\star \mathrm{d} (F^{\flat}))^{\sharp}\) **-dimensional manifold is an antisymmetric tensor field of type** \((n-2,0)\)**. Or equivalently, an (n-2)-vector field.**

On a 3-dimensional manifold, curl degenerates into a tangent vector field. On a 2-dimensional manifold, curl degenerates into a scalar field.
