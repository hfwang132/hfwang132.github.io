---
title: "Classical Shadows of Quantum States"
date: 2025-05-30T02:53:53+08:00
originalURL: "https://zhuanlan.zhihu.com/p/1911107376045593900"
aliases:
  - "/en/classical_shadows/"
  - "/en/Post_20251012_量子态的经典阴影-Classical-Shadows/"
draft: false
tags: ["Classical Shadows", "Haar Measure"]
categories: ["Quantum Information"]
---

## I. Quantum State Tomography  

At present, quantum states consisting of hundreds or thousands of qubits can already be prepared (twenty references omitted here).

But how do we know that the prepared quantum state $\rho$ is indeed the one $\rho$ that we want? Or, more broadly: how can we learn (some or all) information about a quantum state $\rho$?

To learn a quantum state $\rho$, we first need to prepare $\rho$, then measure it in different measurement bases to obtain probability distribution functions, and finally use these probability distribution functions to learn $\rho$. This process is called **quantum state tomography**.

## II. Full Quantum State Tomography  

If our goal is to completely reconstruct $\rho$, that is, to learn all information about $\rho$, then this process is called **full state tomography (FST)**.

Taking a system composed of $n$ qubits as an example, its quantum state $\rho$ can be written as:

$\begin{aligned} \rho &= \frac{1}{2^n}\sum\_i c\_i P\_i \\\\ &\phantom{==}  P\_i = \sigma\_{i\_1}\otimes \cdots \otimes \sigma\_{i\_n}, \quad i=(i\_1,...,i\_n), \quad i\_k= 0,1,2,3 \\\\ &\phantom{==} \sigma\_0=\mathbb{I},\  \sigma\_1=X,\ \sigma\_2 = Y,\ \sigma\_3=Z  \end{aligned}$

where $\sigma\_0=\mathbb{I},\  \sigma\_1=X,\ \sigma\_2 = Y,\ \sigma\_3=Z$ are the single-qubit Pauli matrices, and $c\_i = \operatorname{tr}[\rho P\_i]$.

Clearly, as long as we measure the expectation values $c\_i = \operatorname{tr}[\rho P\_i]$ of the operators $P\_i$, we can perform FST on the quantum state $\rho$. These $c\_i$ are called Pauli coefficients.

There are a total of $4^n - 1$ Pauli coefficients to measure, because $P\_0 = \mathbb{I}^{\otimes n}$ is the identity matrix, causing $c\_{0}$ to always equal 1.

This measurement method is called Pauli measurements, and it is the method most commonly used.

> Note that in practice only $3^n$ measurement bases are needed, because the measurement outcomes for the remaining $(4^n-3^n-1)$ $P\_i$ are the marginal distributions of the outcomes for these $3^n$ $P\_j$.  
>   
> For example, the measurement outcomes of $\mathbb{I}\otimes Y$ can be obtained entirely from those of $X \otimes Y$—because the probability distribution of the former is a marginal distribution of that of the latter.

This article mainly considers systems composed of $n$ qubits, though the extension to qudits is also straightforward. However, continuous-variable systems are not discussed here.

### 2.1 Sample Complexity  

As mentioned above, to learn a quantum state $\rho$, we need to first prepare multiple copies of $\rho$ and then measure them in different measurement bases. This naturally raises a direct question:

**For a** $d$ **-dimensional quantum state** $\rho$**, how many copies are needed to estimate** $\rho$ **within an error** $\epsilon$**?**

> A $d$-dimensional quantum state $\rho$ is defined as a positive semidefinite operator with trace 1 on a $d$-dimensional Hilbert space. It is also commonly called a density matrix and is characterized by $D^2-1$ real parameters.

To better understand and formulate this question, let us first introduce some terminology. We define **sample complexity** as follows: as the dimension $d$ increases and the error $\epsilon$ decreases, the required number of samples $N$ also grows. The rate of growth $N \sim O(f(d,\epsilon))$ is the sample complexity.

For a single qubit, $d=2$, whereas for a system composed of $n$ qubits, it is $d=2^n$. For $n$ k-dimensional qudits, it is $d=k^n$. Thus, the dimension of the Hilbert space grows exponentially with the number of particles.

Next, let us consider the error $\epsilon$. The two most commonly used functions for characterizing the error between two quantum states $\rho$ and $\sigma$ are **fidelity** $F(\rho,\sigma)$ and **trace distance** $T(\rho,\sigma)$:

$F(\rho,\sigma):=\operatorname{tr}\left[\sqrt{\sqrt{\sigma}\rho\sqrt{\sigma}}\right]^2$   
 $T(\rho,\sigma):=\frac{1}{2}||\rho-\sigma||\_1$

where $||\cdot||\_1$ is the trace norm / 1-norm, defined as $|| A||\_1 =\operatorname{tr}\left[\sqrt{A^\dagger A}\right]$.

The closer the fidelity is to 1 and the closer the trace distance is to 0, the smaller the error. They satisfy:

$1-\sqrt{F} \le T \le \sqrt{1-F}$

If trace distance $T(\rho,\sigma)$ is used as the error $\epsilon$, then the error $\delta:=1-F$ calculated using fidelity satisfies $\delta\ge \epsilon^2$.

This article mainly uses $||\rho - \sigma||\_1$ as the error.

### 2.2 Upper Bounds on Sample Complexity  

Intuitively, to reconstruct a quantum state $\rho$, the dependence of sample complexity on $d$ must be at least $\sim d^2$, or equivalently $\Omega(d^2)$. This is because we need at least $\sim d^2$ measurement-basis (POVM) elements for the measurement basis to be informationally complete. On the other hand, repeated measurements are needed for the estimator to approach the true value. To ensure that the error between the two is less than $\epsilon$, the relationship between sample complexity and error $\epsilon$ should be approximately inverse, $\sim O(\epsilon^{-m})$.

Therefore, we conjecture that the sample complexity is $\boxed{ N = O(d^l/\epsilon^m) }$, where $l \ge 2$. Next, we study the sample complexity under different measurement schemes.

### 2.3 Complexity of Pauli Measurements  

Next, we give a relatively loose upper bound on sample complexity [1], obtained using the Pauli measurements mentioned above, which are also the most commonly used method.

We first introduce Hoeffding's inequality, which will be used later:

> **Hoeffding's Inequality**  
> Given $N$ independent random variables $X\_i,\ i=1,...,N$ with respective ranges $[a\_i,b\_i]$, their sum $S=\sum\_iX\_i$ satisfies  
> $\begin{aligned} P(|S-\mathbb{E}(S)| \ge \epsilon) < 2\exp \left[-\frac{2 N^2 \epsilon^2}{\sum\_{i}(b\_i-a\_i)^2}  \right] \end{aligned}$   
> If $X\_1,...,X\_N$ have identical distributions, range $[a,b]$, and mean $Y = S/N=\sum\_iX\_i /N$, then  
>  $\begin{aligned} P(|Y-\mathbb{E}(Y)| \ge \epsilon) < 2\exp \left[ -\frac{2 N \epsilon^2}{(b-a)^2} \right] \end{aligned}$

Next, we apply Hoeffding's inequality.

> For the quantum state $\rho = \frac{1}{2^n}\sum\_i c\_i P\_i $, repeatedly measure the operator $P\_i$, and let the average of the outcomes be an estimator $\hat{c}\_i$ of $c\_i = \operatorname{tr}[\rho P\_i]$.  
>   
> Applying Hoeffding's inequality to $\hat{c}\_i$, and noting that $\hat{c}\_i$ takes values $\pm1$, gives:  
>   
> $P[|\hat{c}\_i-c\_i| > \epsilon\_i] \le 2 \exp \left[-N\epsilon\_i^2/2\right]$   
>   
> where $N$ is the number of repeated measurements of $P\_i$.  
>   
> Then, by the union bound, among $(4^n-1)$ $c\_i$, the probability that any one $|\hat{c}\_i-c\_i| > \epsilon\_i$ is:  
>   
> $P[|\hat{c}\_i-c\_i| > \epsilon\_i, \ \exists \  i] \le (4^n - 1) \cdot 2 \exp \left[-N\delta^2/2\right]$   
>   
> Now, we want all $|\hat{c}\_i-c\_i|$ to be smaller than $\epsilon\_1$ with high probability. That is, the probability of an error greater than $\epsilon\_1$ should be a very small number $\delta \ll 1$. Setting the right-hand side above equal to $\delta$ gives:  
>   
> $N= \frac{2}{\epsilon\_1^2}\log \frac{2\cdot (4^n-1)}{\delta}= O\left(\frac{n -\log \delta}{\epsilon\_1^2}\right) $   
>   
> Substituting $d=2^n$ yields:  
>   
> $\boxed{ N= O(\log(d/\delta)/\epsilon^2\_1)  }$

This is the sample complexity required to estimate all Pauli coefficients within error $\epsilon\_1$ with a failure rate below $\delta$.

---

Note! Here, $\epsilon\_1$ is only the measurement error of a single Pauli coefficient $c\_i$, whereas what we want is the error $\epsilon$ of the density matrix $\rho = \frac{1}{2^n}\sum\_i c\_i P\_i $.

> To this end, we define the error matrix:  
>   
> $\Delta = \hat{\rho}-\rho = \sum\_i(\hat{c}\_i-c\_i)P\_i$   
>   
> and require its trace norm to be less than $\epsilon$:  
>   
> $||\Delta||\_1<\epsilon$   
>   
> Note that the Hilbert-Schmidt norm is easier to calculate: $||\Delta||\_2^2 := \operatorname{tr}[A^\dagger A] = \frac{1}{2^n}\sum\_i |\hat{c}\_i-c\_i|^2$, because   
> $\operatorname{tr}[P\_i^\dagger P\_j]=\operatorname{tr}[P\_iP\_j]=\delta\_{ij}$.  
>   
> We can therefore use the Cauchy inequality $||A||\_1 \le \sqrt{d}||A||\_2$, where $d = 2^n$ is the order of the matrix:  
>   
> $||\Delta||\_1 \le \sqrt{2^n}||\Delta||\_2 = (\sum\_i |\hat{c}\_i-c\_i|^2)^{1/2} \le (\sum\_i \epsilon\_1^2)^{1/2} = (4^n-1)^{1/2} \ \epsilon\_1$   
>   
> Let $||\Delta||\_1 \le \epsilon$; then $\epsilon \sim(4^n-1)^{1/2} \ \epsilon\_1\sim 2^n \epsilon\_1$, so  
>   
> $N \sim (n - \log \delta)/\epsilon\_1^2 \sim (n - \log \delta)4^n /\epsilon^2 = \log \frac{d}{\delta} \cdot d^2/\epsilon^{2}$   
>   
> Finally, considering that there are $3^n$ measurement bases and that $N$ measurements are required in each basis, we obtain:  
>   
> $N \mapsto 3^n \cdot N \sim \log \frac{d}{\delta}  \cdot d^{3.585} /\epsilon^{2}$

Usually, the failure rate $\delta$ is not included in the sample-complexity scaling, so:

$\boxed{ N = O(\log d  \cdot d^{3.585} /\epsilon^{2}) = O(N \cdot 12^N/\epsilon^2)} $

Update: In February 2025, the record for the upper bound was improved to $\boxed{ N = O(\log d  \cdot d^{3.322} /\epsilon^{2}) = O(N \cdot 10^N/\epsilon^2)} $, while the lower bound was proven to be $\Omega(d^{3.188}\log (d)/\epsilon^2)=\Omega(N \cdot 9.118^N /\epsilon^2)$ [2].

### 2.3 Sample Complexity of Single-Copy Measurements  

In fact, we can do better: the above upper bound can be reduced to $\boxed{O(\log d \cdot d^3 / \epsilon^{2})}$.

This is because $3^n$ measurement settings yield $3^n \cdot 2^n = 6^n = d^{2.585}$ POVM elements, whereas the minimum number of POVM elements required to guarantee informational completeness is $4^n = d^2$. Thus, we may use a SIC-POVM with exactly $d^2$ elements, or MUBs (Mutually Unbiased Bases), which contain $(d+1)$ measurement bases, each with $d$ elements, for a total of $d(d+1)$ POVM elements. Either method can reduce the upper bound on sample complexity to $O(\log d \cdot d^3 /\epsilon^{2})$.

The lower bound has been proven to be $\Omega(d^3 /\epsilon^{2})$ [3], though no concrete measurement scheme has yet been found. Compared with the upper bound, the lower bound removes the dependence on $\log(d)$, which has little impact in typical experiments.

### 2.4 Sample Complexity of Multi-Copy Measurements  

All the measurement methods above are single-copy measurements, because we measure only one copy at a time. We can consider a more general setting—jointly measuring multiple copies $\rho^{\otimes n}$ through entanglement—which is called multi-copy measurements. Such measurements require quantum memory and are essentially difficult to implement on current quantum hardware.

It has been proven that, for this most general type of measurement, the tight bound on sample complexity is $\boxed{\Theta(d^2 / \epsilon^{2})}$[4,5]. This was not proven until 2016.

Summary:

$\begin{aligned} \hline & \text{POVM} & \quad & \text{Sample Complexity}\ (d=2^n)\\\\ \hline  & \text{Pauli Measurements} & \quad & O(d^{3.322}\log (d)/\epsilon^2), \  \Omega(d^{3.188}\log (d)/\epsilon^2) \\\\ & \text{Single-copy measurements} & \quad & O(d^{3}\log (d)/\epsilon^2)^\dagger \\\\ & \text{Multi-copy measurements} & \quad & \Theta(d^2/\epsilon^2)\\\\ \hline \end{aligned}$

The $\dagger$ lower bound has been proven to be $\Omega(d^3 / \epsilon^2)$ [3], but no corresponding concrete measurement method exists.

## III. Classical Shadows  

In the previous section, we mentioned that if we measure all Pauli coefficients (the expectation values of Pauli operators), require the error of every result to be no greater than $\epsilon$, and require a failure rate no greater than $\delta$, then the sample complexity is:

$\boxed{ N = O\left(\frac{n-\log\delta}{\epsilon^2}\right)=O\left(\log \left(\frac{d}{\delta}\right) \cdot \epsilon^{-2}\right) }$

This reveals a seemingly astonishing fact: if we are concerned only with expectation values of operators rather than the quantum state itself, then sample complexity can be drastically reduced to logarithmic scaling.

In fact, for any $M$ operators $O\_1,...,O\_M$, if we wish to estimate their expectation values within error $\epsilon$ and with a failure rate below $\delta$, the required sample complexity is only:

$\boxed{ N \sim \log(M/\delta)\cdot \epsilon^{-2} \cdot (\max\_i||O\_i||^2\_{\text{shadow}}) }$

where the specific form of $||\cdot||\_{\text{shadow}}$ depends on the measurement method. This result comes from the famous 2020 work “Classical Shadows” by Huang et al. [6].

From the analysis in Section II, this complexity is not surprising. So why has “Classical Shadows” become so popular in recent years?

This is because previous research on sample complexity was often motivated by reducing theoretical upper bounds rather than by physical applications; even when measurement methods existed, they were difficult to realize experimentally and were more like what mathematicians call “theoretically existent.” Classical shadows, however, provide a simple, concrete, and effective measurement method: the implementation steps are highly explicit, and experimental physicists can use it out of the box. In addition, logarithmic complexity itself is an excellent selling point, even if it is not as surprising as it initially appears.

In fact, as early as 2017, Scott Aaronson proposed shadow tomography [7], which also identified logarithmic complexity $\log(M)$. However, he considered the probabilities $\operatorname{tr}[\rho E\_i]$ of $M$ two-outcome POVMs, rather than $M$ general physical-observable operators $\langle O\_i \rangle = \operatorname{tr}[\rho O\_i]$. Shadow Tomography received less attention than Classical Shadows partly because the measurement method it provided was relatively complicated.

> Fun fact: Scott Aaronson later went to work at OpenAI, but has recently left again.

### 3.1 A Concrete Implementation of Classical Shadows  

Now let us look at how Classical Shadows is carried out in practice.

Roughly speaking, the procedure consists of two steps:

**1.** Measure the quantum state to obtain Classical Shadows, and store them on a classical computer.

**2.** Estimate the expectation values of $M$ operators from the stored Classical Shadows using a certain algorithm.

Let us first look at **1**, which proceeds as follows:

**1.1** Randomly select a $U$ from the Clifford operators, apply it to the quantum state $\rho$, and obtain $U\rho U^\dagger$.

**1.2** Measure $U\rho U^\dagger$ (in the computational basis) and obtain the outcome $|b\rangle \in \{0,1\}^n$

**1.3** Store $U | b\rangle \langle b| U^\dagger$ in the memory of a classical computer.

Now let us examine the expectation value of $U | b\rangle \langle b| U^\dagger$. Note that there are two random variables here, $U$ and $|b\rangle$. The expectation value we refer to is with respect to these two random variables, namely:

$\begin{aligned} &\mathbb{E}\_{U,b}[U^\dagger |b\rangle\langle b| U^\dagger] \\\\ &:= \mathbb{E}\_U\left[\sum\_{b=0,1} \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right] \end{aligned}$

This can be shown to be a quantum channel, denoted by:

$\mathcal{M}(\rho):=\mathbb{E}\_{U\sim \nu}\left[\sum\_{b=1}^d \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right]$

where $\nu$ is the distribution followed by $U$, which is a uniform distribution. Its probability space is not the usual real line, but a group—here, the Clifford group.

It can be shown (the proof is in the next section) that $\mathcal{M}(\rho)$ can be written analytically as:

$\boxed{ \mathcal{M}(\rho)= \frac{\rho + \operatorname{tr}[\rho] \mathbb{I}}{d+1} }$

where $d=2^n$ is the dimension of the Hilbert space. This is a depolarizing channel.

Therefore, the inverse of $\mathcal{M}$ is:

$\boxed{ \mathcal{M}^{-1}(X)=(d+1) X - \operatorname{tr}[X]\mathbb{I} }$

We can thus use $\mathcal{M}(U|b\rangle\langle b| U^\dagger)$ as an estimator of $\rho$:

$\boxed{ \begin{aligned} \hat{\rho}&=\mathcal{M}^{-1}(U|b\rangle\langle b| U^\dagger)\\\\ &=(d+1) U|b\rangle\langle b| U^\dagger - \mathbb{I} \end{aligned} }$

This estimator is unbiased because

$\boxed{ \mathbb{E}[\hat{\rho}]=\rho }$

Now, by repeating Step 1 $N$ times, we obtain $N$ $\hat{\rho}$:

$\boxed{ S(\rho,N)=\{\hat{\rho}\_1,\hat{\rho\_2},...,\hat{\rho}\_N\} }$

This $S(\rho,N)$ is the classical shadow of $\rho$.

Thus, the second step (estimating the expectation value $\{o\_1,..., o\_M\}$ of $\{O\_1,...,O\_M\}$) is straightforward:

$\hat{o\_i}=\operatorname{tr}[\hat{\rho} O\_i] = \operatorname{tr}[\sum\_{k}\hat{\rho}\_k O\_i]$

To avoid the impact of outliers and improve the success rate, one actually needs to use the median-of-means method: divide $S(\rho,N)$ into $K$ parts, calculate $\hat{o\_i}$ for each part, and then take the median of the $K$ results.

### 3.2 Haar Measure and Unitary t-design  

Clearly, the key to the validity of the procedure described in the previous section is the following equation:

$\boxed{ \mathcal{M}(\rho)= \frac{\rho + \operatorname{tr}[\rho] \mathbb{I}}{d+1} }$

How can we prove this equation? We need some knowledge of Haar measure and t-designs.

Intuitively, Haar measure is the “uniform” distribution on a group. Since the probability distribution (measure) under consideration is over the space formed by unitary operators (that is, the $U(d)$ group), rather than the ordinary real line, concepts such as a “uniform” distribution require a special characterization.

> **Haar Measure**  
>   
> Given a group $U(d)$ and one of its Borel subsets $S$, if for every $g\in U(d)$, the measure $\mu$ satisfies:  
>  $\mu(g S)=\mu(S)=\mu(Sg)$   
> then $\mu$ is called a Haar measure.  
>   
> Here $U(d)$ denotes the $d$-dimensional unitary group, namely the group of all unitary operators on a $d$-dimensional Hilbert space. A Borel subset may be understood as the simplest kind of $\sigma$-algebra, namely a collection of measurable sets.

Thus, Haar measure defines “uniformity” using translation invariance.

Intuitively, if we want the error in quantum state tomography to be uniform, then we would like to randomly select quantum gates from $U(d)$ according to Haar measure.

However, on practical quantum hardware, for ease of operation or due to hardware limitations, we generally do not select quantum gates from the continuous $U(d)$. The usual approach is to select uniformly at random from a finite set of quantum gates. The Clifford group is generally chosen as this set.

This naturally raises a direct question: can the uniform distribution over a finite group “approximate” or “simulate” the uniform distribution over a continuous group?

More specifically, given the Haar measure $\mu$ on $U(d)$ and a measure $\nu$ on its finite-element subset $S \subsetneq U(d)$, can $\nu$ satisfy

$\mathbb{E}\_{V\sim \nu}[V^{\otimes t}O V^{\dagger \otimes t}] = \mathbb{E}\_{U \sim \mu}[U^{\otimes t}O U^{\dagger \otimes t}]$

for every operator $O \in \mathcal{L}({\mathcal{H}^{\otimes t}})$ on the Hilbert space $\mathcal{H}^{\otimes t}:= (\mathbb{C}^d)^{\otimes t}$?

If so, then $\nu$ is called a **unitary t-design**. Hereafter, abbreviated as t-design.

For convenience, define the $M^{(t)}(A)$-th moment of an operator $A\in \mathcal{L}({\mathcal{H}^{\otimes t}})$ as:

$M^{(t)}(A):=\mathbb{E}\_{U \sim \mu}[U^{\otimes t}A U^{\dagger \otimes t}]$

We can then summarize the definition of a t-design in one sentence:

> **Unitary t-design**  
>   
> A measure $\nu$ on a finite subset of $U(d)$ is called a unitary t-design if its t-th moment is the same as the t-th moment of Haar measure.

### 3.3 Schur-Weyl Duality  

Now let us examine the t-th moment $M^{(t)}$ of Haar measure. It has many useful properties, which we state below without proof.

First, we turn $\mathcal{L}(\mathcal{H}^{\otimes t})$ into an inner-product space using the Hilbert-Schmidt inner product (HS inner product). The HS inner product is defined as:

$\langle A ,B\rangle := \operatorname{tr}[A^\dagger B], \quad A,B \in \mathcal{L}(\mathcal{H^{\otimes t}})$

With an inner product, we can define projections. The t-th moment is precisely a projection operator on this inner-product space.

> **The t-th moment** $M^{(t)}$ **is the projection operator onto the commutant**  
>   
> $M^{(t)} \in \mathcal{L}(\mathcal{L}(\mathcal{H}^{\otimes t}))$ is a projection operator on the HS inner-product space $\mathcal{L}(\mathcal{H}^{\otimes t})$. It projects the operator $A$ onto the subspace $\text{Comm}^{(t)}(U(d))$, where $\text{Comm}^{(t)}(U(d))$ is the **commutant** of $U(d)$, defined as the set of all operators that commute with $B^{\otimes t}$:  
>   
> $\text{Comm}^{(t)}(S) :=\{A \in \mathcal{L}(\mathcal{H}^{\otimes t}) \mid [A,B^{\otimes t}] = 0\quad\forall B\in S\}$   
>   
> It can be shown that $\text{Comm}^{(t)}(U(d))$ is a subspace of $\mathcal{L}(\mathcal{H}^{\otimes t})$.  
>   
> In group theory, the commutant is also called the centralizer.

In other words, the t-th moment $M^{(t)}(A)$ of any operator always lies in the commutant.

What properties, then, does this commutant have?

> **Schur-Weyl duality: the commutant is the space spanned by all permutation operators**  
>   
> $\text{Comm}^{(t)}(U(d)) = \operatorname{span}(V\_d(\pi): \pi \in S\_t)$   
>   
> where the permutation operator $V\_d(\pi) \in \mathcal{L}(\mathcal{H}^{\otimes t})$ is defined as:  
>   
> $V\_d(\pi) |\psi\_1\rangle \otimes \cdots \otimes |\psi\_t\rangle := |\psi\_{\pi^{-1}(1)}\rangle \otimes \cdots \otimes |\psi\_{\pi^{(-1)}(t)}\rangle$

With Schur-Weyl duality, we can use the permutation operators $V\_{d}(\pi)$ as a basis for the commutant.

> However, permutation operators are not mutually orthogonal as a basis for the commutant, because $\langle V\_d(\pi), V\_{d}(\sigma)\rangle \ne \delta\_{\pi,\sigma}$.  
>   
> In fact: $\langle V\_d(\pi), V\_{d}(\sigma)\rangle = \operatorname{tr}[V\_d(\pi)^{\dagger} V\_{d}(\sigma)] = \operatorname{tr}[V\_d(\pi^{-1}\sigma)]=d^{# \text{cycle}(\pi^{-1}\sigma)}$   
> where $#\text{cycle}(\pi)$ is the number of cycles of the permutation $\pi$ (the number of closed loops in the permutation graph).

Thus, the t-th moment $M^{(t)}(A)$ of any operator can be written as a linear combination of the permutation operators corresponding to the t-th permutation group.

Using this, we can easily calculate the first and second moments, because the first permutation group is trivial and contains only the identity operator $\mathbb{I}$, while the second permutation group contains only the identity operator $\mathbb{I}\_2 = \mathbb{I}^{\otimes2}$ and the SWAP operator, denoted $F := \mathsf{SWAP}$.

> **First and second moments of an operator**:  
> $\boxed{ M^{(1)}(A):=\mathbb{E}\_{U \sim \mu}[UA U^\dagger]=\operatorname{tr}[A] \frac{\mathbb{I}}{d}  }$   
> $\boxed{ M^{(2)}(A):=\mathbb{E}\_{U \sim \mu}[U^{\otimes 2}A U^{\dagger \otimes 2}] = \alpha\ \mathbb{I}\_2+ \beta\ F}$   
> where  
> $\alpha = \frac{\operatorname{tr}(O)-d^{-1}\operatorname{tr}(FO)}{d^2-1}, \quad \beta = \frac{\operatorname{tr}(FO)-d^{-1}\operatorname{tr}(O)}{d^2-1}$   
> Proof sketch: write the moments as linear combinations of permutation operators, then take the trace of both sides to solve for the coefficients.

In particular, the second moment of a pure state is:

> **Second moment of a pure state**  
> $\boxed{ M^{(2)}(|\psi\rangle\langle\psi|)=\frac{\mathbb{I}\_2+ F}{d(d+1)} }$   
> where $|\psi\rangle \in \mathcal{H}^{\otimes 2}$.  
> Proof sketch: compute directly from the formula.  
> In fact, the t-th moment of a pure state is an equal-weight linear combination of the permutation operators of the t-th permutation group.

Finally, we state without proof that the uniform distribution over the Clifford group forms a 3-design. Moreover, a (t+1)-design is also a t-design. Therefore, the uniform distribution over the Clifford group is also a 2-design. We will use these facts in the next section.

### 3.4 Measurement Channel  

With the groundwork on Haar measure and t-designs in place, we can now prove that the measurement channel can be written in the following analytic form:

$\begin{aligned} \mathcal{M}(\rho)&:=\mathbb{E}\_{U\sim \nu}\left[\sum\_{b=1}^d \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right] \\\\ &= \frac{\operatorname{tr}(\rho) \mathbb{I} + \rho}{d+1} \end{aligned}$

> Proof:  
> By the properties of the partial trace, we have  
> $\begin{aligned} \mathcal{M}(\rho)&:=\mathbb{E}\_{U\sim \nu}\left[\sum\_{b=1}^d \langle b | U \rho U^\dagger | b\rangle (U^\dagger |b\rangle\langle b| U^\dagger)\right] \\\\ &= \sum\_{b=1}^d \operatorname{tr}\_1\left( (\rho \otimes \mathbb{I}) \mathbb{E}\_{U\sim \nu} [U^{\otimes 2} |b\rangle\langle b|^{\otimes 2}U^{\dagger\otimes 2}]\right) \end{aligned}$   
> Since $\nu$ is a 2-design, its second moment is the same as the second moment of Haar measure:  
> $\begin{aligned} \mathbb{E}\_{U\sim \nu} [U^{\otimes 2} |b\rangle\langle b|^{\otimes 2}U^{\dagger\otimes 2}] &= \frac{\mathbb{I} \otimes \mathbb{I}+ F}{d(d+1)} \end{aligned}$   
> Therefore  
> $\begin{aligned} \mathcal{M}(\rho)&= \sum\_{b=1}^d \operatorname{tr}\_1\left( (\rho \otimes \mathbb{I}) \frac{\mathbb{I} \otimes\ \mathbb{I}+ F}{d(d+1)}\right) \\\\ &= \frac{d}{d(d+1)}\operatorname{tr}\_1\left( (\rho \otimes \mathbb{I}) + F(\rho \otimes \mathbb{I})\right) \\\\ &= \frac{1}{d+1}(\operatorname{tr}(\rho)\mathbb{I}+ \rho) \end{aligned}$   
> Q.E.D.

### 3.5 Upper Bound on the Variance of the Estimator  

In the previous section, we proved

$\boxed{ \mathcal{M}(\rho)= \frac{\rho + \operatorname{tr}[\rho] \mathbb{I}}{d+1} }$

that is, we proved that

$\boxed{ \begin{aligned} \hat{\rho}&=\mathcal{M}^{-1}(U|b\rangle\langle b| U^\dagger)\\\\ &=(d+1) U|b\rangle\langle b| U^\dagger - \mathbb{I} \end{aligned} }$

is unbiased. In other words, the expectation value of the estimator $\hat{o\_i}:= \operatorname{tr}(O\_i \hat{\rho})$ for an operator equals its true value $\mathbb{E}[\hat{o}\_i] = \operatorname{tr}[\rho O\_i]$.

However, this alone is not enough: we have not given an upper bound on the variance of the estimator, and hence cannot determine the sample complexity.

Next, we prove that the upper bound on the variance of the estimator is $\boxed{\operatorname{Var}(\hat{o}\_i) \le 3 \operatorname{tr}(O\_i^2)}$.

> **Upper bound on the variance of the estimator**  
> The variance of the estimator is:  
> $\operatorname{Var}(\hat{o\_i})=\mathbb{E}[\hat{o}\_i^2]-\mathbb{E}[\hat{o}\_i]^2$   
> where  
> $\mathbb{E}\left(\hat{\sigma}\_i^2\right):=\sum\_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\langle b| U \rho U^{\dagger}|b\rangle \operatorname{tr}\left(O\_i \mathcal{M}^{-1}\left(U^{\dagger}|b\rangle\langle b| U\right)\right)^2\right]$   
> First, note that  
> $\operatorname{tr}(A \mathcal{M}(B))=\sum\_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\langle b| U B U^{\dagger}|b\rangle\langle b| U A U^{\dagger}|b\rangle\right]=\operatorname{tr}(\mathcal{M}(A) B)$   
> so $\operatorname{tr}(A \mathcal{M}^{-1}(B))=\operatorname{tr}(\mathcal{M}^{-1}(A) B)$   
> therefore  
> $\begin{aligned} \mathbb{E}\left(\hat{o}\_i^2\right) & =\sum\_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\langle b| U \rho U^{\dagger}|b\rangle \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right) U^{\dagger}|b\rangle\langle b| U\right)^2\right] \\\\ & =\sum\_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[\operatorname{tr}\left(\rho U^{\dagger}|b\rangle\langle b| U\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right) U^{\dagger}|b\rangle\langle b| U\right)^2\right] \\\\ & =\operatorname{tr}\left(\left(\rho \otimes \mathcal{M}^{-1}\left(O\_i\right) \otimes \mathcal{M}^{-1}\left(O\_i\right)\right)\left(\sum\_{b=1}^d \underset{U \sim \nu}{\mathbb{E}}\left[U^{\dagger \otimes 3}|b\rangle\left\langle b\right|^{\otimes 3} U^{\otimes 3}\right]\right)\right) \end{aligned}$   
> where the final step uses $\operatorname{tr}(A \otimes B) = \operatorname{tr}(A) \operatorname{tr}(B)$.  
> Since $\nu$ is a 3-design,  
> $\begin{aligned} \underset{U \sim \nu}{\mathbb{E}}\left[U^{\dagger \otimes 3}|b\rangle\left\langle b\right|^{\otimes 3} U^{\otimes 3}\right] = \frac{1}{d(d+1)(d+1)}\underset{\pi \in S\_3}{\sum}V\_d(\pi) \end{aligned}$   
> thus  
> $\begin{aligned} &\operatorname{tr}\left(\left(\rho \otimes \mathcal{M}^{-1}\left(O\_i\right) \otimes \mathcal{M}^{-1}\left(O\_i\right)\right)\left(\sum\_{\pi \in S\_3} V\_d(\pi)\right)\right) \\\\ & =\operatorname{tr}(\rho) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right)\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right)\right)+\operatorname{tr}(\rho) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right)^2\right)\\\\ & \quad+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i\right)\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right)\right) +\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i\right)^2\right)\\\\ & \quad+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i\right)^2\right)+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i\right)\right) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i\right)\right)   \end{aligned}$ (\\*）  
> We now use a trick: the variance $\operatorname{Var}\left(\hat{o}\_i\right)=\mathbb{E}\left[\left(\hat{o}\_i-\operatorname{Tr}\left(O\_i \rho\right)\right)^2\right]$ depends only on the traceless part $O\_i^{(0)} := O\_i - \operatorname{tr}(O\_i) \frac{\mathbb{I}}{d}$ of $O\_i$. This is because  
> $\hat{o}\_i-\operatorname{Tr}\left(O\_i \rho\right)=\operatorname{Tr}\left(O\_i \hat{\rho}\right)-\operatorname{Tr}\left(O\_i \rho\right)=\operatorname{Tr}\left(O\_i^{(0)} \hat{\rho}\right)-\operatorname{Tr}\left(O\_i^{(0)} \rho\right)$   
> Note that $\mathcal{M}$ is trace-preserving.  
> Thus, in the expression for the variance, all $O\_i$ can be replaced by $O\_i^{(0)}$:  
> $\begin{aligned} & \operatorname{tr}\left(\left(\rho \otimes \mathcal{M}^{-1}\left(O\_i^{(0)}\right) \otimes \mathcal{M}^{-1}\left(O\_i^{(0)}\right)\right)\left(\sum\_{\pi \in S\_3} V\_d(\pi)\right)\right) \\\\ & =0+\operatorname{tr}(\rho) \operatorname{tr}\left(\mathcal{M}^{-1}\left(O\_i^{(0)}\right)^2\right)+0+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i^{(0)}\right)^2\right)+\operatorname{tr}\left(\rho \mathcal{M}^{-1}\left(O\_i^{(0)}\right)^2\right)+0 \\\\ & =(d+1)^2 \operatorname{tr}\left(O\_i^{(0) 2}\right)+2(d+1)^2 \operatorname{tr}\left(\rho O\_i^{(0) 2}\right) \end{aligned}$   
> Therefore  
> $\begin{aligned} \operatorname{Var}\left(\hat{o}\_i\right) & =\frac{(d+1)^2}{(d+1)(d+2)}\left(\operatorname{tr}\left(O\_i^{(0) 2}\right)+2 \operatorname{tr}\left(\rho O\_i^{(0) 2}\right)\right)-\operatorname{tr}\left(O\_i^{(0)} \rho\right)^2 \\\\ & \leq \operatorname{tr}\left(O\_i^{(0) 2}\right)+2 \operatorname{tr}\left(\rho O\_i^{(0) 2}\right) \\\\ & \leq 3 \operatorname{tr}\left(O\_i^{(0) 2}\right) \\\\ & \leq 3 \operatorname{tr}\left( O\_i^2\right) \end{aligned}$   
> Q.E.D.

### 3.6 Sample Complexity  

In Section II, we used Hoeffding's inequality to give a loose upper bound on sample complexity. Here, we use median-of-means estimation to prove a loose upper bound on sample complexity.

> **Median-of-means estimation**  
> Given $N$ independent identically distributed random variables $X\_i,\ i=1,...,N$ with expectation $\mu$ and variance $\sigma^2$, divide them into $k$ groups, each containing $m=N/k$ random variables. Then the average $\hat{\mu}\_j = \sum\_{i=j}^{j+m-1} X\_i$ of one group has variance $\sigma^2/m$. By **Chebyshev's inequality**, we have:  
> $\begin{aligned} P(|\hat{\mu}\_j - \mu| > \epsilon ) \le \frac{\sigma^2}{m \epsilon^2} \end{aligned}$   
> Set the right-hand side equal to $p$; then $m= \sigma^2/(p\epsilon^2)$.  
> Define the random variable:  
> $Z\_j = \begin{cases} 1,& |\hat{\mu}\_j - \mu| > \epsilon \\\\ 0,& |\hat{\mu}\_j - \mu| \le \epsilon \end{cases}$   
> Since we ultimately take the median of $\hat{\mu}\_1,...,\hat{\mu}\_k$, we want the probability $P\left(\sum\_{j=1}^k Z\_j > \frac{k}{2}\right)$ that more than half of the $\hat{\mu}\_j$ have an error greater than $\epsilon$ to be sufficiently small.  
> Let $S=\sum\_{j=1}^k Z\_j$. By **Hoeffding's inequality**, we have:  
> $P(S-\mathbb{E}(S)>t)\le \exp\left(-\frac{2t^2}{k}\right)$   
> where $\mathbb{E}(S) \le kp$. Set $t = k/2 - kp$, yielding:  
> $P\left(S>\frac{k}{2}\right) \le P(S-\mathbb{E}(S)>t)\le \exp\left(-2k\left(\frac{1}{2}-p\right)^2\right)$   
> Without loss of generality, let $p = 1/4$; then  
> $P\left(\sum\_{j=1}^k Z\_j > \frac{k}{2}\right) \le \exp\left( - \frac{k}{8}\right)$   
> Setting the right-hand side equal to $\delta$ gives $k =8 \log (1/\delta)$.  
> Since $m=\sigma^2/(p\epsilon^2) =4\sigma^2/\epsilon^2$, we have  
> $\boxed{ N = km =32 \sigma^2 \log(1/\delta)/\epsilon^2 }$   
> This is the number of samples required to estimate $\hat{\mu}$ within error $\epsilon$ with a failure rate below $\delta$.

Now apply median-of-means to our problem. The variance $\sigma^2$ of $X\_i:= \hat{o}\_i$ satisfies $\sigma^2 \le 3 \operatorname{tr}(O\_i^2) = 3||O\_i||^2$, and substituting gives

$N  = 96 ||O\_i||^2\log(1/\delta)/\epsilon^2$

Now we need to simultaneously estimate $M$ $\hat{o}\_i$, namely $\hat{o}\_1,...,\hat{o}\_M$.

When applying Hoeffding's inequality:

$P(S-\mathbb{E}(S)>t)\le \exp\left(-\frac{2t^2}{k}\right)$

we can choose $M$ $S\_i$, namely $S\_1, ..., S\_M$, and take the union bound:

$P(S\_i-\mathbb{E}(S\_i)>t,\ \exists S\_i \in\{S\_1,...,S\_M\})\le M\exp\left(-\frac{2t^2}{k}\right)$

This is the key to logarithmic complexity: when taking the union bound, $M$ appears outside the exponent. Therefore, when solving in reverse for $N$, $M$ appears inside the logarithm.

Therefore, we can prove that the sample complexity is:

$\boxed{ N  = O\left( \log(M/\delta)\max\_i||O\_i||^2 /\epsilon^2 \right) }$

### 3.7 Pauli Measurements  

All the derivations introduced above are based on Clifford measurements. However, Clifford measurements are global measurements, requiring entangling gate operations among the qubits, followed by measurement in the computational basis.

In practice, local measurements are more commonly used: single-qubit gates are applied to each qubit separately, followed by measurement in the computational basis. These gates are usually selected from the single-qubit Clifford group, which can implement measurements in the Pauli bases (that is, $X, Y, Z$).

(To be continued)

### 3.8 Derandomization  

Classical shadows differ greatly from traditional FST. In traditional FST, we measure the same number of samples in every measurement basis, which ensures that errors are more uniform to some extent. In classical shadows, because measurement bases are selected randomly, the number of samples under different measurement bases also differs.

This raises the question: compared with randomly selecting bases, is it better to set the number of samples under different measurement bases to be the same? This is the so-called derandomization.

(To be continued)

## References  

1. Cotler, J. & Wilczek, F. Quantum Overlapping Tomography. Phys. Rev. Lett. 124, 100401 (2020).
2. Acharya, Jayadev, et al. "Pauli measurements are not optimal for single-copy tomography." Proceedings of the 57th Annual ACM Symposium on Theory of Computing. 2025.
3. Nayak, A., & Lowe, A. (2025). Lower bounds for learning quantum states with single-copy measurements. ACM Transactions on Computation Theory.
4. O’Donnell, R. & Wright, J. Efficient quantum tomography. in Proceedings of the forty-eighth annual ACM symposium on Theory of Computing 899–912 (ACM, Cambridge MA USA, 2016). doi:10.1145/2897518.2897544.
5. Haah, J., Harrow, A. W., Ji, Z., Wu, X. & Yu, N. Sample-optimal tomography of quantum states. in Proceedings of the forty-eighth annual ACM symposium on Theory of Computing 913–925 (ACM, Cambridge MA USA, 2016). doi:10.1145/2897518.2897585.
6. Huang, H.-Y., Kueng, R. & Preskill, J. Predicting many properties of a quantum system from very few measurements. Nat. Phys. 16, 1050–1057 (2020).
7. Aaronson, Scott. "Shadow tomography of quantum states." Proceedings of the 50th annual ACM SIGACT symposium on theory of computing. 2018.
