---
title: "高精度时间测量——TDC / Time Tagger 原理和结构分析"
date: 2025-11-02T12:53:03+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/1967603349005248271"
author: "Haifei"
tags: ["Time Tagger", "Time-to-Digital Converter", "TCSPC", "时间相关单光子计数仪"]
categories: ["实验物理"]
---

## 一、什么是 TDC / Time Tagger  

Time-to-Digital Converter（TDC）本质上就是一个非常精准的（皮秒量级）计时器，它给每个输入的脉冲信号都打上高精度的时间戳（Timestamp）。

因此，TDC 也叫 Time Tagger，其中“Tag”就是打上时间戳的意思。

TDC / Time Tagger 是 Hong-Ou-Mandel 干涉、荧光寿命等实验的核心，可以说量子光学实验几乎离不开它。

## 二、TDC 的结构  

TDC 的大体结构非常简单，如下图所示：

{{< figure src="images/v2-c136336af8c23e0bf7d17c82f9d0cb1e_r.png" >}}

TDC / Time Tagger 的结构。图源：我自己

  
  

TDC 的每一个通道都输入到一个比较器（comparator）。比较器负责将输入的模拟脉冲信号转化为数字脉冲信号。FPGA 负责给这些数字脉冲打上高精度的时间戳，并通过 USB / Ethernet 等协议传输到上位机做后处理。

> 当然，如果芯片设计实力雄厚，也可以把 FPGA 替换成定制的 ASIC（专用芯片）。

以 Swabian Instruments 的 Time Tagger 为例，其内部采用核心板 （搭载 FPGA）+ 底板（搭载比较器）的设计。这种设计的优点是便于测试，且可扩展性强。

{{< figure src="images/v2-0c01ce9b28ce5eb64b763f060c59bd36_1440w.png" >}}

Swabian Instruments Time Tagger，图源：https://www.swabianinstruments.com/time-tagger/

  
  
{{< figure src="images/v2-e2bb57f85a49edbe2cc7acdbb483405f_r.png" >}}

Swabian Instruments Time Tagger 结构分析。图源：我自己。

  
  

Swabian Instruments 这款 Time Tagger Ultra 采用的 FPGA 是 Xilinx Kintex 7 系列（xc7k160t），算是中低档系列（28 nm 工艺）。成本 400-500 美元左右。

比较器则是 Texas Instruments 的 LMH7322，兼容 LVDS 标准，RMS随机抖动 500-600 fs。成本 10 美元左右。

再加上时钟管理、DDR、USB 各种芯片，个人估计——整块板子的 BOM 物料成本，满打满算也不会超过 2000 美元。

**然而，Swabian Instruments 能把这一套整机卖到 2 万欧元**！凭什么？

凭的就是知识产权：主要是 **FPGA 片上的硬件设计**，其次是完善的上位机软件和 API。

下一节我们就来介绍 FPGA 片上的硬件设计。

## 三、FPGA 实现 TDC 的原理  

熟悉 FPGA 的朋友都知道，这玩意儿的时钟频率最高也就只能跑到几百 MHz，再高的话，通常都会时序违例（Timing Violation）。但是 TDC 打上的时间戳的精度在 ps 量级，对应的频率是几百 GHz！那 FPGA 究竟是怎么实现 TDC 的呢？总不可能让 FPGA 跑在几百 GHz 吧？

实际上，FPGA 实现 TDC 的方式十分巧妙，用到的核心器件是计算加法的过程中需要用到的进位器（CARRY）。

> Xilinx 7 系列中的进位器是 CARRY4，Xilinx Ultrascale 系列中的进位器是 CARRY8。顾名思义，前者有 4 位，后者有 8 位。下面我们以 CARRY4 为例进行讲解。

CARRY4 器件的框图如下：

{{< figure src="images/v2-4d776b3c61d3bdbacb5a4ebfbdc2830f_r.png" >}}

图源：https://docs.amd.com/r/en-US/ug953-vivado-7series-libraries/CARRY4

  
  
> 看起来很复杂？别慌，下面会对其进行讲解。

在 Verilog 语言中可以通过 CARRY4 原语（Primitive）调用它：

```
CARRY4 CARRY4_inst (
   .CO(CO),         // 4-bit carry out
   .O(O),           // 4-bit carry chain XOR data out
   .CI(CI),         // 1-bit carry cascade input
   .CYINIT(CYINIT), // 1-bit carry initialization
   .DI(DI),         // 4-bit carry-MUX data in
   .S(S)            // 4-bit carry-MUX select input
);
```

在我们介绍它实现 TDC 的原理之前，我们先来介绍一下它的本职工作——计算加法的进位。

### 3.1 全加器  

我们先来复习一下组合逻辑电路如何计算加法。

负责加法计算的器件叫做全加器。n 位全加器是由 1 位全加器串联而成的。

1 位全加器有三个输入信号，分别是两个加数（A, B），以及一个进位输入（CI）。输出信号有两个，一个是加和（O），一个是进位输出（CO）。

下面是 1 位全加器的真值表：

| A | B | CI | CO | O |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 1 | 0 |
| 0 | 1 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 1 |

我们写出逻辑式：

\[\begin{aligned} \text{O}  &= \text{A} \oplus \text{B} \oplus \text{CI} \\ \text{CO} &= \text{A} \cdot \text{B} + \text{A} \cdot \text{CI} + \text{B} \cdot \text{CI} \end{aligned}\]

> 其中，符号 \(\oplus\) 代表异或（XOR），符号 \(\cdot\) 代表与（AND），符号 \(+\) 代表或（OR）。AND 的优先级高于 OR。

有了 \(1\) 位全加器之后，我们只要把第 \((n-1)\) 位的 \(\text{CO}\) 连接到第 \(n\) 位的 \(\text{CI}\) ，就可以实现 \(n\) 位全加器。

这样一来，我们就可以用异或门（XOR），与门（AND），或门（OR）计算加法了。

然而，上述逻辑式还可以进一步简化，从而减少逻辑门的数量。令 \(\text{DI}=\text{A}\cdot \text{B}\) ， \(\text{S}=\text{A} \oplus \text{B}\) ，则

\[\begin{aligned} \text{O}  &= \text{A} \oplus \text{B} \oplus \text{CI} \\ &= \text{S}\oplus \text{CI} \\ \text{CO} &= \text{A} \cdot \text{B} + \text{A} \cdot \text{CI} + \text{B} \cdot \text{CI}\\ &= \text{A}\cdot \text{B} + (\text{A} \oplus \text{B})\cdot \text{CI} \\ &= (\text{A} \oplus \text{B}) \,? \,\text{CI} : (\text{A}\cdot \text{B})\\ &= \text{S} \, ? \, \text{CI}: \text{DI} \end{aligned}\]

> 其中 \(a \,?\, b:c\) 是三元运算符，表示 \(\text{if }a,\text{ then }b,\text{ else }c\) 。这个运算由 MUX（多路选择器，Multiplexer）实现。  
>   
> DI 叫做 generator，S 叫做 propagator。顾名思义，DI 产生进位，S 传播进位。

现在，我们将上述逻辑式向量化：

\[\begin{aligned} \text{O}[n]&=\text{S}[n] \oplus \text{DI}[n] \\ \text{CO}[n]&= \text{S}[n]\,?\, \text{CO}[n-1] : \text{DI}[n] \end{aligned}\]

于是就可以画出电路图了（以 4 位全加器为例）：

{{< figure src="images/v2-98317849fd889ba5274f505b6d4ad017_r.png" >}}

4 位全加器的电路图。图源：我自己

  
  

这个电路实现了 \(\{\text{CO}, \,\text{O[3:0]}\} = \text{A[3:0]} + \text{B[3:0]} + \text{CI}\) 的运算。

### 3.2 CARRY4 的结构  

把上一节电路图里的核心部分拿出来，就是 CARRY4 了：

{{< figure src="images/v2-2bede568f768105af2612fca64e00259_r.png" >}}

图中红框圈出的部分就是 CARRY4。图源：我自己

  
  

对比一下官方文档中的电路图：

{{< figure src="images/v2-4d776b3c61d3bdbacb5a4ebfbdc2830f_r.png" >}}

图源：https://docs.amd.com/r/en-US/ug953-vivado-7series-libraries/CARRY4

  
  

是不是一模一样？

> 唯一的不同在于 CI 可以被 CYINIT 覆盖。当 CYINIT 为 1 时，输出 1，当 CYINIT 为 0 时，输出 CI。这只是为了编程方便。  
>   
> 例如，当计算减法时，逻辑式为 \(\text{O} = \text{A} + \sim\text{B} + 1\) ，其中 \(\sim\) 为按位否（bit-wise NOT）。所以计算减法时只要将最低位的 CARRY4 的 CYINIT 设置为 1 即可。

### 3.3 CARRY4 做高精度延时线  

前两节我们介绍了 CARRY4 的本职工作——计算加法。现在我们来介绍它在 TDC 里的功能——皮秒量级延时线。

CARRY4 里有一条较长的关键路径（critical path）：

\[\text{CI} \rightarrow \text{CO}[0] \rightarrow \text{CO}[1] \rightarrow \text{CO}[2] \rightarrow \text{CO}[3] \]

任何组合逻辑门的计算都需要皮秒量级的时间。具体到上面的路径，每个箭头要花几皮秒到几十皮秒的时间。

如果我们把多个 CARRY4 首尾相连，我们就得到了一条很长的延时线（delay line），并且延时的精度为皮秒量级：

\[\text{CI} \rightarrow \text{CO}[0] \rightarrow \text{CO}[1] \rightarrow \text{CO}[2] \rightarrow \cdots \rightarrow \text{CO}[N-1]\]

从逻辑式 \(\text{CO}[n]= \text{S}[n]\,?\, \text{CO}[n-1] : \text{DI}[n] \) 中可以看出，我们只要将 \(\text{S}[n]\) 全部设置为高电平， 就可以让进位信号沿着这条链传播下去了。而 \(\text{DI}[n]\) 的高低则无所谓，不影响进位信号的传播。

这其实模拟了人做加法时传播进位的过程：想象我们计算 \(1111_2 + 0001_2 = 10000_2\) ，我们先计算最低位的 \(1+1=10\) ，发现产生了进位，于是我们把它记录到下一位。这导致下一位又产生进位，以此类推。而计算机计算这每一个进位所需要的时间是几-几十皮秒。

见下图，我们将输入脉冲（trigger 信号）接到 \(\text{CI}\) ，并在下一个时钟上升沿记录 \(\text{CO}[N-1:0]\) ，就可以知道图中的时间间隔 \(\tau\) 。于是就能以皮秒精度确定输入脉冲到达的时间了。

{{< figure src="images/v2-b7668dd3655a7d6c0414ebf92eb6a7ec_r.png" >}}

TDC 时序图。图源：我自己

  
  

有小伙伴肯定发现了盲点：按照这个工作原理，要是两个脉冲在一个时钟周期内到达，那岂不是只能记录一个（比如第一个）？没错，这就是为什么 TDC / Time Tagger 也有死时间（dead time），通常在几到十几纳秒，由 FPGA 的时钟频率决定。

> 当然，如果能设计 ASIC 专用芯片，定制延时线，效果肯定比 FPGA 更好。毕竟 FPGA 的 CARRY4 / CARRY8 的设计初衷并不是用来做延时线的。

## 四、总结  

本文介绍了 FPGA 实现的 TDC（Time-to-Digital Converter）/Time Tagger 的结构及工作原理；其中，采用 CARRY4/CARRY8 构建的高精度延时线构成了 FPGA 硬件设计的关键部分。

## 参考  

[1] Castelvero, L., López Grande, I. H. & Pruneri, V. High-Performance Time-to-Digital Conversion on a 16-nm Ultrascale+ FPGA. *IEEE Access* **12**, 149569–149579 (2024).  
[2] Zhu, M., Qi, X., Cui, T. & Gao, Q. Tapped delay line for compact time-to-digital converter on UltraScale FPGA and its coding method. *Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment* **1056**, 168639 (2023).  
[3] Hua, Y. & Chitnis, D. A Highly Linear and Flexible FPGA-Based Time-to-Digital Converter. *IEEE Trans. Ind. Electron.* **69**, 13744–13753 (2022).
