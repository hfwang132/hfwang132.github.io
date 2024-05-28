---
title: "Polling Jupyter widget UI events in runtime"
date: 2023-07-01T17:48:54+08:00
draft: false
categories: ["CS"]
tags: ["Python", "Jupyter Notebook"]
---

Let's look at a code snippet in the Jupyter Notebook:

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

`IntSlider` is an interactive Jupyter Notebook widget. When the user interacts with the slider, the slider value should change.

However, if you run the above codes, you will find that the printed value of the slider won't change at all -- it will be stuck at its initial value.

---

In fact, the UI elements won't be updated until all code blocks are finished executing. In other words, the update of the UI elements is *blocked* by the execution of any code block.

In order to poll the states of UI elements inside a running loop, we can use the [jupyter-ui-poll](https://pypi.org/project/jupyter-ui-poll/) library. The modified codes are as follows:

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

