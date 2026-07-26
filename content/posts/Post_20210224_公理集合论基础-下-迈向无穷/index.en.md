---
title: "Foundations of Axiomatic Set Theory (Part II): Toward Infinity"
date: 2021-02-24T22:21:02+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/346542841"
author: "Haifei"
tags: ["Set Theory"]
categories: ["Methods of Mathematical Physics"]
---

## Link to the Previous Article  
[Foundations of Axiomatic Set Theory (Part I): The Empty Set and Russell's Paradox](https://zhuanlan.zhihu.com/p/346371552)## Constructing Natural Numbers (ZF3: Axiom of Pairing, ZF4: Axiom of Union)  

In the previous article, we successfully defined a unique set called the empty set and resolved Russell's paradox. Next, we will use the empty set to construct more sets. To do so, we need more constructive axioms.

> Axiom of Pairing: \(\forall a \forall b \exists c \forall x((x\in c)\leftrightarrow (x=a )\vee (x=b))\)

It states that, for arbitrary a and b, one can construct a set c containing a and b, and only a and b. This is also a constructive axiom.

Since the empty set is all we currently have available, let us try using it.

Replacing a and b in the axiom of pairing with the empty set \(\emptyset \), we obtain a set \(\{\emptyset,\emptyset\}\), which, according to the axiom of extensionality, equals \(\{\emptyset\}\).

Likewise, we can also construct \(\{\{\emptyset\}\}\), \(\{\{\{\emptyset\}\}\}\), and so on.

Replacing a and b in the axiom of pairing with \(\emptyset \) and \(\{\emptyset\}\), we can obtain \(\{\emptyset,\{\emptyset\}\}\), and so forth.

This allows us to construct many sets, but we still cannot construct a set with more than two elements. For example, \(\{\emptyset,\emptyset\}\) has only one element, \(\{\emptyset,\{\emptyset\}\}\) has two elements, and so on.

To construct sets containing more elements, let us introduce another axiom:

> Axiom of Union: \(\forall x \exists X \forall u(\exists t(u\in t\wedge t\in x ) \leftrightarrow  u \in X)\)

It is somewhat laborious to interpret these symbols directly, so let us illustrate the meaning of this axiom with an example.

Suppose we have a set \(x=\{\{a\},\{b,c\}\}\). This set has two elements and can be obtained using the axiom of pairing. The axiom of union allows us to construct \(X=\{a,b,c\}\) from it. That is, we can construct a new set such that every element of every element in \(x\) belongs to \(X\).

Write \(X=\bigcup x\), and call \(X\) the union of \(x\). In particular, write \(x\cup y=\bigcup \{x,y\}\). This is the familiar union operation on sets. In the example above, this means that we can construct the union of two sets, \(\{{a,b}\}\cup \{c\} = \{a,b,c\}\).

In this way, we can construct sets with more than two elements. Indeed, by combining a set of n elements with a set of one element, we can construct a set of (n+1) elements. Thus, as long as we continue doing this, given any finite number of objects, we can construct a set having these objects as its elements.

We can now define operations such as intersection and difference; these are omitted here, and readers may try defining them on their own.

> 【Optional Reading】We can now also define subsets and proper subsets; this is very easy:  
>  \(\forall u(u\in X \rightarrow u\in Y)\rightarrow X\subseteq Y\)   
> We all know that the empty set is a subset of every set. This string of symbols also handles the case of the empty set. Since for any \(u\), \(u\in \emptyset\) is a false proposition, and a false proposition implies any proposition, it can also imply \(u\in Y\), (where \(Y\) is an arbitrary set), and thus \(\emptyset\subseteq Y\). This shows that the convention that “a false proposition implies any proposition” is very useful.

At this point, we can define natural numbers:

> First, define \(\emptyset=0\).  
>   
> By the axiom of pairing, we can construct \(\{\emptyset\}\). Define \(\{\emptyset\}=1\), namely \(\{0\}=1\).  
>   
> Next, we can define \(\{0,1\}=2\).  
>   
> By the axiom of union, given any finite number of objects, we can construct a set having these objects as its elements. Therefore, we can define \(\{0,1,2\}=3\).  
>   
> And so on.

Notice the idea of “encapsulation” here: once we have defined the natural number “3”, we no longer write it as \(\{\emptyset,\{\emptyset\},\{\emptyset,\{\emptyset\}\}\}\).

You may not be entirely satisfied with the words “and so on.” Therefore, let us now define the successor of a natural number:

\[S(x):=x\cup\{x\}\]

A colon followed by an equals sign denotes a definition. Thus, we have \(1=S(0)\), \(2=S(1)\), and so on.

Note that zero is not the successor of any natural number. This is an axiom in Peano arithmetic, but it can be proved in the axiomatic system of set theory. The proof is left as an exercise for interested readers (hint: use proof by contradiction and the fact that the empty set has no elements).

Why define it as above rather than directly defining \(1=\{0\},\,2=\{1\},\, 3=\{2\},\cdots\)? Because with the previous definition, we have \(1\subseteq2,\, 1\subseteq3,\,2\subseteq3,\cdots\), and so on, giving us a natural ordering relation. With the latter definition, although we still have \(1\subseteq2,\,2\subseteq3,\cdots\), \(1\subseteq3\) no longer holds, so we lose a natural ordering relation.

Our mathematical universe now has a new kind of object—the natural numbers. We can subsequently use natural numbers to define integers, rational numbers, real numbers, complex numbers, and so on. Clearly, the edifice of mathematics is built brick by brick.

Now that we have defined natural numbers, can we define the set of natural numbers \(\{0,1,2,\cdots\}\)? That is, a set of which every natural number is an element.

Unfortunately, no. The axiom of union can guarantee only “any finite number,” not “infinitely many.” In other words, give me any finite number of natural numbers, and I can use the axiom of union to construct a set of which those natural numbers are all elements.

However, if you ask me to construct a set **in advance** such that every number you provide afterward belongs to it, this currently cannot be done. This is precisely the distinction between “potential infinity” and “actual infinity.”

The same principle applies in everyday life. Your client should specify the objective first and then have you carry it out, rather than specifying the objective only after you have finished.

But mathematics will not stop here. We wish to study “actual infinity,” that is, genuine infinity, leaving the client with nothing to nitpick.

## Toward Infinity (ZF6: Axiom of Infinity, ZF5: Axiom of Power Set, ZF8: Axiom Schema of Replacement)  
> Axiom of Infinity: \(\exists X(\emptyset \in X \wedge \forall x(x\in X \rightarrow x\cup\{x\}\in X))\).

It means that there exists a set \(X\) such that the empty set belongs to it, and for every element of it, the successor of that element also belongs to it. In this way, we obtain the set of natural numbers. This is a truly infinite set.

> Axiom Schema of Replacement: \(\forall A\exists B(B=\{y|\exists x(x\in A\wedge\varphi(x,y)\,)\})\)

It means that the image of any set under a function is still a set.

Combining the axiom schema of replacement with the axiom of infinity, we can obtain all kinds of countably infinite sets. For example, to construct the set of even numbers, we need only let \(\varphi\) be \(\varphi(x,y):y=2x\).

However, this yields only countably infinite sets. Can we construct infinite sets of greater cardinality? The axiom of power set can do this.

> Axiom of Power Set: \(\forall X\exists Y\forall u(u\in Y\leftrightarrow u\subseteq X)\)

It means that we can construct a new set whose elements are all the subsets of a given set. We call this set the power set of the original set, denoted \(\mathcal{P}(X)\).

In this way, we can generate “more infinite” sets. Their “cardinality” is greater than that of countably infinite sets.

Readers may try using the axiom of infinity to prove the axiom of existence. In that case, we can discard the axiom of existence (see the previous article).

## Eliminating Pathologies (ZF7: Axiom of Regularity)  

Does there exist a set that belongs to itself?

Does there exist such a set \(\{x_0,x_1,\cdots\}\) that, for every \(n\), we have \(x_{n+1}\in x_n\)? In other words, does there exist an infinite descending chain with respect to membership?

The sets in the two examples above are both rather pathological. To eliminate such pathologies, we need the axiom of regularity.

> Axiom of Regularity: \(\forall x(x\neq \emptyset\rightarrow \exists y(y\in x\wedge x\cap y=\emptyset))\)

It states that every nonempty set \(x\) has a minimal element \(y\) with respect to “\(\in\).” In other words, every nonempty set \(x\) contains an element \(y\) such that no element of \(x\) belongs to \(y\).

Readers may try using the axiom of regularity to prove that “no set belongs to itself.” This can also resolve Russell's paradox.

There is an interesting fact about the axiom of regularity: even if we remove the axiom of regularity (ZF7), the remaining ZF axioms cannot construct the pathological objects that it forbids. If so, why do we still need ZF7?

The answer is that although we can construct new sets only through axioms, from an ontological perspective we have not ruled out the possibility that our set-theoretic universe already contains a class of pathological sets forbidden by ZF7. They need not be constructed from anything else; they simply exist in the universe. Thus, like ZF0, ZF7 is an ontological commitment. ZF0 commits to “the existence of certain things,” whereas ZF7 commits to “the nonexistence of certain things.”

## Axiom of Choice  

The axiom of choice is so important that its name deserves to be the title of this section. However, there is already far too much popular exposition about it, so there is no need for this article to reinvent the wheel. Only its expression is given here:

\[\forall X[\emptyset\notin X\wedge\forall x\forall y(x\in X\wedge y\in X\rightarrow x\cap y=\emptyset)\rightarrow\exists S \forall x(x\in X\rightarrow\exists !y(S\cap x=\{y\}))]\]

Here, \(\exists!y\) means “there exists a unique y.”

It is worth noting that the axiom of choice is not part of the ZF system. ZF system + axiom of choice = ZFC system. Mainstream mathematics uses the ZFC system.

There are many interesting facts about the axiom of choice. Readers are encouraged to search for them online; they will not be elaborated upon here.

## Summary  

At this point, we have introduced all nine axioms of ZFC axiomatic set theory. They are:

ZF1 Axiom of Extensionality

ZF2 Axiom Schema of Separation

ZF3 Axiom of Pairing

ZF4 Axiom of Union

ZF5 Axiom of Power Set

ZF6 Axiom of Infinity

ZF7 Axiom of Regularity

ZF8 Axiom Schema of Replacement

C Axiom of Choice

The first eight axioms constitute the so-called “ZF” axiomatic system; adding the axiom of choice yields the “ZFC axiomatic system.” “Z” and “F” are the initials of the names of its proposers; “C” stands for “Axiom of Choice”—the axiom of choice.
