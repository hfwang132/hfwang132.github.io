---
title: "Why Does the Intensity of a Thermal Light Field Follow an Exponential Distribution?"
date: 2024-06-21T00:36:00+08:00
originalURL: "https://zhuanlan.zhihu.com/p/704163123"
aliases:
  - "/en/thermal_exponential_dist/"
  - "/en/Post_20240727_为什么热光场的光强服从指数分布/"
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

## 1. An Elegant Argument  
Nobel laureate Ketterle used a very elegant argument when discussing the $g^{(2)}$ of a classical thermal light field in the [8.422 open course](https://av.tib.eu/media/42704):

According to the central limit theorem, the electric field $E$ follows a Gaussian distribution, and therefore the light intensity $I$ follows an exponential distribution.


> The probability density function (pdf) of the exponential distribution is: $f(x) = \gamma e^{-\gamma x}$ .

The moments of the exponential distribution have the following property:

$\langle I^n \rangle = n! \langle I\rangle^n$ 

Thus, the classical second-order correlation function $g^{(2)}(0)$ of a thermal light field is

$g^{(2)} := \langle I^2\rangle/\langle I\rangle^2 = 2$ 

This argument is remarkably elegant because it fully exploits the “chaotic” nature of thermal light: according to the central limit theorem, regardless of the probability distributions of the electric fields in the individual frequency modes, their superposition must follow a Gaussian distribution. Consequently, the square of the electric field follows an exponential distribution.



---

## 2. A Review of Probability and Statistics  
Wait, is it really that simple? Let us use the probability and statistics knowledge we learned as undergraduates to analyze this: if a random variable follows a Gaussian distribution, does its square really follow an exponential distribution?


> Let us write down the cdf (cumulative distribution function) of the Gaussian distribution:  
> $p(E<x) = \Phi(x) = \int\_{-\infty}^{x} \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{t^2}{2\sigma^2}} \mathrm{d}t$   
> Then the cdf of the light intensity is  
> $p(I<y) = p(E^2 < y) = p(-\sqrt{y}<E<\sqrt{y}) = \Phi(\sqrt{y}) - \Phi(-\sqrt{y}) = 2\Phi(\sqrt{y}) - 1$   
> Therefore, the pdf of the light intensity should be  
> $f(y) = p^\prime(I < y) = 2 \Phi^\prime(\sqrt{y}) = \frac{1}{\sigma\sqrt{2\pi y}} e^{-\frac{y}{2\sigma^2}}$

This is not an exponential distribution! Compared with a true exponential distribution, it has an additional $y^{-1/2}$ factor.

Where does the problem lie?

We can take a different approach and ask the reverse question: if a random variable follows an exponential distribution, what distribution does its square root follow?


> The cdf of the exponential distribution is:  
> $p(I<y) = 1 - e^{-\gamma y}$   
> Then the cdf of the electric field is:  
> $p(E < x) = \frac{1 + p(-x<E<x)}{2} = \frac{1 + p(I<x^2)}{2}  = \frac{2 - e^{-\gamma x^2}}{2}$   
> Therefore, the pdf of the electric field should be:  
> $f(x) = p^\prime(E<x) = \gamma x e^{-\gamma x^2}$

This distribution is called the Rayleigh distribution; compared with a Gaussian distribution, it has an additional $x$ factor.

Students with sharp intuition may realize that the Rayleigh distribution actually corresponds to the magnitude of a two-dimensional random vector that follows a Gaussian distribution:

$f(r) = \int\_{0}^{2\pi} \frac{1}{2\pi} e^{-\frac{r^2}{2\sigma^2}} r\mathrm{d}\theta$ 

Wait, the electric field is actually a two-dimensional random variable? That is right! In addition to its amplitude, an electric field also has a phase—it is actually a complex number! If a complex random variable follows a Gaussian distribution, then its modulus squared does indeed follow an exponential distribution.

At this point, the problem is perfectly resolved.

## 3. From Classical to Quantum  
However, everything above can only show that the classical $g^{(2)}$ is 2; it cannot show that the quantum $g^{(2)}$ is also 2.

The only difference between quantum $g^{(2)}$ and classical $g^{(2)}$ is that the former takes into account the particle nature of light. If you detect one photon, the light field has one fewer photon. Therefore, quantum $g^{(2)}$ is not $\langle n ^2\rangle/\langle n\rangle^2$, but rather $\langle n (n-1)\rangle/\langle n\rangle^2$.

Could it be that quantum $g^{(2)}$ is not actually equal to 2, but instead 1.9999? Fortunately, although quantum $g^{(2)}$ and classical $g^{(2)}$ differ in form, quantum $g^{(2)}$ is still equal to 2. Let us derive this below.

According to Boltzmann law, at thermal equilibrium:

$p\_n = p\_0 e^{-n\omega/T} = (1-e^{-\omega/T}) e^{n\omega/T}$ 

where $p\_n$ is the probability that the photon number in a given mode is n.

This is a geometric distribution. The geometric distribution is the discrete version of the exponential distribution, while the exponential distribution is the continuous version of the geometric distribution.

Thus, quantum $g^{(2)}$ is

$$ \begin{align} g^{(2)} := \frac{\langle n(n-1) \rangle}{\langle n\rangle^2} = \frac{\sum n(n-1) p\_n }{(\sum n p\_n)^2} = 2 \end{align} $$


> The calculation is left to the reader as an interesting exercise. The key is to calculate the moments of the geometric distribution, which are much more complicated than those of the exponential distribution.

As we can see, although the form of quantum $g^{(2)}$ has changed, the corresponding probability distribution has also changed from the exponential distribution followed by the light intensity to the geometric distribution followed by the particle number (that is, the discrete version of the exponential distribution). These two effects cancel perfectly, leaving quantum $g^{(2)}$ still equal to 2.

## 4. Quantumness  
How is quantum $g^{(2)}$ special compared with classical $g^{(2)}$? The special point is that quantum $g^{(2)}$ can be less than 1, whereas classical $g^{(2)}$ cannot be less than 1.

For classical $g^{(2)}$, $g^{(2)} = \langle I^2 \rangle / \langle I\rangle^2 \ge [\cancel{\text{Var}(I)} + \langle I\rangle^2] / \langle I\rangle^2 = 1$; that is, its minimum value is attained if and only if the light intensity is constant, namely, when the electric field is a sinusoidal wave with constant amplitude.

Quantum $g^{(2)}$ is different. Detecting one photon means that the light field has one fewer photon, and a single-photon state has only one photon: once it is detected, it is gone. Thus, for a single-photon state, quantum $g^{(2)}$ is 0.


> More generally, light fields with quantum $g^{(2)}$ less than 1 are called sub-Poissonian light fields; those with quantum $g^{(2)}$ greater than 1 are called super-Poissonian light fields.  
>   
> When the light field is a coherent state (with either definite or indefinite phase), quantum $g^{(2)}$ equals 1, and the photon number then follows a Poisson distribution. Its classical counterpart is a sinusoidal wave with either definite or indefinite phase (but definite amplitude).

Quantum $g^{(2)}$ has another special feature: for a thermal light field, even if there is only one frequency mode, that mode can exhibit quantum $g^{(2)}$ equal to 2. For a classical thermal light field, however, the preceding argument may involve superposition between different modes. This once caused confusion in the [open course](https://av.tib.eu/media/42704).

Of course, if Boltzmann law is also used in the classical case, the exponential distribution can be obtained immediately. It is just that the argument using the central limit theorem is exceptionally elegant. Perhaps there is a universal connection between the central limit theorem and Boltzmann law.

