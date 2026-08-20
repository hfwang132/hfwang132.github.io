---
title: "性价比极高的公式"
date: 2022-01-01T19:21:09+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/452415452"
author: "Haifei"
tags: ["数学公式"]
categories: ["数学物理方法"]
---

以下的公式能给解题带来极大的方便

### 一、高斯积分  

$$I_n = \int_{0}^{\infty}x^n e^{-b x^2}\mathrm{d}x  %=  %\left\{\begin{aligned}  %\end{aligned}\right. $$

如下是一个方便的记忆方法：

首先记住

$$I_0 = \frac{1}{2}\sqrt{\frac{\pi}{b}},\quad I_1 = \frac{1}{2}\frac{1}{b}$$

其次有

$$I_{n+2}=\frac{n+1}{2b}I_n$$

这个公式对 $n$ 为奇数和偶数的情况都适用。

如果你在与高斯函数打交道（例如概率论），那么这个积分将会出现得非常频繁！

### 二、三角函数的幂  

$$I_n=\int_{0}^{\frac{\pi}{2}}\sin^{n}x\mathrm{d}x = \int_{0}^{\frac{\pi}{2}}\cos^{n}x\mathrm{d}x$$

下式给出了 $I_n$

$$I_n =  \left\{\begin{aligned} &\frac{(n-1)!!}{n!!}&, \quad n \text{ is odd} \\ &\frac{(n-1)!!}{n!!}\frac{\pi}{2}&, \quad n \text{ is even} \end{aligned}\right.$$

这个公式在球坐标下对 $\theta,\,\varphi$ 积分的时候非常有用！

### 三、x^n的拉普拉斯变换  

$$I_n=\int_{0}^{\infty}x^n\mathrm{e}^{-kx}\mathrm{d}x$$

下式给出了 $I_n$：

$$I_n=\frac{n!}{k^{n+1}}$$

这个公式在球坐标下对 $r$ 积分时的时候有用（如果你在处理带有 $\mathrm{e}^{kr}$ 的项）

### 四、分部积分的快捷方式  

$$I=\int_{a}^{b} u(x)v(x)\mathrm{d}x$$

快捷方式的示意图如下：

$$\begin{alignedat}{6} & u(x) &  \quad & u^{(1)}(x) & \quad & u^{(2)}(x) & \quad & u^{(3)}(x) &  \quad & \cdots \\ & & \searrow^{+} & & \searrow^{-} & & \searrow^{+} & & \searrow^{-} \\ & v(x) & \quad & v^{(-1)}(x) & \quad & v^{(-2)}(x) & \quad & v^{(-3)}(x) & \quad & \cdots & & \end{alignedat}$$

其中 $u^{(n)}(x)$ 表示 $u(x)$ 的 $n$ 阶导函数， $v^{(-n)}(x)$ 表示 $v(x)$ 的 $n$ 次不定积分。

换言之，

$$\begin{aligned} I&=\int_{a}^{b} u(x)v(x)\mathrm{d}x  \\&= \left.u(x)v^{(-1)}(x)\right|^{b}_{a} - \left.u^{(1)}(x)v^{(-2)}(x)\right|^{b}_{a}+\left.u^{(2)}(x)v^{(-3)}(x)\right|_{a}^{b} - \cdots \end{aligned}$$

这个过程直到 $u^{(n)}(x)=0$ 为止。

> 或者你也可以手动在某个位置停下，例如  
>  $\begin{aligned} I&=\int_{a}^{b} u(x)v(x)\mathrm{d}x  \\&= \left.u(x)v^{(-1)}(x)\right|^{b}_{a} - \left.u^{(1)}(x)v^{(-2)}(x)\right|^{b}_{a}+\int_{a}^{b}u^{(2)}(x)v^{(-2)}(x)\mathrm{d}x \end{aligned}$   
> 这种情况下，你希望 $\int_{a}^{b}u^{(2)}(x)v^{(-2)}(x)\mathrm{d}x$ 中包含了 $I$ ，这样就可以移项解出 $I$

### 五、球坐标系下的微分算子  

在正交曲线坐标系下，有

$$\nabla = \frac{\bm{e}_{1}}{h_1}\frac{\partial}{\partial q_1}+\frac{\bm{e}_{2}}{h_2}\frac{\partial}{\partial q_2}+\frac{\bm{e}_{3}}{h_3}\frac{\partial}{\partial q_3}$$

$$\nabla \cdot \mathbf{A} = \frac{1}{h_1h_2h_3}\left[\frac{\partial}{\partial q_1}(A_1h_2h_3)+\frac{\partial}{\partial q_2}(h_1A_2h_3)+\frac{\partial}{\partial q_3}(h_1h_2A_3)\right]$$

$$\nabla\times\mathbf{A}=\frac{1}{h_1h_2h_3}\begin{vmatrix} h_1\bm{e_1} & h_2\bm{e_2} & h_3\bm{e_3} \\ \frac{\partial}{\partial q_1} & \frac{\partial}{\partial q_2} & \frac{\partial}{\partial q_3} \\ h_1A_1 & h_2A_2 & h_3A_3 \end{vmatrix}$$

$$\begin{aligned} \nabla^2u&=\nabla\cdot(\nabla u)\\&= \frac{1}{h_1h_2h_3}\left[\frac{\partial}{\partial q_1}\left(\frac{h_2h_3}{h_1}\frac{\partial}{\partial q_1}\right) + \frac{\partial}{\partial q_2}\left(\frac{h_1h_3}{h_2}\frac{\partial}{\partial q_2}\right) + \frac{\partial}{\partial q_3}\left(\frac{h_1h_2}{h_3}\frac{\partial }{\partial q_3}\right) \right]u \end{aligned}$$

对以上公式作替换

$$\begin{matrix} h_1 \rightarrow 1 &  h_2 \rightarrow r & h_3 \rightarrow r\sin\theta \\ \bm{e}_1 \rightarrow \bm{\widehat{r}} & \bm{e}_2 \rightarrow \bm{\widehat{\theta}} & \bm{e}_3 \rightarrow \bm{\widehat{\varphi}} \end{matrix}$$

即可得到球坐标下的公式。

实际上， $h_1,\,h_2,\,h_3$ 叫做拉梅系数。

有了这一招，你就可以考场手撕球坐标系下的PDE了。

### 六、矩阵的指数  

其实这个很容易推导出来...放到这里凑个数吧：

$$\exp\left(t\begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}\right) =\begin{bmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{bmatrix}$$

$$\exp\left(t\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}\right) =\begin{bmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{bmatrix}$$
