# Curl in high dimension


### 1 Differential Forms

Before introducing the concept of curl, we need to first introduce differential forms and the exterior derivative.

An n-form can be defined as an alternating multilinear mapping $\omega:(T_p^\*M)^n\rightarrow \mathbb{R}$. It maps multiple vectors to a real number. Additionally, it satisfies the alternating property, meaning that exchanging two input vectors results in an output multiplied by a negative sign.

Therefore, an n-form can be explicitly defined as follows:

$$
\omega^1\wedge \omega^2\wedge\cdots\wedge \omega^n(v_1,v_2,\cdots,v_n)= \begin{vmatrix} \omega^1(v_1) & \cdots & \omega^{1}(v_n) \\\\\\ \vdots & \ddots & \vdots \\\\\\ \omega^n(v_1) & \cdots & \omega^n(v_n) \end{vmatrix}\in \mathbb{R}
$$

The set of all n-forms on $T_p^\*M$ can be written as $\bigwedge\_n(T_p^\*M)$.

As for "differential forms," they differ from "forms" in that they are the "forms' fields," meaning that at each point on the manifold, there resides a form. In other words, "forms" are specific to a point, while "differential forms" are specific to the entire manifold.

### 2 Exterior Derivative

The definition of the exterior derivative is as follows:

The exterior derivative is a mapping $\mathrm{d}: \bigwedge^n(T_p^\*M) \rightarrow \bigwedge^{(n+1)}(T_p^\*M)$, which acts on an differential n-form: $\varphi = \sum_I f_I \mathrm{d}x^I = \sum_{(i_1,\cdots,i_n)} f_{(i_1,\cdots,i_n)} \mathrm{d}x^{i_1}\wedge\cdots\wedge\mathrm{d}x^{i_n}$, and yields an differential (n+1)-form:

$\mathrm{d}\varphi = \sum_I \sum_i \frac{\partial f_I}{\partial x_i} \mathrm{d}x_i\wedge x_I$.

> **Comment** These indices are quite all over the place. Let's see the example below instead.
> 
> **Example** For a differential 2-form on a 3-dimensional manifold: $\varphi = z^2\mathrm{d}x\wedge\mathrm{d}y + x\sin y\\,\mathrm{d}y\wedge \mathrm{d}z$, its exterior derivative is given by: $$\begin{aligned} \mathrm{d}\varphi &= \left(\frac{\partial z^2}{\partial x}\mathrm{d}x + \frac{\partial z^2}{\partial y}\mathrm{d}y + \frac{\partial z^2}{\partial z}\mathrm{d}z\right)\wedge\mathrm{d}x\wedge\mathrm{d}y \\\\\\ & + \left(\frac{\partial (x\sin y)}{\partial x}\mathrm{d}x + \frac{\partial (x\sin y)}{\partial y}\mathrm{d}y + \frac{\partial (x\sin y)}{\partial z}\mathrm{d}z\right)\wedge\mathrm{d}y\wedge\mathrm{d}z \\\\\\ &= (2z + \sin y)\\,\mathrm{d}x\wedge\mathrm{d}y\wedge\mathrm{d}z \end{aligned} $$

### 3 Curl in N Dimensions

In the following example, we will explore the relationship between curl and exterior derivative:

> **Example**: On a three-dimensional manifold, when the exterior derivative operator $\mathrm{d}$ acts on a 1-form, it yields a 2-form:
> 
> $$
> \begin{aligned}
> \mathrm{d}(f_i\mathrm{d}x^i) &= \frac{\partial f_1}{\partial x^1}\mathrm{d}x^1\wedge\mathrm{d}x^1 + \frac{\partial f_1}{\partial x^2}\mathrm{d}x^2\wedge\mathrm{d}x^1 + \frac{\partial f_1}{\partial x^3}\mathrm{d}x^3\wedge\mathrm{d}x^1 \\\\
> &\quad+ \frac{\partial f_2}{\partial x^1}\mathrm{d}x^1\wedge\mathrm{d}x^2 + \frac{\partial f_2}{\partial x^2}\mathrm{d}x^2\wedge\mathrm{d}x^2 + \frac{\partial f_2}{\partial x^3}\mathrm{d}x^3\wedge\mathrm{d}x^2 \\\\
> &\quad+ \frac{\partial f_3}{\partial x^1}\mathrm{d}x^1\wedge\mathrm{d}x^3 + \frac{\partial f_3}{\partial x^2}\mathrm{d}x^2\wedge\mathrm{d}x^3 + \frac{\partial f_3}{\partial x^3}\mathrm{d}x^3\wedge\mathrm{d}x^3
> \end{aligned}
> $$
> 
> Applying the Hodge star operator once, it yields a 1-form:
> 
> $$
> \begin{aligned}
> \star \mathrm{d}(f_i\mathrm{d}x^i) &= \phantom{+\frac{\partial f_1}{\partial x^2}\mathrm{d}x^3} -\frac{\partial f_1}{\partial x^2}\mathrm{d}x^3 + \frac{\partial f_1}{\partial x^3}\mathrm{d}x^2 \\\\
> &\phantom{=}+ \frac{\partial f_2}{\partial x^1}\mathrm{d}x^3 \phantom{\\,\\,\\,-\frac{\partial f_1}{\partial x^2}\mathrm{d}x^3} -\frac{\partial f_2}{\partial x^3}\mathrm{d}x^1 \\\\
> &\phantom{=} -\frac{\partial f_3}{\partial x^1}\mathrm{d}x^2 + \frac{\partial f_3}{\partial x^2}\mathrm{d}x^1 \\\\
> &= \left(\frac{\partial f_3}{\partial x^2}-\frac{\partial f_2}{\partial x^3}\right)\mathrm{d}x^1 + \left(\frac{\partial f_1}{\partial x^3}-\frac{\partial f_3}{\partial x^1}\right)\mathrm{d}x^2 + \left(\frac{\partial f_2}{\partial x^1}-\frac{\partial f_1}{\partial x^2}\right)\mathrm{d}x^3
> \end{aligned}
> $$
> 
> It can be expressed as the inner product of the curl and a tangent vector: $\star\mathrm{d}f:\star\mathrm{d}f(v)=\langle \nabla \times f^{\sharp}\mid v \rangle$
> 
> For now, without introducing the Hodge star operator, you only need to know that on a three-dimensional manifold, the Hodge operator applied to an differential n-form yields an differential (3-n)-form.
> 
> Specifically, if the manifold is equipped with an inner product $\langle\mathrm{d}x^i,\mathrm{d}x^j\rangle=\delta^{j}\_i$, then we have:
> $$
> \star(\mathrm{d}x^i \wedge \mathrm{d}x^j) = \mathrm{d}x^k
> $$
> $$\star\mathrm{d}x^i = \mathrm{d}x^j\wedge \mathrm{d}x^k$$
> $$\star(f\\, \mathrm{d}x^i \wedge\mathrm{d}x^j\wedge \mathrm{d}x^k) = f$$
> $$\star f = f\mathrm{d}x^i \wedge\mathrm{d}x^j\wedge \mathrm{d}x^k$$
> where $(i,j,k)$ is an even permutation of $(1,2,3)$.
> 
> Also, note that we use a raised symbol: $\sharp$. This is because the curl operates on tangent vector fields, not cotangent vector fields.
> 
> Specifically, the curl $\nabla\times$ maps a tangent vector field to another tangent vector field: $\Gamma(TM)\rightarrow \Gamma(TM)$. However, $f\in \Gamma(T^*M)$ is a cotangent vector field (a 1-form), so we first need to "raise" it to a tangent vector field: $f^\sharp\in \Gamma(TM)$. This is actually the well-known index raising and lowering in physics: $g^{ij}X_i=X^j$. Similarly, $\flat$ represents lowering a tangent vector field to a cotangent vector field: $g_{ij}X^i=X_j$.
> 
> Returning to the previous example, we have a canonical isomorphism induced by the inner product:
> 
> $$
> \sharp: \star \mathrm{d}f \mapsto \nabla\times f^\sharp
> $$
> or written as:
> $$
> (\star \mathrm{d}f)^\sharp = \nabla\times f^\sharp
> $$
> or written as:
> $$
> \star \mathrm{d}f(v) = \langle\nabla\times f^\sharp\mid v\rangle
> $$
> 
> where $f$ is a 1-form.
> 
> We can also write it as: $\nabla\times F=(\star \mathrm{d} (F^\flat))^\sharp$
> 
> where $F=f^\sharp$ is a tangent vector field, and $f$ is a cotangent vector field (a 1-form).

Inspired by the above example, we can define the curl as:

$$
\begin{aligned}
(\nabla\times) : \quad & \Gamma(TM)\rightarrow \Gamma\left(\bigwedge^{n-2}TM\right) \\\\
& F \mapsto (\star \mathrm{d} (F^\flat))^\sharp
\end{aligned}
$$

where $F$ is a tangent vector field, $F^\flat$ is a cotangent vector field (a 1-form), $\mathrm{d} (F^\flat)$ is a 2-form, and $\star \mathrm{d} (F^\flat)$ is an differential (n-2)-form.

**Therefore, the curl of a tangent vector field $F$ on an $n$-dimensional manifold, denoted as $(\star \mathrm{d} (F^\flat))^\sharp$, is an $(n-2,0)$-type antisymmetric tensor field, or simply an $(n-2)$-vector field.**

In a three-dimensional manifold, the curl reduces to a tangent vector field. In a two-dimensional manifold, the curl reduces to a scalar field.



