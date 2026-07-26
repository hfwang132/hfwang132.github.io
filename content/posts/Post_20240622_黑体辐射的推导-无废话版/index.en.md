---
title: "Derivation of Blackbody Radiation (No-Nonsense Version)"
date: 2024-06-22T18:12:07+08:00
originalURL: "https://zhuanlan.zhihu.com/p/704855471"
aliases:
  - "/en/black_body/"
  - "/en/Post_20240727_黑体辐射的推导-无废话版/"
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

With nothing better to do, let’s review blackbody radiation\~

Many articles on blackbody radiation begin with a lengthy history lesson, which can easily become confusing.

This article gets straight to the point: shut up and calculate.

## 1. What Is the Blackbody Radiation Formula?  
The blackbody radiation formula refers to the energy density radiated by a blackbody per unit frequency.

To calculate the blackbody radiation formula, we need to calculate how many states there are between $\nu$ and $\nu + \mathrm{d}\nu$, how many photons occupy each state, and then multiply them by the photon energy $h\nu$.

$\varepsilon(\nu) \mathrm{d} \nu = [(\nu,\nu+\mathrm{d}\nu) 中有多少个量子态] \times [这些量子态上有多少个光子] \times  h\nu$ 

## 2. Density of States  
How many states are there between $\nu$ and $\nu + \mathrm{d}\nu$?

Consider a rectangular box with periodic boundary conditions, whose length, width, and height are $L\_{x,y,z}$. Then the wavenumber $\kappa\_{x,y,z}$ of electromagnetic waves in the box satisfies:

$\kappa\_i = n\_i/L\_i, \quad(i=x,y,z)$ 


> Note that $\kappa$ is the wavenumber, not the wave vector $k$. Their relation is $k = 2\pi \kappa$.

Thus, the number of quantum states is:

$\mathrm{d} N = \mathrm{d} n\_x\mathrm{d}n\_y\mathrm{d}n\_z = L\_xL\_yL\_z \mathrm{d}\kappa\_x \mathrm{d}\kappa\_y\mathrm{d}\kappa\_z = V \mathrm{d}^3\vec{\kappa}$ 

Let the number of states between $\nu$ and $\nu + \mathrm{d}\nu$ be $f(\nu)$. Then

$f(\nu) \mathrm{d}\nu = \mathrm{d}N = V \mathrm{d}^3\vec{\kappa} = V \cdot4\pi \kappa^2 \mathrm{d}\kappa = V \cdot\frac{4 \pi \nu^2}{c^3} \mathrm{d} \nu$ 

where $\kappa = |\vec{\kappa}|$, and $\nu = c\kappa$.

Therefore, $f(\nu) = V  \cdot4 \pi \nu^2/c^3$.

Since an electromagnetic wave in a given spatial mode has two polarizations, we must also multiply by 2. In addition, we seek the energy density rather than the energy, so we can divide by the volume in advance:

$f(\nu) =  8 \pi \nu^2/c^3$ 

This is the number of states (per unit volume) between $\nu$ and $\nu + \mathrm{d}\nu$.


> The idea in this part is that, in three-dimensional space, the density of states near frequency $\nu$ is proportional to the square of $\nu$, just as the area of a sphere is proportional to the square of its radius.

## 3. Number of Photons in a State  
At thermal equilibrium, how many photons occupy a state with frequency $\nu$? The answer is $1/(e^{h\nu/kT} - 1)$. Let us derive this below:

The partition function for a bosonic system is:

$\begin{aligned} Z &= \sum\_{n\_1,n\_2,\cdots}  \exp[-\beta (n\_1 \varepsilon\_1 + n\_2 \varepsilon\_2 +\cdots)] \\\\ &= \left(\sum\_{n\_1} e^{-\beta n\_1\varepsilon\_1}\right)\left(\sum\_{n\_2} e^{-\beta n\_2\varepsilon\_2}\right)\cdots \\\\ &= \left(\frac{1}{1-e^{-\beta \varepsilon\_1}}\right) \left(\frac{1}{1-e^{-\beta \varepsilon\_2}}\right) \cdots \end{aligned}$ 

where $\varepsilon\_i$ denotes the photon energy in the i-th mode, and $n\_i$ denotes the number of photons in the i-th frequency mode.

Then the average number of photons in the i-th mode is:

$\begin{aligned} \langle n\_i\rangle = -\frac{1}{\beta}\frac{\partial \ln Z}{\partial \varepsilon\_i} = \frac{1}{e^{\beta \varepsilon\_i} - 1} \end{aligned}$ 

That is: the thermal-equilibrium photon number in a state with frequency $\nu$ is $\langle n(\nu)\rangle = 1/(e^{h\nu/kT} - 1)$.


> This is in fact the Bose–Einstein distribution without a chemical potential.

## 4. Result  
$\begin{aligned} \varepsilon(\nu) \mathrm{d} \nu &= [(\nu,\nu+\mathrm{d}\nu) 中有多少个量子态] \times [这些量子态上有多少个光子] \times  h\nu \\\\ &=f(\nu) \mathrm{d} \nu \cdot\langle n(\nu)\rangle \cdot h\nu\\\\ &=\frac{8\pi \nu^2}{c^3} \cdot \frac{1}{e^{h\nu/kT}-1} \cdot h\nu \end{aligned}$ 

Seen this way, the blackbody radiation formula is quite easy to remember: one only needs to remember the density of states $f(\nu)$ and the photon number at thermal equilibrium $\langle n(\nu)\rangle$. The density of states is proportional to the square of the frequency, while the thermal-equilibrium photon number follows the Bose–Einstein distribution.

At low frequencies, $\varepsilon(\nu)$ is limited by the density of states and the energy of a single photon; at high frequencies, $\varepsilon(\nu)$ is limited by the average photon number.



---


> Exercise 1: In a two-dimensional world, what does the density of states look like? What does the blackbody radiation formula look like?  
>   
> Exercise 2: Which step above leads to the ultraviolet catastrophe?  
>   
> Exercise 3: At room temperature and visible-light frequencies ($\sim 5.5 \times 10^{14} \text{Hz}$), what is the approximate thermal-equilibrium photon number in a single mode?



---


> Answer 1: In a two-dimensional world, the density of states is $f(\nu)=2\pi\nu/c^2$, and the blackbody radiation formula is $\varepsilon(\nu)=\frac{2\pi h\nu^2}{c^2(e^{h\nu/kT}-1)}$  
>   
> Answer 2: The ultraviolet catastrophe results from directly replacing $\frac{h\nu}{e^{h\nu/kT}-1}$ with $kT$ from the classical equipartition theorem. When $\nu \ll 1$, $\frac{h\nu}{e^{h\nu/kT}-1} \rightarrow kT$, but when $\nu \gg 1$, $\varepsilon(\nu)$ diverges. This is the ultraviolet catastrophe.  
>   
> Answer 3: At room temperature and visible-light frequencies, $h\nu /kT = \frac{6.6 × 10^{-34} \times 5.5 \times 10^{14}}{1.4 × 10^{-23} \times 300} = 86$, and $\frac{1}{e^{86}-1} \ll 1$. This is why we cannot see blackbody radiation in the visible spectrum.

