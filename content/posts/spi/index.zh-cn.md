---
title: "AXI SPI IP 核的软硬件设计"
date: 2023-06-29T11:33:45+08:00
draft: false
categories: ["EECS"]
tags: ["SPI", "嵌入式系统"]
---

### 1 基础

SPI 有三线模式和四线模式。三线模式有 `SS`（Slave Select）, `SCK`（SPI Clock）, `MOSI`（Master-Out-Slave-In）三条线。四线模式多了一条 `MISO`（Master-In-Slave-Out）。

|信号|全称|功能|
|-|-|-|
|SS|Slave Select|片选|
|SCK|SPI Clock|时钟信号|
|MOSI|Master-Out-Slave-In|主器件向从器件发送指令和数据|
|MISO|Master-In-Slave-Out|从器件向主器件返回数据|

SPI 的时钟有四种模式，分别对应 CPOL=0/1 和 CPHA=0/1。CPOL（Clock Polarity）代表时钟信号在空闲的时候是高还是低；CPHA（Clock Phase）代表在时钟信号相位为 0 度还是 180 度的时候读取数据。

### 2 AXI Quad SPI IP 核

当 Zynq PS 的 SPI 控制器不够用，或者因为其他原因（例如 MIO 被占用）而无法使用的时候，可以在 PL 端使用 SPI 控制器的 IP 核，叫做 AXI Quad SPI。

> 本文只涉及 Standard Mode + Master Mode，不涉及 Dual/Quad Mode 以及 Slave Mode / Multi-master Mode。

{{< figure src="files/axi-quad-spi.png" title="AXI Quad SPI IP 核" >}}

在上图中， `io1_i` 连接 MISO 信号；`ext_spi_clk` 和 `s_axi_clk` 都连接同一个系统时钟即可。`ip2intc_irpt` 可以连接 Zynq 的中断 `pl_ps_irq`。 

可以双击 IP 核配置时钟分频、片选信号个数等等。

### 3 裸机编程

编程顺序如下

- 首先，初始化 SPI 控制器。将各个寄存器的值恢复到默认状态。
- 其次，根据使用场景，配置 SPI 控制器，例如时钟模式的 CPHA 和 CPOL、片选模式为自动还是手动等等。
- 再次，根据需要读写的字节数，向数据发送寄存器（DTR，Data Transmit Register）中写入相应数量的字节。每写入一个字节，该字节都会被压到 TX FIFO 中。
    - 注意，假设发送的字节数为 `n_tx`，接收的字节数为 `n_rx`，那么不仅要向 DTR 写入 `n_tx` 个发送的字节，还要再写入 `n_rx` 个 “dummy” 字节。这是因为 SPI 本质上是一种全双工的协议：为了接收 `n_rx` 个数据，编程人员也必须要发送 `n_rx` 个数据。
- 最后，从数据接收寄存器（DRR，Data Receive Register）中依次读取字节。每读取一个字节，该字节就会从 RX FIFO 出队。
    - 注意，根据场景，编程人员在接收数据时可能需要丢弃前 `n_tx` 个数据。这是因为在主器件发送指令/数据时，从器件可能还没有做出相应，而是要等到前 `n_tx` 个数据都发送完成之后才会返回有效的数据。而由于 SPI 的全双工特性，前 `n_tx` 个无效数据同样会被压入 RX FIFO，因此需要丢弃这些数据。
- 如果采用手动片选模式，需要在收发数据之前手动下拉片选信号，并在收发数据之后手动上拉片选信号。

下述代码向 Slave 发送了 `[0x00 0x37]` 两个字节，并从 Slave 读取一个字节。

```c
#include "xspi.h" // axi quad spi
#include "xparameters.h"
#include "xstatus.h"
#include "xplatform_info.h"
#include "xil_printf.h"
#include "sleep.h"

#define SPI_DEVICE_ID       XPAR_SPI_0_DEVICE_ID
#define SPI_BASEADDR		XPAR_SPI_0_BASEADDR

XSpi Spi;

int main() {
/*
 * SPI Initialize
 */
	XSpi_Config *spi_config_ptr;

	spi_config_ptr = XSpi_LookupConfig(SPI_DEVICE_ID);
	if (spi_config_ptr == NULL) {
		return XST_DEVICE_NOT_FOUND;
	}

	status = XSpi_CfgInitialize(&Spi, spi_config_ptr,
				  spi_config_ptr->BaseAddress);
	if (status != XST_SUCCESS) {
		return XST_FAILURE;
	}

	// Start the SPI driver so that the device is enabled.
	XSpi_Start(&Spi);

	// Disable Global interrupt to use polled mode operation
	XSpi_IntrGlobalDisable(&Spi);

/*
 * 1. Enable master mode.
 * 2. CPHA = 1, CPOL = 0
 * 3. Manual Slave Select
 * 4. TX/RX FIFO Reset
 */
	u32 control;
	control = XSpi_ReadReg(SPI_BASEADDR, XSP_CR_OFFSET);
	control |=
				XSP_CR_MASTER_MODE_MASK |	// Master Mode
				XSP_CR_CLK_PHASE_MASK	|	// Clock Phase
				XSP_CR_MANUAL_SS_MASK	|	// Manual Slave Select
				XSP_CR_TXFIFO_RESET_MASK|	// TX FIFO Reset
				XSP_CR_RXFIFO_RESET_MASK	// RX FIFO Reset
				;
	XSpi_WriteReg(SPI_BASEADDR, XSP_CR_OFFSET, control);

	// write [0x00 0x37] and then read one byte
	XSpi_WriteReg(SPI_BASEADDR, XSP_DTR_OFFSET, 0x00);
	XSpi_WriteReg(SPI_BASEADDR, XSP_DTR_OFFSET, 0x37);
	XSpi_WriteReg(SPI_BASEADDR, XSP_DTR_OFFSET, 0x00);


/*
 * SPI write
 */
	XSpi_WriteReg(SPI_BASEADDR, XSP_SSR_OFFSET, 0xE); // slave select // 0xE: 0b1110
	// initiate a transfer
	control = XSpi_ReadReg(SPI_BASEADDR, XSP_CR_OFFSET);
	control |= XSP_CR_ENABLE_MASK;
	control &= ~XSP_CR_TRANS_INHIBIT_MASK;
	XSpi_WriteReg(SPI_BASEADDR, XSP_CR_OFFSET, control);


/*
 * SPI read
 */
	// wait for the transmit FIFO to be empty
	while (!(XSpi_ReadReg(SPI_BASEADDR, XSP_SR_OFFSET) &
					XSP_SR_TX_EMPTY_MASK));
	control = XSpi_ReadReg(SPI_BASEADDR, XSP_CR_OFFSET);
	control |= XSP_CR_TRANS_INHIBIT_MASK;
	XSpi_WriteReg(SPI_BASEADDR, XSP_CR_OFFSET, control);
	// read data receive register
	while ((XSpi_ReadReg(SPI_BASEADDR, XSP_SR_OFFSET) &
				XSP_SR_RX_EMPTY_MASK) == 0) {
		data = XSpi_ReadReg(SPI_BASEADDR, XSP_DRR_OFFSET);
	}
    // we know (in advance) that the slave will return one byte, so we know this loop will be executed three times.

	// slave de-select
	XSpi_WriteReg(SPI_BASEADDR, XSP_SSR_OFFSET, 0xF); // 0xF: 0b1111

	xil_printf("MISO: 0x%x\n\r", data);

	return 0;
}

```

### 4 Linux 编程

为了在 Linux 中使用 AXI Quad SPI IP 核，需要在 Linux 设备树中添加一个 `spidev` 节点，从而允许通过读写 `/dev/spidevx.y` 文件来读写 SPI。

> 在 `/dev/spidevx.y` 中，`x` 代表第 `x` 个 SPI 控制器，`y` 代表第 `y` 个片选。如果使用 PS SPI，那么设备名可能为 `/dev/spidev0.0`；如果使用 PL SPI（AXI SPI），则设备名可能为 `/dev/spidev1.0`。

设备树通常在启动时被 U-Boot 加载好，并且不可修改。但是 4.14 版本之后的 Linux 内核增加了对 device tree overlay（以下简称 DTO）的支持。DTO 允许在运行时动态加载新的设备树。下面是一段 DTO 的源码：

```dts
/dts-v1/;
/plugin/;
/ {
    fragment@0 {
        target = <&amba>;
        overlay0: __overlay__ {                       
            axi_quad_spi_0: axi_quad_spi@80000000 {
                ...
                status = "okay";
                #address-cells = <1>;
                #size-cells = <0>;
                spidev0: spidev@0 {
                    compatible = "spidev";
                    reg = <0>;
                    spi-max-frequency = <5000000>;
                };
            };                
        };
    };
};
```

> 有几个值得注意的点：
> 
> - 需要在 `/dts-v1/;` 后面增加一行 `/plugin/;` 来表示这是一个 Device Tree Overlay 而不是普通的 Device Tree。[ADI 的 recipes-bsp](https://github.com/analogdevicesinc/meta-adi/blob/master/meta-adi-xilinx/recipes-bsp/device-tree/device-tree.bbappend#L151) 就是通过观察文件中是否包含 `/plugin/;` 来判断设备树是否是 Overlay。
> - `target` 表示修改哪一个节点。这里是 `<&amba>`，它会被扩展为符号为 `amba` 的节点的 phandle。例如，如果 `amba` 节点的 phandle 为 `70`，那么 `<&amba>` 实际上代表 `<70>`。一个 phandle 唯一标识了一个节点，往往是由编译器（dtc）分配的。
> - 往往需要增加编译选项 `-@`。该选项启用符号功能，从而允许通过符号对设备树节点进行引用。否则，只能通过 phandle 的绝对值来引用。为了查看 phandle 的绝对值，需要对设备树二进制进行反编译。

通过 DTO 增加 `spidev` 节点后，在 `/dev` 文件夹下就会多出一个 `/dev/spidev1.0` 文件。可以通过读写该文件来进行 SPI 通信。可以用 `ioctl` 来实现。
