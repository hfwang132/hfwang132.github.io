---
title: "The collapsed state of position measurement"
date: 2024-05-27T17:49:27+08:00
draft: false
tags: ["Quantum Measurement Theory"]
categories: ["Quantum Information"]
---

Common sense tells us that an actual position measurement will not produce a delta function, as the delta function itself is pathological. So what should the collapsed state of an actual position measurement look like?

---

TL;DR:

Let the wave function of the system to be measured be $\varphi(x)$, then the collapsed wave function is:

$\varphi^{(q)}(x) = \mathcal{A}\psi(q-gx) \varphi(x)$ 

where $\psi(x)$ is the initial wave function of the instrument's pointer. $q$ is the reading of the instrument's pointer. $g$ is the coupling strength between the instrument and the system to be measured. $\begin{aligned} \mathcal{A} = \left[\int\_\mathbb{R}\psi(q-gx) \varphi(x)\right]^{-1} \end{aligned}$ is the appropriate normalization constant.

## 1. Prerequisite Knowledge  
### 1.1 Notation Convention  
$L^2(\mathbb{R})$ : Hilbert space of square-integrable functions on $\mathbb{R}$.

$\mathcal{L}(\mathcal{H})$ : (bounded) operators on Hilbert space $\mathcal{H}$.

$\mathbb{I}\_{\mathcal{H}}$ : Identity operator on Hilbert space $\mathcal{H}$.

$\mathcal{E}(\mathcal{H})$ : effect on Hilbert space $\mathcal{H}$. Defined as $\mathcal{E}(\mathcal{H}) := \\\\{ E\in \mathcal{L}(\mathcal{H}) | E =E^\*, 0 \le E\le \mathbb{I}\_{\mathcal{H}}\\\\}$.

$\text{Leb}(\mathbb{R})$ : Lebesgue sigma algebra on $\mathbb{R}$.

### 1.2 Some Basics of Quantum Information  
1) PVM (Projection-Valued Measurement) and POVM

2) Quantum channel and its dual


> I do not intend to introduce them in detail here. Wikipedia or mathematics textbooks already provide comprehensive introductions. Please refer to them yourself. You can also read my [article](../povm)

### 1.3 Measure and Lebesgue Integral  
The spectra of position and momentum operators are continuous. Strictly formulating the continuous spectrum in mathematics requires measure and Lebesgue integral.


> I do not intend to introduce them in detail here. Wikipedia or mathematics textbooks already provide comprehensive introductions. Please refer to them yourself.

Moreover, the letter M in PVM and POVM refers to Measure. Quantum mechanics is built on the foundation of probability theory, and probability theory is built on the foundation of measure theory. So knowledge about measure is necessary.

### 1.4 Spectral Decomposition of Position and Momentum Operators  
The position operator $Q \in \mathcal{L}(L^2(\mathbb{R}))$ on $L^2(\mathbb{R})$ has the spectral decomposition: $Q = \int\_\mathbb{R} x\mathsf{Q}(\mathrm{d}x)$. This is a Lebesgue integral.

Here, $\mathsf{Q}$ is the position projection measurement, i.e., PVM (Projection-Valued Measure, a special case of POVM, Positive Operator-Valued Measure), defined as an operator-valued measure: $\mathsf{Q}: \text{Leb}(\mathbb{R}) \rightarrow \mathcal{E}(L^2(\mathbb{R}))$, $\[\mathsf{Q}(A) \varphi\](x):=\chi\_A(x) \varphi(x)$, where $\chi\_A(x)=\begin{cases} 1, \quad x\in A \\\\ 0, \quad x \notin A \end{cases}$ is the characteristic function of set $A$.


> Selected reading: The momentum PVM can be defined as $\mathsf{P}(A) = F^\* \mathsf{Q}(A) F$, where $F$ is the Fourier-Plancherel operator $\mathcal{F} \in \mathcal{L}(L^2(\mathbb{R}))$, defined as:  
> $(\mathcal{F}\varphi)(p)=\frac{1}{\sqrt{2\pi}}\int\_{\mathbb{R}}\mathrm{e}^{-ipx}\varphi(x)\mathrm{d}x$

## 2. Measurement Model  
The overall idea of this section is as follows:

Consider a system to be measured, with its Hilbert space being $\mathcal{H}$ and state $\rho$. Then we couple the system $\mathcal{H}$ with another system $\mathcal{K}$. You can imagine $\mathcal{K}$ as a pointer on an instrument that can give different readings. Suppose the initial state of system $\mathcal{K}$ is $\sigma$, then the initial state of the composite system is $\rho \otimes \sigma \in \mathcal{H} \otimes \mathcal{K}$.

Next, we let the composite system evolve for a period of time, and the system state becomes $U(\rho\otimes \sigma) U^\dag$.

Finally, we perform a PVM $\mathsf{Z}$ measurement on the auxiliary system $\mathcal{K}$, and according to Born's rule, the probability of getting result $x$ is $\operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z(x)})]$.

In this way, we achieve a POVM $\mathsf{E}$ on $\mathcal{H}$, satisfying $\operatorname{tr}[\rho \mathsf{E(x)}]=\operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z(x)})]$.

Define $\mathcal{I}\_x(\rho) :=\operatorname{tr}\_\mathcal{K}[\rho \mathsf{E(x)}]=\operatorname{tr}\_\mathcal{K}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z(x)})]$, which is the quantum channel induced by the measurement process. If we find the Kraus operators $K\_i$ of the quantum channel, so that $\mathcal{I}\_x(\rho) :=\sum\_i K\_i \rho K\_i^\*$, we can easily obtain the dual channel $\mathcal{I}\_x^\*: \mathcal{I}\_x^\*(\mathcal{M}) =  \sum\_i K\_i^\* \mathcal{M} K\_i$, and the collapsed state after measurement is $\mathcal{I}\_x^\*(\mathbb{I\_\mathcal{H}}) =  \sum\_i K\_i^\* K\_i$.

The above is the overall idea, and below we provide the specific calculation process.

### 2.1 Hamiltonian of the System and the Instrument  
Consider the system $\mathcal{H}$ to be measured and the instrument $\mathcal{K}$, with $\mathcal{H} \cong \mathcal{K} \cong L^2(\mathbb{R})$, i.e., both $\mathcal{H}$ and $\mathcal{K}$ are Hilbert spaces of square-integrable functions on $\mathbb{R}$. You can imagine $\mathcal{K}$ as a pointer on an instrument that can give different readings.

To measure the position of $|\psi\rangle\in \mathcal{H}$, we need to couple the instrument with the system to be measured and let them evolve for a period of time.

The Hamiltonian of this evolution process is $U =e^{-\mathrm{i} g Q\otimes P}$. Here, $Q$ is the position operator on $\mathcal{H}$, $P$ is the momentum operator on $\mathcal{K}$, and $g$ is the coupling strength (the evolution time $t$ is absorbed into it). This Hamiltonian is not difficult to understand because the pointer of the instrument needs to move on the dial to give different readings, and the generator of translation is the momentum operator. Therefore, intuitively, $U$ can be understood as generating a translation on $\mathcal{K}$ according to the position of $|\psi\rangle\in \mathcal{H}$.

### 2.2 Evolution  
According to the spectral decomposition $Q = \int\_{\mathbb{R}} x\mathsf{Q}(\mathrm{d}x)$, we can write $U$ as:

$U = \int\_\mathbb{R} \mathsf{Q}(\mathrm{d}x) \otimes e^{-\mathrm{i}g x P}$ 

Let the initial states of $\mathcal{H}$ and $\mathcal{K}$ be $|\psi\rangle$ and $|\varphi\rangle$ respectively, then the initial state of the composite system $\mathcal{H} \otimes \mathcal{K}$ is:

$|\psi \otimes \varphi\rangle = |\psi\rangle\otimes |\varphi\rangle$.

The state after evolution is:

$U(|\psi\rangle \otimes |\varphi\rangle) = (\int\_\mathbb{R} \mathsf{Q}(\mathrm{d}x) \otimes e^{-\mathrm{i}g x P})(|\psi\rangle \otimes |\varphi\rangle)$

We rewrite the above equation in the integral form:

$U(|\psi\rangle \otimes |\varphi\rangle)=\int\_{\mathbb{R}} \mathsf{Q}(\mathrm{d}x) |\psi\rangle \otimes e^{-\mathrm{i}g x P} |\varphi\rangle = \int\_{\mathbb{R}} \psi(x) |x\rangle \otimes e^{-\mathrm{i}g x P} |\varphi\rangle$

### 2.3 Measurement  
Finally, we measure the position of the pointer of the instrument, i.e., we perform a PVM $\mathsf{Z}$ on $\mathcal{K}$.

The probability of getting the result $q$ is:

$\operatorname{tr}[(\mathbb{I}\_{\mathcal{H}} \otimes \mathsf{Z}(q)) U (|\psi \otimes \varphi\rangle \langle \psi \otimes \varphi|) U^\dag]$

According to Born's rule, this is:

$\|(\mathbb{I}\_{\mathcal{H}} \otimes \mathsf{Z}(q)) U (|\psi \otimes \varphi\rangle)\|^2 = \|\int\_{\mathbb{R}} \psi(x) |x\rangle \otimes \langle q|e^{-\mathrm{i}g x P} |\varphi\rangle\|^2$

According to the definition of the momentum operator, we have:

$\langle q| e^{-\mathrm{i}g x P} |\varphi\rangle = \varphi(q-gx)$

So, the probability of obtaining result $q$ is:

$\|\int\_{\mathbb{R}} \psi(x) |x\rangle \varphi(q-gx)\|^2=\|\psi(x)\varphi(q-gx)\|^2 = |\int\_{\mathbb{R}} \psi(x) \varphi(q-gx)|^2$.

Thus, we have the POVM $\mathsf{E}$ on $\mathcal{H}$:

$\mathsf{E}(q) =|\psi(x)\varphi(q-gx)|^2$

### 2.4 Collapsed State  
At this point, in $\mathcal{I}\_{A}(\rho)$, let $A=\{q\}$, and the quantum state of the system $\mathcal{H}$ to be measured collapses to $\frac{K(q) \rho K(q)^\*}{\text{tr}[K(q) \rho K(q)^\*]}$, where $q$ is the reading of the instrument.

When $\rho = |\varphi\rangle\langle\varphi|$ is a pure state, its collapsed wave function is:

$\varphi^{(q)}(x) = \mathcal{A}\psi(q-gx) \varphi(x)$ 

where $\begin{aligned} \mathcal{A} = \left[\int\_\mathbb{R}\psi(q-gx) \varphi(x)\right]^{-1} \end{aligned}$ is the appropriate normalization constant. Here $q$ is the reading of the probe.

If the probe state is a "widened" Gaussian wave packet: $\psi(x) = \frac{1}{\sqrt{2\pi}\sigma} \exp\left[-\frac{x^2}{2\sigma^2}\right]$, then

$\varphi^{(q)}(x) = \mathcal{A} \exp\left[-\frac{(gx-q)^2}{2\sigma^2}\right] \varphi(x)$ 

This geometric interpretation is already very intuitive.

> In particular, if the probe state itself is a delta function $\psi(x) = \delta(x)$, then the collapsed state after measurement is  
> $\varphi^{(q)}(x) = \delta(x-\frac{q}{g})$  
> Also a delta function.

### 2.5 Measurement Model  
The above analysis process is very useful. We can abstract it into a measurement model: $\mathfrak{M}=(\mathcal{K},\sigma,U,\mathsf{Z})$ .

Here $\mathcal{K}$ is the ancillary system (can be understood as the instrument), $\sigma$ is the initial state of system $\mathcal{K}$, $U$ is the evolution of the composite system $\mathcal{H} \otimes \mathcal{K}$, $\mathsf{Z}$ is the projection measurement (PVM) on the ancillary system. These physical objects implement a POVM measurement on $\mathcal{H}$.

In actual experiments, the ancillary system $\mathcal{K}$ can be regarded as the probe of the instrument, and $\mathsf{Z}$ is the reading of the probe.

## 3. Quantum-Classical Transition  
Finally, you may wonder: what state does the probe collapse to after measurement? This is a very interesting question.

Because we use PVM $\mathsf{Q}$ to measure the position of the instrument probe, it seems that the probe state should collapse to a delta function. In this way, the above analysis seems to simply change one problem into another problem. That is: the problem of how the quantum state of the system to be measured collapses is transformed into the problem of how the probe state collapses.

But in practice, our instrument is a macroscopic classical system, not a quantum system, so the actual situation is more complicated. If you understand some knowledge about POVM and quantum measurement models, you will know: (non-PVM) POVM itself can only provide the probability of measurement results. What the collapsed state is specific to can only be given by a measurement model, and this measurement model will inevitably involve an ancillary system $\mathcal{K}$. If you want to know the quantum state of $\mathcal{K}$, you have to measure the system $\mathcal{K}$ with another system $\mathcal{M}$, and so on. This cyclical process is the process of transition from quantum to classical. The transition from quantum to classical involves the measurement problem, which is an unresolved problem in quantum mechanics, and I don't want to discuss it too much here. Interested readers can search the literature for further study.

In this way, the measurement model seems to be similar to decoherence, both of which seem to solve the measurement problem, but in fact do not. Nevertheless, they still provide us with a lot of insight.

> Of course, the above only talks about the problem of observable quantities with continuous spectra. For observable quantities with discrete spectra, PVM is easily implemented in experiments. PVM can directly give the collapsed state after measurement, and this state has good properties and does not have the pathological properties of delta functions.

## 4. Classical Instrument  
To avoid the problem mentioned above, we can define a course-grained classical instrument that can only distinguish whether particles are in a certain interval:

$\mathsf{Z}: \\{0,1\\} \rightarrow \mathcal{E}(L^2(\mathbb{R}))$ 

$\mathsf{Z}(1) = \int\_a^b \mathsf{Q}(\mathrm{d}x)$ 

$\mathsf{Z}(0) = \mathbb{I}\_{L^2(\mathbb{R})} - \int\_a^b \mathsf{Q}(\mathrm{d}x)$ 

Or distinguish particle positions with a certain precision $g$:

$\mathsf{Z}: \mathbb{Z} \rightarrow \mathcal{E}(L^2(\mathbb{R}))$ 

$\mathsf{Z}(n) =\int\_{gn}^{g(n+1)} \mathsf{Q}(\mathrm{d}x)$ 

Note that they are both PVMs, so the collapsed state can also be determined.

The calculation of these two cases is left to the reader as an exercise.

