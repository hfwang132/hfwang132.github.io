---
title: "Classical Shadows of Quantum States"
date: 2025-05-30T02:53:53+08:00
originalURL: "https://zhuanlan.zhihu.com/p/1911107376045593900"
aliases:
  - "/en/classical_shadows/"
  - "/en/Post_20251012_量子态的经典阴影-Classical-Shadows/"
draft: false
tags: ["Classical Shadows", "Haar Measure"]
categories: ["Quantum Information/Quantum Optics"]
math: true
author: "Haifei"
---

## I. Quantum State Tomography  

At present, quantum states composed of hundreds or thousands of qubits can already be prepared (twenty references omitted here).

But how do we know that the prepared quantum state $\rho$ is indeed the one we want $\rho$? Or, more broadly: how can we learn (some or all) information about a quantum state $\rho$?

To learn a quantum state $\rho$, we first need to prepare $\rho$, then measure it in different measurement bases to obtain probability distribution functions, and finally use these probability distribution functions to learn $\rho$. This process is called **quantum state tomography**.

## II. Full Quantum State Tomography  

If our goal is to completely reconstruct $\rho$, namely, to learn all information about $\rho$, then this process is called **full state tomography (FST)**.

Taking a system composed of $n$ qubits as an example, its quantum state $\rho$ can be written as:

$$\begin{aligned} \rho &= \frac{1}{2^n}\sum_i c_i P_i \\ &\phantom{==}  P_i = \sigma_{i_1}\otimes \cdots \otimes \sigma_{i_n}, \quad i=(i_1,...,i_n), \quad i_k= 0,1,2,3 \\ &\phantom{==} \sigma_0=\mathbb{I},\, \sigma_1=X,\,\sigma_2 = Y,\,\sigma_3=Z  \end{aligned}$$

where $\sigma_0=\mathbb{I},\, \sigma_1=X,\,\sigma_2 = Y,\,\sigma_3=Z$ are the single-qubit Pauli matrices, and $c_i = \operatorname{tr}[\rho P_i]$.

It can be seen that, as long as we measure the expectation values $c_i = \operatorname{tr}[\rho P_i]$ of the operators $P_i$, we can perform FST on the quantum state $\rho$. These $c_i$ are called Pauli coefficients.

There are $4^n - 1$ Pauli coefficients to measure, because $P_0 = \mathbb{I}^{\otimes n}$ is the identity matrix, causing $c_{0}$ to always equal 1.

This measurement method is called Pauli measurements, and it is the method most commonly used.

> Note that in fact only $3^n$ measurement bases are needed, because the measurement results of the remaining $(4^n-3^n-1)$ $P_i$ are marginal distributions of the measurement results of these $3^n$ $P_j$.  
>   
> For example, the measurement result of $\mathbb{I}\otimes Y$ can be obtained entirely from the measurement result of $X \otimes Y$—because the probability distribution of the former is a marginal distribution of that of the latter.

This article mainly uses systems composed of $n$ qubits as examples, but the extension to qudits is also straightforward. However, continuous-variable systems are not discussed here.

### 2.1 Sample Complexity  

As mentioned above, to learn a quantum state $\rho$, we need to first prepare multiple samples of $\rho$ and then measure them in different measurement bases. This naturally raises a direct question:

**For a** $d$ **-dimensional quantum state** $\rho$**, how many samples are needed to estimate** $\rho$ **within an error** $\epsilon$**?**

> A $d$-dimensional quantum state $\rho$ is defined as a positive semidefinite operator with trace 1 on a $d$-dimensional Hilbert space. It is also commonly called a density matrix and is characterized by $d^2-1$ real parameters.

To better understand and formulate this question, let us first introduce some terminology. We define **sample complexity** as follows: as the dimension $d$ increases and the error $\epsilon$ decreases, the required number of samples $N$ also grows. The growth rate $N \sim O(f(d,\epsilon))$ is the sample complexity.

For a single qubit, $d=2$, but for a system composed of $n$ qubits, it is $d=2^n$. For $n$ k-dimensional qudits, it is $d=k^n$. Thus, the Hilbert-space dimension $d$ grows exponentially as the number of particles $n$ increases.

Next, let us consider the error $\epsilon$. The two most commonly used functions for characterizing the error between two quantum states $\rho$ and $\sigma$ are **fidelity** $F(\rho,\sigma)$ and **trace distance** $T(\rho,\sigma)$:

$$F(\rho,\sigma):=\operatorname{tr}\left[\sqrt{\sqrt{\sigma}\rho\sqrt{\sigma}}\right]^2$$  
 $$T(\rho,\sigma):=\frac{1}{2}||\rho-\sigma||_1$$

where $||\cdot||_1$ is the trace norm / 1-norm, defined as $|| A||_1 =\operatorname{tr}\left[\sqrt{A^\dagger A}\right]$.

The closer the fidelity is to 1 and the closer the trace distance is to 0, the smaller the error. They satisfy:

$$1-\sqrt{F} \le T \le \sqrt{1-F}$$

If the trace distance $T(\rho,\sigma)$ is used as the error $\epsilon$, then the error $\delta:=1-F$ calculated using fidelity satisfies $\delta\ge \epsilon^2$.

This article mainly uses trace distance $||\rho - \sigma||_1$ as the error (the extra constant 1/2 is unimportant for scaling).

### 2.2 Upper Bounds on Sample Complexity  

Intuitively, to reconstruct a quantum state $\rho$, the dependence of sample complexity on $d$ is at least $\sim d^2$, or equivalently $\Omega(d^2)$, because we need at least $\sim d^2$ measurement-basis (POVM) elements in order for the measurement basis to be informationally complete. On the other hand, we need to perform repeated measurements so that the estimator approaches the true value. To make both errors smaller than $\epsilon$, the relationship between sample complexity and the error $\epsilon$ is likely inverse, $\sim O(\epsilon^{-m})$.

Therefore, we conjecture that the sample complexity is $\boxed{ N = O(d^l/\epsilon^m) }$, where $l \ge 2$. Next, we study sample complexity under different measurement schemes.

### 2.3 Complexity of Pauli Measurements  

Next, we give a relatively loose upper bound on sample complexity [[1]](#ref\_1), provided by the Pauli measurements mentioned above, which are also the most commonly used method.

We first introduce Hoeffding's inequality, which will be used later:

> **Hoeffding's inequality**  
> Given $N$ independent random variables $X_i,\,i=1,...,N$, with respective ranges $[a_i,b_i]$, their sum $S=\sum_iX_i$ satisfies  
> $\begin{aligned} P(|S-\mathbb{E}(S)| \ge \epsilon) \lt 2\exp \left[-\frac{2 N^2 \epsilon^2}{\sum_{i}(b_i-a_i)^2}  \right] \end{aligned}$  
> If the $X_1,...,X_N$ have the same distribution, range $[a,b]$, and mean $Y = S/N=\sum_iX_i /N$, then  
>  $\begin{aligned} P(|Y-\mathbb{E}(Y)| \ge \epsilon) \lt 2\exp \left[ -\frac{2 N \epsilon^2}{(b-a)^2} \right] \end{aligned}$

Next, we apply Hoeffding's inequality.

> For a quantum state $\rho = \frac{1}{2^n}\sum_i c_i P_i $, repeatedly measure the operator $P_i$, and take the average of the outcomes as an estimator $\hat{c}_i$ of $c_i = \operatorname{tr}[\rho P_i]$.  
>   
> Applying Hoeffding's inequality to $\hat{c}_i$, and noting that $\hat{c}_i$ takes values $\pm1$, gives:  
>   
> $P[|\hat{c}_i-c_i| \gt \epsilon_i] \le 2 \exp \left[-N\epsilon_i^2/2\right]$  
>   
> where $N$ is the number of repeated measurements of $P_i$.  
>   
> Thus, by the union bound, among the $(4^n-1)$ $c_i$, the probability that any one $|\hat{c}_i-c_i| \gt \epsilon_i$ is:  
>   
> $P[|\hat{c}_i-c_i| \gt \epsilon_i, \,\exists \, i] \le (4^n - 1) \cdot 2 \exp \left[-N\delta^2/2\right]$  
>   
> Now, we want all $|\hat{c}_i-c_i|$ to be smaller than $\epsilon_1$ with high probability. That is, the probability of an error greater than $\epsilon_1$ should be a small number $\delta \ll 1$. Setting the right-hand side above equal to $\delta$ yields:  
>   
> $N= \frac{2}{\epsilon_1^2}\log \frac{2\cdot (4^n-1)}{\delta}= O\left(\frac{n -\log \delta}{\epsilon_1^2}\right) $  
>   
> Substituting $d=2^n$ gives:  
>   
> $\boxed{ N= O(\log(d/\delta)/\epsilon^2_1)  }$

This is the sample complexity required to estimate all Pauli coefficients within error $\epsilon_1$ at a failure rate below $\delta$.

---

Note! Here, $\epsilon_1$ is only the measurement error of a single Pauli coefficient $c_i$, whereas what we want is the error $\epsilon$ of the density matrix $\rho = \frac{1}{2^n}\sum_i c_i P_i $.

> To this end, define the error matrix:  
>   
> $\Delta = \hat{\rho}-\rho = \sum_i(\hat{c}_i-c_i)P_i$  
>   
> and require its trace norm to be less than $\epsilon$:  
>   
> $||\Delta||_1\lt \epsilon$  
>   
> Note that the Hilbert-Schmidt norm is easier to calculate: $||\Delta||_2^2 := \operatorname{tr}[A^\dagger A] = \frac{1}{2^n}\sum_i |\hat{c}_i-c_i|^2$, because  
> $\operatorname{tr}[P_i^\dagger P_j]=\operatorname{tr}[P_iP_j]=\delta_{ij}$.  
>   
> We can therefore use the Cauchy inequality $||A||_1 \le \sqrt{d}||A||_2$, where $d = 2^n$ is the order of the matrix:  
>   
> $||\Delta||_1 \le \sqrt{2^n}||\Delta||_2 = (\sum_i |\hat{c}_i-c_i|^2)^{1/2} \le (\sum_i \epsilon_1^2)^{1/2} = (4^n-1)^{1/2} \,\epsilon_1$  
>   
> Let $||\Delta||_1 \le \epsilon$. Then $\epsilon \sim(4^n-1)^{1/2} \,\epsilon_1\sim 2^n \epsilon_1$, so  
>   
> $N \sim (n - \log \delta)/\epsilon_1^2 \sim (n - \log \delta)4^n /\epsilon^2 = \log \frac{d}{\delta} \cdot d^2/\epsilon^{2}$  
>   
> Finally, considering that there are $3^n$ measurement bases, and each measurement basis requires $N$ measurements. Therefore:  
>   
> $N \mapsto 3^n \cdot N \sim \log \frac{d}{\delta}  \cdot d^{3.585} /\epsilon^{2}$

Usually, the failure rate $\delta$ is not included in the range of sample complexity, so:

$$\boxed{ N = O(\log d  \cdot d^{3.585} /\epsilon^{2}) = O(N \cdot 12^N/\epsilon^2)} $$

Update: In February 2025, the record for the upper bound was improved to $\boxed{ N = O(\log d  \cdot d^{3.322} /\epsilon^{2}) = O(N \cdot 10^N/\epsilon^2)} $, while the lower bound was proven to be $\Omega(d^{3.188}\log (d)/\epsilon^2)=\Omega(N \cdot 9.118^N /\epsilon^2)$ [[2]](#ref\_2).

### 2.3 Sample Complexity of Single-Copy Measurements  

In fact, we can do better: the above upper bound can be reduced to $\boxed{O(\log d \cdot d^3 / \epsilon^{2})}$.

This is because $3^n$ measurement settings yield $3^n \cdot 2^n = 6^n = d^{2.585}$ POVM elements, whereas the minimum number of POVM elements required to guarantee informational completeness is $4^n = d^2$. Thus, we can use a SIC-POVM with exactly $d^2$ elements, or use MUB (Mutually Unbiased Bases), which contains $(d+1)$ measurement bases, with $d$ elements in each basis, for a total of $d(d+1)$ POVM elements. Either method can reduce the upper bound on sample complexity to $O(\log d \cdot d^3 /\epsilon^{2})$.

The lower bound has been proven to be $\Omega(d^3 /\epsilon^{2})$ [[3]](#ref\_3), but no specific measurement method has yet been found. Compared with the upper bound, the lower bound only lacks $\log(d)$, which has little impact in general experiments.

### 2.4 Sample Complexity of Multi-Copy Measurements  

All the measurement methods above are single-copy measurements, because only one sample is measured at a time. We can consider the more general case—performing joint measurements by entangling multiple samples $\rho^{\otimes n}$—which is called multi-copy measurements. Such measurements require quantum memory and are essentially difficult to implement with current quantum hardware.

It has been proven that, for this most general measurement scheme, the tight bound on sample complexity is $\boxed{\Theta(d^2 / \epsilon^{2})}$ [[4]](#ref\_4) [[5]](#ref\_5). This was not proven until 2016.

Summary:

$$\begin{aligned} \hline & \text{POVM} & \quad & \text{Sample Complexity}\,(d=2^n)\\ \hline  & \text{Pauli Measurements} & \quad & O(d^{3.322}\log (d)/\epsilon^2), \, \Omega(d^{3.188}\log (d)/\epsilon^2) \\ & \text{Single-copy measurements} & \quad & O(d^{3}\log (d)/\epsilon^2),\,\Omega(d^3 / \epsilon^2) \\ & \text{Multi-copy measurements} & \quad & \Theta(d^2/\epsilon^2)\\ \hline \end{aligned}$$

Note that in this table, $O(\cdot)$ denotes an upper bound, $\Omega(\cdot)$ denotes a lower bound, and $\Theta(\cdot)$ denotes a tight bound.

## III. Classical Shadows  

In the previous section, we mentioned that if we measure all Pauli coefficients (the expectation values of Pauli operators), require that the error of every result be no greater than $\epsilon$, and have a failure rate no higher than $\delta$, then the sample complexity is:

$$\boxed{ N = O\left(\frac{n-\log\delta}{\epsilon^2}\right)=O\left(\log \left(\frac{d}{\delta}\right) \cdot \epsilon^{-2}\right) }$$

This reveals a seemingly surprising fact: if we are concerned only with expectation values of operators rather than the quantum state itself, the sample complexity can be drastically reduced to logarithmic order, completely eliminating its dependence on $d^{\sim2-3.5}$.

In fact, for any $M$ operators $O_1,...,O_M$, if we wish to estimate their expectation values within error $\epsilon$ and at a failure rate below $\delta$, then only the following sample complexity is needed:

$$\boxed{ N \sim \log(M/\delta)\cdot \epsilon^{-2} \cdot (\max_i||O_i||^2_{\text{shadow}}) }$$

The specific form of $||\cdot||_{\text{shadow}}$ depends on the measurement method. This result comes from the famous 2020 work “Classical Shadows” by Huang et al. [[6]](#ref\_6).

From the analysis in Section II, this complexity is not surprising. So why have “Classical Shadows” become so popular in recent years?

In my opinion, this is because earlier research on sample complexity was mostly motivated by narrowing theoretical upper bounds rather than physical applications; even when measurement schemes existed, they were difficult to implement experimentally and were more often cases of “theoretically existing” in the mathematician's sense. Classical shadows, however, provide a simple, concrete, and effective measurement method: the implementation steps are very clear, and experimental physicists can use it out of the box. In addition, logarithmic complexity itself is an excellent selling point (even if it is not as surprising as it first appears).

In fact, as early as 2017, Scott Aaronson proposed shadow tomography [[7]](#ref\_7), which also identified logarithmic complexity $\log(M)$. However, he considered the probabilities $\operatorname{tr}[\rho E_i]$ of $M$ two-outcome POVMs, rather than $\langle O_i \rangle = \operatorname{tr}[\rho O_i]$ general physical observable operators $M$. The reason Shadow Tomography did not receive as much attention as Classical Shadows is also that its proposed measurement scheme was relatively complicated.

> Fun fact: Scott Aaronson's blog is very interesting; for example, this highly controversial post: [Shtetl-Optimized » Blog Archive » Cargo Cult Quantum Factoring](https://scottaaronson.blog/?p=6957)

### 3.1 Concrete Implementation of Classical Shadows  

Now let us look at how Classical Shadows are specifically implemented.

Broadly speaking, the procedure consists of two steps:

**1.** Measure the quantum state to obtain so-called “Classical Shadows,” and store them on a classical computer

**2.** Starting from the stored Classical Shadows, simultaneously estimate the expectation values of $M$ operators using a certain algorithm.

Let us first look at **1**, which is performed as follows:

**1.1** Randomly select a $U$ from the Clifford operators, apply it to the quantum state $\rho$, and obtain $U\rho U^\dagger$.

**1.2** Measure $U\rho U^\dagger$ (in the computational basis), obtaining the outcome $|b\rangle \in \{0,1\}^n$

**1.3** Store $U | b\rangle \langle b| U^\dagger$ in the memory of a classical computer

Now let us consider the expectation value of $U | b\rangle \langle b| U^\dagger$. Note that there are two random variables here, $U$ and $|b\rangle$. The expectation value we refer to is with respect to these two random variables, namely:

$$\begin{aligned} &\mathbb{E}_{U,b}[U^\dagger |b\rangle\langle b| U^\dagger] \\ &:= \mathbb{E}_U\left[\sum_{b=0,1} \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right] \end{aligned}$$

It can be proven that this is a quantum channel, denoted by:

$$\mathcal{M}(\rho):=\mathbb{E}_{U\sim \nu}\left[\sum_{b=1}^d \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right]$$

where $\nu$ is the distribution followed by $U$, which is a uniform distribution. Its probability space is not the usual number line, but a group—here, the Clifford group.

It can be proven (the proof is given in the next section) that $\mathcal{M}(\rho)$ can be written analytically as:

$$\boxed{ \mathcal{M}(\rho)= \frac{\rho + \operatorname{tr}[\rho] \mathbb{I}}{d+1} }$$

where $d=2^n$ is the dimension of the Hilbert space. This $\mathcal{M}(\rho)$ is in fact a depolarizing channel.

Thus, the inverse of $\mathcal{M}$ can be obtained directly as:

$$\boxed{ \mathcal{M}^{-1}(X)=(d+1) X - \operatorname{tr}[X]\mathbb{I} }$$

We can therefore use $\mathcal{M}^{-1}(U|b\rangle\langle b| U^\dagger)$ as an estimator of $\rho$:

$$\boxed{ \begin{aligned} \hat{\rho}&=\mathcal{M}^{-1}(U|b\rangle\langle b| U^\dagger)\\ &=(d+1) U|b\rangle\langle b| U^\dagger - \mathbb{I} \end{aligned} }$$

This estimator is unbiased because

$$\boxed{ \mathbb{E}[\hat{\rho}]=\rho }$$

Now, by repeating step 1 $N$ times, we can obtain $N$ $\hat{\rho}$:

$$\boxed{ S(\rho,N)=\{\hat{\rho}_1,\hat{\rho_2},...,\hat{\rho}_N\} }$$

This $S(\rho,N)$ is the classical shadow of $\rho$.

Thus, the second step (estimating the expectation value $\{o_1,..., o_M\}$ of $\{O_1,...,O_M\}$) is straightforward:

$$\hat{o_i}=\operatorname{tr}[\hat{\rho} O_i] = \operatorname{tr}[\sum_{k}\hat{\rho}_k O_i]$$

To avoid the effect of outliers and guarantee the success probability, in practice we need to use the median-of-means method: divide $S(\rho,N)$ into $K$ parts, calculate $\hat{o_i}$ for each part, and then take the median of the $K$ results.

### 3.2 Haar Measure and Unitary t-design  

Clearly, the key to why the procedure described in the previous section works lies in the following equation:

$$\boxed{ \mathcal{M}(\rho)= \frac{\rho + \operatorname{tr}[\rho] \mathbb{I}}{d+1} }$$

How can this equation be proven? We need some knowledge of Haar measure and t-designs.

Intuitively, Haar measure is the “uniform” distribution on a group. Since the probability distribution (measure) we consider is over the space formed by unitary operators (that is, the $U(d)$ group), rather than an ordinary number line, concepts such as a “uniform” distribution require special characterization.

> **Haar Measure**  
>   
> Given a group $U(d)$ and one of its Borel subsets $S$, if for every $g\in U(d)$, the measure $\mu$ satisfies:  
>  $\mu(g S)=\mu(S)=\mu(Sg)$  
> then $\mu$ is called a Haar measure.  
>   
> Here $U(d)$ refers to the $d$-dimensional unitary group, namely, the group of all unitary operators on a $d$-dimensional Hilbert space. A Borel subset can be understood as the simplest type of $\sigma$-algebra, namely, a collection of measurable sets.

Thus, Haar measure defines “uniformity” through translation invariance.

Intuitively, if we want the error of quantum state tomography to be uniform, then we would like to randomly select quantum gates from $U(d)$ according to Haar measure.

However, on actual quantum hardware, for ease of operation or due to hardware limitations, we generally do not select quantum gates from the continuous $U(d)$. The usual approach is to select uniformly at random from a finite set of quantum gates. The Clifford group is generally selected as this set.

This naturally leads to a direct question: **Can the uniform distribution over a finite group “approximate” or “simulate” the uniform distribution over a continuous group?**

More specifically, given the Haar measure $\mu$ on $U(d)$ and a measure $\nu$ on its finite subset $S \subsetneq U(d)$, can $\nu$ satisfy

$$\mathbb{E}_{V\sim \nu}[V^{\otimes t}O V^{\dagger \otimes t}] = \mathbb{E}_{U \sim \mu}[U^{\otimes t}O U^{\dagger \otimes t}]$$

for any operator $O \in \mathcal{L}({\mathcal{H}^{\otimes t}})$ on the Hilbert space $\mathcal{H}^{\otimes t}:= (\mathbb{C}^d)^{\otimes t}$?

If so, then $\nu$ is called a **unitary t-design**. Hereafter, it is referred to simply as a t-design.

For convenience, define the $M^{(t)}(A)$-th moment of an operator $A\in \mathcal{L}({\mathcal{H}^{\otimes t}})$ as:

$$M^{(t)}(A):=\mathbb{E}_{U \sim \mu}[U^{\otimes t}A U^{\dagger \otimes t}]$$

Thus, the definition of a t-design can be summarized in one sentence:

> **Unitary t-design**  
>   
> A measure $\nu$ on a finite subset of $U(d)$ is called a unitary t-design if its t-th moment is the same as the t-th moment of the Haar measure.

### 3.3 Schur-Weyl Duality  

Now let us consider the t-th moment $M^{(t)}$ of the Haar measure. It has many useful properties, which we will state without proof below.

First, we turn $\mathcal{L}(\mathcal{H}^{\otimes t})$ into an inner-product space through the Hilbert-Schmidt inner product (HS inner product). The HS inner product is defined as:

$$\langle A ,B\rangle := \operatorname{tr}[A^\dagger B], \quad A,B \in \mathcal{L}(\mathcal{H^{\otimes t}})$$

Once we have an inner product, we can define projections. The t-th moment is precisely a projection operator on this inner-product space.

> **Theorem: The t-th moment** $M^{(t)}$ **is the projection operator onto the commutant**  
>   
> $M^{(t)} \in \mathcal{L}(\mathcal{L}(\mathcal{H}^{\otimes t}))$ is a projection operator on the HS inner-product space $\mathcal{L}(\mathcal{H}^{\otimes t})$. It projects an operator $A$ onto the subspace $\text{Comm}^{(t)}(U(d))$, where $\text{Comm}^{(t)}(U(d))$ is the **commutant** of $U(d)$, defined as the set of all operators that commute with $B^{\otimes t}$:  
>   
> $\text{Comm}^{(t)}(S) :=\{A \in \mathcal{L}(\mathcal{H}^{\otimes t}) \mid [A,B^{\otimes t}] = 0\quad\forall B\in S\}$  
>   
> It can be proven that $\text{Comm}^{(t)}(U(d))$ is a subspace of $\mathcal{L}(\mathcal{H}^{\otimes t})$.  
>   
> In group theory, a commutant is also called a centralizer.

In other words, the t-th moment $M^{(t)}(A)$ of any operator always lies in the commutant.

What properties, then, does this commutant have?

> **Schur-Weyl duality: The commutant is the space spanned by all permutation operators**  
>   
> $\text{Comm}^{(t)}(U(d)) = \operatorname{span}(V_d(\pi): \pi \in S_t)$  
>   
> where the permutation operator $V_d(\pi) \in \mathcal{L}(\mathcal{H}^{\otimes t})$ is defined as:  
>   
> $V_d(\pi) |\psi_1\rangle \otimes \cdots \otimes |\psi_t\rangle := |\psi_{\pi^{-1}(1)}\rangle \otimes \cdots \otimes |\psi_{\pi^{(-1)}(t)}\rangle$

With Schur-Weyl duality, we can use the permutation operators $V_{d}(\pi)$ as a basis for the commutant.

> However, permutation operators are not mutually orthogonal as a basis for the commutant, because $\langle V_d(\pi), V_{d}(\sigma)\rangle \ne \delta_{\pi,\sigma}$.  
>   
> In fact: $\langle V_d(\pi), V_{d}(\sigma)\rangle = \operatorname{tr}[V_d(\pi)^{\dagger} V_{d}(\sigma)] = \operatorname{tr}[V_d(\pi^{-1}\sigma)]=d^{\# \text{cycle}(\pi^{-1}\sigma)}$  
> where $\#\text{cycle}(\pi)$ is the number of cycles of the permutation $\pi$ (the number of closed loops in the permutation diagram).

Therefore, **the t-th moment** $M^{(t)}(A)$ **of any operator can be written as a linear combination of permutation operators corresponding to the t-th permutation group.**

Using this, we can easily calculate the first and second moments, because the first permutation group is trivial and contains only the identity operator $\mathbb{I}$, while the second permutation group contains only the identity operator $\mathbb{I}_2 = \mathbb{I}^{\otimes2}$ and the SWAP operator, denoted $F := \mathsf{SWAP}$.

> **First and second moments of an operator**:  
> $\boxed{ M^{(1)}(A):=\mathbb{E}_{U \sim \mu}[UA U^\dagger]=\operatorname{tr}[A] \frac{\mathbb{I}}{d}  }$  
> $\boxed{ M^{(2)}(A):=\mathbb{E}_{U \sim \mu}[U^{\otimes 2}A U^{\dagger \otimes 2}] = \alpha\ \mathbb{I}_2+ \beta\ F}$  
> where  
> $\alpha = \frac{\operatorname{tr}(O)-d^{-1}\operatorname{tr}(FO)}{d^2-1}, \quad \beta = \frac{\operatorname{tr}(FO)-d^{-1}\operatorname{tr}(O)}{d^2-1}$  
> Proof hint: Write the moment as a linear combination of permutation operators, then take the trace of both sides to solve for the coefficients.

In particular, the second moment of a pure state is:

> **Second moment of a pure state**  
> $\boxed{ M^{(2)}(|\psi\rangle\langle\psi|)=\frac{\mathbb{I}_2+ F}{d(d+1)} }$  
> where $|\psi\rangle \in \mathcal{H}^{\otimes 2}$.  
> Proof hint: Calculate directly from the formula.  
> In fact, **the t-th moment of a pure state is an equal-weight linear combination of the permutation operators of all t-th permutation groups**.

Finally, we state without proof that **the uniform distribution over the Clifford group forms a 3-design**. Moreover, a (t+1)-design is also a t-design. Therefore, the uniform distribution over the Clifford group is also a 2-design. We will use these facts in the next section.

### 3.4 Measurement Channel  

With the groundwork on Haar measure and t-designs laid, we can now prove that the measurement channel can be written in the following analytical form:

$$\begin{aligned} \mathcal{M}(\rho)&:=\mathbb{E}_{U\sim \nu}\left[\sum_{b=1}^d \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right] \\ &= \frac{\operatorname{tr}(\rho) \mathbb{I} + \rho}{d+1} \end{aligned}$$

> Proof:  
> By the properties of the partial trace,  
> $\begin{aligned} \mathcal{M}(\rho)&:=\mathbb{E}_{U\sim \nu}\left[\sum_{b=1}^d \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right] \\ &= \sum_{b=1}^d \operatorname{tr}_1\left( (\rho \otimes \mathbb{I}) \mathbb{E}_{U\sim \nu} [U^{\otimes 2} |b\rangle\langle b|^{\otimes 2}U^{\dagger\otimes 2}]\right) \end{aligned}$  
> Since $\nu$ is a 2-design, its second moment is the same as the second moment of the Haar measure:  
> $\begin{aligned} \mathbb{E}_{U\sim \nu} [U^{\otimes 2} |b\rangle\langle b|^{\otimes 2}U^{\dagger\otimes 2}] &= \frac{\mathbb{I} \otimes \mathbb{I}+ F}{d(d+1)} \end{aligned}$  
> Therefore  
> $\begin{aligned} \mathcal{M}(\rho)&= \sum_{b=1}^d \operatorname{tr}_1\left( (\rho \otimes \mathbb{I}) \frac{\mathbb{I} \otimes\ \mathbb{I}+ F}{d(d+1)}\right) \\ &= \frac{d}{d(d+1)}\operatorname{tr}_1\left( (\rho \otimes \mathbb{I}) + F(\rho \otimes \mathbb{I})\right) \\ &= \frac{1}{d+1}(\operatorname{tr}(\rho)\mathbb{I}+ \rho) \end{aligned}$  
> Q.E.D.

### 3.5 Upper Bound on the Variance of the Estimator  

In the previous section, we proved

$$\boxed{ \mathcal{M}(\rho)= \frac{\rho + \operatorname{tr}[\rho] \mathbb{I}}{d+1} }$$

that is, we proved that

$$\boxed{ \begin{aligned} \hat{\rho}&=\mathcal{M}^{-1}(U|b\rangle\langle b| U^\dagger)\\ &=(d+1) U|b\rangle\langle b| U^\dagger - \mathbb{I} \end{aligned} }$$

is unbiased. In other words, the expectation value of the estimator $\hat{o_i}:= \operatorname{tr}(O_i \hat{\rho})$ of an operator equals the true value $\mathbb{E}[\hat{o}_i] = \operatorname{tr}[\rho O_i]$.

However, this alone is not enough: we have not provided an upper bound on the estimator's variance, and hence cannot determine the sample complexity.

Next, we prove that the upper bound on the variance of the estimator is $\boxed{\operatorname{Var}(\hat{o}_i) \le 3 \operatorname{tr}(O_i^2)}$.

> **Upper bound on the variance of the estimator**  
> The variance of the estimator is:  
> $\operatorname{Var}(\hat{o_i})=\mathbb{E}[\hat{o}_i^2]-\mathbb{E}[\hat{o}_i]^2$  
> where  
> $\mathbb{E}\left(\hat{\sigma}_i^2\right):=\sum_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\langle b| U \rho U^{\dagger}|b\rangle \operatorname{tr}\left(O_i \mathcal{M}^{-1}\left(U^{\dagger}|b\rangle\langle b| U\right)\right)^2\right]$  
> First, note that  
> $\operatorname{tr}(A \mathcal{M}(B))=\sum_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\langle b| U B U^{\dagger}|b\rangle\langle b| U A U^{\dagger}|b\rangle\right]=\operatorname{tr}(\mathcal{M}(A) B)$  
> so $\operatorname{tr}(A \mathcal{M}^{-1}(B))=\operatorname{tr}(\mathcal{M}^{-1}(A) B)$  
> Therefore  
> $\begin{aligned} \mathbb{E}\left(\hat{o}_i^2\right) & =\sum_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\langle b| U \rho U^{\dagger}|b\rangle \operatorname{tr}\left(\mathcal{M}^{-1}\left(O_i\right) U^{\dagger}|b\rangle\langle b| U\right)^2\right] \\ & =\sum_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\operatorname{tr}\left(\rho U^{\dagger}|b\rangle\langle b| U\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O_i\right) U^{\dagger}|b\rangle\langle b| U\right)^2\right] \\ & =\operatorname{tr}\left(\left(\rho \otimes \mathcal{M}^{-1}\left(O_i\right) \otimes \mathcal{M}^{-1}\left(O_i\right)\right)\left(\sum_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[U^{\dagger \otimes 3}|b\rangle\left\langle b\right|^{\otimes 3} U^{\otimes 3}\right]\right)\right) \end{aligned}$  
> where the final step uses $\operatorname{tr}(A \otimes B) = \operatorname{tr}(A) \operatorname{tr}(B)$.  
> Since $\nu$ is a 3-design,  
> $\begin{aligned} \underset{U \sim \nu}{\mathbb{E}}\left[U^{\dagger \otimes 3}|b\rangle\left\langle b\right|^{\otimes 3} U^{\otimes 3}\right] = \frac{1}{d(d+1)(d+1)}\underset{\pi \in S_3}{\sum}V_d(\pi) \end{aligned}$  
> Therefore  
> $\begin{aligned} &\operatorname{tr}\left(\left(\rho \otimes \mathcal{M}^{-1}\left(O_i\right) \otimes \mathcal{M}^{-1}\left(O_i\right)\right)\left(\sum_{\pi \in S_3} V_d(\pi)\right)\right) \\ & =\operatorname{tr}(\rho) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O_i\right)\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O_i\right)\right)+\operatorname{tr}(\rho) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O_i\right)^2\right)\\ & \quad+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O_i\right)\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O_i\right)\right) +\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O_i\right)^2\right)\\ & \quad+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O_i\right)^2\right)+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O_i\right)\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O_i\right)\right)   \end{aligned}$ (\*)  
> Now we use a trick: the variance $\operatorname{Var}\left(\hat{o}_i\right)=\mathbb{E}\left[\left(\hat{o}_i-\operatorname{Tr}\left(O_i \rho\right)\right)^2\right]$ depends only on the traceless part $O_i^{(0)} := O_i - \operatorname{tr}(O_i) \frac{\mathbb{I}}{d}$ of $O_i$. This is because  
> $\hat{o}_i-\operatorname{Tr}\left(O_i \rho\right)=\operatorname{Tr}\left(O_i \hat{\rho}\right)-\operatorname{Tr}\left(O_i \rho\right)=\operatorname{Tr}\left(O_i^{(0)} \hat{\rho}\right)-\operatorname{Tr}\left(O_i^{(0)} \rho\right)$  
> Note that $\mathcal{M}$ is trace-preserving.  
> Therefore, in the expression for the variance, all $O_i$ can be replaced by $O_i^{(0)}$:  
> $\begin{aligned} & \operatorname{tr}\left(\left(\rho \otimes \mathcal{M}^{-1}\left(O_i^{(0)}\right) \otimes \mathcal{M}^{-1}\left(O_i^{(0)}\right)\right)\left(\sum_{\pi \in S_3} V_d(\pi)\right)\right) \\ & =0+\operatorname{tr}(\rho) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O_i^{(0)}\right)^2\right)+0+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O_i^{(0)}\right)^2\right)+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O_i^{(0)}\right)^2\right)+0 \\ & =(d+1)^2 \operatorname{tr}\left(O_i^{(0) 2}\right)+2(d+1)^2 \operatorname{tr}\left(\rho O_i^{(0) 2}\right) \end{aligned}$  
> Thus  
> $\begin{aligned} \operatorname{Var}\left(\hat{o}_i\right) & =\frac{(d+1)^2}{(d+1)(d+2)}\left(\operatorname{tr}\left(O_i^{(0) 2}\right)+2 \operatorname{tr}\left(\rho O_i^{(0) 2}\right)\right)-\operatorname{tr}\left(O_i^{(0)} \rho\right)^2 \\ & \leq \operatorname{tr}\left(O_i^{(0) 2}\right)+2 \operatorname{tr}\left(\rho O_i^{(0) 2}\right) \\ & \leq 3 \operatorname{tr}\left(O_i^{(0) 2}\right) \\ & \leq 3 \operatorname{tr}\left( O_i^2\right) \end{aligned}$  
> Q.E.D.

### 3.6 Sample Complexity  

In Section II, we used Hoeffding's inequality to obtain a loose upper bound on sample complexity. Here, we use median-of-means estimation to obtain a loose upper bound on sample complexity.

> **Median-of-means estimation**  
> Given $N$ independent identically distributed random variables $X_i,\,i=1,...,N$, with expectation $\mu$ and variance $\sigma^2$. Divide them into $k$ groups, each containing $m=N/k$ random variables. Then the variance of the mean $\hat{\mu}_j = \sum_{i=j}^{j+m-1} X_i$ of one group is $\sigma^2/m$. By **Chebyshev's inequality**,  
> $\begin{aligned} P(|\hat{\mu}_j - \mu| \gt \epsilon ) \le \frac{\sigma^2}{m \epsilon^2} \end{aligned}$  
> Let the right-hand side equal $p$. Then $m= \sigma^2/(p\epsilon^2)$.  
> Define the random variable:  
> $Z_j = \begin{cases} 1,& |\hat{\mu}_j - \mu| \gt \epsilon \\ 0,& |\hat{\mu}_j - \mu| \le \epsilon \end{cases}$  
> Since we ultimately take the median of $\hat{\mu}_1,...,\hat{\mu}_k$, we want the probability $P\left(\sum_{j=1}^k Z_j \gt \frac{k}{2}\right)$ that more than half of the $\hat{\mu}_j$ have an error greater than $\epsilon$ to be sufficiently small.  
> Let $S=\sum_{j=1}^k Z_j$. By **Hoeffding's inequality**,  
> $P(S-\mathbb{E}(S)\gt t)\le \exp\left(-\frac{2t^2}{k}\right)$  
> where $\mathbb{E}(S) \le kp$. Let $t = k/2 - kp$. Then:  
> $P\left(S\gt \frac{k}{2}\right) \le P(S-\mathbb{E}(S)\gt t)\le \exp\left(-2k\left(\frac{1}{2}-p\right)^2\right)$  
> Without loss of generality, let $p = 1/4$. Then  
> $P\left(\sum_{j=1}^k Z_j \gt \frac{k}{2}\right) \le \exp\left( - \frac{k}{8}\right)$  
> Setting the right-hand side equal to $\delta$ gives $k =8 \log (1/\delta)$.  
> Since $m=\sigma^2/(p\epsilon^2) =4\sigma^2/\epsilon^2$,  
> $\boxed{ N = km =32 \sigma^2 \log(1/\delta)/\epsilon^2 }$  
> This is the number of samples required to estimate $\hat{\mu}$ within error $\epsilon$ at a failure rate below $\delta$.

Now apply median of means to our problem. The variance $\sigma^2$ of $X_i:= \hat{o}_i$ satisfies $\sigma^2 \le 3 \operatorname{tr}(O_i^2) = 3||O_i||^2$. Substitution gives

$$N  = 96 ||O_i||^2\log(1/\delta)/\epsilon^2$$

Now we want to simultaneously estimate $M$ $\hat{o}_i$, namely $\hat{o}_1,...,\hat{o}_M$.

When applying Hoeffding's inequality:

$$P(S-\mathbb{E}(S)\gt t)\le \exp\left(-\frac{2t^2}{k}\right)$$

We can select $M$ $S_i$, namely $S_1, ..., S_M$, and take a union bound:

$$P(S_i-\mathbb{E}(S_i)\gt t,\ \exists S_i \in\{S_1,...,S_M\})\le M\exp\left(-\frac{2t^2}{k}\right)$$

The key to logarithmic complexity lies here: when taking the union bound, $M$ appears outside the exponent. Therefore, when solving in reverse for $N$, $M$ appears inside the logarithm.

Therefore, we can prove that the sample complexity is:

$$\boxed{ N  = O\left( \log(M/\delta)\max_i||O_i||^2 /\epsilon^2 \right) }$$

### 3.7 Pauli Measurements  

All the derivations introduced above are based on Clifford measurements. However, Clifford measurement is a global measurement, requiring entangling gate operations on the individual qubits before measurement in the computational basis.

In practice, local measurements are more commonly used: single-qubit gate operations are performed separately on each qubit, followed by measurements in the computational basis. Usually, these gates are selected from the single-qubit Clifford group, which can implement measurements in the Pauli bases (namely, $X, Y, Z$). In this case, sample complexity also depends on the locality of the operator to be measured. This is obvious: if the operator to be measured is highly entangled, it is difficult to expect a small number of local measurements to reveal information about the entanglement.

(To be continued)

### 3.8 Derandomization  

Classical shadows differ greatly from conventional FST. In conventional FST, we measure the same number of samples in every measurement basis, which ensures that the error is more uniform to some extent. In classical shadows, however, because the measurement bases are selected randomly, the numbers of samples under different measurement bases also differ.

This raises the question: compared with randomly selecting bases, would it be better to set the number of samples under different measurement bases to be the same? This is the so-called derandomization.

(To be continued)

## References  

1. [^](#ref\_1\_0)Cotler, J. & Wilczek, F. Quantum Overlapping Tomography. Phys. Rev. Lett. 124, 100401 (2020).
2. [^](#ref\_2\_0)Acharya, Jayadev, et al. "Pauli measurements are not optimal for single-copy tomography." Proceedings of the 57th Annual ACM Symposium on Theory of Computing. 2025.
3. [^](#ref\_3\_0)Nayak, A., & Lowe, A. (2025). Lower bounds for learning quantum states with single-copy measurements. ACM Transactions on Computation Theory.
4. [^](#ref\_4\_0)O’Donnell, R. & Wright, J. Efficient quantum tomography. in Proceedings of the forty-eighth annual ACM symposium on Theory of Computing 899–912 (ACM, Cambridge MA USA, 2016). doi:10.1145/2897518.2897544.
5. [^](#ref\_5\_0)Haah, J., Harrow, A. W., Ji, Z., Wu, X. & Yu, N. Sample-optimal tomography of quantum states. in Proceedings of the forty-eighth annual ACM symposium on Theory of Computing 913–925 (ACM, Cambridge MA USA, 2016). doi:10.1145/2897518.2897585.
6. [^](#ref\_6\_0)Huang, H.-Y., Kueng, R. & Preskill, J. Predicting many properties of a quantum system from very few measurements. Nat. Phys. 16, 1050–1057 (2020).
7. [^](#ref\_7\_0)Aaronson, Scott. "Shadow tomography of quantum states." Proceedings of the 50th annual ACM SIGACT symposium on theory of computing. 2018.
