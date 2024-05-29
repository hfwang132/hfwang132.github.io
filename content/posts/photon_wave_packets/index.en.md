---
title: "What is the relationship between photons and electromagnetic field wave packets?"
date: 2024-04-13T16:10:38+08:00
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

### A wave packet can correspond to a photon
**Example**: A photon can be in a **coherent superposition** state of different frequencies: $|\psi\rangle=\sum\_{k}c\_k|k\rangle,\quad \sum\_k|c\_k|^2=1$, at which point the photon can behave as a wave packet.

You can imagine **an atom de-exciting and emitting a photon**, and this photon will indeed behave as a wave packet.


> Some may argue: excluding various non-ideal factors, the linewidth of this photon only depends on natural broadening (lifetime), making it look like a single frequency, thus poorly localized, and not considered a wave packet. Indeed so.   
> However, if we consider a single photon produced by a pulsed pump in a low-gain regime parametric process, its natural linewidth is very large. At this point, it is indeed in a coherent superposition state of different frequencies and behaves as a well-localized wave packet in the time domain.

**Definition of Single Photon State**

A state of the form $\sum\_{k}c\_k|0,\cdots,\underbrace{1}\_{k-\text{th}},\cdots,0\rangle$ is called a single photon state, where $|0,\cdots,\underbrace{1}\_{k-\text{th}},\cdots,0\rangle$ indicates one photon in the k-th mode, and $\sum\_{k}|c\_k|^2=1$.

Intuitively, coherently superimposing states with one photon in different modes still results in a single photon state.

### But a photon is not necessarily a wave packet
**Counterexample 1**: A photon passing through an NPBS (non-polarizing beam splitter) will travel two paths simultaneously: the transmitted path and the reflected path. At this point, the photon is non-localized.

**Counterexample 2**: A circularly polarized photon passing through a PBS (polarizing beam splitter) will travel two paths simultaneously: the transmitted path and the reflected path. At this point, the photon is non-localized. If the paths are considered a degree of freedom of the Hilbert space, the photon is in an entangled state of path and polarization.

**Counterexample 3**: A photon can also be two wave packets in the same path: using a PBS to split a photon into two paths, then using another PBS to recombine these two paths. If the optical paths are different, after recombining, the photon becomes two wave packets, one in front of the other.

**Counterexample 4**: A photon can even interfere with itself: first splitting the photon into two wave packets, then controlling the two paths to be nearly identical, and finally recombining the two wave packets. This is the Michelson/Mach-Zehnder interferometer at the single-photon level.

---

### More interesting photon states
The above three counterexamples are related to spatiotemporal modes and are well-known facts. Here are some other interesting states that might refresh your understanding of photons.

**Example 1**: Frequency superposition state

As mentioned above, a photon can be in a superposition state of different frequencies. More importantly, a photon can be two wave packets rather than one in the frequency domain. For example, a photon can be in a superposition state of wavelengths 1557nm and 1563nm. Such states can be prepared experimentally[[1]](#ref__1).

**Example 2**: Electric field superposition state (Schrödinger cat state)

In cases of very few photons, the electric and magnetic fields also have significant uncertainties (just like momentum and position). The electric and magnetic fields form a pair of canonical variables.

Experimentally, Schrödinger cat states can be prepared, where the electric field is in a superposition state of $|\alpha\rangle$ and $|-\alpha\rangle$. At this point, if you measure the electric field at a certain point (along the polarization direction), you might measure positive or negative values.

When the photon number is large, such states are fragile and quickly decohere into a statistical mixture of $|\alpha\rangle$ and $|-\alpha\rangle$.

However, at a low photon number level, such states can be prepared experimentally[[2]](#ref__2).

**Example 3**: Frequency entangled state

Two photons can be in a frequency entangled state: $|\psi\rangle=\frac{1}{2}(|\mu\rangle \otimes|\nu\rangle+|\nu\rangle \otimes|\mu\rangle)$. In short, if one photon is observed to have a wavelength of 1557nm, the other photon's wavelength will immediately collapse to 1663nm, and vice versa[[1]](#ref__1).

**Example 4**: Number entangled state

Experimentally, NOON states can be prepared: $|\psi\rangle=\frac{1}{2}(|N,0\rangle + |0,N\rangle)$, meaning if one mode has N photons, the other mode has none, and vice versa. There can only be 0 or N, not other numbers.

These two modes can be spatial modes. You can imagine a group of photons being in a superposition state of all going left and all going right. If you detect N photons on one side, you immediately know there are no photons on the other side, and vice versa.

Of course, when the photon number is large, such states are quite fragile, making it difficult to maintain a stable phase relationship among all the photons.

---

In summary, photons have many degrees of freedom. Any degree of freedom you can think of can be superimposed and entangled. The three difficulties at high photon numbers are preparation, decoherence, and characterization (state tomography).

A photon can be a wave packet, but it doesn't have to be; a wave packet can be a photon, but it doesn't have to be. The key is to understand coherent superposition in quantum mechanics: $\sum\_{k}c\_k|0,\cdots,\underbrace{1}\_{k-\text{th}},\cdots,0\rangle$.

## References
1. ^[a](#ref__1__0)[b](#ref__1__1)Shukhin, A., Hurvitz, I., Trajtenberg-Mills, S., Arie, A. & Eisenberg, H. Two-dimensional Control of a Biphoton Joint Spectrum. Preprint at http://arxiv.org/abs/2311.09660 (2023).
2. [^](#ref__2__0)Lvovsky, A. I. et al. Production and applications of non-Gaussian quantum states of light. Preprint at http://arxiv.org/abs/2006.16985 (2020).

