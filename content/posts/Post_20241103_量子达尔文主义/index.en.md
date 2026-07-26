---
title: "Quantum Darwinism"
date: 2024-11-03T14:44:37+08:00
originalURL: "https://www.zhihu.com/question/2840709847/answer/21823919227"
aliases:
  - "/en/quantum_darwinism/"
  - "/en/Post_20250108_量子达尔文主义/"
draft: false
tags: ["Quantum Darwinism"]
categories: ["Quantum Information/Quantum Optics"]
author: "Haifei"
---

Personally, among the interpretations of quantum mechanics, I find Zurek's **Existential Interpretation**—also known as **Quantum Darwinism** [1]—to be the most interesting at present. Zurek himself is one of the founders of decoherence theory.

Quantum Darwinism does not directly provide the dynamics of the measurement process, but it makes several highly illuminating observations:

**(1)** Measurement outcomes can become macroscopic facts because their information is replicated (cloned) many times and dispersed throughout the environment, allowing different observers to reach a consensus.

> The specific cloning process:  
>  $|s_k\rangle |\varepsilon_0\rangle \rightarrow |s_k\rangle |\varepsilon_k\rangle$   
> Here $|s_k\rangle$ is the state of the system, and $|\varepsilon_k\rangle$ is the state of the environment.  
> Clearly, for a particular k, there exists a unitary process $U$ such that $U|s_k\rangle |\varepsilon_0\rangle = |s_k\rangle |\varepsilon_k\rangle$ .  
> However, this process $U$ cannot simultaneously clone any other $|s_k\rangle$ ; rather, it can only clone a set of orthogonal $|s_k\rangle$ . This is the no-cloning theorem discussed in point (2) below.

**(2)** According to the no-cloning theorem, a unitary process can only clone a set of orthogonal states.

> **Comment:** From (1) and (2), we can conclude that measurement outcomes must be orthogonal. In other words, measurement outcomes form a complete orthogonal basis in Hilbert space.  
>   
> However, there are infinitely many complete orthogonal bases in Hilbert space. Which one does a particular measurement correspond to?  
>   
> For example, “a live cat” and “a dead cat” are quantum states, but “a live cat plus a dead cat” and “a live cat minus a dead cat” are equally valid quantum states. Why can we observe only the former pair of outcomes rather than the latter?  
>   
> Point (3) below provides an explanation.

**(3)** The interaction between the system and the environment allows only one set of orthogonal quantum states (the preferred basis) to survive, while the information of all other quantum states (superpositions of the preferred basis) is ultimately lost.

> **Comment:** Point (3) is the origin of the name “quantum Darwinism.” It is supported by a rigorous dynamical model, namely the decoherence model. However, the decoherence model can only turn a superposition into a mixed state rather than a pure state, and thus still does not provide the dynamics of the measurement process.  
>   
> So what does a mixed state mean? A mixed state has two physical meanings: one is a description of an ensemble, and the other is a description of subjective information. For example, for a mixed state of a qubit $a|0\rangle\langle0|+b|1\rangle\langle1|$ , we have two ways of interpreting it: first, we have a quantum ensemble in which a proportion $\frac{a}{a+b}$ of the qubits are in the $|0\rangle$ state, and a proportion $\frac{b}{a+b}$ of the qubits are in the $|1\rangle$ state; second, we have only one qubit, and we know that it is either in the $|0\rangle$ state or in the $|1\rangle$ state, but do not know which is actually the case. We only know that it is in the $\frac{a}{a+b}$ state with probability $|0\rangle$ , and in the $\frac{b}{a+b}$ state with probability $|1\rangle$ . If someone accepts only the ensemble interpretation, they will most likely believe in the many-worlds interpretation.  
>   
> Clearly, at this point, we still have not explained the origin of probability—that is, why measurement outcomes occur probabilistically. Point (4) below is Zurek's explanation of the origin of probability:

**(4)** Probability originates from quantum entanglement: if we have an entangled pair $(A,B)$ in the state $|a_1\rangle |b_1\rangle + |a_2\rangle|b_2\rangle + \cdots + |a_N\rangle |b_N\rangle$ , then any permutation operation on $B$ does not change the physical state. This is because any such permutation operation can be canceled by the same permutation operation on $A$ . Precisely because permuting the branches has no effect whatsoever on the physical state, the branches must occur with equal probability.

> **Comment:** The equal-probability case can be generalized to the unequal-probability case. This is because the environment always has more degrees of freedom than the system; that is, $B$ has more degrees of freedom than $A$ . For example, suppose the system $A$ is a qubit, whose Hilbert space is two-dimensional, while the Hilbert space of $B$ is 1024-dimensional (for example, 10 qubits). Then we can imagine a state such as $|0\rangle (|b_1\rangle + \cdots + |b_k\rangle) + |1\rangle (|b_{k+1}\rangle + \cdots + |b_{1024}\rangle)$ . At this point, according to the principle of equal probability, the probability of $|0\rangle$ is $\frac{k}{1024}$ , and the probability of $|1\rangle$ is $\frac{1024-k}{1024}$ .  
>   
> In fact, the dimension of the environment's Hilbert space is of order $2^{10^{23}}$ , far more than $2^{10} = 1024$ , so all probabilities between 0 and 1 can be realized using this model.

These are the four key points of Zurek's existential interpretation. Point (3) is called “**Einselection**,” short for “Environment-Induced Superselection,” while point (4) is called “**Envariance**,” short for “Environment-assisted Invariance.”

---

The following are personal philosophical comments:

Personally, I think Zurek's most brilliant observation is actually point (1), which establishes the philosophical tone of the existential interpretation. Let me restate it here:

**Measurement outcomes can become macroscopic facts because their information is replicated many times and dispersed throughout the environment, allowing different observers to reach a consensus.**

This statement implies that different observers can observe different facts. Zurek's work quantitatively characterizes this point through mutual information [1]. The reason this does not happen is that, as the information leaked into the environment and the portion of the environment accessible to observers increase, mutual information grows very rapidly.

The idea that “different observers can observe different facts” is not surprising in relativity. Carlo Rovelli's Relational Quantum Mechanics interpretation emphasizes precisely this point.

Returning to point (1), it implies a philosophical view: the boundary between what is known and what exists is blurred. In Zurek's own words [2]

> "I strongly suspect that the ultimate message of quantum theory is that the separation between what exists and what is known to exist – between the **epistemic** and the **ontic** – must be abolished."  
>   
> "Surprisingly, as the nascent quantum theory matured, quantum awkwardness did not go away. The lesson of the developments that started with decoherence, and led, through einselection and pointer states to quantum Darwinism and related insights, is that quantum states are **epiontic**. It now appears that the distinction between **what is** and **what is known** about what exists – something we take for granted in our everyday world – is not there at the fundamental level."  
>   
> Translation:  
>   
> I strongly suspect that the ultimate message quantum theory seeks to convey is this: the distinction between “what exists” and “what is known to exist”—that is, the distinction between the epistemic and the ontic—must be abolished.  
>   
> Surprisingly, as the nascent theory of quantum mechanics gradually matured, quantum awkwardness did not disappear. Research beginning with decoherence, passing through einselection and pointer states, and ultimately developing into quantum Darwinism and related insights, shows that quantum states are “epiontic,” integrating the epistemic and the ontic. It now appears that at the fundamental level, the distinction we take for granted in our everyday world between “what is” and “what is known” does not actually exist.

Zurek reconciles the conflict between ontological interpretations (hidden variables, many worlds) and epistemological interpretations (quantum Bayesianism, relational quantum mechanics). He says that quantum mechanics is neither entirely epistemic nor entirely ontic, but rather “epiontic.” In other words:

What is known is what exists; what exists is what is known.

## References  

1. Zurek, W. H. Quantum Theory of the Classical: Einselection, Envariance, Quantum Darwinism and Extantons. Entropy 2022, 24 (11), 1520. [https://doi.org/10.3390/e24111520](https://doi.org/10.3390/e24111520)
2. Emergence of the Classical from within the Quantum Universe. [https://arxiv.org/abs/2107.03378](https://arxiv.org/abs/2107.03378)
