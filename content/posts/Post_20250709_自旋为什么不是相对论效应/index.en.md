---
title: "Why Spin Is Not a Relativistic Effect"
date: 2025-07-09T19:23:54+08:00
originalURL: "https://www.zhihu.com/question/457103119/answer/1926360925780312832"
aliases:
  - "/en/spin_and_relativity/"
  - "/en/Post_20251012_自旋为什么不是相对论效应/"
draft: draft
tags: ["spin", "relativity"]
categories: ["Mathematical Methods of Physics"]
author: "Haifei"
---

Conclusion: integer spin is a classical effect, whereas half-integer spin is a quantum effect and has little to do with relativity.

The reason is simple: spin-1 is the smallest faithful representation of SO(3), while spin-1/2 is the smallest faithful representation of SU(2).

So why can quantum mechanics lift SO(3) to SU(2)? Because quantum states are rays and are equivalent up to a global phase. In other words, quantum mechanics requires projective representations of SO(3). And projective representations of SO(3) are in one-to-one correspondence with representations of SU(2) (Bargmann's theorem). This is why quantum mechanics considers SU(2) rather than SO(3).

Put more simply, quantum mechanics is insensitive to global phase, so after a 360-degree rotation there may be a phase difference; for spin-1/2, this phase is pi.

Surely someone will ask: why can it only be $\pi$, rather than $\pi/2$? Wouldn't that give us spin-1/4? Good question. This is a limitation of three-dimensional space. In two-dimensional space (SO(2)), no such limitation exists, and arbitrary spin is allowed. These are the so-called anyons, which form the basis of topological quantum computing.

As for relativity, my personal view is that it has absolutely nothing to do with half-integer spin. After all, nonrelativistic quantum mechanics likewise permits half-integer spin.

Some may say that the Dirac equation predicted spin-1/2, so half-integer spin is a relativistic effect. But the Dirac equation was not the only theory to predict spin-1/2; it was not even the first. Long before the Dirac equation, there was already much evidence for half-integer spin: the Stern-Gerlach experiment, the Zeeman effect, and so on... On the theoretical side, the Pauli equation can also perfectly describe nonrelativistic spin-1/2.

---

Some say that integer spin is also quantum. That depends on how you define spin. My understanding is that for a purely classical field, such as the electromagnetic field $A_{\mu}$, we can likewise discuss spin. Of course, if you quantize it and the field can excite particles, then integer spin undoubtedly also has quantum properties—but that quantumness was already contained in your premise, making it equivalent to a tautological piece of nonsense.

---

Others say that nonrelativistic quantum mechanics merely **permits** the existence of spin-1/2, whereas relativistic quantum mechanics **requires** spin-1/2 to necessarily exist. The reason is still the same classic argument: if we require the field equation to be first-order, then we obtain the Dirac equation, and the Dirac equation requires spin-1/2.

This too is a well-known myth. In fact, simply modifying the algebra satisfied by the gamma matrices in the Dirac equation yields the first-order DKP equation, which describes spin-0 and spin-1.

Moreover, Dirac's motivation was that in the Schrödinger equation the spatial part is second-order while the time part is first-order, so they are different, and thus he made the spatial part first-order. But it is equally possible for me to make the time part second-order as well, yielding the Klein-Gordan and Proca equations describing spin 0 and 1. In any case, second-order equations can always be reduced to first-order form, and after doing so one obtains DKP.

Some may think that relativistic quantum mechanics (that is, quantum field theory) consists entirely of the Dirac equation. In fact, quantum field theory uses KG/Proca/Maxwell just as much as it uses Dirac. The Dirac equation is usually taught first simply because the electron is important, and Dirac + Maxwell is sufficient to describe quantum electrodynamics.

If there were no spin-1/2 particles in the world, then relativistic quantum mechanics, like nonrelativistic quantum mechanics, could still remain self-consistent. It would merely be a matter of modifying the Lagrangian; after all, the Standard Model Lagrangian is already a mess. A mathematical prediction does not mean something must exist; there are plenty of things predicted mathematically that do not exist, and plenty of mathematically self-consistent models that do not describe the real world. Physics is an experimental discipline.

---

In one sentence: the DKP equation of relativistic quantum mechanics (which, like the Dirac equation, is first-order and satisfies the mass-energy relation) can describe spinless particles, so relativistic quantum mechanics does not necessarily require the existence of spin.

**What does “necessarily” mean here? It means that if spin did not exist, relativistic quantum mechanics would collapse. Clearly, that is not actually the case.**
