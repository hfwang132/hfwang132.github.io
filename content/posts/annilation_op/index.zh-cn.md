---
title: "产生湮灭算符是怎么得到的？"
date: 2024-05-27T17:47:25+08:00
draft: false
tags: ["数学物理方法"]
categories: ["量子信息"]
---


产生湮灭算符的定义动机很简单，完全可以从经典力学中得到。

想想我们是怎么解经典谐振子的。由于位置和动量是耦合起来的：

$\begin{cases} \frac{\mathrm{d}x}{\mathrm{d}t} = \omega p \\\\ \frac{\mathrm{d}p}{\mathrm{d}t} = -\omega x \end{cases}$ 

即

$\frac{\mathrm{d}}{\mathrm{d}t} \begin{bmatrix} x \\\\ p \end{bmatrix} = \begin{bmatrix} 0 & \omega \\\\ -\omega & 0 \end{bmatrix} \begin{bmatrix} x \\\\ p \end{bmatrix}$ 

那么我们只要将它们解耦就可以了。对角化得到特征向量 $a^{\pm} =  x\pm\mathrm{i}p$ ，于是 $a^{\pm}$ 的导数就只和自己有关：

$\frac{\mathrm{d}a^{\pm}}{\mathrm{d}t}=\mp\mathrm{i}\omega a^{\pm},\quad a^{\pm}=a_0^{\pm} \exp (\mp\mathrm{i}\omega t)$ 

这一套流程里的 $a^{+}$ 和 $a^{-}$ 量子化之后就是湮灭和产生算符。


> 记 $a^{+}\rightarrow\hat{a},\quad a^{-}\rightarrow \hat{a}^\dag$ ，则 $[\hat{a},\hat{a}^\dag]=[\hat{x}+\mathrm{i}\hat{p},\hat{x}-\mathrm{i}\hat{p}]=-\mathrm{i}[\hat{x},\hat{p}] = 1$ 。  
>   
> 后面的故事大家都很熟悉了。

多模情况也很简单。每当我们解耦出来一个特征向量，我们都会把它叫做一个模式，对应的就是该模式上的产生湮灭算符。这就是准粒子（例如声子）的由来。

在经典力学里，$a^{+}$ 和 $a^{-}$ 只是为了方便求解而扩展到复数域的技巧，而在量子力学里，它们有实实在在的物理含义。所以量子力学离不开复数。

