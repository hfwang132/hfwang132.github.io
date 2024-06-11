---
title: "Does the idler light passing through the optical fiber amplifier still entangle with the signal light?"
date: 2024-05-27T18:36:47+08:00
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

Does the idler light passing through the optical fiber amplifier still entangle with the signal light, which is produced by SPDC?

Let's consider two extremes:

Extreme 1: The gain of the amplifier is equal to 1, that is, there is no gain at all.

In this case, the amplifier acts as if it has done nothing and is an identity channel. So, of course, the entanglement will still be maintained. (Actually, it's not necessarily the case. Even if the gain is zero, additional noise may be introduced, but we ignore it here for now).

Extreme 2: The gain of the amplifier is very large.

Assuming that entanglement can be maintained at this point, we can obtain macroscopic Schrödinger cat states. But such states are basically unattainable experimentally because they have already decohered. (Of course, there are exceptions, such as bright squeezed states).

So, between these two extremes, we can say that when the gain is relatively small, entanglement can be maintained, but when the gain is relatively large (actually, the "relatively large" magnitude estimate is about ~10, referring to the N00N state), entanglement will disappear due to noise or decoherence.

Next, let's discuss two cases separately, based on the $\chi^{(2)}$ nonlinear parametric amplifier and the stimulated emission amplifier.

## 1. Optical Amplifier Based on $\chi^{(2)}$ Nonlinearity
If the optical fiber amplifier here is based on $\chi^{(2)}$ nonlinearity, that is, PDC, parametric down-conversion. If PDC is used for optical amplification, it can also be called OPA, optical parametric amplification. Note that PDC here should be distinguished from SPDC, spontaneous parametric down-conversion.

Assuming that the pump for both SPDC and OPA is strong enough, then their Hamiltonians can be written as:

$H_\text{SPDC}=\mathrm{i}\hbar(\hat{a}^\dag \hat{b}^\dag - \hat{a} \hat{b})$ 

$H_\text{OPA} = \mathrm{i}\hbar(\hat{b}^\dag \hat{c}^\dag -\hat{b}\hat{c})$ 

where $\hat{a}$ and $\hat{b}$ represent the annihilation operators on the idler and signal modes of SPDC, and $\hat{b}$ and $\hat{c}$ represent the annihilation operators on the signal and idler modes of OPA.

So the final quantum state is:

$|\Psi\rangle = \exp[\mathrm{i}g_\text{2}H_\text{OPA} /\hbar]\exp[\mathrm{i}g_\text{1}H_\text{SPDC}/\hbar] |0,0,0\rangle_{abc}$ 

where $g_1$ is the logarithm of the gain of SPDC, and $g_2$ is the logarithm of the gain of OPA.

Finally, just trace out the idler of OPA:

$\rho=\operatorname{tr}_c[|\Psi\rangle\langle\Psi|]$ 

> The specific calculations might not be straightforward. If there are quantum information theorists interested in helping with the calculation, it would be great. Also, consider what entanglement measure to use. The PPT criterion definitely cannot be used because these are two modes, not two qubits.  
>   
> However, we can guess the calculation process: blindly guess that the process of passing through OPA and tracing out the OPA idler is equivalent to a dephasing channel. Then we approximate the SPDC state in the low-gain limit as a Bell state. At this point, the degree of entanglement depends directly on the strength of dephasing, which is positively correlated with the gain of OPA, and likely proportional to the gain, i.e., $\exp(g_2)$. Considering a 20 dB gain, the degree of entanglement will decrease by $10^{20/10} = 100$ times.

So after some "calculation", we conclude: the larger the gain of OPA, the smaller the degree of entanglement.

---

## 2. Optical Amplifier Based on Stimulated Emission
The above is about amplifiers based on parametric down-conversion. But the most commonly used EDFA is not based on $\chi^{(2)}$ nonlinearity, but on stimulated emission amplification, similar to the principle of lasers.

At this point, the Hamiltonian is much more complicated than OPA because it involves atoms. Let's first consider a single-mode optical field:

$H = \hbar\omega a^\dag a + \sum_j \hbar \omega_a \sigma^+_j \sigma^-_j + \hbar \Omega \sum_j (\sigma^+_j a -\sigma_j^- a^\dag)$ 

where $\omega$ is the frequency of the optical field, $\omega_a$ is the energy level difference of the atom, $\sigma^{\pm}$ is the raising and lowering operators of the atomic levels, $\Omega$ is the Rabi frequency.

This is actually the Hamiltonian of the Tavis-Cummings model. There is no general analytical solution for this thing, so we can only do perturbation approximations.

After some perturbation calculations [[1]](#ref\_1), we can obtain:

$(\Delta X)^2 = G (\Delta X_{0})^2 + (2 n_{\text{sp}}-1)(G-1) \frac{1}{4}$ 

where $X$ is any quadrature of the optical field, which can be understood as the real or imaginary part of the electric field intensity. $G$ is the gain. $n_\text{sp} = \frac{N_2}{N_2-N_1}$ represents the degree of population inversion. The larger $n_\text{sp}$, the lower the inversion degree, and the smaller $n_\text{sp}$, the higher the inversion degree, with a minimum of 1.

It can be seen that EDFA not only amplifies the noise of the input signal by a factor of $G$, but also introduces additional noise from vacuum fields, and amplifies the noise from vacuum fields by $(2 n_{\text{sp}}-1)(G-1)$ times. This is the Amplified Spontaneous Emission (ASE), the noise amplified by spontaneous emission. See the figure below:

{{< figure src="image/edfa.jpg" title="Wigner representation of the quantum state after passing through EDFA. Image source [1]" >}}

  
The above is about dynamics. How do these dynamics affect entanglement?

It is well known that the signal and idler obtained by SPDC form an entangled state: $|\Psi\rangle_\text{SPDC} \approx |\text{vac}\rangle + \lambda \int \mathrm{d}\omega_s \mathrm{d}\omega_i f(\omega_s,\omega_i)a^\dag_s(\omega_s) a^\dag_i(\omega_i) |\text{vac}\rangle$, where $f(\omega_s,\omega_i)$ is the joint frequency distribution, depending on phase matching conditions and pump linewidth (momentum conservation and energy conservation conditions). $|\text{vac}\rangle$ represents the vacuum state on all modes, and $\lambda \ll 1$ represents the average number of photons of SPDC in the low gain limit, which is commonly used in experiments.

$f(\omega_s,\omega_i)$ is usually inseparable, that is, it cannot be written as $f(\omega_s,\omega_i) = f_s(\omega_s) f_i(\omega_i)$. Therefore, the signal and idler modes of SPDC show frequency entanglement.

Since it is frequency entangled, we need to consider the multi-mode situation. For simplicity, let's consider only two frequency modes $\omega = \mu,\nu$. Then the SPDC state can be written as:

$|\text{vac}\rangle + \lambda (|1\rangle \otimes |0\rangle \otimes |0\rangle \otimes |1\rangle+ |0\rangle \otimes |1\rangle \otimes |1\rangle \otimes |0\rangle)$

where from left to right, the four modes are respectively the $\mu$ and $\nu$ frequency modes of the signal and the $\mu$ and $\nu$ frequency modes of the idler. After amplification by EDFA, we get:

$|0\rangle \otimes |0\rangle \otimes |G,0\rangle \otimes |G,0\rangle   +\lambda(|1\rangle \otimes |0\rangle \otimes |G,0\rangle \otimes |G,1\rangle+ |0\rangle \otimes |1\rangle \otimes |G,1\rangle \otimes |G,0\rangle)$

where $|G,0\rangle,|G,1\rangle$ represent the states obtained by $|0\rangle ,|1\rangle$ after passing through EDFA. I really don't know how to calculate this thing. But we can see some clues from their Wigner function shapes.

Let's first look at the Wigner functions of $|0\rangle$ and $|1\rangle$:

{{< figure src="image/fock_wigner.jpg" title="Wigner functions of vacuum state and single photon state, image source Wikipedia" >}}

After passing through the high gain EDFA, they will spread out like a big pancake from the origin in all directions, and also have to add amplified spontaneous emission noise (ASE), so the Wigner negativity of the single photon state should also disappear.

At this point, the state is already a mixed state with very large uncertainties in both particle number and phase, similar to a thermal state. Why do I claim it's a mixed state? This is because in the Tavis-Cummings model, the final step of the calculation involves tracing out the atomic state, which almost certainly gives a mixed state.

With such a large gain and uncertainty in particle number, the difference between $|0\rangle$ and $|1\rangle$ is already small, so $|G,0\rangle \approx |G,1\rangle$. So the quantum state can be written as:

$ [|0\rangle \otimes |0\rangle+\lambda(|1\rangle \otimes |0\rangle + |0\rangle \otimes |1\rangle)] \otimes (|G,0\rangle \otimes |G,0\rangle)$

The first two modes are signal modes, and the last two modes are idler modes. It can be seen that they are no longer entangled at this point, but separable states.

---

In summary, EDFA amplifies the noise of the input signal and also introduces additional ASE noise. These noises cause the quantum state to become a mixed state. Generally, when entangled pure states become mixed states, the degree of entanglement decreases or even disappears.

If you really want to dig deeper, you can follow the steps in [1] and use perturbation theory to calculate the evolution of the quantum state in the Tavis-Cummings model ([1] calculates in the Heisenberg representation, so it can only provide the expectation values of operators, not the quantum state).

## Reference
1. Inoue, K. Quantum Noise in Optical Amplifiers. in Optical Amplifiers - A Few Different Dimensions (ed. Choudhury, P. K.) (InTech, 2018). doi:10.5772/intechopen.72992.
