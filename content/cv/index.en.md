---
title: "CV"
date: 2023-06-12T15:24:39+08:00
draft: false
comment: false
---

# Haifei WANG
---
hfwang132@gmail.com

# Education
---

### Bachelor of Science in Physics, *Wuhan University*, Sep 2019 -- Jun 2023

- Honor Graduate of Hongyi Honor College
- GPA: 3.97/4.00 (top 2\%)
- Core Courses: Classical Mechanics (99), 
  Thermodynamics and Statistical Physics (99), Mathematical Physics (98), Electrodynamics (93), Quantum Mechanics (96), Solid-state Physics (91), Electronic Circuits (96), Electronic Design Automation (93), Digital IC Design (97).

# Research Experience
---

### Research Assistant, *Department of Physics, Fudan University*, Jul 2021 - Aug 2021

Advisor: Professor Yuanbo Zhang (Department of Physics, Fudan University, zhyb@fudan.edu.cn)

- **Description**: An auto-calibrator for STM (scanning tunneling microscope) tips. At present, STM tips are manually calibrated. An automatic calibration software would save plenty of time.
- **My Work**: Based on existing LabVIEW APIs and DOS spectrum data, developed a python package to auto-calibrate the STM tips.
- **Results**: The developed python package has APIs that
    - detect the edges and dirts on the surface of the sample, 
    - judge whether the tip is sharp enough, 
    - perform bias spectroscopy in clean areas to judge whether there are impurity atoms on the tip, and
    - calibrate the tip.

### Research Assistant, *School of Physics and Technology, Wuhan University*, Mar 2021 -- Jun 2021

Advisor: Professor Shengjun Yuan (Department of Physics, Wuhan University, s.yuan@whu.edu.cn)

- **Description**: A time-dependent Schrodinger equation solver based on the Trotter-Suzuki method.
- **My Work**: Learned about the algorithm in the paper and wrote a program to realize the algorithm. Later optimized the algorithm on FPGA and achieved 200+ times acceleration.
- **Results**: Performed nanoscale simulation and reproduced the paper's results. 

# Project Experience
---

### Team Leader, College Integrated Circuits Competition of China, Mar 2022 -- Jul 2022

[http://univ.ciciec.com/](http://univ.ciciec.com/)

Advisor: Professor Sheng Chang (Department of Physics, Wuhan University, changsheng@whu.edu.cn)

- **Description**: An FPGA CNN accelerator for SSD MobileNetV1 based on Intel Cyclone V SoC.
- **My Work**:
    - pruning and quantization of the model, and
    - optimization of the interaction between PS (processing system) and PL (programmable logic), including 
        - the use of openMP and NEON assembly to accelerate PS operations and,
        - the implementation of double buffering to increase PL throughput.
- **Results**: The inference time of an image was reduced from 1000+ ms to 210 ms. The project has won the second prize in the Central China Division.

# Internship
---

### Teaching Assistant, *2022 AMD-Xilinx Summer School, China*, Jul 2022 -- Aug 2022

[https://openhw.org/summer_school.html](https://openhw.org/summer_school.html)

- **Description**: About 800 students with various backgrounds participated in the 2022 AMD-Xilinx Summer School and learned about high-level synthesis, Xilinx's PYNQ platform, and Xilinx's latest technology Vitis AI.
- **My Work**: As TA of one of the 30 classes, arrange for students to use the remote laboratory, collect students' questions and feedback, and provide technical support.

### Intern, *Xilinx Technology Shanghai Ltd.*, Mar 2023 -- Jun 2023

- **Description**: SDR software-hardware codesign based on AD9361 RF-tranceiver and the PYNQ framework.
    - AD9361 is an RF transceiver chip designed by ADI, and has found tremendous applications in software-defined radios (SDR).
    - PYNQ is a framework that allows users to access the programmable logic from the application level, boosting hardware verification and software development.
    - In this project, we build a custom Linux Kernel, supporting both PYNQ and AD9361, making it possible to develop high-level SDR applications while utilizing the power and flexibility of heterogeneous platforms.
- **My work**:
    - built a customized Linux kernel with support for AD9361 and PYNQ drivers,
    - ported the hardware design from the ZCU102 board to the PYNQ-ZU board, and
    - developed a simple FM demodulation application based on the PYNQ framework.

# Awards
---

- National Scholarship (<1\%), Ministry of Education of PRC, Sep 2022
- 13th Chinese College Mathematics Competition -- First Prize, Dec 2021
- 2022 Interdisciplinary Contest in Modeling (ICM) -- Meritorious Winner, May 2022
- Honor Graduate of Hongyi Honor College, Jun 2023
- Wuhan University 2023 Outstanding Bachelor's Degree Thesis (5%), Jun 2023
- Wuhan University 2023 Outstanding Graduate (10%), Jun 2023

# Skills
---

### Coding

- C/C++
- Fortran
- Python
- $\LaTeX$
- Matlab
- Mathematica
- Verilog

### Softwares

- Simulink
- LabVIEW
- Vivado, Vitis HLS, PetaLinux

### Language

- CET-6 633
- TOEFL 103
- GRE 331 (V: 163, Q: 168)
