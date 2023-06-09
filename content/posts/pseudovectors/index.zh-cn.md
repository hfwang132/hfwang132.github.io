---
title: "赝矢量到底是什么？"
date: 2023-06-10T02:21:18+08:00
draft: false
---

## 1 引子

我们在物理书中经常看到所谓“赝矢量”（pseudo-vector）和“赝标量”（pseudo-scalar）的说法。

其实，在 3 维流形上，“赝矢量”是两个切矢量的外积 $v\in T\_pM\wedge T\_pM=\bigwedge^2(T\_pM)$ ，“赝标量”是三个切矢量的外积 $s\in T\_pM\wedge T\_pM\wedge T\_pM=\bigwedge^3(T\_pM)$ 。

在配备了内积（或者非退化双线性形式）之后， $\bigwedge^2(T\_pM)$ 和 $\bigwedge^1(T\_pM)$ 之间有 Hodge 对偶关系，所以我们“误把”赝矢量当作矢量了。同理，由于 \bigwedge^3(T\_pM) 和 $\bigwedge^0(T\_pM)$ （标量场）之间有 Hodge 对偶关系，所以我们“误把”赝标量当作标量了。

实际上，3 维流形上的赝矢量，在数学上就是 2-矢量（bivector，2-vector）。它和 2-form 的定义是类似的，只不过 2-vector 在切空间的外积中 $v\in\bigwedge^2(T\_pM)$ ，而 2-form 在余切空间的外积中 $\omega\in\bigwedge^2(T\_p^\*M)$ 。

---

## 2 空间反演变换

回想一下，我们之所以把“赝矢量”叫做“赝矢量”，是因为它们在空间反演变换下会有奇怪的行为。但是如果你把它当作两个矢量的外积，那么一切怪异的行为都有了解释。

具体地，看下图，在空间反演变换下，磁场竟然调转了方向！这就类似于你往一个方向移动，但是镜子里的你往另一个方向移动。这不得不说是一个灵异事件。

{{< figure src="pseudovector.svg" title="磁场是一个 bivector。如果你把磁场看成 vector，就会出现图中这种灵异的现象：磁场照了一下镜子，发现自己的头变成脚了。" >}}


但实际上，点 $p$ 处的磁场并非一个 vector，而是一个 bivector。即 $B|\_p\in (T\_pM)\wedge (T\_pM)$ 。它的基为 $\frac{\partial}{\partial x}\wedge \frac{\partial}{\partial y},\\,\frac{\partial}{\partial y}\wedge \frac{\partial}{\partial z},\\,\frac{\partial}{\partial z}\wedge \frac{\partial}{\partial x}$ 。

所以说，并没有什么灵异事件（欢迎收看《走近科学》）。在空间反演变换下，磁场对应的两个 vector 分别都朝向了正确的方向，只不过人类非要用右手螺旋定则，将一个 bivector 看成是一个 vector，这才导致了诡异现象的出现。

虽然数学上对 bivector 有完善的定义，但我们还是想问：怎样画出 bivector？答案是：可以把一个 bivector 画成有取向的面元。不同形状的面元，只要它们相互平行，且面积相同，就指的是同一个 bivector。换句话说，同一个 bivector 可以有许多不同的画法，只要保证它们平行，且面积和取向相同即可。

{{< figure src="bivectors.jpeg" title="平行、面积相同、取向相同的面元，对应同一个 bivector。" >}}

实际上，将 bivector 通过右手螺旋定则，看成一个 vector ，这只在三维流形中可行。因为只有在三维流形中，三减二才恰好等于一。在四维流形中，由于四减二等于二，我们只能把 bivector 对偶成另外一个 bivector ，而不是一个 vector。

而在五维流形中，bivector 可以对偶成一个 trivector ，...，在 n 维流形中，bivector 可以对偶成一个 (n-2)-vector。

---

## 3 麦克斯韦方程的外代数形式

顺便一提，电场也是一个 bivector，它的基为 $\frac{\partial}{\partial t}\wedge \frac{\partial}{\partial x},\\,\frac{\partial}{\partial t}\wedge \frac{\partial}{\partial y},\\,\frac{\partial}{\partial t}\wedge \frac{\partial}{\partial z}$ ，有一个时间维度。之所以它看起来不是“赝矢量”，是因为我们只考虑了空间反演变换，没有考虑时间反演变换。

如果考虑余切空间中的电磁 2-形式（采取自然单位制）:

$$ \begin{aligned} F&=E\_x\mathrm{d}t\wedge\mathrm{d}x+E\_y\mathrm{d}t\wedge\mathrm{d}y+E\_z\mathrm{d}t\wedge\mathrm{d}z \\\\ &+B\_x \mathrm{d}y\wedge\mathrm{d}z + B\_y \mathrm{d}z\wedge\mathrm{d}x + B\_z\mathrm{d}x\wedge\mathrm{d}y \end{aligned} $$

由于我们可以通过度规张量来任意升降一个张量的指标，所以对上式升指标，我们也可以写出一个 $(2,0)$ 型电磁张量，它以 $\frac{\partial}{\partial t},\frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z}$ 的外积为基。

不过我们暂时先采用 $(0,2)$ 型反对称张量（微分形式），因为这样做可以利用外微分（Exterior Derivative）的符号 $\mathrm{d}$ 。

现在，再考虑电流 1-形式： $J=-\rho\mathrm{d}t+J\_x\mathrm{d}x+J\_y\mathrm{d}y+J\_z\mathrm{d}z$

于是，在闵可夫斯基度规 $\text{diag}(-1,1,1,1)$ 下，麦克斯韦方程就可以写成很简洁的形式：

$$ \left\\{\quad \begin{aligned} \mathrm{d}F&=0 \\\\ \star \\, \mathrm{d}\star F &= J \end{aligned} \right. $$ 

其中 $\star$ 是 Hodge 星算子（也就是 Hodge 对偶）。

可以看出，在外代数的语言中，电磁场是一个 2-vector 或者 2-form，而不是一个 vector 或者 1-form。

不过电流确实是一个 vector（或 1-form）。