---
title: "A Null Pointer Cannot Be Accessed, but Would the Bytes at That Location Feel Lonely?"
date: 2023-05-16T16:27:25+08:00
originalURL: "https://www.zhihu.com/question/596371908/answer/3030576234"
aliases:
  - "/en/pointer0/"
  - "/en/Post_20240126_0指针不能访问-那那个位置的字节会不会很孤独/"
draft: false
author: "Haifei"
---

There are two cases to consider: physical addresses and virtual addresses.

---

If we are talking about physical address 0x0, then it is not lonely at all. Every time the system resets, the program counter stops by to say hello:

“Hey, buddy, how do I get to the reset interrupt service routine?”

“Go to 0x100000!”

“Thanks!”

This is because, on most architectures, the interrupt vector table is placed at physical address 0x0. And the first interrupt is the reset interrupt.



---

As for virtual address 0x0, since it is not mapped to any physical address, the bytes at its physical location are irrelevant, let alone whether they are lonely: you cannot ask whether someone who does not exist is lonely.

The reason virtual address 0x0 is not allowed to correspond to an actual physical address is to prevent programmer mistakes, such as passing a null pointer and then having that null pointer translated into a real physical address. This could result in accidentally accessing somewhere the programmer did not intend to access.

To avoid programmer mistakes, modern operating systems simply reserve 0x0 and do not allow it to correspond to any real address. That way, when programmers make a mistake, the operating system can immediately tell them that they wrote something wrong.

If the operating system is bypassed and virtual address 0x0 is forcibly accessed, it will most likely report an MMU Translation fault. This is because the MMU cannot find a physical address corresponding to 0x0. This type of error is a hardware error and is fatal; it will most likely cause a crash or blue screen and require a hardware reset to resolve.

Of course, most people are not bored enough to bypass the operating system. In that case, the operating system will gently tell you that an error has occurred, and this error will not cause a crash or blue screen. From this, we can see that programmers' peaceful days depend on the operating system bearing the burden and pressing onward.

