---
title: "电磁波是光子的概率波吗？"
date: 2025-10-12T20:30:00+08:00
draft: false
tags: ["电磁波", "光子"]
categories: ["量子光学"]
---

## 概率场 vs 量子场  

电磁场不是光子的概率场，正如狄拉克场不是电子的概率场。

**概率场**只对非相对论情形下的单粒子态适用。而**电磁场**和**狄拉克场**属于**量子场**，要放到量子场论的框架下去讨论。

虽然狄拉克场不是电子的概率场，但在低速和单电子近似下，狄拉克方程的确可以退化成薛定谔方程，此时狄拉克场的第一个旋量分量就是电子的概率场，也就是薛定谔波函数。见附录 1。

光子能不能这样搞呢？很遗憾不能，因为光子本身就是个相对论粒子，无法直接考虑低速极限。

不过，如果用腔赋予光子等效质量，再考虑低速极限，那么电磁场还真能看成薛定谔意义上的概率场 [1]。不过这只是一种等效而已。

虽然不能直接考虑低速极限，但还是可以考虑单光子情形。此时的确可以定义一个和电磁场有关的概率分布。但这个概率分布不像薛定谔波函数那样有良好的性质，例如守恒的概率流。详见下文。

总之要记住：概率场不是基本实体。量子场才是基本实体，而概率场只是量子场在非相对论和单粒子情形下的近似而已。

> 概率场就是非相对论量子力学中所说的波函数。有时候人们也把量子场叫做波函数，不推荐这么说，容易和概率场混淆。

下面我们回答两个问题：

1. 既然电磁场不是光子的概率场，那么探测到光子的概率如何计算？
2. 既然电磁场不是光子的概率场，那么电磁场究竟是什么？

---

## 如何计算探测到光子的概率  

问题 1： 既然电磁场不是概率场，那么，探测到光子的概率如何计算？

正确的问法应该是：光场的量子态的初态 $|i\rangle$ 从 $t$ 到 $t+\mathrm{d}t$ 这段时间在 $\mathbf{r}$ 处被探测（吸收）一个光子变成终态 $|f\rangle$ 的概率 $w(\mathbf{r},t) \mathrm{d}t$ 是多少？Glauber 的光探测理论 [2] 告诉我们答案是：

$\begin{aligned} w(\mathbf{r},t) \propto |\langle f | E^{(+)}(\mathbf{r},t)| i\rangle|^2 \end{aligned}$

其中 $E^{(+)}$ 是电场湮灭算符： $E^{(+)}(\mathbf{r},t)=\sum\_\mathbf{k,\sigma} \mathcal{E}\_\mathbf{k}a\_\mathbf{k,\sigma}e^{\mathrm{i}(\mathbf{k}\cdot \mathbf{r}-\omega\_\mathbf{k} t)}$ ，其中 $\sigma = 0,1$ 代表偏振， $a\_{\mathbf{k},\sigma}$ 是模式 $(\mathbf{k},\sigma)$ 上的湮灭算符， $\mathcal{E}\_\mathbf{k}=\sqrt{\frac{\hbar \omega\_\mathbf{k}}{\epsilon\_0 V}}$ 是单光子振幅，有电场量纲， $V$ 为光场模式体积。

> 至于为什么概率正比于 $\begin{aligned} |\langle f | E^{(+)}(\mathbf{r},t)| i\rangle|^2 \end{aligned}$ ，以及正比的比例常数是什么，就要将探测器（通常是一个原子）本身的动力学考虑进来，并且使用完整的量子场论方法了。此处不再赘述（hand-wavingly）。

然而，在探测光子时，我们通常不知道终态是什么，而是只知道探测到了一个光子。因此我们需要对终态 $|f\rangle$ 进行求和：

$\begin{aligned} \sum\_f|\langle f | E^{(+)}(\mathbf{r},t)| i\rangle|^2 &= \sum\_f\langle i | E^{(-)}|f\rangle \langle f| E^{(+)} |  i\rangle \\\\ &= \langle i|E^{(-)}E^{(+)}|i\rangle  \end{aligned}$

所以，光场的量子态的初态 $|i\rangle$ 从 $t$ 到 $t+\mathrm{d}t$ 这段时间在 $\mathbf{r}$ 处被探测（吸收）一个光子变成终态 $|f\rangle$ 的概率为 $w(\mathbf{r},t) \propto \langle i|E^{(-)}E^{(+)}|i\rangle $ 。

可见， $\langle E^{(-)}E^{(+)}\rangle $ 是最接近概率分布的场。然而，它仍然不满足概率分布的性质。这是因为光子数不守恒，导致对其进行标准化存在困难。

> 为什么是电场 $E^{(\pm)}$ 不是磁场 $B^{(\pm)}$ ？因为光子被吸收通常是借助与原子的电偶极相互作用来完成的。不过，由于这里说的是正比，所以用 $B^{(\pm)}$ 乃至矢势 $A^{(\pm)}$ 都可以，这是因为横场（transverse field）部分 $A^{(\pm)},E^{(\pm)},B^{(\pm)}$ 总是成正比的，而偶极相互作用只有横场部分有贡献。

既然光子数不守恒导致无法标准化，那我们能不能人为限制光子数呢？答案是可以。我们可以限制光子数量为一个，且单光子态为：

$|1\_\psi\rangle = \sum\_{\mathbf{k},\sigma} \psi\_\mathbf{k,\sigma}|1\_\mathbf{k,\sigma}\rangle = \sum\_\mathbf{k,\sigma} \psi\_\mathbf{k,\sigma} a^\dagger\_\mathbf{k,\sigma} |0\rangle$

其中 $\sum\_{\mathbf{k},\sigma} |\psi\_\mathbf{k,\sigma}|^2 = 1$ 。

于是可以定义一个类似于波函数的东西 [3]：

$\psi(\mathbf{r},t) = \langle 0 | E^{(+)}(\mathbf{r},t) | 1\_\psi\rangle$

此时在某个区域 $D$ 中探测到一个光子的概率就正比于 $\int\_D |\psi(\mathbf{r})|^2 \mathrm{d}^3 \mathbf{r}$ 。因为：

$\begin{aligned} \int\_D |\psi(\mathbf{r})|^2 \mathrm{d}^3 \mathbf{r} &= \langle 1\_\psi | E^{(-)}(\mathbf{r}) | 0\rangle\langle 0 | E^{(+)}(\mathbf{r}) | 1\_\psi\rangle \\\\ &=  \langle 1\_\psi | E^{(-)}(\mathbf{r}) E^{(+)}(\mathbf{r}) | 1\_\psi\rangle \end{aligned}$

> 第二个等号是因为 $E^{(-)}$ 湮灭一个光子，导致 $ E^{(+)}(\mathbf{r}) | 1\_\psi\rangle$ 正比于 $|0\rangle$ 。

为了让 $\psi(\mathbf{r},t)$ 成为真正的概率分布，我们还要标准化消去量纲。我们不妨先展开 $\psi(\mathbf{r},t)$ ：

$\begin{aligned} \psi(\mathbf{r},t) &= \langle 0 | E^{(+)}(\mathbf{r},t) | 1\_\psi\rangle \\\\ &= \left\langle 0 \left| \sum\_\mathbf{k,\sigma} \mathcal{E}\_\mathbf{k}a\_\mathbf{k,\sigma}e^{\mathrm{i}(\mathbf{k}\cdot \mathbf{r}-\omega\_\mathbf{k} t)} \psi\_\mathbf{k,\sigma} a^\dagger\_\mathbf{k,\sigma} \right| 0 \right\rangle \\\\ &=  \sum\_\mathbf{k,\sigma} \mathcal{E}\_\mathbf{k}e^{\mathrm{i}(\mathbf{k}\cdot \mathbf{r}-\omega\_\mathbf{k} t)} \psi\_\mathbf{k,\sigma}  \end{aligned}$

其中 $\mathcal{E}\_\mathbf{k}$ 携带电场量纲。我们只要把它去掉就可以得到无量纲的单光子概率分布：

$\psi^\prime(\mathbf{r},t) = \sum\_\mathbf{k,\sigma} e^{\mathrm{i}(\mathbf{k}\cdot \mathbf{r}-\omega\_\mathbf{k} t)} \psi\_\mathbf{k,\sigma} $

在自由空间中，可将求和号 $\sum\_{\mathbf{k}}$ 换成积分号 $\int \frac{\mathrm{d}^3\mathbf{k}}{(2\pi)^3}$ 。

$\psi^\prime(\mathbf{r},t) = \sum\_\sigma \int \frac{\mathrm{d}^3\mathbf{k}}{(2\pi)^3} e^{\mathrm{i}(\mathbf{k}\cdot \mathbf{r}-\omega\_\mathbf{k} t)} \psi\_\mathbf{k,\sigma} $

然而，这个 $\psi^\prime(\mathbf{r},t)$ 只适用于单光子子空间。由于光子数通常不守恒，所以它的应用场景很有限。另外，它也无法像薛定谔波函数那样定义出一个守恒的概率流。

## 电磁场究竟是什么  

问题 2：既然电磁场不是概率场，那么电磁场究竟是什么？

电磁场本质上就是量子场论中的光子场 $A\_\mu$ ，而光子场和其他各种粒子的场 $\psi$ （狄拉克场、胶子场、夸克场...）一样，都是量子场。

至于量子场是什么，就要到量子场论中去寻找答案了。鉴于本文不是量子场论教材，就辛苦读者自己去翻阅了。

> 有些人可能会说：电磁场明明就是一个经典的场！你凭什么说它是量子场？对此我只能说你 too young too simple。这就和你说电子是一个经典的小球一样——当你没学量子力学的时候，你会认为所有粒子都是经典粒子；当你没学量子场论的时候，你会认为所有场都是经典场。其实，一切都是量子的，只不过很多时候没有表现出量子性而已。  
>   
> 电磁场什么时候表现出量子性？Lamb shift，Casimir effect，自发辐射...在很多现象里电磁场都表现出了量子性。猫态，GKP 态...这些振幅和相位的叠加态更是量子电磁场的直接体现。  
>   
> 之所以宏观电磁波没有表现出量子性，是因为光子很容易损耗（吸收/散射），对应的 Lindblad 算符是湮灭算符。开放系统的指针态是 Lindblad 算符的本征态，而湮灭算符的本征态正是相干态（Coherent state），它有明确的振幅和相位，且量子不确定性远小于自身。这就是为什么生活中的电磁波都是经典的：因为经典电磁波可以从损耗中存活下来。

## 附录 1 狄拉克方程如何近似成薛定谔方程 / 量子场如何近似成概率场  
> 狄拉克方程  
> $\mathrm{i}\gamma^\mu D\_\mu \psi - m\psi=0$ ，  
> 其中  
> $\gamma^0 = \begin{bmatrix} I & 0 \\\\ 0 &-I \end{bmatrix},\  \gamma^i=\begin{bmatrix} 0 & \sigma^i \\\\ -\sigma^i & 0 \end{bmatrix} \quad(i=1,2,3)$   
> $\sigma^i $ 是泡利矩阵，  
> 以及 $\psi = \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix}$ ，其中 $\psi\_1 = \begin{bmatrix}\psi\_{1\uparrow} \\\\ \psi\_{1\downarrow}\end{bmatrix}$ 是电子的两个自旋分量， $\psi\_2 = \begin{bmatrix}\psi\_{2\uparrow} \\\\ \psi\_{2\downarrow}\end{bmatrix}$ 是正电子的两个自旋分量。  
> 代入狄拉克方程得：  
> $\mathrm{i}\begin{bmatrix} I & 0 \\\\ 0 &-I \end{bmatrix} D\_t \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix} + \mathrm{i} \begin{bmatrix} 0 & \bm\sigma \cdot \mathbf{D} \\\\ -\bm\sigma \cdot \mathbf{D} & 0 \end{bmatrix} \begin{bmatrix}\psi\_1 \\\\ \psi\_2 \end{bmatrix} -m \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix}=0$   
> 其中 $D\_t =  \partial\_t +\mathrm{i}eA\_0 = \partial\_t - \mathrm{i}e\phi$ ， $\mathbf{D} = \nabla +\mathrm{i}e\mathbf{A}$ （使用 $(-,+,+,+)$ 度规约定）。  
> 化简得  
> $\mathrm{i} \begin{bmatrix}D\_t\psi\_1 \\\\ -D\_t\psi\_2\end{bmatrix} +\mathrm{i} \begin{bmatrix}\bm\sigma\cdot \mathbf{D} \psi\_2 \\\\ -\bm\sigma\cdot \mathbf{D}\psi\_1\end{bmatrix} -m \begin{bmatrix}\psi\_1 \\\\ \psi\_2\end{bmatrix}=0$   
> 即  
> $\boxed{ \begin{aligned} \mathrm{i} D\_t \psi\_1 + \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi\_2 - m\psi\_1 &= 0 \\\\ -\mathrm{i} D\_t \psi\_2 - \mathrm{i} \bm\sigma \cdot \mathbf{D} \psi\_1 - m\psi\_2 &= 0 \end{aligned}  }\quad (\star)$   
> 这就是狄拉克方程的展开形式：我们把电子项 $\psi\_1$ 和正电子项 $\psi\_2$ 写成两个方程。原来它们在同一个方程里。  
> 在低能情形下不考虑电子静质量带来的相位变化 $\mathrm{e}^{-\mathrm{i}mt}$ ，因此把它分离出来，也就是把 $\psi = \begin{bmatrix}\psi\_1\\\\ \psi\_2\end{bmatrix}$ 换成 $\psi = \begin{bmatrix}\varphi \mathrm{e}^{-\mathrm{i}mt}\\\\ \chi  \mathrm{e}^{-\mathrm{i}mt}\end{bmatrix}$ ，代入展开后的狄拉克方程 $(\star)$ 得：  
> $\begin{aligned} &\mathrm{i} D\_t \varphi + \mathrm{i} \bm\sigma \cdot \mathbf{D} \chi  = 0 &(1)\\\\ -&\mathrm{i} D\_t \chi - \mathrm{i} \bm\sigma \cdot \mathbf{D} \varphi - 2m\chi = 0 &(2) \end{aligned}$   
> 由于低能情形下正电子项 $\chi$ 很小，所以 $D\_t \chi \approx 0$ ，代入 $(2)$ 得：  
> $\chi \approx - \frac{\mathrm{i}}{2m} \bm\sigma \cdot \mathbf{D} \varphi$   
> 将其再代入 $(1)$ 得：  
> $\mathrm{i} D\_t \varphi +  \frac{1}{2m}(\bm\sigma \cdot \mathbf{D})^2 \varphi = 0 $   
> 可以证明（见附录 2）  
> $\begin{aligned} (\bm \sigma \cdot \mathbf{D})^2 &=\mathbf{D}^2 - \mathrm{i}e \bm\sigma\cdot \mathbf{B} \\\\ &= (\nabla +\mathrm{i}e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B} \\\\ &= -(\mathbf{p} + e\mathbf{A})^2 - e \bm\sigma\cdot \mathbf{B}  \end{aligned}$   
> 所以  
> $\mathrm{i} D\_t \varphi =  \frac{1}{2m}[(\mathbf{p} + e\mathbf{A})^2 + e \bm\sigma\cdot \mathbf{B} ] \varphi$   
> 把 $D\_t = \partial\_t - \mathrm{i}e\phi$ 代入得  
> $\boxed{ \mathrm{i} \partial\_t \varphi =  \left[\frac{1}{2m}(\mathbf{p} + e\mathbf{A})^2+ \frac{e}{2m} \bm\sigma\cdot \mathbf{B}  - e\phi  \right]\varphi }$   
> 这就是（带自旋的）电子的薛定谔方程，也叫做泡利方程。注意此处 $e$ 是正数，而电子 $\varphi$ 带负电荷。  
> 这里的 $\varphi$ 就是概率场，也就是非相对论量子力学中说的波函数。

## 附录 2  

证明 $(\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B}$ ，其中 $\mathbf{D} = \nabla+ \mathrm{i}e\mathbf{A}$ 。

> 根据恒等式  
>   
> $(\bm\sigma \cdot \mathbf{a})(\bm\sigma \cdot \mathbf{b}) = \mathbf{a} \cdot \mathbf{b} + \mathrm{i}\bm\sigma \cdot(\mathbf{a}\times\mathbf{b})$  
>   
> 得  
>   
> $(\bm\sigma \cdot \mathbf{D})^2 = \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D})$  
>   
> 于是我们需要计算 $(\mathbf{D}\times\mathbf{D})$ 。  
>   
> 我们先计算 $[D\_i, D\_j]$ ：  
>   
> $\begin{aligned} [D\_i, D\_j] &= [\partial\_i +\mathrm{i}eA\_i, \partial\_j +\mathrm{i}eA\_j] \\\\ &= \cancel{[\partial\_i,\partial\_j]} + \cancel{e^2[A\_i, A\_j]} + \mathrm{i}e[\partial\_i, A\_j] - \mathrm{i}e[\partial\_j,A\_i] \end{aligned}$  
>   
> 于是我们需要计算 $[\partial\_i, A\_j]$ ：  
>   
> $\begin{aligned} [\partial\_i, A\_j] f &= \partial\_i (A\_j f) -A\_j \partial\_i f \\\\ &= (\partial\_i A\_j) f + A\_j \partial\_if - A\_j \partial\_i f \\\\ &= (\partial\_iA\_j)f \end{aligned}$  
>   
> 所以 $[\partial\_i, A\_j] = (\partial\_i A\_j)$ 。  
>   
> 于是  
>   
> $\begin{aligned} [D\_i, D\_j] &= \mathrm{i}e[\partial\_i, A\_j] -\mathrm{i}e[\partial\_j,A\_i] \\\\ &= \mathrm{i}e (\partial\_i A\_j - \partial\_j A\_i) \\\\ &= \mathrm{i}e \epsilon\_{ijk}B^k \end{aligned}$  
>   
> 于是  
>   
> $\begin{aligned} (\mathbf{D}\times\mathbf{D})^k &=\epsilon^{kij} D\_i D\_j \\\\ &= \frac{1}{2} \epsilon^{kij}[D\_i,D\_j] \\\\ &= \frac{\mathrm{i}e}{2} \epsilon^{kij} \epsilon\_{ijl} B^l \\\\ &= \frac{\mathrm{i}e}{2} (\delta^k\_l \delta^j\_j - \delta^k\_j\delta^j\_l) B^l \\\\ &=\mathrm{i}e \delta^k\_l B^l \\\\ &= \mathrm{i}eB^k \end{aligned}$  
>   
> 所以 $\mathbf{D}\times \mathbf{D} = \mathrm{i}e\mathbf{B}$ 。  
>   
> 于是  
>   
> $\begin{aligned} (\bm\sigma \cdot \mathbf{D})^2 &= \mathbf{D}^2 +\mathrm{i} \bm\sigma\cdot (\mathbf{D} \times \mathbf{D}) \\\\ &= \mathbf{D}^2 - e \bm\sigma\cdot \mathbf{B} \end{aligned}$  
>   
> 证毕。

## 参考  

1. [1]Sharoglazova, V., Puplauskis, M., Mattschas, C. et al. Energy–speed relationship of quantum particles challenges Bohmian mechanics. Nature 643, 67–72 (2025). [https://www.nature.com/articles/s41586-025-09099-4](https://www.nature.com/articles/s41586-025-09099-4)
2. [2]Scully, M.O. and Zubairy, M.S. (1997) Quantum Optics. Cambridge University Press, Cambridge. http://dx.doi.org/10.1017/CBO9780511813993
3. [3] arXiv:quant-ph/0508202 [https://arxiv.org/pdf/quant-ph/0508202](https://arxiv.org/pdf/quant-ph/0508202)