---
title: "运行时拉取 Jupyter Widgets UI 组件的状态"
date: 2023-06-30T20:07:39+08:00
draft: false
categories: ["CS"]
tags: ["Python", "Jupyter Notebook"]
---

先看一段 Jupyter Notebook 中的代码：

```python
import time
import ipywidgets as widgets
from IPython.display import display

slider = widgets.IntSlider()
display(slider)

while True:
    print(slider.value)
    time.sleep(1)
```

运行上面的代码，`IntSlider()` 会显示一个可交互的滑块小组件。

当用户滑动滑块时，它的值应当改变，变化的值应当可以在 `while` 循环内打印出来。

然而，如果你运行上面这段代码，打印的滑块值不会有任何改变，一直是初始值。

实际上，只有在所有代码块运行完成之后，滑块的值才会开始更新。在那之前，UI 组件的更新会被运行中的代码块所阻塞。

为了在循环里拉取 UI 组件的值，可以使用 [jupyter-ui-poll](https://pypi.org/project/jupyter-ui-poll/) 库。改动后的代码如下：

```python
import time
import ipywidgets as widgets
from IPython.display import display
from jupyter_ui_poll import ui_events

slider = widgets.IntSlider()
display(slider)

while True:
    with ui_events() as poll:
        poll(1) # poll one event
    print(slider.value)
    time.sleep(1)
```

这段代码每隔 1 秒钟拉取（poll）一次 UI 组件的状态，从而实现想要的功能。

下面是一段应用示例，可以与 python 异步编程结合使用：

```python
import nest_asyncio
nest_asyncio.apply()

import asyncio
from jupyter_ui_poll import ui_events

from pyrtlsdr import RtlSdr

sdr = RtlSdr()

sdr.center_freq = 92_700_000 # an FM radio station running at 92.7MHz

async def streaming():
    it = 0
    async for data in sdr.stream():        
        # perform FM demodulation
        audio = fm_demodulation(data)

        # poll UI events
        with ui_events() as poll:
            poll(10)
            sdr.center_freq = slider.value

        # play the audio
        display(Audio(audio, autoplay=True, rate=48000, normalize=False))
        
        it = it + 1
        if it == it_num:
            break

slider = widgets.IntSlider()

display(slider)
    
asyncio.run(streaming())
```

上面这段代码模拟了一个 FM 收音机。 
