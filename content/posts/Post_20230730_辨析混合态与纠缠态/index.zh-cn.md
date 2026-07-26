---
title: "辨析混合态与纠缠态"
date: 2023-07-30T02:51:44+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/646801699"
author: "Haifei"
tags: ["量子纠缠"]
categories: ["量子信息/量子光学"]
---

## 一、纯态与混合态  

要想搞明白纯态和混合态，首先就必须搞明白**密度算子**（density operator），或**密度矩阵**（density matrix）。

### 1.1密度算子是啥？  

当我第一次看到密度算子的时候，我觉得它非常神奇。因为它是将**一个态与自己的对偶做张量积**：

\[v \mapsto v\otimes v^*\]

或者写得物理风格一点：

\[| \psi \rangle \mapsto |\psi \rangle \langle \psi |\]

我们都知道，一个量子态 \(v\) 就是希尔伯特空间的一个向量而已，即 \(v \in H\) 。但是密度算子非要搞成 \(v\otimes v^*\in H\otimes H^* \cong \operatorname{End}(H)\) ，这有什么用？

更要命的是，这样搞出来的一个东西，它的矩阵（也就是密度矩阵）的秩（rank）必然只为一。这类似于你将一个列向量 \(x\) 与它自己的共轭转置相乘：

\[xx^\dagger= \begin{bmatrix} 1 \\2 \end{bmatrix} \begin{bmatrix} 1 & 2 \end{bmatrix}= \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}\]

这并没有给出更多的信息，反倒是搞出了一个不可逆矩阵。

所以密度算子到底有什么用？实际上，它的有用之处，体现在你把多个不同态对应的密度矩阵加起来的时候。举个例子，假设现在又给了一个新的列向量 \(y\) ：

\[yy^\dagger= \begin{bmatrix} 2 \\ 1 \end{bmatrix} \begin{bmatrix} 2 & 1 \end{bmatrix}= \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}\]

再把 \(xx^\dagger\) 和 \(yy^\dagger\) 加起来：

\[xx^\dagger+yy^\dagger= \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} + \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} 5 & 4 \\ 4 & 5 \end{bmatrix}\]

现在你会发现，这个新的矩阵是无法表示成一个列向量与自己的转置的乘积的！这就是所谓的**混合态**。而如果一个密度矩阵可以被表示成某个列向量与自己的乘积，那么它就对应一个**纯态**。

### 1.2 密度算子是干嘛的？  

那么，为什么会出现混合态呢？量子态难道不都是纯态吗？难道还有量子态不能被表示成希尔伯特空间中一个向量？

实际上，在如下两种情况下，混合态和密度算子的概念是有用的：

1. 我们在考虑一个**量子系综**，即大量（不一定相干）的量子态的集合。这常用于量子统计力学。
2. 我们对某个量子系统的**知识（信息）有限**。例如，给定一个多粒子系统，即使我们知道其整体量子态，但对于其中一个粒子（子系统），我们并不清楚它处于什么量子态，我们只知道它有一定概率处于某一个态。这常用于量子信息。

第一种情况的例子是偏振度为零的自然光。此时对应密度算子可以写成： \(\rho = \frac{1}{2} |H\rangle\langle H| + \frac{1}{2}|V\rangle\langle V| = \frac{1}{2}I\) ，其中 H 代表水平偏振，V 代表竖直偏振。当然，偏振度介于零到一之间的部分偏振光也可以用密度矩阵表示： \(\rho = \frac{I+P\bm{r}\cdot\bm{\sigma}}{2} = \frac{I+P(x\sigma_x+y\sigma_y+z\sigma_z)}{2}\) ，其中 \(\bm{\sigma}\) 是泡利矩阵， \(P\) 是偏振度， \(\bm{r}\) 是 Bloch 向量，对应 Bloch 球面上的坐标。

第二种情况的例子是量子隐形传态。我们都知道，如果 Alice 不将测量结果作为经典信息告诉 Bob，那么量子隐形传态是无法完成的（这也是为什么量子隐形传态不意味着超光速通信）。在 Bob 得知 Alice 的测量结果之前，他拥有的 qubit 就可以用一个混合态对应的密度矩阵来描述。

### 1.3 密度算子的定义  

最后，我们来定义密度算子。注意到一开始的例子没有对量子态做标准化。现在，我们完成标准化：

\[x= \begin{bmatrix} 1 \\ 2 \end{bmatrix} \mapsto  \begin{bmatrix} \frac{1}{\sqrt{5}} \\ \frac{2}{\sqrt{5}} \end{bmatrix}, \quad y= \begin{bmatrix} 2 \\ 1 \end{bmatrix} \mapsto  \begin{bmatrix} \frac{2}{\sqrt{5}} \\ \frac{1}{\sqrt{5}} \end{bmatrix}\]

\[xx^\dagger \mapsto   \begin{bmatrix} \frac{1}{5} & \frac{2}{5}\\ \frac{2}{5} & \frac{4}{5} \end{bmatrix}, \quad yy^\dagger \mapsto   \begin{bmatrix} \frac{4}{5} & \frac{2}{5}\\ \frac{2}{5} & \frac{1}{5} \end{bmatrix}\]

然后，把“将若干纯态相加”改成“将若干纯态加权混合”：

\[\rho = \frac{1}{2}xx^\dagger + \frac{1}{2}yy^\dagger= \begin{bmatrix} \frac{1}{2} & \frac{2}{5}\\ \frac{2}{5} & \frac{1}{2} \end{bmatrix}\]

这启发我们对密度算子做出如下定义：

\[\rho = \sum_{i} p_i |\psi_i\rangle\langle\psi_i|, \quad \sum_i p_i = 1\]

如果你的品味更加偏数学一点，你还可以将密度矩阵定义为如下集合中的元素，即复希尔伯特空间上所有**迹等于一的半正定算子**的集合。注意到半正定性蕴含了自伴性（即厄米性）。

## 二、可分离态与纠缠态  

要想搞明白什么是纠缠态，我们就必须搞清楚，在量子力学中，我们如何描述多粒子系统。

我们都知道，一个粒子所处的量子态可以用希尔伯特空间中的一个向量 \(|\psi\rangle \in H\) 来描述。但是多个粒子怎么办呢？

此时，我们需要用到向量空间的**张量积**。

例如，一个粒子的量子态属于一个希尔伯特空间： \(|\psi\rangle\in H_1\) ，另一个粒子的量子态属于另一个希尔波特空间： \(|\varphi\rangle\in H_2\) 。为了描述这两个系统构成的整体系统，我们可以将 \(H_1\) 和 \(H_2\) 做张量积： \(H = H_1\otimes H_2\) 。这个新的 \(H\) 也是一个向量空间。

假设 \(H_1\) 有两个基 \(|\psi_1\rangle,|\psi_2\rangle\) ， \(H_2\) 有三个基 \(|\varphi_1\rangle,|\varphi_2\rangle,|\varphi_3\rangle\) ，那么 \(H = H_1\otimes H_2\) 这个新的向量空间将会有六个基：

\[|\psi_i\rangle\otimes|\varphi_j\rangle, \, i=1,2,\, j=1,2,3\]

我们可以用矩阵来表示 \(H = H_1\otimes H_2\) 中的向量，例如：

\(\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}\) （未标准化，标准化需要除以 \(\sqrt{1^2+\cdots+6^2}\) ）。

那么**可分离态**是什么意思呢？与纯态类似，它的矩阵也是可以写成列向量与行向量的乘积，例如：

\[\begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}\]

用线性代数的话来说，就是它可以写成两个（或多个）向量的张量积 \(s=s_1\otimes s_2\) 。

**纠缠态**则与可分离态相对，它不能写成若干个向量的张量积，例如之前的 \(\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}\) ，这在数学上叫做不可分的（non-separable）。

## 三、混合态与纠缠态有什么区别？  

当我们讨论混合态时，我们考虑的空间是 \(H\otimes H^*\) ，即一个希尔伯特空间与自己的对偶的张量积。

一个态被称为混合态，当且仅当它是 \(H\otimes H^*\) 上的不可分向量。

而当我们讨论纠缠态时，我们一般考虑的空间是 \(H \otimes H\) ，即希尔伯特空间彼此的张量积。

> 注：更一般地，应考虑 \(\bigotimes_i H_i\) 。 注：对于全同粒子，应当将张量积改为对称积或外积。前者对应玻色子，后者对应费米子。

一个态被称为纠缠态，当且仅当它是 \(H \otimes H\) 上的不可分向量。

当然，我们也可以问一个混态是不是纠缠态。此时我们考虑的是 \(H \otimes H\) 上的 Endomorphism。

## 四、混合态与纠缠态有什么关系？  

经过评论区拷打，加上这一节。

1. 一个态可以是混合态但不是纠缠态，也可以是纠缠态但不是混合态，也可以同时是混合态和纠缠态，也可以都不是。

2. 对于一个纠缠态做偏迹（partial trace）运算会得到一个混合态。例如，正如上文所说，在 Bob 得知 Alice 的测量结果之前，他拥有的 qubit 就是整体量子态 trace 掉 Alice 的 qubit 得到的，此时结果是一个混合态。特别地，对于两粒子系统，其纠缠程度等于偏迹运算后的混合程度，即 Schmidt Number 等于纯度的倒数。

3. 如何判定一个一般的多粒子混合态是纠缠态？此时我们考虑的空间是 \((H\otimes \cdots \otimes H) \otimes (H\otimes \cdots \otimes H)^* \cong \mathrm{End}(H^{\otimes n})\) 。对于两个粒子而言，这个问题有明确的答案：可以用 [PPT 准则（Positive Partial Transpose Criteria）](https://en.wikipedia.org/wiki/Peres–Horodecki\_criterion)来判断。对于多个粒子而言，这个问题相对 open：有许多不同的准则，且它们各有优劣。
