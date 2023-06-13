---
title: "Python 协程/异步IO"
date: 2023-06-13T22:05:45+08:00
draft: false
categories: ["EECS"]
tags: ["Python"]
---

最近做项目用到 Python 协程/异步，现在总结一下：

## 导入

```python
import asyncio
```

如果在 IPython 环境里使用，需要加两行：

```python
import nest_asyncio
nest_asyncio.apply()
import asyncio
```

## 协程

协程（coroutines）是 Python 异步编程的核心。一个 coroutine 要用 `async def` 来定义。

```python
async def main():
    # do something
    print("Hello world!")
```

为了运行它，不能直接调用 `main()`，而是需要用 `run()`：

```python
asyncio.run(main())
```

如何在一个协程里嵌套另一个协程呢？就像我们在一个函数里嵌套另一个函数那样。你需要使用 `await` 语句：

```python
import asyncio

async def coro_1():
    print("I am the coroutine 1.")

async def coro_2():
    print("I am the coroutine 2.")

async def main():
    await coro_1()
    await coro_2()
    print("Hello World!")

asyncio.run(main())
```

协程嵌套在另一个协程里，需要使用 `await` 来调用。如果直接写成下面这样：

```python
async def main():
    coro_1()
    coro_2()
    print("Hello World!")
```

则会收到警告如下：

```
01.py:10: RuntimeWarning: coroutine 'coro_1' was never awaited
  coro_1()
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
01.py:11: RuntimeWarning: coroutine 'coro_2' was never awaited
  coro_2()
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
Hello World!
```

可以看到，`coro_1` 和 `coro_2` 并没有被调用。

## 任务

如果像上一节那样使用协程，那么协程就失去了它的意义。协程真正有用的地方，在于它们可以并发执行。考虑如下代码：

```python
import asyncio

async def coro_1():
    print("I am the coroutine 1.")

async def coro_2():
    print("I am the coroutine 2.")

async def main():
    task_1 = asyncio.create_task(coro_1())
    task_2 = asyncio.create_task(coro_2())

    await task_1
    await task_2

    print("Hello World!")

asyncio.run(main())
```

在这个代码中，我们用 `create_task` 为 `coro_1` 和 `coro_2` 分别创建了任务 `task_1` 和 `task_2`。它们实际上是被一起执行的。为了验证这一点，我们加入一些延时：

```python
import asyncio
import time

async def coro_1():
    print("I am the coroutine 1.")
    await asyncio.sleep(1)

async def coro_2():
    print("I am the coroutine 2.")
    await asyncio.sleep(1)

async def main():
    st = time.time()

    task_1 = asyncio.create_task(coro_1())
    task_2 = asyncio.create_task(coro_2())

    await task_1
    await task_2

    et = time.time()

    print("Elapsed: %f s" % (et - st))

asyncio.run(main())
```

运行结果如下：

```
I am the coroutine 1.
I am the coroutine 2.
Elapsed: 1.001298 s
```

而如果不使用 `create_task`，直接 `await` 两个协程：

```python
import asyncio
import time

async def coro_1():
    print("I am the coroutine 1.")
    await asyncio.sleep(1)

async def coro_2():
    print("I am the coroutine 2.")
    await asyncio.sleep(1)

async def main():
    st = time.time()

    await coro_1()
    await coro_2()

    et = time.time()

    print("Elapsed: %f s" % (et - st))

asyncio.run(main())
```

那么结果如下：

```
I am the coroutine 1.
I am the coroutine 2.
Elapsed: 2.002527 s
```

也就是说，如果不使用 `create_task` 来创建任务，那么 `coro_2()` 实际上是在 `coro_1()` 执行完之后才开始被执行的。

从这个例子中我们可以看出，`await` 真正的意思是“等待任务完成”。

另外，也可以使用 `gather` 来同时运行两个协程：

```python
import asyncio

async def coro_1():
    print("Coroutine 1 starts")
    await asyncio.sleep(1)
    print("Coroutine 1 finishes")

async def coro_2():
    print("Coroutine 2 starts")
    await asyncio.sleep(2)
    print("Coroutine 2 finishes")

async def main():
    print("Starting main coroutine")
    await asyncio.gather(coro_1(), coro_2())
    print("Main coroutine finished")

asyncio.run(main())
```

### 异步循环

现在我们来看看 `async for`。

```python
import asyncio
import time
 
async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield i
 
async def custom_coroutine():
    async for item in async_generator():
        print(item)
        time.sleep(1)
 
st = time.time()
asyncio.run(custom_coroutine())
et = time.time()

print("Elasped: %f s" % (et - st))
```

运行结果为

```
0
1
2
3
4
5
6
7
8
9
Elasped: 10.013134 s
```

将 `async for` 和 `yield` 组合使用，可以得到一个异步生成器。实际上，一个异步生成器是定义了 `__aiter__` 和 `__anext__` 方法的类实例。下面给出与上述代码等价的实现：

```python
import asyncio
import time

class AsyncGenerator:
    def __init__(self, N):
        self.i = 0
        self.N = N

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        if i >= self.N:
            raise StopAsyncIteration
        await asyncio.sleep(1)
        self.i += 1
        return i

async def main():
    async for p in AsyncGenerator(10):
        print(p)

st = time.time()
asyncio.run(main())
et = time.time()
print("Elasped: %f s" % (et - st))    
```

## 案例

最后给出一个我在项目中使用到的案例：

```python
sdr = RtlSdr()
sdr.center_freq = 92_700_000 # an FM radio station running at 92.7MHz

async def main():
    async for data in sdr.stream():        
        # perform FM demodulation
        audio = fm_demodulation(data)
        # play the audio
        display(Audio(audio, autoplay=True, rate=48000, normalize=False))

asyncio.run(main())
```

这是一个 FM 收音机应用，使用 `async for` 来从收音机读取数据，然后在 `async for` 循环内对数据进行解调和播放。以这种方式，我们就能实现对音频数据的实时流处理。
