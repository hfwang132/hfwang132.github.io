---
title: "对微分形式不变性的理解"
date: 2021-02-16T14:23:58+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/350936061"
author: "Haifei"
tags: ["微分几何"]
categories: ["数学物理方法"]
---

21/03/2025：本文大改

## 什么是微分形式不变性？  

按照教科书上所说，微分形式不变性的意思是：做变量替换，微分等式的形式不变。即：

> 如果，当 \(\mathrm{d}y\) 中的 \(y\) 指函数 \(y=f(x)\) ，\(\mathrm{d}x\) 中的 \(x\) 指函数 \(\phi(x)=x\) 时，有 \(\mathrm{d}y=a\mathrm{d}x\) 成立，也就是 \(\mathrm{d}f=a\mathrm{d}\phi\) 成立，   
>   
> 那么，当 \(\mathrm{d}y\) 中的 \(y\) 指函数 \(y=g(t)\) ，\(\mathrm{d}x\) 中的 \(x\) 指函数 \(x=\varphi(t)\) 时，同样有 \(\mathrm{d}y=a\mathrm{d}x\) 成立，也就是 \(\mathrm{d}g=a\mathrm{d}\varphi\) 成立。   
>   
>  \(\mathrm{d}f=a\mathrm{d}\phi\) 和 \(\mathrm{d}g=a\mathrm{d}\varphi\) 是不同的两个等式，但是它们都可以写成 \(\mathrm{d}y=a\mathrm{d}x\) 。这就是微分形式的不变性。

但真的有必要这么绕吗？

实际上，在更高的观点看来，所谓微分形式不变性本身就是不言自明的。

考虑一维流形 \(M\) 上的可微函数 \(y: M \rightarrow \mathbb{R}\) ，其微分是流形上的余切向量场（cotangent vector fields），或 1-形式： \(\mathrm{d}y: \mathcal{T}^1_0(M) \rightarrow \mathcal{F}(M)\) ，其中 \(\mathcal{T}_0^1(M)\) 代表 \(M\) 上所有可微切向量场的集合， \(\mathcal{F}\) 代表 \(M\) 上所有可微函数的集合。

我们分别为 \(M\) 指定两组坐标系 \(x: M \rightarrow \mathbb{R}^1\) 和 \(t: M\rightarrow \mathbb{R}^1\) 。坐标系本身也是 \(M\) 上的函数。

\(\mathrm{d} y = a \mathrm{d} x\) （其中 \(a\) 是 \(M\) 上的函数）的成立是不需要依赖于任何坐标系的。这是因为 \(\mathrm{d}y\) 只依赖于 \(y\) ，\(\mathrm{d}x\) 只依赖于 \(x\) 。换句话说，无论你将 \(y\) 和 \(x\) 看成是 \(x\) 的函数，还是看成 \(t\) 的函数，都不影响 \(\mathrm{d} y = a \mathrm{d} x\) 这个式子的成立。

在微分几何里， \(y\) 和 \(x\) 都是 \(M\) 上的可微函数，它们的实在性不依赖于任何坐标系。因此 \(\mathrm{d}y\) 和 \(\mathrm{d}x\) 的实在性也不依赖于任何坐标系。就像一个雕像，无论你从哪个角度看它，都不会形象它本身的任何性质。

于是，我们可以将“微分形式不变性”解读为“ \(\mathrm{d}f\) 只依赖于 \(f\) ，不依赖于坐标系”。

## 偏导与微分有什么不同？  

偏导数与微分非常不同。求偏导操作是需要指定一个坐标系的，没有坐标系就无法求偏导。坐标系变化后，偏导也会随之变化。更致命的是：即使 \(x_1\) 没有变化，只要 \(x_2,\cdots,x_n\) 变化了， \(\frac{\partial f}{\partial x_1}\) 也会变化。可见，如果只研究偏导数，我们就会迷失在坐标系变换里，而无法抽象到更高的层次。

为什么我们不仅要研究导数，还要研究微分？原因就在于此了：微分是不依赖于坐标系的，或者说，是典范的。

## 微分形式不变性有什么用？  

最直接的应用就是证明链式法则：

> 把 \(\mathrm{d}x =\frac{\partial x}{\partial t} \mathrm{d}t\) 代入 \(\mathrm{d}y = \frac{\partial y}{\partial x} \mathrm{d}x\) 得   
>   
>  \(\mathrm{d}y = \frac{\partial y}{\partial x} \mathrm{d}x = \frac{\partial y}{\partial x}\frac{\partial x}{\partial t} \mathrm{d}t\)

在这个简单的证明中，我们用到了“代入法”。

其实这是个伪证。实际上，是先有了链式法则，才有了微分形式不变性。

利用“代入法”，我们还可以证明许多有用的式子。下面是一个例子：

### 习题 1  

（热力学）已知 \(\mathrm{d}E=T\mathrm{d}S-p\mathrm{d}V\) ，即 \(\left.\left(\frac{\partial E}{\partial S}\right)\right|_V=T,\,\left.\left(\frac{\partial E}{\partial V}\right)\right|_S=-p\) ，求 \(\left.\left(\frac{\partial E}{\partial T}\right)\right|_V,\,\left.\left(\frac{\partial E}{\partial V}\right)\right|_T\)

> 解： 将 \(\mathrm{d}S=\left.\left(\frac{\partial S}{\partial T}\right)\right|_V\mathrm{d}T+\left.\left(\frac{\partial S}{\partial V}\right)\right|_T\mathrm{d}V\) 代入 \(\mathrm{d}E=T\mathrm{d}S-p\mathrm{d}V\) 得   
>   
> \(\begin{aligned} \mathrm{d}E&=T\mathrm{d}S-p\mathrm{d}V \\ &=T\left[\left.\left(\frac{\partial S}{\partial T}\right)\right|_V\mathrm{d}T+\left.\left(\frac{\partial S}{\partial V}\right)\right|_T\mathrm{d}V\right]-p\mathrm{d}V \\ &=T\left.\left(\frac{\partial S}{\partial T}\right)\right|_V\mathrm{d}T+\left[\left.T\left(\frac{\partial S}{\partial V}\right)\right|_T-p\right]\mathrm{d}V \end{aligned}\)   
>   
> 因此 \(\left.\left(\frac{\partial E}{\partial T}\right)\right|_V=T\left.\left(\frac{\partial S}{\partial T}\right)\right|_V,\) \(\left.\left(\frac{\partial E}{\partial V}\right)\right|_T=T\left.\left(\frac{\partial S}{\partial V}\right)\right|_T-p\)

我们不仅可以通过“代入”来证明式子，还可以通过简单的“移项”来证明式子。下面是一些例子：

### 习题 2  

（热力学）已知 \(\mathrm{d}E=T\mathrm{d}S-p\mathrm{d}V\) ，即 \(\left.\left(\frac{\partial E}{\partial S}\right)\right|_V=T,\,\left.\left(\frac{\partial E}{\partial V}\right)\right|_S=-p\) ，求 \(\left.\left(\frac{\partial S}{\partial V}\right)\right|_E\)

> 解： 由 \(\mathrm{d}E=T\mathrm{d}S-p\mathrm{d}V \) 移项得 \(\mathrm{d}S=\frac{1}{T}\mathrm{d}E-\frac{p}{T}\mathrm{d}V\) ，所以 \(\left.\left(\frac{\partial S}{\partial V}\right)\right|_E=\frac{p}{T}\)

### 习题 3  

已知 \(z=z(x,y)\) 的偏导数以及其反函数的偏导数存在，证明： \(\frac{\partial z}{\partial x}\frac{\partial x}{\partial y}\frac{\partial y}{\partial z}=-1\)

> 证： 设 \(\mathrm{d}z=a\mathrm{d}x+b\mathrm{d}y\) ，且 \(a\) , \(b\) 不为零（因为反函数的偏导数存在）。移项得 \(\mathrm{d}x=\frac{1}{a}\mathrm{d}z-\frac{b}{a}\mathrm{d}y\) 以及 \(\mathrm{d}y=\frac{1}{b}\mathrm{d}z-\frac{a}{b}\mathrm{d}x\) ，所以 \(\frac{\partial z}{\partial x}\frac{\partial x}{\partial y}\frac{\partial y}{\partial z}=a\cdot\left(-\frac{b}{a}\right)\cdot\left(\frac{1}{b}\right)=-1\)

可以看到，在这些例子中，我们将微分形式 \(\mathrm{d}E\) ， \(\mathrm{d}S\) ， \(\mathrm{d}V\) 等都当作日常的变量来做移项和代换。这是很自然的，因为它们都是 1-形式，它们的定义不依赖于任何坐标系。

在证明以上式子的过程中，我们实际上不知不觉地用到了反函数定理和隐函数定理。

### 习题 4  

验证反函数定理：

如果 \(\mathbf{y} : \mathbb{R}^n\rightarrow \mathbb{R}^n\) 可微且它的导数（雅可比矩阵）可逆，则 \(\frac{\partial \mathbf{x}}{\partial \mathbf{y}}=\left(\frac{\partial \mathbf{y}}{\partial \mathbf{x}}\right)^{-1}\) 。

> 证： 记雅可比矩阵为   
>   
>  \(\frac{\partial \mathbf{y}}{\partial \mathbf{x}}= \begin{bmatrix} \frac{\partial y_1}{\partial x_1}&\frac{\partial y_1}{\partial x_2}&\cdots&\frac{\partial y_1}{\partial x_n}\\ \frac{\partial y_2}{\partial x_1}&\frac{\partial y_2}{\partial x_2}&\cdots&\frac{\partial y_2}{\partial x_n}\\ \vdots&\vdots&\ddots&\vdots\\ \frac{\partial y_n}{\partial x_1}&\frac{\partial y_n}{\partial x_2}&\cdots&\frac{\partial y_n}{\partial x_n} \end{bmatrix}\)   
>   
> 则有   
>  \(\mathrm{d}\mathbf{y} = \frac{\partial \mathbf{y}}{\partial \mathbf{x}}\mathrm{d} \mathbf{x}\)   
>   
> 即   
>  \(\begin{bmatrix} \mathrm{d}y_1 \\ \mathrm{d}y_2 \\ \vdots \\ \mathrm{d}y_n \end{bmatrix} = \begin{bmatrix} \frac{\partial y_1}{\partial x_1}&\frac{\partial y_1}{\partial x_2}&\cdots&\frac{\partial y_1}{\partial x_n}\\ \frac{\partial y_2}{\partial x_1}&\frac{\partial y_2}{\partial x_2}&\cdots&\frac{\partial y_2}{\partial x_n}\\ \vdots&\vdots&\ddots&\vdots\\ \frac{\partial y_n}{\partial x_1}&\frac{\partial y_n}{\partial x_2}&\cdots&\frac{\partial y_n}{\partial x_n} \end{bmatrix} \begin{bmatrix} \mathrm{d}x_1 \\ \mathrm{d}x_2 \\ \vdots \\ \mathrm{d}x_n \end{bmatrix}\)   
>   
> 解得   
>  \(\begin{bmatrix} \mathrm{d}x_1 \\ \mathrm{d}x_2 \\ \vdots \\ \mathrm{d}x_n \end{bmatrix} = \begin{bmatrix} \frac{\partial y_1}{\partial x_1}&\frac{\partial y_1}{\partial x_2}&\cdots&\frac{\partial y_1}{\partial x_n}\\ \frac{\partial y_2}{\partial x_1}&\frac{\partial y_2}{\partial x_2}&\cdots&\frac{\partial y_2}{\partial x_n}\\ \vdots&\vdots&\ddots&\vdots\\ \frac{\partial y_n}{\partial x_1}&\frac{\partial y_n}{\partial x_2}&\cdots&\frac{\partial y_n}{\partial x_n} \end{bmatrix}^{-1} \begin{bmatrix} \mathrm{d}y_1 \\ \mathrm{d}y_2 \\ \vdots \\ \mathrm{d}y_n \end{bmatrix}\)   
>   
> 即 \(\mathrm{d}\mathbf{x} = \left(\frac{\partial \mathbf{y}}{\partial \mathbf{x}}\right)^{-1}\mathrm{d} \mathbf{y}\)   
>   
> 所以 \(\frac{\partial \mathbf{x}}{\partial \mathbf{y}}=\left(\frac{\partial \mathbf{y}}{\partial \mathbf{x}}\right)^{-1}\)

### 习题 5  

验证隐函数定理：

已知 \(f:\mathbb{R}^m\times\mathbb{R}^n\rightarrow\mathbb{R^n}\) ， \(\mathbf f(x_1,x_2,\cdots,x_m,y_1,y_2,\cdots,y_n)=\bm{0}\) ，如果 \(\frac{\partial\mathbf{f}}{\partial\mathbf{y}}\) 可逆，则 \(\frac{\partial \mathbf y}{\partial \mathbf x}=-\left(\frac{\partial \mathbf f}{\partial \mathbf y}\right)^{-1}\frac{\partial \mathbf  f}{\partial \mathbf x}\)

> 证： 由 \(\mathbf{f}=\mathbf{0}\) 得 \(\mathrm{d} \mathbf{f} = \mathbf{0}\) ，即 \(\begin{bmatrix} \mathrm{d}f_1 \\  \vdots \\ \mathrm{d}f_m \end{bmatrix} = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_m} & \frac{\partial f_1}{\partial y_1} & \cdots & \frac{\partial f_1}{\partial y_n}  \\ \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\ \frac{\partial f_{m}}{\partial x_1} & \cdots & \frac{\partial f_{m}}{\partial x_m} & \frac{\partial f_{m}}{\partial y_1} & \cdots & \frac{\partial f_{m}}{\partial y_n}  \end{bmatrix} \begin{bmatrix} \mathrm{d} x_1 \\ \vdots \\ \mathrm{d} x_m \\ \mathrm{d}y_1  \\ \vdots \\ \mathrm{d}y_n  \end{bmatrix} = \begin{bmatrix} 0  \\ \vdots  \\ 0  \end{bmatrix}\)   
>   
> 移项得：  
>  \(\begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_m}   \\ \vdots & \ddots & \vdots  \\ \frac{\partial f_{m}}{\partial x_1} & \cdots & \frac{\partial f_{m}}{\partial x_m}  \end{bmatrix} \begin{bmatrix} \mathrm{d} x_1 \\ \vdots \\ \mathrm{d} x_m  \end{bmatrix} = -\begin{bmatrix} \frac{\partial f_1}{\partial y_1} & \cdots & \frac{\partial f_1}{\partial y_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_{m}}{\partial y_1} & \cdots & \frac{\partial f_{m}}{\partial y_n}  \end{bmatrix} \begin{bmatrix}  \mathrm{d}y_1  \\ \vdots \\ \mathrm{d}y_n  \end{bmatrix}\)   
>   
> 解得：  
>  \(\begin{bmatrix}  \mathrm{d}y_1  \\ \vdots \\ \mathrm{d}y_n  \end{bmatrix} = -\begin{bmatrix} \frac{\partial f_1}{\partial y_1} & \cdots & \frac{\partial f_1}{\partial y_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_{m}}{\partial y_1} & \cdots & \frac{\partial f_{m}}{\partial y_n}  \end{bmatrix}^{-1} \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_m}   \\ \vdots & \ddots & \vdots  \\ \frac{\partial f_{m}}{\partial x_1} & \cdots & \frac{\partial f_{m}}{\partial x_m}  \end{bmatrix} \begin{bmatrix} \mathrm{d} x_1 \\ \vdots \\ \mathrm{d} x_m  \end{bmatrix}\)   
>   
> 即 \(\mathrm{d}\mathbf{y}=\left[-\left(\frac{\partial \mathbf f}{\partial \mathbf y}\right)^{-1}\frac{\partial \mathbf  f}{\partial \mathbf x}\right]\mathrm{d}\mathbf{x}\)

可见，从某种程度上来说，反函数定理和隐函数定理都几乎是不言自明的。的确，在教科书里，它们都是由链式法则证出来的，而链式法则本身就是“微分形式不变性”的最直接体现。

反函数定理和隐函数定理是最泛用的工具。习题 1 - 3 都可以由反函数定理和隐函数定理证得。

## 什么是高阶微分？  

高阶微分没有意义，因为任何函数作两次**外**微分都会得到零： \(\mathrm{d}\mathrm{d}=0\) 。

虽然高阶（外）微分没有什么意义，但“高阶微分形式”倒是很有意义的。在微分几何中，“微分形式”是一个专有名词。我们有 1 阶微分形式、2 阶微分形式、...、n 阶微分形式，或简称 n-形式。

“高阶微分形式”仍然具有上面所说的“不变性”。例如， \(\mathrm{d}f \wedge \mathrm{d}g\) 的定义只依赖于 \(f\) 和 \(g\) 的定义，不依赖于任何坐标系。

例如，在热力学中，我们有：

\[\mathrm{d} p \wedge \mathrm{d} V = \mathrm{d} T \wedge \mathrm{d}S \]

> 证明： \(\mathrm{d} T \wedge \mathrm{d}S - \mathrm{d} p \wedge \mathrm{d} V= \mathrm{d}(T\mathrm{d}S - p \mathrm{d}V) = \mathrm{d}\mathrm{d}E = 0\)

它不依赖于任何局部坐标系而成立。利用这一点，我们可以证明麦克斯韦关系式，步骤如下：

\[\begin{aligned} \mathrm{d} T \wedge \mathrm{d}S &=\left[\left(\frac{\partial T}{\partial V}\right)_S \mathrm{d}V + \left(\frac{\partial T}{\partial S}\right)_V \mathrm{d}S\right] \wedge \mathrm{d}S \\ &=  \left(\frac{\partial T}{\partial V}\right)_S   \mathrm{d}V \wedge \mathrm{d}S \end{aligned}\]

\[\begin{aligned} \mathrm{d} p \wedge \mathrm{d}V &=\left[\left(\frac{\partial p}{\partial V}\right)_S \mathrm{d}V + \left(\frac{\partial p}{\partial S}\right)_V \mathrm{d}S\right] \wedge \mathrm{d}V \\ &=  \left(\frac{\partial p}{\partial S}\right)_V   \mathrm{d}S \wedge \mathrm{d}V \\ &= - \left(\frac{\partial p}{\partial S}\right)_V   \mathrm{d}V \wedge \mathrm{d}S \end{aligned}\]

所以 \(\begin{aligned} \left(\frac{\partial T}{\partial V}\right)_S = - \left(\frac{\partial p}{\partial S}\right)_V \end{aligned}\)

其他麦克斯韦关系式也可由此方法得到。

如此一来，不仅是“一阶微分形式”，或 1-形式，具有不变性，而且是“n 阶微分形式”，或 n-形式，都具有不变性。并且它们也很有用（例如，用来证明麦克斯韦关系式）。

## 分析 vs 几何  

微分形式的不变性是基于链式法则、隐函数定理和反函数定理的。

在初等微积分（数学分析）中，微分形式的不变性是这些定理的体现。换句话说，在运用微分形式不变性的时候，我们实际上用到了这些定理。

而在微分几何的观点中，微分形式的不变性是不言自明的。当然，微分几何建立在初等微积分的基础上。

回到一开始的例子：

> 如果，当 \(\mathrm{d}y\) 中的 \(y\) 指函数 \(y=f(x)\) ，\(\mathrm{d}x\) 中的 \(x\) 指函数 \(\phi(x)=x\) 时，有 \(\mathrm{d}y=a\mathrm{d}x\) 成立，也就是 \(\mathrm{d}f=a\mathrm{d}\phi\) 成立，   
>   
> 那么，当 \(\mathrm{d}y\) 中的 \(y\) 指函数 \(y=g(t)\) ，\(\mathrm{d}x\) 中的 \(x\) 指函数 \(x=\varphi(t)\) 时，同样有 \(\mathrm{d}y=a\mathrm{d}x\) 成立，也就是 \(\mathrm{d}g=a\mathrm{d}\varphi\) 成立。   
>   
>  \(\mathrm{d}f=a\mathrm{d}\phi\) 和 \(\mathrm{d}g=a\mathrm{d}\varphi\) 是不同的两个等式，但是它们都可以写成 \(\mathrm{d}y=a\mathrm{d}x\) 。这就是微分形式的不变性。

在分析的观点中，以上的函数 \(f\) 和 \(g\) 是不同的函数，函数 \(\phi\) 和 \(\varphi\) 也是不同的函数。而 \(y,\ x,\ t\) 都只是变量，不是函数本身。

而在几何的观点中， \(y\) 就是函数 \(y\) ；\(x\) 就是函数 \(x\) ； \(t\) 就是函数 \(t\) 。它们都是流形上的函数。

---

再来看一个例子（反函数定理）：

> 由 \(\mathrm{d}y = a\mathrm{d}x\) 移项得到 \(\mathrm{d}x = \frac{1}{a}\mathrm{d}y\)

在分析的观点中，这个操作是运用了反函数定理，而不是简单的移项。因为函数从 \(y=f(x)\) 变成了 \(x=g(y)\) ，且 \(f\) 和 \(g\) 是两个不同的函数。

但在几何的观点中，这确实是一个平平无奇的移项操作。

---

再来看一个例子（隐函数定理）：

> 由 \(\mathrm{d}z = a\mathrm{d}x + b \mathrm{d}y\) 移项得到 \(\mathrm{d}x = \frac{1}{a}\mathrm{d}z - \frac{b}{a}\mathrm{d}y\)

在分析的观点中，这实际上是运用了隐函数定理，而不是简单的移项。因为函数从 \(z=f(x,y)\) 变成了 \(x=g(y,z)\) ，且 \(f\) 和 \(g\) 是两个不同的函数。

但在几何的观点中，这确实是一个平平无奇的移项操作。
