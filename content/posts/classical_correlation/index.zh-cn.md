---
title: "量子纠缠与经典关联的区别，以及量子测量问题"
date: 2024-05-27T17:33:11+08:00
draft: false
tags: ["量子测量理论"]
categories: ["量子信息"]
---


很多物理工作者向大众科普量子纠缠的时候都会举一个例子：


> 想象你有两个盒子，其中一个放了披萨，另一个放了汉堡，在打开盒子之前无法知道其中是什么。Alice 和 Bob 一人拿走一个盒子，并且走到相距很远的地方。此时 Alice 打开盒子就能知道遥远彼端的 Bob 的盒子里有什么。

这个例子肯定有什么不对...因为它压根就没有涉及到量子力学。

的确如此，这个例子表现的是经典关联，而非量子纠缠。令披萨为 $|0\rangle$ ，汉堡为 $|1\rangle$ ，那么在上面这个例子中，系统的状态为

$\rho_{\text{classical correlation}} = \frac{1}{2} \left( |01\rangle\langle 01| + |10\rangle\langle 10| \right)$ 

写成矩阵形式就是：

$\rho_{\text{classical correlation}} = \begin{bmatrix} 0 & 0 & 0 & 0 \\\\ 0 & \frac{1}{2} & 0 & 0 \\\\ 0 & 0 & \frac{1}{2} & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix}$ 

而真正的量子纠缠应该如下：

$\rho_{\text{quantum entanglement}} = |\psi\rangle\langle\psi | = \frac{1}{2} \left( |01\rangle\langle 01| + |10\rangle\langle 10| + |01\rangle\langle 10| + |10\rangle\langle 01 | \right)$ 

其中 $|\psi\rangle = \frac{1}{\sqrt{2}} (|01\rangle + |10 \rangle)$ 

写成矩阵形式就是：

$\rho_{\text{quantum entanglement}} = \begin{bmatrix} 0 & 0 & 0 & 0 \\\\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\\\ 0 & \frac{1}{2} & \frac{1}{2} & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix}$ 

可见，真正的量子纠缠是有非对角项的。这些非对角项也叫相干项（coherences）。

同样可见，当上面的量子纠缠态退相干之后，才会得到经典关联。换句话说，经典关联是量子纠缠退相干之后的结果。

退相干也是**量子测量问题（measurement problem）**的一个诠释：当系统与环境纠缠后，如果考察系统部分的偏迹，会发现系统的状态是退相干的。这样一来，量子纠缠就变成了经典关联，此时密度矩阵只剩下了对角项。

但退相干不能解释波函数的坍缩问题。因为下面这个过程仍然是由系统和环境的整体波函数坍缩而导致的。

$\begin{bmatrix} 0 & 0 & 0 & 0 \\\\ 0 & \frac{1}{2} & 0 & 0 \\\\ 0 & 0 & \frac{1}{2} & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix} \xrightarrow{\text{collapse}}  \begin{cases} \begin{bmatrix} 0 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix}, & \text{with }\frac{1}{2} \text{ probability} \\\\ \begin{bmatrix} 0 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 0 \end{bmatrix}, & \text{with }\frac{1}{2} \text{ probability} \end{cases}$ 

这一步无法用退相干来解释。因此测量问题至今尚未解决。这也很好理解：退相干本身仍然是一个酉的演化过程，而波函数坍缩是非酉的。

所以，我们只能暂时接受：波函数坍缩在现代量子力学中是一个公设，而非可以导出的定理。这将会导致一个完备性问题：我们无法通过量子力学本身来决定一个过程应该是酉的演化过程还是非酉的坍缩过程。

这个问题也叫做 Heisenberg cut，即如何找到这样一个“cut”，使得在其之下系统都会正常演化，而在其之上会系统会坍缩。当然，由于我们现有的测量仪器都是粒子数很大的系统，所以我们无需担心这个问题——我们十分确定，我们的测量会诱导系统的坍缩。



---

在 categorical quantum theory 中，描述量子纠缠需要 $\mathbf{Hilb}$ 张量范畴，而描述经典关联只需要 $\mathbf{Rel}$ 张量范畴。前者的张量积是希尔伯特空间的张量积，而后者的张量积是集合的笛卡尔积。

笛卡尔积（以及直积、直和）是无法描述量子纠缠的。希尔伯特空间的张量积才是纠缠现象得以存在的根源。前者是经典的标志，可以描述经典关联，后者是量子的标志，可以描述量子纠缠。

然而，真正的经典物理是决定论的，它由 $\mathbf{Set}$ 范畴描述。而 $\mathbf{Rel}$ 范畴是概率论的，它介于 $\mathbf{Hilb}$ 和 $\mathbf{Set}$ 之间。也许，如何从 $\mathbf{Rel}$ 范畴过渡到 $\mathbf{Set}$ 范畴，才是解决测量问题的最后一步，而这一步本身就不在 $\mathbf{Hilb}$ 范畴之内。

测量问题和统计力学中的一些问题比较相似，例如熵与时间之矢。这些问题的根源都是谷堆悖论式的：它们只在系统足够大时才涌现出来，以至于我们难以找到一个小与大的界限，也即 Heisenberg cut。

