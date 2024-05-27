---
title: "The Difference Between Quantum Entanglement and Classical Correlation, and the Quantum Measurement Problem"
date: 2024-05-27T17:33:11+08:00
draft: false
tags: ["Quantum Measurement Theory"]
categories: ["Quantum Information"]
---

Many physicists use an example to explain quantum entanglement to the public:

> Imagine you have two boxes, one containing pizza and the other a burger. Before opening the boxes, you cannot know what is inside. Alice and Bob each take a box and move to distant locations. When Alice opens her box, she instantly knows what is in Bob's box far away.

This example must be wrong... because it doesn't involve quantum mechanics at all.

Indeed, this example demonstrates classical correlation, not quantum entanglement. Let pizza be $|0\rangle$ and burger be $|1\rangle$, then in the above example, the state of the system is

$\rho_{\text{classical correlation}} = \frac{1}{2} \left( |01\rangle\langle 01| + |10\rangle\langle 10| \right)$

In matrix form, it is:

$\rho_{\text{classical correlation}} = \begin{bmatrix} 0 & 0 & 0 & 0 \\\\ 0 & \frac{1}{2} & 0 & 0 \\\\ 0 & 0 & \frac{1}{2} & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix}$

However, true quantum entanglement should be as follows:

$\rho_{\text{quantum entanglement}} = |\psi\rangle\langle\psi | = \frac{1}{2} \left( |01\rangle\langle 01| + |10\rangle\langle 10| + |01\rangle\langle 10| + |10\rangle\langle 01 | \right)$

Where $|\psi\rangle = \frac{1}{\sqrt{2}} (|01\rangle + |10 \rangle)$

In matrix form, it is:

$\rho_{\text{quantum entanglement}} = \begin{bmatrix} 0 & 0 & 0 & 0 \\\\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\\\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix}$

As you can see, true quantum entanglement has off-diagonal terms. These off-diagonal terms are also called coherences.

Similarly, when the above quantum entangled state decoheres, classical correlation is obtained. In other words, classical correlation is the result of the decoherence of quantum entanglement.

Decoherence is also an interpretation of the **quantum measurement problem**: when a system entangles with the environment, if we examine the partial trace of the system, we find that the system's state is decohered. In this way, quantum entanglement becomes classical correlation, and the density matrix only retains the diagonal terms.

But decoherence cannot explain the problem of wavefunction collapse. Because the following process is still caused by the collapse of the overall wavefunction of the system and the environment.

$\begin{bmatrix} 0 & 0 & 0 & 0 \\\\ 0 & \frac{1}{2} & 0 & 0 \\\\ 0 & 0 & \frac{1}{2} & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix} \xrightarrow{\text{collapse}}  \begin{cases} \begin{bmatrix} 0 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix}, & \text{with }\frac{1}{2} \text{ probability} \\\\ \begin{bmatrix} 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix}, & \text{with }\frac{1}{2} \text{ probability} \end{cases}$

This step cannot be explained by decoherence. Therefore, the measurement problem has not yet been resolved. This is also understandable: decoherence itself is still a unitary evolution process, while wavefunction collapse is non-unitary.

So, we can only temporarily accept that wavefunction collapse is an axiom in modern quantum mechanics, rather than a theorem that can be derived. This leads to a completeness problem: we cannot determine through quantum mechanics alone whether a process should be a unitary evolution or a non-unitary collapse process.

This problem is also called the Heisenberg cut, which is how to find such a "cut" so that below it the system evolves normally, while above it the system collapses. Of course, since our existing measuring instruments are systems with a large number of particles, we don't need to worry about this problem—we are very certain that our measurements will induce the collapse of the system.

---

In categorical quantum theory, describing quantum entanglement requires the tensor category of $\mathbf{Hilb}$, while describing classical correlation only requires the tensor category of $\mathbf{Rel}$. The tensor product of the former is the tensor product of Hilbert spaces, while the tensor product of the latter is the Cartesian product of sets.

The Cartesian product (as well as direct product and direct sum) cannot describe quantum entanglement. The tensor product of Hilbert spaces is the root cause of entanglement phenomena. The former is a hallmark of classicality and can describe classical correlation, while the latter is a hallmark of quantum mechanics and can describe quantum entanglement.

However, true classical physics is deterministic and is described by the category of $\mathbf{Set}$. The category of $\mathbf{Rel}$ is probabilistic and lies between $\mathbf{Hilb}$ and $\mathbf{Set}$. Perhaps, transitioning from the category of $\mathbf{Rel}$ to the category of $\mathbf{Set}$ is the final step in solving the measurement problem, and this step itself is not within the category of $\mathbf{Hilb}$.

The measurement problem is similar to some problems in statistical mechanics, such as entropy and the arrow of time. The root of these problems is also a heap paradox: they only emerge when the system is large enough, making it difficult to find a boundary between small and large, i.e., the Heisenberg cut.
