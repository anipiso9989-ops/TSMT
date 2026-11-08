# Part I — Foundations of Mathematical Thought

> *Before you can solve problems, you must know what a mathematical object is, what a claim means, what follows from what, and what counts as having established something. Everything else in this guide rests on these six chapters.*

**Chapters in this part**

1. Mathematics as the Study of Structure
2. Definition: Making Meaning Precise
3. Logic: The Grammar of Inference
4. Proof: The Technology of Shared Certainty
5. Abstraction and the Ladder of Structure
6. First-Principles Reasoning

**What you should be able to do after Part I**

- Given an unfamiliar claim, state precisely what it asserts, what it assumes, and what would refute it.
- Write a definition that is unambiguous, non-circular, and well-defined.
- Negate any quantified statement mechanically and correctly.
- Choose a proof engine by matching the *structure of the goal*, and audit the result for gaps.
- Identify which features of a situation are load-bearing and which are decoration.
- Rebuild a standard result from its assumptions instead of citing it.

---

# Chapter 1 — Mathematics as the Study of Structure

## 1. Core Idea

Mathematics does not study numbers, shapes, or functions. It studies **structures**: collections of objects together with the relations and operations on them, described by axioms. A theorem is never a statement about the world. It is a conditional statement of the form:

> *In every structure satisfying these axioms, the following holds.*

Numbers, triangles, permutations, graphs, and probability spaces are all **models** — concrete realizations — of structures. The reason one theorem can settle a question about resistors, another about prime numbers, and a third about error-correcting codes is that all three situations are models of the same structure, or of structures linked by a structure-preserving map.

This reframing has a sharp practical consequence. When you meet a problem, the productive question is not *"what topic is this?"* but **"what structure is this, and what is already known about it?"** Topic labels ("number theory", "geometry") are indexing conventions for humans. Structure is what the mathematics actually responds to.

## 2. First Principles

**Why abstraction from instances is forced.** There are infinitely many triangles, integers, and graphs. A finite mind cannot verify a claim case by case. The only way to make a statement about infinitely many objects checkable in finite time is to find a finite description that all of them satisfy — axioms — and then reason from the description rather than from the objects. This is not a stylistic preference; it is the only available method.

**What a structure is.** Formally, a structure is a tuple

$$\mathcal{S} = (D;\; R_1,\dots,R_m;\; f_1,\dots,f_n;\; c_1,\dots,c_k)$$

consisting of a domain $D$, relations $R_i \subseteq D^{a_i}$, operations $f_j : D^{b_j} \to D$, and distinguished constants $c_l \in D$, together with a set of axioms these must satisfy. Everything else — what the elements "are", what they are called, how they are drawn — is irrelevant to the mathematics.

**The transfer principle.** If a statement $\varphi$ is derivable from axioms $\Sigma$, then $\varphi$ holds in *every* structure satisfying $\Sigma$. This is the engine behind the entire guide: prove once in the abstract, apply everywhere. It is also the reason a single counterexample destroys a universal claim, while a single example never establishes one.

**Meaning is use.** A symbol has no intrinsic content. Its meaning is fixed by the operations it participates in and the axioms those operations obey. This is why the same marks can appear in two incompatible structures: "$1+1=2$" is true in $\mathbb{N}$ and false in $\mathbb{Z}/2\mathbb{Z}$, where $1+1=0$. Neither statement is "the truth about 1". Each is a truth about a structure.

## 3. Reasoning Process

When confronting any mathematical situation, run this sequence:

1. **Name the objects.** What are the elements of the domain? Are they numbers, sets, functions, configurations, processes?
2. **Name the relations and operations.** What can be compared, combined, composed, or transformed?
3. **State the axioms you are allowed to use.** Which properties are given? Which are you hoping for? The gap between these two lists is the problem.
4. **Look for a second model.** Is this situation an instance of something you already know — a group, a lattice, a metric space, a matroid, a Markov chain? Matching a known structure imports an entire library of theorems for free.
5. **Ask what the structure forbids.** Structures are characterized as much by their impossibilities as their possibilities. A structure with no order relation cannot support an inequality argument. A structure without inverses cannot support cancellation.
6. **Record the transfer.** Once a theorem is proved in the abstract, list every model in which you may now use it. This list is your working capital.

The most common failure at this stage is **premature topic classification**: deciding "this is a geometry problem" and therefore reaching only for geometric tools, when the situation is really a statement about a finite set with a symmetric group acting on it.

## 4. Demonstrations

### Demonstration 1.1 — One relation, three costumes

Consider the relation

$$\frac{1}{x} + \frac{1}{y} = 1.$$

Algebraically, this is equivalent to

$$x + y = xy \iff xy - x - y = 0 \iff (x-1)(y-1) = 1.$$

That last form is the *structural* form: it says the pair $(x-1,\,y-1)$ consists of two numbers with product $1$.

Now observe three situations that are models of this relation.

**(a) Parallel resistors.** Two resistors $R_1, R_2$ in parallel have equivalent resistance $R$ given by $\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}$. Setting $x = R_1/R$, $y = R_2/R$ and dividing through by $R$, we recover exactly $\frac1x + \frac1y = 1$. So the structural form says: the two *normalized* resistances satisfy $(x-1)(y-1)=1$. Consequence, transferred for free: for positive $x,y$ with $\frac1x+\frac1y=1$ we must have $x>1$ and $y>1$. Indeed, if $x \le 1$ then $\frac1x \ge 1$, so $\frac1y = 1 - \frac1x \le 0$, impossible for positive $y$. In the structural form this is the statement that $x-1$ and $y-1$ are both positive and reciprocal. That is a physical prediction — no branch of a parallel pair can have normalized resistance at most $1$ — obtained by pure algebra.

**(b) A Diophantine problem.** Solve $\frac1x + \frac1y = \frac12$ in positive integers. Dividing by $2$ and substituting $X = x/2$, $Y = y/2$ gives $\frac1X+\frac1Y = 1$, so $(X-1)(Y-1)=1$ with $X,Y$ positive rationals. Alternatively, directly: $2(x+y) = xy$, so $(x-2)(y-2)=4$. Since $x,y$ are positive integers, $x-2$ and $y-2$ are integers whose product is $4$; the factor pairs $(1,4),(2,2),(4,1)$ give $(x,y) = (3,6),(4,4),(6,3)$. The *same* factorization move that solved the resistor problem solved this one, because both are models of the same relation.

**(c) The harmonic mean.** The harmonic mean $H$ of $x$ and $y$ satisfies $\frac{2}{H} = \frac1x+\frac1y$. Under the normalization $H=1$ we are back to the identical equation. So any theorem about $\frac1x+\frac1y=1$ is a theorem about pairs whose harmonic mean is $1$.

**What to notice.** The topic changed three times; the mathematics did not. Once you have the structural form $(x-1)(y-1)=1$, every model inherits the conclusion. This is what "transfer" means in practice, and it is the single highest-leverage habit in this guide.

### Demonstration 1.2 — A theorem that transfers between two unrelated-looking structures

Let $\zeta = e^{2\pi i/12}$, a primitive $12$th root of unity, and let $G = \{1,\zeta,\zeta^2,\dots,\zeta^{11}\}$ under multiplication. Let $H = \mathbb{Z}/12\mathbb{Z} = \{0,1,\dots,11\}$ under addition mod $12$.

The map $\varphi(k) = \zeta^k$ satisfies

$$\varphi(a+b \bmod 12) = \zeta^{a+b} = \zeta^a\zeta^b = \varphi(a)\varphi(b).$$

It is a bijection. So $(\mathbb{Z}/12\mathbb{Z}, +)$ and $(G, \cdot)$ are **the same structure** — isomorphic — and every theorem about one is a theorem about the other.

Now prove a theorem in the additive model and read it off in the multiplicative one.

*Claim.* The equation $3x \equiv 0 \pmod{12}$ has exactly $\gcd(3,12)=3$ solutions modulo $12$.

*Proof.* $3x \equiv 0 \pmod{12}$ means $12 \mid 3x$, i.e. $4 \mid x$. Among $0,\dots,11$ the solutions are $0,4,8$: exactly three. $\blacksquare$

*Transferred claim.* The equation $z^3 = 1$ has exactly three solutions among the $12$th roots of unity.

*Verification.* $z^3=1$ with $z=\zeta^k$ means $\zeta^{3k}=1$, i.e. $12 \mid 3k$, i.e. $k \in \{0,4,8\}$, giving $z \in \{1,\zeta^4,\zeta^8\} = \{1, e^{2\pi i/3}, e^{4\pi i/3}\}$. Correct — and notice we did not have to solve a cubic.

**What to notice.** The transfer required no insight about complex numbers. It required only the observation that a structure-preserving bijection existed. Learning to *see* such bijections is Chapter 19; learning to *use* them is this chapter.

### Demonstration 1.3 — When the same symbols mean different things

In $\mathbb{Z}/2\mathbb{Z}$, $1+1=0$. In $\mathbb{N}$, $1+1=2$. Both are true; they are statements about different structures. A student who treats "$1+1=2$" as a universal truth about the marks "$1$", "$+$", "$2$" will be confused by coding theory, where adding two bit strings componentwise mod $2$ is exactly the operation that makes error correction work: two errors in the same position cancel.

Similarly, in $\mathbb{Z}/2\mathbb{Z}$ every element satisfies $x^2=x$, so $(a+b)^2 = a^2+b^2$ — the "freshman's dream" is a theorem there and a blunder in $\mathbb{R}$.

**What to notice.** The lesson is not "be careful with notation". The lesson is that **the axioms determine the truth**, and identifying the axioms is a necessary step in any argument. When someone says "but it's obviously true", ask: *true in which structure?*

## 5. Connections

- **→ Ch. 2.** Structures are specified by definitions. A sloppy definition produces a structure that is not the one you intended.
- **→ Ch. 5.** Abstraction is the act of *constructing* a structure from instances; this chapter is the destination, Chapter 5 is the method.
- **→ Ch. 19.** Isomorphism and duality are the precise form of "same structure, different costume".
- **→ Ch. 25.** Applied modeling is the reverse direction: given a piece of the world, find a structure that models it. The accuracy of the model is exactly the extent to which the structure's theorems are true of the world.
- **← Ch. 3, 4.** You cannot reason about structures without logic and proof.

## 6. Limitations

**The structure can be the wrong one.** Every model discards information. A structure that is adequate for one question may be catastrophically inadequate for another: treating a fluid as a continuum is excellent for pipe flow and useless for the behavior of individual molecules. The failure is not in the mathematics; it is in the identification of the model with the thing.

**Over-abstraction destroys the property you need.** If you ascend to "any set" you lose order, and with it every inequality argument. If you ascend to "any group" you lose commutativity, and with it the ability to cancel in the naive way. Abstraction must stop at the rung where the properties you need are still present — no higher (you lose power) and no lower (you drown in cases).

**Structural identity can be invisible.** Two structures may be isomorphic with no efficient way to find the isomorphism. "Same structure" is a mathematical fact, not necessarily a computational convenience.

**Axioms are human artifacts.** The historical record shows definitions and standards of rigor changing over centuries. What counts as "the" structure of the real numbers, of continuity, or of a function has shifted. Treat axioms as *commitments you can inspect*, not as revelations.

## 7. Applications

- **Coding theory and compression.** Hamming's error-correcting codes came from recognizing that the set of error patterns forms a structure under mod-2 addition, so that "two errors in the same position" is the identity. The structure made the engineering problem tractable.
- **Physics.** Conservation laws are structural statements: they assert that a certain quantity is invariant under a group of transformations. Noether's theorem makes the link between symmetry structure and conserved quantities explicit.
- **Machine learning.** A neural network layer is a composition of linear maps and pointwise nonlinearities; understanding what a architecture *can* represent is a question about the structure of function classes, not about any particular dataset.
- **Finance.** The no-arbitrage assumption is a structural axiom; the entire apparatus of risk-neutral pricing is a theorem that transfers to every market model satisfying it.
- **Software.** Type systems are structures; a type checker is a proof assistant for a weak logic. "Well-typed programs do not go wrong" is a transfer theorem.

## 8. Mastery Criteria

You have this chapter when you can:

1. Given a theorem statement, identify the structure it is about and name at least one *other* model of that structure.
2. Take a relation from one domain and rewrite it in structural form (as in Demonstration 1.1), then read off a consequence in a different domain.
3. Produce an example of the same symbols meaning different things in two structures, and explain what determines the difference.
4. Explain, without notes, why a single counterexample refutes a universal claim while a single example never proves one.
5. Given a problem, state which properties are *used* by a proposed solution and whether the ambient structure actually supplies them.
6. Identify a case where a model is adequate for one question and inadequate for another, and say what information the model discards.

**Diagnostic question.** "Two problems look completely different. Under what conditions would you expect a single argument to solve both?" A weak answer talks about similar-looking formulas. A strong answer talks about a shared structure, a structure-preserving map, and the specific axioms the argument consumes.

### AI Tutor Brief

- **Generate:** (i) problems that are the same structure in different domains and ask the learner to identify the correspondence; (ii) problems where the ambient structure *lacks* a property the learner will be tempted to assume (no order, no inverses, non-commutative); (iii) "which axioms did this proof actually use?" audits of short arguments.
- **Probe misconceptions:** topic-label thinking ("this is geometry, so use geometry"); assuming $\mathbb{R}$-like properties in arbitrary structures; confusing a model with the structure.
- **Transfer distance:** high. Always include at least one problem whose surface topic is unrelated to the chapter's examples.
- **Do not** accept "it's the same idea" as an answer. Require the explicit structure-preserving map or the explicit shared axiom set.

---

# Chapter 2 — Definition: Making Meaning Precise

## 1. Core Idea

A **definition** is a deliberate, public act of fixing the meaning of a term for the duration of an argument. It is not a description, not an observation, and not a theorem. It is a commitment.

Three obligations come with that commitment:

1. **Unambiguity.** Given any object in the intended domain, the definition must decide, in principle, whether the term applies.
2. **Non-circularity.** The term must be explained using terms already available. (Every system has undefined primitives; the discipline is to know which ones you are standing on.)
3. **Well-definedness.** If the definition names an object via a representative or a choice, the resulting object must not depend on which representative or choice was used.

Almost every serious mathematical error in student work is, at bottom, a definitional error: a term used in two senses in the same argument, an object defined by a choice whose independence was never checked, or a hypothesis smuggled into a definition.

## 2. First Principles

**Why definitions are load-bearing.** A proof is a chain of forced inferences. Each link requires that both parties agree on what the words mean. Without that agreement, "proof" degenerates into persuasion. Definitions are the mechanism by which mathematics achieves *checkability by a stranger*.

**Definition versus theorem.** A definition cannot be true or false; it can only be useful or useless, precise or vague. "A prime is an integer greater than $1$ whose only positive divisors are $1$ and itself" is a definition. "Every integer greater than $1$ has a prime divisor" is a theorem, and it requires proof (it is where the well-ordering of $\mathbb{N}$ enters). Confusing the two produces the classic error of "proving" a definition.

**Necessary and sufficient.** For a definition of the form "$P$ if and only if $Q$", there are two distinct claims:

- $Q$ is **sufficient** for $P$: if $Q$ holds, then $P$ holds. (The "if" direction, as usually written.)
- $Q$ is **necessary** for $P$: if $P$ holds, then $Q$ holds. (The "only if" direction.)

A definition needs both. A *characterization theorem* also needs both, and each direction usually has a different proof. When only one direction is true, you have a theorem, not a definition — and a very common error is to use the unproved direction.

**Well-definedness.** Suppose you define a function on rationals by choosing a representation: $f(p/q) = p + q$. This is not a definition at all, because $\frac12 = \frac24$ but $1+2 = 3 \neq 6 = 2+4$. The object "$f$" does not exist. The repair is either to prove independence of the representation, or to define $f$ on the *equivalence class* directly.

This is not a pedantic issue. It is exactly the issue that makes arithmetic in $\mathbb{Z}/n\mathbb{Z}$ legitimate, that makes the determinant well-defined, and that makes "the" antiderivative ambiguous until you fix a constant.

**Extensional versus intensional.** Two definitions can pick out the same set by different descriptions. "$n$ is even" and "$n^2$ is even" pick out the same integers — but that is a theorem, not a tautology. Keep the description and the object separate; proofs often consist precisely in showing two descriptions coincide.

## 3. Reasoning Process

1. **Unpack mechanically.** Replace every defined term by its definition, recursively, until only primitives remain. Most "hard" problems become transparent at this step.
2. **Test with examples and near-misses.** For each clause of the definition, construct an object that satisfies every clause *except* that one. If you cannot, the clause may be redundant; if the object still qualifies, the definition is not doing what you think.
3. **Check the quantifiers.** "There exists a $\delta$" and "for every $\delta$" define entirely different concepts. Definitions are the most common place for quantifier errors to hide.
4. **Check well-definedness.** If the definition involves a choice, a representative, an ordering, or a limit, prove independence. Write the independence proof even when it seems obvious — it is where the real content usually lives.
5. **Ask what the definition excludes.** A definition that excludes nothing is vacuous. A definition that excludes too much is unusable. The boundary cases (empty set, zero, the degenerate triangle, the trivial group) are where definitions earn their keep.
6. **Distinguish definition from characterization.** If you find yourself proving something, you are not defining; you are characterizing. Label it correctly, because the proof obligations differ.

## 4. Demonstrations

### Demonstration 2.1 — A definition that fails: well-definedness

*Attempted definition.* For a rational number $r$, write $r = p/q$ with $p,q$ integers, $q \neq 0$, and define
$$\delta(r) = p - q.$$

*Failure.* $r = \frac12$ gives $\delta = 1 - 2 = -1$. But $r = \frac24$ gives $\delta = 2-4 = -2$. The same input produces two outputs. $\delta$ is not a function.

*Diagnosis.* The definition quantified over a *representation* while claiming to define a function of the *number*. The repair must either (a) restrict to a canonical representation ($q>0$, $\gcd(p,q)=1$) and then prove that the formula depends only on $r$ — which fails here — or (b) define directly on the equivalence class.

*Contrast: a definition that succeeds.* Define, for $r = p/q$ in lowest terms with $q>0$, the **height** $h(r) = |p| + q$. This *is* well-defined, because lowest terms with positive denominator is a canonical form: every rational has exactly one such representation. The proof is one line (uniqueness of reduced form), but the line is mandatory.

**What to notice.** The difference between $\delta$ and $h$ is not the formula. It is whether the formula is invariant under change of representative. Whenever you see "write $x$ as ..." in a definition, stop and check invariance.

### Demonstration 2.2 — The definition of continuity, and how the definition does the work

*Definition.* $f : \mathbb{R} \to \mathbb{R}$ is **continuous at** $a$ if
$$\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \; \big(|x-a| < \delta \implies |f(x)-f(a)| < \varepsilon\big).$$

*Claim.* $f(x) = x^2$ is continuous at $a = 2$.

*Proof.* Let $\varepsilon > 0$. We must produce $\delta>0$ such that $|x-2|<\delta$ forces $|x^2-4|<\varepsilon$. Factor:
$$|x^2 - 4| = |x-2|\,|x+2|.$$
If we first insist that $|x-2| < 1$, then $|x+2| = |(x-2)+4| \le |x-2| + 4 < 5$. So choosing
$$\delta = \min\left(1, \frac{\varepsilon}{5}\right)$$
gives $|x^2-4| < \frac{\varepsilon}{5}\cdot 5 = \varepsilon$ whenever $|x-2|<\delta$. $\blacksquare$

**What to notice.** The definition did not merely state the goal; it dictated the proof strategy. Because the definition begins "for all $\varepsilon$, there exists $\delta$", the proof *must* begin by accepting an arbitrary $\varepsilon$ and *must* end by exhibiting a $\delta$. The extra restriction $|x-2|<1$ is not cheating — it is the standard technique of bounding the "uncontrolled" factor by first confining $x$ to a neighborhood. Every $\varepsilon$-$\delta$ proof has this shape.

### Demonstration 2.3 — The cost of an imprecise definition

Consider the phrase "a number is even if it is divisible by two". Read literally, "if" gives only sufficiency: divisibility by two implies evenness. It does **not** exclude the possibility that some number not divisible by two is also even. So the definition is compatible with $3$ being even.

"Even only if divisible by two" gives only necessity, and permits $4$ to be odd.

Only the biconditional — "even if and only if divisible by two" — pins the concept down. This is why definitions in mathematics are written with "iff", "if and only if", or the compact "$\stackrel{\text{def}}{\iff}$".

**What to notice.** The words "if" and "only if" are not stylistic variants. They are the two halves of a definition, and dropping one silently enlarges or shrinks the concept. In your own writing, write definitions with explicit biconditionals.

## 5. Connections

- **← Ch. 1.** A structure is a domain plus operations plus axioms; the axioms are definitions in action.
- **→ Ch. 3.** The quantifier structure of a definition determines the shape of its negation. You cannot negate what you have not parsed.
- **→ Ch. 4.** Proofs are chains of definitional unpacking plus inference. Most "gaps" in a proof are unperformed unpackings.
- **→ Ch. 14.** Canonical forms are what make definitions by representation well-defined. Lowest terms, reduced row echelon form, and cycle decomposition are all canonical forms in this sense.
- **→ Ch. 32.** The fastest way to break a theorem is to find the clause of a definition that its proof silently strengthened.

## 6. Limitations

**Definitions cannot create existence.** Defining "the largest prime" does not produce one. Definitions of objects via descriptions ("the smallest positive integer not definable in fewer than twenty words") can be outright paradoxical. Existence is always a separate theorem.

**Circularity is often invisible.** Euclid defined a point as "that which has no part" and a line as "breadthless length" — definitions that are circular or vacuous. Modern treatments take point and line as primitives. The lesson is not that Euclid was foolish but that *every* system has a bottom, and the bottom is chosen, not derived.

**Definitions slide.** "Function", "continuity", and "computability" have all changed meaning historically. A proof that was correct under an older definition may be invalid under the newer one. This matters when reading older mathematics.

**Precision has a cost.** Over-formalized definitions can obscure the idea. The right level of precision is the minimum that makes the argument checkable — no less, and not much more.

**Some things resist sharp definition.** "Important problem", "elegant proof", "natural" are used constantly by working mathematicians and cannot be defined sharply enough to be mechanized. This is a genuine limit, not a temporary gap.

## 7. Applications

- **Specification and contracts.** An API specification is a definition. Ambiguity in the specification is a bug that no amount of testing removes, because the tests themselves must appeal to the specification.
- **Metrics and measurement.** "User engagement", "risk", "fairness" — each requires a definition with explicit clauses, and each definition excludes something. Choosing the definition *is* the substantive decision.
- **Statistics.** "Unbiased estimator", "confidence interval", "p-value" have precise definitions that are routinely misreported. Most statistical scandals are definitional.
- **Law.** Legal definitions are explicit about their exclusions for exactly the reason mathematics is: a decision procedure must terminate on actual cases.
- **Machine learning.** Loss functions are definitions of "good". A model optimizes the definition it is given, including its unintended exclusions.

## 8. Mastery Criteria

You have this chapter when you can:

1. Unpack a nested definition to primitives without skipping steps.
2. Construct a near-miss example for any clause of a definition.
3. Detect a failure of well-definedness and repair it, either by canonical form or by redefining on equivalence classes.
4. Distinguish, in your own writing, a definition from a characterization theorem, and supply the correct proof obligations for each.
5. State the negation of any definition correctly and explain what a violation looks like concretely.
6. Identify the primitive (undefined) terms in a mathematical system you are using, and say why they were chosen as primitives.

**Diagnostic question.** "Here is a proposed definition. Find the object that satisfies every clause but one, and the object that satisfies the definition but should not." A learner who can do both has understood the definition; a learner who can only recite it has not.

### AI Tutor Brief

- **Generate:** (i) definitions with a deliberately missing clause, asking the learner to find the counterexample; (ii) "write the definition of X" tasks for concepts the learner already uses informally; (iii) well-definedness traps involving representatives, orderings, or choices; (iv) near-miss classification tasks.
- **Probe misconceptions:** treating a definition as a theorem; using only one direction of an "iff"; ignoring degenerate cases; assuming well-definedness without proof.
- **Transfer distance:** medium. Definitions transfer well, so push on *unfamiliar* concepts defined in the prompt itself — the learner must reason from the given definition, not from prior knowledge.
- **Do not** let the learner appeal to a textbook definition. If the problem supplies a definition, that definition is the only permitted source of meaning.

---

# Chapter 3 — Logic: The Grammar of Inference

## 1. Core Idea

Logic is the study of **which conclusions are forced by which premises**, independent of what the premises are about. Its power is exactly its content-independence: the same rules validate an argument about primes and an argument about interest rates. Its blindness is the same fact: logic can tell you that your conclusion follows, never that your premises are worth holding, and never that your conclusion is interesting.

For the working mathematician, logic is not a subject to be studied but a **hygiene discipline**. It supplies four things:

1. A canonical form for statements (connectives and quantifiers).
2. A mechanical procedure for negation.
3. A sharp distinction between validity (the argument's form) and truth (the premises' content).
4. A catalog of errors that *look* like reasoning.

## 2. First Principles

**Connectives.** $\neg$ (not), $\land$ (and), $\lor$ (or, inclusive), $\implies$ (implies), $\iff$ (iff). Each is defined by its truth table. Two consequences matter constantly:

- $P \implies Q$ is equivalent to $\neg P \lor Q$. In particular, an implication is false **only** when $P$ is true and $Q$ is false.
- $P \implies Q$ is *not* the same as $Q \implies P$ (converse), nor as $\neg P \implies \neg Q$ (inverse). It **is** equivalent to $\neg Q \implies \neg P$ (contrapositive).

**Quantifiers as a game.** $\forall x \, P(x)$ means: an adversary may choose any $x$ in the domain, and $P$ must hold. $\exists x \, P(x)$ means: you must produce a witness $x$, and then $P$ must hold. Reading quantifiers as a game with alternating moves makes their *order* visceral: whoever moves later can see the earlier choices.

$$\forall \varepsilon>0\ \exists \delta>0\ \forall x: \quad \text{the } \delta \text{ may depend on } \varepsilon \text{ but not on } x.$$
$$\exists \delta>0\ \forall \varepsilon>0\ \forall x: \quad \text{one } \delta \text{ must work for all } \varepsilon.$$

These are wildly different claims, and the difference is *entirely* the order of the first two quantifiers.

**Negation is mechanical.** Push $\neg$ inward, flipping each quantifier and negating the body:

$$\neg\big(\forall x\, \exists y\, P(x,y)\big) \equiv \exists x\, \forall y\, \neg P(x,y).$$

There is no need for intuition here. Negation is an algorithm, and getting it wrong is a computational error, not a conceptual one.

**Vacuous truth.** $\forall x \in \emptyset\, P(x)$ is true for any $P$. Likewise $P \implies Q$ is true whenever $P$ is false. This is not a convention to be tolerated; it is forced by the truth table, and it is *useful*: it lets theorems be stated without carving out empty cases. But it also means that a statement can be true and completely uninformative, so "true" and "substantive" are different questions.

**Validity versus soundness.** An argument is **valid** if the conclusion follows from the premises. It is **sound** if it is valid *and* the premises are true. Valid-but-unsound arguments are the standard vehicle of mathematical-looking nonsense: "All primes are odd; $2$ is prime; therefore $2$ is odd" is perfectly valid.

## 3. Reasoning Process

1. **Canonicalize.** Rewrite the statement using only $\neg, \land, \lor, \implies, \forall, \exists$, with all quantifiers at the front where possible. Remove "unless", "but", "however", "only when" by translating them explicitly.
2. **Mark the dependencies.** Draw arrows from each quantified variable to the statements that may depend on it. A $\delta$ that depends on $x$ when it should not is now visible as a stray arrow.
3. **Negate mechanically** if you plan to argue by contradiction, or if you want to know what a counterexample must look like. The negation is also the specification for a counterexample search.
4. **Separate form from content.** Ask: is the *shape* of this argument valid? Then ask: are the premises true? Do these in that order; mixing them is how people talk themselves into errors.
5. **Hunt the quantifier swap.** The single most common logical error in analysis, probability, and optimization is exchanging $\forall$ and $\exists$. Check every "there exists" for what it is allowed to depend on.
6. **Check the vacuity.** Is the hypothesis satisfiable? If not, the theorem is true and empty, and you have learned nothing.

## 4. Demonstrations

### Demonstration 3.1 — Negating a definition correctly

*Definition (continuity at $a$).*
$$C(a): \quad \forall \varepsilon>0\ \exists \delta>0\ \forall x\ \big(|x-a|<\delta \implies |f(x)-f(a)|<\varepsilon\big).$$

*Negation.* Apply the algorithm:
$$\neg C(a): \quad \exists \varepsilon>0\ \forall \delta>0\ \exists x\ \big(|x-a|<\delta \land |f(x)-f(a)|\ge \varepsilon\big).$$

Read as a game: *there is a tolerance $\varepsilon$ that you cannot meet; no matter how tightly I am required to confine $x$, you can find an $x$ within that confinement whose value is off by at least $\varepsilon$.* This is precisely the operational meaning of discontinuity, and it tells you how to *prove* discontinuity: exhibit the bad $\varepsilon$, then for each $\delta$ exhibit the bad $x$.

*Worked instance.* $f(x) = 1/x$ for $x \neq 0$, $f(0)=0$, at $a=0$. Take $\varepsilon = 1$. Given any $\delta>0$, choose $x = \min(\delta/2, 1/2)$, so $|x|<\delta$ and $|f(x)| = 1/x \ge 2 > 1 = \varepsilon$. Hence $\neg C(0)$ holds: $f$ is discontinuous at $0$. $\blacksquare$

**What to notice.** The proof of discontinuity is *generated* by the negated formula. There was no guesswork. This is the practical payoff of mechanical negation: it converts "show that it fails" into a construction with explicit slots.

### Demonstration 3.2 — The quantifier swap that changes the theorem

*Statement A (continuity on a set).* $\forall x \in (0,1)\ \forall \varepsilon>0\ \exists \delta>0\ \forall y \in (0,1): |x-y|<\delta \implies |f(x)-f(y)|<\varepsilon.$

*Statement B (uniform continuity).* $\forall \varepsilon>0\ \exists \delta>0\ \forall x,y \in (0,1): |x-y|<\delta \implies |f(x)-f(y)|<\varepsilon.$

In A, $\delta$ may depend on $x$ and $\varepsilon$. In B, $\delta$ may depend only on $\varepsilon$. Clearly B implies A. The converse fails.

*Counterexample.* $f(x) = 1/x$ on $(0,1)$ satisfies A but not B.

*Proof of A.* Fix $x \in (0,1)$ and $\varepsilon>0$. For $y$ with $|y-x| < x/2$ we have $y > x/2$, hence
$$|f(x)-f(y)| = \frac{|y-x|}{xy} < \frac{|y-x|}{x\cdot (x/2)} = \frac{2|y-x|}{x^2}.$$
So $\delta = \min(x/2,\ \varepsilon x^2/2)$ works. Note that $\delta$ depends on $x$ — legitimately, because $x$ was chosen before $\delta$ in the quantifier order.

*Proof of $\neg$B.* Take $\varepsilon = 1$. Let $\delta>0$ be arbitrary. Choose $n$ large enough that $\frac{1}{n} < \delta$ and $\frac{1}{n}-\frac{1}{n+1} = \frac{1}{n(n+1)} < \delta$; set $x = 1/n$, $y = 1/(n+1)$. Then $|x-y|<\delta$ but
$$|f(x)-f(y)| = \left|n - (n+1)\right| = 1 \ge \varepsilon.$$
Since $\delta$ was arbitrary, $\neg$B holds. $\blacksquare$

**What to notice.** The *same* function, the *same* formula, and the only difference is which variable was chosen first. The failure of B is caused by the fact that as $x \to 0$, the required $\delta$ shrinks to $0$ — so no single $\delta$ serves all $x$. When you see a quantifier-order error in your own work, look for exactly this mechanism: *a quantity that blows up as a parameter varies*.

### Demonstration 3.3 — Converse and inverse errors

Let $P(x)$ be "$x = 2$" and $Q(x)$ be "$x^2 = 4$". The implication $P \implies Q$ is true. Its converse $Q \implies P$ is false ($x=-2$). Its inverse $\neg P \implies \neg Q$ is false for the same reason. Its contrapositive $\neg Q \implies \neg P$ is true.

*Why this matters in practice.* A problem that asks you to *solve* $x^2=4$ is asking for the set defined by $Q$, which properly contains the set defined by $P$. If you "solve" by assuming $P$, you have found one point and called it the answer. This is the mechanism behind the most common lost-marks error in algebra: performing a non-reversible operation (squaring, multiplying by an expression that might be zero, applying a non-injective function) and then failing to check.

**What to notice.** Every algebraic step is an implication. Steps that are *equivalences* preserve the solution set. Steps that are only implications enlarge it, and require a verification pass at the end. Track which is which, explicitly, while you work.

### Demonstration 3.4 — Vacuous truth, used well and used badly

*Used well.* "Every element of the empty set is a purple elephant" is true. This lets us state "every prime $p>2$ is odd" without a caveat, and it lets the statement "for all $x \in S$, $P(x)$" be true even when $S$ is empty — which is exactly what we want when a theorem's hypothesis happens to be unsatisfiable.

*Used badly.* "All unicorns are blue, therefore some unicorn is blue." The premise is vacuously true; the conclusion does not follow. The error is treating $\forall$ as implying $\exists$, which requires a nonempty domain.

**What to notice.** $\forall x\, P(x)$ and $\exists x\, P(x)$ differ by an existence assumption. In every theorem you use, ask whether the domain is guaranteed nonempty. This is precisely the gap in many false proofs about maxima and minima: "the maximum is attained at the point where..." presumes the maximum exists.

## 5. Connections

- **← Ch. 2.** Definitions supply the predicates; logic supplies the grammar. A definition with a missing clause is a logical error wearing a definitional costume.
- **→ Ch. 4.** Proof engines are logic in motion. Contrapositive and contradiction are direct applications of the equivalences above.
- **→ Ch. 11.** Extremal arguments live or die on an existence quantifier: "the maximum is attained" must be proved, not assumed.
- **→ Ch. 21.** Probability statements are quantified statements with a measure attached; quantifier errors here produce the classic "almost surely" versus "surely" confusions.
- **→ Ch. 29.** Statistical claims are quantified claims about populations and samples; nearly every misinterpretation is a quantifier-order or scope error.

## 6. Limitations

**Logic does not generate.** It audits. A valid proof of an uninteresting theorem is still uninteresting. The creative work — choosing definitions, conjecturing the right statement, finding the key construction — is not logical inference and is not mechanizable in practice.

**Formal validity can mask material failure.** An argument can be impeccable in form and useless in content because a premise is false, or because a term is being used equivocally. Logic sees only the form.

**Expressiveness limits.** First-order logic cannot express "for every property $P$" without ascending to second order, and sufficiently rich formal systems contain statements neither provable nor refutable within them. This is a real boundary on what formal derivation can deliver — but it is a boundary on *formal systems*, not on mathematical practice, which routinely steps outside a system to a richer one.

**The map of "all errors" is not logical.** Most actual mathematical mistakes are not logical fallacies. They are: using an unproved lemma, misreading a definition, generalizing from three cases, or drawing the picture wrong. Logic catches only the subset that is formally invalid.

## 7. Applications

- **Program correctness.** Loop invariants and pre/post-conditions are quantified statements; a Hoare triple is an implication. Debugging is often the construction of the counterexample to a false triple.
- **Contract design.** "For all inputs satisfying $P$, the function returns a value satisfying $Q$" is a specification; the negation tells you exactly what a failing test case must look like.
- **Experimental science.** A hypothesis is a quantified claim; a single well-chosen counterexample refutes it, while confirmation instances never prove it. This asymmetry is the logical core of the scientific method.
- **Risk and regulation.** "The system is safe" requires a quantifier: safe for all inputs, or for all inputs in a specified distribution, or with probability at least $1-\alpha$? These are different claims with different evidence requirements.
- **AI evaluation.** "The model is correct" versus "the model is correct on the test distribution" is a quantifier distinction that determines whether a benchmark result means anything at all.

## 8. Mastery Criteria

You have this chapter when you can:

1. Translate an English mathematical statement into canonical quantifier form, and back, without loss.
2. Negate any statement mechanically, and read the negation as an operational recipe.
3. Identify the dependence structure of every quantified variable in a definition and say which dependencies are legitimate.
4. Distinguish validity from soundness in a given argument, and construct a valid-but-unsound argument on demand.
5. State precisely when vacuous truth applies, and detect when a proof has assumed existence without proving it.
6. Given an algebraic manipulation, classify each step as an equivalence or a one-way implication, and say what verification it therefore requires.

**Diagnostic question.** "Negate: for every $\varepsilon$ there is $N$ such that for all $n>N$, $|a_n - L|<\varepsilon$." A learner who produces $\exists \varepsilon\ \forall N\ \exists n>N$ with $|a_n-L|\ge\varepsilon$ has the skill. A learner who produces "for every $\varepsilon$ there is $N$ such that for all $n>N$, $|a_n-L|\ge\varepsilon$" has negated the wrong part.

### AI Tutor Brief

- **Generate:** (i) statements to negate, escalating from single quantifiers to four alternating ones; (ii) quantifier-order pairs where one is true and the other false, with a request to prove both; (iii) arguments containing a converse/inverse error or a vacuous-existence error, to be diagnosed; (iv) "which step is not reversible?" audits of algebraic solutions.
- **Probe misconceptions:** swapping $\forall\exists$; negating the consequent instead of the whole implication; treating $\forall$ as implying $\exists$; believing a true implication licenses its converse.
- **Transfer distance:** medium-high. Logic transfers perfectly in form, so the difficulty must come from *content*: use unfamiliar definitions from analysis, probability, or combinatorics.
- **Do not** accept prose negations. Require symbols, in canonical order, with the dependency structure visible.

---

# Chapter 4 — Proof: The Technology of Shared Certainty

## 1. Core Idea

A **proof** is a finite sequence of statements, each of which is an axiom, a definition, a previously established result, or a consequence of earlier statements by a specified rule of inference, terminating in the claim.

That definition is correct and nearly useless, because it describes the *audit trail* rather than the *purpose*. The purpose is this:

> A proof is a device for making a conclusion **forced** for a competent skeptic who has not seen the argument before and who is actively looking for a gap.

Everything about proof writing follows from that sentence. It explains why proofs are explicit (the skeptic cannot read your mind), why they are finite (the skeptic must be able to check them), why they name their assumptions (the skeptic will not grant what you did not ask for), and why a proof that convinces only its author is not yet a proof.

## 2. First Principles

**What a proof must contain.** Four things, always:

1. **Premises.** Exactly what is assumed, stated up front.
2. **Goal.** Exactly what is to be shown, in canonical quantifier form (→ Ch. 3).
3. **Chain.** Steps that are each justified by a named rule, definition, or prior result.
4. **Closure.** An explicit statement that the goal has been reached, and under what conditions.

**The four engines.** Every proof uses one of four global strategies, and the choice is determined by the *shape of the goal*, not by taste.

| Engine | Used when the goal has the form | Mechanism |
|---|---|---|
| **Direct** | $P \implies Q$ | Assume $P$; derive $Q$. |
| **Contrapositive** | $P \implies Q$ where $\neg Q$ is more informative than $P$ | Prove $\neg Q \implies \neg P$; equivalent by Ch. 3. |
| **Contradiction** | $S$, where $S$ has no obvious hypothesis to assume | Assume $\neg S$; derive an impossibility. |
| **Cases** | $S$ where the domain splits into finitely many kinds | Prove $S$ on each kind; argue the kinds exhaust the domain. |

**Existence and uniqueness are separate obligations.** "There is exactly one $x$ with property $P$" is two theorems: $\exists x\,P(x)$, and $\forall x\forall y\,(P(x)\land P(y)\implies x=y)$. They almost always have different proofs, and conflating them produces the standard error of exhibiting an object and declaring it unique.

**Constructive versus non-constructive existence.** A constructive proof produces the object (or an algorithm for it). A non-constructive proof shows that the object must exist without producing it. Both are legitimate. But they deliver different things: a constructive proof gives you a computation, a non-constructive proof gives you only a guarantee. Know which one you have.

**Rigor is a spectrum, not a binary.** Standards of rigor rise over time; proofs accepted in one era are repaired in the next. In practice, rigor means: *every gap is either filled or explicitly flagged*. A proof with one flagged gap is more honest and more useful than a proof with an unflagged one.

## 3. Reasoning Process

1. **Write the goal in quantifier form.** If you cannot, you do not yet know what you are proving (→ Ch. 2, 3).
2. **List your assets.** Hypotheses, definitions, previously proved results. Everything not on this list is unavailable. This is the single most effective anti-circularity device.
3. **Match the goal's shape to an engine.** Goal is an implication? Direct or contrapositive. Goal is a negative claim ("no such object exists")? Contradiction. Goal is a classification? Cases. Goal is a "for all $n$"? Induction (→ Ch. 10).
4. **Work from both ends.** Derive consequences of the assets; derive prerequisites of the goal; aim to make the two frontiers meet. Most proofs are found backwards and written forwards.
5. **Fill gaps in order of cheapness.** Algebraic manipulations first, then case splits, then auxiliary constructions (→ Ch. 17).
6. **Audit.** Four questions, every time:
   - Are all cases covered? (Draw the boundary of the domain.)
   - Is anything assumed that was not granted? (Check against the asset list.)
   - Is any step non-reversible in a way that requires a verification pass? (→ Ch. 3.)
   - Does the conclusion say exactly what was claimed, no more? (Universality creep is common: proving it for positive integers when the claim was all integers.)
7. **Rewrite for the reader.** Put the key idea first. A proof is a communication, and the reader's first thirty seconds determine whether they will find the gap.

## 4. Demonstrations

### Demonstration 4.1 — Irrationality of $\sqrt2$, with the engine made visible

*Claim.* There is no rational $r$ with $r^2 = 2$.

*Proof.* Suppose, for contradiction, that $r^2 = 2$ with $r \in \mathbb{Q}$. Write $r = p/q$ with $p,q \in \mathbb{Z}$, $q \neq 0$, and $\gcd(p,q) = 1$ — that is, in lowest terms. (Every rational has such a representation; this is a canonical-form fact, → Ch. 14.)

Then $p^2 = 2q^2$, so $p^2$ is even. Since the square of an odd number is odd, $p$ is even (this is the contrapositive, → Demonstration 4.3). Write $p = 2k$. Then $4k^2 = 2q^2$, so $q^2 = 2k^2$, and by the same argument $q$ is even.

Hence $2 \mid p$ and $2 \mid q$, contradicting $\gcd(p,q)=1$. Therefore no such $r$ exists. $\blacksquare$

**What to notice — three things.**

1. The engine is **contradiction**, but the *content* is a **descent**: from a putative solution in lowest terms we produce a smaller one (dividing both by $2$), and lowest terms forbids infinite descent. The lowest-terms hypothesis is doing all the work; without it the argument proves nothing. This is the prototype of the minimal-counterexample method (→ Ch. 10, 32).
2. The step "$p^2$ even $\Rightarrow$ $p$ even" is not obvious and is *not* proved here — it is cited as a lemma. Every proof has such citations; the discipline is to know which ones you are leaning on.
3. The argument is a **template**, not a fact about $2$. The same descent proves $\sqrt{n}$ irrational for every $n$ that is not a perfect square (using prime factorization). Recognizing templates is how one proof becomes many (→ Ch. 18).

### Demonstration 4.2 — A non-constructive existence proof

*Claim.* There exist irrational numbers $x, y$ such that $x^y$ is rational.

*Proof.* Consider $\alpha = \sqrt2^{\sqrt2}$. By trichotomy, $\alpha$ is either rational or irrational.

- **Case 1:** $\alpha$ is rational. Take $x = y = \sqrt2$, both irrational, and $x^y = \alpha$ rational. Done.
- **Case 2:** $\alpha$ is irrational. Take $x = \alpha$ and $y = \sqrt2$. Then
$$x^y = \left(\sqrt2^{\sqrt2}\right)^{\sqrt2} = \sqrt2^{\sqrt2 \cdot \sqrt2} = \sqrt2^{2} = 2,$$
which is rational. Done. $\blacksquare$

**What to notice.** The proof splits on a dichotomy and in one branch produces a *specific* pair; in the other it produces a pair whose first component it cannot identify. We learn that a suitable pair exists without learning, in Case 2, what $x$ actually is. This is the characteristic signature of a non-constructive existence proof: **the law of excluded middle does the construction for you.**

This is legitimate mathematics, and it is also a warning: if your goal is an algorithm, this proof gives you none. (In fact $\sqrt2^{\sqrt2}$ is irrational, by the Gelfond–Schneider theorem — so Case 2 is the live one, and the "construction" is useless computationally.)

### Demonstration 4.3 — Choosing the engine by goal shape

*Claim.* For every integer $n$, if $n^2$ is odd then $n$ is odd.

*Direct attempt.* Assume $n^2$ odd. Then $n^2 = 2k+1$. We want $n = 2m+1$. From $n^2 = 2k+1$ we would need to extract a square root — not available in the integers. Direct proof stalls.

*Contrapositive.* The contrapositive of "$n^2$ odd $\Rightarrow$ $n$ odd" is "$n$ even $\Rightarrow$ $n^2$ even". Assume $n = 2m$. Then $n^2 = 4m^2 = 2(2m^2)$, which is even. $\blacksquare$

**What to notice.** The contrapositive is not a trick; it is the *same* claim (Ch. 3), and it is easier because the hypothesis "$n$ even" hands you a usable algebraic form ($n=2m$), whereas "$n^2$ odd" hands you a form you cannot factor. **Rule of thumb: prefer the contrapositive when the negated conclusion gives you a structural form that the original hypothesis does not.**

A contradiction proof would also work (assume $n^2$ odd and $n$ even, derive $n^2$ even, contradiction) but is strictly longer: it proves the same implication and then adds a detour. Prefer the weakest engine that suffices.

### Demonstration 4.4 — A proof with a missing case, and its repair

*Claim.* For every real $x$, if $x^2 < x$ then $0 < x < 1$.

*Flawed proof.* Divide both sides of $x^2<x$ by $x$ to obtain $x<1$. Since $x^2 \ge 0$, we also have $0 \le x^2 < x$, so $x>0$. Hence $0<x<1$. $\blacksquare$

*Diagnosis.* The division by $x$ is only valid when $x>0$ — which is exactly one of the things being proved. This is **circular reasoning** in its most common form: an algebraic operation silently assumes a hypothesis. The proof is also invalid for $x<0$.

*Repair by cases.*

- If $x = 0$: $x^2 = 0 \not< 0 = x$. Hypothesis fails.
- If $x < 0$: then $x^2 > 0 > x$, so $x^2 > x$. Hypothesis fails.
- If $x > 0$: dividing $x^2<x$ by $x>0$ gives $x<1$. So $0<x<1$.

The three cases exhaust $\mathbb{R}$, and in the only surviving case the conclusion holds. $\blacksquare$

**What to notice.** The flaw was not in the algebra; it was in the **domain coverage**. The original proof covered one third of the domain and asserted the rest. This is the most frequent serious error in olympiad and research writing alike, and the audit question "are all cases covered?" is the only reliable defense. Note also that the repaired proof is *shorter to verify* than the flawed one, because each case is trivial.

## 5. Connections

- **← Ch. 2, 3.** Proofs are definitional unpacking plus logical inference. A gap is almost always an unpacking you skipped or a quantifier you moved.
- **→ Ch. 8, 10, 11.** The four engines are the skeleton; invariants, induction, and extremality are the *content* that most olympiad proofs are made of.
- **→ Ch. 17.** Working backwards is how the chain in step 4 of the Reasoning Process actually gets built.
- **→ Ch. 32.** The audit is adversarial: you are hunting for the counterexample that your own proof has excluded by accident.
- **→ Ch. 35.** Communicating a proof is a distinct skill from finding one, and it is the skill that determines whether your work has any effect.

## 6. Limitations

**A proof does not explain.** The classic example is the algebraic proof that $\binom{2n}{n}$ is even for $n \ge 1$ via $\binom{2n}{n} = 2\binom{2n-1}{n-1}$: correct, and it tells you nothing about *why*. The combinatorial proof (pair each subset with its complement) is the explanation. Prefer proofs that explain, when you can find them — they generalize (→ Ch. 12).

**Correct proofs can be uninformative.** A proof by exhaustive verification of $10^6$ cases establishes the theorem and advances understanding not at all. This is a real trade-off, not a defect of rigor.

**Proof does not establish applicability.** A theorem about an abstract structure is true of that structure. Whether the structure models your situation is a separate question (→ Ch. 1, 25).

**Some claims cannot be stated sharply enough to prove.** Many important practical questions ("is this program correct?") resist precise formulation: the program's behavior often *defines* the specification rather than the reverse. Demanding proof of an ill-posed claim produces the illusion of rigor rather than rigor.

**Rigor is expensive.** Full formalization is rarely worth the cost outside of critical systems. The working standard is: gaps flagged, key lemmas isolated, boundary cases checked.

## 7. Applications

- **Software verification.** A type system, a contract, or a model checker is a proof engine with a restricted logic. Knowing which engine you are in tells you what it can and cannot certify.
- **Experimental design.** A falsification protocol is a contrapositive argument: to establish "$H$ implies $O$", test $\neg O$ and infer $\neg H$.
- **Quantitative finance.** A pricing argument is a proof from axioms (no arbitrage, market completeness) to a conclusion (a unique price). The 2008 crisis was, in part, a failure to audit which axioms the models actually required.
- **Engineering safety cases.** A safety case is a proof with explicit premises; most failures trace to an unstated premise ("the operator will respond within 30 seconds") rather than to invalid inference.
- **Mathematical writing.** A paper's correctness is judged by strangers, which is exactly the skeptic model above. Write for the skeptic, not for the author.

## 8. Mastery Criteria

You have this chapter when you can:

1. State, for any claim, which of the four engines is appropriate and *why*, based on the goal's logical form.
2. Write a proof that a competent stranger can check without asking a question.
3. Separate existence from uniqueness and discharge both obligations explicitly.
4. Distinguish constructive from non-constructive existence, and say what each delivers.
5. Find the missing case in a supplied proof, and repair it without adding length.
6. Detect circular reasoning, including the algebraic variety where an operation silently assumes a hypothesis.
7. Produce an alternative proof of a known result that explains *why* it is true, and compare the explanatory value of the two.

**Diagnostic question.** "Here is a correct-looking proof. Find the case it does not cover, or the hypothesis it uses without being granted, or the step that is not reversible." A learner who cannot find one on demand cannot audit their own work either.

### AI Tutor Brief

- **Generate:** (i) proofs with exactly one planted defect (missing case, circularity, quantifier slip, non-reversible step); (ii) claims where the contrapositive is dramatically easier, to test engine selection; (iii) existence-and-uniqueness problems requiring both halves; (iv) requests to produce both a constructive and a non-constructive proof of the same existence claim.
- **Probe misconceptions:** "proof = computation"; assuming the conclusion in algebraic disguise; believing a diagram is a case analysis; treating one example as a proof.
- **Transfer distance:** high. Use unfamiliar domains so the learner cannot pattern-match to a memorized proof template.
- **Do not** accept "it's clear" or "obviously". Require the named justification for every nontrivial step. Conversely, do not demand formalization of arithmetic identities — the standard is a competent human skeptic, not a proof assistant.

---

# Chapter 5 — Abstraction and the Ladder of Structure

## 1. Core Idea

**Abstraction is deliberate information loss.** You discard every feature of a situation that the argument does not use, keep the features it does use, and thereby obtain a statement that applies to *everything* sharing those features.

The discarded information is not wasted; it is what makes the result portable. A theorem about "any finite set with a group acting on it" is more useful than a theorem about the vertices of a specific hexagon, precisely because it forgot the hexagon.

Abstraction happens in rungs:

1. **Instance** — this triangle, this number, this graph.
2. **Pattern** — a regularity observed across instances ("the sum is always a perfect square").
3. **Structure** — the axioms that generate the pattern ("a finite abelian group of odd order").
4. **Structure of structures** — relations between structures (homomorphisms, quotients, duality).

Most learners stop at rung 2 and mistake pattern recognition for understanding. Most working mathematicians live at rung 3. The genuinely powerful move — and the one this chapter trains — is knowing **which rung the problem requires**, because climbing too high destroys the properties you need.

## 2. First Principles

**Why information loss is productive.** Consider a claim about all $n$-gons. At rung 1 you must check infinitely many figures. At rung 2 you notice the angle sum looks like $(n-2)\pi$. At rung 3 you prove it once by triangulation, and the proof uses only: (i) a polygon can be cut into triangles, (ii) triangle angle sum is $\pi$, (iii) the cuts contribute no net angle. Nothing else. Because the proof consumed only those three facts, it is valid for every polygon for which those three facts hold — and you now know exactly where it might fail.

**The quotient construction.** The formal mechanism of abstraction is the **quotient**: define an equivalence relation, then treat equivalence classes as new objects. Abstracting "the integer $n$" to "the class $[n]$ modulo $12$" discards $n$ and keeps only its residue. What survives is exactly what the operations respect.

This gives the precise criterion for when abstraction is legitimate: **you may quotient by a relation exactly when every operation you intend to use is well-defined on the classes** (→ Ch. 2). Arithmetic mod $12$ is legitimate because addition and multiplication of residues do not depend on representatives. Ordering of residues is *not* well-defined, which is why $\mathbb{Z}/12\mathbb{Z}$ has no natural order — a structural fact with real consequences.

**The minimal-structure principle.** Use the weakest axioms that support your argument. If your proof never uses commutativity, state the theorem for non-abelian groups: you have strengthened the result at zero cost. If your proof uses order, you cannot state it for groups at all.

**Abstraction hides mechanism.** A theorem at rung 3 tells you *that* something holds for all groups; it does not tell you *which* element of your particular group does the job. This is the price: generality is bought with constructivity.

## 3. Reasoning Process

1. **Inventory the features.** List everything true of the situation: sizes, orderings, algebraic operations, topology, symmetries, finiteness, positivity.
2. **Mark usage.** For each feature, ask: does my argument *use* this? Be strict — "it feels relevant" is not usage. Cross out unused features.
3. **Climb to the rung that keeps the used features and drops the rest.** That is the correct level of generality.
4. **Check the quotient is legitimate.** If you have replaced objects by classes, verify well-definedness of every operation you use.
5. **Prove once at that rung.** The proof should now be shorter, because you have fewer hypotheses to juggle and no irrelevant detail.
6. **Descend and instantiate.** Apply the abstract result to each concrete model, and check that each model actually satisfies the axioms. Most misapplications happen here, not in the abstract proof.

## 4. Demonstrations

### Demonstration 5.1 — Climbing from figures to $n$-gons

*Claim.* The interior angles of a convex $n$-gon sum to $(n-2)\pi$.

*Proof.* Choose a vertex $v$. Because the polygon is convex, the segments from $v$ to each non-adjacent vertex lie inside the polygon, cutting it into exactly $n-2$ triangles. (There are $n-3$ non-adjacent vertices besides the two neighbors of $v$; each segment adds one triangle, starting from $1$ triangle when $n=3$.) The angles of these triangles partition the interior angles of the polygon, and each triangle contributes $\pi$. Hence the total is $(n-2)\pi$. $\blacksquare$

**What to notice.** The proof consumed exactly three facts: convexity (so the cuts stay inside), triangulability (so the pieces are triangles), and the triangle angle sum (the base case). At rung 1, "the angle sum" is a fact about a drawing. At rung 3 it is a theorem about *any* object admitting a triangulation with those properties — which is why the same computation works for the angle defect on surfaces and reappears in the Gauss–Bonnet theorem.

**Where it breaks (and this is the point).** Convexity is genuinely used. For a non-convex simple polygon the angle sum formula still holds, but the *proof* needs a different triangulation argument (a simple polygon always admits a triangulation, but not by fanning from an arbitrary vertex). And for a self-intersecting polygon the formula fails. Knowing exactly which hypothesis the proof consumed tells you exactly where to look for failure — this is the practical form of "understanding the abstraction".

### Demonstration 5.2 — Proving once at rung 3 and instantiating twice

Let $G$ be a group: a set with an associative operation, an identity $e$, and inverses.

*Claim.* If $a^2 = e$ for every $a \in G$, then $G$ is abelian.

*Proof.* Let $a,b \in G$. Since $a^2 = e$, multiplying on the right by $a^{-1}$ gives $a = a^{-1}$; similarly $b = b^{-1}$. Now
$$(ab)^2 = e \implies abab = e \implies ab = (ab)^{-1} = b^{-1}a^{-1} = ba,$$
using the identity $(xy)^{-1} = y^{-1}x^{-1}$ and the fact that $a^{-1}=a$, $b^{-1}=b$. Hence $ab = ba$. $\blacksquare$

**What to notice.** The proof used only: associativity, inverses, identity, and the hypothesis $a^2=e$. It never mentioned what the elements *are*. So it holds in every model:

- $G = \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ under addition (here $a^2 = a+a = 0$ for all $a$): abelian. ✓
- $G =$ the four symmetries of a non-square rectangle (identity, horizontal flip, vertical flip, $180^\circ$ rotation), under composition: each non-identity element is its own inverse, and the group is abelian. ✓
- $G =$ the symmetries of an equilateral triangle ($S_3$, six elements): the hypothesis fails (a $120^\circ$ rotation does not square to the identity), so the theorem says nothing. ✓ — and indeed $S_3$ is not abelian.

**What to notice (second).** The third bullet is as important as the first two. A theorem is only applicable when its hypotheses hold, and checking hypotheses is a separate skill from proving the theorem. Learners routinely apply an abstract result to a model that does not satisfy its axioms.

### Demonstration 5.3 — The quotient, done properly

*Construction.* On $\mathbb{Z}$, define $a \sim b$ iff $12 \mid (a-b)$. This is an equivalence relation (reflexive, symmetric, transitive — each is a one-line check). Let $[a]$ denote the class of $a$, and let $\mathbb{Z}/12\mathbb{Z} = \{[0],[1],\dots,[11]\}$.

*Attempted definition.* $[a] + [b] := [a+b]$.

*Well-definedness.* Suppose $[a] = [a']$ and $[b] = [b']$, i.e. $a' = a + 12m$ and $b' = b + 12n$. Then
$$a' + b' = a + b + 12(m+n),$$
so $[a'+b'] = [a+b]$. The definition does not depend on the representatives. $\blacksquare$

*Attempted definition that fails.* $[a] \le [b] := a \le b$.

*Failure.* $[0] = [12]$ and $0 \le 1$, so $[0] \le [1]$. But also $12 \le 1$ is false, so with representatives $0' = 12$, $b'=1$ we get $[0] \not\le [1]$. The relation depends on representatives and is therefore not a relation on classes at all.

**What to notice.** Abstraction is not free: it is licensed by invariance. The quotient construction tells you *exactly* which structures survive the abstraction — here, the additive and multiplicative structure survive, the order does not. This is the general pattern behind quotient spaces, quotient groups, and the reason "modulo $n$" arithmetic is a ring but not an ordered ring.

## 5. Connections

- **← Ch. 1.** This chapter is the *method* for the object studied in Chapter 1.
- **← Ch. 2.** Well-definedness is the gatekeeper of every quotient.
- **→ Ch. 14.** Canonical forms are the computational face of quotients: lowest terms, reduced echelon form, cycle decomposition.
- **→ Ch. 18.** Generalization is abstraction along the parameter axis; this chapter is abstraction along the feature axis.
- **→ Ch. 19.** Isomorphism is the statement that two structures are the same rung-3 object; duality is a rung-4 relation.
- **→ Ch. 25.** Modeling is abstraction applied to the world, with the additional hazard that the world does not come with axioms.

## 6. Limitations

**Over-abstraction.** Climb too high and you lose the property that made the problem solvable. A theorem about "any set" cannot use order; a theorem about "any ring" cannot use division. The correct rung is determined by the *argument*, not by ambition.

**Abstraction can conceal the mechanism.** Knowing that a finite group's element orders divide its order does not tell you how to find the order of a given element. Generality and constructivity trade off.

**Quotients can destroy information you need later.** Working mod $12$ loses the integer. If a later step requires the actual value, the abstraction is premature — this is the mathematical form of "losing the units".

**Abstractions can be vacuous.** A structure with no models supports every theorem and means nothing. Always ask whether the axioms are satisfiable, and whether they are satisfiable by something you care about.

**Naming is not understanding.** Saying "this is a matroid" or "this is a Hilbert space" is the beginning of an analysis, not the end. The value is in knowing which theorems of that structure apply — which requires knowing which hypotheses they use.

## 7. Applications

- **Programming.** An interface is an abstraction: it fixes the operations and their contracts, and hides the representation. A good interface is exactly a set of axioms; a leaky abstraction is one whose axioms are violated by its implementations.
- **Physics.** "Particle", "field", "temperature" are rung-3 abstractions; their power is that thermodynamic theorems apply to any system satisfying the axioms, regardless of microstructure.
- **Statistics.** "Random variable" abstracts away the sample space; you keep the distribution and discard the outcomes. This is why the same theorem covers dice, insurance claims, and noise.
- **Economics.** "Utility function" and "equilibrium" are abstractions whose axioms (completeness, transitivity, convexity) are empirically contestable — a case where the abstraction's hypotheses are the weak point, not its logic.
- **Machine learning.** "Function class", "capacity", "generalization bound" are abstractions over datasets. Knowing which assumptions a bound uses tells you when it will fail to predict practice.

## 8. Mastery Criteria

You have this chapter when you can:

1. Take a concrete result and identify the minimal set of features its proof uses.
2. State the result at the correct rung, and exhibit at least two models that satisfy the hypotheses and one that does not.
3. Construct a quotient legitimately: define the relation, prove it is an equivalence, and prove the operations are well-defined.
4. Give an example where quotienting destroys a structure that a later step needs.
5. Explain the trade-off between generality and constructivity in a specific case.
6. Recognize when a name ("group", "metric space", "matroid") is being used as a substitute for an argument, and demand the specific hypotheses.

**Diagnostic question.** "Here is a proof. Which hypotheses did it actually use?" A learner who answers by listing all the hypotheses has not understood the proof. A learner who can delete a hypothesis and show the proof still works has.

### AI Tutor Brief

- **Generate:** (i) "delete a hypothesis" tasks — prove the theorem with a weaker assumption, or exhibit a counterexample showing the hypothesis is needed; (ii) quotient constructions with a well-definedness obligation; (iii) classification tasks: which of these five objects satisfy the given axioms?; (iv) problems stated in a concrete domain that become easy once the learner identifies the structure.
- **Probe misconceptions:** pattern-matching without proof; assuming all hypotheses are necessary; applying abstract theorems without checking hypotheses; believing "more general" always means "better".
- **Transfer distance:** high, but always include a *hypothesis-checking* item, since that is where transfer fails in practice.
- **Do not** reward naming structures. Reward correct identification of which theorems apply and why.

---

# Chapter 6 — First-Principles Reasoning

## 1. Core Idea

**First-principles reasoning** means rebuilding a claim from the smallest set of assumptions you can personally defend, rather than citing an authority, a formula, or an analogy.

It is not a rejection of prior knowledge. It is a **dependency audit**: for every statement you use, you know what it rests on, and you know which of those supports you could reconstruct if challenged.

The practical form is a **why-chain**. Ask "why?" repeatedly until you hit something you are willing to accept as bedrock — a definition, an axiom, or an observation. What remains is the actual content of the claim. Everything above the bedrock is scaffolding that can be rebuilt in a different shape when the problem changes.

## 2. First Principles

**The three layers.** Every mathematical system has:

- **Primitives** — undefined terms (set, point, line, element).
- **Axioms** — accepted without proof (the parallel postulate, the completeness of $\mathbb{R}$).
- **Theorems** — everything else, derived.

The layers are a *choice*, not a discovery. Different choices produce different mathematics (Euclidean versus hyperbolic geometry). Knowing which layer a statement lives in tells you what it would take to overturn it: a theorem falls to a counterexample, an axiom falls only to a different axiom system.

**The dependency graph.** Theorems form a directed acyclic graph: $A$ supports $B$ if $B$'s proof uses $A$. This graph is the real structure of a subject, and it is almost never the same as the order of chapters in a textbook. Reconstructing a fragment of the graph is the single most efficient way to learn an advanced field.

**Two tests for "fundamental".** A statement is fundamental to the extent that:

1. **It has lasted.** Longevity is evidence that it is not an artifact of a temporary formalism.
2. **It is generative.** The rest of the field can be *derived* from it using standard methods, rather than merely stated in its vocabulary.

These tests are heuristics, not theorems. But they reliably distinguish core ideas from notational conventions.

**Why derivation beats memorization.** A memorized formula is a single point of failure with no error-correction. A derived formula comes with its own audit trail: if you can derive it, you can check it in an unfamiliar case, adapt it when the hypotheses change, and notice when it does not apply. Derivation is slower once and faster forever.

## 3. Reasoning Process

1. **Pick the claim.** State it precisely (→ Ch. 2, 3).
2. **List its supports.** What does the standard proof use? Name each lemma, formula, and definition.
3. **Ask "why?" of each support.** Repeat until bedrock. Mark anything you cannot derive and cannot defend as a **gap** — honestly.
4. **Identify the weakest sufficient hypothesis.** Which supports are actually load-bearing? Delete each in turn and see what breaks. This is where new mathematics comes from (→ Ch. 18).
5. **Reconstruct.** Derive the claim from the bedrock without looking. The reconstruction will differ from the textbook's, and that difference is your understanding.
6. **Test the reconstruction.** Apply it in a case the textbook did not consider. If it fails, you have found either an error or a hypothesis you did not notice.
7. **Record the graph.** Write the dependency fragment down. It becomes reusable capital.

## 4. Demonstrations

### Demonstration 6.1 — The quadratic formula, with every assumption surfaced

*Claim.* If $a \neq 0$, the solutions of $ax^2 + bx + c = 0$ are $x = \dfrac{-b \pm \sqrt{b^2-4ac}}{2a}$.

*Derivation.* Since $a \neq 0$, divide by $a$:
$$x^2 + \frac{b}{a}x + \frac{c}{a} = 0.$$
Complete the square: add and subtract $\left(\frac{b}{2a}\right)^2$:
$$\left(x + \frac{b}{2a}\right)^2 - \frac{b^2}{4a^2} + \frac{c}{a} = 0 \implies \left(x+\frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}.$$
Take square roots — **here the assumption that we work over an ordered field, or at least a field with square roots, enters**:
$$x + \frac{b}{2a} = \pm\frac{\sqrt{b^2-4ac}}{2a} \implies x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}. \qquad \blacksquare$$

**Assumption audit.** (i) $a \neq 0$ — otherwise the equation is linear and the formula divides by zero. (ii) $2a \neq 0$ — implied by (i) in a field of characteristic $\neq 2$. (iii) The discriminant $b^2-4ac$ must have a square root in the ambient field: over $\mathbb{R}$ this requires $b^2-4ac \ge 0$; over $\mathbb{C}$ it always holds; over $\mathbb{Q}$ it holds only when the discriminant is a perfect square. (iv) Characteristic $\neq 2$ is genuinely needed — in characteristic $2$ the formula is not even meaningful.

**What to notice.** The formula is not a fact about symbols; it is a *conditional* fact with four hypotheses. Three of them are invisible in the usual presentation. A first-principles derivation surfaces all four, and thereby tells you exactly when the formula will betray you.

### Demonstration 6.2 — AM–GM from a single inequality

*Claim.* For real $a,b \ge 0$, $\dfrac{a+b}{2} \ge \sqrt{ab}$, with equality iff $a=b$.

*Derivation.* For any real $x$, $x^2 \ge 0$. Take $x = \sqrt a - \sqrt b$ (legitimate since $a,b\ge0$):
$$(\sqrt a - \sqrt b)^2 \ge 0 \implies a - 2\sqrt{ab} + b \ge 0 \implies \frac{a+b}{2} \ge \sqrt{ab}.$$
Equality holds iff $\sqrt a = \sqrt b$ iff $a=b$. $\blacksquare$

**Assumption audit.** The derivation uses: (i) squares of reals are non-negative; (ii) $\sqrt{\cdot}$ is defined for non-negative reals; (iii) the field operations respect order. Note what is **not** used: no calculus, no induction, no case analysis, no cleverness.

**What to notice.** The entire content of AM–GM, for two variables, is the triviality $(\sqrt a - \sqrt b)^2 \ge 0$. The general $n$-variable inequality is *not* a triviality, and the fact that the two-variable case is easy is misleading. This is a case where first-principles reasoning also tells you where the difficulty lives: in the passage from $2$ to $n$ (→ Ch. 10, 20).

Also note: this argument is unavailable for complex numbers, because $\mathbb{C}$ has no order compatible with its field operations. AM–GM is a theorem about *ordered* fields. Trying to use it on complex moduli is legitimate only after passing to $|z| \in \mathbb{R}_{\ge 0}$.

### Demonstration 6.3 — Two derivations of $1+2+\cdots+n$, and what each one teaches

*Claim.* $\displaystyle\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$ for $n \ge 1$.

**Derivation A (pairing).** Write the sum forwards and backwards and add columnwise:
$$\begin{array}{cccccc}
S &=& 1 &+& 2 &+ \cdots +& n\\
S &=& n &+& (n-1) &+ \cdots +& 1\\
\hline
2S &=& (n+1) &+& (n+1) &+ \cdots +& (n+1)
\end{array}$$
There are $n$ columns, each summing to $n+1$, so $2S = n(n+1)$. $\blacksquare$

**Derivation B (induction).** Base case $n=1$: $1 = 1\cdot 2/2$. Inductive step: if $\sum_{k=1}^{n} k = n(n+1)/2$, then
$$\sum_{k=1}^{n+1} k = \frac{n(n+1)}{2} + (n+1) = \frac{(n+1)(n+2)}{2}. \qquad \blacksquare$$

**What each teaches.** Derivation A **explains** the formula: the answer is half of $n$ copies of $n+1$, and you can *see* why. It also generalizes immediately to any arithmetic progression. Derivation B **certifies** the formula but explains nothing; it is the right tool when you already know the answer and need a proof, and it generalizes to sums where no pairing exists.

**What to notice.** Both are rigorous. They are not interchangeable, because they support different follow-up questions. If someone asks "what is $1+3+5+\cdots+(2n-1)$?", Derivation A's method adapts (pair the extremes) and Derivation B's does too but requires knowing the answer in advance. If someone asks "what is $\sum k^2$?", pairing fails and induction succeeds (once you guess). **Knowing which derivation to reach for is the skill; the formula itself is the least important part.**

### Demonstration 6.4 — A dependency audit that changes the meaning of a "fact"

*Claim.* The interior angles of a triangle sum to $\pi$.

*Why-chain.* Why? Because when a transversal crosses two parallel lines, alternate interior angles are equal. Why? Because of the parallel postulate. Why do we have the parallel postulate? Because it is an axiom of Euclidean geometry.

**What the audit reveals.** The claim is not a fact about triangles-in-the-abstract. It is a fact about triangles *in a geometry satisfying the parallel postulate*. Drop that axiom and the claim fails: on a sphere, a triangle with three right angles (one eighth of the sphere, with vertices at three mutually perpendicular directions) has angle sum $3\pi/2 > \pi$. In hyperbolic geometry the sum is less than $\pi$.

**What to notice.** A statement everyone "knows" turns out to be a *conditional* statement whose condition is usually invisible. This is the characteristic yield of a dependency audit: it converts a fact into a conditional, and in doing so it tells you (i) when the fact applies, (ii) what would have to change for it to fail, and (iii) where to look for a generalization. Every one of those three is a research opportunity (→ Ch. 18, 31).

## 5. Connections

- **← Ch. 1.** Bedrock is a choice of structure; first-principles reasoning makes that choice visible.
- **← Ch. 4.** A derivation is a proof whose *purpose* is understanding rather than certification.
- **→ Ch. 10.** Induction is the first-principles engine for statements indexed by $\mathbb{N}$.
- **→ Ch. 18.** Asking "which hypothesis is really needed?" is the entry point to generalization.
- **→ Ch. 22.** Asymptotic reasoning is first-principles reasoning about scale: which term dominates, and why.
- **→ Ch. 35.** Research judgment depends on knowing which parts of your field are bedrock and which are fashion.

## 6. Limitations

**Bedrock is a choice, and choices can be wrong for the problem.** Taking the parallel postulate as bedrock is right for architecture and wrong for navigation. Taking "the reals are the true numbers" is right for calculus and wrong for computation (where floating point is the actual object).

**First-principles reasoning is slow.** Rebuilding everything from scratch is a poor use of time when a trusted theorem is available and its hypotheses are clearly satisfied. The skill is knowing *when* to audit and when to use.

**Derivation is not immune to error.** A reconstruction can reproduce a textbook's mistake, or introduce a new one. Derivation must be checked like any proof — often by the methods of Ch. 4.

**Some things are not derivable from below.** You cannot derive the usefulness of a definition from more primitive notions; usefulness is judged by what the definition *does* downstream. First-principles reasoning has a direction, and it does not run backwards.

**Incompleteness.** In any sufficiently expressive formal system there are true statements not derivable within it. First-principles reasoning within a system is bounded by the system. In practice this rarely binds, but it is a real limit on the slogan "everything can be derived".

## 7. Applications

- **Debugging.** The most effective debugging is a dependency audit: what must be true for this output to be correct, and which of those can I test directly?
- **Engineering design.** "Why is this component here?" asked repeatedly, until the answer is a requirement or "nobody knows". The second answer is where the risk lives.
- **Quantitative finance.** Deriving a pricing formula from no-arbitrage shows exactly which market assumptions it needs; citing the formula does not. The difference is the difference between a risk manager and a formula user.
- **AI research.** Most architecture choices are inherited, not derived. Asking which capability each component provides, and what would break without it, is how ablation studies are designed.
- **Learning a new field.** Read the definitions, then reconstruct the two or three central theorems from them. The rest of the field is usually elaboration.

## 8. Mastery Criteria

You have this chapter when you can:

1. Produce a why-chain for a standard result down to explicitly named bedrock.
2. State every hypothesis a formula requires, including the ones usually left implicit.
3. Delete a hypothesis and determine whether the result survives, with a proof or a counterexample.
4. Give two derivations of the same fact and articulate what each one explains that the other does not.
5. Reconstruct a central theorem of a field you are learning from its definitions, without notes.
6. Identify which of your beliefs are theorems and which are axioms, and say what evidence would change each.

**Diagnostic question.** "State the quadratic formula and then tell me three situations in which it does not apply." A learner who can only recite the formula fails. A learner who names $a=0$, a non-square discriminant in the ambient field, and characteristic $2$ has done a dependency audit.

### AI Tutor Brief

- **Generate:** (i) "derive, don't cite" tasks for standard formulas; (ii) hypothesis-necessity problems: remove a hypothesis, then prove or refute; (iii) why-chain prompts that must terminate at a named axiom; (iv) pairs of derivations with a request to compare explanatory power.
- **Probe misconceptions:** treating a formula as unconditional; confusing "I have seen the proof" with "I can reconstruct it"; believing axioms are self-evident rather than chosen.
- **Transfer distance:** medium. The skill is domain-general, but it must be exercised on *unfamiliar* formulas so that recall cannot substitute for derivation.
- **Do not** accept "by the standard theorem" as a justification when the task is derivation. Conversely, do not demand derivation of arithmetic facts — calibrate to the level where derivation is informative.

---

## Part I checkpoint

Before continuing, verify the following without notes. If any item fails, return to the indicated chapter.

1. State the transfer principle and give two models of the same structure. (Ch. 1)
2. Define a concept of your own and prove it is well-defined. (Ch. 2)
3. Negate a four-quantifier statement correctly and read the negation as a construction. (Ch. 3)
4. Write a complete proof, then find its weakest step and repair it. (Ch. 4)
5. Take a theorem you know and state it at the weakest sufficient hypotheses. (Ch. 5)
6. Derive a formula you use routinely, listing every assumption. (Ch. 6)

A learner who can do all six has the foundation. A learner who can do four has gaps that will compound in Part II.

---
