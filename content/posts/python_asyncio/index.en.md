---
title: "Python coroutines and asyncio"
date: 2023-06-13T22:05:41+08:00
draft: false
categories: ["CS"]
tags: ["Python"]
---

Recently, I have been using Python coroutines/asynchronous programming in a project. Now, I will summarize my experience.

## Import

```python
import asyncio
```

If `asyncio` is to be used in an IPython environment, we have to add two more lines：

```python
import nest_asyncio
nest_asyncio.apply()
import asyncio
```

## Coroutines

Coroutines are the core of asynchronous programming in Python. To define a coroutine, you need to use `async def`.


```python
async def main():
    # do something
    print("Hello world!")
```

To execute the coroutine, you cannot directly call `main()`. Instead, you need to use `run()`:

```python
asyncio.run(main())
```

To nest one coroutine within another, similar to nesting one function within another, you can use `await`:

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

When nesting coroutines within another coroutine, you need to use `await` to invoke them. If you write it directly as follows:

```python
async def main():
    coro_1()
    coro_2()
    print("Hello World!")
```

You will receive the following warnings:

```
01.py:10: RuntimeWarning: coroutine 'coro_1' was never awaited
  coro_1()
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
01.py:11: RuntimeWarning: coroutine 'coro_2' was never awaited
  coro_2()
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
Hello World!
```

As can been seen, `coro_1` and `coro_2` has not been called.

## Tasks

We would lose the point if we use coroutines in the way as shown in the previous section. The true significance of coroutines lies in their ability to be executed concurrently. Consider the following code:

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

In this code, we used `create_task` to create tasks `task_1` and `task_2` for `coro_1` and `coro_2` respectively. They are actually executed together. To verify this, we can add some delays:

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

The results are:

```
I am the coroutine 1.
I am the coroutine 2.
Elapsed: 1.001298 s
```

If we do not use `create_task` but rather directly `await` the two coroutines:

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

Then the outcomes are:

```
I am the coroutine 1.
I am the coroutine 2.
Elapsed: 2.002527 s
```

In other words, if we don't use `create_task` to create tasks, `coro_2()` will not be executed until `coro_1()` has finished.

From this example, we can observe that the true meaning of `await` is "wait for the task to complete".

Furthermore, we can use `gather` to run multiple coroutines concurrently:

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

### Asynchronous For loop

Now we can look at `async for`.

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

The result is:

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

By combining `async for` and `yield`, we can create an asynchronous generator. In reality, an asynchronous generator is an instance of a class that has `__aiter__` and `__anext__` methods. Here's an equivalent implementation of the previous code:


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

## Example

At last, I will give an example of using `asyncio` in a project:

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

This is an FM radio application that uses `async for` to read data from the receiver, demodulate the data into audio signals and finally play the audio in a streamed manner. In other words, we are essentially processing and streaming the audio data in real time.