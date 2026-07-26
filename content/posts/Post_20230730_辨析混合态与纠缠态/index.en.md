---
title: "Distinguishing Mixed States from Entangled States"
date: 2023-07-30T02:51:44+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/646801699"
author: "Haifei"
tags: ["Quantum Entanglement"]
categories: ["Quantum Information"]
---

## I. Pure States and Mixed States  

To understand pure states and mixed states, one must first understand the **density operator**, or **density matrix**.

### 1.1 What Is a Density Operator?  

When I first encountered the density operator, I found it quite remarkable. This is because it takes the **tensor product of a state with its own dual**:

\[v \mapsto v\otimes v^*\]

Or, written in a more physics-style manner:

\[| \psi \rangle \mapsto |\psi \rangle \langle \psi |\]

We all know that a quantum state \(v\) is merely a vector in a Hilbert space, namely \(v \in H\) . But why insist on making the density operator \(v\otimes v^*\in H\otimes H^* \cong \operatorname{End}(H)\) ? What is the point of this?

More troublingly, the matrix thus obtained (namely, the density matrix) necessarily has rank one. This is analogous to multiplying a column vector \(x\) by its own conjugate transpose:

\[xx^\dagger= \begin{bmatrix} 1 \\2 \end{bmatrix} \begin{bmatrix} 1 & 2 \end{bmatrix}= \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}\]

This does not provide any additional information; instead, it produces a non-invertible matrix.

So what exactly is the use of a density operator? In fact, its usefulness becomes apparent when you add together the density matrices corresponding to several different states. For example, suppose we are given another new column vector \(y\) :

\[yy^\dagger= \begin{bmatrix} 2 \\ 1 \end{bmatrix} \begin{bmatrix} 2 & 1 \end{bmatrix}= \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}\]

Then add \(xx^\dagger\) and \(yy^\dagger\) together:

\[xx^\dagger+yy^\dagger= \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} + \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} 5 & 4 \\ 4 & 5 \end{bmatrix}\]

You will now find that this new matrix cannot be represented as the product of a column vector and its own transpose! This is what is known as a **mixed state**. If a density matrix can be represented as the product of some column vector with itself, then it corresponds to a **pure state**.

### 1.2 What Are Density Operators For?  

Then why do mixed states arise? Are quantum states not all pure states? Are there quantum states that cannot be represented by a vector in a Hilbert space?

In fact, the concepts of mixed states and density operators are useful in the following two situations:

1. We are considering a **quantum ensemble**, that is, a collection of a large number of quantum states (not necessarily coherent). This is commonly used in quantum statistical mechanics.
2. Our **knowledge (information)** about a quantum system is limited. For example, given a multiparticle system, even if we know its overall quantum state, for one of its particles (a subsystem), we do not know which quantum state it is in; we only know that it has a certain probability of being in a particular state. This is commonly used in quantum information.

An example of the first case is natural light with zero degree of polarization. The corresponding density operator can then be written as: \(\rho = \frac{1}{2} |H\rangle\langle H| + \frac{1}{2}|V\rangle\langle V| = \frac{1}{2}I\) , where H represents horizontal polarization and V represents vertical polarization. Of course, partially polarized light with a degree of polarization between zero and one can also be represented using a density matrix: \(\rho = \frac{I+P\bm{r}\cdot\bm{\sigma}}{2} = \frac{I+P(x\sigma_x+y\sigma_y+z\sigma_z)}{2}\) , where \(\bm{\sigma}\) is a Pauli matrix, \(P\) is the degree of polarization, and \(\bm{r}\) is the Bloch vector, corresponding to coordinates on the Bloch sphere.

An example of the second case is quantum teleportation. We all know that if Alice does not communicate her measurement result to Bob as classical information, quantum teleportation cannot be completed (which is also why quantum teleportation does not imply faster-than-light communication). Before Bob learns Alice's measurement result, the qubit he possesses can be described by a density matrix corresponding to a mixed state.

### 1.3 Definition of the Density Operator  

Finally, let us define the density operator. Note that the quantum states in the initial example were not normalized. We now normalize them:

\[x= \begin{bmatrix} 1 \\ 2 \end{bmatrix} \mapsto  \begin{bmatrix} \frac{1}{\sqrt{5}} \\ \frac{2}{\sqrt{5}} \end{bmatrix}, \quad y= \begin{bmatrix} 2 \\ 1 \end{bmatrix} \mapsto  \begin{bmatrix} \frac{2}{\sqrt{5}} \\ \frac{1}{\sqrt{5}} \end{bmatrix}\]

\[xx^\dagger \mapsto   \begin{bmatrix} \frac{1}{5} & \frac{2}{5}\\ \frac{2}{5} & \frac{4}{5} \end{bmatrix}, \quad yy^\dagger \mapsto   \begin{bmatrix} \frac{4}{5} & \frac{2}{5}\\ \frac{2}{5} & \frac{1}{5} \end{bmatrix}\]

Then, change “adding several pure states” into “mixing several pure states with weights”:

\[\rho = \frac{1}{2}xx^\dagger + \frac{1}{2}yy^\dagger= \begin{bmatrix} \frac{1}{2} & \frac{2}{5}\\ \frac{2}{5} & \frac{1}{2} \end{bmatrix}\]

This motivates the following definition of a density operator:

\[\rho = \sum_{i} p_i |\psi_i\rangle\langle\psi_i|, \quad \sum_i p_i = 1\]

If your taste is more mathematical, you may also define a density matrix as an element of the following set: the set of all **positive semidefinite operators with trace equal to one** on a complex Hilbert space. Note that positive semidefiniteness implies self-adjointness (that is, Hermiticity).

## II. Separable States and Entangled States  

To understand what an entangled state is, we must first clarify how we describe multiparticle systems in quantum mechanics.

We all know that the quantum state of a particle can be described by a vector \(|\psi\rangle \in H\) in a Hilbert space. But what about multiple particles?

Here, we need the **tensor product** of vector spaces.

For example, the quantum state of one particle belongs to a Hilbert space: \(|\psi\rangle\in H_1\) , while the quantum state of another particle belongs to another Hilbert space: \(|\varphi\rangle\in H_2\) . To describe the overall system formed by these two systems, we can take the tensor product of \(H_1\) and \(H_2\) : \(H = H_1\otimes H_2\) . This new \(H\) is also a vector space.

Suppose \(H_1\) has two basis vectors \(|\psi_1\rangle,|\psi_2\rangle\) , and \(H_2\) has three basis vectors \(|\varphi_1\rangle,|\varphi_2\rangle,|\varphi_3\rangle\) ; then the new vector space \(H = H_1\otimes H_2\) will have six basis vectors:

\[|\psi_i\rangle\otimes|\varphi_j\rangle, \, i=1,2,\, j=1,2,3\]

We can use matrices to represent vectors in \(H = H_1\otimes H_2\) , for example:

\(\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}\) (unnormalized; normalization requires division by \(\sqrt{1^2+\cdots+6^2}\) ).

So what does a **separable state** mean? Similar to a pure state, its matrix can also be written as the product of a column vector and a row vector, for example:

\[\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}\]

In the language of linear algebra, it can be written as the tensor product of two (or more) vectors \(s=s_1\otimes s_2\) .

An **entangled state** is the opposite of a separable state: it cannot be written as the tensor product of several vectors, such as the earlier \(\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}\) . Mathematically, this is called non-separable.

## III. What Is the Difference Between Mixed States and Entangled States?  

When discussing mixed states, the space we consider is \(H\otimes H^*\) , namely the tensor product of a Hilbert space and its own dual.

A state is called a mixed state if and only if it is a non-separable vector on \(H\otimes H^*\) .

When discussing entangled states, the space we generally consider is \(H \otimes H\) , namely the tensor product of Hilbert spaces with one another.

> Note: More generally, one should consider \(\bigotimes_i H_i\) . Note: For identical particles, the tensor product should be replaced by the symmetric product or exterior product. The former corresponds to bosons, and the latter to fermions.

A state is called an entangled state if and only if it is a non-separable vector on \(H \otimes H\) .

Of course, we may also ask whether a mixed state is entangled. In this case, what we consider is an endomorphism on \(H \otimes H\) .

## IV. What Is the Relationship Between Mixed States and Entangled States?  

After being grilled in the comments section, I have added this section.

1. A state can be mixed but not entangled; it can also be entangled but not mixed; it can be both mixed and entangled; or it can be neither.

2. Taking a partial trace of an entangled state yields a mixed state. For example, as stated above, before Bob learns Alice's measurement result, the qubit he possesses is obtained by tracing out Alice's qubit from the overall quantum state; at this point, the result is a mixed state. In particular, for a two-particle system, its degree of entanglement equals the degree of mixing after the partial-trace operation, that is, the Schmidt Number equals the reciprocal of the purity.

3. How can one determine whether a general multiparticle mixed state is entangled? The space considered in this case is \((H\otimes \cdots \otimes H) \otimes (H\otimes \cdots \otimes H)^* \cong \mathrm{End}(H^{\otimes n})\) . For two particles, this question has a definite answer: it can be determined using the [PPT criterion (Positive Partial Transpose Criteria)](https://en.wikipedia.org/wiki/Peres–Horodecki\_criterion). For multiple particles, this question remains relatively open: there are many different criteria, each with its own advantages and disadvantages.
