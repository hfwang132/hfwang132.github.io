---
title: "Highly Useful Formulas"
date: 2022-01-01T19:21:09+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/452415452"
author: "Haifei"
tags: ["Mathematical Formulas"]
categories: ["Mathematical Physics Methods"]
---

The following formulas can make problem solving much more convenient.

### I. Gaussian Integrals  

\[I_n = \int_{0}^{\infty}x^n e^{-b x^2}\mathrm{d}x  %=  %\left\{\begin{aligned}  %\end{aligned}\right. \]

Here is a convenient way to remember it:

First, remember

\[I_0 = \frac{1}{2}\sqrt{\frac{\pi}{b}},\quad I_1 = \frac{1}{2}\frac{1}{b}\]

Next,

\[I_{n+2}=\frac{n+1}{2b}I_n\]

This formula applies to both odd and even cases of \(n\).

If you are dealing with Gaussian functions (for example, in probability theory), then this integral will appear very frequently!

### II. Powers of Trigonometric Functions  

\[I_n=\int_{0}^{\frac{\pi}{2}}\sin^{n}x\mathrm{d}x = \int_{0}^{\frac{\pi}{2}}\cos^{n}x\mathrm{d}x\]

The following expression gives \(I_n\)

\[I_n =  \left\{\begin{aligned} &\frac{(n-1)!!}{n!!}&, \quad n \text{ is odd} \\ &\frac{(n-1)!!}{n!!}\frac{\pi}{2}&, \quad n \text{ is even} \end{aligned}\right.\]

This formula is very useful when integrating \(\theta,\,\varphi\) in spherical coordinates!

### III. The Laplace Transform of x^n  

\[I_n=\int_{0}^{\infty}x^n\mathrm{e}^{-kx}\mathrm{d}x\]

The following expression gives \(I_n\):

\[I_n=\frac{n!}{k^{n+1}}\]

This formula is useful when integrating \(r\) in spherical coordinates (if you are dealing with terms containing \(\mathrm{e}^{kr}\))

### IV. A Shortcut for Integration by Parts  

\[I=\int_{a}^{b} u(x)v(x)\mathrm{d}x\]

The diagram for the shortcut is as follows:

\[\begin{alignedat}{6} & u(x) &  \quad & u^{(1)}(x) & \quad & u^{(2)}(x) & \quad & u^{(3)}(x) &  \quad & \cdots \\ & & \searrow^{+} & & \searrow^{-} & & \searrow^{+} & & \searrow^{-} \\ & v(x) & \quad & v^{(-1)}(x) & \quad & v^{(-2)}(x) & \quad & v^{(-3)}(x) & \quad & \cdots & & \end{alignedat}\]

Here, \(u^{(n)}(x)\) denotes the \(n\)th derivative of \(u(x)\), and \(v^{(-n)}(x)\) denotes the \(n\)th indefinite integral of \(v(x)\).

In other words,

\[\begin{aligned} I&=\int_{a}^{b} u(x)v(x)\mathrm{d}x  \\&= \left.u(x)v^{(-1)}(x)\right|^{b}_{a} - \left.u^{(1)}(x)v^{(-2)}(x)\right|^{b}_{a}+\left.u^{(2)}(x)v^{(-3)}(x)\right|_{a}^{b} - \cdots \end{aligned}\]

This process continues until \(u^{(n)}(x)=0\).

> Or, you may also stop manually at a certain point, for example  
>  \(\begin{aligned} I&=\int_{a}^{b} u(x)v(x)\mathrm{d}x  \\&= \left.u(x)v^{(-1)}(x)\right|^{b}_{a} - \left.u^{(1)}(x)v^{(-2)}(x)\right|^{b}_{a}+\int_{a}^{b}u^{(2)}(x)v^{(-2)}(x)\mathrm{d}x \end{aligned}\)   
> In this case, you want \(\int_{a}^{b}u^{(2)}(x)v^{(-2)}(x)\mathrm{d}x\) to contain \(I\), so that you can rearrange the terms to solve for \(I\)

### V. Differential Operators in Spherical Coordinates  

In orthogonal curvilinear coordinates, we have

\[\nabla = \frac{\bm{e}_{1}}{h_1}\frac{\partial}{\partial q_1}+\frac{\bm{e}_{2}}{h_2}\frac{\partial}{\partial q_2}+\frac{\bm{e}_{3}}{h_3}\frac{\partial}{\partial q_3}\]

\[\nabla \cdot \mathbf{A} = \frac{1}{h_1h_2h_3}\left[\frac{\partial}{\partial q_1}(A_1h_2h_3)+\frac{\partial}{\partial q_2}(h_1A_2h_3)+\frac{\partial}{\partial q_3}(h_1h_2A_3)\right]\]

\[\nabla\times\mathbf{A}=\frac{1}{h_1h_2h_3}\begin{vmatrix} h_1\bm{e_1} & h_2\bm{e_2} & h_3\bm{e_3} \\ \frac{\partial}{\partial q_1} & \frac{\partial}{\partial q_2} & \frac{\partial}{\partial q_3} \\ h_1A_1 & h_2A_2 & h_3A_3 \end{vmatrix}\]

\[\begin{aligned} \nabla^2u&=\nabla\cdot(\nabla u)\\&= \frac{1}{h_1h_2h_3}\left[\frac{\partial}{\partial q_1}\left(\frac{h_2h_3}{h_1}\frac{\partial}{\partial q_1}\right) + \frac{\partial}{\partial q_2}\left(\frac{h_1h_3}{h_2}\frac{\partial}{\partial q_2}\right) + \frac{\partial}{\partial q_3}\left(\frac{h_1h_2}{h_3}\frac{\partial }{\partial q_3}\right) \right]u \end{aligned}\]

Substituting

\[\begin{matrix} h_1 \rightarrow 1 &  h_2 \rightarrow r & h_3 \rightarrow r\sin\theta \\ \bm{e}_1 \rightarrow \bm{\widehat{r}} & \bm{e}_2 \rightarrow \bm{\widehat{\theta}} & \bm{e}_3 \rightarrow \bm{\widehat{\varphi}} \end{matrix}\]

gives the formulas in spherical coordinates.

In fact, \(h_1,\,h_2,\,h_3\) are called the Lamé coefficients.

With this trick, you can derive PDEs in spherical coordinates from scratch during an exam.

### VI. The Exponential of a Matrix  

Actually, this is easy to derive... it is included here just to round out the list:

\[\exp\left(t\begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}\right) =\begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{bmatrix}\]

\[\exp\left(t\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\right) =\begin{bmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{bmatrix}\]
