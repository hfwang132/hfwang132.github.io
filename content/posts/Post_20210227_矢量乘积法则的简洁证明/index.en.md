---
title: "A Concise Proof of Vector Product Rules"
date: 2021-02-27T00:46:19+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/353243862"
author: "Haifei"
tags: ["Vector Calculus"]
categories: ["Mathematical Methods in Physics"]
---

I believe that anyone learning vector calculus for the first time finds the product rules for vectors quite daunting:

Easy difficulty:

\[\nabla(fg)=f\nabla g+g\nabla f\]

\[\nabla\cdot(f\mathrm{A})=f\nabla\cdot\mathrm{A}+\nabla f\cdot \mathrm{A}\]

\[\nabla\times(f\mathrm{A})=f\nabla\times\mathrm{A}+\nabla f\times\mathrm{A}\]

Hard difficulty:

\[\nabla\cdot(\mathrm{A}\times\mathrm{B})=\mathrm{B}\cdot(\nabla\times\mathrm{A})-\mathrm{A}\cdot(\nabla\times\mathrm{B})\]

Hell difficulty:

\[\nabla(\mathrm{A}\cdot \mathrm{B})=\mathrm{A}\times(\nabla\times\mathrm{B})+(\mathrm{A}\cdot\nabla)\mathrm{B}+\mathrm{B}\times(\nabla\times\mathrm{A})+(\mathrm{B}\cdot\nabla)\mathrm{A}\]

\[\nabla\times(\mathrm{A}\times\mathrm{B})=\mathrm{A}(\nabla\cdot \mathrm{B})-\mathrm{B}(\nabla\cdot\mathrm{A})+(\mathrm{B}\cdot\nabla)\mathrm{A}-(\mathrm{A}\cdot\nabla)\mathrm{B}\]

DLC: second derivatives

\[\nabla\times(\nabla f)=0\]

\[\nabla\cdot(\nabla\times\mathrm{A})=0\]

\[\nabla\times(\nabla\times\mathrm{A})=\nabla(\nabla\cdot\mathrm{A})-(\nabla\cdot\nabla)\mathrm{A}\]

---

## A Concise Proof  

To make the proof as concise as possible, we would like to use a single expression with subscripts to represent multiple expressions, rather than having to write out x, y, and z every time.

We use \(x_i\) to represent x, y, and z. That is, \(x_1\) represents \(x\) , \(x_2\) represents \(y\) , and \(x_3\) represents \(z\) .

Before beginning the proof, let us first introduce some useful notation and relations.

---

**Einstein Convention: Einstein Summation Convention**

\(\sum_{i}a_ib_i\) can be written as \(a_ib_i\) , that is, the summation symbol can simply be omitted. Whenever subscripts contain the same letter, it indicates summation over that index. To denote a particular term, one must write \(a_ib_j\) , using different letters.

As another example, \(c_{ik}=\sum_{j}a_{ij}b_{jk}\) can be written as \(c_{ik}=a_{ij}b_{jk}\) . This is in fact the multiplication of two matrices \(C=AB\) .

---

**Kronecker Delta** \(\delta_{ij}\)

The definition of the Kronecker delta is \[  \delta_{ij}=  \begin{cases}  1&i=j\\  0&i\neq j  \end{cases}  \]

---

**Rule 1 (trace):** \(a_i\delta_{ij}b_{j}=a_ib_i\) .

That is, if the two indices of a Kronecker delta appear in an expression, the Kronecker delta can be eliminated and the two indices can be made identical. Conversely, two originally identical indices can be changed into two distinct indices, and a Kronecker delta can be inserted to relate them.

If you are not yet accustomed to the Einstein summation convention, here it is again in conventional notation: \(\sum_{i,j}a_i\delta_{ij}b_j=\sum_{i}a_ib_i\)

You may notice that this is the dot product of vectors. Later, we will use the Kronecker delta to represent the dot product and \(\nabla\cdot\) , namely the divergence.

---

**Levi-Civita Symbol** \(\epsilon_{ijk}\)

The definition of the Levi-Civita symbol is \(\epsilon_{ijk}= \begin{cases} 1&(i,j,k)是(1,2,3)的偶置换\\ -1&(i,j,k)是(1,2,3)的奇置换\\ 0& i,j,k中的任意两个相同 \end{cases}\)

For example, \(\epsilon_{123}=1,\,\epsilon_{213}=-1,\,\epsilon_{112}=0,\,\epsilon_{333}=0\) .

---

**Rule 2 (determinant):** \(\epsilon_{ijk}a_ib_jc_k=\begin{vmatrix}a_1 &a_2&a_3\\ b_1&b_2&b_3\\ c_1&c_2&c_3\end{vmatrix}\)

You may vaguely sense that this can represent the cross product, since the cross product can be represented by a determinant. Indeed, later we will use the Levi-Civita symbol to represent \(\nabla\times\) , namely the curl.

---

**Relationship Between the Kronecker Delta and the Levi-Civita Symbol**

\[\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}\]

This expression is not difficult to prove; one only needs to consider the parities of ijk and klm. If their parities are the same, the left-hand side is 1; if their parities are opposite, the left-hand side is -1.

\[\epsilon_{ijk}\epsilon_{klm}=\begin{cases}1&(i=l,\,j=m,\,i\neq j)\\-1&(i=m,\,j=l,\,i\neq j)\end{cases}\]

Then simply compare with the right-hand side.

---

**Gradient**

The ith component of the gradient is defined as \((\nabla f)_i=\frac{\partial }{\partial x_i}f\)

**Divergence**

The divergence is defined as \(\nabla\cdot\mathrm{A}=\frac{\partial}{\partial x_i}A_i=\delta_{ij}\frac{\partial}{\partial x_i}A_j\)

**Curl**

The ith component of the curl is defined as \((\nabla\times\mathrm{A})_i=\epsilon_{ijk}\frac{\partial}{\partial x_j}A_k\)

---

**One convenience of index notation is that all the previous vector multiplications become scalar multiplications, and scalar multiplication is commutative.**

With these preparations, we can begin the proof.

---

\[\nabla(fg)=f\nabla g+g\nabla f\]

Proof: \([\nabla(fg)]_i=\frac{\partial }{\partial x_i}(fg)=g\frac{\partial }{\partial x_i}f+f\frac{\partial }{\partial x_i}g=(f\nabla g+g\nabla f)_i\)

Comment: This simply applies the product rule once for every i, but all of it can be expressed using a single formula.

---

\[\nabla\cdot(f\mathrm{A})=f\nabla\cdot\mathrm{A}+\nabla f\cdot \mathrm{A}\]

Proof: \(\nabla\cdot(f\mathrm{A})=\frac{\partial}{\partial x_i}(fA_i)=f\frac{\partial}{\partial x_i}A_i+A_i\frac{\partial}{\partial x_i}f=f\nabla\cdot\mathrm{A}+\nabla f\cdot \mathrm{A}\)

Comment: \(fA_i\) is a scalar, so one can directly apply the scalar product rule.

---

\[\nabla\times(f\mathrm{A})=f\nabla\times\mathrm{A}+\nabla f\times\mathrm{A}\]

Proof:

\[\begin{aligned} \left[\nabla\times(f\mathrm{A})\right]_i&=\epsilon_{ijk}\frac{\partial}{\partial x_j}(fA_k) \\&=\epsilon_{ijk}f\frac{\partial}{\partial x_j}A_k+\epsilon_{ijk}A_k\frac{\partial}{\partial x_j}f \\&=\left[f\nabla\times\mathrm{A}+\nabla f\times\mathrm{A} \right]_i\end{aligned}\]

Comment: Note the use of the commutativity of scalar multiplication.

---

\[\nabla\cdot(\mathrm{A}\times\mathrm{B})=\mathrm{B}\cdot(\nabla\times\mathrm{A})-\mathrm{A}\cdot(\nabla\times\mathrm{B})\]

Proof:

\[\begin{aligned} \nabla\cdot(\mathrm{A}\times\mathrm{B})&=\frac{\partial}{\partial x_i}(\mathrm{A}\times\mathrm{B})_i \\&=\frac{\partial}{\partial x_i}(\epsilon_{ijk}A_jB_k) \\&=\epsilon_{ijk}\frac{\partial}{\partial x_i}(A_jB_k) \\&=B_k\epsilon_{ijk}\frac{\partial}{\partial x_i}A_j+\epsilon_{ijk}A_j\frac{\partial}{\partial x_i}B_k \\&=B_k\epsilon_{kij}\frac{\partial}{\partial x_i}A_j-\epsilon_{jik}A_j\frac{\partial}{\partial x_i}B_k \\&=\mathrm{B}\cdot(\nabla\times\mathrm{A})-\mathrm{A}\cdot(\nabla\times\mathrm{B})  \end{aligned}\]

Comment: Note the use of the permutation properties of the Levi-Civita symbol. \(ijk\) and \(kij\) have the same parity, whereas \(ijk\) and \(jik\) have opposite parities.

---

\[\nabla(\mathrm{A}\cdot \mathrm{B})=\mathrm{A}\times(\nabla\times\mathrm{B})+(\mathrm{A}\cdot\nabla)\mathrm{B}+\mathrm{B}\times(\nabla\times\mathrm{A})+(\mathrm{B}\cdot\nabla)\mathrm{A}\]

Proof:

\[\begin{aligned} [\nabla(\mathrm{A}\cdot \mathrm{B})]_i&=\frac{\partial }{\partial x_i}(\mathrm{A}\cdot\mathrm{B}) \\&=\frac{\partial }{\partial x_i}(A_jB_j) \\&=B_j\frac{\partial }{\partial x_i}A_j+A_j\frac{\partial }{\partial x_i}B_j \end{aligned}\]

At this point, the proof seems to have stalled. However, notice that the result contains a curl, which means that we need to produce a Levi-Civita symbol; earlier, we derived the relation between the Levi-Civita symbol and the Kronecker delta:

\[\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}\]

Therefore, we consider inserting two Kronecker delta symbols. First, consider the first term of the expression above:

\[\begin{aligned}  \end{aligned} \begin{aligned} B_j\frac{\partial }{\partial x_i}A_j&=\delta_{im}\delta_{jl}B_j\frac{\partial }{\partial x_m}A_l \\&=(\delta_{il}\delta_{jm}-\epsilon_{ijk}\epsilon_{klm})B_j\frac{\partial }{\partial x_m}A_l \\&=\delta_{il}\delta_{jm}B_j\frac{\partial }{\partial x_m}A_l-\epsilon_{ijk}\epsilon_{klm}B_j\frac{\partial }{\partial x_m}A_l \\&=B_j\frac{\partial }{\partial x_j}A_i-\epsilon_{ijk}B_j(\epsilon_{klm}\frac{\partial }{\partial x_m}A_l) \\&=\left[(\mathrm{B}\cdot\nabla)\mathrm{A}+\mathrm{B}\times(\nabla\times\mathrm{A})\right]_i \end{aligned}\]

The second term follows similarly, and thus the original expression is proved.

Comment: One needs to use the insertion and elimination rules for the Kronecker delta flexibly.

---

\[\nabla\times(\mathrm{A}\times\mathrm{B})=\mathrm{A}(\nabla\cdot \mathrm{B})-\mathrm{B}(\nabla\cdot\mathrm{A})+(\mathrm{B}\cdot\nabla)\mathrm{A}-(\mathrm{A}\cdot\nabla)\mathrm{B}\]

Proof: Leave it to the reader.

Hint: Use \(\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}\) .

---

\[\nabla\times(\nabla\times\mathrm{A})=\nabla(\nabla\cdot\mathrm{A})-(\nabla\cdot\nabla)\mathrm{A}\]

Proof: Leave it to the reader.

Hint: Use \(\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}\) .

---

The tool used in this article is very powerful: tensor analysis.

By using tensor notation, you can work with quantities that have more indices, rather than only two like matrices. For example, the Levi-Civita symbol is a third-order tensor; by using it, you can write a third-order determinant in a more compact form. Of course, mathematically, tensors are not simply “things with multiple indices”; they are defined through multilinear maps, which is beyond the scope of this article.

Tensor analysis can be used not only to prove these vector identities, but also to help you complete proofs for other practical problems. For example: prove that the force on a magnetic dipole m in a magnetic field is \(\bm{F}=\nabla (\bm{m}\cdot\bm{B})\) .

In more advanced physical theories (such as general relativity), tensors are indispensable language. Start becoming familiar with tensors through electrodynamics!

---

Note: Tensors are divided into covariant and contravariant tensors: the former use subscripts, while the latter use superscripts. However, in Euclidean space, after choosing a standard orthonormal basis, there is no distinction between them (there actually is a distinction, but there is an isomorphism between them induced by the Euclidean metric), so they can all be written with subscripts.

Note: A matrix as a linear map is a first-order covariant and first-order contravariant tensor, i.e., a tensor of type (1,1); a matrix as a quadratic form is a second-order covariant tensor, i.e., a tensor of type (0,2).

Note: In any case, you should not call a third-order tensor a three-dimensional matrix. Matrices can only be second-order tensors, and second-order tensors possess many useful properties; thus, matrices hold a special place in our minds.
