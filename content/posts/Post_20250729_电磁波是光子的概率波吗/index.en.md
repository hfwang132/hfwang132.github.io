---
title: "Is an Electromagnetic Wave a Photon Probability Wave?"
date: 2025-07-29T14:22:00+08:00
originalURL: "https://www.zhihu.com/question/1916984034279532400/answer/1933532708040086594"
aliases:
  - "/en/photon_wave_func2/"
  - "/en/Post_20251012_电磁波是光子的概率波吗/"
draft: false
tags: ["electromagnetic waves", "photons"]
categories: ["Quantum Information/Quantum Optics"]
author: "Haifei"
---

## Probability Waves vs. Quantum Fields  

The electromagnetic field is not the probability wave of photons, just as the Dirac field is not the probability wave of electrons.

A probability wave refers to the single-particle wavefunction (in the position representation) in nonrelativistic quantum mechanics.

**Clearly, probability waves** apply only to single-particle states in the nonrelativistic regime. The **electromagnetic field** and the **Dirac field**, on the other hand, are **quantum fields** and must be discussed within the framework of quantum field theory.

Although the Dirac field is not the probability wave of an electron, under the low-velocity and single-electron approximations, the Dirac equation can indeed reduce to the Schrödinger equation. In this case, the first spinor component of the Dirac field is the electron's probability wave, namely the Schrödinger wavefunction. See Appendix 1.

Can photons be treated this way? Unfortunately, no, because photons themselves are relativistic particles, and a low-velocity limit cannot be considered directly.

However, if a cavity is used to endow photons with an effective mass, and one then considers the low-velocity limit, the electromagnetic field can indeed be regarded as a probability wave in the Schrödinger sense [1]. However, this is only an effective description.

Although the low-velocity limit cannot be considered directly, the single-photon case can still be considered. In this case, one can indeed define a probability distribution related to the electromagnetic field. However, this probability distribution does not have the desirable properties of a Schrödinger wavefunction, such as a conserved probability current. See below for details.

In short, remember: probability waves are not fundamental entities. Quantum fields are the fundamental entities, while probability waves are merely approximations of quantum fields in the nonrelativistic and single-particle regime.

Below, we answer two questions:

1. Since the electromagnetic field is not the probability wave of photons, how is the probability of detecting a photon calculated?
2. Since the electromagnetic field is not the probability wave of photons, what exactly is the electromagnetic field?

---

## How to Calculate the Probability of Detecting a Photon  

Question 1: Since the electromagnetic field is not a probability wave, how is the probability of detecting a photon calculated?

The correct question should be: what is the probability $w(\mathbf{r},t) \mathrm{d}t$ that the quantum state of the optical field, initially in state $|i\rangle$, evolves during the interval from $t$ to $t+\mathrm{d}t$ and has one photon detected (absorbed) at $\mathbf{r}$, becoming the final state $|f\rangle$? Glauber's photodetection theory [2] tells us that the answer is:

$\begin{aligned} w(\mathbf{r},t) \propto |\langle f | E^{(+)}(\mathbf{r},t)| i\rangle|^2 \end{aligned}$

Here $E^{(+)}$ is the electric-field annihilation operator: $E^{(+)}(\mathbf{r},t)=\sum_\mathbf{k,\sigma} \mathcal{E}_\mathbf{k}a_\mathbf{k,\sigma}e^{\mathrm{i}(\mathbf{k}\cdot \mathbf{r}-\omega_\mathbf{k} t)}$, where $\sigma = 0,1$ denotes polarization, $a_{\mathbf{k},\sigma}$ is the annihilation operator for mode $(\mathbf{k},\sigma)$, $\mathcal{E}_\mathbf{k}=\sqrt{\frac{\hbar \omega_\mathbf{k}}{\epsilon_0 V}}$ is the single-photon amplitude and has the dimensions of an electric field, and $V$ is the mode volume of the optical field.

> As for why the probability is proportional to $\begin{aligned} |\langle f | E^{(+)}(\mathbf{r},t)| i\rangle|^2 \end{aligned}$, and what the proportionality constant is, one must take into account the dynamics of the detector itself (usually an atom) and use the full quantum field theory approach. This will not be discussed further here (hand-wavingly).

However, when detecting a photon, we usually do not know what the final state is; we only know that one photon has been detected. Therefore, we need to sum over the final state $|f\rangle$:

$\begin{aligned} \sum_f|\langle f | E^{(+)}(\mathbf{r},t)| i\rangle|^2 &= \sum_f\langle i | E^{(-)}|f\rangle \langle f| E^{(+)} |  i\rangle \\\\ &= \langle i|E^{(-)}E^{(+)}|i\rangle  \end{aligned}$

Therefore, the probability that the quantum state of the optical field, initially in state $|i\rangle$, evolves during the interval from $t$ to $t+\mathrm{d}t$ and has one photon detected (absorbed) at $\mathbf{r}$, becoming the final state $|f\rangle$, is $w(\mathbf{r},t) \propto \langle i|E^{(-)}E^{(+)}|i\rangle $.

Clearly, $\langle E^{(-)}E^{(+)}\rangle $ is the field quantity closest to a probability distribution. However, it still does not satisfy the properties of a probability distribution. This is because photon number is not conserved, making it difficult to normalize it.

> Why the electric field $E^{(\pm)}$ rather than the magnetic field $B^{(\pm)}$? Because photon absorption is usually accomplished through electric dipole interactions with atoms. However, since we are discussing proportionality here, one may use $B^{(\pm)}$ or even the vector potential $A^{(\pm)}$, because the transverse-field part $A^{(\pm)},E^{(\pm)},B^{(\pm)}$ is always proportional, and only the transverse-field part contributes to the dipole interaction.

Since the nonconservation of photon number prevents normalization, can we artificially restrict the photon number? The answer is yes. We can restrict the number of photons to one, with the single-photon state given by:

$|1_\psi\rangle = \sum_{\mathbf{k},\sigma} \psi_\mathbf{k,\sigma}|1_\mathbf{k,\sigma}\rangle = \sum_\mathbf{k,\sigma} \psi_\mathbf{k,\sigma} a^\dagger_\mathbf{k,\sigma} |0\rangle$

where $\sum_{\mathbf{k},\sigma} |\psi_\mathbf{k,\sigma}|^2 = 1$.

We can then define something resembling a wavefunction [3]:

$\psi(\mathbf{r},t) = \langle 0 | E^{(+)}(\mathbf{r},t) | 1_\psi\rangle$

The probability of detecting one photon in some region $D$ is then proportional to $\int_D |\psi(\mathbf{r})|^2 \mathrm{d}^3 \mathbf{r}$. This is because:

$\begin{aligned} \int_D |\psi(\mathbf{r})|^2 \mathrm{d}^3 \mathbf{r} &= \langle 1_\psi | E^{(-)}(\mathbf{r}) | 0\rangle\langle 0 | E^{(+)}(\mathbf{r}) | 1_\psi\rangle \\\\ &=  \langle 1_\psi | E^{(-)}(\mathbf{r}) E^{(+)}(\mathbf{r}) | 1_\psi\rangle \end{aligned}$

> The second equality follows because $E^{(-)}$ annihilates one photon, causing $ E^{(+)}(\mathbf{r}) | 1_\psi\rangle$ to be proportional to $|0\rangle$.

To make $\psi(\mathbf{r},t)$ a genuine probability distribution, we must also normalize it to eliminate the dimensions. Let us first expand $\psi(\mathbf{r},t)$:

$\begin{aligned} \psi(\mathbf{r},t) &= \langle 0 | E^{(+)}(\mathbf{r},t) | 1_\psi\rangle \\\\ &= \left\langle 0 \left| \sum_\mathbf{k,\sigma} \mathcal{E}_\mathbf{k}a_\mathbf{k,\sigma}e^{\mathrm{i}(\mathbf{k}\cdot \mathbf{r}-\omega_\mathbf{k} t)} \psi_\mathbf{k,\sigma} a^\dagger_\mathbf{k,\sigma} \right| 0 \right\rangle \\\\ &=  \sum_\mathbf{k,\sigma} \mathcal{E}_\mathbf{k}e^{\mathrm{i}(\mathbf{k}\cdot \mathbf{r}-\omega_\mathbf{k} t)} \psi_\mathbf{k,\sigma}  \end{aligned}$

Here $\mathcal{E}_\mathbf{k}$ carries the dimensions of an electric field. We only need to add the denominator corresponding to the sum to obtain a dimensionless single-photon probability distribution.

However, this applies only to the single-photon subspace. Since photon number is generally not conserved, its range of application is very limited. Furthermore, unlike the Schrödinger wavefunction, it cannot define a conserved probability current.

## What Exactly Is the Electromagnetic Field?  

Question 2: Since the electromagnetic field is not a probability wave, what exactly is the electromagnetic field?

The electromagnetic field is essentially the photon field $A_\mu$ in quantum field theory. Like the fields $\psi$ of all other kinds of particles (the Dirac field, gluon field, quark field...), the photon field is a quantum field.

As for what a quantum field is, the answer must be sought in quantum field theory. Since this article is not a quantum field theory textbook, readers will have to consult one themselves.

> Some people may say: the electromagnetic field is obviously a classical field! What makes you say that it is a quantum field? To this I can only say: you too young too simple. This is like saying that an electron is a classical little ball—when you have not studied quantum mechanics, you think all particles are classical particles; when you have not studied quantum field theory, you think all fields are classical fields. In fact, everything is quantum; it is just that quantum behavior often does not manifest itself.  
>   
> When does the electromagnetic field exhibit quantum behavior? The Lamb shift, the Casimir effect, spontaneous emission... The electromagnetic field exhibits quantum behavior in many phenomena. Cat states, GKP states... These superposition states of amplitudes and phases are even more direct manifestations of the quantum electromagnetic field.  
>   
> The reason macroscopic electromagnetic waves do not exhibit quantum behavior is that photons are easily lost (absorbed/scattered), and the corresponding Lindblad operator is the annihilation operator. The pointer states of an open system are eigenstates of the Lindblad operator, while the eigenstates of the annihilation operator are precisely coherent states (Coherent state). They have definite amplitudes and phases, and their quantum uncertainty is far smaller than their magnitudes. This is why the electromagnetic waves encountered in everyday life are all classical: classical electromagnetic waves can survive loss.

## Appendix 1: How the Dirac Equation Approximates the Schrödinger Equation / How a Quantum Field Approximates a Probability Wave  
> The Dirac equation  
> $\mathrm{i}\gamma^\mu D_\mu \psi - m\psi=0$,  
> where  
> $\gamma^0 = \begin{bmatrix} I & 0 \\\\ 0 &-I \end{bmatrix},\  \gamma^i=\begin{bmatrix} 0 & \sigma^i \\\\ -\sigma^i & 0 \end{bmatrix} \quad(i=1,2,3)$   
> $\sigma^i $ are the Pauli matrices,  
> and $\psi = \begin{bmatrix}\psi_1 \\\\ \psi_2\end{bmatrix}$, where $\psi_1 = \begin{bmatrix}\psi_{1\uparrow} \\\\ \psi_{1\downarrow}\end{bmatrix}$ are the two spin components of the electron, and $\psi_2 = \begin{bmatrix}\psi_{2\uparrow} \\\\ \psi_{2\downarrow}\end{bmatrix}$ are the two spin components of the positron.  
> Substituting into the Dirac equation gives:  
> $\mathrm{i}\begin{bmatrix} I & 0 \\\\ 0 &-I \end{bmatrix} D_t \begin{bmatrix}\psi_1 \\\\ \psi_2\end{bmatrix} + \mathrm{i} \begin{bmatrix} 0 & \bm\sigma \cdot \mathbf{D} \\\\ -\bm\sigma \cdot \mathbf{D} & 0 \end{bmatrix} \begin{bmatrix}\psi_1 \\\\ \psi_2 \end{bmatrix} -m \begin{bmatrix}\psi_1 \\\\ \psi_2\end{bmatrix}=0$   
> where $D_t =  \partial_t +\mathrm{i}eA_0 = \partial_t - \mathrm{i}e\phi$, $\mathbf{D} = \nabla +\mathrm{i}e\mathbf{A}$ (using the $(-,+,+,+)$ metric convention).  
> Simplifying gives  
> $\mathrm{i} \begin{bmatrix}D_t\psi_1 \\\\ -D_t\psi_2\end{bmatrix} +\mathrm{i} \begin{bmatrix}\bm\sigma\cdot \mathbf{D} \psi_2 \\\\ -\bm\sigma\cdot \mathbf{D}\psi_1\end{bmatrix} -m \begin{bmatrix}\psi_1 \\\\ \psi_2\end{bmatrix}=0$   
> that is,  
> $\boxed{ \begin{aligned} \mathrm{i} D_t \psi_1 + \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi_2 - m\psi_1 &= 0 \\\\ -\mathrm{i} D_t \psi_2 - \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi_1 - m\psi_2 &= 0 \end{aligned}  }\quad (\star)$   
> This is the expanded form of the Dirac equation: we write the electron term $\psi_1$ and the positron term $\psi_2$ as two equations. Originally, they were in the same equation.  
> In the low-energy regime, we do not consider the phase change $\mathrm{e}^{-\mathrm{i}mt}$ due to the electron rest mass, so we separate it out; that is, we replace $\psi = \begin{bmatrix}\psi_1\\\\ \psi_2\end{bmatrix}$ with $\psi = \begin{bmatrix}\varphi \mathrm{e}^{-\mathrm{i}mt}\\\\ \chi  \mathrm{e}^{-\mathrm{i}mt}\end{bmatrix}$. Substituting this into the expanded Dirac equation $(\star)$ gives:  
> $\begin{aligned} &\mathrm{i} D_t \varphi + \mathrm{i} \bm\sigma \cdot \mathbf{D} \chi  = 0 &(1)\\\\ -&\mathrm{i} D_t \chi - \mathrm{i} \bm\sigma \cdot \mathbf{D} \varphi - 2m\chi = 0 &(2) \end{aligned}$   
> Since the positron term $\chi$ is small in the low-energy regime, $D_t \chi \approx 0$. Substituting this into $(2)$ gives:  
> $\chi \approx - \frac{\mathrm{i}}{2m} \bm\sigma \cdot \mathbf{D} \varphi$   
> Substituting this again into $(1)$ gives:  
> $\mathrm{i} D_t \varphi +  \frac{1}{2m}(\bm\sigma \cdot \mathbf{D})^2 \varphi = 0 $   
> It can be shown (see Appendix 2) that  
> $\begin{aligned} (\bm \sigma \cdot \mathbf{D})^2 &=\mathbf{D}^2 - \mathrm{i}e \bm\sigma\cdot \mathbf{B} \\\\ &= (\nabla +\mathrm{i}e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B} \\\\ &= -(\mathbf{p} + e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B}  \end{aligned}$   
> Therefore  
> $\mathrm{i} D_t \varphi =  \frac{1}{2m}[(\mathbf{p} + e\mathbf{A})^2 + e \bm\sigma\cdot \mathbf{B} ] \varphi$   
> Substituting $D_t = \partial_t - \mathrm{i}e\phi$ gives  
> $\boxed{ \mathrm{i} \partial_t \varphi =  \left[\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2+ \frac{e}{2m} \bm\sigma\cdot \mathbf{B}  - e\phi  \right]\varphi }$   
> This is the Schrödinger equation for an electron (with spin), also called the Pauli equation. Note that $e$ is positive here, whereas the electron $\varphi$ carries negative charge.  
> The $\varphi$ here is the probability wave, namely the wavefunction referred to in nonrelativistic quantum mechanics.

## Appendix 2  

Prove $(\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B}$, where $\mathbf{D} = \nabla+ \mathrm{i}e\mathbf{A}$.

> Using the identity  
>   
> $(\bm\sigma \cdot \mathbf{a})(\bm\sigma \cdot \mathbf{b}) = \mathbf{a} \cdot \mathbf{b} + \mathrm{i}\bm\sigma \cdot(\mathbf{a}\times\mathbf{b})$  
>   
> gives  
>   
> $(\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D})$  
>   
> Thus we need to calculate $(\mathbf{D}\times\mathbf{D})$.  
>   
> We first calculate $[D_i, D_j]$:  
>   
> $\begin{aligned} [D_i, D_j] &= [\partial_i +\mathrm{i}eA_i, \partial_j +\mathrm{i}eA_j] \\\\ &= \cancel{[\partial_i,\partial_j]} + \cancel{e^2[A_i, A_j]} + \mathrm{i}e[\partial_i, A_j] - \mathrm{i}e[\partial_j,A_i] \end{aligned}$  
>   
> Thus we need to calculate $[\partial_i, A_j]$:  
>   
> $\begin{aligned} [\partial_i, A_j] f &= \partial_i (A_j f) -A_j \partial_i f \\\\ &= (\partial_i A_j) f + A_j \partial_if - A_j \partial_i f \\\\ &= (\partial_iA_j)f \end{aligned}$  
>   
> Therefore $[\partial_i, A_j] = (\partial_i A_j)$.  
>   
> Thus  
>   
> $\begin{aligned} [D_i, D_j] &= \mathrm{i}e[\partial_i, A_j] -\mathrm{i}e[\partial_j,A_i] \\\\ &= \mathrm{i}e (\partial_i A_j - \partial_j A_i) \\\\ &= \mathrm{i}e \epsilon_{ijk}B^k \end{aligned}$  
>   
> Thus  
>   
> $\begin{aligned} (\mathbf{D}\times\mathbf{D})^k &=\epsilon^{kij} D_i D_j \\\\ &= \frac{1}{2} \epsilon^{kij}[D_i,D_j] \\\\ &= \frac{\mathrm{i}e}{2} \epsilon^{kij} \epsilon_{ijl} B^l \\\\ &= \frac{\mathrm{i}e}{2} (\delta^k_l \delta^j_j - \delta^k_j\delta^j_l) B^l \\\\ &=\mathrm{i}e \delta^k_l B^l \\\\ &= \mathrm{i}eB^k \end{aligned}$  
>   
> Therefore $\mathbf{D}\times \mathbf{D} = \mathrm{i}e\mathbf{B}$.  
>   
> Thus  
>   
> $\begin{aligned} (\bm\sigma \cdot \mathbf{D})^2 &= \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D}) \\\\ &= \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B} \end{aligned}$  
>   
> Q.E.D.

## References  

1. [1]Sharoglazova, V., Puplauskis, M., Mattschas, C. et al. Energy–speed relationship of quantum particles challenges Bohmian mechanics. Nature 643, 67–72 (2025). [https://www.nature.com/articles/s41586-025-09099-4](https://www.nature.com/articles/s41586-025-09099-4)
2. [2]Scully, M.O. and Zubairy, M.S. (1997) Quantum Optics. Cambridge University Press, Cambridge. http://dx.doi.org/10.1017/CBO9780511813993
3. [3] arXiv:quant-ph/0508202 [https://arxiv.org/pdf/quant-ph/0508202](https://arxiv.org/pdf/quant-ph/0508202)
