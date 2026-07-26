---
title: "Understanding the Invariance of Differential Forms"
date: 2021-02-16T14:23:58+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/350936061"
author: "Haifei"
tags: ["Differential Geometry"]
categories: ["Mathematical Methods in Physics"]
---

21/03/2025: Major revision of this article

## What Is the Invariance of Differential Forms?  

According to textbooks, the invariance of differential forms means that, under a change of variables, the form of a differential equation remains unchanged. That is:

> If, when \(\mathrm{d}y\) in \(y\) denotes the function \(y=f(x)\) and \(\mathrm{d}x\) in \(x\) denotes the function \(\phi(x)=x\), \(\mathrm{d}y=a\mathrm{d}x\) holds, that is, \(\mathrm{d}f=a\mathrm{d}\phi\) holds,   
>   
> then, when \(\mathrm{d}y\) in \(y\) denotes the function \(y=g(t)\) and \(\mathrm{d}x\) in \(x\) denotes the function \(x=\varphi(t)\), \(\mathrm{d}y=a\mathrm{d}x\) likewise holds, that is, \(\mathrm{d}g=a\mathrm{d}\varphi\) holds.   
>   
>  \(\mathrm{d}f=a\mathrm{d}\phi\) and \(\mathrm{d}g=a\mathrm{d}\varphi\) are two different equations, but both can be written as \(\mathrm{d}y=a\mathrm{d}x\). This is the invariance of differential forms.

But is it really necessary to make things so convoluted?

In fact, from a higher-level perspective, the so-called invariance of differential forms is self-evident.

Consider a differentiable function \(y: M \rightarrow \mathbb{R}\) on the one-dimensional manifold \(M\). Its differential is a cotangent vector field on the manifold, or a 1-form: \(\mathrm{d}y: \mathcal{T}^1_0(M) \rightarrow \mathcal{F}(M)\), where \(\mathcal{T}_0^1(M)\) denotes the set of all differentiable tangent vector fields on \(M\), and \(\mathcal{F}\) denotes the set of all differentiable functions on \(M\).

Let us assign two coordinate systems \(x: M \rightarrow \mathbb{R}^1\) and \(t: M\rightarrow \mathbb{R}^1\) to \(M\), respectively. The coordinate systems themselves are also functions on \(M\).

The validity of \(\mathrm{d} y = a \mathrm{d} x\) (where \(a\) is a function on \(M\)) does not depend on any coordinate system. This is because \(\mathrm{d}y\) depends only on \(y\), and \(\mathrm{d}x\) depends only on \(x\). In other words, whether you regard \(y\) and \(x\) as functions of \(x\) or as functions of \(t\) does not affect the validity of the expression \(\mathrm{d} y = a \mathrm{d} x\).

In differential geometry, \(y\) and \(x\) are both differentiable functions on \(M\), and their existence does not depend on any coordinate system. Therefore, the existence of \(\mathrm{d}y\) and \(\mathrm{d}x\) likewise does not depend on any coordinate system. Like a statue, no matter from which angle you view it, none of its properties are affected.

Thus, we may interpret the “invariance of differential forms” as “\(\mathrm{d}f\) depends only on \(f\) and not on the coordinate system.”

## What Is the Difference Between Partial Derivatives and Differentials?  

Partial derivatives and differentials are very different. Computing a partial derivative requires specifying a coordinate system; without a coordinate system, one cannot compute a partial derivative. When the coordinate system changes, the partial derivatives change accordingly. More critically, even if \(x_1\) does not change, \(\frac{\partial f}{\partial x_1}\) changes as long as \(x_2,\cdots,x_n\) changes. Clearly, if we study only partial derivatives, we become lost in coordinate transformations and cannot abstract to a higher level.

Why do we study not only derivatives but also differentials? This is the reason: differentials do not depend on coordinate systems, or in other words, they are canonical.

## What Is the Use of the Invariance of Differential Forms?  

The most direct application is proving the chain rule:

> Substituting \(\mathrm{d}x =\frac{\partial x}{\partial t} \mathrm{d}t\) into \(\mathrm{d}y = \frac{\partial y}{\partial x} \mathrm{d}x\) gives   
>   
>  \(\mathrm{d}y = \frac{\partial y}{\partial x} \mathrm{d}x = \frac{\partial y}{\partial x}\frac{\partial x}{\partial t} \mathrm{d}t\)

In this simple proof, we used the “method of substitution.”

In fact, this is a false proof. In reality, the chain rule came first, and only then came the invariance of differential forms.

Using the “method of substitution,” we can also prove many useful formulas. Here is an example:

### Exercise 1  

(Thermodynamics) Given \(\mathrm{d}E=T\mathrm{d}S-p\mathrm{d}V\), that is, \(\left.\left(\frac{\partial E}{\partial S}\right)\right|_V=T,\,\left.\left(\frac{\partial E}{\partial V}\right)\right|_S=-p\), find \(\left.\left(\frac{\partial E}{\partial T}\right)\right|_V,\,\left.\left(\frac{\partial E}{\partial V}\right)\right|_T\)

> Solution: Substituting \(\mathrm{d}S=\left.\left(\frac{\partial S}{\partial T}\right)\right|_V\mathrm{d}T+\left.\left(\frac{\partial S}{\partial V}\right)\right|_T\mathrm{d}V\) into \(\mathrm{d}E=T\mathrm{d}S-p\mathrm{d}V\) gives   
>   
> \(\begin{aligned} \mathrm{d}E&=T\mathrm{d}S-p\mathrm{d}V \\ &=T\left[\left.\left(\frac{\partial S}{\partial T}\right)\right|_V\mathrm{d}T+\left.\left(\frac{\partial S}{\partial V}\right)\right|_T\mathrm{d}V\right]-p\mathrm{d}V \\ &=T\left.\left(\frac{\partial S}{\partial T}\right)\right|_V\mathrm{d}T+\left[\left.T\left(\frac{\partial S}{\partial V}\right)\right|_T-p\right]\mathrm{d}V \end{aligned}\)   
>   
> Therefore \(\left.\left(\frac{\partial E}{\partial T}\right)\right|_V=T\left.\left(\frac{\partial S}{\partial T}\right)\right|_V,\) \(\left.\left(\frac{\partial E}{\partial V}\right)\right|_T=T\left.\left(\frac{\partial S}{\partial V}\right)\right|_T-p\)

Not only can we prove formulas through “substitution”; we can also prove formulas through simple “transposition.” Here are some examples:

### Exercise 2  

(Thermodynamics) Given \(\mathrm{d}E=T\mathrm{d}S-p\mathrm{d}V\), that is, \(\left.\left(\frac{\partial E}{\partial S}\right)\right|_V=T,\,\left.\left(\frac{\partial E}{\partial V}\right)\right|_S=-p\), find \(\left.\left(\frac{\partial S}{\partial V}\right)\right|_E\)

> Solution: Transposing terms in \(\mathrm{d}E=T\mathrm{d}S-p\mathrm{d}V \) gives \(\mathrm{d}S=\frac{1}{T}\mathrm{d}E-\frac{p}{T}\mathrm{d}V\), so \(\left.\left(\frac{\partial S}{\partial V}\right)\right|_E=\frac{p}{T}\)

### Exercise 3  

Given that the partial derivatives of \(z=z(x,y)\) and those of its inverse function exist, prove: \(\frac{\partial z}{\partial x}\frac{\partial x}{\partial y}\frac{\partial y}{\partial z}=-1\)

> Proof: Let \(\mathrm{d}z=a\mathrm{d}x+b\mathrm{d}y\), and let \(a\), \(b\) be nonzero (because the partial derivatives of the inverse function exist). Transposing terms gives \(\mathrm{d}x=\frac{1}{a}\mathrm{d}z-\frac{b}{a}\mathrm{d}y\) and \(\mathrm{d}y=\frac{1}{b}\mathrm{d}z-\frac{a}{b}\mathrm{d}x\), so \(\frac{\partial z}{\partial x}\frac{\partial x}{\partial y}\frac{\partial y}{\partial z}=a\cdot\left(-\frac{b}{a}\right)\cdot\left(\frac{1}{b}\right)=-1\)

As can be seen, in these examples, we treat the differential forms \(\mathrm{d}E\), \(\mathrm{d}S\), \(\mathrm{d}V\), and so on as ordinary variables, performing transposition and substitution on them. This is natural, because they are all 1-forms, whose definitions do not depend on any coordinate system.

In proving the above formulas, we have in fact unknowingly used the inverse function theorem and the implicit function theorem.

### Exercise 4  

Verify the inverse function theorem:

If \(\mathbf{y} : \mathbb{R}^n\rightarrow \mathbb{R}^n\) is differentiable and its derivative (Jacobian matrix) is invertible, then \(\frac{\partial \mathbf{x}}{\partial \mathbf{y}}=\left(\frac{\partial \mathbf{y}}{\partial \mathbf{x}}\right)^{-1}\).

> Proof: Denote the Jacobian matrix by   
>   
>  \(\frac{\partial \mathbf{y}}{\partial \mathbf{x}}= \begin{bmatrix} \frac{\partial y_1}{\partial x_1}&\frac{\partial y_1}{\partial x_2}&\cdots&\frac{\partial y_1}{\partial x_n}\\ \frac{\partial y_2}{\partial x_1}&\frac{\partial y_2}{\partial x_2}&\cdots&\frac{\partial y_2}{\partial x_n}\\ \vdots&\vdots&\ddots&\vdots\\ \frac{\partial y_n}{\partial x_1}&\frac{\partial y_n}{\partial x_2}&\cdots&\frac{\partial y_n}{\partial x_n} \end{bmatrix}\)   
>   
> Then   
>  \(\mathrm{d}\mathbf{y} = \frac{\partial \mathbf{y}}{\partial \mathbf{x}}\mathrm{d} \mathbf{x}\)   
>   
> that is,   
>  \(\begin{bmatrix} \mathrm{d}y_1 \\ \mathrm{d}y_2 \\ \vdots \\ \mathrm{d}y_n \end{bmatrix} = \begin{bmatrix} \frac{\partial y_1}{\partial x_1}&\frac{\partial y_1}{\partial x_2}&\cdots&\frac{\partial y_1}{\partial x_n}\\ \frac{\partial y_2}{\partial x_1}&\frac{\partial y_2}{\partial x_2}&\cdots&\frac{\partial y_2}{\partial x_n}\\ \vdots&\vdots&\ddots&\vdots\\ \frac{\partial y_n}{\partial x_1}&\frac{\partial y_n}{\partial x_2}&\cdots&\frac{\partial y_n}{\partial x_n} \end{bmatrix} \begin{bmatrix} \mathrm{d}x_1 \\ \mathrm{d}x_2 \\ \vdots \\ \mathrm{d}x_n \end{bmatrix}\)   
>   
> Solving gives   
>  \(\begin{bmatrix} \mathrm{d}x_1 \\ \mathrm{d}x_2 \\ \vdots \\ \mathrm{d}x_n \end{bmatrix} = \begin{bmatrix} \frac{\partial y_1}{\partial x_1}&\frac{\partial y_1}{\partial x_2}&\cdots&\frac{\partial y_1}{\partial x_n}\\ \frac{\partial y_2}{\partial x_1}&\frac{\partial y_2}{\partial x_2}&\cdots&\frac{\partial y_2}{\partial x_n}\\ \vdots&\vdots&\ddots&\vdots\\ \frac{\partial y_n}{\partial x_1}&\frac{\partial y_n}{\partial x_2}&\cdots&\frac{\partial y_n}{\partial x_n} \end{bmatrix}^{-1} \begin{bmatrix} \mathrm{d}y_1 \\ \mathrm{d}y_2 \\ \vdots \\ \mathrm{d}y_n \end{bmatrix}\)   
>   
> that is, \(\mathrm{d}\mathbf{x} = \left(\frac{\partial \mathbf{y}}{\partial \mathbf{x}}\right)^{-1}\mathrm{d} \mathbf{y}\)   
>   
> Therefore \(\frac{\partial \mathbf{x}}{\partial \mathbf{y}}=\left(\frac{\partial \mathbf{y}}{\partial \mathbf{x}}\right)^{-1}\)

### Exercise 5  

Verify the implicit function theorem:

Given \(f:\mathbb{R}^m\times\mathbb{R}^n\rightarrow\mathbb{R^n}\), \(\mathbf f(x_1,x_2,\cdots,x_m,y_1,y_2,\cdots,y_n)=\bm{0}\), if \(\frac{\partial\mathbf{f}}{\partial\mathbf{y}}\) is invertible, then \(\frac{\partial \mathbf y}{\partial \mathbf x}=-\left(\frac{\partial \mathbf f}{\partial \mathbf y}\right)^{-1}\frac{\partial \mathbf  f}{\partial \mathbf x}\)

> Proof: From \(\mathbf{f}=\mathbf{0}\), we obtain \(\mathrm{d} \mathbf{f} = \mathbf{0}\), that is, \(\begin{bmatrix} \mathrm{d}f_1 \\  \vdots \\ \mathrm{d}f_m \end{bmatrix} = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_m} & \frac{\partial f_1}{\partial y_1} & \cdots & \frac{\partial f_1}{\partial y_n}  \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ \frac{\partial f_{m}}{\partial x_1} & \cdots & \frac{\partial f_{m}}{\partial x_m} & \frac{\partial f_{m}}{\partial y_1} & \cdots & \frac{\partial f_{m}}{\partial y_n}  \end{bmatrix} \begin{bmatrix} \mathrm{d} x_1 \\ \vdots \\ \mathrm{d} x_m \\ \mathrm{d}y_1  \\ \vdots \\ \mathrm{d}y_n  \end{bmatrix} = \begin{bmatrix} 0  \\ \vdots  \\ 0  \end{bmatrix}\)   
>   
> Transposing terms gives:  
>  \(\begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_m}   \\ \vdots & \ddots & \vdots  \\ \frac{\partial f_{m}}{\partial x_1} & \cdots & \frac{\partial f_{m}}{\partial x_m}  \end{bmatrix} \begin{bmatrix} \mathrm{d} x_1 \\ \vdots \\ \mathrm{d} x_m  \end{bmatrix} = -\begin{bmatrix} \frac{\partial f_1}{\partial y_1} & \cdots & \frac{\partial f_1}{\partial y_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_{m}}{\partial y_1} & \cdots & \frac{\partial f_{m}}{\partial y_n}  \end{bmatrix} \begin{bmatrix}  \mathrm{d}y_1  \\ \vdots \\ \mathrm{d}y_n  \end{bmatrix}\)   
>   
> Solving gives:  
>  \(\begin{bmatrix}  \mathrm{d}y_1  \\ \vdots \\ \mathrm{d}y_n  \end{bmatrix} = -\begin{bmatrix} \frac{\partial f_1}{\partial y_1} & \cdots & \frac{\partial f_1}{\partial y_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_{m}}{\partial y_1} & \cdots & \frac{\partial f_{m}}{\partial y_n}  \end{bmatrix}^{-1} \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_m}   \\ \vdots & \ddots & \vdots  \\ \frac{\partial f_{m}}{\partial x_1} & \cdots & \frac{\partial f_{m}}{\partial x_m}  \end{bmatrix} \begin{bmatrix} \mathrm{d} x_1 \\ \vdots \\ \mathrm{d} x_m  \end{bmatrix}\)   
>   
> that is, \(\mathrm{d}\mathbf{y}=\left[-\left(\frac{\partial \mathbf f}{\partial \mathbf y}\right)^{-1}\frac{\partial \mathbf  f}{\partial \mathbf x}\right]\mathrm{d}\mathbf{x}\)

It can be seen that, to some extent, both the inverse function theorem and the implicit function theorem are almost self-evident. Indeed, in textbooks, they are both proved using the chain rule, and the chain rule itself is the most direct manifestation of the “invariance of differential forms.”

The inverse function theorem and the implicit function theorem are the most broadly applicable tools. Exercises 1–3 can all be proved using the inverse function theorem and the implicit function theorem.

## What Are Higher-Order Differentials?  

Higher-order differentials are meaningless, because taking the **exterior** differential of any function twice yields zero: \(\mathrm{d}\mathrm{d}=0\).

Although higher-order (exterior) differentials have little meaning, “higher-order differential forms” are quite meaningful. In differential geometry, “differential form” is a technical term. We have first-order differential forms, second-order differential forms, ..., n-th-order differential forms, or simply n-forms.

“Higher-order differential forms” still possess the “invariance” described above. For example, the definition of \(\mathrm{d}f \wedge \mathrm{d}g\) depends only on the definitions of \(f\) and \(g\), and not on any coordinate system.

For example, in thermodynamics, we have:

\[\mathrm{d} p \wedge \mathrm{d} V = \mathrm{d} T \wedge \mathrm{d}S \]

> Proof: \(\mathrm{d} T \wedge \mathrm{d}S - \mathrm{d} p \wedge \mathrm{d} V= \mathrm{d}(T\mathrm{d}S - p \mathrm{d}V) = \mathrm{d}\mathrm{d}E = 0\)

It holds independently of any local coordinate system. Using this, we can prove the Maxwell relations as follows:

\[\begin{aligned} \mathrm{d} T \wedge \mathrm{d}S &=\left[\left(\frac{\partial T}{\partial V}\right)_S \mathrm{d}V + \left(\frac{\partial T}{\partial S}\right)_V \mathrm{d}S\right] \wedge \mathrm{d}S \\ &=  \left(\frac{\partial T}{\partial V}\right)_S   \mathrm{d}V \wedge \mathrm{d}S \end{aligned}\]

\[\begin{aligned} \mathrm{d} p \wedge \mathrm{d}V &=\left[\left(\frac{\partial p}{\partial V}\right)_S \mathrm{d}V + \left(\frac{\partial p}{\partial S}\right)_V \mathrm{d}S\right] \wedge \mathrm{d}V \\ &=  \left(\frac{\partial p}{\partial S}\right)_V   \mathrm{d}S \wedge \mathrm{d}V \\ &= - \left(\frac{\partial p}{\partial S}\right)_V   \mathrm{d}V \wedge \mathrm{d}S \end{aligned}\]

Therefore \(\begin{aligned} \left(\frac{\partial T}{\partial V}\right)_S = - \left(\frac{\partial p}{\partial S}\right)_V \end{aligned}\)

The other Maxwell relations can likewise be obtained by this method.

In this way, not only do “first-order differential forms,” or 1-forms, possess invariance, but “n-th-order differential forms,” or n-forms, all possess invariance as well. Moreover, they are also useful (for example, for proving the Maxwell relations).

## Analysis vs. Geometry  

The invariance of differential forms is based on the chain rule, the implicit function theorem, and the inverse function theorem.

In elementary calculus (mathematical analysis), the invariance of differential forms is a manifestation of these theorems. In other words, when applying the invariance of differential forms, we are in fact using these theorems.

From the perspective of differential geometry, however, the invariance of differential forms is self-evident. Of course, differential geometry is built upon elementary calculus.

Returning to the initial example:

> If, when \(\mathrm{d}y\) in \(y\) denotes the function \(y=f(x)\) and \(\mathrm{d}x\) in \(x\) denotes the function \(\phi(x)=x\), \(\mathrm{d}y=a\mathrm{d}x\) holds, that is, \(\mathrm{d}f=a\mathrm{d}\phi\) holds,   
>   
> then, when \(\mathrm{d}y\) in \(y\) denotes the function \(y=g(t)\) and \(\mathrm{d}x\) in \(x\) denotes the function \(x=\varphi(t)\), \(\mathrm{d}y=a\mathrm{d}x\) likewise holds, that is, \(\mathrm{d}g=a\mathrm{d}\varphi\) holds.   
>   
>  \(\mathrm{d}f=a\mathrm{d}\phi\) and \(\mathrm{d}g=a\mathrm{d}\varphi\) are two different equations, but both can be written as \(\mathrm{d}y=a\mathrm{d}x\). This is the invariance of differential forms.

From the perspective of analysis, the functions \(f\) and \(g\) above are different functions, and the functions \(\phi\) and \(\varphi\) are also different functions. Meanwhile, \(y,\ x,\ t\) are merely variables, not the functions themselves.

From the perspective of geometry, however, \(y\) is the function \(y\); \(x\) is the function \(x\); and \(t\) is the function \(t\). They are all functions on the manifold.

---

Consider another example (the inverse function theorem):

> Transposing terms in \(\mathrm{d}y = a\mathrm{d}x\) gives \(\mathrm{d}x = \frac{1}{a}\mathrm{d}y\)

From the perspective of analysis, this operation uses the inverse function theorem rather than being a simple transposition of terms. This is because the function changes from \(y=f(x)\) to \(x=g(y)\), and \(f\) and \(g\) are two different functions.

From the perspective of geometry, however, this truly is an utterly ordinary transposition of terms.

---

Consider another example (the implicit function theorem):

> Transposing terms in \(\mathrm{d}z = a\mathrm{d}x + b \mathrm{d}y\) gives \(\mathrm{d}x = \frac{1}{a}\mathrm{d}z - \frac{b}{a}\mathrm{d}y\)

From the perspective of analysis, this in fact uses the implicit function theorem rather than being a simple transposition of terms. This is because the function changes from \(z=f(x,y)\) to \(x=g(y,z)\), and \(f\) and \(g\) are two different functions.

From the perspective of geometry, however, this truly is an utterly ordinary transposition of terms.
