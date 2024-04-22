---
title: "Quantum state tomography"
date: 2024-04-22T15:06:14+08:00
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

## Quantum State Tomography

Quantum state tomography is the process of deducing the [quantum state] based on the [results of measurements on a quantum state ensemble]. Its formulation is straightforward, as follows:

Given a series of measurement operators $\{\Pi\_1, \ldots, \Pi\_n\}$ and their corresponding measurement probabilities $p\_k = \operatorname{Tr}[\rho \Pi\_k]$, find the quantum state $\rho$.

In other words, in these $n$ equations $p\_k = \operatorname{Tr}[\rho \Pi\_k]$, given $p\_k$ and $\Pi\_k$, find $\rho$.

> Conversely, if $\rho$ and $p\_k$ are known, and you want to find $\Pi\_k$, that's called Detector tomography. However, that's not the topic of this article.

Why care about state tomography? Because we want to know what the quantum state prepared in the experiment looks like. The method is state tomography.

From the equation $p\_k = \operatorname{Tr}[\rho \Pi\_k]$, you can see that if $\rho$ has $n$ degrees of freedom, we need at least $n$ measurement operators, and they must be "independent of each other." This condition is known as tomographical completeness or informational completeness.

> **Why is it called "Tomography"?**  
> State tomography is called "tomography" because the tomography of continuous-variable photon states is really similar to the CT (Computed Tomography) in hospitals. CT reconstructs a 3D image from projection images from various angles, while the tomography of continuous-variable photon states reconstructs the Wigner function from projection images at various angles. The latter is a kind of "two-dimensional image."  
> It's also understandable with discrete variables because (von Neumann) measurement is essentially projection, and tomography is reconstructing the original quantum state from the measured projections.  
> In short, tomography is named because it is the process of reconstructing the whole from projections.

## State Tomography of a Single Qubit
A qubit's density operator has only three degrees of freedom (Bloch vector), so in theory, only three measurement operators are needed. For example, you can choose $\{(\mathbb{I} + X)/2,\\\\,\\\\, (\mathbb{I} + Y)/2,\\\\,\\\\, (\mathbb{I} + Z)/2 \}$ as the three measurement operators (where $X, Y, Z$ are Pauli matrices). They correspond to the X, Y, Z axes on the Bloch sphere, which are equivalent to measuring the x, y, and z components of the Bloch vector.

However, the issue is that in experiments, we do not directly measure probabilities but rather counts. If we want to know the probability $p\_Z = \operatorname{Tr}[\rho (\mathbb{I} + Z)/2] = \langle0|\rho|0\rangle$, we must use counts $p\_Z = \frac{N\_Z}{N\_Z + N\_{-Z}}$, while measuring $N\_{-Z}$ requires another measurement operator $(\mathbb{I} - Z)/2$.

In general, since we measure counts and require normalization, the actual number of measurement operators required is always one more than the theoretical requirement. And the degrees of freedom for the density operator of $N$ qubits is $4^n - 1$, and adding one precisely equals $4^n$.

For $n = 1$, we need four measurement operators. This was also the method adopted by the earliest article on photon state tomography[[1]](#ref\_1).

Okay, let's dive deeper into the state tomography of a single qubit, which will help us expand to multiple qubits later.

A qubit's density operator is $\rho = \frac{\mathbb{I} + xX + yY + zZ}{2}$. Tomography involves solving for $x, y, z$. As mentioned earlier, we choose four measurement operators: $\{(\mathbb{I} + X)/2,\\\\,\\\\, (\mathbb{I} + Y)/2,\\\\,\\\\, (\mathbb{I} + Z)/2,\\\\,\\\\, (\mathbb{I} - Z)/2 \}$. Thus, the measured counts are:

- $N\_X = N p\_X = N \operatorname{Tr}[\rho \frac{\mathbb{I} + X}{2}] = N \frac{1 + x}{2}$,
- $N\_Y = N p\_Y = N \operatorname{Tr}[\rho \frac{\mathbb{I} + Y}{2}] = N \frac{1 + y}{2}$,
- $N\_Z = N p\_Z = N \operatorname{Tr}[\rho \frac{\mathbb{I} + Z}{2}] = N \frac{1 + z}{2}$,
- $N\_{-Z} = N p\_{-Z} = N \operatorname{Tr}[\rho \frac{\mathbb{I} - Z}{2}] = N \frac{1 - z}{2}$.

By solving these four equations together, we can find the unknowns $x, y, z, N$.

Okay, that's it. It's that simple.

## Maximum Likelihood Estimation  
Wait, is it really that simple? Observant readers might notice that the density operator must be positive definite, but the above solution process doesn't guarantee positive definiteness.

In fact, following the above steps, it is entirely possible to derive non-positive-definite density operators. In other words, the result might be "non-physical."

This is because experimental data is subject to error, which can lead to non-physical results under certain conditions.

Note, this is not due to errors caused by an imperfect experimental system but by quantum statistical errors, or fluctuations. For example, for coherent states, the count distribution is Poissonian, with variance equal to the mean. When time is limited, and not much data can be collected, the relative error $\frac{\Delta N}{N} = \frac{1}{\sqrt{N}}$ might be quite high.

Some might suggest: "What if we add a constraint to ensure positive definiteness?" In this example, as long as we require $|x|, |y|, |z| \leq 1$, positive definiteness can be guaranteed.

But here's the problem: Adding constraints leads to no solution when faced with errors.

Okay, given that no solution is caused by errors, we can resort to a different approach, converting the problem from [solving equations] to [fitting].

What is fitting? We know that two points determine a straight line. However, if the data points themselves have large errors, we might need many points, which almost certainly do not lie on a single straight line. In this case, there's no solution for the straight-line equation.

Even with no solution, we can fit! Using the least-squares method!

So where does the least-squares method come from? The answer is Maximum Likelihood Estimation (MLE).

The basic idea behind MLE is to find a straight line (among many) that is most likely to generate the measured points. The specific implementation involves setting a likelihood function with straight-line parameters as independent variables, where the function value represents the probability of measuring these results with the given straight-line parameters. The whole problem then becomes an optimization problem: Find the maximum value of the likelihood function and its corresponding straight-line parameters.

> In many cases, experimental errors are assumed to follow a normal distribution, so the likelihood function is exponential in the form $L = e^{-\mathcal{L}}$. By taking the logarithm of the likelihood function and inverting it, we get a new likelihood function, $\mathcal{L}$, and the optimization problem becomes finding the minimum value of the new likelihood function.
> This new likelihood function can generally be interpreted as "given this straight line, the total error between the theoretical and actual measurements."

All of these ideas can be directly applied to our state tomography. We can set a likelihood function with the degrees of freedom for the positive-definite matrix $\rho(x,y,z)$, where the function value is the probability of measuring the observed results given quantum state $\rho$.

Let's convert these ideas into an algorithm:

Define a valid density operator $\rho(x,y,z) = \frac{\mathbb{I} + xX + yY + zZ}{2}$, with $|x|, |y|, |z| \leq 1$.

Define the likelihood function as the probability of measuring the observed results, given quantum state $\rho$:

$
\begin{aligned}
\mathcal{L}(x,y,z) &= P(N\_1 = n\_1, N\_2 = n\_2, \ldots) \\\\
&= \prod\_k \exp\left[-\frac{(n\_k - \hat{n}\_k)^2}{2\hat{n}\_k}\right] \\\\
&= \prod\_k \exp\left[-\frac{(n\_k - N \operatorname{Tr}[\rho \Pi\_k])^2}{2N \operatorname{Tr}[\rho \Pi\_k]}\right]
\end{aligned}
$

> In this case, we use the continuous normal distribution instead of the discrete Poisson distribution because when counts are large (typically a few hundred to a few thousand), the normal distribution can closely approximate the Poisson distribution. More importantly, the likelihood function of the normal distribution provides an unbiased estimate, just as effective as the Poisson distribution (see appendix)!  
> 
> Using the Poisson distribution for the likelihood function is also possible, but the result (see appendix) is less intuitive, and it poses a greater computational burden for computers.

For easier calculations, the negative logarithm is taken and unnecessary constants $N$ are removed, resulting in:

$\begin{aligned} \mathcal{L}(x,y,z)=\sum\_k\frac{\left(p\_k-\hat{p}\_k\right)^2}{2\hat{p}\_k}=\sum\_k\frac{\left(p\_k-\operatorname{Tr}[\rho(x,y,z)\Pi\_k]\right)^2}{2\operatorname{Tr}[\rho(x,y,z)\Pi\_k]} \end{aligned}$ 

Thus, we only need to find $(x\_0,y\_0,z\_0) = \underset{|x|,|y|,|z|\le1}{\operatorname{arg\\\\,min}} \mathcal{L}(x,y,z)$ to obtain the optimal solution.


> This is a constrained optimization problem. Can we transform it into an unconstrained optimization problem? See the following.

## State tomography of multiple qubits  
The density matrix of n qubits has $4^n -1$ degrees of freedom. In this case, the corresponding Bloch vector consists of Pauli Correlators:

$\begin{aligned} \rho = \frac{1}{2^n}\sum\_{i\_1,\ldots,i\_n=0}^{3} c\_{i\_1i\_2\ldots i\_n} \sigma\_{i\_1} \otimes \sigma\_{i\_2} \otimes \ldots \sigma\_{i\_n} \end{aligned}$ 

where $\sigma\_i,\\\\,i=0,1,2,3$ represent the identity matrix and the Pauli matrices $\mathbb{I},X,Y,Z$. The coefficients $c\_{i\_1i\_2\ldots i\_n}$ are called correlators.

In this case, we need at least $4^n$ measurement operators to measure and count, and then we can do maximum likelihood estimation.

The state $\rho$ can be set as $\rho(\mathbf{t})=\frac{T^\dag(\mathbf{t})T(\mathbf{t})}{\operatorname{Tr}(T^\dag(\mathbf{t})T(\mathbf{t}))}$, where 

$T(\mathbf{t})=\begin{bmatrix} t\_1 & 0 & 0 & \ldots & 0 \\\\ t\_{2^n+1}+it\_{2^n+2} & t\_2 & 0 & \ldots & 0 \\\\ t\_{2^n+5}+it\_{2^n+6} & t\_{2^n+3}+it\_{2^n+4} & t\_3 & \ldots & 0 \\\\ \ldots & \ldots & \ldots & \ddots & \ldots \\\\ t\_{4^n - 1}+it\_{4^n} & t\_{4^n - 3}+it\_{4^n-2} & t\_{4^n - 5}+it\_{4^n-4} & \ldots & t\_{2^n} \end{bmatrix}$ 

This ensures that $\rho(\mathbf{t})$ is positive definite.

Compared to treating the correlators $c\_{i\_1i\_2\ldots i\_n}$ as parameters and constraining their absolute values to be no greater than one, the advantage of parameterizing with T(t) is that it transforms the upcoming maximum likelihood estimation from a constrained problem into an unconstrained problem (as there are no constraints on t).

The likelihood function in this case is:

$\begin{aligned} \mathcal{L}(\mathbf{t})=\sum\_k\frac{\left(p\_k-\hat{p}\_k\right)^2}{2\hat{p}\_k}=\sum\_k\frac{\left(p\_k-\operatorname{Tr}[\rho(\mathbf{t})\Pi\_k]\right)^2}{2\operatorname{Tr}[\rho(\mathbf{t})\Pi\_k]} \end{aligned}$ 

## Selection of measurement operators  
What types of measurement operators are best to use?

In general, for polarization-encoded photon qubits, we simply use six projection measurements—H, V, D, A, R, L—and their combinations (they are easy to implement, requiring only wave plates). For n qubits, there are $6^n>4^n$ projection operators, which is sufficient.

Since $(|H\rangle\langle H|, |V\rangle\langle V|)$ form a POVM, $(|D\rangle\langle D|, |A\rangle\langle A|)$ form a POVM, and $(|R\rangle\langle R|, |L\rangle\langle L|)$ form a POVM, which means six projection measurements correspond to three POVMs. Thus, we need $3^n$ POVMs, or $3^n$ measurement settings (where "measurement settings" refer to wave plate angles).

However, there is a question: is there a better way to reduce the number of POVMs, thereby reducing the time required for tomography? After all, $6^n>4^n$ is redundant.

From this point, you could say it’s on the academic frontier, where I could promote some of our group's work. More on this later, haha.

## State tomography of continuous-variable photonic states  
Continuous-variable photonic states consider the entire Fock space, rather than just the subspace of zero-photon and single-photon Fock space. The reason we care about continuous variables is that photons are fundamentally harmonic oscillators, not two-level systems. Considering the former is more natural and aligns better with the nature of photons. Indeed, the classical electromagnetic waves in our daily life are a type of continuous-variable photonic state (coherent state).

A single-mode continuous-variable photonic state can be described by quasi-probability distribution functions. There are three such functions: Glauber P-, Husimi Q-, and Wigner functions, referred to as P-, Q-, and W-, respectively. Among them, only the Wigner function's marginal distributions correspond to actual observable probability distributions, which is why we typically consider the Wigner function.


> **What is the Wigner function?**  
>   
> How do we understand the Wigner function? Let's start from classical electromagnetic waves. We know that single-mode (monochromatic) electromagnetic waves can be described by a point on the complex plane (i.e., using a phasor diagram). Superposition of electromagnetic waves directly corresponds to complex number addition (or vector addition).  
> 
> This so-called phasor representation can be immediately extended to quantum mechanics. For a quantized single-mode classical electromagnetic field, its phasor representation is no longer an infinitesimal point but a circle with a certain size. In fact, it is a Gaussian function on the complex plane, with the standard deviation determined by the uncertainty principle. This Gaussian function is the Wigner function of the classical electromagnetic wave, and its marginal distribution corresponds to the probability distribution of the quadrature field strength (the electric field is also an observable and has uncertainty). The quantum state obtained by quantizing a classical electromagnetic wave is called the Coherent state.  
>   
> For a more general quantum optical field, its Wigner function can have strange shapes and can even take on negative values. However, this does not mean we get negative probabilities—after taking the marginal distribution, we always get a non-negative probability. This is because the area occupied by these negative values is small enough to be smaller than the area allowed by the uncertainty principle, meaning the uncertainty principle ensures that we cannot observe negative probability.

{{< figure src="image/wigner.jpg" title="Some interesting Wigner functions for photon states. The left image shows a squeezed state, and the right image shows a Schrödinger cat state." >}}

  
State tomography of continuous-variable photon states is completed by measuring quadrature. In this case, all measurement operators have the following form:

$\begin{aligned} \Pi\_\theta = \frac{ae^{-i\theta}+a^\dag e^{i\theta}}{2} \end{aligned}$ 

This is the so-called "quadrature" (I don't know the Chinese translation). Conceptually, it projects the entire Wigner function onto a straight line, with this line making an angle $\theta$ with the x-axis.

{{< figure src="image/irt.jpg" title="Quantum state tomography of continuous-variable optical states" >}}

  
Quantum information theory tells us that if we want to reconstruct the Wigner function with infinite precision, we need infinitely many values of $\theta$, which means countless measurement operators. Of course, we don't need infinite precision, so we only need to take $\theta$ at some reasonable intervals. For example, taking steps of 0.01 radians from 0 to 2pi.

After obtaining the probability density function of the quadrature, we can use the inverse Radon transform to reconstruct the Wigner function. This is similar to the principle used in hospital CT scans.

As for how to measure quadratures experimentally, it's simple: like in radio technology, mix the signal with a local oscillator. This is called homodyne measurement. Specifically, this involves mixing the signal to be measured with a laser using a beam splitter, then recording the difference in the two output signals. Changing the phase of the laser changes $\theta$.

{{< figure src="image/homodyne.jpg" title="Homodyne Measurement" >}}
  
## Appendix: Maximum Likelihood Estimation for Poisson Distribution  
The likelihood function corresponding to the Poisson distribution is as follows:

$ \begin{aligned} \mathcal{L}(\mathbf{t}) &= P(N\_1=n\_1,N\_2=n\_2,\cdots) \\\\ &= \prod\_k e^{-\lambda\_k} \frac{\lambda\_k^{n\_k}}{n\_k!} \\\\ &\xrightarrow{-\log} \sum\_k (\lambda\_k - n\_k \log \lambda\_k + \cancel{\log n\_k!}) \\\\  &\xrightarrow{\frac{1}{N}} \sum\_k(\hat{p}\_k(\mathbf{t})-p\_k \log \hat{p}\_k(\mathbf{t})) \end{aligned}$ 

where $\lambda\_k = N \operatorname{Tr}[\rho(\mathbf{t}) \Pi\_k] = N \hat{p}\_k(\mathbf{t})$.

By taking the derivative of the likelihood function to find the minimum, we can find that the minimum occurs at $\hat{p}\_k(\mathbf{t}) = p\_k$. This shows that both the Poisson distribution and the normal distribution yield unbiased estimators. However, the Poisson distribution's likelihood function contains logarithms, while the normal distribution's likelihood function contains only polynomials, making the latter more computer-friendly and converging faster. Therefore, we generally use the likelihood function corresponding to the normal distribution.

## References  
1. [^](#ref\_1\_0) James, D. F. V., Kwiat, P. G., Munro, W. J. & White, A. G. Measurement of qubits. Phys. Rev. A 64, 052312 (2001).
