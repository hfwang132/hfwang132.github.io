---
title: "The Difference Between Quantum Entanglement and Classical Correlations, and the Quantum Measurement Problem"
date: 2024-04-30T15:24:28+08:00
originalURL: "https://zhuanlan.zhihu.com/p/695458530"
aliases:
  - "/en/classical_correlation/"
  - "/en/Post_20240527_量子纠缠与经典关联的区别-以及量子测量问题/"
draft: false
tags: ["quantum measurement theory"]
categories: ["quantum information"]
math: true
author: "Haifei"
---

When many physicists popularize quantum entanglement to the general public, they often give an example:

> Imagine that you have two boxes, one containing a pizza and the other containing a hamburger, and you cannot know what is inside before opening them. Alice and Bob each take one box and travel to places far apart. At this point, when Alice opens her box, she can know what is in Bob's box far away.

There must be something wrong with this example... because it does not involve quantum mechanics at all.

Indeed, this example illustrates classical correlation rather than quantum entanglement. Let pizza be \(|0\rangle\) and hamburger be \(|1\rangle\). Then, in the example above, the state of the system is

\[\rho_{\text{classical correlation}} = \frac{1}{2} \left( |01\rangle\langle 01| + |10\rangle\langle 10| \right)\]

In matrix form, this is:

\[\rho_{\text{classical correlation}} = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & 0 & 0 \\ 0 & 0 & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}\]

True quantum entanglement, on the other hand, should be as follows:

\[\rho_{\text{quantum entanglement}} = |\psi\rangle\langle\psi | = \frac{1}{2} \left( |01\rangle\langle 01| + |10\rangle\langle 10| + |01\rangle\langle 10| + |10\rangle\langle 01 | \right)\]

where \(|\psi\rangle = \frac{1}{\sqrt{2}} (|01\rangle + |10 \rangle)\)

In matrix form, this is:

\[\rho_{\text{quantum entanglement}} = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}\]

As can be seen, true quantum entanglement has off-diagonal terms. These off-diagonal terms are also called coherences.

Likewise, it can be seen that classical correlation is obtained only after the quantum entangled state above decoheres. In other words, classical correlation is the result of quantum entanglement after decoherence.

Decoherence is also an interpretation of the **quantum measurement problem**: when a system becomes entangled with its environment, if one considers the partial trace over the system, one finds that the state of the system is decohered. In this way, quantum entanglement becomes classical correlation, and at this point the density matrix retains only diagonal terms.

However, decoherence cannot explain the problem of wavefunction collapse. This is because the following process is still caused by the collapse of the overall wavefunction of the system and environment.

\[\begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & \frac{1}{2} & 0 & 0 \\ 0 & 0 & \frac{1}{2} & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix} \xrightarrow{\text{collapse}}  \begin{cases} \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}, & \text{with }\frac{1}{2} \text{ probability} \\ \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}, & \text{with }\frac{1}{2} \text{ probability} \end{cases}\]

This step cannot be explained by decoherence. Therefore, the measurement problem remains unsolved to this day. This is easy to understand: decoherence itself is still a unitary evolution process, whereas wavefunction collapse is non-unitary.

Therefore, we can only provisionally accept that wavefunction collapse is an axiom in modern quantum mechanics, rather than a theorem that can be derived. This leads to a completeness problem: we cannot determine through quantum mechanics itself whether a process should be a unitary evolution process or a non-unitary collapse process.

This problem is also called the Heisenberg cut: namely, how to find such a “cut” such that systems below it evolve normally, while systems above it collapse. Of course, since our existing measuring instruments are all systems with very large numbers of particles, we need not worry about this problem—we are quite certain that our measurements induce the collapse of the system.

---

In categorical quantum theory, describing quantum entanglement requires a \(\mathbf{Hilb}\) tensor category, whereas describing classical correlation requires only a \(\mathbf{Rel}\) tensor category. The tensor product of the former is the tensor product of Hilbert spaces, while that of the latter is the Cartesian product of sets.

Cartesian products (as well as direct products and direct sums) cannot describe quantum entanglement. The tensor product of Hilbert spaces is the very root of the existence of entanglement phenomena. The former is a hallmark of the classical and can describe classical correlation; the latter is a hallmark of the quantum and can describe quantum entanglement.

However, true classical physics is deterministic, and it is described by the \(\mathbf{Set}\) category. The \(\mathbf{Rel}\) category, meanwhile, belongs to probability theory; it lies between \(\mathbf{Hilb}\) and \(\mathbf{Set}\). Perhaps the transition from the \(\mathbf{Rel}\) category to the \(\mathbf{Set}\) category is the final step in resolving the measurement problem, and this step itself does not lie within the \(\mathbf{Hilb}\) category.

The measurement problem is similar to certain problems in statistical mechanics, such as entropy and the arrow of time. The roots of these problems are all Sorites-paradox-like: they emerge only when a system is sufficiently large, such that it is difficult for us to find a boundary between small and large—that is, the Heisenberg cut.
