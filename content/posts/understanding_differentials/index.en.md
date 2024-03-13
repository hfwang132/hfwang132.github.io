---
title: "Understanding differentials in four levels"
date: 2024-03-13T18:41:18+08:00
draft: false
tags: ["Differential Geometry"]
categories: ["Mathematical Physics"]
---

## One Differential is an Infinitesimal?

Physicists like to think of differentials as very small quantities, which is convenient for calculations but gives a feeling of lack of rigor.

In fact, it is indeed lacking rigor, and the second mathematical crisis arose from this.

Rigor and clarity are always complementary. Treating differentials as infinitesimal satisfies intuition but cannot withstand rational scrutiny.

---

## Two Differential as Linear Function

I like to think of differentials as a machine, for example,

$f: f(x,y)=x^2+2y^2$ 

The differential at $(1,1)$ is a machine like this:

{{< figure src="image/machine.jpg" title="" >}}

It takes two numbers as input and produces one number as output.

Written out, it looks like this:

$\mathrm{d}f|\_{(1,1)}(a,b)=\frac{\partial f}{\partial x}\bigg|\_{(1,1)}a+\frac{\partial f}{\partial y}\bigg|\_{(1,1)}b=2a+4b$ 

Since the partial derivatives may vary at each point, if we say the differential at a certain point is a machine, then the differentials collectively form an ocean of machines.

You may also notice that this machine is "linear"; it is simply a linear map from $\mathbb{R}^2$ to $\mathbb{R}$.

---

The knowledge of linear algebra tells us that the collection of linear functions forms a linear space. In other words, linear functions themselves are "vectors" that can be added and scaled.

Going back to the analogy above, it means we can add two machines: $\mathrm{d}f|\_p+\mathrm{d}g|\_p$ ,

and also scale a machine by a factor: $\lambda \cdot \mathrm{d}f|\_p $ .

The subscript $p$ indicates the differential at point $p$.

What does it mean to add machines? For example, if

$\mathrm{d}f|\_p(a,b)=2a+4b,\,\, \mathrm{d}g|\_p(a,b)=a-b$ ,

then $\mathrm{d}f|\_p(a,b)+\mathrm{d}g|\_p(a,b)=3a+3b$ .

This is similar to adding two vectors: $(2,4)+(1,-1)=(3,3)$ .

In fact, they are vectors. Yes, you heard it right, differentials are vectors (fields).

---

## Three Differential as Covector Field

### 3.1 Tangent Space

If you want to study differentials on a curved surface, then you need to redefine some concepts. For example, differentials are linear, but manifolds are curved, so we need to define something linear within this curvature. This linear thing is the tangent space.

As the name suggests, the tangent space is a tangent plane to a curved surface at a certain point. But how do we define it? The curvature here is not embedded in another space but intrinsic to space itself. We cannot find the equation of a tangent plane as in classical analytic geometry.

Let's try a different approach:

Firstly, it is linear, which means it is a vector space.

> A vector space is a group equipped with scalar multiplication. Specifically, its elements (called vectors) satisfy the following properties:  
> *(1) Commutativity of vector addition*  
> *(2) Associativity of vector addition*  
> *(3) Existence of an identity element for vector addition (similar to zero)*  
> *(4) Existence of an inverse element for vector addition (similar to the negative number)*  
> *The above four properties indicate that the vector space is an abelian group with respect to vector addition.*  
> *(5) Existence of a multiplicative identity for scalar multiplication*  
> *(6) Associativity of scalar multiplication*  
> *(7) Distributivity of scalar multiplication with respect to vector addition*  
> *(8) Distributivity of scalar multiplication with respect to scalar addition*

A vector space does not have to be $\mathbb{R}^n,\,\mathbb{C}^n$, as long as a set is defined with addition and scalar multiplication operations satisfying the above properties, it is a vector space.

We can define such a vector space, where the elements are linear maps from a set of smooth functions to the real number field:

> $v:\mathcal{F}\_M\rightarrow\mathbb{R}$ such that  
> *(1) $v(\lambda f+\mu g)=\lambda v(f)+\mu v(g)$ (linearity)*  
> *(2) $v|\_p(f\cdot g)=f|\_p\cdot v(g)+g|\_p\cdot v(f)$ (Leibniz law)*  
> where $\mathcal{F}\_M$ is the set of all smooth functions on the differential manifold $M$.

It can be proven that the collection of $v$ forms a vector space.

Although this definition seems complicated, it is actually just finding the directional derivative of a function at a certain point.

Taking a bivariate function as an example, we can explicitly write out an instance of $v$: $\left(a\frac{\partial}{\partial x}+b\frac{\partial}{\partial y}\right)\bigg|\_p$ 

If $(\frac{\partial}{\partial x}\bigg|\_p,\frac{\partial}{\partial y}\bigg|\_p)$ is taken as the basis, then its coordinates are $(a,b)$.

This linear space is the tangent space at point $p$ on the manifold, denoted as $T\_pM$.

All these operations are at a certain point $p$, where each point grows a tangent space. You can imagine that every point on a curved surface grows a tangent plane.

---

### 3.2 Cotangent Space

We just introduced the tangent space $T\_p M$ . Now let's call the dual space of the tangent space $T\_p^\*M$ the *cotangent space*.

The differential at a point is precisely an element in the cotangent space. In other words, the differential at a certain point is a cotangent vector.

Elements in the dual space (cotangent vectors) are linear functionals that map elements in the original space to a number. This is exactly what we said before about machines:

{{< figure src="image/machine.jpg" title="" >}}

But now the input should be elements in the tangent space: $\left(a\frac{\partial}{\partial x}+b\frac{\partial}{\partial y}\right)\bigg|\_p$ .

We said that differentials form an ocean of machines. Therefore, the ocean of cotangent vectors (i.e., differentials) can be called the cotangent vector field.

In mathematics, the differential (cotangent vector field) has a cool name called the cotangent bundle projection. For more details, see:

[https://zhuanlan.zhihu.com/p/629852598](https://zhuanlan.zhihu.com/p/629852598)  


---

After talking so much abstract nonsense, let's define it below:

The differential at a point $p$ on manifold $M$ is such a

 linear functional that acts on elements $v|\_p\in T\_pM$ in the tangent space and produces $\mathrm{d}f|\_p(v|\_p)=v|\_p(f)$ 

Let's take a more explicit example, for a bivariate function:

$\mathrm{d}f|\_{p}:\mathrm{d}f|\_{p}(v|\_p)=v|\_p(f)=  \frac{\partial f}{\partial x} \bigg|\_{p} a+\frac{\partial f}{\partial y}\bigg|\_{p}b$ , where $v|\_p=\left(a\frac{\partial}{\partial x}+b\frac{\partial}{\partial y}\right)\bigg|\_p$ 

## Four Differential as Linear Mapping Characterized by Jacobian Matrix

So far, we have discussed functions that map to domains $\mathbb{R},\mathbb{C}, \cdots$. What if the target domain can be $\mathbb{R}^2, \mathbb{R}^3,\cdots$?

For example, $\bm{f}:\mathbb{R}^n\rightarrow\mathbb{R}^m$ .

In this case, $\bm{f}$ can be seen as $m$ functions:

$f\_i:\mathbb{R}^n\rightarrow\mathbb{R},\,\,i=1,\cdots,m$ 

Then we have

$\begin{bmatrix}\mathrm{d}f\_1 \\\\ \mathrm{d}f\_2 \\\\ \vdots \\\\ \mathrm{d}f\_m \end{bmatrix}= \begin{bmatrix} \frac{\partial f\_1}{\partial x\_1}&\frac{\partial f\_1}{\partial x\_2}&\cdots&\frac{\partial f\_1}{\partial x\_n} \\\\ \frac{\partial f\_2}{\partial x\_1}&\frac{\partial f\_2}{\partial x\_2}&\cdots&\frac{\partial f\_2}{\partial x\_n} \\\\ \vdots&\vdots&\ddots&\vdots \\\\ \frac{\partial f\_m}{\partial x\_1}&\frac{\partial f\_m}{\partial x\_2}&\cdots&\frac{\partial f\_m}{\partial x\_n} \end{bmatrix}\begin{bmatrix}\mathrm{d}x\_1 \\\\ \mathrm{d}x\_2 \\\\ \vdots \\\\ \mathrm{d}x\_n \end{bmatrix}$

where $\begin{bmatrix} \frac{\partial f\_1}{\partial x\_1}&\frac{\partial f\_1}{\partial x\_2}&\cdots&\frac{\partial f\_1}{\partial x\_n} \\\\ \frac{\partial f\_2}{\partial x\_1}&\frac{\partial f\_2}{\partial x\_2}&\cdots&\frac{\partial f\_2}{\partial x\_n} \\\\ \vdots&\vdots&\ddots&\vdots \\\\ \frac{\partial f\_m}{\partial x\_1}&\frac{\partial f\_m}{\partial x\_2}&\cdots&\frac{\partial f\_m}{\partial x\_n} \end{bmatrix}$ is the **Jacobian matrix**.

In fact, the differential is the linear mapping characterized by the Jacobian matrix. Below, we explain in detail.

---

For a univariate function, the Jacobian matrix is just the derivative.

Although we are used to thinking of derivatives as slopes, let's change our perspective: If you consider the action of a univariate function as stretching along the number line, then the derivative is the local stretching ratio. The advantage of this perspective is its ease of generalization to multivariate functions.

Because, for multivariate functions, you often cannot draw a curve as you would for univariate functions. So, as an alternative method, you can think of a multivariate function as a space being stretched, such as $f: R^2→R^2$. You can imagine that each point in $R^2$ is stretched to a new point by $f$.

If you zoom in on this local stretch, it looks like the case of a univariate function—linear—parallel lines are stretched to parallel lines.

And what we call the differential is precisely this local linear mapping! The matrix of this linear mapping is the Jacobian matrix.

For more detailed explanations, see lectures 71-72 of Khan Academy's Multivariable Calculus course:

[https://www.youtube.com/watch?v=bohL918kXQk](https://www.youtube.com/watch?v=bohL918kXQk)  
