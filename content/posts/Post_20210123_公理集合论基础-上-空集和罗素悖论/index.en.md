---
title: "Foundations of Axiomatic Set Theory (Part I): The Empty Set and Russell's Paradox"
date: 2021-01-23T17:41:35+08:00
draft: false
math: true
originalURL: "https://zhuanlan.zhihu.com/p/346371552"
author: "Haifei"
tags: ["Set Theory"]
categories: ["Mathematical Physics Methods"]
---

## Preview  

After reading this article, you will understand the first three axioms of ZF axiomatic set theory—the Axiom of Existence, the Axiom of Extensionality, and the Axiom Schema of Separation—and use them to resolve Russell's paradox and define the empty set.

## Introduction  

We often hear statements such as “set theory is the foundation of modern mathematics.” In the eyes of many people, the set theory learned in secondary school consists merely of sets and simple operations—how could that be foundational? To understand this, we must understand how set theory was axiomatized.

Since Euclid's *Elements*, the idea of axiomatization has become deeply ingrained. There is no need to elaborate on the significance of axiomatization. The axiomatization of calculus resolved the second crisis in mathematics (Berkeley's criticism of the “infinitesimals” in Newtonian calculus); the axiomatization of set theory resolved the third crisis in mathematics. However, unlike the traditional style of axiomatization in ancient Greece, the axiomatization of modern mathematics has departed from natural language and is built upon symbolic language. Why do this?

In Francis Bacon's theory of idols, the “Idol of the market place” describes the illusions caused by the vagueness and ambiguity of natural language. This is something mathematics, in its pursuit of rigor, should avoid. The third crisis in mathematics made people realize that describing mathematical objects in natural language is dangerous. No matter how watertight your natural language may appear, it may still leave loopholes for fallacies.

The only way to solve this problem is to abandon natural language and turn instead to symbolic language. Such symbolic languages constitute the axiomatic systems of modern logic. The discipline that studies these symbolic languages is called mathematical logic (Mathematical logic).

This article aims to explain how symbolic language is used to establish modern mathematics on the foundation of set theory. Therefore, before introducing axiomatic set theory, we need to introduce mathematical logic and its two most fundamental logical systems: propositional logic (Propositional Logic) and first-order logic (First-Order Logic).

## Introduction to Mathematical Logic  

Part of the reason natural language has loopholes is that it is created and interpreted by the human mind. Yet the human mind “is not a blank slate (tabula rasa).” Owing to its inherent distortions, it is not a perfect plane capable of fully receiving the images of the world, but rather a curved mirror. In other words, the human mind is naturally prone to deception.

Symbolic language succeeds precisely because it detaches itself from the human mind, retaining only formalized rules. In theory, computers can also reason using such a language without making mistakes. This is because symbolic language has neither vagueness nor ambiguity; everything is strictly determined. We need only specify suitable rules for arranging symbols, so that the mathematics familiar to us can be reconstructed from them. In this way, mathematics is established upon a solid foundation and can never go wrong. Under such rigorous scrutiny, we leave no opening whatsoever for fallacies such as “Russell's paradox.”

So where do these symbolic rules come from? The answer is mathematical logic. **Just as we hope that the axioms of set theory determine “which ways of defining new sets are legitimate,” mathematical logic determines “which ways symbols may form formulas (that is, strings of symbols) are legitimate.”** Essentially, definitions, theorems, and proofs in mathematics are, at their foundation, strings of symbols, just as computers are fundamentally made of 1s and 0s.

A seemingly obvious logical rule such as “p→p” must be proved in mathematical logic. You may feel that this can be seen directly from semantics, but we now wish to study various expressions and their legitimacy from the perspective of syntax rather than semantics.

More specifically, semantics studies how the human mind interprets (Interpret) a string of symbols, or how a string of symbols refers to various entities in the real world through the human mind. But mathematical logic does not study semantics; it studies syntax. As stated above, syntax serves to determine **“which ways symbols may form formulas (that is, strings of symbols) are legitimate.”** In other words, syntax refers to the rules by which we use symbols to generate formulas (that is, strings of symbols). To establish a solid symbolic language system, we should study syntax separately. This is the original intention of mathematical logic.

**Mathematical logic is the discipline of logic, not “logic concerning mathematics and physics.”** Mathematical logic is a mature discipline. Set theory is built upon first-order logic in mathematical logic.

## Propositional Logic  

$\neg a$ denotes “not $a$.” If $a$ is true, then $\neg a$ is false, and vice versa. In other words, the truth table of $\neg$ is

|  |  |  |
| --- | --- | --- |
| a | T | F |
| ¬a | F | T |

Here T denotes true (True), and F denotes false (False).

$a \vee b$ denotes “$a$ or $b$.”

$a \wedge b$ denotes “$a$ and $b$,” and is equivalent to “$\neg(\neg a\vee \neg b)$.” Their truth tables are straightforward.

$a\rightarrow b$ denotes “if $a$, then $b$,” or “$a$ implies $b$.” Its truth table is as follows:

|  |  |  |
| --- | --- | --- |
| a→b | a | ¬a |
| b | T | T |
| ¬b | F | T |

> The column headed “a” is easy to understand: a true proposition can imply a true proposition, but cannot imply a false proposition. **Yet the column headed “**¬a**” seems to indicate that “a false proposition implies every proposition.” Why is it defined this way?** For details, see:

[How should an inference in logic whose premise is false but whose conclusion is true be interpreted?](https://www.zhihu.com/question/21020308/answer/16917222)
> In addition, in the examples below, readers can also appreciate why we stipulate that “a false proposition implies every proposition.”

> 【Optional Reading 1】“$a\rightarrow b$” is equivalent to “$(\neg a)\vee b$.” To see this, you need only substitute the four cases into the truth table.  
>   
> Specifically, when $a$ is true, $\neg a$ is false, so the truth value of “$(\neg a)\vee b$” depends on $b$. When $a$ is false, $\neg a$ is true, so regardless of the truth value of $b$, “$(\neg a)\vee b$” is true. Thus, “$a\rightarrow b$” and “$(\neg a)\vee b$” have the same truth table.

Define $a\leftrightarrow b$ to be $(a\rightarrow b)\wedge(b\rightarrow a)$.

> 【Optional Reading 2】It can be seen that we need only $\{\neg,\vee\}$ to obtain all propositional connectives $\{\neg,\wedge,\vee,\rightarrow, \leftrightarrow \}$. The former is called a functionally complete set of propositional connectives. $\{\neg,\rightarrow\}$, $\{\neg,\wedge\}$, and so on are also functionally complete sets of propositional connectives.

The axiomatic system of propositional logic consists of four parts: a symbol set, formation rules, axioms, and inference rules (see Optional Reading 3). We need not delve here into how the propositional logic system derives those obvious logical rules (in the axiomatic system of propositional logic, an apparently obvious formula such as p→p must be proved). We need only know that the foundations of our symbols and logic are solid. If you are truly concerned about this, you may study mathematical logic before studying axiomatic set theory.

> 【Optional Reading 3】The axiomatic system L of propositional logic  
>   
> 1) The axiomatic system of propositional logic consists of four parts: a symbol set, formation rules, axioms, and inference rules.  
>   
> The symbol set of the propositional logic axiomatic system L is p1, p2, ..., ¬, →, (, ). Note that the final two symbols are parentheses.  
>   
> Symbols such as ∧ and ∨ are absent because they can be represented using ¬ and → (see Optional Readings 1 and 2).  
>   
> Every statement should be composed of symbols from the symbol set. But this does not mean that an arbitrarily assembled string of symbols, such as ((p1→, is legitimate. To form legitimate statements, we also need formation rules.  
>   
> 2) The axiomatic system L has two formation rules: (¬A) and (A→B).  
>   
> They specify what kinds of formulas (symbol sequences) are syntactically well-formed.  
>   
> Note that A and B are not symbols in the symbol set; they stand for arbitrary formulas. A formula is a sequence composed of a string of symbols.  
>   
> For example, we may first use the second rule to generate (p1→p2), then use the first rule to generate (¬p3), and finally use the second rule to generate ((¬p3)→(p1→p2)), which is a syntactically legitimate formula.  
>   
> 3) The three axioms of the axiomatic system L are  
>   
> L1: (A→(B→A))  
> L2: ((A→(B→C))→((A→B)→(A→C)))  
> L3: (((¬B)→(¬A))→(A→B))  
>   
> They are responsible for connecting the axiomatic system L with classical logic. From these axioms, we can derive all formulas of classical logic. Of course, we have not yet defined what derivation is. This leads to the inference rules introduced below.  
>   
> 4) The inference rule of the axiomatic system: from A and A→B, one may infer B. This is also called the rule of detachment. The inference rule tells us how to prove new formulas. Note that proof and implication are two different concepts.  
>   
> In summary, the axiomatic system L consists of a symbol set, formation rules, axioms, and inference rules.  
>   
> Let us now prove p→p.   
>   
> By axiom L1: (p→((p→p)→p))   
> By axiom L2: ((p→((p→p)→p))→((p→(p→p))→(p→p)))   
> By the inference rule: ((p→(p→p))→(p→p))   
> Again by axiom L1: (p→(p→p))   
> By the inference rule: (p→p), Q.E.D.  
>   
> Why not take a simple and intuitive formula such as (p→p) as an axiom? Should axioms not be self-evident truths? This is because from L1, L2, and L3, we can derive all classical logical formulas (first-order logic is not yet included here), and there is no overlap or redundancy among L1, L2, and L3. In other words, this minimizes the number of axioms.  
>   
> Put differently, our goal is not to treat intuitive things as axioms, but to make as few things as possible into axioms. The more concise the axioms, the better.  
>   
> At this point, we have introduced an axiomatic system L for propositional logic.

## First-Order Logic  

The $\{\neg,\wedge,\vee,\rightarrow, \leftrightarrow \}$ introduced above are called propositional connectives. Together with formation rules, axioms, and inference rules, they form a **propositional logic** system. Next, let us look at quantifiers. A propositional logic system, together with quantifiers and their associated rules and axioms, becomes a **first-order logic** system.

$\exists x(\varphi(x))$ denotes “there exists $x$ satisfying $\varphi(x)$,” where $\varphi(x)$ is a property of $x$.

$\forall x(\varphi(x))$ denotes “for every $x$, $\varphi(x)$ holds.” It is equivalent to “$\neg \exists x \neg\varphi(x)$,” that is, “there does not exist an $x$ that fails to satisfy $\varphi(x)$.”

Thus, quantifiers require only $\exists$ for completeness; $\forall$ can be expressed using $\exists$.

Below are some simple exercises that will further help you become familiar with the first-order logic system—the symbolic language of axiomatic set theory.

1) $\forall x(x\in A\rightarrow \varphi(x))$ can be abbreviated as $\forall x\in A, \varphi(x)$. It means “for all $x$ in $A$, $\varphi(x)$ holds.”

2) $\forall x(x\in A\leftrightarrow \varphi(x))$ means “for all $x$ in $A$, $\varphi(x)$ holds, and $x$ satisfying $\varphi(x)$ belong to $A$.” In other words, $A$ contains precisely those elements satisfying property $\varphi$.

3) $\exists x(x\in A \wedge \varphi(x))$ can be abbreviated as $\exists x\in A, \varphi(x)$. It means “there exists some $x$ in $A$ such that $\varphi(x)$.”

> 【Optional Reading 4】**Note the contrast between 1) and 3)!** In 3), one cannot replace “$\wedge$” with “$\rightarrow$” and write $\exists x(x\in A \rightarrow \varphi(x))$.  
>   
> This is because if there exists an $x$ that does not belong to $A$ (and in fact this is inevitable, because we will later prove that no set contains everything), then $x\in A$ is false. Since a false proposition implies every proposition (see propositional logic), it can also imply $\varphi(x)$. Thus, the meaning of this expression is “provided $x$ does not belong to $A$, it satisfies $\varphi$,” which is not what we intend.  
>   
> Then why does 1) use the symbol “$\rightarrow$” rather than “$\wedge$”?  
>   
> First, let us see why “$\rightarrow$” is used. The quantifier “$\forall$” means that all $x$ are considered, so we discuss the two cases $x\in A$ and $x\notin A$.  
>   
> On the one hand, if $x$ belongs to $A$, then $x\in A$ is true. In order for $x\in A \rightarrow \varphi(x)$ to be true, according to the truth table, we can only require $\varphi(x)$ to be true;  
>   
> On the other hand, if $x$ does not belong to $A$, then $x\in A$ is false. According to the truth table, a false proposition can imply any proposition, so $x\in A \rightarrow \varphi(x)$ is true; that is, in this case it tells us no further information.  
>   
> Combining the two cases above, we conclude that $x\in A \rightarrow \varphi(x)$ is true if and only if “for all $x$ in $A$, $\varphi(x)$ holds.” This is exactly what we wish to express!  
>   
> From the above analysis, you can appreciate the benefit of stipulating that “a false proposition implies every proposition.”  
>   
> Why can “$\rightarrow$” not be replaced with “$\wedge$” in 1)? This is because if $x$ does not belong to $A$, then $x\in A \wedge \varphi(x)$ must be false. The quantifier “$\forall$” means that all $x$ are considered, and there are always some $x$ that do not belong to $A$. Therefore, $\forall x(x\in A\wedge \varphi(x))$ is a proposition that is always false and is of no use.  
>   
> **These three examples, 1), 2), and 3), are worth pondering.** If you fully understand them, subsequent learning will be much easier. If you do not wish to analyze them, you may also “take for granted” and remember their corresponding meanings.

Due to space limitations, this article introduces only the axiomatic system of propositional logic (see Optional Reading 4) and will not introduce the axiomatic system of first-order logic.

## Russell's Paradox  

The definition of a set that we learned in secondary school is nothing more than “a collection of certain elements,” along with several properties:

Definiteness (an object either belongs to set A or does not belong to A),

Unorderedness (changing the order of elements does not change the set), and

Distinctness (any two elements in a set are not identical).

These three properties seem to determine the concept of a set. However, from the perspective of modern mathematics, they are merely naïve and deeply flawed natural language. They do not explain how sets are possible, or how new sets may be legitimately defined.

To demonstrate this fully, let us look at Russell's paradox. Define the following set:

$$B=\{x|x\notin x\}$$

That is, B is the set of all “sets that do not belong to themselves.” This object is not prohibited by naïve set theory, yet it is disastrous.

**Now ask a simple question: does B belong to itself? If B belongs to itself, then by the definition of B, B does not belong to itself; if B does not belong to itself, then by definition B belongs to itself. Thus we obtain “p if and only if not p,” which violates the law of excluded middle. This is Russell's paradox.**

(The paradox here specifically means a paradox in the logical sense, namely, “p if and only if not p.”)

Such an object should be prohibited, but naïve set theory does not prohibit it. In other words, naïve set theory is “inconsistent.” An inconsistent system is useless, **because from “p if and only if not p” one can prove any proposition, as follows:**

> p → p ∨ q  
> (p ∨ q) ∧ (¬p) → q  
> Therefore (p ∧ ¬p) → q  
>   
> Of course, in this proof we omit many steps, because we have not yet derived more theorems in the axiomatic system L (see Optional Reading 3). Readers who wish to get to the bottom of things may try to provide a complete proof using axiomatic system L. Here, we shall accept it provisionally.

A theory from which every proposition can be derived is obviously useless. Thus, people had to reconstruct set theory.

We introduced Russell's paradox first in order to let readers feel the necessity of replacing natural language. In the technical details of axiomatizing set theory that follow, we will resolve Russell's paradox, thereby allowing readers to appreciate the great significance of symbolic language replacing natural language.

## Ontological Commitment (ZF0: Axiom of Existence, Axiom of Existence)  

In the previous section, we saw that $B=\{x|x\notin x\}$ is an illegitimate definition. A new set theory should avoid this problem. How can it be avoided? Since the problem lies in definitions, we can address it at the root by using a set of axioms to determine the rules for defining new sets. **Then, whenever we define a new set, we need only check whether it follows these axioms. In other words, axioms are our sole basis for defining new sets.**

To define new sets from existing sets, we must first have a set. Therefore, our first axiom is called the “Axiom of Existence”:

> Axiom of Existence: $\exists x(x=x)$

It states that a set exists.

**Do not laugh! If we had only rules for generating sets from sets, but no set available to use, then the mathematical universe would contain nothing at all. “One cannot make bricks without straw”; the Axiom of Existence is no joke.**

**Before we use symbols to refer to an entity, we always assume that some entity exists. A commitment regarding the existence of an entity is called an ontological commitment.**

This is a good start, because for the first time we are using entirely abstract symbols rather than natural-language statements such as “a set is a collection of elements.”

In fact, the Axiom of Existence can be derived from other axioms, but for ease of learning, we shall temporarily treat it as the “zeroth” axiom and discard it at an appropriate time later. It is really just scaffolding: once the building is complete, it will be removed.

You may have noticed that “$x=x$” is a tautology. Why do this? Because according to the symbolic rules of the axiomatic system, “$\exists x$” must be followed by something. Since we merely want to express “there exists a set,” it need only be followed by a true proposition.

**You may also have noticed that** $x$ **is merely a symbol; the formula** $\exists x(x=x)$ **itself does not indicate that it is a “set”—what if it is a number? Do not worry: so far, numbers have not been defined, because we take set theory as our foundation. Starting from the foundation means that we must forget everything else in mathematics.**

You may imagine the following scene: the world of mathematics has just been born and is almost empty. Only a planet called “first-order logic” floats within it, with an inexhaustible supply of raw materials (a symbol set), foundations (axioms), and some symbolic rules (formation rules and inference rules). However, aimlessly and continuously using rules to generate new formulas (strings of symbols) is of no use. We need to create some axioms so that these symbols can be organized into useful things. These initial axioms are the axioms of set theory. Later, we will see that **numbers too are defined using sets**.

The symbol “$x$” is merely a “thing”; we simply call this thing a set. **Essentially, all mathematical objects built upon set theory are sets**: the number “$3$” is a set, and the ordered pair $(1,2)$ is also a set... It is merely that when a set acquires a new structure, we give it a new name, such as “integer,” “ordered pair,” “ring,” “probability space,” or “algebra.” If this seems surprising to you now, that is fine; we will understand it later.

You may also understand it this way: at the lowest level, even the most complex software on a computer is nothing more than 1s and 0s; they simply possess complex organization and structure.

We now have an axiom. An axiom is something that cannot be proved, but is created from nothing by the gods of the mathematical universe (that is, mathematicians). Let us continue enriching our mathematical universe.

## Introducing the Membership Symbol (ZF1: Axiom of Extensionality, Axiom of Extensionality)  

Before creating new sets, we must also define how to determine whether two sets are equal:

> Axiom of Extensionality: $\forall A \forall B(\forall x(x \in A\leftrightarrow x \in B)\rightarrow A=B)$

It states that if every element of A belongs to B, and every element of B belongs to A, then A and B are equal.

Wait—we have not defined what “$\in$” is! No matter. In mathematical logic, we have a symbol set; symbols such as “$\forall$,” “$\exists$,” and even parentheses “$($” are all in this symbol set. We need only add a new symbol “$\in$” to the symbol set to denote some binary relation ( “$\notin$” can be defined using symbols such as “$\in$” and “$\neg$”). Note that the symbol set itself imposes no stipulations or interpretations upon symbols; axioms associated with them give symbols structure and meaning.

It should be emphasized that “$\in$” represents only a binary relation. People may think of the object before “$\in$” as “the thing being contained,” and the object after it as “a thing containing some things,” but for “$\in$,” the things before and after it are no different: both are some kind of “thing.” And “$\in$” itself is merely a predicate obeying certain rules. We must now become accustomed to thinking by forgetting everything, as Descartes did.

The significance of this axiom is that it specifies the first property of the symbol “$\in$”: equality. If every object standing in the “$\in$” relation to A also stands in the “$\in$” relation to B, and vice versa, then we say that A and B are “equal.”

Returning to the main topic, observe how this axiom entails the so-called “definiteness,” “unorderedness,” and “distinctness.” In fact, according to the symbolic rules (which are not listed here), the set $\{x,x,y\}$ is a legitimate formula; it is simply equal to $\{x,y\}$ under the Axiom of Extensionality (every element of $\{x,x,y\}$ belongs to $\{x,y\}$, and vice versa). We may denote all sets equal to $\{x,y\}$ by $\{x,y\}$. This is the so-called distinctness; unorderedness is even simpler: the symbolic rules themselves impose no stipulations about order. For elements within a set, the only useful information is the binary relation “$\in$”; no other symbol specifies other relations, such as an order relation (which we will define later). Finally, definiteness is also entailed, because it is plainly determined by the basic rules of logic (the law of excluded middle). Thus, we have no need at all for natural-language expressions such as “distinctness.”

## The Empty Set (ZF2: Axiom Schema of Separation, Axiom Schema of Separation)  

So far, we still do not have a definite set available for use, because the Axiom of Existence merely states that a set exists and tells us nothing more about it. Of course, we could denote this existing set by A and use it as raw material to create new sets. But there is a better approach: defining an empty set as raw material. Then at least we know exactly what this raw material is.

However, we cannot define the empty set from the axioms currently available. We need one more axiom:

> Axiom Schema of Separation: $\forall A \exists B \forall x(x\in B\leftrightarrow x\in A \wedge \varphi(x))$

It is called the Axiom Schema of Separation because $\varphi(x)$ represents any legitimate string of symbols (involving x); that is, this one axiom contains infinitely many axioms. Below, we shall simply call it the Axiom of Separation.

The significance of the Axiom of Separation is that, given any set A, we can use property $\varphi$ to separate all objects in A satisfying $\varphi$ and form a new set. We denote this new set by $B=\{x\in A|\varphi(x)\}$.

At last, we have our first **constructive axiom. A constructive axiom is a rule for constructing new sets from old sets.**

Of course, knowing such a rule alone is useless; we must first have an “old set.” Fortunately, the Axiom of Existence tells us that we have at least one “old set” available.

Note! What we usually write as $B=\{x|\varphi(x)\}$ is, at present, illegitimate, because it is not obtained from an existing set. Instead, it directly stipulates a property $\varphi$ and extracts from nowhere all elements satisfying $\varphi$ to form a set. **This is not actually a set, but a “class” (Class). It is the chief culprit behind Russell's paradox!** Russell's paradox forms a set by extracting from nowhere all elements satisfying the property “does not belong to itself.” This is wrong. Doing so can form only a class, not a set.

The Axiom of Existence asserts that a set exists. We shall now use the Axiom of Separation to construct a definite set—the empty set.

By the Axiom of Existence, there exists a set $X$ (although we do not know exactly what it is); then, by the Axiom of Separation, $\{x\in X|x\neq x\}$ is a set.

The false proposition $x\neq x$ can imply $x\in X$, and of course it can also imply $x\in Y$, $x\in Z$, and so on, while $X$, $Y$, and $Z$ may be different sets. That is, there may be many such sets, but below we shall use the Axiom of Extensionality to prove that these sets are equal.

Let $A= \{x\in X|x\neq x\} ,B= \{x\in Y |x\neq x\} $. Here $X$ and $Y$ are arbitrary sets. We need only prove $A=B$.

By the Axiom of Extensionality: $\forall A \forall B(\forall x(x \in A\leftrightarrow x \in B)\rightarrow A=B)$. It is clear that we need only check whether $\forall u(u \in A\leftrightarrow u \in B)$ holds for arbitrary $A$ and $B$.

In fact, since $A= \{x\in X|x\neq x\}$, $x\in A$ is false for every $x$ (otherwise the contradictory expression $x\neq x$ would follow). A false proposition can imply every proposition; therefore $x \in A\rightarrow x \in B$.

(Note that $x \in A\rightarrow x \in B$ being true does not mean that $x\in A$ is true.)

We have just proved $\forall x (x \in A\rightarrow x \in B)$, and by the same reasoning we can also prove $\forall x (x \in B\rightarrow x \in A)$. Hence $\forall x (x \in B\leftrightarrow x \in A)$, and thus $A=B$.

In this way, we have proved that $\{x\in X|x\neq x\}$ is unique; that is, it is independent of what $X$ specifically is. We denote this uniquely determined set by $\emptyset$ and call it the empty set.

**From the above analysis, we find that the empty set contains nothing, because for every** $x$**,** $x\in \emptyset $ **is a false proposition.**

**Notice that we did not define the empty set using natural language such as “the empty set contains nothing.” Instead, we first defined the empty set with axioms, and then proved that “the empty set contains nothing.”** This illustrates formal axiomatization replacing natural language.

We now finally have a brick. Next, we can use the empty set as this brick to build more sets. But before that, we can first resolve Russell's paradox.

> Other versions of axiomatic set theory may take the “Axiom of the Empty Set” as an axiom, asserting that an empty set exists. In our version, however, the Axiom of the Empty Set can be derived from the Axiom of Existence plus the Axiom Schema of Separation.

## The Resolution of Russell's Paradox  

Recall how Russell's paradox arose. We first defined $B=\{x|x\notin x\}$, and derived $B\in B\rightarrow B\notin B$ and $B\in B\leftarrow B\notin B$, thereby producing a contradiction. **To resolve Russell's paradox, we need only make one of them fail. We will make the latter fail.** The derivation is as follows:

> (1) By the Axiom of Separation, we can define $B=\{x\in A|x\notin x\}$. Call $x\notin x$ property $\varphi$.  
>   
> (2) Suppose $B\in B$. Then, by the definition of $B$, $B$ satisfies property $\varphi$, namely $B\notin B$—a contradiction! Thus, we can only have $B\notin B$.  
>   
> (3) Next, we prove $B\notin A$. We proceed by contradiction. Suppose $B\in A$.  
>   
> On the one hand, by (2), $B\notin B$; that is, $B$ satisfies property $\varphi$.  
>   
> On the other hand, by our assumption, $B\in A$.  
> Therefore, B belongs to A and B satisfies property $\varphi$. By the definition of $B$, $B\in B$, contradicting (2)! Thus $B\notin A$.  
>   
> Since $B\notin A$, $B\notin B$ cannot imply $B\in B$.

Thus, we have resolved Russell's paradox: the set $B$ does not belong to itself, and that is all; no contradiction occurs.

If you feel that all this happened too quickly, I will describe it once more in more natural language below. **Originally, we defined a set B from nowhere using the property “does not belong to itself,” but the Axiom Schema of Separation tells us that this is not permitted.** This is the key point! We must separate the new set B from an existing set A, and A is proved not to contain element B; hence “B does not belong to itself” cannot imply “B belongs to itself.” Notice that **deriving “B belongs to B” from “B does not belong to B” requires another condition: namely, “B belongs to A.”**

**Put another way, the key to Russell's paradox is “self-reference,” and the Axiom of Separation eliminates the possibility of “self-reference.” B refers only to elements of A; not every element can be referred to by the definition of B.**

The above analysis also proves that for every set $A$, there is always a set $B=\{x\in A|x\notin x\}$ that does not belong to $A$ (by (3)). **Therefore, the set of all sets does not exist; or equivalently, a set containing everything does not exist.**

## Intermission  

This article introduced the first three axioms of the axiomatic system of set theory—the Axiom of Existence, the Axiom of Extensionality, and the Axiom Schema of Separation—and used them to resolve Russell's paradox and construct our first set—the empty set.

In the next article, we will introduce more axioms and use them to create some mathematical objects, such as natural numbers.

The Axiom of Existence can be derived from the later “Axiom of Infinity,” but for ease of learning, it is sometimes first treated as the “zeroth” axiom and then removed later. In fact, there are only nine axioms, namely:

ZF1 Axiom of Extensionality

ZF2 Axiom Schema of Separation

ZF3 Pairing Axiom

ZF4 Union Axiom

ZF5 Power Set Axiom

ZF6 Axiom of Infinity (from which the Axiom of Existence can be derived)

ZF7 Axiom of Regularity

ZF8 Axiom Schema of Replacement

ZF9 Axiom of Choice

The first eight axioms constitute the so-called “ZF” axiomatic system; adding the Axiom of Choice yields the “ZFC axiomatic system.” “Z” and “F” are the initials of the surnames of the proposers, while “C” stands for “Axiom of Choice”—the Axiom of Choice.

Sequel to this article:

[Foundations of Axiomatic Set Theory (Part II): Toward Infinity](https://zhuanlan.zhihu.com/p/346542841)
