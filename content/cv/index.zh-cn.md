---
title: "简历"
date: 2023-06-12T15:24:46+08:00
draft: true
comment: false
---

<!-- # 王海飞
---
hfwang132@gmail.com

# 教育背景
---

### 学士，武汉大学，弘毅学堂（珠峰计划荣誉学院），物理学方向，2021.3 -- 2021.6

- [荣誉毕业生](docs/Honor_Graduate.pdf)
- [GPA：3.97/4.00](docs/transcript-Haifei_Wang.pdf)
- 经典力学（99）、热力学与统计力学（99）、数学物理方法（98）、电动力学（93）、量子力学（96）、固体物理（91）、电子线路（模电/数电）（96）、电子设计自动化（93）、数字集成电路设计（97）

# 科研经历
---

### 研究助理，复旦大学物理学系，2021.7 -- 2021.8

导师：张远波教授（复旦大学物理学系，zhyb@fudan.edu.cn）

- **描述**：一种用于扫描隧道显微镜（STM）探针的自动校准器。目前，STM 探针需要手动校准。自动校准软件可以节省大量时间。
- **我的工作**：基于现有的 LabVIEW API 和 DOS 谱数据，开发了一个用于自动校准 STM 探针的 Python 软件包。
- **结果**：开发的 Python 软件包具有以下 API：
    - 检测样品表面的台阶和污垢、
    - 判断探针是否足够锋利、
    - 在清洁区域进行 DOS 谱分析，判断探针上是否有杂质原子、
    - 校准探针。

### 研究助理，武汉大学物理与技术学院，2021.3 -- 2021.6

导师：袁声军教授（武汉大学物理科学与技术学院，s.yuan@whu.edu.cn）

- **描述**：基于 Trotter-Suzuki 方法的时变薛定谔方程求解器。
- **我的工作**：学习论文中的算法，并编写程序实现。随后在FPGA上优化该算法，实现了200多倍的加速。
- **结果**：进行了纳米尺度模拟，并复现了论文的结果。

# 项目经验
---

### 队长，中国大学生集成电路创新创业大赛，2022.3 -- 2022.7

[http://univ.ciciec.com/](http://univ.ciciec.com/)

导师：常胜教授（武汉大学物理科学与技术学院，changsheng@whu.edu.cn）

- **描述**：基于 Intel Cyclone V SoC 的 SSD MobileNetV1 的 FPGA CNN 加速器。
- **我的工作**：
    - 对模型进行剪枝和量化，以及
    - 优化PS（处理系统）和PL（可编程逻辑）之间的交互，包括
        - 使用 openMP 和 NEON 汇编加速 PS 操作，并
        - 实现双缓冲以增加PL吞吐量。
- **结果**：单张图像的推理时间从 1000 多毫秒减少到 210 毫秒。该项目在华中地区获得了二等奖。

# 实习经历
---

### 助教，2022 AMD-Xilinx 暑期学校（中国），2022.7 -- 2022.8

[https://openhw.org/summer_school.html](https://openhw.org/summer_school.html)

- **描述**：约 800 名具有不同背景的学生参加了 2022 AMD-Xilinx 暑期学校，学习高层次综合、Xilinx 的 PYNQ 平台和 Vitis AI。
- **我的工作**：作为班级助教（共 30 个班级），安排学生使用远程实验室，收集学生的问题和反馈，并提供技术支持。

### 实习生，上海赛灵思科技有限公司，2023.3 -- 2023.6

- **描述**：基于 AD9361 射频收发器和 PYNQ 框架的 SDR 软硬件协同设计。
    - AD9361 是 ADI 设计的射频收发器芯片，在软件定义无线电（SDR）中得到广泛应用。
    - PYNQ 是一个允许用户从应用层访问可编程逻辑的框架，可以提高硬件验证和软件开发的效率。
    - 在该项目中，我们构建了一个定制的 Linux 内核，支持 PYNQ 和 AD9361 内核驱动，使得我们既能充分利用异构平台的强大和灵活性，又能在较高的层次上开发软件无线电应用。

- **我的工作**：
    - 构建了一个定制的 Linux 内核，支持 AD9361 和 PYNQ 驱动、
    - 将硬件设计从 ZCU102 板卡移植到 PYNQ-ZU 板卡上、
    - 基于 PYNQ 框架开发了一个简单的 FM 解调应用程序。

- **涉及技能**：
    - 高层次综合技术（信号处理 IP 核）
    - PS-PL 协同仿真
    - 嵌入式 Linux 设备树
    - 裸机应用开发
      - 裸机编程 SPI IP 核
    - Linux 应用开发
      - 用于 SPI 通信的 C 库
      - 对 C 库进行 Python 包装，方便使用者调用

# 获奖
---

- [国家奖学金](docs/MOE-National_Scholarship.pdf)，2022.09
- [第十三届全国大学生数学竞赛一等奖](docs/2021-math-1st-prize.pdf)，2021.12
- [2022 美国大学生数学建模竞赛 -- Meritorious Winner（一等奖）](docs/ICM-Meritorious_Winner_2022.pdf)，2022.05
- [2023 年武汉大学弘毅学堂荣誉毕业生](docs/Honor_Graduate.pdf)，2023.6
- [武汉大学 2023 届优秀学士学位论文](docs/Outstanding_Thesis.pdf)（5%），2023.6
- [武汉大学 2023 届优秀本科毕业生](docs/Outstanding_Graduate.pdf)（10%），2023.6

# 技能
---

### 编码

- C/C++
- Fortran
- Python
- $\LaTeX$
- Matlab
- Mathematica
- Verilog

### 软件

- Simulink
- LabVIEW
- Vivado, Vitis HLS, PetaLinux

### 语言

- [CET-6 633](docs/CET-6.pdf)
- [TOEFL 103](docs/TOEFL-Haifei_Wang.pdf)
- [GRE 331 (V: 163, Q: 168)](docs/GRE-Haifei_Wang.pdf) -->