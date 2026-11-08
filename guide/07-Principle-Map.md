# Principle Map: Dependencies, Cross-References, and Sequencing

This file is the structural index of the guide. Use it for three purposes:

1. **Sequencing** — what must be learned before what.
2. **Diagnosis** — when a learner fails at chapter $N$, which prerequisite is the likely cause.
3. **Tutor configuration** — which principles are available as targets, and which combinations are legal.

---

## 1. Dependency graph

An arrow $A \to B$ means *B assumes A*. The graph is a DAG; there are no cycles.

```
                         ┌──────────────────────────────┐
                         │ 1  Mathematics as Structure  │
                         └──────────────┬───────────────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    ▼                   ▼                   ▼
            ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
            │ 2 Definition  │   │  3  Logic     │   │ 5 Abstraction │
            └───────┬───────┘   └───────┬───────┘   └───────┬───────┘
                    │                   │                   │
                    └───────────┬───────┴───────────┬───────┘
                                ▼                   ▼
                        ┌───────────────┐   ┌───────────────┐
                        │  4  Proof     │   │6 First Princ. │
                        └───────┬───────┘   └───────┬───────┘
                                │                   │
        ┌───────────────────────┴───────────────────┘
        ▼
┌───────────────────────────────────────────────────────────────────┐
│                    PART II  (7 – 17)                              │
│                                                                   │
│  7 Anatomy ──┬──► 8 Invariants ──┬──► 16 Constructive             │
│              ├──► 9 Symmetry     │                                │
│              ├──► 10 Induction ──┼──► 14 Decomposition            │
│              ├──► 11 Extremal ───┘        │                       │
│              ├──► 12 Counting ────────────┤                       │
│              ├──► 13 Pigeonhole           │                       │
│              ├──► 15 Transformation ◄─────┘                       │
│              └──► 17 Backwards                                    │
│                                                                   │
│  (8,9,10,11,12,13,14,15,16,17 are mutually independent               │
│   but are combined constantly; 7 is the prerequisite for all.)     │
└───────────────────────────────┬───────────────────────────────────┘
                                ▼
┌───────────────────────────────────────────────────────────────────┐
│                    PART III  (18 – 24)                            │
│                                                                   │
│  18 Generalization ◄── (5, 6, 10, 17)                             │
│  19 Isomorphism    ◄── (1, 5, 14)                                 │
│  20 Optimization   ◄── (6, 11, 16)                                │
│  21 Probability    ◄── (12, 13)                                   │
│  22 Asymptotics    ◄── (10, 15)                                   │
│  23 Multi-Lens     ◄── (15, 19)                                   │
│  24 Compound       ◄── (7 – 23)   ← synthesis checkpoint           │
└───────────────────────────────┬───────────────────────────────────┘
                                ▼
┌───────────────────────────────────────────────────────────────────┐
│                    PART IV  (25 – 30)                             │
│                                                                   │
│  25 Modeling     ◄── (1, 6, 18)                                   │
│  26 Estimation   ◄── (22)                                         │
│  27 Scaling      ◄── (18, 26)                                     │
│  28 Computation  ◄── (22, 25)                                     │
│  29 Uncertainty  ◄── (21, 25)                                     │
│  30 Systems      ◄── (8, 11, 19, 25)                              │
└───────────────────────────────┬───────────────────────────────────┘
                                ▼
┌───────────────────────────────────────────────────────────────────┐
│                    PART V  (31 – 35)                              │
│                                                                   │
│  31 Conjecture   ◄── (7, 18, 22)                                  │
│  32 Counterex.   ◄── (4, 10, 18, 20)                              │
│  33 Experiment   ◄── (12, 22, 28)                                 │
│  34 Invention    ◄── (7, 18, 19, 31)                              │
│  35 Judgment     ◄── (24, 31 – 34)                                │
└───────────────────────────────────────────────────────────────────┘
```

### Hard prerequisites

| Chapter | Cannot be studied without |
|---|---|
| 4 | 2, 3 |
| 7 | 3, 4 |
| 8–17 | 7 |
| 20 | 6, 11 |
| 22 | 10 |
| 24 | 8–23 (all) |
| 25 | 1, 6 |
| 28 | 22 |
| 29 | 21 |
| 31 | 7, 18 |
| 32 | 4, 10 |
| 35 | 31–34 |

### Soft prerequisites (helpful, not required)

| Chapter | Benefits from |
|---|---|
| 9 | 8 (invariance is the discrete form of symmetry) |
| 12 | 10 (recursive counting) |
| 14 | 2 (canonical forms need well-definedness) |
| 19 | 14 (classification needs canonical forms) |
| 23 | 15, 19 |
| 27 | 18 (scaling is generalization in the size parameter) |
| 30 | 8, 11 |
| 33 | 12, 28 |

---

## 2. Cross-reference matrix

Rows: the chapter you are reading. Columns: chapters it draws on most heavily.

| Ch | Draws on | Is drawn on by |
|---|---|---|
| 1 | — | 5, 19, 25 |
| 2 | 1 | 4, 5, 14 |
| 3 | 2 | 4, 11, 21, 29 |
| 4 | 2, 3 | 8, 10, 11, 32, 35 |
| 5 | 1, 2 | 18, 19, 25 |
| 6 | 1, 4 | 18, 20, 25 |
| 7 | 3, 4 | 8–17, 25, 31, 34 |
| 8 | 4, 7 | 9, 10, 16, 27, 30 |
| 9 | 8, 13 | 11, 19, 20, 27 |
| 10 | 4, 8 | 12, 14, 22, 32 |
| 11 | 3, 8, 9 | 20, 32 |
| 12 | 10 | 13, 15, 21, 33 |
| 13 | 9, 12 | 11, 21, 31 |
| 14 | 2, 5, 10 | 19, 32 |
| 15 | 3, 12 | 19, 22, 23 |
| 16 | 8, 10, 11 | 20, 22, 28 |
| 17 | 4, 7, 11 | 18, 20, 34 |
| 18 | 5, 6, 10, 17 | 19, 27, 31, 32 |
| 19 | 1, 5, 14 | 20, 23, 30 |
| 20 | 6, 11, 16 | 21, 26, 32 |
| 21 | 12, 13 | 22, 25, 29 |
| 22 | 10, 15 | 25, 26, 27, 28 |
| 23 | 15, 19 | 34, 35 |
| 24 | 7–23 | 35 |
| 25 | 1, 6, 18 | 26, 27, 28, 29, 30 |
| 26 | 22 | 27, 28 |
| 27 | 18, 26 | 28, 30 |
| 28 | 22, 25 | 29, 33 |
| 29 | 21, 25 | 31, 35 |
| 30 | 8, 11, 19, 25 | 35 |
| 31 | 7, 18, 22 | 32, 33, 34, 35 |
| 32 | 4, 10, 18, 20 | 31, 33, 35 |
| 33 | 12, 22, 28 | 31, 34 |
| 34 | 7, 18, 19, 31 | 35 |
| 35 | 24, 31–34 | — |

---

## 3. Target-principle index (for the tutor)

The tutor may generate problems for any principle in this table. "Signature" is the phrase that should appear in the problem's *reasoning*, not in its statement.

| Ch | Principle | Signature the problem should have | Common decoys |
|---|---|---|---|
| 1 | Structure | Same relations in a different domain | Topic-label thinking |
| 2 | Definition | A supplied definition must be used; a clause is missing | Appeal to prior knowledge |
| 3 | Logic | Quantifier order matters; negation is the key | Prose reading |
| 4 | Proof | One engine is much shorter; a gap must be found | "It's obvious" |
| 5 | Abstraction | A hypothesis can be deleted; a quotient is needed | Over-abstraction |
| 6 | First principles | A standard formula must be derived or its scope found | Recall |
| 7 | Anatomy | Goal type is ambiguous; a hypothesis is superfluous | Immediate computation |
| 8 | Invariant | Reachability or termination question | Direct construction |
| 9 | Symmetry | Data can be relabeled; a WLOG is available or invalid | "By symmetry" |
| 10 | Induction | A discrete parameter with recursive structure | Direct proof |
| 11 | Extremal | Existence of an object with a property | Random construction |
| 12 | Counting | An identity or a count | Algebraic expansion |
| 13 | Pigeonhole | More objects than slots | Structural argument |
| 14 | Decomposition | Classification; cases; canonical form | Ad hoc casework |
| 15 | Transformation | The current representation resists | Pushing harder |
| 16 | Constructive | "Find" or "describe an algorithm" | Existence only |
| 17 | Backwards | Goal is a relation; auxiliary object needed | Forward search |
| 18 | Generalization | An arbitrary constant; a failing induction | Special-case proof |
| 19 | Isomorphism | Two structures that are the same | Analogy |
| 20 | Optimization | Bound plus attainment; a certificate | Bound only |
| 21 | Probability | Existence via expectation; base rate | Direct construction |
| 22 | Asymptotics | Large/small parameter; growth comparison | Exact computation |
| 23 | Multi-lens | Easy statement, hard in its current branch | One-lens persistence |
| 24 | Compound | Requires three or more principles | Single-technique |
| 25 | Modeling | Real system, noisy data, a decision | Fitting |
| 26 | Estimation | No data; implausible claim | Precision |
| 27 | Scaling | Variables with dimensions; scale-up question | Curve fitting |
| 28 | Computation | Error, stability, verification | "The computer says" |
| 29 | Uncertainty | Selection, aggregation, base rates | Naive statistics |
| 30 | Systems | Feedback, thresholds, interfaces | Sum-of-parts |
| 31 | Conjecture | Data with a pattern; a vague claim | Pattern = proof |
| 32 | Counterexample | A universal claim; a boundary | Verification bias |
| 33 | Experiment | A computable family; a transform needed | Brute force |
| 34 | Invention | A result to be transformed | Relabeling |
| 35 | Judgment | A choice under uncertainty | Effort as proxy |

---

## 4. Legal combinations

Combination problems are the main instrument for levels 3–4. The following pairs are natural, well-tested, and produce clean chains:

| Combination | Chain shape | Example problem type |
|---|---|---|
| 8 + 14 | Invariant, then case split to prove completeness | Reachability with a weighted invariant |
| 8 + 10 | Monovariant as descent | Termination of a process |
| 9 + 13 | Symmetry reduces cases, pigeonhole produces the object | Ramsey-type |
| 10 + 11 | Induction with an extremal choice in the step | Existence for all $n$ |
| 11 + 12 | Extremal object counted two ways | Double counting at an extremum |
| 12 + 15 | Bijection, then generating function | Counting with a recurrence |
| 14 + 15 | Canonical form as a change of representation | Classification |
| 15 + 18 | Substitution that exposes a parameter | Generalizing a solved case |
| 16 + 20 | Algorithm plus exchange certificate | Greedy optimality |
| 18 + 20 | Generalize to get a bound, specialize to attain | Sharp inequality |
| 19 + 23 | Isomorphism across branches | Same theorem, two lenses |
| 21 + 22 | First moment plus asymptotics | Existence at large $n$ |
| 22 + 27 | Scaling exponent from dimensions, corrections from asymptotics | Physical law |
| 25 + 29 | Model plus selection diagnosis | Confounded data |
| 28 + 33 | Computation plus experiment design | Conjecture from simulation |
| 31 + 32 | Conjecture plus boundary hunt | Falsification |
| 32 + 34 | Counterexample plus inversion | Repairing a theorem |
| 33 + 34 | Experiment plus variant generation | Research lab |

**Illegal or unproductive combinations** (the tutor should avoid these):

- 26 + 27 on a problem with no physical dimensions (scaling is vacuous).
- 30 on a single-agent optimization problem (no feedback, no emergence).
- 35 as a *problem* target: judgment is assessed through scenarios, not solved problems.

---

## 5. Sequencing plans

### Plan A — Olympiad (12 months, ~8 h/week)

| Months | Content | Emphasis |
|---|---|---|
| 1 | Ch. 1–6 | Definitions, quantifiers, proof audit |
| 2–3 | Ch. 7–10 | Anatomy, invariants, symmetry, induction |
| 4–5 | Ch. 11–14 | Extremal, counting, pigeonhole, decomposition |
| 6–7 | Ch. 15–17 | Transformation, construction, backwards |
| 8 | Ch. 24 (checkpoint) + review | Strategy under time pressure |
| 9–10 | Ch. 18–20, 23 | Generalization, structure, optimization |
| 11 | Ch. 31–33 | Conjecture, counterexample, experiment |
| 12 | Full review + mock contests | Transfer under pressure |

### Plan B — AI research / quantitative (12 months)

| Months | Content | Emphasis |
|---|---|---|
| 1 | Ch. 1–4 | Rigor and quantifiers |
| 2 | Ch. 5–7 | Abstraction, first principles, anatomy |
| 3–4 | Ch. 8, 10, 12, 15 | Invariants, induction, counting, transforms |
| 5–6 | Ch. 20–22 | Optimization, probability, asymptotics |
| 7–8 | Ch. 25–28 | Modeling, estimation, scaling, computation |
| 9 | Ch. 29–30 | Uncertainty, systems |
| 10–11 | Ch. 18–19, 23 | Generalization, structure, lenses |
| 12 | Ch. 31, 33, 35 | Conjecture, experiment, judgment |

### Plan C — Repair plan (for a learner with gaps)

When the diagnostic shows weakness codes concentrated in the foundations, do **not** proceed to Part II. Instead:

| Weakness code | Repair sequence |
|---|---|
| W-DEF, W-QORDER, W-CONV | Ch. 2 → 3 → 4, with audit drills only |
| W-CASE-EXH, W-CIRC | Ch. 4 → 14 → 32 |
| W-INV-FIND, W-INV-PRESERVE | Ch. 8 → 10 → 16 |
| W-BOUND-ONLY, W-EXIST | Ch. 11 → 20 |
| W-MEAN-TYPICAL, W-SELECTION | Ch. 21 → 29 |
| W-PATTERN, W-ASYMPTOTIC | Ch. 22 → 31 → 33 |
| W-ABANDON, W-GREEDY | Ch. 24 → 16 |

The repair plan is usually 4–6 weeks. It is the highest-yield investment in the entire curriculum, because these codes compound.

---

## 6. Assessment checkpoints

| Checkpoint | After | Tests | Pass criterion |
|---|---|---|---|
| CP-0 | Diagnostic | All | Baseline recorded |
| CP-1 | Ch. 6 | 2, 3, 4, 6 | Level 2 on 3 of 4 |
| CP-2 | Ch. 11 | 7–11 | Level 2 on 4 of 5; one unaided |
| CP-3 | Ch. 17 | 12–17 | Level 3 on 3 of 6; one combination |
| CP-4 | Ch. 24 | 18–24 | Level 3 on 3 of 7; two combinations |
| CP-5 | Ch. 30 | 25–30 | Level 3 on 3 of 6; one applied transfer |
| CP-6 | Ch. 35 | 31–35 | Level 3 on 3 of 5; one original problem invented |

**Failure at a checkpoint** means returning to the weakest chapter in that block, not repeating the whole block.

---

## 7. How to read a failure

When a learner fails at chapter $N$, the cause is usually upstream. Use this table.

| Symptom at chapter $N$ | Likely upstream cause |
|---|---|
| Cannot start | Ch. 7 (anatomy) or Ch. 3 (goal not parsed) |
| Starts, but the approach is irrelevant | Ch. 7 (goal type), Ch. 24 (signature selection) |
| Right principle, wrong execution | Ch. 2 (definition unpacking) or Ch. 6 (derivation) |
| Right execution, missing case | Ch. 14 (exhaustiveness) or Ch. 4 (audit) |
| Right proof, wrong conclusion | Ch. 3 (quantifiers) or Ch. 7 (goal statement) |
| Cannot verify the answer | Ch. 3 (reversibility) or Ch. 4 (audit) |
| Understands the chapter, cannot use it | Ch. 5 (structure) or Ch. 18 (generality) |
| Can use it in the chapter, not outside | Insufficient far-transfer practice — the tutor's fault, not the learner's |

The last row is important. **Transfer failure is usually a curriculum failure**: the learner practiced near-transfer only. The remedy is more far-transfer problems, not more reading.

---
