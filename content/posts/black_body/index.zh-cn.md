---
title: "黑体辐射的推导（无废话版）"
date: 2024-07-27T15:50:09+08:00
draft: false
tags: ["量子光学"]
categories: ["量子信息"]
---


闲来无事，复习一下黑体辐射吧\~

很多讲黑体辐射的文章都要一上来就跟你讲一大段历史，很容易看迷糊。

本文单刀直入，直接闭嘴计算。

## 1. 黑体辐射公式是什么  
黑体辐射公式指的是一个黑体在单位频率中所辐射的能量密度。

要计算黑体辐射公式，就要计算从 $\nu$ 到 $\nu + \mathrm{d}\nu$ 之间有多少个态，以及每个态上有多少个光子，再将它们乘以光子的能量 $h\nu$ 。

$\varepsilon(\nu) \mathrm{d} \nu = [(\nu,\nu+\mathrm{d}\nu) 中有多少个量子态] \times [这些量子态上有多少个光子] \times  h\nu$ 

## 2. 态密度  
$\nu$ 到 $\nu + \mathrm{d}\nu$ 之间有多少个态？

考虑一个周期性边界条件的长方体盒子，长宽高为 $L\_{x,y,z}$ 。那么盒子中的电磁波的波数 $\kappa\_{x,y,z}$ 就满足：

$\kappa\_i = n\_i/L\_i, \quad(i=x,y,z)$ 


> 注意 $\kappa$ 是波数，而不是波矢 $k$ 。二者的关系为 $k = 2\pi \kappa$ 。

于是量子态的数量为：

$\mathrm{d} N = \mathrm{d} n\_x\mathrm{d}n\_y\mathrm{d}n\_z = L\_xL\_yL\_z \mathrm{d}\kappa\_x \mathrm{d}\kappa\_y\mathrm{d}\kappa\_z = V \mathrm{d}^3\vec{\kappa}$ 

设 $\nu$ 到 $\nu + \mathrm{d}\nu$ 之间的态的数量为 $f(\nu)$ ，则

$f(\nu) \mathrm{d}\nu = \mathrm{d}N = V \mathrm{d}^3\vec{\kappa} = V \cdot4\pi \kappa^2 \mathrm{d}\kappa = V \cdot\frac{4 \pi \nu^2}{c^3} \mathrm{d} \nu$ 

其中 $\kappa = |\vec{\kappa}|$ ，且 $\nu = c\kappa$ 。

所以 $f(\nu) = V  \cdot4 \pi \nu^2/c^3$ 。

由于一个空间模式的电磁波有两种偏振，因此还要乘以 2。另外，我们要求的是能量密度，而不是能量，所以我们可以提前把体积除掉：

$f(\nu) =  8 \pi \nu^2/c^3$ 

这就是 $\nu$ 到 $\nu + \mathrm{d}\nu$ 之间的（单位体积的）态的数量。


> 这一部分的想法就是在三维空间中，频率 $\nu$ 附近的态密度正比于 $\nu$ 的平方，正如一个球面的面积正比于半径的平方。

## 3. 态上的光子数  
热平衡时，频率为 $\nu$ 的态上有多少个光子数？答案是 $1/(e^{h\nu/kT} - 1)$ 。下面来推导一下：

玻色子体系的配分函数为：

$\begin{aligned} Z &= \sum\_{n\_1,n\_2,\cdots}  \exp[-\beta (n\_1 \varepsilon\_1 + n\_2 \varepsilon\_2 +\cdots)] \\\\ &= \left(\sum\_{n\_1} e^{-\beta n\_1\varepsilon\_1}\right)\left(\sum\_{n\_2} e^{-\beta n\_2\varepsilon\_2}\right)\cdots \\\\ &= \left(\frac{1}{1-e^{-\beta \varepsilon\_1}}\right) \left(\frac{1}{1-e^{-\beta \varepsilon\_2}}\right) \cdots \end{aligned}$ 

其中 $\varepsilon\_i$ 表示第 i 个模式上的光子能量， $n\_i$ 表示第 i 个频率模式上的光子数。

那么第 i 个模式上的平均光子数为：

$\begin{aligned} \langle n\_i\rangle = -\frac{1}{\beta}\frac{\partial \ln Z}{\partial \varepsilon\_i} = \frac{1}{e^{\beta \varepsilon\_i} - 1} \end{aligned}$ 

也就是说：频率为 $\nu$ 的态上的热平衡光子数是 $\langle n(\nu)\rangle = 1/(e^{h\nu/kT} - 1)$ 。


> 其实这就是不带化学势的玻色-爱因斯坦分布。

## 4. 结果  
$\begin{aligned} \varepsilon(\nu) \mathrm{d} \nu &= [(\nu,\nu+\mathrm{d}\nu) 中有多少个量子态] \times [这些量子态上有多少个光子] \times  h\nu \\\\ &=f(\nu) \mathrm{d} \nu \cdot\langle n(\nu)\rangle \cdot h\nu\\\\ &=\frac{8\pi \nu^2}{c^3} \cdot \frac{1}{e^{h\nu/kT}-1} \cdot h\nu \end{aligned}$ 

这么看来，黑体辐射公式还是很好记的，只要记住态密度 $f(\nu)$ 和热平衡时的光子数 $\langle n(\nu)\rangle$ 即可。态密度正比于频率的平方，热平衡光子数服从玻色爱因斯坦分布。

当频率较低时， $\varepsilon(\nu)$ 被态密度和单个光子的能量所限制，当频率较高时， $\varepsilon(\nu)$ 被平均光子数所限制。



---


> 习题 1：在二维世界中，态密度长什么样？黑体辐射的公式长什么样？  
>   
> 习题 2：紫外灾难是上面哪一步出错导致的？  
>   
> 习题 3：在常温和可见光频率（ $\sim 5.5 \times 10^{14} \text{Hz}$ ）下，单个模式的热平衡的光子数大概是多少？



---


> 答案 1：在二维世界中，态密度为 $f(\nu)=2\pi\nu/c^2$ ，黑体辐射公式为 $\varepsilon(\nu)=\frac{2\pi h\nu^2}{c^2(e^{h\nu/kT}-1)}$   
>   
> 答案 2：紫外灾难是直接把 $\frac{h\nu}{e^{h\nu/kT}-1}$ 换成了经典能均分定理的 $kT$ 。当 $\nu \ll 1$ 时， $\frac{h\nu}{e^{h\nu/kT}-1} \rightarrow kT$ ，但当 $\nu \gg 1$ 时， $\varepsilon(\nu)$ 就会发散，这就是紫外灾难。  
>   
> 答案 3：在常温和可见光频率下， $h\nu /kT = \frac{6.6 × 10^{-34} \times 5.5 \times 10^{14}}{1.4 × 10^{-23} \times 300} = 86$ ， $\frac{1}{e^{86}-1} \ll 1$ 。这就是为什么我们看不到可见光波段的黑体辐射的原因。

