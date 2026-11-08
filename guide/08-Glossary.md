# Glossary

Working definitions of every load-bearing term in the guide. Where a term has a precise technical meaning and a looser working meaning, both are given. Chapter references point to the place where the term is developed.

---

**Abstraction** — Deliberate information loss: keeping the features an argument uses and discarding the rest, so the result applies to every object sharing those features. (Ch. 5)

**Adversarial audit** — Reading your own argument as someone trying to find a gap. The four audit questions: are all cases covered, is anything assumed that was not granted, is any step non-reversible, does the conclusion say exactly what was claimed. (Ch. 4)

**Affine** — Preserved by translations and linear maps; a property that does not depend on the choice of origin. (Ch. 15)

**Auxiliary object** — An object introduced that was not in the problem (a line, a variable, a function, a sequence), justified by well-definedness, and used to make the goal reachable. (Ch. 17)

**Base rate** — The prior probability of a condition in the population, before any evidence. Dominates posterior probabilities when the condition is rare. (Ch. 21, 29)

**Bijection** — A map that is both injective and surjective; a reversible encoding. Proves equal cardinality without counting. (Ch. 12)

**Boundary hunting** — Systematically searching for the case where a claim fails: deleting hypotheses one at a time, testing degenerate and extremal cases. (Ch. 32)

**Canonical form** — A unique representative of each equivalence class, produced by a reduction that preserves the class and is idempotent. Examples: lowest terms, reduced echelon form, cycle type. (Ch. 14)

**Certificate** — A checkable object that proves optimality (or feasibility) without re-solving the problem. In linear programming, the dual solution. (Ch. 20)

**Characterization** — A theorem of the form "$P$ iff $Q$", where $Q$ is an alternative description of $P$. Distinct from a definition, and requiring two proofs. (Ch. 2)

**Combinatorial proof** — A proof of an identity by exhibiting a set that both sides count, or a bijection between two families. (Ch. 12)

**Compound strategy** — The selection and sequencing of principles to solve a problem that no single principle solves. (Ch. 24)

**Condition number** — The sensitivity of a problem's output to a relative change in its input. A property of the problem, not the algorithm. (Ch. 28)

**Conjecture** — A precisely stated, falsifiable mathematical claim believed but not proved. Must specify its domain, its sharpness claim, and what would refute it. (Ch. 31)

**Constructive existence** — An existence proof that produces the object or an algorithm for it, as opposed to a proof that the object must exist. (Ch. 4, 16)

**Contrapositive** — The statement $\neg Q \implies \neg P$, logically equivalent to $P \implies Q$. (Ch. 3)

**Converse** — The statement $Q \implies P$. Not equivalent to $P \implies Q$, and not implied by it. (Ch. 3)

**Counterexample** — A single object refuting a universal claim. The minimal counterexample, if one exists, has extra structure by well-ordering. (Ch. 32)

**Decomposition** — Partitioning a problem into parts that are exhaustive, independent, and simpler. (Ch. 14)

**Definition** — A deliberate act fixing the meaning of a term. Must be unambiguous, non-circular, and (when it names an object via a representative) well-defined. (Ch. 2)

**Degrees of freedom** — The number of independent directions in which a configuration can vary after the constraints are imposed. (Ch. 7)

**Descent** — Proving nonexistence by showing that any putative object yields a strictly smaller one, contradicting well-ordering. (Ch. 10)

**Difficulty type** — One of four causes of hardness: search, construction, impossibility, estimation. Determines the first move. (Ch. 24)

**Dimensional analysis** — The use of dimensional homogeneity to constrain the form of a physical law. (Ch. 27)

**Dominant balance** — The principle that a solution is controlled by a small number of terms that balance, and that the balance can change in thin regions. (Ch. 22)

**Double counting** — Counting one set of objects along two decompositions; the equality of the two totals is the identity to be proved. (Ch. 12)

**Duality** — A contravariant correspondence between two structures with an explicit dictionary, such that theorems translate. Weaker than isomorphism, often more useful. (Ch. 19)

**Emergence** — An aggregate property that no component has. Example: intransitive majority preferences from transitive individual preferences. (Ch. 30)

**Equivalence relation** — Reflexive, symmetric, transitive relation. Its classes partition the set; the quotient is the set of classes. (Ch. 5, 14)

**Exchange argument** — Proving optimality by showing that any configuration with a given local pattern can be improved by swapping two elements. (Ch. 16, 20)

**Extremal principle** — Proving existence or structure by choosing the object maximizing or minimizing a quantity, then using the inequality that extremality provides. (Ch. 11)

**Falsifiability** — The property of a claim that specifies what observation would refute it. The entry ticket for a conjecture. (Ch. 31)

**Fermi reasoning** — Order-of-magnitude estimation by multiplicative decomposition into independently estimable factors. (Ch. 26)

**First-principles reasoning** — Rebuilding a claim from the smallest set of assumptions one can defend, with an explicit dependency audit. (Ch. 6)

**Generalization** — Replacing a problem by a family containing it, chosen so the family has more structure. (Ch. 18)

**Hint ladder** — The five-level escalation protocol used by the tutor: restate, orient, categorize, scaffold, solution-skeleton. (Protocol §6)

**Induction** — The principle that if $P(1)$ holds and $P(n) \implies P(n+1)$, then $P(n)$ holds for all $n$; equivalent to the well-ordering of $\mathbb{N}$. (Ch. 10)

**Integrality gap** — The difference between the optimum of an integer program and that of its continuous relaxation. (Ch. 20)

**Invariant** — A quantity unchanged by every allowed move; used to prove unreachability. (Ch. 8)

**Isomorphism** — A bijection preserving all operations and relations; isomorphic structures satisfy the same theorems. (Ch. 19)

**Lemma** — A subsidiary theorem proved in order to prove a larger one. (Ch. 4)

**Model** — A mathematical structure together with an interpretation mapping its theorems to statements about a target system. The assumptions are the model. (Ch. 25)

**Monovariant** — A quantity that changes in only one direction under every allowed move; used to prove termination when bounded. (Ch. 8)

**Multiple comparisons** — Testing many hypotheses inflates the probability of at least one false positive: $1-(1-\alpha)^m$. (Ch. 29)

**Necessary and sufficient** — $Q$ is necessary for $P$ if $P \implies Q$; sufficient if $Q \implies P$. A definition or characterization needs both. (Ch. 2)

**Non-constructive existence** — An existence proof that does not produce the object. (Ch. 4)

**Pigeonhole principle** — If $n$ objects occupy $m < n$ boxes, some box has at least two. The art is choosing the boxes. (Ch. 13)

**Principle signature** — The structural feature of a problem that indicates which principle applies. (Ch. 24, and each chapter's opening)

**Probabilistic method** — Proving that an object with a property exists by showing that a random object has the property with positive probability. (Ch. 21)

**Quotient** — The set of equivalence classes of a relation, with operations that must be proved well-defined on classes. (Ch. 5)

**Reduction (in a proof)** — A transformation of a claim into an equivalent or stronger one that is easier to prove. (Ch. 10, 18)

**Regression to the mean** — The tendency of extreme measurements to be less extreme on re-measurement, when the measurement includes independent noise. (Ch. 29)

**Relaxation** — Replacing a hard problem by an easier one whose feasible set contains the original's; the easier optimum bounds the harder one. (Ch. 20)

**Rigor** — The property of an argument in which every gap is either filled or explicitly flagged. A spectrum, not a binary. (Ch. 4)

**Selection bias** — Error caused by the sample not being representative of the population, usually because the selection mechanism is correlated with the quantity of interest. (Ch. 29)

**Sharpness** — The property of a bound that is attained by some case; a non-sharp bound may be improvable. (Ch. 20, 32)

**Simpson's paradox** — A trend present in every stratum of a population but reversed in the pooled data, caused by unequal stratum sizes. (Ch. 29)

**Singular perturbation** — A perturbation in which the small parameter multiplies the highest-order term, so the reduced problem has a different structure and loses solutions. (Ch. 22)

**Stability (numerical)** — The property of an algorithm that does not amplify the errors it introduces. Distinct from the conditioning of the problem. (Ch. 28)

**Structural equivalence** — Sameness of structure, made precise by isomorphism; or a verified dictionary, in the case of duality. (Ch. 19)

**Sufficient condition** — A condition that implies the goal. Working backwards is the construction of a chain of sufficient conditions. (Ch. 17)

**Symmetry** — A transformation preserving the structure of a problem and the goal; it partitions configurations into orbits. (Ch. 9)

**Transfer distance** — How far a practice problem is from the chapter's setting: near (same domain), medium (adjacent), far (unrelated). Mastery requires far transfer. (Protocol §5.3)

**Vacuous truth** — The truth of $\forall x \in \emptyset\, P(x)$ and of $P \implies Q$ when $P$ is false. Useful for stating theorems without empty cases; dangerous when existence is assumed. (Ch. 3)

**Validity vs soundness** — An argument is valid if the conclusion follows from the premises; sound if valid and the premises are true. (Ch. 3)

**Well-definedness** — The independence of a definition from the representative or choice used to state it. (Ch. 2)

**Well-ordering** — Every nonempty set of positive integers has a least element; equivalent to induction and the basis of descent. (Ch. 10)

**WLOG ("without loss of generality")** — A restriction of the problem to a subset of configurations, legitimate only if the goal is invariant under the symmetry group and every orbit has a representative satisfying the restriction. (Ch. 9)

---
