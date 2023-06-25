---
title: "工作总结"
date: 2023-06-25T14:14:15+08:00
draft: false
---

> 给从今年三月到现在断断续续的工作做一个总结

## 1  AD9361 + PYNQ 内核

### 1.1 现有工作

这个工作基本上来说就是通过 Petalinux 将 PYNQ 和 AD9361 的驱动构建到同一个内核中。

在 ZedBoard 上，[2019_R1](https://github.com/analogdevicesinc/meta-adi/tree/2019_R1) + [PYNQ v2.4](https://github.com/Xilinx/PYNQ/tree/image_v2.4) 版本可以成功。启星和我在这个[链接](https://github.com/hfwang132/zedboard-adi-pynq)中总结了构建的步骤以及各种可能的问题和解决办法。

在 PYNQ-ZU 上，由于 PYNQ-ZU 的 BSP 只有 PYNQ v2.7 及以后的版本，而 PYNQ v2.7 需要配合 2020 年版本的工具链，并且在该版本遇到了一些问题（见 1.2.1 节），因此没有成功。

### 1.2 遇到的问题

#### 1.2.1 ADI 的 Yocto Layer 与 PYNQ 不兼容

**2019 年之后的版本**的 [meta-adi](https://github.com/analogdevicesinc/meta-adi) 的 [recipes-bsp](https://github.com/analogdevicesinc/meta-adi/blob/master/meta-adi-xilinx/recipes-bsp/device-tree/device-tree.bbappend#L166) 会覆盖掉 PYNQ 的 [recipes-bsp](https://github.com/Xilinx/PYNQ/blob/master/sdbuild/boot/meta-pynq/recipes-bsp/device-tree/device-tree.bbappend) 所引入的修改。

如下是文件 `meta-adi-xilinx/recipes-bsp/device-tree/device-tree.bbappend` 的一部分：

```bb
do_configure:append() {
    ...
    cp "${KERNEL_DTB_PATH}/${KERNEL_DTB}.dts" "${DT_FILES_PATH}/system-top.dts"
    ...
}
```

它直接将 `system-top.dts` 覆盖掉。而更合适的实践应该是向 `system-top.dts` 中[增加代码](https://github.com/Xilinx/PYNQ/blob/image_v3.0.1/sdbuild/boot/meta-pynq/recipes-bsp/device-tree/device-tree.bbappend#L22)（PYNQ 就是这么做的）。

由于这个原因，没有构建出 [ADI master branch](https://github.com/analogdevicesinc/meta-adi) + PYNQ v3.0.1 的内核。也许可以对 [recipes-bsp](https://github.com/analogdevicesinc/meta-adi/blob/master/meta-adi-xilinx/recipes-bsp/device-tree/device-tree.bbappend#L166) 做一些修改从而使其与 PYNQ 兼容，但是这个工作搁置了。并且我们有理由搁置这个工作，见下一节（第 1.2.2 节）。

另外，Yocto 官方建议，当使用多个 Yocto Layer 的时候，应该要去 [OpenEmbedded Layer Index](https://layers.openembedded.org/layerindex/branch/master/layers/) 和 [Yocto Project Compatible Index](https://www.yoctoproject.org/software-overview/layers/) 查看不同的 Layer 之间是否兼容。这两个 Index 并未收录到 meta-pynq 和 meta-adi。

#### 1.2.2 FPGA MANAGER 的问题

[meta-adi-xilinx 的文档](https://github.com/analogdevicesinc/meta-adi/tree/master/meta-adi-xilinx#fpga-manager)明确提到了他们没有对 FPGA MANAGER 的官方支持。而如果禁用 FPGA MANAGER，那么就无法在板卡启动之后重载比特流。这让 PYNQ 失去了意义。

**我猜 ADI 的想法是将 FPGA 作为一个功能固定的外设，即，设备树和比特流都在系统启动的时候加载好，并且不希望被修改。这与 PYNQ 的想法从根本上是矛盾的**。

因此，不建议将 AD9361 和 PYNQ 的驱动集成在一个内核中，而是允许系统启动后动态地加载 AD9361 的设备树和比特流，见下一节（第 2 节）。

## 2  User-Space AD9361 驱动

为了绕开上一节提到的困难，可以在用户空间中使用 AD9361 驱动，而不是将驱动集成到内核中。但是，为了与 AD9361 的 SPI 接口通信，需要在 Linux 设备树中添加一个 `spidev` 节点，从而允许通过读写 `/dev/spidevx.y` 文件来读写 SPI

> 在 `/dev/spidevx.y` 中，`x` 代表第 `x` 个 SPI 控制器，`y` 代表第 `y` 个片选。如果使用 PS SPI，那么设备名可能为 `/dev/spidev0.0`；如果使用 PL SPI（AXI SPI），则设备名可能为 `/dev/spidev1.0`。

设备树通常是在启动时被 U-Boot 加载好，并且不可修改的。但是 4.14 版本之后的 Linux 内核增加了对 device tree overlay 的支持，它允许在运行时动态加载新的设备树。PYNQ 库也提供了 [API](https://pynq.readthedocs.io/en/latest/pynq_package/pynq.overlay.html#pynq.overlay.Overlay) 来实现这个操作：

```python
class pynq.overlay.Overlay(bitfile_name, dtbo=None, download=True, ignore_version=False, device=None, gen_cache=False)
```

这个 API 不仅允许下载比特流（`bitfile_name`），而且允许动态增量加载新的设备树（`dtbo`）。

```dts
/dts-v1/;
/plugin/;
/ {
    fragment@0 {
        target = <&amba>;
        overlay0: __overlay__ {                       
            axi_quad_spi_0: axi_quad_spi@80000000 {
                bits-per-word = <8>;
                clock-names = "ext_spi_clk", "s_axi_aclk";
                clocks = <&zynqmp_clk 71>, <&zynqmp_clk 71>;
                compatible = "xlnx,axi-quad-spi-3.2", "xlnx,xps-spi-2.00.a";
                fifo-size = <16>;
                interrupt-names = "ip2intc_irpt";
                interrupt-parent = <&gic>;
                interrupts = <0 104 1>;
                num-cs = <0x1>;
                reg = <0x0 0x80000000 0x0 0x10000>;
                xlnx,num-ss-bits = <0x1>;
                xlnx,spi-mode = <0>;
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
