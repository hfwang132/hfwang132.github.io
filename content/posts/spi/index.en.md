---
title: "Hardware & Software Design of AXI Quad SPI IP Core"
date: 2023-07-01T17:49:31+08:00
draft: false
categories: ["EECS"]
tags: ["SPI", "Embedded Systems"]
---

### 1 Basics

SPI has three-wire mode and four-wire mode. The three-wire mode consists of three wires - `SS` (Slave Select), `SCK` (SPI Clock), and `MOSI` (Master-In-Slave-Out). The four wire mode has an extra line called `MISO` (Master-In-Slave-Out).

|Signals|Full Name|
|-|-|
|SS|Slave Select|
|SCK|SPI Clock|
|MOSI|Master-Out-Slave-In|
|MISO|Master-In-Slave-Out|

SPI clock has four modes: CPOL=0/1 and CPHA=0/1. CPOL stands for clock polarity -- clock low or high when in idle. CPHA stands for clock phase -- data valid at 0 degree or 180 degrees.

### 2 AXI Quad SPI IP Core

When we run out of Zynq PS SPI controllers for some reason, we can turn to PL SPI IP cores, which is called AXI Quad SPI.

{{< figure src="files/axi-quad-spi.png" title="AXI Quad SPI IP core" >}}

In the picture, `io1_i` connects to MISO; `ext_spi_clk` and `s_axi_clk` can be connected to a same system clock. `ip2intc_irpt` can be connected to the Zynq interrupt `pl_ps_irq`.

You can double-click on the IP core to configure clock divider, number of slave selects, and more.

### 3 Bare-Metal Programming

The programming sequence is as follows:

- First, initialize the SPI controller. Set the value of all registers to their default values.
- Next, depending on your needs, configure the SPI controller. For example, the clock mode (CPHA and CPOL) and slave select mode (auto or manual).
- Then, depending on the number of bytes need to be written and read, write to the DTR (Data Transmit Register) the corresponding number of bytes. Each written byte will be shifted into the TX FIFO.
    - Note: If the number of written bytes is `n_tx` and the number of read bytes is `n_rx`, then we should not only write `n_tx` bytes to the DTR, but also write another `n_rx` "dummy" bytes. This is because SPI, in nature, is a full-duplex protocol -- in order to receive `n_rx` bytes, you also need to send `n_rx` bytes.
- Finally, read the bytes out of the DRR (Data Receive Register). When the DRR is read, the read byte will be dequed.
    - Note: depending on the scene, when receiving from the slave, the programmer may need to discard the first `n_tx` bytes. This is because when the master is sending data/instructions, the slave may not yet respond. Rather, the slave will not respond until the master has sent all of the bytes (instruction & data). But due to the full-duplex nature of the SPI protocol, the first `n_tx` dummy bytes will also be pushed into the RX FIFO. Therefore, one may need to discard those bytes.
- If we use the manual slave select mode, we should assert the SS signal before the transfer and de-assert the SS signal after the transfer.

The following code sends two bytes `[0x00 0x37]` to the slave and reads one byte from the slave.

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

### 4 Linux Programming

In order to use the AXI Quad SPI IP core in Linux, we should add a `spidev` node to the device tree, so that we could achieve SPI communication by reading from or writing to the `/dev/spidevx.y` device.

> In `/dev/spidevx.y`, `x` stands for the x-th SPI controller, and `y` stands for the y-th chip.

The device tree is usually initialized during boot-up and is read-only. However, after the 4.14 version of the Linux kernel, we can use the "device tree overlay" (briefed as DTO from now on) to dynamically add incremental device trees. Below is a code snippet of DTO.

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

> Some points to be noted:
> 
> - We should add one more line `/plugin/;` after `/dts-v1/;` to show that this is an DTO file rather than an ordinary device tree file.
> - `target` stands for which node is to be modified. Here it is `<&amba>`, and it will be extended to the phandle of the node which has the symbol `amba`. For example, if the phandle of `amba` is `70`, then `<&amba>` virtually stands for `<70>`. A phandle uniquely denotes a node and is usually allocated by the device tree compiler.
> - In most cases, we should add the `-@` compiler option, which enables support for symbol. Otherwise we can only reference the nodes by their phandle, which requires de-compiling the device tree binaries.
