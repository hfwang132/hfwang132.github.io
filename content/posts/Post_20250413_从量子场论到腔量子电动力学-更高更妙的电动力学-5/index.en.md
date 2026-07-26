---
title: "From Quantum Field Theory to Cavity Quantum Electrodynamics [Higher and More Subtle Electrodynamics · 6]"
date: 2025-04-13T01:52:37+08:00
originalURL: "https://zhuanlan.zhihu.com/p/1894566826417034044"
aliases:
  - "/en/gm_5/"
  - "/en/Post_20250406_从量子场论到腔量子电动力学-更高更妙的电动力学-5/"
draft: false
categories: ["Mathematical Physics Methods"]
tags: ["quantum field theory", "cavity quantum electrodynamics", "electrodynamics", "Jaynes-Cummings"]
math: true
author: "Haifei"
---

In this article, we start from the QED Lagrangian:

\[\begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi - eA_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \end{aligned} \]

This Lagrangian is highly complex: it not only takes into account the electron's antiparticle—the positron—but the coupling term \(- eA_\mu \bar{\psi} \gamma^\mu \psi\) is also a cubic term, capable of describing various processes such as electron-positron pair creation/annihilation. Due to the presence of the cubic term, this Lagrangian has no analytic solution and can only be solved using perturbation theory in quantum field theory.

However, after a series of simplifications and approximations (the low-energy approximation, the Born-Oppenheimer approximation, the long-wavelength/dipole approximation, the two-level approximation, and the rotating-wave approximation), we surprisingly arrive at a model with an analytic solution:

\[H =  \frac{\omega_{ab}}{2} \sigma_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger) \]

This is the classic Hamiltonian of cavity quantum electrodynamics: the Jaynes-Cummings Hamiltonian. How is this achieved? Let us break it down below.

---

## I. Canonical Quantization  

If only the electromagnetic field or only the Dirac field is present, then because their Lagrangians/Hamiltonians contain only quadratic terms, the harmonic oscillator model can be used to directly obtain analytic solutions.

For example, the canonical quantization of the electromagnetic field in vacuum uses the harmonic oscillator model in the Coulomb gauge \( \nabla \cdot \mathbf{A} = 0\) to obtain creation and annihilation operators and analytic solutions for plane-wave modes. The evolution of these modes is mutually independent (decoupled).

> The analytic solution is \(\mathbf{A}(\mathbf{x},t) = \sum_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega_\mathbf{k}V}} \left[ a_{\mathbf{k},\sigma} \bm{\epsilon}_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}(\mathbf{k}\cdot \mathbf{x}-\omega_\mathbf{k}t)} + \text{h.c.} \right]\), where \(\epsilon_{\mathbf{k},\sigma}\) denotes two vectors perpendicular to \(\mathbf{k}\) and to each other, \(\sigma\) denotes polarization, \(\text{h.c.}\) denotes Hermitian conjugate, and \(V\) denotes the cavity volume. If it is not a cavity but all of space, replace \(\sum\frac{1}{\sqrt{V}}\) with \(\int \mathrm{d}^3\mathbf{k} \frac{1}{(2\pi)^{3/2}}\).  
>   
> Since canonical quantization is standard textbook material in quantum optics, we will not elaborate on it here. For details, see the appendix chapters of [Atom-Photon Interactions by Cohen-Tannoudji](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197)[[1]](#ref\_1).

In the presence of sources, we cannot set \(\phi=0\) under the condition \(\nabla\cdot \mathbf{A}=0\), which means that there are no longer only transverse modes \(\mathbf{E}_{\perp}(\mathbf{k},t) = -\partial_t \mathbf{A}(\mathbf{k},t)\); there are also longitudinal modes \(\mathbf{E}_{\parallel}(\mathbf{k},t) = -\mathrm{i}\mathbf{k} \phi(\mathbf{k},t) = -\mathrm{i}\frac{\mathbf{k}}{k^2} \rho(\mathbf{k},t)\) associated with the sources.

The transverse modes \(\mathbf{E}_{\perp}\) can be represented using creation and annihilation operators for plane-wave modes, but the longitudinal modes \(\mathbf{E}_{\parallel}\) are associated with the sources.

If we regard the sources as classical objects, then the longitudinal modes cannot be quantized.

If, however, we treat the sources fully quantum mechanically—that is, treat them as quantum fields like \(\mathbf{A}\) (namely \(\rho = -e\bar\psi\gamma^0\psi =  -e\psi^\dagger\psi\))—then the longitudinal modes are coupled to the Dirac field \(\psi\). At this point, the modes that can be decoupled are no longer plane-wave modes, but mixed modes of the electromagnetic and Dirac fields.

If we could solve for these modes, that would still be fine. But this is where the problem arises: unlike the free terms \(\bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi \) and \(-\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \), the coupling term \(e\bar\psi A_\mu\gamma^\mu \psi\) is not quadratic—it is cubic and anharmonic! This prevents us from analytically calculating the mixed modes; in other words, there is no analytic solution. At most, we can write \(\mathbf{A}(\mathbf{x})\) rather than \(\mathbf{A}(\mathbf{x},t)\):

\[\mathbf{A}(\mathbf{x}) = \sum_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega_\mathbf{k}V}} \left[ a_{\mathbf{k},\sigma} \bm{\epsilon}_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}\mathbf{k}\cdot \mathbf{x}} + \text{h.c.} \right]\]

The time dependence of this field \(\mathbf{A}(\mathbf{x})\) cannot be written in analytic form. The same is true for the Dirac field \(\psi\).

At this point, we can only use perturbation theory to solve the system, treating the coupling term as a perturbation on top of the free terms.

Fortunately, the coupling constant \(e = \sqrt{4\pi \alpha} \simeq 0.3\) (in natural units) between the electromagnetic and Dirac fields is not very strong, making perturbation theory applicable. What follows is the subject matter of quantum field theory—calculating the S-matrix, scattering amplitudes, and so on—which will not be introduced here.

## II. Low-Energy Approximation  

In high-energy situations, we need quantum field theory. But in low-energy situations, we have a well-developed approximate theory: quantum mechanics. In this section, we examine how the Lagrangian in the high-energy regime reduces to an effective Hamiltonian in the low-energy regime.

### 2.1 High-Energy Physics / Low-Energy Physics  

Let us first review the physical meanings of the operator fields \(\psi\), \(\bar\psi\), and \(A\):

The physical meaning of the field \(\psi(\mathbf{x},t)\) is to annihilate an electron or create a positron at the spacetime point \((\mathbf{x},t)\).

The physical meaning of the field \(\bar\psi\) is to create an electron or annihilate a positron.

In the Lagrangian, these two fields always appear in pairs because of charge conservation.

The field \(A_\mu\) can both create and annihilate photons, because the photon is its own antiparticle.

Thus, the coupling term \( e\bar{\psi} \gamma^\mu A_\mu \psi\) can describe the following various processes:

1. Annihilate an electron, create a photon, and then create an electron.
2. Annihilate an electron, annihilate a photon, and then create an electron.
3. Annihilate a photon and create an electron-positron pair.
4. Annihilate an electron-positron pair and create a photon.
5. ... (other higher-order processes)

Among these, 3 and 4, as well as other higher-order processes, belong to high-energy physics and require quantum field theory to handle.

By contrast, 1 and 2 belong to low-energy physics. They represent an electron transitioning from one state to another by absorbing or emitting a photon.

Considering only the low-energy regime entails the following two points:

> 1. The number of electrons remains unchanged. The creation and annihilation of electron-positron pairs are neglected.  
>   
> 2. The positron term \(\psi _2\approx 0\) of the Dirac field \(\psi = \begin{bmatrix}\psi_1\\ \psi_2\end{bmatrix}\) is small. The electron term \(\psi_1 = \begin{bmatrix}\psi_{1\uparrow} \\ \psi_{1\downarrow}\end{bmatrix}\) is what concerns us. This is because our universe is filled with electrons, whereas positrons are scarce.

The theory in the low-energy regime can be greatly simplified, as shown in Section 4.3. Before that, however, let us expand the Dirac equation for familiarity.

### 2.2 Dirac Equation  

Varying the QED Lagrangian yields the Dirac equation

\(\mathrm{i}\gamma^\mu D_\mu \psi - m\psi=0\),

where

\[\gamma^0 = \begin{bmatrix} I & 0 \\ 0 &-I \end{bmatrix},\  \gamma^i=\begin{bmatrix} 0 & \sigma^i \\ -\sigma^i & 0 \end{bmatrix} \quad(i=1,2,3)\]

\(\sigma^i \) are the Pauli matrices,

and \(\psi = \begin{bmatrix}\psi_1 \\ \psi_2\end{bmatrix}\), where \(\psi_1 = \begin{bmatrix}\psi_{1\uparrow} \\ \psi_{1\downarrow}\end{bmatrix}\) are the two spin components of the electron, and \(\psi_2 = \begin{bmatrix}\psi_{2\uparrow} \\ \psi_{2\downarrow}\end{bmatrix}\) are the two spin components of the positron.

Substituting into the Dirac equation gives:

\[\mathrm{i}\begin{bmatrix} I & 0 \\ 0 &-I \end{bmatrix} D_t \begin{bmatrix}\psi_1 \\ \psi_2\end{bmatrix} + \mathrm{i} \begin{bmatrix} 0 & \bm\sigma \cdot \mathbf{D} \\ -\bm\sigma \cdot \mathbf{D} & 0 \end{bmatrix} \begin{bmatrix}\psi_1 \\ \psi_2 \end{bmatrix} -m \begin{bmatrix}\psi_1 \\ \psi_2\end{bmatrix}=0\]

where \(D_t =  \partial_t +\mathrm{i}eA_0 = \partial_t - \mathrm{i}e\phi\) and \(\mathbf{D} = \nabla +\mathrm{i}e\mathbf{A}\) (using the \((-,+,+,+)\) metric convention).

Simplifying gives

\[\mathrm{i} \begin{bmatrix}D_t\psi_1 \\ -D_t\psi_2\end{bmatrix} +\mathrm{i} \begin{bmatrix}\bm\sigma\cdot \mathbf{D} \psi_2 \\ -\bm\sigma\cdot \mathbf{D}\psi_1\end{bmatrix} -m \begin{bmatrix}\psi_1 \\ \psi_2\end{bmatrix}=0\]

that is,

\[\boxed{ \begin{aligned} \mathrm{i} D_t \psi_1 + \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi_2 - m\psi_1 &= 0 \\ -\mathrm{i} D_t \psi_2 - \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi_1 - m\psi_2 &= 0 \end{aligned}  }\quad (\star)\]

This is the expanded form of the Dirac equation: we have written the electron term \(\psi_1\) and the positron term \(\psi_2\) as two equations. Originally, they were in the same equation.

We can further expand each of them into two equations corresponding to the two spin states. However, since we are more familiar with Pauli operators, there is no need to do so.

So far, we have not made any approximations. Beginning with the next section, we apply the low-energy approximation to the Dirac equation.

### 2.3 Low-Energy Effective Hamiltonian  

In the low-energy regime, we do not consider the phase variation \(\mathrm{e}^{-\mathrm{i}mt}\) caused by the electron rest mass, so we separate it out by replacing \(\psi = \begin{bmatrix}\psi_1\\ \psi_2\end{bmatrix}\) with \(\psi = \begin{bmatrix}\varphi \mathrm{e}^{-\mathrm{i}mt}\\ \chi  \mathrm{e}^{-\mathrm{i}mt}\end{bmatrix}\). Substituting this into the expanded Dirac equation \((\star)\) gives:

\[\begin{aligned} &\mathrm{i} D_t \varphi + \mathrm{i} \bm\sigma \cdot \mathbf{D} \chi  = 0 &(1)\\ -&\mathrm{i} D_t \chi - \mathrm{i} \bm\sigma \cdot \mathbf{D} \varphi - 2m\chi = 0 &(2) \end{aligned}\]

Since the positron term \(\chi\) is small in the low-energy regime, \(D_t \chi \approx 0\). Substituting this into \((2)\) gives:

\[\chi \approx - \frac{\mathrm{i}}{2m} \bm\sigma \cdot \mathbf{D} \varphi\]

Substituting it further into \((1)\) gives:

\[\mathrm{i} D_t \varphi +  \frac{1}{2m}(\bm\sigma \cdot \mathbf{D})^2 \varphi = 0 \]

It can be shown (see the appendix) that

\[\begin{aligned} (\bm \sigma \cdot \mathbf{D})^2 &=\mathbf{D}^2 - \mathrm{i}e \bm\sigma\cdot \mathbf{B} \\ &= (\nabla +\mathrm{i}e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B} \\ &= -(\mathbf{p} + e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B}  \end{aligned}\]

Therefore,

\[\mathrm{i} D_t \varphi =  \frac{1}{2m}[(\mathbf{p} + e\mathbf{A})^2 + e \bm\sigma\cdot \mathbf{B} ] \varphi\]

Substituting \(D_t = \partial_t - \mathrm{i}e\phi\) yields

\[\boxed{ \mathrm{i} \partial_t \varphi =  \left[\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2+ \frac{e}{2m} \bm\sigma\cdot \mathbf{B}  - e\phi  \right]\varphi }\]

This is the Schrödinger equation for an electron (with spin), also called the Pauli equation. Note that \(e\) is positive here, while the electron \(\varphi\) carries negative charge.

We may therefore define the effective Hamiltonian of the electron as:

\[\boxed{ H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2- \frac{e}{2m} \bm\sigma\cdot \mathbf{B}  - e\phi   }\]

Since the magnetic field is much weaker than the electric field \(B\sim E/c\), the order of magnitude of the magnetic-field-related term (\(\frac{e}{2m} \bm\sigma\cdot \mathbf{B}\)) in the Hamiltonian is \(\alpha\approx \frac{1}{137}\) times that of the electric-field-related term (\(e\phi\)). Therefore, in the usual Hamiltonian \(H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2 - e\phi  \), we can neglect the spin term \(\frac{e}{2m} \bm\sigma\cdot \mathbf{B}\).

Thus, **the low-energy limit of quantum field theory is quantum mechanics**.

> We know that solving the spinless Schrödinger equation in the hydrogen atom yields results requiring fine-structure corrections. There are three such corrections: spin-orbit coupling, the relativistic kinetic-energy correction, and the Darwin term. The kinetic-energy correction arises from the mass-energy relation \(E^2 = p^2 +m^2\); the Darwin term arises from interference between the electron and positron terms (which can also be understood as fluctuations of virtual electron-positron pairs); and spin-orbit coupling, as the name suggests, arises from electron spin, which has already been taken into account by the Pauli equation.   
>   
> Therefore, solving the Pauli equation for the hydrogen atom yields the spin-orbit coupling correction. However, it still does not yield the relativistic kinetic-energy correction or the Darwin term. To obtain all three fine-structure corrections simultaneously, quantum field theory and the Dirac equation are still required.   
>   
> In addition, there is another correction term of the same order of magnitude as the fine-structure corrections, called the Lamb shift, which arises from fluctuations of the electromagnetic field (virtual photons), rather than fluctuations of electron-positron pairs.

---

## III. Long-Wavelength Approximation and Dipole Representation  

We now consider the interaction between a light field and electrons in an atom. The first approximation we need to make is the **Born-Oppenheimer approximation**, namely decoupling the Hamiltonians of the atomic core and the electrons so that we need only consider the electronic Hamiltonian. This is because electrons move much faster than the atomic core, allowing us to regard the force on the core as an average force; conversely, we can regard electrons as moving in a fixed background Coulomb potential. Next, we make a series of further approximations.

### 3.1 Long-Wavelength Approximation (Dipole Approximation)  

Since the Bohr radius (~50 pm) is much smaller than optical wavelengths (~500 nm), we can neglect the gradient of the transverse component of the light field inside the atom. That is, in the Hamiltonian \(H=\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2 - e\phi  + H_\text{EM}\), we replace \(\mathbf{A}(\mathbf{x})\) with a field \(\mathbf{A}(\mathbf{0})\) that depends only on time. Here \(H_\text{EM}=\sum_{\mathbf{k,\sigma}} \omega_{\mathbf{k,\sigma}}\left(a_{\mathbf{k,\sigma}}^\dagger a_{\mathbf{k,\sigma}} + \frac{1}{2}\right)\) is the Hamiltonian of the transverse component of the light field.

Substituting \(\mathbf{x}=\mathbf{0}\) into

\[\mathbf{A}(\mathbf{x}) = \sum_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega_\mathbf{k}V}} \left[ a_{\mathbf{k},\sigma} \bm{\epsilon}_{\mathbf{k},\sigma} \mathrm{e}^{\mathrm{i}\mathbf{k}\cdot \mathbf{x}} + \text{h.c.} \right]\]

gives

\[\mathbf{A}(\mathbf{0}) = \sum_{\mathbf{k},\sigma} \frac{1}{\sqrt{2\omega_\mathbf{k}V}} \left(a_{\mathbf{k},\sigma} + a^\dagger_{\mathbf{k},\sigma}\right) \bm{\epsilon}_{\mathbf{k},\sigma} \]

This approximation is also called the dipole approximation, because it is equivalent to neglecting higher-order terms (quadrupoles, octupoles, and so on) in the multipole expansion.

### 3.2 Dipole Representation  

Define the dipole operator as \(\mathbf{d}=-e\mathbf{x}\) (\(e\) is positive, and \(\mathbf{x}\) is the position of the electron relative to the atomic nucleus), and perform the unitary transformation

\[\boxed{U=\exp\left[ -\mathrm{i}\mathbf{d}\cdot \mathbf{A}(\mathbf{0})\right]} = \exp\left[ \sum_{\mathbf{k},\sigma} (\lambda _{\mathbf{k,\sigma}} a_{\mathbf{k,\sigma}}^\dagger - \lambda_{\mathbf{k,\sigma}}^* a_{\mathbf{k,\sigma}} )\right] = \prod_{\mathbf{k,\sigma}} D_{\mathbf{k,\sigma}}(\lambda_{\mathbf{k,\sigma}})\]

where \(\lambda_{\mathbf{k,\sigma}} = -\mathrm{i}\mathbf{d}\cdot \epsilon_{\mathbf{k,\sigma}}\), and \(D_{\mathbf{k,\sigma}}(\alpha) = \exp( \alpha a^\dagger_{\mathbf{k,\sigma}} - \alpha a_{\mathbf{k,\sigma}})\) is the translation operator for the \(({\mathbf{k,\sigma}})\) mode.

It can be shown[[1]](#ref\_1) that the Hamiltonian in the new representation is:

\[\boxed{ H \mapsto U^\dagger H U = \frac{1}{2m}\mathbf{p}^2 - e\phi  +\mathbf{d}\cdot \mathbf{E}_\perp(\mathbf{0}) + H_\text{EM}+ H_{\text{dip}} } \quad (3)\]

where \( \mathbf{E}_\perp(\mathbf{0}) = \sum_{\mathbf{k,\sigma}} \mathrm{i} \sqrt{\frac{\omega_k}{2V}} (a_{\mathbf{k,\sigma}} - a^\dagger_{\mathbf{k,\sigma}}) \epsilon_{\mathbf{k,\sigma}}\) is the transverse component of the electric field, and \(H_{\text{dip}} = \sum_{\mathbf{k,\sigma}} \frac{1}{2V} (\epsilon_{\mathbf{k,\sigma}} \cdot \mathbf{d})^2\) is the dipole self-energy, which can usually be neglected.

This representation is called the \(\mathbf{d}\cdot\mathbf{E}\) representation, also known as the dipole representation. The original representation is called the \(\mathbf{p}\cdot \mathbf{A}\) representation.

### 3.3 Two-Level Approximation  

We now simplify the atom to a two-level system (with only a ground state and an excited state), namely by simplifying the atomic Hamiltonian \(\frac{1}{2m}\mathbf{p}^2 - e\phi\) to \(H_{\text{atom}} = \frac{\omega_{ab}}{2} \sigma_z\), where \(\omega_{ab}\) is the energy-level separation, \(\sigma_z = |b\rangle\langle b| - |a\rangle\langle a|\), \(|b\rangle\) is the excited state, and \(|a\rangle\) is the ground state.

Transitions between the two levels impose requirements on the polarization state of the light field (selection rules), so we need only consider the corresponding polarization state \(\sigma\). This allows us to write \(\mathbf{d} \cdot \mathbf{E}_{\perp}(\mathbf0)\) as \(dE_\perp(0)\).

In addition, the dipole operator must be projected into the two-level subspace: \(d\mapsto (|a\rangle\langle a| + |b\rangle\langle b| ) d = d_{ab}|a\rangle\langle b| + d_{ba} |b\rangle \langle a|\). Here \(d_{ba} = d_{ab}^*\).

> There is no \(d_{aa} |a\rangle \langle a|\) term because \(d_{aa} =-e \int \langle \psi_a|\mathbf{x}|\psi_a\rangle =-e\int\psi^*(\mathbf{x})\ \mathbf{x}\ \psi(\mathbf{x})\mathrm{d}^3\mathbf{x}= 0\). Similarly, there is no \(d_{bb}=0\).

We can always choose the phase \(d_{ab} \mapsto d_{ab}\mathrm{e}^{\mathrm{i}\theta}\) such that \(d_{ab} = d_{ba}\) is real. The dipole operator can then be written as:

\[\boxed{ d=d_{ab}(\sigma_+ +\sigma_-) }\]

where \(\sigma_+ = |b\rangle\langle a|,\ \sigma_-=|a\rangle\langle b|\).

The electric field operator can be written as:

\[E_\perp(\mathbf{0}) = \sum_{\mathbf{k}} \mathrm{i} \sqrt{\frac{\omega_k}{2V}} (a_{\mathbf{k}} - a^\dagger_{\mathbf{k}}) \]

We can absorb the imaginary factor \(\mathrm{i}\) into the annihilation/creation operators: \(a_{\mathbf{k}} \mapsto \mathrm{i}a_\mathbf{k}, \ a_{\mathbf{k}}^\dagger \mapsto -\mathrm{i}a_{\mathbf{k}}^\dagger\). Thus,

\[\boxed{ E_\perp(\mathbf{0}) = \sum_{\mathbf{k}} \sqrt{\frac{\omega_k}{2V}} (a_{\mathbf{k}} +a^\dagger_{\mathbf{k}})  }\]

Substituting these relations into the Hamiltonian \((3)\) in the dipole representation, and neglecting the dipole self-energy, gives:

\[\boxed{ H =  \frac{\omega_{ab}}{2} \sigma_z +\sum_{\mathbf{k}} g_{\mathbf{k}}(\sigma_+ +\sigma_-)(a_{\mathbf{k}} +a^\dagger_{\mathbf{k}}) + H_\text{EM} }\]

where \(g_{\mathbf{k}}=d_{ab}\sqrt{\frac{\omega_k}{2V}} \) is the coupling strength between the two-level system and the light field.

### 3.4 Cavity Quantum Electrodynamics (Cavity QED)  

Now consider placing the atom in a very small cavity. If the cavity length is \(\sim 100 \mu \text{m}\), then the free spectral range is \(c/(2L)\sim 1.5 \text{THz}\); that is, the frequency difference between adjacent modes is \(\sim 1.5 \text{THz}\), much greater than the natural linewidth \(\sim 10 \text{MHz}\) and coupling strength \(g\sim 100\text{MHz}\). This allows us to select a single light-field mode to interact with the two-level atom. The detunings \(\Delta =\omega_\mathbf{k}-\omega_{ab}\) of the other light-field modes are then large and can be neglected.

We thus obtain the interaction Hamiltonian between a single light field and a single electron in the atom:

\[\boxed{ H =  \frac{\omega_{ab}}{2} \sigma_z +g(\sigma_+ +\sigma_-)(a +a^\dagger) + \omega\left(a^\dagger a +\frac{1}{2}\right) }\]

where \(g = g_{\mathbf{k}}\) and \(\omega=\omega_\mathbf{k}\) are the coupling strength and frequency of the selected light field.

There is another advantage of the cavity: the coupling strength \(g_{\mathbf{k}}=d_{ab}\sqrt{\frac{\omega_k}{2V}} \) is relatively strong because the mode volume \(V\) is very small.

Since \(\sigma_+ a^\dagger\) represents creating a photon while the electron transitions from the lower energy level to the higher energy level, its probability is very low \(\sim\frac{1}{\omega+\omega_{ab}}\) and can be neglected. Similarly, \(\sigma_-a\) can also be neglected. This is called the rotating-wave approximation (RWA).

After making the rotating-wave approximation, we obtain the Jaynes-Cummings Hamiltonian:

\[\boxed{ H =  \frac{\omega_{ab}}{2} \sigma_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger)  }\]

The Jaynes-Cummings model has [analytic solutions](https://zhuanlan.zhihu.com/p/701838204), called dressed states. They will not be introduced here due to space limitations.

## Epilogue: The Charm of Physics  

We began with the QED Lagrangian:

\[\begin{aligned} \mathcal{L}=  \bar{\psi}(\mathrm{i}\gamma^\mu \partial_\mu -m)\psi - eA_\mu \bar{\psi} \gamma^\mu \psi -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} \end{aligned} \]

This Lagrangian is highly complex: it not only takes into account the electron's antiparticle—the positron—but the coupling term \(- eA_\mu \bar{\psi} \gamma^\mu \psi\) is also a cubic term, capable of describing various processes such as electron-positron pair creation/annihilation. The existence of the cubic term means that it has no analytic solution and can only be solved using perturbation theory in quantum field theory.

Yet after a series of simplifications and approximations (the low-energy approximation, the Born-Oppenheimer approximation, the long-wavelength/dipole approximation, the two-level approximation, and the rotating-wave approximation), we surprisingly obtain a model with an analytic solution!

\[H =  \frac{\omega_{ab}}{2} \sigma_z + \omega\left(a^\dagger a +\frac{1}{2}\right)+g(\sigma^+a + \sigma^-a^\dagger) \]

Clearly, according to the situation under consideration, we made a series of appropriate and necessary simplifications, thereby grasping the essence amid a vast array of complex phenomena and ultimately gaining a better understanding of the world.

This methodology can be applied not only in physics, but also generalized to other disciplines.

That is the charm of physics.

---

The [Higher and More Subtle Electrodynamics] series ends here. I hope you enjoyed this journey!

## Appendix  

Prove \((\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B}\), where \(\mathbf{D} = \nabla+ \mathrm{i}e\mathbf{A}\).

> Using the identity  
>   
> \((\bm\sigma \cdot \mathbf{a})(\bm\sigma \cdot \mathbf{b}) = \mathbf{a} \cdot \mathbf{b} + \mathrm{i}\bm\sigma \cdot(\mathbf{a}\times\mathbf{b})\)   
>   
> we obtain  
>   
> \((\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D})\)   
>   
> Thus, we need to calculate \((\mathbf{D}\times\mathbf{D})\).   
>   
> First, let us calculate \([D_i, D_j]\):   
>   
> \[\begin{aligned} [D_i, D_j] &= [\partial_i +\mathrm{i}eA_i, \partial_j +\mathrm{i}eA_j] \\ &= \cancel{[\partial_i,\partial_j]} + \cancel{e^2[A_i, A_j]} + \mathrm{i}e[\partial_i, A_j] - \mathrm{i}e[\partial_j,A_i] \end{aligned}\]   
>   
> Thus, we need to calculate \([\partial_i, A_j]\):  
>   
> \[\begin{aligned} [\partial_i, A_j] f &= \partial_i (A_j f) -A_j \partial_i f \\ &= (\partial_i A_j) f + A_j \partial_if - A_j \partial_i f \\ &= (\partial_iA_j)f \end{aligned}\]   
>   
> Therefore, \([\partial_i, A_j] = (\partial_i A_j)\).   
>   
> Hence  
>   
> \[\begin{aligned} [D_i, D_j] &= \mathrm{i}e[\partial_i, A_j] -\mathrm{i}e[\partial_j,A_i] \\ &= \mathrm{i}e (\partial_i A_j - \partial_j A_i) \\ &= \mathrm{i}e \epsilon_{ijk}B^k \end{aligned}\]   
>   
> Hence  
>   
> \(\begin{aligned} (\mathbf{D}\times\mathbf{D})^k &=\epsilon^{kij} D_i D_j \\ &= \frac{1}{2} \epsilon^{kij}[D_i,D_j] \\ &= \frac{\mathrm{i}e}{2} \epsilon^{kij} \epsilon_{ijl} B^l \\ &= \frac{\mathrm{i}e}{2} (\delta^k_l \delta^j_j - \delta^k_j\delta^j_l) B^l \\ &=\mathrm{i}e \delta^k_l B^l \\ &= \mathrm{i}eB^k \end{aligned}\)   
>   
> Therefore, \(\mathbf{D}\times \mathbf{D} = \mathrm{i}e\mathbf{B}\).   
>   
> Hence  
>   
> \(\begin{aligned} (\bm\sigma \cdot \mathbf{D})^2 &= \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D}) \\ &= \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B} \end{aligned}\)   
>   
> Q.E.D.

## References  

1. ^[a](#ref\_1\_0)[b](#ref\_1\_1)Atom-Photon Interactions by Cohen-Tannoudji [https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197](https://onlinelibrary.wiley.com/doi/book/10.1002/9783527617197)
