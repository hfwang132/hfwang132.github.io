---
title: "A simple quantum description of lasers"
date: 2024-05-27T17:42:31+08:00
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

This article aims to derive the coherent state of a laser from basic quantum dynamics.

Consider the interaction between a two-level system and a single-mode light field, where the frequency of the light field equals the energy level difference.

The two-level system initially starts in the excited state $|e\rangle$, and the light field is in the vacuum state $|0\rangle$.

According to the Jaynes-Cummings model, even if the light field is in the vacuum state, spontaneous emission will occur. After a short period, the quantum state evolves from $|e,0\rangle$ to:

$|\psi\rangle = a |e,0\rangle + b |g,1\rangle$

where $|g,1\rangle$ represents the two-level system in the ground state, and the coupled light field mode contains one photon, which is the spontaneously emitted photon.

Now consider $N$ two-level systems in the excited state, which are not coupled with each other but only with the light field. The initial spontaneously emitted photon induces stimulated emission in other two-level systems, so the overall quantum state can be written as:

$|\Psi\rangle = C|\psi\rangle^{\otimes N} =  C\sum_k \sum_m\mathcal{P}_m[|e,0\rangle^{\otimes (N-k)} \otimes |g,1\rangle^{\otimes k}]$

where $C$ is a normalization constant to be determined, and $\mathcal{P}_m$ denotes all possible permutations of $|e,0\rangle^{\otimes (N-k)} \otimes |g,1\rangle^{\otimes k}$, with a total of $\frac{N!}{(N-k)!\,k!}$ permutations. Note that we have not yet used the Fock space (i.e., we haven't symmetrized for identical bosons).

> This step is quite informal, and possibly incorrect, because it doesn't explain why stimulated emission means that the overall quantum state is the tensor product of the spontaneous emission state $|\psi\rangle = a |e,0\rangle + b |g,1\rangle$. However, we will see later that it gives the correct result. Therefore, this derivation must contain some insight that I haven't yet identified.

The quantum state of the light field is obtained by tracing out the quantum state of the two-level systems:

$\rho = \operatorname{Tr}_{\text{a}}[|\Psi\rangle\langle\Psi|] = C^2 \sum_k |a^{N-k}b^k|^2 \sum_m\mathcal{P}_m[(|0\rangle\langle 0|)^{\otimes (N-k)} \otimes (|1\rangle\langle 1|)^{\otimes k}]$

Now we symmetrize the tensor product of identical particles and map it to Fock space, which is well-known as $|1\rangle ^{\otimes k} \rightarrow \sqrt{k!} |k\rangle$, so the above equation becomes

$\rho = C^2 \sum_k |a^{N-k}b^k|^2 \left(\frac{N!}{(N-k)!\,k!}\right)^2 k! |k\rangle\langle k|$

When $k \ll N$, $\frac{N!}{(N-k)!} \sim \left(\frac{N}{e}\right)^k$. Let $\alpha = \frac{b}{a} \cdot \frac{N}{e}$, then the above equation can be written as:

$\rho = C^2 a^N \sum_k \frac{|\alpha|^{2k}}{k!} |k\rangle\langle k|$

Normalizing it, we get:

$\rho = e^{-|\alpha|^2} \sum_k \frac{|\alpha|^{2k}}{k!} |k\rangle\langle k|$

This is a Poisson distribution with an average particle number of $|\alpha|^2$. In the coherent state representation, it can be written as:

$\rho = \int_0^{2\pi} \frac{\mathrm{d}\theta}{2\pi} |\alpha e^{\mathrm{i}\theta}\rangle \langle \alpha e^{\mathrm{i}\theta}|$

It is thus a phase-randomized coherent state. The coherent state $|\alpha\rangle$ corresponds to a classical electromagnetic wave with very well-defined amplitude and phase, but here its phase is integrated from $0$ to $2\pi$. This represents our ignorance of the phase information, which fundamentally comes from our ignorance of the microscopic state of the two-level systems (the gain medium). Therefore, this $\rho = \rho_{\text{epistemic}}$ is an epistemic quantum state.

From the perspective of an ontic quantum state, the quantum state of the system should collapse to a state with a definite phase $\rho_{\text{ontic}} = |\alpha\rangle$, but we cannot know which phase it is. This is because, at optical frequencies $\sim 10^{15} \text{Hz}$, humans cannot observe the absolute phase. However, relative phase can be observed, so we can still observe interference phenomena. If the reader is curious about this, they can read further in this article [[1]](#ref_1).

## References
1. Bartlett, S. D., Rudolph, T. & Spekkens, R. W. Dialogue Concerning Two Views on Quantum Coherence: Factist and Fictionist. Int. J. Quantum Inform. 04, 17–43 (2006).
