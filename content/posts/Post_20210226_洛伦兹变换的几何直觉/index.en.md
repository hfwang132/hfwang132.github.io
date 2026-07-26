---
title: "Geometric Intuition for Lorentz Transformations"
date: 2021-02-26T23:05:45+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/353230273"
author: "Haifei"
tags: ["Relativity"]
categories: ["Methods of Mathematical Physics"]
---

You do not need to know any formulas to gain an intuitive understanding of various phenomena in special relativity (length contraction, time dilation, the twin paradox, etc.).

---

## A Small Modification to the Galilean Transformation  

Let us first look at the classical Galilean transformation. In a t-x diagram, the Galilean transformation appears as a shear transformation. Points slide along lines parallel to the x-axis.

{{< figure src="images/v2-1434b48b249a720bee168ee9630156e7_r.jpg" >}}

Galilean transformation, viewed from Little Red's and Little Green's perspectives

  
  

For the Lorentz transformation in special relativity, the lines used for sliding are no longer the straight lines in the figure above, but rather one branch of a hyperbola.

{{< figure src="images/v2-60bedce6616d3e6ea971d5b3d95e6b27_r.jpg" >}}

Lorentz transformation, viewed from Little Red's and Little Green's perspectives. This figure is a silent proof of the time dilation effect

  
  
## How Should This Hyperbola Be Interpreted?  

1. The worldlines (line segments) connecting the origin to points on the hyperbola have the same proper time. In other words, in the figure above, the watches on Little Red's and Little Green's own wrists have elapsed the same amount of time.

Although Little Red's time differs in the eyes of different observers, the time she experiences is uniquely determined in her own view; this is proper time. Proper time is the time experienced by the reference frame itself.

If Little Red is taken as the reference frame, then the length of the red line segment in the figure on the left is Little Red's proper time.

2. When they each look at the other, both feel that the other's time passes more slowly. This can be seen simply by drawing a straight line parallel to the x-axis.

3. The asymptotes of the hyperbola are the worldlines of light.

4. The reciprocal of the slope is velocity. We can see that no matter how a point slides along the hyperbola, the reciprocal of its slope can never reach the speed of light. A worldline can only approach an asymptote infinitely closely.

5. Lines of simultaneity and worldlines are symmetric about the asymptotes. If a worldline is vertical, then its line of simultaneity is horizontal. If a worldline is not vertical, then see the figure below

{{< figure src="images/v2-3018abd2f2aa19d0a2e95c69abc11846_r.jpg" >}}

The green dashed lines are Little Green's lines of simultaneity. The upper green dashed line is tangent to the hyperbola, while the lower green dashed line and the solid green line are symmetric about an asymptote

  
  

For Little Green, her lines of simultaneity (green dashed lines) and her worldline (solid green line) are symmetric about an asymptote.

Why are they symmetric? If you know a little about linear transformations, you should have this intuition about them: linear transformations preserve the parallelism of grid lines. Look at the figure below

{{< figure src="images/v2-54a6605a9eff52807f7755757da3fb6c_r.jpg" >}}

The Lorentz transformation is a linear transformation; the linear transformation simultaneously stretches the grid and the lines of simultaneity (dashed lines in the figure)

  
  

Observe this figure and think about how the red grid is stretched into the green grid. Then you can see how the originally horizontal lines of simultaneity (red dashed lines) are transformed into slanted lines of simultaneity (green dashed lines). Note that this figure is a silent proof that “lines of simultaneity and worldlines are symmetric about the asymptotes.”

You can imagine a hand pulling the thick solid red line in the figure above along the hyperbola to the position of the thick solid green line. The accompanying change in the grid is the Lorentz transformation of every point in the plane.

In fact, the lines of simultaneity are tangent to the hyperbola, so from Little Green's perspective, Little Red's time passes more slowly. This does not contradict the fact that, in Little Red's eyes, Little Green's time passes more slowly.

## What Is the Use of the Geometric Intuition Above?  

1. It can intuitively explain the time dilation effect, because lines of simultaneity are tangent to the hyperbola.

2. It can intuitively explain the length contraction effect. To do so, we need to draw another figure.

{{< figure src="images/v2-a47157582355cbeca375e617c8642fa3_r.jpg" >}}

Length contraction effect. Note that the green dashed line appears longer than the red dashed line, but it is actually shorter!

  
  

The red and green dashed lines in the figure are lines of simultaneity. To measure the length of an object, the positions of both ends must be measured at the same moment (you cannot measure the position of one end now and measure the position of the other end one second later).

From the figure, the moving object appears to be longer (the green dashed line), but the length contraction effect tells us that a moving object becomes shorter.

This is because four-dimensional spacetime is not a Euclidean space, but a Minkowski space. In Euclidean space, the distance between two points is \(s=\sqrt{x^2+y^2}\) , but in Minkowski space, the “spacelike interval” between two points is \(s=\sqrt{x^2-t^2}\) , with a minus sign added to the square of time. Thus, the green dashed line is actually shorter than the red dashed line.

(Note: Corresponding to the “spacelike interval,” there is also a “timelike interval.” The former represents distance in space, while the latter represents distance in time. The former is defined as \(\sqrt{x^2-t^2}\) , and the latter is defined as \(\sqrt{t^2-x^2}\) )

3. It can intuitively explain why velocity addition still cannot exceed the speed of light.

{{< figure src="images/v2-dbcfda7e063841d2b2efc9700ae1e633_r.jpg" >}}

In the figure on the left, Little Red moves at 0.5 times the speed of light relative to Little Blue, and Little Green also moves at 0.5 times the speed of light relative to Little Red. Then, from Little Blue's perspective, can Little Green's velocity equal the speed of light?

The figure on the right clearly shows that, from Little Blue's perspective, Little Green's velocity does not catch up with the speed of light. However, from Little Red's perspective, Little Green is indeed moving at 0.5 times the speed of light relative to her, because Little Green's worldline bisects the red dashed line in the figure.

4. It can explain the twin paradox

(To be continued)

---

## Q&A：  

Q: How is the length of a curve calculated in Minkowski space?

A: Simply divide the curve into many small line segments, calculate their lengths separately according to \(s=\sqrt{x^2-t^2}\) , and then add them together.
