---
title: "Since Parseval's Theorem for the Fourier Transform Represents a Conservation Law, What Symmetry Corresponds to It?"
date: 2024-01-26T23:49:29+08:00
draft: false
tags: ["Symmetry"]
categories: ["Mathematical Methods in Physics"]
---

**Link:** [https://www.zhihu.com/question/640869828/answer/3373753127]

Here is a preliminary exploration.

## Fourier-Plancherel Operator
Define the Fourier-Plancherel operator $\mathcal{F} \in \mathcal{L}(L^2(\mathbb{R}))$ as:

$(\mathcal{F}\varphi)(p)=\frac{1}{\sqrt{2\pi}}\int\_{\mathbb{R}}\mathrm{e}^{-ipx}\varphi(x)\mathrm{d}x$ 

It is actually a unitary operator:

$\mathcal{F}^\dag\mathcal{F}=\mathbb{I}\_{L^2(\mathbb{R})}$ 

And Parseval's theorem is merely a restatement of this fact:

$\langle\varphi \mathcal{F}^\dag|\mathcal{F\varphi}\rangle=\langle\varphi|\mathcal{F}^\dag\mathcal{F}|\varphi\rangle=\langle\varphi|\varphi\rangle=1$ 

Does this theorem involve any conservation of physical quantities?

Of course, I can also say the conservation associated with the "identity operator" (that is, conservation of probability).

$\langle\varphi|\mathcal{F}^\dag\mathbb{I}\_{L^2(\mathbb{R})}\mathcal{F}|\varphi\rangle=\langle\varphi|\mathbb{I}\_{L^2(\mathbb{R})}|\varphi\rangle=1$ 

This is because $[\mathcal{F},\mathbb{I}\_{L^2(\mathbb{R})}]=0$ .

But all operators commute with the identity operator, so this is nothing special.

## Some Properties of the Fourier-Plancherel Operator
**Property 1:** $\mathcal{F}^\dag Q\mathcal{F} = P$ , $\mathcal{F}P\mathcal{F}^\dag  = Q$

Where $Q$ and $P$ are the position and momentum operators, defined as:

$(Q\varphi)(x)=x\varphi(x)$ 

$(P\varphi)(x) = -\mathrm{i}\varphi^\prime(x)$ 

**Property 2:** $\mathcal{F}^2=(\mathcal{F}^*)^2=\mathcal{P}$ 

Where $\mathcal{P}$ is the parity operator, defined as:

$(\mathcal{P}\varphi)(x)=\varphi(-x)$ 

**Property 3:** $\mathcal{F}^4=\mathbb{I}\_{L^2(\mathbb{R})}$ 

This is because $\mathcal{P}^2=\mathbb{I}\_{L^2(\mathbb{R})}$ 

## Conserved Quantities
We know that the conservation corresponding to parity symmetry is parity symmetry itself, i.e., the Hamiltonian is invariant under parity transformation.

As a review, let's briefly derive parity conservation.

Parity transformation is represented by the parity operator $\mathcal{P}$.

The Hamiltonian is invariant under parity transformation, which can be written as:

$\mathcal{P}\mathcal{H}\mathcal{P}^\dag=\mathcal{H}$ 

or

$[\mathcal{H},\mathcal{P}]=0$ 

Thus:

$\frac{\mathrm{d}}{\mathrm{d}t}\langle \mathcal{P} \rangle = \frac{\mathrm{i}}{\hbar}\langle[\mathcal{H},\mathcal{P}]\rangle = 0$ 

i.e., parity is conserved.

So, is there a conserved quantity corresponding to the Fourier-Plancherel operator $\mathcal{F}$? Unfortunately, $\mathcal{F}$ is not an observable because it is not a self-adjoint operator.

> However, we can define $\mathcal{G} = \frac{\mathcal{F}+\mathcal{F}^\dag}{2}$, making $\mathcal{G}$ a self-adjoint operator. It corresponds to the Fourier cosine transform.  
>   
> That said, although $\mathcal{F}$ is not self-adjoint, it is a normal operator, meaning it can be orthogonally diagonalized, although its eigenvalues are not necessarily real.  
>   
> Some authors define observables as normal operators rather than self-adjoint ones. In this sense, $\mathcal{F}$ can be an observable.

If we must have a conserved quantity, it seems not impossible. Suppose there is a Hamiltonian invariant under the Fourier-Plancherel transform:

$\mathcal{F}^\dag\mathcal{H}\mathcal{F} = \mathcal{H}$ 

i.e.,

$[\mathcal{H},\mathcal{F}]=0$ 

then:

$\frac{\mathrm{d}}{\mathrm{d}t}\langle \mathcal{F} \rangle = \frac{\mathrm{i}}{\hbar}\langle[\mathcal{H},\mathcal{F}]\rangle = 0$ 

At this time, $\langle\mathcal{F}\rangle$ is a conserved quantity. However, I'm not sure what significance this conserved quantity has at the moment.

You may wonder if there exists a Hamiltonian satisfying $\mathcal{F}^\dag\mathcal{H}\mathcal{F} = \mathcal{H}$. Of course! The well-known harmonic oscillator Hamiltonian $\mathcal{H}=P^2+Q^2$ satisfies this condition because

$$
\begin{aligned} \mathcal{F}^\dag\mathcal{H}\mathcal{F}&=\mathcal{F}^\dag(P^2+Q^2)\mathcal{F} \\\\ 
&=(\mathcal{F}^\dag P\mathcal{F})^2+(\mathcal{F}^\dag Q\mathcal{F})^2 \\\\
&=(\mathcal{P}^\dag Q\mathcal{P})^2+P^2 \\\\
&=(-Q)^2+P^2 \\\\
&=\mathcal{H} \end{aligned}
$$ 

