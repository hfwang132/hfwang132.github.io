---
title: "POVM: a brief introduction"
date: 2024-03-10T02:22:12+08:00
draft: false
tags: ["Quantum Measurement Theory"]
categories: ["Quantum Information"]
---

# Projection Measurement

Traditionally, a measurement, in the sense of Von Neumann, is a series of projection operators. By performing spectral decomposition on the self-adjoint operator corresponding to the observable, denoted as $ O = \sum\_i \lambda\_i |\varphi\_i\rangle\langle\varphi\_i| $, we obtain these projection operators $ |\varphi\_i\rangle\langle\varphi\_i| $. This part is well-known to students who have studied elementary quantum mechanics.

Besides the Von Neumann measurement, there is a more general type of measurement called Generalized Measurements or Positive Operator Valued Measures (POVMs).

# Generalized Measurements (POVMs)

> Definition: POVM
> 
> A POVM is a mapping $ \mathsf{E}: X \rightarrow \mathcal{L}(\mathcal{H}) $, satisfying
> 
> $ \mathsf{E}(x) \ge 0, \quad \forall x \in X $
> $ \sum\_ {x \in X} \mathsf{E}(x) = \mathbb{I}\_{\mathcal{H}} $
> where $ X $ represents the set of possible measurement outcomes, and $ \mathcal{L}(\mathcal{H}) $ represents the set of all bounded operators on $ \mathcal{H} $.
> Born's Rule
> 
> The probability of obtaining result $ x $ when measuring a quantum state $ \rho $ with a POVM $ \mathsf{E} $ is given by $ p\_{\rho}^{\mathsf{E}}(x) = \operatorname{tr}[\rho \mathsf{E}(x)] $.

When I first encountered POVMs, I was not clear about how they are implemented. This is because traditional measurements involve projection operators satisfying $ \mathsf{E}(x)^2 = \mathsf{E}(x), \quad \forall x \in X $. However, general POVMs do not satisfy this condition.

In fact, traditional projection measurements, also known as PVMs (Projection Valued Measures), are a special type of POVM.

PVMs are to POVMs what pure states are to mixed states. In other words, a POVM is a statistical mixture of PVMs, just as a mixed state is a statistical mixture of pure states.

# Implementing POVMs

So, how do we implement POVMs? We can actually use PVMs and composite systems to implement POVMs.

Consider a system with a Hilbert space $ \mathcal{H} $ and a state $ \rho $.

Next, we couple system $ \mathcal{H} $ with another system $ \mathcal{K} $. Suppose the initial state of system $ \mathcal{K} $ is $ \sigma $. Then, the initial state of the composite system is $ \rho \otimes \sigma $ in $ \mathcal{H} \otimes \mathcal{K} $.

After that, we let the composite system evolve for a period of time, resulting in the system's state becoming $ U(\rho \otimes \sigma) U^\dag $.

Finally, we perform a PVM $ \mathsf{Z} $ measurement on subsystem $ \mathcal{K} $. According to Born's rule, the probability of obtaining result $ x $ is $ \operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z}(x))] $.

Thus, we have implemented a POVM $ \mathsf{E} $ such that $ \operatorname{tr}[\rho \mathsf{E}(x)] = \operatorname{tr}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z}(x))] $.

# Measurement Model

Let's summarize the physical objects involved in implementing POVMs: the ancilla system $ \mathcal{K} $, the initial state $ \sigma $ of system $ \mathcal{K} $, the evolution $ U $ of the composite system, and the projection measurement $ \mathsf{Z} $ on the ancilla system. These physical objects together realize a POVM measurement.

So, we can define $ \mathfrak{M} = (\mathcal{K},\sigma,U,\mathsf{Z}) $ as a Measurement Model.

In actual experiments, the ancilla system $ \mathcal{K} $ can be considered as a probe of the instrument, and $ \mathsf{Z} $ is the readout of the probe.

Post-Measurement State
POVMs themselves cannot determine the post-measurement state. The actual determination of the post-measurement state depends on the specific implementation of the measurement, that is, the measurement model.

For a measurement model $ \mathfrak{M} = (\mathcal{K},\sigma,U,\mathsf{Z}) $, the post-measurement state of system $ \mathcal{H} $ is $ \rho\_x = \operatorname{tr}\_{\mathcal{K}}[U(\rho\otimes \sigma) U^\dag(\mathbb{I}\_{\mathcal{H}}\otimes \mathsf{Z}(x))] $, where $ \operatorname{tr}\_{\mathcal{K}}[\cdot] $ denotes the partial trace.

# Quantum Instruments

POVMs provide probabilities for each measurement outcome but do not determine the post-measurement state. Therefore, we aim to find a mathematical object that includes both the measurement probabilities and the post-measurement states. This mathematical object is called a Quantum Instrument.

> Definition: Quantum Instrument
> 
> An operator $ \mathcal{I}\_x: \mathcal{I}\_x(\rho) = \rho\_x $ is called a Quantum Instrument if $ \operatorname{tr}\left[\sum\_{x\in X} \rho\_x \right] = \operatorname{tr}[\rho] = 1 $.

It can be seen that $ \mathcal{I}\_x $ not only provides the measurement probability $ p\_x = \operatorname{tr}[\rho\_x] $, but also gives the post-measurement state $ \frac{\rho\_x}{\operatorname{tr}[\rho\_x]} $.

Obviously, the same POVM corresponds to countless Quantum Instruments.

So, for any Quantum Instrument, can we always implement it? The answer is yes.

> Theorem
> 
> Given any Quantum Instrument, we can always find a Measurement Model to implement it (in fact, there are countless implementations). Proof omitted.