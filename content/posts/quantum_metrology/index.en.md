---
title: "A beginner's guide to quantum metrology"
date: 2024-04-23T19:05:46+08:00
draft: false
tags: ["Quantum Metrology"]
categories: ["Quantum Information"]
---

## I. Introduction to Quantum Metrology  
Quantum metrology is the science of using the quantum properties of quantum states for precise measurements.

The reason for studying quantum metrology is that the precision of any physical measurement is limited by the Heisenberg Uncertainty Principle in quantum mechanics, known as the Heisenberg Limit. The goal of quantum metrology is to approach and surpass this limit.

Of course, most measurements in daily life do not need to reach the Heisenberg Limit (e.g., weighing oneself). However, in high-precision imaging and various high-precision scientific experiments, people have indeed approached the Heisenberg Limit.

> **Gravitational Waves**: **LIGO** (Light Interferometer Gravitational-wave Observatory) is an optical interferometer used to detect gravitational waves. It can detect changes in the length of the interference arms down to $10^{-19}$ m, which is one ten-thousandth the size of a proton and one billionth the wavelength of light. At this insane level of precision, LIGO uses the **squeezed state** of the light field to reduce quantum noise.

Of course, quantum noise does not only appear in extreme cases like LIGO. Below are two examples related to imaging.

> **Shot Noise**: You have certainly used a CMOS camera. Have you noticed that when the environment is dark, the photos you take have a lot of noise? This is caused by **shot noise**.
>
> What is shot noise? The electrons excited by photons come one by one, and their generation follows a Poisson distribution (completely random generation time), with the relative variance inversely proportional to the average number of electrons. This variance is the shot noise.
>
> Therefore, when the number of electrons is small, their relative variance is large, resulting in a low signal-to-noise ratio (SNR) and causing noise to appear.
>
> Shot noise is given by the particle-number-phase uncertainty principle. However, due to historical reasons, it is not called the Heisenberg Limit but the shot noise limit or the standard quantum limit, distinguishing it from the Heisenberg Limit.

> **Diffraction Limit**: Imaging precision is measured not only in time (i.e., signal-to-noise ratio) but also in space (i.e., the number of pixels). If we infinitely increase the number of pixels, can we achieve infinite precision?
>
> If you have studied optics, you know this is impossible due to the **diffraction limit**.
>
> In fact, the diffraction limit is a type of Heisenberg Limit because it corresponds to a momentum-position uncertainty. If we need more accurate positioning, the diffraction limit tells us that without changing the wavelength, we need to increase the aperture size. From the perspective of the Heisenberg principle, this is because photons entering the aperture at different angles have different momenta, and this momentum information is lost at the moment of imaging. The more momentum information lost, the more accurate the photon's position measurement. Conversely, to reduce the wavelength without changing the aperture size, we need to decrease the wavelength, as smaller wavelengths correspond to larger momenta, and a larger momentum range received by the same aperture.

These examples are quite interesting. I hope you enjoy them. Of course, even more interesting is to come: what mathematical tools do people use to characterize quantum noise? How do people design quantum states to achieve the Heisenberg Limit? After reading this article, you will have a deeper understanding of these issues and complete your introduction to quantum metrology.

## II. Maximum Likelihood Estimation  
What is measurement? First, we need to define measurement. Note that measuring the same physical quantity always gives a series of different results with certain probabilities (whether in classical or quantum physics). We usually take the average of these results as the final result.

Thus, the measurement process actually gives a series of **random variables** (i.e., individual measurement results), and we construct **statistics** (i.e., functions of random variables) like the average to estimate the physical quantity itself. We call this statistic an estimator.

This estimator is also a random variable with its own mean and variance. We refer to the estimator's value as the measurement result, and its variance as the measurement error. The relative error is the error divided by the mean; the measurement precision is the reciprocal of the relative error.

At this point, we have defined the measurement process, which is essentially a **parameter estimation** problem:

> **Parameter Estimation**: Given a probability density function $p(\mathbf{x};\theta)$, where $\mathbf{x}$ is the measurement result and $\theta$ is the physical quantity to be measured (a parameter of the probability density function rather than its variable), construct an estimator $\hat{\theta} = \hat{\theta}(\mathbf{x})$ such that its mean is equal to or close to the parameter (unbiasedness) and its variance is as small as possible (efficiency). Additionally, there is an implicit condition: we require that as the sample size increases, the estimator approaches the true parameter value (consistency).

> **Unbiasedness**: Unbiasedness means that $\mathbb{E}(\hat{\theta}(X)) = \theta$, i.e., the mean of the estimator equals the true value of the parameter.

> **Efficiency**: How do we measure efficiency? We will introduce it later, but the variance of the estimator has a CR lower bound: $(\Delta \hat{\theta})^2 \ge \frac{1}{F(\theta)}$, where $F(\theta)$ is called Fisher information. Efficiency can be measured by $F(\theta)/(\Delta \hat{\theta})^2 \le 1$. When $F(\theta)/(\Delta \hat{\theta})^2 = 1$, meaning the lower bound is reached, we call the statistic efficient.

> **Consistency**: Consistency requires $\lim_{n\rightarrow \infty} P(|\hat{\theta} - \theta|>\epsilon) = 0$ for any positive number $\epsilon > 0$. Here, $n$ is the number of samples. This is also called convergence in probability: $\operatorname{plim}_{n\rightarrow \infty} \hat{\theta} = \theta$.

The most commonly used method in statistics for dealing with parameter estimation problems is Maximum Likelihood Estimation (MLE). The idea is simple: find a parameter such that, under this parameter, the probability of obtaining the observed results is the highest.

The specific steps are also simple:

> **Maximum Likelihood Estimation**: Let the likelihood function $f(\theta; \mathbf{x}) = p(\mathbf{x}; \theta)$, and find its maximum point $\hat{\theta}(\mathbf{x}) = \operatorname{arg\,max} f(\theta; \mathbf{x})$.
>
> $\hat{\theta}(\mathbf{X})$ is the estimator given by maximum likelihood estimation.
>
> In practice, people often take the logarithm of the likelihood function to simplify calculations, i.e., $\log f(\theta; \mathbf{x})$, called the log-likelihood function.

In fact, maximum likelihood estimation usually does not satisfy unbiasedness, but people still favor it. This is because maximum likelihood estimation is always asymptotically efficient (variance reaches the CR lower bound as the sample size tends to infinity) and asymptotically unbiased (the mean of the estimator tends to the true parameter value as the sample size increases).

In quantum measurements, maximum likelihood estimation is also used in most cases. Therefore, this article will focus on maximum likelihood estimation.

> Other parameter estimation methods include Bayesian estimation and method of moments. These, along with maximum likelihood estimation, form the three most important parameter estimation methods.

## III. Fisher Information and CR Lower Bound

The likelihood function is the core of maximum likelihood estimation. Let's see what quantities can be derived from the likelihood function.

First, we get a quantity called the Score Function, which is the derivative of the log-likelihood function with respect to the true parameter value:

> **Score Function**: The Score Function $s(\theta; \mathbf{x})$ is defined as:
>
> $s(\theta; \mathbf{x}) = \frac{\partial}{\partial \theta} \log f(\theta; \mathbf{x})$,
>
> where $f(\theta; \mathbf{x})$ is the likelihood function.

Its meaning is also clear: it indicates the impact of changes in the parameter value on the likelihood function. If the derivative is positive, the parameter value needs to increase because increasing the parameter value increases the likelihood function (i.e., the probability is higher). Conversely, if the derivative is negative, the parameter value needs to decrease. When is the parameter value ideal? Of course, it is when the derivative is zero. This is easy to understand: the derivative of the likelihood function at its maximum point is zero.

Of course, the derivative being zero is only a necessary condition, not a sufficient condition. To ensure that the zero point of the likelihood function's derivative corresponds to a maximum, the second derivative needs to be negative. Hence, we define Fisher Information:

> **Fisher Information**: Fisher Information is the expectation (with respect to the random variable $X$) of the negative second derivative of the log-likelihood function (with respect to the parameter $\theta$):
>
> $F(\theta) = \mathbb{E}\left(-\frac{\partial^2}{\partial \theta^2} f(\theta, X)\right)$
>
> It can actually be proven that Fisher Information is always non-negative. Therefore, setting the derivative of the likelihood function to zero always yields a maximum value. In fact, Fisher Information can also be expressed using the square of the first derivative, so it is certainly non-negative:
>
> $F(\theta) = \mathbb{E}\left[\left(\frac{\partial}{\partial \theta} f(\theta, X)\right)^2\right]$ (proof omitted).

> **Significance of Fisher Information**: The significance of Fisher Information is the sensitivity of the likelihood function to the parameter near its maximum.
>
> Intuitively, the more sensitive the likelihood function is, the more efficient our estimate is. Because when the likelihood function is sensitive to the parameter, a small change in the parameter causes a sharp decrease in the likelihood function, allowing us to determine the parameter with high confidence. Conversely, if the likelihood function is not sensitive to the parameter, we cannot narrow down the parameter to a small range because the parameter can vary over a wide range without significantly decreasing the likelihood function.

Understanding the significance of Fisher Information, we can quickly understand the Cramér-Rao Bound:

> **Cramér-Rao Bound**: The variance of an unbiased estimator has the following lower bound:
>
> $(\Delta \theta)^2 \ge \frac{1}{F(\theta)}$
>
> where $F(\theta)$ is Fisher Information. This is called the Cramér-Rao Bound.

This essentially quantifies the significance of Fisher Information into an inequality. The larger the Fisher Information, the more sensitive the likelihood function is to the parameter, and the smaller the variance of the parameter estimator can be. Conversely, the smaller the Fisher Information, the less sensitive the likelihood function is to the parameter, and the larger the variance of the parameter estimator will be.

So far, the maximum likelihood estimation, Fisher Information, and CR lower bound we have introduced have nothing to do with quantum mechanics, but they are necessary foundations. In the next section, we will introduce quantum Fisher Information and quantum CR lower bound, and apply them to quantum measurements.

## IV. Quantum Fisher Information and Quantum CR Bound  

In this section, we will apply all the statistical concepts mentioned in the previous section to quantum mechanics. This is possible because quantum measurements can also be described using probability theory.

First, we need a probability density function. In quantum mechanics, given a state and a POVM, we can obtain a probability density function:

> **Probability Density Function**: $p_{\rho}^{E}(x)=\operatorname{tr}[\rho E(x)]$, where $\rho$ is the quantum state being measured, $E(x)$ is the POVM, satisfying $\sum_{x\in X} E(x) = \mathbb{I}$, where $X$ is the set of all possible measurement results, and $\mathbb{I}$ is the identity operator.

In quantum mechanics, the physical quantity we want to measure is encoded in the quantum state, i.e., $\rho(\theta)$, so the likelihood function is:

> **Likelihood Function**: $f^{E}(\theta; x) = p_{\rho(\theta)}^{E}(x) = \operatorname{tr}[\rho(\theta) E(x)]$

Note that this likelihood function depends on the POVM $E$. For each POVM, we have a likelihood function.

Taking the negative second derivative of the likelihood function and taking the expectation value, we get the Fisher information as follows:

> **Fisher Information**: $F^{E}(\theta) = \mathbb{E}\left[(\frac{\partial}{\partial \theta} f^{E}(\theta; X))^2\right]$

Note that **Fisher Information** depends not only on the parameter $\theta$ but also on the selected POVM, i.e., the chosen measurement method.

Now we can define quantum Fisher information, which is the largest among the Fisher information corresponding to different POVMs.

> **Quantum Fisher Information**: $F(\theta) = \sup_{E\in \mathsf{E}} F^{E}(\theta)$, where $\mathsf{E}$ is the set of all POVMs. In other words, quantum Fisher information is the supremum of classical Fisher information.

So far, we have only given a series of definitions and have not obtained any new results. Next, we will further restrict the problem to hope to get some useful results.

We restrict the form of $\rho(\theta)$. The parameter $\theta$ is usually encoded in a unitary process: $U = e^{-iH\theta}$. Applying this unitary process to a state $\rho_0$, we get $\rho(\theta) = e^{-iH\theta}\rho_0 e^{iH\theta}$. Here $\rho_0$ can also be called a probe state.

> **Why Unitary Encoding** Here we give an example. If we want to know the phase difference introduced by a birefringent crystal between H and V polarized light, we need to consider the transformation $e^{i\frac{Z}{2}\theta} = \begin{bmatrix} e^{i\theta/2} & 0 \\\\ 0 & e^{-i\theta/2} \end{bmatrix}$, where $Z$ is the Pauli Z matrix.
> 
> If the Hilbert space is not just a two-level system (a qubit) but can be larger (qudit or multiple qubits), the unitary transformation acting on the state vector is a larger unitary transformation that can always be diagonalized as $\sum_{k} e^{i\theta_k} |k\rangle\langle k|$.
> 
> In other words, its eigenvalues are always complex numbers with a modulus of one. Therefore, the important information is the phase of these complex numbers. How to design measurement circuits to detect these phases is the problem of Quantum Phase Estimation. Quantum Phase Estimation is a fundamental and important algorithm primitive in quantum computing.

Next, let's look at the derivative of $\rho(\theta)$. Those familiar with quantum mechanics should be familiar with it, and the result will have a commutator:

> $\frac{\partial}{\partial \theta} \rho(\theta) = i[\rho, H]$

But there is actually another derivative representation called the Symmetric Logarithmic Derivative (SLD):

> **Symmetric Logarithmic Derivative (SLD)**: $\frac{\partial}{\partial \theta} \rho(\theta) = \frac{1}{2}\\{\rho, L_{\rho}(H)\\} = \frac{1}{2}[\rho L_{\rho}(H) + L_{\rho}(H) \rho]$

where $L_{\rho}(H)$ is defined as the operator satisfying $\frac{1}{2}\\{\rho, L_{\rho}(H)\\} = i[\rho, H]$. Its explicit form is

> **Explicit Form of SLD**: $L_{\rho}(H) = 2i\sum_{k,l} \frac{\lambda_k - \lambda_l}{\lambda_k + \lambda_l} \langle k | H | l \rangle | k \rangle\langle l |$, where $\lambda_k$ and $|k\rangle$ are the eigenvalues and eigenvectors of $\rho$, respectively. The reader can verify this easily using the definition.

Why define SLD? Because SLD is very useful in calculating quantum Fisher information. Next, let's derive the quantum Fisher information and quantum CR bound.

Earlier, we mentioned that for a POVM $E$, Fisher information is: $F^{E}(\theta) = \mathbb{E}\left[(\frac{\partial}{\partial \theta} f^{E}(\theta; X))^2\right]$. Now we substitute all the formulas:

> $\begin{aligned}
> F^{E}(\theta) &= \mathbb{E}\left[\left(\frac{\partial}{\partial \theta} f^{E}(\theta; X)\right)^2\right] \\\\
> &= \mathbb{E}\left[\frac{1}{p^{E}(X; \theta)^2}\left(\frac{\partial}{\partial \theta} p^{E}(X; \theta)\right)^2\right] \\\\
> &= \sum_{x\in X}\frac{p^{E}(x; \theta)}{p^{E}(x; \theta)^2}\left(\frac{\partial}{\partial \theta} p^{E}(x; \theta)\right)^2 \\\\
> &= \sum_{x\in X}\frac{1}{\operatorname{tr}[\rho E(x)]}\left(\frac{\partial}{\partial \theta} \operatorname{tr}[\rho E(x)] \right)^2 \\\\
> &= \sum_{x\in X}\frac{1}{\operatorname{tr}[\rho E(x)]}\left( \operatorname{tr}\left[\frac{\partial \rho}{\partial \theta} E(x)\right] \right)^2 \\\\
> &= \sum_{x\in X}\frac{1}{\operatorname{tr}[\rho E(x)]}\left( \operatorname{tr}\left[\frac{L \rho + \rho L}{2} E(x)\right] \right)^2 \\\\
> &= \sum_{x\in X}\frac{1}{\operatorname{tr}[\rho E(x)]}\left( \operatorname{tr}\frac{ L \rho E(x) + E(x) \rho L}{2} \right)^2 \\\\
> &= \sum_{x\in X}\frac{1}{\operatorname{tr}[\rho E(x)]}\left[ \operatorname{Re}\left(\operatorname{tr}[L \rho E(x)] \right)\right]^2 \\\\
> &\le \sum_{x\in X}\frac{1}{\operatorname{tr}[\rho E(x)]}\left| \operatorname{tr}[L \rho E(x)] \right|^2 \\\\
> &= \sum_{x\in X}\frac{1}{\operatorname{tr}[\rho E(x)]}\left| \operatorname{tr}[L \rho^{\frac{1}{2}}\rho^{\frac{1}{2}} E(x)^{\frac{1}{2}} E(x)^{\frac{1}{2}}] \right|^2 \\\\
> &\le \sum_{x\in X}\frac{1}{\operatorname{tr}[\rho E(x)]} \operatorname{tr}[\rho E(x) L^2] \operatorname{tr}[\rho E(x)] \\\\
> &=  \operatorname{tr}\left[\rho \left(\sum_{x\in X}E(x) \right) L^2\right] \\\\
> &= \operatorname{tr}[\rho L^2]
> \end{aligned}$

It can be seen that the Fisher information has an upper bound $F^{E}(\theta) \le \operatorname{tr}[\rho L^2]$. Now the question is whether this upper bound can be achieved? The answer is yes; each inequality sign above can reach equality.

> The condition for the first inequality to hold as equality is that $L$ is a Hermitian operator, in which case $L \rho E(x) = E(x) \rho L = (L \rho E(x))^\dag$. This is always satisfied because SLD has a property: if $H$ is Hermitian, then $L_\rho(H)$ is also Hermitian.
> 
> The condition for the second inequality to hold as equality is the Cauchy-Schwarz inequality condition: $\rho^{\frac{1}{2}}E(x)^{\frac{1}{2}}$ and $\rho^{\frac{1}{2}}E(x)^{\frac{1}{2}}L$ are linearly dependent, i.e., $\exists k\in \mathbb{C}, \\, \rho^{\frac{1}{2}}E(x)^{\frac{1}{2}} = k\rho^{\frac{1}{2}}E(x)^{\frac{1}{2}}L$. This can be done. We let $E(x)$ be the projection operator (which is the most commonly used POVM, also called von Neumann measurement), then $E(x)^{\frac{1}{2}} = E(x) = E(x)^2$, and $\forall \sigma, \\,\sigma E(x) = k E(x)$. At this point, as long as $L = \sum_x c_x E(x)$, i.e., the projection operators in the POVM are eigenvectors of $L$, the inequality can hold as equality.

Since the upper bound can be reached, we have derived the supremum of the Fisher information, which is the quantum Fisher information:

> **Quantum Fisher Information**: $F(\theta) = \operatorname{tr}[\rho L^2]$, where $\rho = \rho(\theta) = e^{-iH\theta} \rho_0 e^{iH\theta}$, $L=L_{\rho}(H)$.
> 
> The sufficient condition for achieving quantum Fisher information is: use projection measurement, and the projection basis vectors are the eigenvectors of SLD.

Since we have quantum Fisher information, there is also a quantum CR bound:

> **Quantum Cramér-Rao Bound**: $(\Delta \theta)^2 \ge \frac{1}{F(\theta)} = \frac{1}{\operatorname{tr}[\rho L^2]}$

The $\rho$ considered above are all general mixed states. If we consider a pure state $\rho = |\psi\rangle\langle \psi|$, then the quantum Fisher information has a simpler expression:

> **Quantum Fisher Information for Pure State**:
> 
> $\begin{aligned}
> F(\theta) &= 4 (\Delta H)^2 \\\\
> &= 4 \left(\langle \psi | H^2 | \psi \rangle - \langle \psi | H | \psi \rangle^2\right) \\\\
> &= 4 \left(\langle \psi_0 | H^2 | \psi_0 \rangle - \langle \psi_0 | H | \psi_0 \rangle^2\right)
> \end{aligned}$
> 
> Proving this formula is an interesting but not difficult exercise, which we leave to the reader.

The quantum CR bound for pure states is almost the Heisenberg Uncertainty Principle: $\Delta \theta \Delta H \ge \frac{1}{2}$. However, there are still some differences: the Heisenberg Uncertainty Principle refers to the product of the variances of two operators, while the quantum CR bound for pure states is the product of the variance of an operator and a parameter. Also, for mixed states, we do not have such a direct expression.

Now that we have such powerful tools, let's apply these tools to some practical problems.

## V. Quantum Phase Estimation

Previously, we mentioned quantum phase estimation, which is:

> **Quantum Phase Estimation**: Given a unitary transformation, find the phase of its eigenvalues.
>
> If the considered Hilbert space is n-dimensional, then there are (n-1) phases to be estimated (global phase can be ignored).

We have not yet touched upon quantum estimation with multiple parameters (we will discuss this in the appendix). Now, we consider the case of only one parameter. There are two scenarios: two-level systems and harmonic oscillator systems.

### 5.1 Two-Level Systems

Let's consider a two-level system with Hamiltonian $H = \frac{\hat{Z}}{2}$, and the initial state of the system is a pure state, i.e., $|\psi(\theta)\rangle = e^{-i \frac{\hat{Z}}{2} \theta} |\psi_0\rangle $.

In this case, the quantum Fisher information is:

$ \begin{aligned}
F(\theta) &= 4 \left(\Delta \frac{\hat{Z}}{2}\right)^2 = (\Delta \hat{Z})^2 \\\\
&= \left\langle \psi_0 \left| \hat{Z}^2 \right| \psi_0 \right\rangle - \left\langle \psi_0 \left| Z \right| \psi_0 \right\rangle^2 \\\\
&= 1 - \left\langle \psi_0 \left| \hat{Z} \right| \psi_0 \right\rangle^2 
\end{aligned}$

To maximize the quantum Fisher information, we require $\left\langle \psi_0 \left| \hat{Z} \right| \psi_0 \right\rangle = 0$, in other words, $|\psi_0\rangle$ should lie on the equator of the Bloch sphere. This also aligns with our intuition: the closer the initial state is to the equator, the more evident the rotation of the Bloch sphere will be on the initial state. If the initial state is at the north or south pole, then the Fisher information will be zero, meaning the initial state cannot sense any rotation.

Choosing the observable $X$ or $Y$ both can achieve the CR lower bound. Let's directly choose the observable as $X + i Y$ (although this is not an observable, we can separately observe $X$ and $Y$, and then combine the results into a complex number), with an expected value of $e^{i\theta}$ and a variance of 1. Then we have $1 =|\Delta e^{i\theta}| = |ie^{i\theta}\Delta\theta| = \Delta \theta$. In other words, $\Delta \theta = \frac{1}{F(\theta)}$, achieving the CR lower bound.

### 5.2 Harmonic Oscillator Systems

Now let's consider a harmonic oscillator system with Hamiltonian $H = \hat{N} = \hat{a}^\dag \hat{a}$ corresponding to the unitary transformation $e^{i\hat{N}\theta} = \sum_{k=0}^{\infty} e^{i N \theta} |N\rangle\langle N|$.

In this case, the quantum Fisher information is:

$ \begin{aligned}
F(\theta) &= 4 \left(\Delta \hat{N}\right)^2 \\\\
&= 4 [\langle \psi | \hat{N}^2 | \psi \rangle - \langle \psi | \hat{N} | \psi \rangle^2]
\end{aligned}$

Next, we classify and discuss different initial states (probe states).

### 5.2.1 Number State

$| \psi_0 \rangle = | N \rangle$

In this case, the quantum Fisher information is:

$F(\theta) = 0$.

This is easy to understand because the phase of the number state is completely random (according to the particle number-phase uncertainty principle). It can be seen that number states cannot be used to detect phase.

### 5.2.2 Coherent State

$|\psi_0 \rangle = | \alpha \rangle$

In this case, the quantum Fisher information is:

$F(\theta) = 4 |\alpha|^2 = 4 \bar{n}$.

It gives the CR lower bound of measurement error: $\Delta \theta \ge \frac{1}{2 \sqrt{\bar{n}}}$. This is the limit allowed by shot noise. It is given by the particle number-phase uncertainty relation. However, we generally do not call this the Heisenberg limit; instead, we call it the shot noise limit or the standard quantum limit. In the literature, this limit is often distinguished from the Heisenberg limit. This is because we can further increase $\Delta N$ to reduce $\Delta \theta$. When $\Delta$ is proportional to $\bar{n}$, i.e., $\Delta \theta \sim \frac{1}{\bar{n}}$, we call this the Heisenberg limit.

[...]

## VI. Quantum Imaging and Quantum Illumination
## VII. Other Quantum Parameter Estimation Problems
### 7.1 Gain Sensing
### 7.2 Noise Sensing
