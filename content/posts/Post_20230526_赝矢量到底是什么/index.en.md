---
title: "What Exactly Is a Pseudovector?"
date: 2023-05-26T18:11:03+08:00
originalURL: "https://zhuanlan.zhihu.com/p/632488326"
aliases:
  - "/en/pseudovectors/"
  - "/en/Post_20230610_赝矢量到底是什么/"
draft: false
tags: ["Exterior algebra"]
categories: ["Mathematical methods in physics"]
math: true
author: "Haifei"
---

In physics books, we often encounter the terms “pseudovector” (pseudo-vector) and “pseudoscalar” (pseudo-scalar).

In fact, on a 3-dimensional manifold, a “pseudovector” is the exterior product of two tangent vectors \(v\in T_pM\wedge T_pM=\bigwedge^2(T_pM)\), while a “pseudoscalar” is the exterior product of three tangent vectors \(s\in T_pM\wedge T_pM\wedge T_pM=\bigwedge^3(T_pM)\).

After equipping the space with an inner product (or a nondegenerate bilinear form), there is a Hodge duality relation between \(\bigwedge^2(T_pM)\) and \(\bigwedge^1(T_pM)\), so we “mistakenly regard” pseudovectors as vectors. Similarly, because there is a Hodge duality relation between \(\bigwedge^3(T_pM)\) and \(\bigwedge^0(T_pM)\) (a scalar field), we “mistakenly regard” pseudoscalars as scalars.

In fact, mathematically, a pseudovector on a 3-dimensional manifold is a 2-vector (bivector, 2-vector). Its definition is analogous to that of a 2-form, except that a 2-vector lies in the exterior product of the tangent space \(v\in\bigwedge^2(T_pM)\), whereas a 2-form lies in the exterior product of the cotangent space \(\omega\in\bigwedge^2(T_p^*M)\).

---

Recall that the reason we call “pseudovectors” “pseudovectors” is that they exhibit strange behavior under spatial inversion. But if you regard one as the exterior product of two vectors, all of this strange behavior can be explained.

Specifically, look at the figure below: under spatial inversion, the magnetic field actually reverses direction! This is like moving in one direction while your reflection in the mirror moves in the other direction. One has to admit that this is a paranormal event.

{{< figure src="images/v2-150afa97add22c5c168c9e770fed9873_r.jpg" >}}

A magnetic field is a bivector. If you regard the magnetic field as a vector, the paranormal phenomenon shown in the figure appears: the magnetic field looks into a mirror and finds that its head has turned into its feet.

  
  

But in fact, the magnetic field at point \(p\) on the manifold \(M\) is not a vector, but a bivector. That is, \(B|_p\in (T_pM)\wedge (T_pM)\). Its basis is \(\frac{\partial}{\partial x}\wedge \frac{\partial}{\partial y},\,\frac{\partial}{\partial y}\wedge \frac{\partial}{\partial z},\,\frac{\partial}{\partial z}\wedge \frac{\partial}{\partial x}\).

Thus, there is no paranormal event at all (welcome to *Approaching Science*). Under spatial inversion, the two vectors corresponding to the magnetic field each point in the correct direction; it is merely because humans insist on using the right-hand screw rule to regard a bivector as a vector that this bizarre phenomenon arises.

Although bivectors have a rigorous mathematical definition, we still want to ask: how should a bivector be drawn? The answer is: a bivector can be drawn as an oriented surface element. Surface elements of different shapes refer to the same bivector as long as they are parallel to each other and have the same area. In other words, the same bivector can be depicted in many different ways, provided that they are parallel and have the same area and orientation.

{{< figure src="images/v2-8eaa2d066145c8fa7f4f4336286f4062_1440w.jpg" >}}

Parallel surface elements with the same area and orientation correspond to the same bivector.

  
  

In fact, regarding a bivector as a vector through the right-hand screw rule is possible only on a three-dimensional manifold. This is because only on a three-dimensional manifold does three minus two happen to equal one. On a four-dimensional manifold, since four minus two equals two, we can only dualize a bivector into another bivector, rather than into a vector.

On a five-dimensional manifold, a bivector can be dualized into a trivector; ..., on an n-dimensional manifold, a bivector can be dualized into an (n-2)-vector.

---

Incidentally, the electric field is also a bivector, with basis \(\frac{\partial}{\partial t}\wedge \frac{\partial}{\partial x},\,\frac{\partial}{\partial t}\wedge \frac{\partial}{\partial y},\,\frac{\partial}{\partial t}\wedge \frac{\partial}{\partial z}\), and it has one time dimension. The reason it does not appear to be a “pseudovector” is that we consider only spatial inversion and not time reversal.

If we consider the electromagnetic 2-form in the cotangent space (using natural units):

\[\begin{align} F&=E_x\mathrm{d}t\wedge\mathrm{d}x+E_y\mathrm{d}t\wedge\mathrm{d}y+E_z\mathrm{d}t\wedge\mathrm{d}z\\ &+B_x \mathrm{d}y\wedge\mathrm{d}z + B_y \mathrm{d}z\wedge\mathrm{d}x + B_z\mathrm{d}x\wedge\mathrm{d}y \end{align}\]

Since we can freely raise or lower the indices of a tensor using the metric tensor, by raising the indices in the above expression, we can also write an electromagnetic tensor of type \((2,0)\), whose basis is the exterior products of \(\frac{\partial}{\partial t},\frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z}\).

For now, however, we adopt an antisymmetric tensor (differential form) of type \((0,2)\), because this allows us to use the exterior derivative (Exterior Derivative) \(\mathrm{d}\).

Now consider the current 1-form: \(J=-\rho\mathrm{d}t+J_x\mathrm{d}x+J_y\mathrm{d}y+J_z\mathrm{d}z\)

Then, under the Minkowski metric \(\text{diag}(-1,1,1,1)\), Maxwell's equations can be written in a very concise form:

\[\left\{\quad \begin{align} \mathrm{d}F&=0\\ \star\,\mathrm{d}\star F &= J \end{align} \right.\]

Here \(\star\) is the Hodge star operator (that is, the Hodge dual).

It can be seen that, in the language of exterior algebra, the electromagnetic field is a 2-vector or 2-form, rather than a vector or 1-form.

However, the current is indeed a vector (or 1-form).
