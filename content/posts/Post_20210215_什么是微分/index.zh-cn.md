---
title: "什么是微分？"
date: 2021-02-15T21:44:54+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/350863444"
author: "Haifei"
tags: ["微分几何"]
categories: ["数学物理方法"]
---

## 一 微分是无穷小？  

物理人喜欢把微分看做是一个很小的量，这在计算时总是很方便的，但是给人一种不严谨的感觉。

实际上，它确实不严谨，第二次数学危机就是因此产生的。

严谨性与易懂性永远是互补的。把微分看做无穷小，迎合感性的胃口，却无法通过理性的审查。

---

## 二 微分是线性函数  

我喜欢把（某一点处的）微分看做一个机器，例如

\[f:f(x,y)=x^2+2y^2\]

在 \((1,1)\) 处的微分

它就是这样一个机器：

{{< figure src="images/v2-6d1332097f22ecd45338f34dc1b3292a_r.jpg" >}}

它接受两个数，吐出一个数。

写出来就是这样：

\[\mathrm{d}f|_{(1,1)}(a,b)=\frac{\partial f}{\partial x}\bigg|_{(1,1)}a+\frac{\partial f}{\partial y}\bigg|_{(1,1)}b=2a+4b\]

由于每一点的偏导可能不同，所以如果说某一点的微分是一个机器，那么，微分就是机器构成的海洋。

你可能还注意到了这个机器是“线性的”，它不过就是 \(\mathbb{R}^2\) 到 \(\mathbb{R}\) 的线性映射。

---

线性代数的知识告诉我们，线性函数的集合可以构成线性空间。换言之，线性函数自己就是个“矢量”，是可以加减数乘的。

回到上面的比喻，就是说，我们可以把两个机器加起来： \(\mathrm{d}f|_p+\mathrm{d}g|_p\) ，

也可以将一个机器变为原来的 \(\lambda\) 倍大： \(\lambda \cdot \mathrm{d}f|_p \) 。

下标 p 表示在 p 点的取值。

把机器加起来是什么意思呢？举个例子，若

\(\mathrm{d}f|_p(a,b)=2a+4b,\,\, \mathrm{d}g|_p(a,b)=a-b\) ，

则 \(\mathrm{d}f|_p(a,b)+\mathrm{d}g|_p(a,b)=3a+3b\) 。

这很像是两个矢量的相加： \((2,4)+(1,-1)=(3,3)\) 。

实际上，它们就是矢量。是的，你没听错，微分是矢量（场）。

---

## 三 微分是对偶矢量场/协变矢量场  
### 3.1 切空间  

如果你想要在一个弯曲的面上研究微分，那么你就需要重新定义一些概念。比如，微分是线性的，可是流形是弯曲的，所以我们需要在这弯曲中定义一个线性的东西出来。这个线性的东西就是切空间。

顾名思义，切空间就是一个曲面在某一个点处的切面。但是要怎么定义它呢？这里的弯曲并不是嵌在另一个空间里的弯曲，而是空间本身的弯曲，这种弯曲是内禀的。我们不能像古典解析几何那样去求切面方程。

我们换一个思路：

首先，它是线性的，也就是说它是一个向量空间。

> 向量空间就是一个配备了数乘的阿贝尔群。具体地说，它里面的元素（称为矢量）满足如下性质：  
> *（1）矢量的加法交换律*  
> *（2）矢量的加法结合律*  
> *（3）矢量的加法有单位元(类似于零)*  
> *（4）矢量的加法有逆元(类似于相反数)*  
> *以上四个性质表明线性空间对于矢量加法而言是一个阿贝尔群。*  
> *（5）数乘有乘法单位元*  
> *（6）数乘的乘法结合律*  
> *（7）数乘的乘法分配律（对标量分配）*  
> *（8）数乘的乘法分配律（对矢量分配）*

向量空间不必是 \(\mathbb{R}^n,\,\mathbb{C}^n\)，只要一个集合里定义了加法和数乘运算且满足以上性质，这个集合就是一个向量空间。

我们可以定义这样一个向量空间，它其中的元素是光滑函数的集合到实数域的线性映射：

> \(v:\mathcal{F}_M\rightarrow\mathbb{R}\) 满足  
> （1）\(v(\lambda f+\mu g)=\lambda v(f)+\mu v(g)\) （线性律）  
> （2） \(v|_p(f\cdot g)=f|_p\cdot v(g)+g|_p\cdot v(f)\) （莱布尼茨律）  
> 其中 \(\mathcal{F}_M\) 是微分流形 \(M\) 上所有光滑函数构成的集合。

可以证明， \(v\) 的集合可以构成向量空间。

别看这个定义这么复杂，实际上就是对一个函数在某一点求方向导数。

以二元函数为例，我们显式地写出 \(v\) 的一个实例： \(\left(a\frac{\partial}{\partial x}+b\frac{\partial}{\partial y}\right)\bigg|_p\)

如果以 \((\frac{\partial}{\partial x}\bigg|_p,\frac{\partial}{\partial y}\bigg|_p)\) 为基，那么它的坐标就是 \((a,b)\) 。

这个线性空间就是流形 \(M\) 上点 \(p\) 处的切空间，记作 \(T_pM\) 。

以上所有操作都是在某一点 \(p\) 的，每一点都长出了一个切空间。你可以想象成弯曲面上的每一点都长出了一个切平面。

我们可以把 \(\frac{\partial}{\partial x}\) 简写成 \(\partial_x\) ，把 \(\frac{\partial}{\partial y}\) 简写成 \(\partial_y\) 。

---

### 3.2余切空间  

刚才介绍了切空间 \(T_p M\) 。我们现在把切空间的对偶空间 \(T_p^*M\) 叫做*余切空间*。

某一点的微分正是余切空间中的元素。换言之，某一点的微分是一个余切矢量。

对偶空间中的元素（余切矢量）是线性泛函，能把原空间中的元素映射成一个数。这正是我们之前所说的机器：

{{< figure src="images/v2-6d1332097f22ecd45338f34dc1b3292a_r.jpg" >}}

只不过现在的输入应该是切空间中的元素 \(\left(a\partial_x+b\partial_y\right)|_p\) 。

我们说过，微分是机器的海洋。因此余切矢量的海洋（也就是微分）可以叫做余切矢量场。

在数学中，微分（余切矢量场）有一个酷炫的名字，叫做余切丛的截影。详见

[一文入门微分几何（物理人版）](https://zhuanlan.zhihu.com/p/629852598)

---

说了这么多抽象废话，下面来定义一下：

流形 \(M\) 上某一点 \(p\) 处的微分是这样一个线性泛函，它作用到切空间的元素 \(v|_p\in T_pM\) 上，得到 \(\mathrm{d}f|_p(v|_p)=v|_p(f)\)

再举一个更显式的例子，以二元函数为例：

\[\mathrm{d}f|_{p}:\mathrm{d}f|_{p}(v|_p)=v|_p(f)= (\partial_x f)|_{p}\cdot a+(\partial_y f)|_{p}b,\quad \text{其中}\quad v|_p=\left(a\partial_x+b\partial_y\right)|_p\]

> 切空间中的矢量也可以叫协变矢量，余切空间中的矢量也可以叫做协变矢量。这是怎么一回事？  
>   
> **逆变矢量**  
>   
> 在接触微分几何前，我们基本上都在使用逆变矢量场，而非协变矢量场。这是因为当我们选定一组基之后，坐标变换是基变换的逆变换，这就是“逆变”的意思，即变换规则与基变换相反。  
>   
> 例如，给定一个矢量场 \(A^\mu = (A^x, A^y, A^z)\) ，即 \(A = A^\mu e_\mu\) ，其中 \(e_\mu\) 是我们选取的基。注意这里使用了爱因斯坦求和约定，即对相同的上下标进行求和。  
>   
> 当做基变换 \(e^\prime_\nu = M^{\mu}_\nu e_{\mu}\) 时，由于 \(A^\mu e_\mu = A^{\prime \mu} e^\prime_\mu\) ，很显然，坐标变换就应当是 \(A^{\prime \mu} = (M^{-1})^{\mu}_{\nu} A^\nu\) 。  
>   
> 实际上， \(e_\mu = \partial_\mu = \frac{\partial}{\partial x_\mu}\) 。这看起来可能很奇怪，不过在微分几何中，逆变矢量的定义就是偏导算子，正如上文所说。  
>   
> 注意，逆变矢量的坐标都应该写成上标，例如 \(A^\mu\) ，以便于和基的下标 \(e_\mu\) 缩并（根据爱因斯坦求和约定）。  
>   
> **协变矢量**  
>   
> 反过来，“协变”的意思就是坐标变换和基变换的矩阵相同。但怎么会有这样的矢量呢？  
>   
> 实际上，协变矢量生活在另一个空间，叫做原空间的对偶空间。  
>   
> 对偶空间中的矢量 \(\omega_\mu\) （写成下标）可以和原空间中的矢量 \(v^{\mu}\) （上标）相互缩并成为一个标量： \(\omega_\mu v^\mu = C\) 。  
>   
> 与 \(e_\mu = \partial_\mu\) 对偶的基是 \(\mathrm{d}x^\mu\) ，满足 \(\mathrm{d}x^\mu \partial_\nu = \delta^\mu_\nu = \begin{cases} 1 & \mu=\nu \\ 0 & \mu\ne \nu\end{cases}\) 。  
>   
> 运用和之前相似的推理，我们能够得出，对偶基 \(\mathrm{d}x^\mu\) 的变换矩阵是基 \(\partial_\mu\) 变换的逆矩阵。从而，对偶矢量的坐标 \(\omega_\mu\) 变换矩阵是基 \(v^\mu\) 变换矩阵的逆的逆，也就是正好等于基变换矩阵本身。  
>   
> 这就是“协变”的意思，即变换规则与基变换相同。  
>   
> 因此我们也可以说，微分是协变矢量场。

## 四微分形式是反对称协变张量场/反对称多重线性泛函  

微分形式可以看做是协变反对称张量场。反对称的意思就是，交换下标会改变符号： \(\omega_{\mu \nu} = -\omega_{\nu\mu}\) 。

例如，二阶反对称协变张量场 \(\omega_{\mu\nu}\) 是 2-形式。

特别地，协变矢量场（即我们通常所说的微分） \(\omega_\mu\) 是 1-形式，而标量场是 0-形式。

两个 1-形式通过 wedge product 可以得到 2-形式：

\[\omega = \alpha \wedge \beta = \alpha_\mu \beta_\nu\mathrm{d}x^\mu \wedge  \mathrm{d}x^\nu \]

其中 \(\mathrm{d}x^\mu \wedge  \mathrm{d}x^\nu  = -\mathrm{d}x^\nu \wedge  \mathrm{d}x^\mu\)

以此类推。

此节之前所说的微分都是 1-形式。（某一点的）1-形式是切空间到实数域的线性泛函，那么 n-形式呢？

（某一点的）n-形式定义为一个 n 输入的反对称多重线性泛函。反对称的意思是交换两个输入，输出会多一个负号：

\[\omega^1\wedge \omega^2\wedge\cdots\wedge \omega^n(v_1,v_2,\cdots,v_n)= \begin{vmatrix} \omega^1(v_1) & \cdots & \omega^{1}(v_n) \\ \vdots & \ddots & \vdots \\ \omega^n(v_1) & \cdots  & \omega^n(v_n) \end{vmatrix}\]

根据行列式的性质，交换两列，行列式会变为相反数。这完美刻画了微分形式的反对称性。

> 例：  
>   
> 在 3 维流形上的点 \(p\) 处有一个 2-形式 ： \(\omega = 5\mathrm{d}x^1 \wedge \mathrm{d}x^3 -2\mathrm{d}x^2\wedge \mathrm{d}x^3\)   
>   
> 它作用到两个切矢量 \(u=\partial_1+2\partial_2+3\partial_3\) 和 \(v=3\partial_1-2\partial_2+\partial_3\) 上得到：   
>   
> \[\begin{aligned} \omega(u,v)&= 5\begin{vmatrix} \mathrm{d}x^1(\partial_1+2\partial_2+3\partial_3) & \mathrm{d}x^1(3\partial_1-2\partial_2+\partial_3) \\ \mathrm{d}x^2(\partial_1+2\partial_2+3\partial_3) & \mathrm{d}x^2(3\partial_1-2\partial_2+\partial_3) \end{vmatrix}\\ &-2\begin{vmatrix} \mathrm{d}x^2(\partial_1+2\partial_2+3\partial_3) & \mathrm{d}x^2(3\partial_1-2\partial_2+\partial_3) \\ \mathrm{d}x^3(\partial_1+2\partial_2+3\partial_3) & \mathrm{d}x^3(3\partial_1-2\partial_2+\partial_3) \end{vmatrix} \\&=5\cdot\begin{vmatrix}1&3\\2 &-2\end{vmatrix}-2\cdot\begin{vmatrix}2&-2\\3 & 1\end{vmatrix} \\&=-48 \end{aligned}\]  
>   
> 它的几何意义是：矢量 \(u\) 和 \(v\) 所形成的平行四边形在面元 \(\omega\) 上的投影面积。当然，这个面积是有向的，因此有可能出现负值。

为什么我们要求微分形式拥有反对称的结构？这是因为我们希望微分形式可以刻画体积的概念。详见：

[为何行列式要这样定义，而这样定义出来的数的绝对值为何就是所成几何体的「体积」？](https://www.zhihu.com/question/440490236/answer/1731646509)

当有了体积的概念之后，我们就可以对微分形式积分了。实际上，我们在高等数学中做面积分和体积分的时候，用到的都是微分形式：

\[\mathrm{d}x\, \mathrm{d}y \,\mathrm{d}z := \mathrm{d}x \wedge \mathrm{d}y \wedge \mathrm{d}z\]

在微分几何中，我们是对微分形式积分，而不是对函数积分。例如，在 \(\int f(x) \mathrm{d}x\) 这个式子中， \(\mathrm{d}x\) 是 1-形式， \(f(x) \mathrm{d}x\) 也是 1-形式；在 \(\int f(x,y,z) \,\mathrm{d}x\, \mathrm{d}y \,\mathrm{d}z\) 这个式子中， \(\mathrm{d}x\, \mathrm{d}y \,\mathrm{d}z := \mathrm{d}x \wedge \mathrm{d}y \wedge \mathrm{d}z\) 是 3-形式， \(f(x)\mathrm{d}x \wedge \mathrm{d}y \wedge \mathrm{d}z\) 也是 3-形式。

## 五 微分是外微分  

以上所说的“微分”，指的都是一个数学对象经过“微分运算”后得到的另一个数学对象。

那么，什么才是“微分运算”本身呢？它就是外微分。

定义外微分运算 \(\mathrm{d}\) ，它将 n-形式变为 (n+1)-形式：

\[\begin{aligned} \mathrm{d} \omega &= \mathrm{d}(\omega_\mu \mathrm{d}x^\mu)\ \\  &:= \mathrm{d}(\omega_\mu) \wedge \mathrm{d}x^\mu \\ &= (\partial_\nu \omega_\mu\mathrm{d}x^\nu)\wedge\mathrm{d}x^\mu  \end{aligned}\]

一句话概括，外微分运算就是对每个基上的分量取全微分再 wedge 上对应的基。

特别地，对 0-形式（标量场）做外微分运算，就是我们通常所说的微分： \(\mathrm{d}f = (\partial_\mu f) \mathrm{d}x^\mu\) 。

至于外微分有什么用，敬请移步本专栏其他文章。关于微分就暂时讲到这了。
