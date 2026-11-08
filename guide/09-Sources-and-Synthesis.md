# Sources and Synthesis

This guide is an original framework. It is not a summary, an abridgement, or a reproduction of the three foundational sources. This file records what was extracted from each, how it was transformed, and what is new here — so that the provenance is auditable and the originality is explicit.

---

## 1. The three sources

| Source | Role in this project |
|---|---|
| Richard W. Hamming, *The Art of Doing Science and Engineering: Learning to Learn* | Supplies the **meta-level**: what it means to think well over a career, how to choose problems, how to reason under uncertainty, how computation and modeling fit into reasoning, and the philosophical status of mathematical structures. |
| Sandor Lehoczky and Richard Rusczyk, *The Art of Problem Solving, Volume 1: The Basics* | Supplies the **elementary technique layer**: the proof techniques, the "methods not memory" pedagogy, and the specific problem-solving moves (working backwards, auxiliary constructions, case discipline, pigeonhole, counting two ways). |
| Sandor Lehoczky and Richard Rusczyk, *The Art of Problem Solving, Volume 2: And Beyond* | Supplies the **structural technique layer**: correspondences, generating functions, recurrences, functional identities, classification methods, and the transition from technique to structure. |

No text from these books is reproduced. Where a specific idea is theirs, it is paraphrased and attributed at the level of the idea, and then **rebuilt inside this guide's own architecture** — which is where the original work lies.

---

## 2. What was extracted, and where it went

### 2.1 From Hamming

| Idea (paraphrased) | Where it appears here | How it was transformed |
|---|---|---|
| Education is *what, when, why*; training is *how*. Both are needed, and education must be built on technical experience. | README (design commitments); Ch. 35 | Turned into the guide's split between *principles* (education) and *demonstrations* (training), with the mastery criteria as the bridge. |
| Style of thinking, not content, is what a course should transmit; style is caught from examples, not from rules. | README; Ch. 24; Ch. 35 | Converted into the **signature table** and the **difficulty taxonomy** — an attempt to make "style" partly explicit and therefore trainable. |
| Back-of-the-envelope calculation: a quick model to test whether a quantitative claim is even plausible. | Ch. 26 | Systematized into a procedure (decompose → anchor → log-combine → second route → range), with the two-route agreement rule as the reliability criterion. |
| The purpose of computing is insight, not numbers. | Ch. 28 | Turned into the chapter's standard: a computation must yield a structural claim (scaling law, threshold, mechanism), not a table. |
| Knowledge doubles on a timescale shorter than a career; half of technical knowledge is obsolete in about fifteen years; therefore concentrate on fundamentals. | Ch. 6 | Turned into the **two tests for "fundamental"** (longevity, generativity) and the dependency-audit procedure. |
| Mathematics has no unique foundation; the schools (Platonic, formalist, logicist, intuitionist, constructivist) each capture something and each fails; meaning arises from use, not from definition. | Ch. 1; Ch. 2 | Turned into the operational stance: *truth is relative to a structure*, and identifying the structure is a required step in any argument. |
| Standards of rigor rise over time; proofs are more or less convincing rather than certainly convincing. | Ch. 4 | Turned into **rigor as a spectrum** (every gap filled or flagged) and the four audit questions. |
| The creative process: recognize, refine, saturate, abandon temporarily, insight, clean up. "If I had a solution, what would it look like?" | Ch. 7; Ch. 17; Ch. 35 | Turned into the **form question** and the **backward chain**, with the incubation step preserved in the stuckness protocol. |
| Analogy is the main tool of creativity, and a useful analogy need not be close — it need only suggest the next move. | Ch. 18; Ch. 19; Ch. 23 | Turned into the distinction between **analogy (unverified), duality (verified dictionary), and isomorphism (exact)**, with the verification requirement made explicit. |
| Impossibility proofs rest on assumptions; experts dismiss what does not fit their frame. | Ch. 32 | Turned into **boundary hunting**: delete each hypothesis and find the counterexample. |
| The whole is more than the sum of the parts; feedback and stability are the central issues in systems. | Ch. 30 | Turned into the four properties (feedback, emergence, nonlinearity, interfaces) and the interface audit. |
| Work on important problems; confidence and courage are prerequisites; consistent direction compounds while random effort does not. | Ch. 35 | Turned into the **important-problem table** (why / known / obstruction / progress) and the quantified compounding argument. |
| Data are unreliable in ways that are systematic, not random. | Ch. 29 | Turned into the taxonomy: noise, bias, selection, aggregation, regression to the mean, multiple comparisons. |

**What was deliberately not taken from Hamming:** the historical and technical chapters (hardware, software, coding theory, filters, fiber optics, quantum mechanics) supply illustrations but not the guide's structure. The guide borrows the *stance* — reasoning about reasoning, with technical material as evidence — not the content.

### 2.2 From *The Art of Problem Solving, Volume 1*

| Idea (paraphrased) | Where it appears here | How it was transformed |
|---|---|---|
| The book teaches approaches, not facts; formulas should become obvious rather than memorized; the exercises are the point. | README; Ch. 6 | Turned into the **derivation requirement** in every demonstration, and the rule that the guide contains no problem sets (the tutor supplies practice). |
| Subjects should be learned together, because the connections are the point. | Ch. 23 | Turned into the **multiple-lenses** chapter and the translation table. |
| Proof techniques: contradiction, induction, pigeonhole; converses are not automatic; "iff" needs two directions. | Ch. 3; Ch. 4; Ch. 10; Ch. 13 | Reorganized by **goal shape** rather than by technique name, producing the four-engine table. |
| Rigorous means complete, with no unproven assumptions; circular reasoning is easy to hide. | Ch. 4 | Turned into the **asset-list discipline** and the circularity audit (including the algebraic variety). |
| Think about what is special about every restriction in the problem. | Ch. 7 | Turned into the **generic vs special constraint** distinction and the "unused hypothesis is a signal" rule. |
| Working backwards; adding auxiliary lines; the auxiliary line is chosen to create similar triangles or equal angles. | Ch. 17 | Turned into the **backward chain** with the auxiliary object *forced* by the chain, rather than guessed. |
| Always check that the proof covers all cases and makes no assumptions that are not part of the problem. | Ch. 4; Ch. 14; Ch. 32 | Turned into the **exhaustiveness obligation** and the boundary table. |
| Convincing but wrong: a wrong step hidden among correct ones; patterns are not proofs. | Ch. 4; Ch. 31 | Turned into the **planted-defect** problem type and the mechanism requirement for conjectures. |
| Counting two ways; counting the wrong thing; doing it another way. | Ch. 12 | Turned into the **relation-selection** method (choose the set of pairs) and the multiplicity discipline. |
| Aesthetics matter; a proof can explain as well as certify; multiple proofs of the same theorem are valuable. | Ch. 4; Ch. 23 | Turned into the **explanation vs certification** distinction and the "two lenses" requirement. |

### 2.3 From *The Art of Problem Solving, Volume 2*

| Idea (paraphrased) | Where it appears here | How it was transformed |
|---|---|---|
| Proofs are essential to understanding: if you do not know why a tool works, you cannot use it fully. | Ch. 4; Ch. 6 | Turned into the rule that every demonstration is a complete argument and every formula is derived. |
| Clever correspondences; counting by finding the right representation. | Ch. 12; Ch. 19 | Turned into the **bijection-as-isomorphism** view and the "find the set both sides count" procedure. |
| Generating functions turn recurrences into algebra. | Ch. 15 | Turned into the four-step transform-solve-return-verify procedure, with verification made mandatory. |
| Functional identities: isolate, substitute values, use cyclic structure. | Ch. 15; Ch. 18 | Absorbed into **transformation** (substitution and parameterization) rather than kept as a separate topic. |
| Recurrences, continued fractions, repeated structures. | Ch. 10; Ch. 15; Ch. 22 | Turned into the **recursion ↔ induction duality** and the asymptotics of recursively defined sequences. |
| Classification methods: cycle decomposition, canonical forms, invariants. | Ch. 14; Ch. 19 | Turned into the **canonical form → classification** procedure with the uniqueness obligation made explicit. |
| General methods for Diophantine equations (factorization, modular obstruction, descent, Pell). | Ch. 24 (Demonstration 24.1); Ch. 32 | Turned into the **macro** concept: a named sequence of principles that recurs as a unit. |
| Geometric transformations: projection, inversion, homothety, continuity arguments. | Ch. 15; Ch. 19 | Turned into the **transformation table** and the "reversibility must be tracked" rule. |
| Graph theory: planarity, Euler trails, colorings, the Platonic solids. | Ch. 8; Ch. 19; Ch. 30 | Used as demonstration material for invariants, duality, and systems rather than as a subject chapter. |

---

## 3. What is original to this guide

The sources supply ideas. The following are constructed here and are not in the sources:

1. **The eight-part chapter template** (Core Idea, First Principles, Reasoning Process, Demonstrations, Connections, Limitations, Applications, Mastery Criteria) and the failure mode each section is designed to prevent.

2. **The principle taxonomy and dependency graph.** The sources organize by subject (AoPS) or by lecture topic (Hamming). This guide organizes by *principle*, with an explicit DAG, hard and soft prerequisites, and a repair plan keyed to weakness codes.

3. **The difficulty taxonomy** (search / construction / impossibility / estimation) and the **signature table** that maps a problem's surface to a candidate principle. This is the guide's answer to "how do I know which technique to use?", which neither source addresses systematically.

4. **The boundary-table method** (Ch. 32, Demonstration 32.4): for each hypothesis of a theorem, delete it, produce a counterexample, and name what the hypothesis prevents. This is a specific, reusable instrument.

5. **The mastery-level scale (0–4) with behavioral descriptors**, and the certification protocol (five conditions, spaced review, downgrade rule).

6. **The transfer-distance framework** (near / medium / far) and the rule that mastery requires three consecutive far-transfer successes. This makes "understanding" measurable in a way that neither source attempts.

7. **The weakness-code taxonomy** (26 codes with symptom, root cause, and remediation), which turns diagnosis into a cumulative, queryable record.

8. **The hint ladder** (five levels, escalation rules, one level per exchange) and the **anti-dependency protocol** (effort gates, solution withholding, explain-back, fading).

9. **The compound-strategy macros** (Ch. 24): named sequences of principles that recur, such as "pick a modulus → enumerate residues → show divisibility → descend".

10. **The applied reasoning chapters** (modeling, estimation, scaling, computation, uncertainty, systems) treated as *reasoning principles* rather than as applications of mathematics. Hamming gestures at this; the guide makes it a structural part of the curriculum.

11. **The research chapters** (conjecture, counterexample, experiment, invention, judgment) as trainable practices with protocols, rather than as advice.

12. **The AI tutor protocol** in its entirety: the role definition, the learner-model schema, the diagnostic stages, the problem-generation specification, the evaluation rubric, and the guardrails.

---

## 4. Verification notes

Mathematical claims in the demonstrations were checked by computation or by direct argument. Where a demonstration is a classical theorem, the proof given is a standard one, presented in this guide's voice and connected to the chapter's principle. The following were verified numerically during preparation:

- The Moser circle-problem counts $1,2,4,8,16,31$ and the formula $\binom{n}{4}+\binom{n}{2}+1$.
- The line-arrangement count $n(n+1)/2+1$ for $n = 0,\dots,5$.
- The $6\times6$ board's complex weight $(1+i)^2 = 2i \ne 0$ under fourth-root-of-unity weighting.
- The Sylvester–Gallai minimal-distance inequality $h(c-b)/\sqrt{h^2+c^2} < h$ for $0<b<c$.
- The Braess network equilibria ($65$ minutes without the link, $80$ with it).
- The Simpson's-paradox table ($90\%$ vs $88.9\%$, $22.2\%$ vs $20\%$, overall $29\%$ vs $82\%$).
- The logistic-map stability condition $|2-r|<1$ and the $r=3.2$ two-cycle ($\approx 0.513$, $\approx 0.799$).
- The $100!$ digit count ($158$) via Stirling.
- The atmospheric mass estimate ($5.3\times10^{18}$ kg vs the accepted $5.15\times10^{18}$ kg).
- The M/M/1 waiting times $\rho/(1-\rho)$ at $\rho = 0.5, 0.8, 0.9, 0.95, 0.99$.
- The two-square identity and its complex-modulus proof.
- The reciprocal-quartic substitution and the absence of real roots.
- Binet's formula from both the generating function and the matrix diagonalization.
- The weighted AM–GM induction step.
- The Erdős–Szekeres distinct-labels argument.
- The Dirichlet approximation pigeonhole bound.

Any error that survives is the author's, and should be reported as a defect of this guide, not of the sources.

---

## 5. How to extend this guide

The architecture is designed to accept new chapters without restructuring. To add a principle:

1. **Place it in the DAG.** Identify its hard prerequisites and the chapters that would draw on it. Update `07-Principle-Map.md`.
2. **Write the eight sections.** The *Limitations* section is the one that determines whether the chapter is worth having: a principle whose failure modes you cannot state is a principle you do not understand.
3. **Write the AI Tutor Brief.** Specify the target subskill, the common failure modes, and the transfer distance.
4. **Add a weakness code** if the principle has a characteristic error not covered by the existing 26.
5. **Add a checkpoint item.** A principle that is not assessed will not be learned.
6. **Add it to the signature table** in Ch. 24, with its decoys.

The guide's value is in the connections, not the count. A new chapter that does not connect to at least three existing ones should probably be a section instead.

---
