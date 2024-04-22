---
title: "【量光实验杂谈·二】HBT实验测量SPDC多模压缩态的频谱关联与纯度"
date: 2024-02-05T00:12:16+08:00
draft: false
tags: ["量子光学"]
categories: ["量子信息"]
---

上篇我们说了在 HBT 实验中，用非光子数分辨的单光子探测器测量量子二阶关联函数的原理。

[https://zhuanlan.zhihu.com/p/679453473](https://zhuanlan.zhihu.com/p/679453473)  
这篇我们来看看量子二阶关联函数有什么用。除了老生常谈的用来区分【超泊松统计/泊松统计/亚泊松统计】以及区分【光子集聚/反集聚】以外，HBT 实验还可以用来测量多模压缩态的频谱纯度。

## SPDC 产生多模压缩态  
SPDC（Spontaneous Parametric Down-Conversion，自发参量下转换）是一种实验上用来产生关联光子对的方法。 将一束激光打到非线性晶体上，如果满足相位匹配条件，则会发生自发参量下转换过程。在这个过程中，一个泵浦光子被转化为两个频率相等的光子，分别称为信号光子（signal photon）和闲频光子（idler photon），且满足能量守恒和动量守恒。其哈密顿量如下：

$H = i\hbar g\,a^\dag\_s a^\dag\_i a\_p + h.c.$ 

其中 $g$ 代表作用强度。

当泵浦光很强，以至于其强度几乎不会被损耗的时候，我们可以只关注信号光子和闲频光子的子希尔伯特空间。此时哈密顿量为：

$H = i\hbar g \alpha\_p \,a^\dag\_s a^\dag\_i + h.c.$ 

不失一般性，令 $\alpha\_p$ 为实数，且令 $\chi=g\alpha\_p$ ，则有

$H = i\hbar \chi (a^\dag\_s a^\dag\_i - a\_sa\_i)$ 

实际上，由于泵浦作用的空间有限，动量会具有不确定性，在频谱上表现为具有一定线宽。此时哈密顿量如下：

$\begin{aligned} H=i\hbar \chi \int d\omega\_s d\omega\_i [f(\omega\_s,\omega\_i) a\_s^\dag(\omega\_s) a\_i^\dag(\omega\_i) -f^\*(\omega\_s,\omega\_i) a\_s(\omega\_s) a\_i(\omega\_i)] \end{aligned}$ 

现在我们用 $L^2(\mathbb{R^2})$ 的一组正交基函数（例如 Hermite 函数） $\{\varphi\_k\}\_{k\in \mathbb{N}}$ 将 $f(\omega\_s,\omega\_i)$ 展开：

$\begin{aligned} f(\omega\_s,\omega\_i)=\sum\_{k,l} C\_{kl}\varphi\_k(\omega\_s)\varphi\_l(\omega\_i) \end{aligned}$ 

并且记 $a\_k^\dag = \int d\omega\_s \,\varphi\_k(\omega\_s)a\_s^\dag(\omega\_s),\quad b\_k^\dag = \int d\omega\_i \,\varphi\_k(\omega\_i) a\_i^\dag(\omega\_i)$ ，则有

$\begin{aligned} H=i\hbar \chi \sum\_{k,l}\left( C\_{kl}a^\dag\_k b^\dag\_l - C^\*\_{kl} a\_kb\_l\right) \end{aligned}$ 

对其进行施密特分解（奇异值分解），得

$\begin{aligned} H=i\hbar \chi \sum\_{k}\left( \lambda\_k A^\dag\_k B^\dag\_k - \lambda\_k A\_k B\_k\right) \end{aligned}$ 

其中 $\sum\_k\lambda^2\_k=1$ 。


> 注意：由于奇异值分解的谱总是非负实数，所以 $\lambda\_k$ 是实数且大于零。

这其实就是多模压缩态的哈密顿量。


> 复习一下各种压缩态：  
> 单模压缩态： $\begin{aligned} H=i\hbar\left(g^\*\frac{a^2}{2}-g\frac{a^{\dag2}}{2}\right) \end{aligned}$   
> 双模压缩态： $\begin{aligned} H=i\hbar\left(g^\*a b-g a^\dag b^\dag\right) \end{aligned}$   
> 多模压缩态： $\begin{aligned} H=i\hbar\sum\_{k}\left(g\_k^\*a\_k b\_k-g\_k a\_k^\dag b\_k^\dag\right) \end{aligned}$ 

现在我们分别来看看薛定谔绘景与海森堡绘景下的系统演化。

在薛定谔绘景下，

$\begin{aligned} |\Psi\_{\text{out}}\rangle &=e^{\frac{H\tau}{i\hbar}}|\Psi\_{\text{in}}\rangle \\\\ &= \sum\_{k} \frac{1}{\cosh(r\_k)}\sum\_{n=0}^{\infty}\tanh^n(r\_k)|n\_k,n\_k\rangle \end{aligned}$ 

其中 $r\_k=\chi \tau \lambda\_k$ 。注意到它拥有热光场的形式。

当 $r\_k$ 很小时，有 

$|\Psi\_{\text{out}}\rangle\approx \sum\_{k} \left(|0\_k,0\_k\rangle + r\_k|1\_k,1\_k\rangle\right)$ 


> 这也是大多数实验所符合的情况。  
> 在探测到光子的前提下，条件量子态（Conditional State）为 $|\Psi\_\text{conditional}\rangle=\sum\_k\lambda\_k|1\_k,1\_k\rangle$ 。这就是预报式单光子源的原理。

在海森堡绘景下，

$\begin{aligned} A\_k &\rightarrow e^{\frac{H\tau}{i\hbar}} A\_k e^{-\frac{H\tau}{i\hbar}} \\\\ &= A\_k + [e^{\frac{H\tau}{i\hbar}},A\_k]+[e^{\frac{H\tau}{i\hbar}},[e^{\frac{H\tau}{i\hbar}},A\_k]] + \cdots \\\\ &=\cosh(r\_k) A\_k - \sinh(r\_k)B\_k^\dag \end{aligned}$ 

$\begin{aligned} B\_k &\rightarrow e^{\frac{H\tau}{i\hbar}} B\_k e^{-\frac{H\tau}{i\hbar}} \\\\ &= B\_k + [e^{\frac{H\tau}{i\hbar}},B\_k]+[e^{\frac{H\tau}{i\hbar}},[e^{\frac{H\tau}{i\hbar}},B\_k]] + \cdots \\\\ &=\cosh(r\_k) B\_k - \sinh(r\_k)A\_k^\dag \end{aligned}$ 

其中 $r\_k=\chi \tau \lambda\_k$ 。

## 如何刻画频谱关联？  
频谱关联指的是信号光子和闲频光子的频谱之间的关联。一个无关联的联合频谱可以写成两个光子各自频谱的乘积： $f(\omega\_s,\omega\_i)=\phi(\omega\_s)\psi(\omega\_i)$ 。如果不能写成这个形式，就意味着有频谱关联。

具体如何刻画频谱关联呢？我们可以用施密特数来刻画频谱的关联程度，其定义如下：

$\begin{aligned} K= \frac{1}{\sum\_k\lambda^4\_k} \end{aligned}$ 


> **例**  
> 对于无关联的联合频谱，有 $\{\lambda\_k\}=\{1\}$ ， $K=1$ 。  
> 对于有两个模式，且系数相等的联合频谱，有 $\{\lambda\_k\}=\{\frac{1}{2},\frac{1}{2}\}$ ， $K=2$ 。  
> 对于有 n 个模式，且系数相等的联合频谱，有 $K=n$ 。  
> 对于有 n 个模式，且系数彼此不完全相等的联合频谱，有 $1<K<n$ 。

为什么我们会关心频谱关联？这是因为它和光子的纯度有密切的关系：


> **性质**  
> 在 $r\_k$ 很小，且探测到光子的前提下，量子态为 $|\Psi\_\text{conditional}\rangle=\sum\_k\lambda\_k|1\_k,1\_k\rangle$ 。  
> 对于该量子态，将两个光子中的其中一个 trace 掉（做偏迹运算），剩下光子的量子态的纯度为 $P=\frac{1}{K}$ 。这是因为：  
> $\begin{aligned} P &= \operatorname{tr}[\operatorname{tr}\_2[|\psi\rangle\langle\psi|]^2] \\\\  &=  \operatorname{tr}\left[\operatorname{tr}\_B\left(\sum\_{k}\lambda\_k \left| 1\_k, 1\_k\right\rangle\sum\_{l}\lambda\_l \left\langle 1\_l ,1\_l\right|\right)^2\right] \\\\ &= \operatorname{tr}\left[\left(\sum\_{k}\lambda\_k^2 \left|1\_k \right\rangle\left\langle 1\_k\right|\right)^2\right] \\\\ &= \operatorname{tr}\left[\sum\_{k}\left(\lambda\_k^2\left| 1\_k \right\rangle\left\langle 1\_k\right|\right)^2\right] \\\\ &= \operatorname{tr}\left[\sum\_{k}\lambda\_k^4 |1\_k\rangle\langle 1\_k|\right] \\\\ &=\sum\_{k}\lambda\_k^4=\frac{1}{K} \end{aligned}$ 

可见，纯度与施密特数呈反比关系。也就是说，频谱关联越强，光子在频域上的纯度越低。这对预报式单光子源以及各种多光子干涉实验是不利的。对于前者，频谱关联会降低单光子的频域全同性，对于后者，频谱关联会降低干涉对比度。

## 用 HBT 实验测量频谱关联  
在上一篇中，我们说到 HBT 实验探测的是：

$\begin{aligned} \frac{C\_{12}R}{S\_1S\_2}=\frac{\langle n(n-1)\rangle}{\langle n\rangle^2} \end{aligned}$ 

其中 $C\_{12}$ 是两个探测器的符合计数率， $S\_1$ 和 $S\_2$ 分别是第一个和第二个探测器的计数率， $R$ 是光子通量。


> 当各个模式的频率相同或相近时，有 $\begin{aligned} \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} \approx g^{(2)}(0) \end{aligned}$ 。

我们之所以说用 HBT 实验可以测量频谱关联，是因为 $\begin{aligned} \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} = 1+\frac{1}{K} \end{aligned}$ 。证明如下：

$\begin{aligned} \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} &=\frac{\langle n^2\rangle-\langle n\rangle}{\langle n\rangle^2} \\\\ &=\frac{\sum\_{k} \langle n\_k^2 \rangle + 2\sum\_{i>j} \langle n\_i n\_j \rangle - \langle n\rangle}{\langle n\rangle^2} \\\\ &= \frac{ \sum\_{k} \left(\langle n\_k \rangle + 2\langle n\_k\rangle^2 \right) + 2\sum\_{i>j} \langle n\_i \rangle \langle n\_j \rangle  - \langle n\rangle}{\langle n\rangle^2} \\\\ &= \frac{\langle n\rangle + \langle n\rangle^2 +\sum\_{k} \langle n\_k\rangle^2 - \langle n\rangle}{\langle n\rangle^2} \\\\ &= 1+\frac{\sum\_{k} \langle n\_k\rangle^2}{ \left\langle \sum\_{k} n\_k\right\rangle^2} \\\\ &= 1 + \frac{\sum\_k \sinh^4(r\_k)}{\left(\sum\_k \sinh^2(r\_k)\right)^2} \\\\ &\approx 1+\frac{\sum\_k r\_k^4}{\left(\sum\_k r\_k^2\right)^2} \\\\ &= 1 + \frac{\sum\_k \lambda\_k^4}{\left(\sum\_k \lambda\_k^2\right)^2} \\\\ &= 1+\sum\_k \lambda\_k^4 \\\\ &= 1+\frac{1}{K} \\\\ &= 1+P \end{aligned}$ 

其中第三个等号用到了结论：对于热光场有 $ \langle n\_k^2 \rangle =\langle n\_k \rangle + 2\langle n\_k\rangle^2$ ，且各个模式之间没有关联 $\langle n\_i n\_j\rangle=\langle n\_i\rangle\langle n\_j\rangle$ 。

第六个等号是因为在海森堡绘景下有：

$\begin{aligned} \langle n\_k\rangle&=\langle 0|A\_k^\dag A\_k|0\rangle \\\\ &\rightarrow\langle 0| (\cosh(r\_k) A\_k^\dag - \sinh(r\_k)B\_k)(\cosh(r\_k) A\_k - \sinh(r\_k)B\_k^\dag)|0\rangle \\\\ &= \sinh^2(r\_k) \end{aligned}$ 

## 结论  
借助 HBT 实验，我们就能测量频谱关联和纯度，这不得不说是一件很神奇的事情。因为普通的方法需要用到 tunable filter 来测 JSI（Joint Spectral Intensity），再根据 JSI 计算频谱关联和纯度。而 HBT 实验甚至连 filter 都不需要，可见 HBT 实验的优越性。

## 注  
关于以上推导我能找到最早的文献是 [1]，但是文献 [1] 中跳了太多步骤，中间的逻辑链是我自己一点一点补上的。

利用 HBT 实验测频谱关联的文献见 [2] 和 [3]，它们引用的都是文献 [1]。

## 参考文献  
[1] Christ, A., Laiho, K., Eckstein, A., Cassemiro, K. N. & Silberhorn, C. Probing multimode squeezing with correlation functions. *New J. Phys.* **13**, 033027 (2011).

[2] Faruque, I. I. *et al.* Estimating the Indistinguishability of Heralded Single Photons Using Second-Order Correlation. *Phys. Rev. Applied* **12**, 054029 (2019).

[3] Paesani, S. *et al.* Near-ideal spontaneous photon sources in silicon quantum photonics. *Nat Commun* **11**, 2505 (2020).  
 