---
title: "激光的全量子理论"
date: 2024-07-19T01:07:36+08:00
draft: false
tags: ["量子光学"]
categories: ["量子信息"]
---

> 大部分介绍激光的资料都是以经典或半经典形式推导的。那么激光的全量子理论是什么样的呢？它又有什么用呢？

本文简要介绍激光的 Scully\-Lamb 理论，它是一个全量子的理论，由于一般量子光学教材的最后几章才会介绍，加上（半）经典的理论在大部分情况下也很好用，所以熟悉 Scully\-Lamb 理论的人并不多。

Scully\-Lamb 理论对泵浦强度低于或接近阈值时的光子数分布作出了更准确的预言，这是（半）经典理论所做不到的。

本文结构如下：

第一节介绍 Jaynes\-Cummings 模型，它负责处理光场与二能级系统的相互作用。

第二节介绍 Lindblad 主方程，它负责处理光场与热库的相互作用。

第三节推导 Scully\-Lamb 理论。它无非就是 Jaynes\-Cummings 模型和 Lindblad 主方程共同作用的结果。

为简明起见，本文设置 $\hbar = 1$ 。

## 1. Jaynes\-Cummings 模型（JCM）  
（熟悉 JCM 的可以跳过这一节）


> JCM 描述的是一个单模光场与一个二能级系统的耦合，由于它将光场也量子化了，因此是一个全量子模型。  
>   
> 除了光场量子化，JCM 还做了偶极矩近似（Dipole Approximation）和旋转波近似（Rotating\-Wave Approximation，RWA），以便于求解。这个过程不在本文介绍的范围内，请有兴趣的读者自行参阅教材和互联网资料。

记单模光场的希尔伯特空间为 $\mathcal{H} \cong L^{2}(\mathbb{R})$ ，二能级系统的希尔伯特空间为 $\mathcal{K} \cong \mathbb{C}^2$ ，则 Jaynes\-Cumming 哈密顿量 $H \in \mathcal{L}(\mathcal{H}\otimes \mathcal{K})$ 如下：

$\begin{aligned} H&= \underbrace{\omega \left(a^\dag a+\frac{1}{2}\right)}\_{\text{field}}+ \underbrace{\omega\_a \frac{\sigma\_z}{2}}\_{\text{atom}} +  \underbrace{\Omega(\sigma\_+ a + \sigma\_- a^{\dag})}\_{\text{atom-field coupling}} \\\\ &= \underbrace{\omega \left(a^\dag a+\frac{1}{2}+\frac{\sigma\_z}{2}\right)}\_{H\_0} + \underbrace{\frac{\Delta}{2} \sigma\_z + \Omega(\sigma\_+ a + \sigma\_- a^{\dag})}\_{H\_\text{I}} \end{aligned}$ 

其中 $a^\dag , a$ 是 $\mathcal{H}$ 上的产生和湮灭算符， $\sigma\_z, \sigma\_{\pm}$ 是 $\mathcal{K}$ 上的泡利 Z 算符和升降算符。 $\Omega$ 叫做拉比频率，它衡量了光场与二能级系统之间的耦合强度。

### 1.1 JCM 的对角化  
由于 $H\_0$ 只有对角项，我们可以从解中将它分离出来：令 $|\psi\rangle = e^{-\mathrm{i}H\_0t} |\psi\_\text{I}\rangle$ ，则有 $\mathrm{i} \frac{\mathrm{d}}{\mathrm{d}t}|\psi\_\text{I}\rangle = H\_\text{I}|\psi\_\text{I}\rangle$ 。因此我们只需要研究 $H\_\text{I}$ 即可。这个方法叫做相互作用表象（Interaction Picture）。

我们可以将 $H\_\text{I}$ 在光子数表象下展开：

$\begin{aligned} H\_\text{I} &= \color{gray}{  \begin{matrix} |g,0\rangle \\\\ |e,0\rangle \\\\ |g,1\rangle \\\\ |e,1\rangle \\\\ |g,2\rangle \\\\ \vdots \end{matrix} } \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & \cdots \\\\ 0 & 0 & 1 & 0 & 0 & \cdots \\\\ 0 & 1 & 0 & 0 & 0 & \cdots \\\\ 0 & 0 & 0 & 0 & \sqrt{2} & \cdots \\\\ 0 & 0 & 0 & \sqrt{2} & 0 & \cdots \\\\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix}\Omega+ \begin{bmatrix} -1 & 0 & 0 & 0 & 0 & \cdots \\\\ 0 & 1 & 0 & 0 & 0 & \cdots \\\\ 0 & 0 & -1 & 0 & 0 & \cdots \\\\ 0 & 0 & 0 & 1 & 0 & \cdots \\\\ 0 & 0 & 0 & 0 & -1 & \cdots \\\\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{bmatrix} \frac{\Delta}{2} \end{aligned} $ 

其中 $g,e$ 分别代表二能级系统的基态和激发态， $0,1,2,\cdots$ 代表光场的激发数（即光子数）。

它可以进一步写成：

$\begin{aligned} H\_\text{I} = \bigoplus\_{n=1}^\infty  \begin{bmatrix} \frac{\Delta}{2} & \Omega\sqrt{n} \\\\ \Omega\sqrt{n} & -\frac{\Delta}{2} \end{bmatrix} \end{aligned}$ 

其中 $n$ 代表总激发数，即二能级系统激发数和光场激发数（即光子数）的总和。

这个矩阵显然可以精确对角化，特征值为 $\pm \sqrt{\left(\frac{\Delta}{2}\right)^2 + n\Omega^2}$ 。记 $\Delta\_n =  \sqrt{\Delta^2 + 4n\Omega^2}$，则原表象（非相互作用表象）下的能级就是 $E\_{\pm,n} =  \omega \left(n + \frac{1}{2}\right) \pm \frac{\Delta\_n}{2}$ 。

这些能级上的本征态叫做缀饰态（dressed state）：

$\begin{aligned} |-,n\rangle &= \cos \theta\_n |e,n-1\rangle - \sin \theta\_n |g,n\rangle \\\\ |+,n\rangle &= \sin \theta\_n |e,n-1\rangle + \cos \theta\_n |g,n\rangle  \end{aligned}$ 

其中

$\begin{aligned} \cos \theta\_n &= \frac{2\sqrt{n}\Omega}{\sqrt{(\Delta\_n-\Delta)^2 + 4n\Omega^2}} \\\\ \sin \theta\_n &= \frac{\Delta\_n-\Delta}{\sqrt{(\Delta\_n-\Delta)^2 + 4n\Omega^2} }\end{aligned}$ 
  
  
### 1.2 JCM 下的光场演化  
由于我们最终只关心光场的量子态，我们会对原子部分取偏迹。设原子初态为 $|e\rangle\langle e|$ ，则经过时间 $\tau$ ，光场演化为

$\rho \rightarrow F(\tau) \rho := \text{tr}\_\text{a}[e^{-\mathrm{i}H \tau} (|e\rangle\langle e|\otimes \rho) e^{\mathrm{i}H\tau}]$ 

其中 $H$ 是 JCM 哈密顿量， $\text{tr}\_\text{a}$ 表示对原子系统取偏迹。

我们先来考察 $|n\rangle$ 经过 $F(\tau)$ 如何演化，即计算 $F(\tau)(|n\rangle\langle n|)$ ：

$\begin{aligned} |e,n\rangle &= \cos \theta\_n | -,n+1\rangle + \sin \theta\_n |+,n+1\rangle \\\\  e^{-\mathrm{i}H\tau} |e,n\rangle &= \cos \theta\_n e^{-\mathrm{i} \frac{\Delta\_{n+1}}{2}\tau} |-,n+1\rangle +  \sin \theta\_n e^{\mathrm{i} \frac{\Delta\_{n+1}}{2}\tau}|+,n+1\rangle \\\\ &= \cos \theta\_n e^{-\mathrm{i} \frac{\Delta\_{n+1}}{2}\tau}  (\cos \theta\_n |e,n\rangle - \sin \theta\_n |g,n + 1\rangle)\\\\&\phantom{=}+  \sin \theta\_n e^{\mathrm{i} \frac{\Delta\_{n+1}}{2}\tau}(\sin \theta\_n |e,n\rangle + \cos \theta\_n |g,n+1\rangle)  \\\\ &= C\_{e,n} |e,n\rangle + C\_{g, n+1} | g, n+1\rangle \\\\  \text{tr}\_\text{atom}[e^{-\mathrm{i}H\tau}|e,n\rangle\langle e,n|e^{\mathrm{i}H\tau}] &=|C\_{e,n}|^2 |n\rangle\langle n| + |C\_{g,n+1}|^2 |n+1\rangle\langle n+1| \end{aligned}$ 

其中

$\begin{aligned} C\_{e,n} &= \cos(\Delta\_{n+1} \tau /2) + \mathrm{i} \cos(2\theta\_n)\sin(\Delta\_{n+1} \tau/2)\\\\ C\_{g,n+1} &= \mathrm{i} \sin (2\theta\_n) \sin (\Delta\_{n+1} \tau/2) \end{aligned}$ 

假设光场的初态是一个光子数混态 $\rho = \sum\_n p\_n |n\rangle\langle n|$ ，则有

$\begin{aligned} F(\tau) \rho &= \sum\_n p\_n F(\tau)(|n\rangle\langle n|)\\\\ &= \sum\_n p\_n [|C\_{e,n}|^2 |n\rangle\langle n | + |C\_{g,n+1}|^2 |n+1\rangle\langle n+1|] \\\\ &= \sum\_n p\_n |C\_{e,n}|^2 |n\rangle\langle n | + \sum\_{n=1} p\_{n-1} |C\_{g,n}|^2 |n\rangle\langle n| \end{aligned}$ 

于是新的 $p\_n^\prime = \langle n|F(\tau) \rho |n\rangle$ 为

$\begin{aligned} \langle n|F(\tau) \rho |n\rangle &= |C\_{e,n}|^2 p\_n + |C\_{g,n}|^2 p\_{n-1} \\\\ &=: (1-C\_n) p\_n + C\_{n-1} p\_{n-1} \end{aligned}$ 

其中 $C\_n := |C\_{g,n+1}|^2 \Rightarrow 1-C\_n = |C\_{e,n}|^2$ 。

$\langle n|F(\tau) \rho |n\rangle$ 的表达式我们之后会用到。

另外还有 $C\_{n-1} = |C\_{g,n}|^2=\sin^2 (2\theta\_n) \sin^2 \left(\frac{\Delta\_{n}}{2} \tau\right) = \frac{4n\Omega^2}{4n\Omega^2+\Delta\_n^2} \sin^2 \left(\frac{\Delta\_{n}}{2}  \tau\right)$ ，这个结果之后也有用。


> 总结：本节求出了 Jaynes\-Cummings 模型的解析解。给定一个二能级原子与光场的耦合系统，其初态为 $\rho$ ，我们可以求出以后任意时刻的状态 $F(\tau) \rho$ 。特别地，我们写出了光场密度矩阵的对角项 $\langle n|F(\tau) \rho |n\rangle$ ，也就是演化后的光子数分布。

## 2. Lindblad 主方程  
对于封闭系统而言，量子态 $\rho$ 的演化遵循海森堡方程： $\frac{\mathrm{d}}{\mathrm{d}t} \rho = -\mathrm{i}[H,\rho]$ 。它其实就是薛定谔方程 $\frac{\mathrm{d}}{\mathrm{d}t}|\psi\rangle = -\mathrm{i}H|\psi\rangle$ 的统计叠加。这是一个酉（幺正，Unitary）的过程。

对于开放系统而言，量子态 $\rho$ 的演化不再是一个酉过程。当环境足够大以至于没有记忆性时，即当环境满足马尔科夫（Markovian）近似时，量子态的演化是一个保迹（trace preserving）且保完全正（complete positive）的量子通道（quantum channel）。可以证明此时 $\frac{\mathrm{d}}{\mathrm{d}t} \rho$ 的一般形式为：

$\begin{aligned} \frac{\mathrm{d}}{\mathrm{d}t} \rho = \mathcal{L}[\rho]= -\mathrm{i}[H,\rho] - \sum\_k \gamma\_k \left(\frac{1}{2} L\_k^\dag L\_k \rho - L\_k \rho L\_k^\dag + \frac{1}{2} \rho L\_k^\dag L\_k\right) \end{aligned}$ 


> 显然 $\frac{\mathrm{d}}{\mathrm{d} t} \text{tr}[\rho]=0$ ，所以它是保迹的。

这就是 Lindblad 主方程，其中 $\mathcal{L}$ 叫做 Lindbladian，可以看作 Hamiltonian 在开放系统下的推广。


> 有时它也叫 Liouvillian，但是 Liouvillian 更加 general 一些，例如它没有 complete positivity 的要求。  
>   
> Liouvillian 是哦系上指的是超算符 $\mathcal{B}(\mathcal{B}(\mathcal{H}))$ ，其中 $\mathcal{B}(\cdot)$ 代表 $\cdot$ 上的所有线性算符。超算符就是“算符的算符”。  
>   
> 在文献中，Liouvillian 和 Lindbladian 有时会混用。

当光场与一个平均光子数为 $\lambda$ 的热库耦合时，它遵循的 Lindblad 主方程为：

$\begin{aligned} \dot{\rho}=\mathcal{L}[\rho] = -\frac{\omega}{2Q}(\lambda +1)&(a^\dag a \rho - 2 a \rho a^\dag + \rho a^\dag a) \\\\ - \frac{\omega}{2Q}\lambda &(a a^\dag \rho - 2a^\dag \rho a+\rho a a^\dag) \end{aligned}$ 

在光学波段，由黑体辐射可知 $\lambda \approx 0$ ，则上式简化为：

$\begin{aligned} \dot{\rho}=\mathcal{L}[\rho] = -\frac{\omega}{2Q}&(a^\dag a \rho - 2 a \rho a^\dag + \rho a^\dag a) \end{aligned}$ 

它的对角项为

$\dot{p}\_n=\langle n | \mathcal{L}[\rho] | n \rangle = -\frac{\omega}{Q}(np\_n - (n+1)p\_{n+1}) $ 

该式的物理意义十分明显：能级 $|n\rangle\langle n|$ 弛豫到 $|n - 1\rangle\langle n -1|$ 的概率正比于 $np\_n$ 。

## 3. Scully\-Lamb 激光理论  
利用上述的 JCM 和 Lindbladian，我们就可以用全量子方式处理激光系统。


> 激光中有很多个原子，为什么不用多原子的 TCM（Tavis\-Cummings 模型），而是用单原子的 JCM？这是因为 TCM 是用来描述原子的集体行为的：当波长处于微波范围时，由于波长和共振腔的长度相近，所有原子会感受到同一个电磁场，这会导致超辐射（Superradiance）等现象。但是在光学波段（$10^{14} \sim 10^{15} \text{Hz}$）内，共振腔的长度远大于相干长度，使得各个原子独立地与光场进行相互作用。此时使用单原子的 JCM 就足够了，我们只要把 JCM 的解对于各个原子作平均即可。

在激光中有两个主要的物理过程：一是 JCM Hamiltonian 所描述的受激辐射过程，二是 Lindbladian 所描述的弛豫过程。我们只要把这两个过程结合起来就可以得到光场 $\rho$ 的演化方程：

$\dot{\rho} = -\mathrm{i}\,\text{tr}\_\text{a}[H,\rho\_\text{af}] + \mathcal{L}[\rho]$ 

其中 $H$ 是 JCM 哈密顿量， $\rho\_\text{af}$ 是原子和光场的整体量子态， $\text{tr}\_\text{a}$ 表示对原子系统取偏迹。

直接计算该方程[1]当然可以给出结果，但为了简化计算[2]，我们可以先考虑这两个过程的相对时间尺度。

### 3.1 时间尺度分析  
1. \*\*受激辐射\*\*：上能级和下能级的原子都可以通过自发辐射的方式退激发，平均寿命为纳秒量级（甚至皮秒量级）。即 JCM 所描述的相干过程的持续时间是\*\*纳秒到皮秒\*\*量级。换言之，在光场的演化 $\rho \rightarrow F(\tau) \rho := \text{tr}\_\text{a}[e^{-\mathrm{i}H \tau} (|e\rangle\langle e|\otimes \rho) e^{\mathrm{i}H\tau}]$ 中， $\tau$ 的平均值为纳秒到皮秒。
2. \*\*弛豫\*\*：光子在腔内来回反射，每次反射有一定概率损失掉。设反射率为 $99.9\%$ ，腔长为 30cm，则弛豫特征时间为 $1\text{ns}  \cdot \frac{\log 37 \%}{\log 99.9 \%} \approx 10^3 \text{ns}$ ，是\*\*微秒\*\*量级。换言之，在光场的演化 $\rho \rightarrow e^{t\_p \mathcal{L}} \rho$ 中， $t\_p$ 的平均值为微秒。

可见，Lindbladian 的作用时间远大于 JCM Hamiltonian 的作用时间。因此，我们可以进行\*\*粗粒度\*\*的分析，将两个过程分开讨论。

记 $\rho(t\_{i+1}) = e^{t\_p \mathcal{L}} F(\tau) \rho(t\_i)$ ，其中 $\tau \ll t\_p = t\_{i+1} - (t\_i + \tau) \approx t\_{i+1} - t\_i$ 。它表示在 $(t\_i,t\_i +\tau)$ 这段时间内，光场根据 JCM 演化；在 $(t\_i+\tau,t\_{i+1})$ 这段时间内，光场根据 Lindbladian 演化。

### 3.2 随机矩阵理论  
注意， $t\_p$ 和 $\tau$ 都是随机变量，因此我们还要对 $\rho(t\_{i+1}) = e^{t\_p \mathcal{L}} F(\tau) \rho(t\_i)$ 这个式子进行平均操作。


> 严格处理需要随机矩阵理论，但我们这里可以不用那么关心严格性。

我们先讨论 $t\_p$ 和 $\tau$ 所服从的概率分布：

1. 因为各个原子独立地与泵浦光相互作用，所以原子被泵浦到激发态的时间是完全随机的。这使得单位时间内的激发数服从泊松分布，且相邻两次激发的时间间隔服从指数分布，即 $p(t\_p) =R e^{-R t\_p}$ ，其中 $R$ 是泵浦速率。
2. 又因为自发辐射发生的时间也是完全随机的，所以 $\tau$ 也服从指数分布，即 $p(\tau) = \gamma e^{-\gamma \tau}$ ，其中 $\gamma^{-1}$ 是激发态的平均寿命。

我们先对 $t\_p$ 求平均：

$\begin{aligned} {\rho}(t\_{i+1}) &= \left[\int \mathrm{d}t\_pe^{-t\_pR}e^{t\_p \mathcal{L}} \right]F(\tau) \bar{\rho}(t\_i) \\\\ &= \ \frac{R}{R-\mathcal{L}} F(\tau) {\rho}(t\_i) \end{aligned}$ 

于是稳态解应满足：

$R[1-F(\tau)] {\rho} = \mathcal{L} \rho$ 

我们考虑上式的对角项，并代入第一节和第二节所得到的 $\langle n|F(\tau) \bar\rho | n\rangle$ 和 $\langle n | \mathcal{L} \bar\rho | n \rangle$ ，有：

$R[C\_n p\_n - C\_{n-1} p\_{n-1}] = -\frac{\omega}{Q}(np\_n - (n+1)p\_{n+1}) $ 

记 $S\_n = \frac{\omega}{Q}np\_n - RC\_{n-1} p\_{n-1}$ ，则有 $S\_n =S\_{n+1}$ ，为了使 $p\_n$ 收敛，我们需令 $S\_n=0$ ，于是有：

$p\_n = \frac{RQ}{n\omega}C\_{n-1} p\_{n-1} =\frac{RQ}{\omega} \frac{4\Omega^2}{4n\Omega^2+\Delta\_n^2} \sin^2 \left(\frac{\Delta\_{n}}{2}  \tau\right)p\_{n-1} $ 

现在我们来对 $\tau$ 求平均

$\begin{aligned} {p}\_n &=\frac{RQ}{\omega} \frac{4\Omega^2}{4n\Omega^2+\Delta\_n^2}\left[ \gamma\int\mathrm{d}\tau e^{-\gamma \tau} \sin^2 \left(\frac{\Delta\_{n}}{2}  \tau\right) \right] \bar{p}\_{n-1} \\\\ &= \frac{A}{B +k} {p}\_{n-1} \end{aligned}$ 

其中 $A = \frac{RQ}{2\omega}$ ， $B=\frac{\Delta^2 + \gamma^2}{4\Omega^2}$ 。

于是 $\begin{aligned} {p}\_n = {p}\_0 \prod\_{k=1}^n\frac{A}{B+k} \end{aligned}$ 。

在实际激光器中， $\Delta$ 和 $\Omega$ 的数量级接近，都为 MHz。而前面提到过， $\gamma^{-1}$ 的数量级为纳秒到皮秒，即 $\gamma$ 的数量级为 GHz 到 THz，因此 $B$ 是一个数量级为 $10^6 \sim 10^{12}$ 的常数。常数 $A$ 则取决于泵浦强度和共振腔的品质。


> 我们之所以只求 $\rho$ 的对角项的稳态解，是因为所有非对角项的稳态解都是零。因此当求出 $p\_n$ 后，我们就能直接写出量子态为 $\rho = \sum\_n p\_n |n\rangle\langle n|$ 。

### 3.3 结果分析：光子数分布  
当泵浦很弱时， $A\ll B$ ，此时 ${p}\_n \approx {p}\_0 \left(\frac{A}{B}\right)^n$ ，这是一个温度为 $T=\omega \left[\log\left(\frac{2\omega B}{RQ}\right)\right]^{-1}$ 的热分布。

当泵浦很强时， $A \gg B$ ，此时 ${p}\_n \approx {p}\_0 \frac{A^n}{n!}$ ，这是一个泊松分布。此时量子态为：

$\rho = e^{-A}\sum\_k \frac{A^{k}}{k!} |k\rangle\langle k |$ 

这是一个平均粒子数为 $A$ 的泊松分布。


> 在相干态表象下， $\rho$ 可以写成：  
>   
> $\rho = \int\_0^{2\pi} \frac{\mathrm{d}\theta}{2\pi} |\alpha e^{\mathrm{i}\theta}\rangle\langle\alpha e^{\mathrm{i}\theta}|,\quad A=|\alpha|^2$   
>   
> 可见它其实是一个相位随机的相干态。相干态 $|\alpha\rangle$ 对应一个振幅和相位都非常确定的经典电磁波，而这里将它的相位从 $0$ 到 $2\pi$ 积分了，这表现了我们对相位信息的无知，这种无知从根本上来源于我们对二能级系统（增益介质）的微观状态的无知。可以说这个 $\rho = \rho\_{\text{epistemic}}$ 是认识论的量子态。  
>   
> 而从本体论的角度而言，系统的量子态应当坍缩为一个有确定相位的 $\rho\_{\text{ontic}} = |\alpha\rangle$ ，只是我们没办法知道是哪个相位而已。这是因为在光学频率 $\sim 10^{15} \text{Hz}$ 下，人类无法观测绝对相位。不过，相对相位可以观测，因此我们仍能观察到干涉现象。简单的计算也可以看出这一点：无论是用混态 $\rho = \int\_0^{2\pi} \frac{\mathrm{d}\theta}{2\pi} |\alpha e^{\mathrm{i}\theta}\rangle\langle\alpha e^{\mathrm{i}\theta}|$ 还是用纯态 $\rho = |\alpha\rangle\langle \alpha|$ 去计算关联函数 $\langle a^\dag(t)a(0)\rangle = \text{tr}[\rho a^\dag(t)a(0)]$ ，计算结果都不会有任何区别。这一度引起了关于相干现象的讨论：相干到底是一种幻觉，还是一种物理实在？ [3]前者的支持者认为上文的“相位坍缩”诠释存在“preferred basis”的问题，不过这个问题可以认为已经被解决了：相干态是在激光腔开放系统下寿命最长的态。

当泵浦数量级与阈值相当时，有精确解 ${p}\_n = p\_0 \frac{B! A^n}{(n+B)!}$ 。此时我们来看看它是超泊松还是亚泊松分布。

$\langle n \rangle = \sum\_n np\_n = A - B + Bp\_0$ 

$\langle n^2\rangle = \langle n \rangle^2 + A$ 

此时 $g^{(2)}(0) = \frac{\langle n(n-1)\rangle}{\langle n\rangle^2} = 1 + \frac{B(1-p\_0)}{[A-B(1-p\_0)]^2} > 1$ 

可见当泵浦不强时，光子数分布实际上是超泊松分布。当泵浦越来越强时， $g^{(2)}(0) \rightarrow 1$ ，趋于泊松分布。如此精细的预言是半经典理论所做不到的。

### 3.4 结果分析：自然线宽  
在薛定谔表象下，量子态 $\rho$ 的演化为 $\mathrm{d}\rho = -\mathrm{i}\,\text{tr}\_\text{a}[H,\rho\_\text{af}]\mathrm{d}\tau+ \mathcal{L}[\rho]\mathrm{d}t\_p$ ，而在海森堡表象下，算符的演化就是它的对偶 channel：

$ \mathrm{d}{R} = \mathrm{i}\,\text{tr}\_\text{a}[H,R]\mathrm{d}\tau + \mathcal{L}^\*[R] \mathrm{d}t\_p$ 

其中 $\begin{aligned} \mathcal{L}^\*[R]= -\frac{\omega}{2Q}&(a^\dag a R- 2 a^\dag R a + R a^\dag a) \end{aligned}$ 。

令 $R = a$ 得：

$\begin{aligned} \mathrm{d}{a} &= -\mathrm{i} \omega a \mathrm{d}\tau - \frac{\omega}{2Q} a \mathrm{d}t\_p \end{aligned}$ 

由 $\gamma \mathrm{d}\tau = R\mathrm{d}t\_p$ 得

$\begin{aligned} \dot{a} &= \frac{\mathrm{d}a}{\mathrm{d}\tau} = -\mathrm{i} \omega a - \frac{\omega}{2Q} \frac{\gamma}{R}a\end{aligned}$ 

解得 $a(t ) =a(0) e^{-\mathrm{i}\omega t} e^{-\frac{\omega\gamma}{2RQ}t}, \quad a>0$ 。

其一阶关联函数为：

$\begin{aligned} g^{(1)}(t>0)&=\langle a^\dag(t) a(0)\rangle / \langle a^\dag(0) a(0)\rangle \\\\ &= \text{tr}[a(0) \rho a^\dag(t)] / \text{tr}[a(0) \rho a^\dag(0)] \\\\ &= e^{-\mathrm{i}\omega t} e^{-\frac{\omega\gamma}{2RQ}t} \end{aligned}$ 

时间平移不变性要求 $g^{(1)}(t) = g^{(1)}(-t)$ ，所以

$\begin{aligned} g^{(1)}(t)= e^{-\mathrm{i}\omega t} e^{-\frac{\omega\gamma}{2RQ}|t|} \end{aligned}$ 

对其进行傅里叶变换即可得到频谱：

$\begin{aligned} F(\omega^\prime) = \frac{\frac{\omega\gamma}{2RQ}}{(\omega^\prime-\omega)^2 + \left(\frac{\omega\gamma}{2RQ}\right)^2} \end{aligned}$ 

这是一个洛伦兹线形，其半高全宽（FWHM）为 $\Delta \omega = \frac{\omega\gamma}{RQ} = \frac{2\gamma}{A}$ 。


> 可见自然线宽取决于上能级和下能级的平均寿命 $\gamma^{-1}$ 。这是很符合直觉的，因为上下能级的寿命决定受激辐射的相干作用时间。  
> 另外，泵浦越强，自然线宽越窄。这也是符合直觉的，因为泵浦越强，两次受激辐射过程的时间间隔越短，于是弛豫的作用时间也越短。

## 参考  
1. Marlan O. Scully \& M. Suhail Zubairy, Quantum Optics
2. Pierre Meystre \& Murray Sargent, Elements of Quantum Optics
3. Bartlett, S. D., Rudolph, T. \& Spekkens, R. W. Dialogue Concerning Two Views on Quantum Coherence: Factist and Fictionist. Int. J. Quantum Inform. 04, 17–43 (2006\).
