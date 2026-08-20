---
title: "矢量乘积法则的简洁证明"
date: 2021-02-27T00:46:19+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/353243862"
author: "Haifei"
tags: ["矢量微积分"]
categories: ["数学物理方法"]
---

相信第一次学矢量微积分的小伙伴都对矢量的乘积法则非常头疼：

简单难度：

$$\nabla(fg)=f\nabla g+g\nabla f$$

$$\nabla\cdot(f\mathrm{A})=f\nabla\cdot\mathrm{A}+\nabla f\cdot \mathrm{A}$$

$$\nabla\times(f\mathrm{A})=f\nabla\times\mathrm{A}+\nabla f\times\mathrm{A}$$

困难难度：

$$\nabla\cdot(\mathrm{A}\times\mathrm{B})=\mathrm{B}\cdot(\nabla\times\mathrm{A})-\mathrm{A}\cdot(\nabla\times\mathrm{B})$$

地狱难度：

$$\nabla(\mathrm{A}\cdot \mathrm{B})=\mathrm{A}\times(\nabla\times\mathrm{B})+(\mathrm{A}\cdot\nabla)\mathrm{B}+\mathrm{B}\times(\nabla\times\mathrm{A})+(\mathrm{B}\cdot\nabla)\mathrm{A}$$

$$\nabla\times(\mathrm{A}\times\mathrm{B})=\mathrm{A}(\nabla\cdot \mathrm{B})-\mathrm{B}(\nabla\cdot\mathrm{A})+(\mathrm{B}\cdot\nabla)\mathrm{A}-(\mathrm{A}\cdot\nabla)\mathrm{B}$$

DLC：二次微分

$$\nabla\times(\nabla f)=0$$

$$\nabla\cdot(\nabla\times\mathrm{A})=0$$

$$\nabla\times(\nabla\times\mathrm{A})=\nabla(\nabla\cdot\mathrm{A})-(\nabla\cdot\nabla)\mathrm{A}$$

---

## 简洁的证明  

为了使证明尽可能简洁，我们希望用一个有下标的式子来表达多个式子，而不是每次都要把 x, y, z 全部写出来。

我们用 $x_i$ 来表示 x, y, z。即 $x_1$ 表示 $x$ ， $x_2$ 表示 $y$ ， $x_3$ 表示 $z$ 。

在开始证明之前，我们先给出一些有用的符号和关系。

---

**Einstein Convention 爱因斯坦求和约定**

$\sum_{i}a_ib_i$ 可以写成 $a_ib_i$ ，即直接把求和符号省略掉。只要下标有相同的字母，就表示对它求和。如果想表示某一项，需要写成 $a_ib_j$ ，即用不同的字母。

再给一个例子， $c_{ik}=\sum_{j}a_{ij}b_{jk}$ 可以写成 $c_{ik}=a_{ij}b_{jk}$ 。这其实就是两个矩阵相乘 $C=AB$ 。

---

**Kronecker Delta** $\delta_{ij}$

Kronecker delta 的定义是 $$  \delta_{ij}=  \begin{cases}  1&i=j\\  0&i\neq j  \end{cases}  $$

---

**规则1（迹）：** $a_i\delta_{ij}b_{j}=a_ib_i$ 。

即如果Kronecker delta的两个下标在式子里出现，那么可以消去Kronecker delta符号，并将两个下标变为同一个下标。反过来，也可以将原来两个相同的下标变成两个不同下标，并插入一个Kronecker delta将这两个下标联系起来。

如果你还不是很习惯爱因斯坦求和约定，这里再用传统写法写一遍： $\sum_{i,j}a_i\delta_{ij}b_j=\sum_{i}a_ib_i$

你可能发现了这就是矢量的点积。我们后面要用Kronecker delta来表示点积和 $\nabla\cdot$ ，也就是散度。

---

**Levi-Civita 符号** $\epsilon_{ijk}$

Levi-Civita 符号的定义是 $\epsilon_{ijk}= \begin{cases} 1&(i,j,k)是(1,2,3)的偶置换\\ -1&(i,j,k)是(1,2,3)的奇置换\\ 0& i,j,k中的任意两个相同 \end{cases}$

例如， $\epsilon_{123}=1,\,\epsilon_{213}=-1,\,\epsilon_{112}=0,\,\epsilon_{333}=0$ 。

---

**规则2（行列式）：** $\epsilon_{ijk}a_ib_jc_k=\begin{vmatrix}a_1 &a_2&a_3\\ b_1&b_2&b_3\\ c_1&c_2&c_3\end{vmatrix}$

你可能隐约感觉到这可以表示叉积，因为叉积可以用行列式表示。实际上，我们后面正是要用Levi-Civita符号来表示 $\nabla\times$ ，也就是旋度。

---

**Kronecker delta与Levi-Civita符号的关系**

$$\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$$

这个式子不难证明，只需要考虑ijk和klm的奇偶性即可。如果奇偶性相同，等式左边就为1，如果奇偶性相反，等式左边就为-1。

$$\epsilon_{ijk}\epsilon_{klm}=\begin{cases}1&(i=l,\,j=m,\,i\neq j)\\-1&(i=m,\,j=l,\,i\neq j)\end{cases}$$

再与等式右边对比即可。

---

**梯度**

梯度的第i个分量定义为 $(\nabla f)_i=\frac{\partial }{\partial x_i}f$

**散度**

散度定义为 $\nabla\cdot\mathrm{A}=\frac{\partial}{\partial x_i}A_i=\delta_{ij}\frac{\partial}{\partial x_i}A_j$

**旋度**

旋度的第i个分量定义为 $(\nabla\times\mathrm{A})_i=\epsilon_{ijk}\frac{\partial}{\partial x_j}A_k$

---

**用下标符号的一个方便之处是，之前的矢量乘法全部变成标量乘法了，而标量乘法是具有交换律的。**

有了这些准备，我们就可以开始证明了。

---

$$\nabla(fg)=f\nabla g+g\nabla f$$

证明： $[\nabla(fg)]_i=\frac{\partial }{\partial x_i}(fg)=g\frac{\partial }{\partial x_i}f+f\frac{\partial }{\partial x_i}g=(f\nabla g+g\nabla f)_i$

评论：其实就是对每个i都用了一遍乘法法则，但是只用一个式子就可以表达出来

---

$$\nabla\cdot(f\mathrm{A})=f\nabla\cdot\mathrm{A}+\nabla f\cdot \mathrm{A}$$

证明： $\nabla\cdot(f\mathrm{A})=\frac{\partial}{\partial x_i}(fA_i)=f\frac{\partial}{\partial x_i}A_i+A_i\frac{\partial}{\partial x_i}f=f\nabla\cdot\mathrm{A}+\nabla f\cdot \mathrm{A}$

评论： $fA_i$ 是一个标量，直接用标量的乘法法则即可。

---

$$\nabla\times(f\mathrm{A})=f\nabla\times\mathrm{A}+\nabla f\times\mathrm{A}$$

证明：

$$\begin{aligned} \left[\nabla\times(f\mathrm{A})\right]_i&=\epsilon_{ijk}\frac{\partial}{\partial x_j}(fA_k) \\&=\epsilon_{ijk}f\frac{\partial}{\partial x_j}A_k+\epsilon_{ijk}A_k\frac{\partial}{\partial x_j}f \\&=\left[f\nabla\times\mathrm{A}+\nabla f\times\mathrm{A} \right]_i\end{aligned}$$

评论：注意使用标量乘法的交换律。

---

$$\nabla\cdot(\mathrm{A}\times\mathrm{B})=\mathrm{B}\cdot(\nabla\times\mathrm{A})-\mathrm{A}\cdot(\nabla\times\mathrm{B})$$

证明：

$$\begin{aligned} \nabla\cdot(\mathrm{A}\times\mathrm{B})&=\frac{\partial}{\partial x_i}(\mathrm{A}\times\mathrm{B})_i \\&=\frac{\partial}{\partial x_i}(\epsilon_{ijk}A_jB_k) \\&=\epsilon_{ijk}\frac{\partial}{\partial x_i}(A_jB_k) \\&=B_k\epsilon_{ijk}\frac{\partial}{\partial x_i}A_j+\epsilon_{ijk}A_j\frac{\partial}{\partial x_i}B_k \\&=B_k\epsilon_{kij}\frac{\partial}{\partial x_i}A_j-\epsilon_{jik}A_j\frac{\partial}{\partial x_i}B_k \\&=\mathrm{B}\cdot(\nabla\times\mathrm{A})-\mathrm{A}\cdot(\nabla\times\mathrm{B})  \end{aligned}$$

评论：注意使用Levi-Civita符号的置换性质。 $ijk$ 和 $kij$ 的奇偶性相同，而 $ijk$ 和 $jik$ 的奇偶性相反。

---

$$\nabla(\mathrm{A}\cdot \mathrm{B})=\mathrm{A}\times(\nabla\times\mathrm{B})+(\mathrm{A}\cdot\nabla)\mathrm{B}+\mathrm{B}\times(\nabla\times\mathrm{A})+(\mathrm{B}\cdot\nabla)\mathrm{A}$$

证明：

$$\begin{aligned} [\nabla(\mathrm{A}\cdot \mathrm{B})]_i&=\frac{\partial }{\partial x_i}(\mathrm{A}\cdot\mathrm{B}) \\&=\frac{\partial }{\partial x_i}(A_jB_j) \\&=B_j\frac{\partial }{\partial x_i}A_j+A_j\frac{\partial }{\partial x_i}B_j \end{aligned}$$

证明到这里好像陷入了停滞，但是注意到结果中有旋度，这意味着我们需要凑出Levi-Civita符号，而我们前面推导过Levi-Civita符号与Kronecker delta的关系：

$$\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$$

因此，我们考虑插入两个Kronecker delta符号。先看上式第一项

$$\begin{aligned}  \end{aligned} \begin{aligned} B_j\frac{\partial }{\partial x_i}A_j&=\delta_{im}\delta_{jl}B_j\frac{\partial }{\partial x_m}A_l \\&=(\delta_{il}\delta_{jm}-\epsilon_{ijk}\epsilon_{klm})B_j\frac{\partial }{\partial x_m}A_l \\&=\delta_{il}\delta_{jm}B_j\frac{\partial }{\partial x_m}A_l-\epsilon_{ijk}\epsilon_{klm}B_j\frac{\partial }{\partial x_m}A_l \\&=B_j\frac{\partial }{\partial x_j}A_i-\epsilon_{ijk}B_j(\epsilon_{klm}\frac{\partial }{\partial x_m}A_l) \\&=\left[(\mathrm{B}\cdot\nabla)\mathrm{A}+\mathrm{B}\times(\nabla\times\mathrm{A})\right]_i \end{aligned}$$

对第二项同理，因此原式得证。

评论：需要灵活使用Kronecker delta的插入和消去规则。

---

$$\nabla\times(\mathrm{A}\times\mathrm{B})=\mathrm{A}(\nabla\cdot \mathrm{B})-\mathrm{B}(\nabla\cdot\mathrm{A})+(\mathrm{B}\cdot\nabla)\mathrm{A}-(\mathrm{A}\cdot\nabla)\mathrm{B}$$

证明：请读者完成。

提示：利用 $\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$ 。

---

$$\nabla\times(\nabla\times\mathrm{A})=\nabla(\nabla\cdot\mathrm{A})-(\nabla\cdot\nabla)\mathrm{A}$$

证明：请读者完成。

提示：利用 $\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$ 。

---

本文用到的工具是十分强大的（张量分析）。

通过使用张量符号，你可以处理具有更多下标的量，而不只是像矩阵那样只有两个。例如 levi-civita 就是个三阶张量，通过使用它，你可以将三阶行列式写成更紧凑的形式。当然，在数学上，张量并不是“有多个下标”这么简单，而是通过多重线性映射来定义的，这超出了本文的范围。

张量分析不仅可以用来证明这些矢量恒等式，还可以帮助你完成其他一些实际问题中的证明。例如：证明磁偶极子m在磁场中受力为 $\bm{F}=\nabla (\bm{m}\cdot\bm{B})$ 。

在更深入的物理理论中（例如广义相对论），张量是必不可少的语言。从电动力学开始熟悉张量吧！

---

注：张量是分协变和逆变的，前者使用下标，后者使用上标。但在欧几里得空间中，取标准正交基之后，二者是没有区别的（其实有区别，只不过它们之间有一个欧式度量诱导的同构），因此可以统一写成下标。

注：作为线性映射的矩阵是一阶协变一阶逆变张量，即 (1,1) 型张量，作为二次型的矩阵是二阶协变张量，即 (0,2) 型张量。

注：无论如何，你都不应该把一个三阶张量叫做一个三维矩阵。矩阵只能是二阶张量，并且二阶张量有很多良好的性质，因此矩阵在我们的心目中有着特殊的地位。
