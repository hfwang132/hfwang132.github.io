---
title: "BCH 公式 - 量子力学爆算的大杀器"
date: 2024-03-07T20:59:38+08:00
draft: false
tags: ["量子光学"]
categories: ["数学物理方法"]
---

**Baker-Campbell-Hausdorff 公式** 可以用来计算海森堡表象下的算符演化：

$e^X Y e^{-X}=Y+[X,Y]+\frac{1}{2!}[X,[X,Y]]+\frac{1}{3!}[X,[X,[X,Y]]]+\cdots$ 


> 这个公式其实只是 BCH 公式的小弟

因为海森堡表象下的算符演化规则是 $A\rightarrow UAU^{\dag}$ ，其中 $U$ 是酉演化算符。

如果 $U$ 由 $H$ 生成，那么就是 $A\rightarrow e^{\frac{t}{i\hbar}H}Ae^{-\frac{t}{i\hbar}H}$ 了。


> **例 1：Phase Shifter（移相器）**  
> 哈密顿量为 $H=\varphi n$ ，湮灭算符 $a$ 的演化为：  
>  $\begin{aligned} e^{-i\varphi n} a e^{i\varphi n}&= a + i\varphi [n, a] - \frac{\varphi}{2!} [n,[n,a]] - \cdots \\\\ &= a (1+i\varphi -\frac{\varphi^2}{2!} - \cdots)\\\\ &= e^{i\varphi} a \end{aligned}$   
>   
> **例 2：Beam Splitter（分束器）**  
> 哈密顿量为 $H= \theta e^{i\varphi} a^{\dag}b + \theta e^{-i\varphi} a b^\dag$ ，演化如下：  
>  $\begin{aligned} e^{-iH} a e^{iH} &= \cos \theta \,a + i \sin\theta\, e^{i\varphi} b \\\\ e^{-iH} b e^{iH} &= i \sin\theta \,e^{-i\varphi} a  + \cos \theta \,b \end{aligned}$   
> 这就是熟悉的 Bogliubov Transformation  
>   
> 这俩例子感觉像是大炮打蚊子，下面来个有用点的：  
>   
> **例 3：Two-mode Squeezed State（双模压缩态）**  
> 哈密顿量为： $\begin{aligned} H=i\hbar\left(g^\*a b-g a^\dag b^\dag\right) \end{aligned}$   
>  $\begin{aligned} a &\rightarrow e^{\frac{H}{i\hbar}} a e^{-\frac{H}{i\hbar}} \\\\ &= a + \left[{\frac{H}{i\hbar}},a\right]+\left[{\frac{H}{i\hbar}},\left[{\frac{H}{i\hbar}},a\right]\right] + \cdots \\\\ &=\cosh(r) a - \sinh(r)e^{i\xi}b^\dag \end{aligned}$   
> 其中 $g = re^{i\xi}$ 。  
> 这个做 SPDC 和 OPO 的很熟。在薛定谔表象下计算反而很难，用海森堡表象加 BCH 公式则容易得多。  
>    
> **例 4：Rotated Quadratures**  
> 生成元是总粒子数 $N$ ，正则位置算符 $Q$ 和正则动量算符 $P$ 的演化为：  
>  $\begin{aligned} e^{i\theta N} Q e^{-i\theta N} = \cos \theta\, Q + i \sin \theta\, P \\\\ e^{i\theta N} P e^{-i\theta N} = i \sin \theta\, Q + \cos \theta P \end{aligned}$   
> 看起来就是把相空间旋转了一下。其实跟 Phase Shifter 差不多。  
> 这个变换在处理 Squeezed states 的时候比较有用。主要就是把坐标变换到 Squeezed Quadrature 上面去。

BCH 公式的一个小弟都这么有用了，那它的本尊岂不是更强大？！现在有请本尊：

$e^{X}e^{Y}=e^Z$ 

$Z=X+Y+{\frac {1}{2}}[X,Y]+{\frac {1}{12}}[X,[X,Y]]-{\frac {1}{12}}[Y,[X,Y]]+\cdots $ 

呃，好像有点不太好用的样子。

实际上我们更常用的是一种特殊情形，即 $[X,Y]$ 为常数的情形，此时 BCH 公式变成

$Z=X+Y+{\frac {1}{2}}[X,Y]$ 


> **例 5：Displacement Operator（平移算子）**  
>  $\begin{aligned} D(\alpha)&=e^{\alpha a^\dag-\alpha^\* a} \\\\ &=e^{-\frac{1}{2}|\alpha|^2}e^{\alpha a^\dag}e^{-\alpha^\* a} \\\\ &=e^{\frac{1}{2}|\alpha|^2}e^{-\alpha^\* a}e^{\alpha a^\dag} \end{aligned}$   
> 可见 BCH 公式允许我们在正规排序（产生算子在湮灭算子前面）和反正规排序之间灵活切换。  
> 实际上，平移算子本身既不是正规排序，也不是反正规排序，而是对称排序。  
>   
> **例 6：Weyl Operator（外尔算子）**  
>  $W(q,p) = e^{i(-qP+pQ)} = e^{\frac{i}{2}qp}U(q)V(p) = e^{-\frac{i}{2}qp}V(p)U(q)$   
> 其中 $U(q)=e^{-iqP}$ 是位置平移算子， $V(p)=e^{ipQ}$ 是动量平移算子。根据 BCH 公式，可以将它们解耦出来。  
> 这个 $W:\mathbb{R}^2\rightarrow \mathcal{L}(L^2(\mathbb{R}))$ 叫做 Weyl Representation。  
> 更一般地，Weyl Transformation 可以将一个经典相空间中的概率密度函数给量子化，变成一个密度算符，反过来，Wigner Transformation 可以将一个密度算符映射为一个相空间中的概率密度函数，这就是量子光学中的 Wigner Representation。  
>   
> **例 7：Glauber P-, Husimi Q- 与 Wigner Representation**  
> 一个密度算子 $\rho$ 的 Wigner 表示是其特征函数的傅里叶变换。  
> 特征函数： $\chi\_W(\lambda)=\operatorname{Tr}[\rho D(\lambda)]$ ，其中 $D(\lambda) = e^{\lambda a^\dag - \lambda a}$ 为平移算子。  
> Wigner 表示： $\begin{aligned} W(\alpha)=\frac{1}{\pi^2}\int \chi\_W(\lambda) e^{-(\lambda a^\* - \lambda^\*\alpha)} \mathrm{d}^2\alpha \end{aligned}$   
> 如果把特征函数改成正规排序和反正规排序，我们就能得到 Glauber P 表示和 Husimi Q 表示：  
> Glauber P 表示： $\begin{aligned} P(\alpha) = \int \operatorname{Tr}[\rho e^{\lambda a^\dag}e^{\lambda^\*a}] e^{-(\lambda \alpha^\* - \lambda^\* \alpha)} \mathrm{d}^2 \alpha \end{aligned}$   
> Husimi Q 表示： $\begin{aligned} Q(\alpha) = \int \operatorname{Tr}[\rho e^{\lambda^\*a}e^{\lambda a^\dag}] e^{-(\lambda \alpha^\* - \lambda^\* \alpha)} \mathrm{d}^2 \alpha \end{aligned}$   
> 这样一来，P 和 Q 有了简单的形式：  
>  $\begin{aligned} P&: \quad \rho = \int P(\alpha) |\alpha \rangle\langle \alpha | \mathrm{d}^2 \alpha \\\\ Q&:\quad Q(\alpha) = \frac{1}{\pi} \langle \alpha | \rho | \alpha \rangle \end{aligned}$   
> 好处是我们可以很方便地通过 P 和 Q 表示来计算正规排序算子和反正规排序算子的期望值：  
>  $\begin{aligned} \langle a^{\dag k} a^l\rangle &= \operatorname{Tr}[a^l \rho a^{\dag k}] \\\\ &= \operatorname{Tr}\left[\int P(\alpha) a^l |\alpha\rangle\langle \alpha | a^{\dag k} \mathrm{d}^2 \alpha\right] \\\\ &= \int \alpha^l \alpha^{\* k} P(\alpha) \mathrm{d}^2 \alpha \end{aligned}$   
>  $\begin{aligned} \langle  a^l a^{\dag k}\rangle &= \operatorname{Tr}[a^{\dag k} \rho a^l] \\\\ &= \frac{1}{\pi} \int \langle \alpha | a^{\dag k} \rho a^l | \alpha \rangle \mathrm{d}^2 \alpha \\\\ &= \int \alpha^l \alpha^{\* k} Q(\alpha) \mathrm{d}^2 \alpha \end{aligned}$   
> 然而经典物理量被量子化之后总是会得到对称排序的算子而不是正规或反正规排序的算子。所以最与经典力学对应的期望值应该是对称排序算子的期望值，即 $\langle S(a^l a^{\dag k})\rangle$ ，其中 $S$ 是对称排序算子。  
> 如果想计算 $\langle S(a^l a^{\dag k})\rangle$ ，就还得拿出 Wigner 表示：  
>  $\begin{aligned} \langle  S(a^l a^{\dag k})\rangle = \int \alpha^l \alpha^{\* k} W(\alpha) \mathrm{d}^2 \alpha \end{aligned}$   
> 根据 BCH 公式，这三种表示的特征函数之间只依次相差了一个 $e^{\frac{1}{2}|\lambda|^2}$ 。这引出了下列变换公式：  
>  $\begin{aligned} W(\alpha) &= \frac{2}{\pi} \int P(\lambda)e^{-2|\alpha-\lambda|^2}\mathrm{d}^2\lambda \\\\ Q(\alpha) &= \frac{2}{\pi} \int W(\lambda)e^{-2|\alpha-\lambda|^2}\mathrm{d}^2\lambda \\\\ Q(\alpha) &= \frac{1}{\pi}\int P(\lambda) e^{-|\alpha - \lambda|^2} \mathrm{d}^2 \lambda \end{aligned}$ 

