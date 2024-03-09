---
title: "Probing g2 with non-photon-number-resolving detectors"
date: 2024-03-10T02:22:26+08:00
draft: false
tags: ["Quantum Optics"]
categories: ["Quantum Information"]
---

## HBT Experiment
Those who have conducted quantum optics experiments must be familiar with the Hanbury Brown and Twiss (HBT) experiment, which can be used to measure the second-order correlation function g2. In this experiment, a beam of light is split into two using a 50:50 beamsplitter, and then each beam is detected separately by two detectors. The correlation of the intensities on both sides is measured as a function of delay, as shown in the figure below:

{{< figure src="image/HBT_g2.png" title="Hanbury Brown and Twiss Experiment  " >}}

The classical normalized g2 is defined as:

$\begin{aligned} g^{(2)}(r\_1, r\_2; \tau) &= \frac{\langle E^\*(r\_1, t) E^\*(r\_2, t + \tau) E(r\_2, t + \tau) E(r\_1, t) \rangle}{\langle |E(r\_1, t)|^2 \rangle \langle |E(r\_2, t + \tau)|^2 \rangle} \\\\ &= \frac{\langle I(r\_1, t) I(r\_2, t + \tau) \rangle}{\langle I(r\_1, t) \rangle \langle I(r\_2, t + \tau) \rangle} \end{aligned}$

where $E$ represents the electric field and $I$ represents the intensity. As per the definition, the HBT experiment measures the classical g2 by normalizing the correlated intensities with the product of the individual intensities.

## Quantum Second-Order Correlation Function
The definition of the quantum normalized g2 is:

$\begin{aligned} g^{(2)}(r\_1, r\_2; \tau) &= \frac{\langle E^-(r\_1, t) E^-(r\_2, t + \tau) E^+(r\_2, t + \tau) E^+(r\_1, t) \rangle}{\langle E^-(r\_1, t) E^+(r\_1, t) \rangle \langle E^-(r\_2, t + \tau) E^+(r\_2, t + \tau) \rangle} \end{aligned}$

In the quantum case, the operators in the numerator should be replaced with the counter-rotating term $E^-$ and the co-rotating term $E^+$, which involve creation and annihilation operators. Additionally, the creation operator must precede the annihilation operator since the detection of a photon is an annihilation process, unlike the classical case. In classical coherent states $|\alpha\rangle$, the annihilation operator $a$ is an eigenstate $a|\alpha\rangle = \alpha|\alpha\rangle$, hence the presence or absence of a photon makes no difference.

In the case of **single-mode**, since $E^+ = i\sqrt{\frac{\hbar \omega}{2\epsilon\_0 V}}a$ and $E^- = i\sqrt{\frac{\hbar \omega}{2\epsilon\_0 V}}a^\dagger$, the quantum g2 can be simplified to:

$\begin{aligned} g^{(2)}(r\_1, r\_2, \tau) &= \frac{\langle a^\dagger(r\_1, t) a^\dagger(r\_2, t + \tau) a(r\_2, t + \tau) a(r\_1, t) \rangle}{\langle n(r\_1, t) \rangle \langle n(r\_2, t + \tau) \rangle} \end{aligned}$

Therefore, to measure quantum g2, we need to replace intensity detectors with photon detectors, **and these photon detectors should be capable of distinguishing photon numbers**.

However, the problem arises because currently available single-photon detectors that can distinguish photon numbers are not very practical: TES detectors have long recovery times; schemes for Demultiplexing in space and time only offer pseudo-photon number resolution; and SNSPDs are expensive, require low temperatures, and their multi-photon efficiency may not be very high.

## NPNR-SPD for Measuring g2
Fortunately, single-photon detectors that cannot distinguish photon numbers (NPNR-SPDs, Non-Photon-Number-Resolving Single-Photon-Detectors) can still measure g2, even though they cannot resolve photon numbers!

> Comment: "Cannot distinguish photon numbers" means they can only differentiate between "no photons" and "one or more photons." Common APD detectors cannot distinguish photon numbers.

The method is simple: just make sure the quantum efficiency of the NPNR-SPD is low enough!

> Quantum efficiency $\eta$ refers to the probability that the detector can detect a photon given that a photon enters it. Conversely, the probability of the photon being "lost" is $1 - \eta$.

At first, it seemed strange to me why lower efficiency is better. But with a little thought, the principle becomes clear:

When the efficiency is low enough, the probability that $k$ photons are not all lost is $1 - (1 - \eta)^k \approx k\eta$. In other words, the probability of the NPNR-SPD detecting a photon is proportional to $k$. Thus, we achieve "photon number resolution" indirectly through "low efficiency".

> The following is a formal (boring) mathematical derivation, which can be skipped:
> [Derivation equations]

Measuring g2 has several uses. Besides the common textbook distinctions of [super-Poissonian statistics/Poissonian statistics/sub-Poissonian statistics] and [photon bunching/antibunching], there is an unexpected application: measuring spectral correlations of photons, which we will discuss in the next part.

## Conclusion: Multi-Mode Scenario
Previously, we assumed that the detected light was single-mode. Hence $E^+$ could be proportional to $a$: $E^+ = i\sqrt{\frac{\hbar \omega}{2\epsilon\_0 V}}a$.

But what if the detected light is multi-mode? In this case, $E^+ = i\sum\_k\sqrt{\frac{\hbar \omega\_k}{2\epsilon\_0 V}}a\_k$, $E^+$ is no longer proportional to $a$, but has a frequency dependence: $E^+\_k \propto \sqrt{\omega\_k}a\_k$.

> The additional term $\sqrt{\omega\_k}$ in the equation is not surprising since the intensity, which is proportional to the frequency times the number of photons, contributes to it.

However, as long as the frequencies of the various modes are the same, we can still eliminate $\sqrt{\omega\_k}$, and obtain:

$\begin{aligned} g^{(2)}(0) = \frac{\langle n(n-1) \rangle}{\langle n \rangle^2} \end{aligned}$

Thus, even if multiple modes are present, if these modes have (approximately) the same frequency, the method of measuring quantum g2 using the HBT experiment remains effective.
