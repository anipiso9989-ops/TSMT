# Part II — Problem-Solving Principles

> *Part I taught you what a mathematical claim is. Part II teaches you eleven moves that solve almost everything solvable at the olympiad and undergraduate level — and that recur, disguised, in research and engineering.*

**Chapters in this part**

7. Problem Anatomy: State, Goal, Constraint, Freedom
8. Invariants and Monovariants
9. Symmetry and "Without Loss of Generality"
10. Induction, Recursion, and Well-Ordering
11. The Extremal Principle
12. Counting Two Ways: Bijection and Double Counting
13. Pigeonhole and Density Arguments
14. Decomposition and Canonical Form
15. Transformation: Changing the Representation
16. Constructive Reasoning and the Algorithmic Stance
17. Working Backwards and Auxiliary Objects

**How this part is meant to be used**

These chapters are *independent of each other* but *mutually reinforcing*. Do not read them in one pass. Read one, then spend a week solving problems that require it, then read the next. Chapter 24 tests whether you can choose among them under pressure, which is the actual skill.

Every chapter in this part ends with a **principle signature**: the situation in which the principle announces itself. Learn the signatures, not the names.

---

# Chapter 7 — Problem Anatomy: State, Goal, Constraint, Freedom

## 1. Core Idea

Every well-posed problem has four parts:

- **State** — what is given, and what may vary.
- **Goal** — what must be produced or established, and in what logical form.
- **Constraints** — the conditions the answer must satisfy.
- **Freedom** — the degrees of freedom left over after the constraints are imposed.

Most failures on hard problems are not failures of technique. They are failures of **anatomy**: the solver never determined what kind of object the answer is, never counted the degrees of freedom, and therefore never noticed which constraint was the load-bearing one.

The most valuable single question in problem solving is not "what formula applies?" but:

> **If I had the answer, what would it look like?**

Hamming's version of this question — *"If I had a solution, what would it look like?"* — is the most reliable way to convert a vague sense of being stuck into a concrete plan. Answering it forces you to specify the *form* of the answer, and the form usually dictates the method.

## 2. First Principles

**Problems are constraint systems.** A problem gives you $k$ unknowns and $c$ independent constraints. Three regimes:

| Regime | Meaning | What to expect |
|---|---|---|
| $c > k$ | Over-determined | Either no solution, or the constraints are dependent and one is redundant. Redundancy is a *gift*: it means a stronger conclusion is available. |
| $c = k$ | Determined | Finitely many solutions (generically). Expect a unique answer or a small finite set. |
| $c < k$ | Under-determined | Infinitely many solutions. The goal must be **invariant** over the free directions, or the problem is ill-posed. |

This count is not rigorous — constraints can be dependent, and integrality can behave like infinitely many constraints — but it is an extremely reliable first diagnostic. An under-determined problem that asks for a specific number is telling you that a hidden invariant exists (→ Ch. 8). An over-determined problem that seems to need all constraints is telling you that one constraint is stronger than it looks.

**Every constraint must be used.** If your solution never uses a hypothesis, either (a) the hypothesis is redundant and the result is stronger than stated, or (b) your solution is wrong. Both are worth knowing. In olympiad problems, unused hypotheses are almost always a sign of an incomplete solution.

**The goal's logical form determines the method.** "Find all $x$" requires a classification (and a proof of exhaustiveness). "Prove there exists" requires a construction or an existence argument. "Prove for all" requires a universal argument. "Find the maximum" requires a bound *and* an attainment (→ Ch. 20). "Determine whether" requires a decision plus justification of both branches.

**Specialness is a signal.** The constraints that look unusual — an odd prime, a condition at a single point, an equality that holds only in one case — are where the problem's mechanism lives. A generic constraint is usually there to make the problem well-posed; a special one is usually there to be exploited.

## 3. Reasoning Process

1. **Restate.** Write the problem in your own words, in one sentence, without looking. If you cannot, you do not understand it yet.
2. **Classify the goal.** Which of: prove / disprove / find all / construct / compute / optimize / classify / decide?
3. **List the constraints** and mark each as *generic* (needed for well-posedness) or *special* (likely load-bearing).
4. **Count.** How many unknowns? How many constraints? Which regime are you in?
5. **Ask the form question.** "If I had the answer, what would it look like?" Write down the expected *shape*: a number, a family, a construction, a residue class, a ratio, an algorithm.
6. **Ask the bridge question.** "What single fact would make the goal immediate?" That fact is your target lemma (→ Ch. 17).
7. **Choose a principle.** Match the problem's shape to a signature from Chapters 8–17.
8. **Plan a check.** Before solving, decide how you will verify the answer: a small case, a limiting case, a symmetry, a magnitude estimate.

## 4. Demonstrations

### Demonstration 7.1 — Anatomy of a Diophantine problem

*Problem.* Find all integers $n \ge 0$ such that $n^2+n+1$ is a perfect square.

**Anatomy.**

- *Goal type:* find all — a classification, requiring both a candidate list and a proof of exhaustiveness.
- *Unknowns:* two ($n$ and the square root $m$). *Constraints:* one equation, plus integrality, plus $n\ge0$, plus $m\ge1$.
- *Regime:* nominally under-determined ($2$ unknowns, $1$ equation), so the *real* constraints are integrality and positivity. This is the key structural observation: **the equation has infinitely many real solutions, and it is the arithmetic constraints that will pin it down.**

**Solution.** Suppose $n^2+n+1 = m^2$ with $m \ge 1$. Multiply by $4$:

$$4n^2+4n+4 = 4m^2 \implies (2n+1)^2 + 3 = (2m)^2 \implies (2m)^2 - (2n+1)^2 = 3.$$

Difference of squares:

$$(2m - 2n - 1)(2m + 2n + 1) = 3.$$

Both factors are integers. Since $n \ge 0$ and $m \ge 1$, we have $2m+2n+1 \ge 3 > 0$, so $2m-2n-1 > 0$ as well. The only factorizations of $3$ into positive integers are $1\cdot3$ and $3\cdot1$.

- $2m-2n-1 = 1$ and $2m+2n+1 = 3$: adding gives $4m = 4$, so $m=1$; then $2n+1 = 3-2 = 1$, so $n = 0$.
- $2m+2n+1 = 1$ is impossible since $2m+2n+1 \ge 3$.

Hence $n = 0$ is the only solution, and indeed $0+0+1 = 1^2$. $\blacksquare$

**What to notice.** The decisive move was not a trick; it was the anatomical observation that the *integrality* constraints, not the equation, do the work. Once you expect a factorization into a bounded number of divisors, the multiplication by $4$ and the difference of squares become obvious rather than magical. **Anatomy predicts method.**

### Demonstration 7.2 — Recognizing an under-determined problem

*Problem.* A rectangle has perimeter $20$. Find its area.

**Anatomy.** Unknowns: width $w$, height $h$. Constraints: $2(w+h) = 20$, i.e. $w+h=10$. That is one constraint for two unknowns: under-determined. The goal (area $wh$) is *not* invariant along the free direction ($w$ can be anything in $(0,10)$), so the problem has no unique answer.

**Diagnosis.** The problem is ill-posed as stated. The correct responses are: (a) report the family $A = w(10-w)$ for $w \in (0,10)$; (b) ask for the range, $0 < A \le 25$; (c) ask for the maximum, which is $25$ at $w=h=5$.

**What to notice.** An under-determined problem is not a dead end — it is a *diagnosis*. The freedom is the interesting object. Once you see that $A = w(10-w)$, the optimization question answers itself, and so does the range question. The failure mode to avoid is inventing a constraint ("assume it's a square") without noticing you have done so; that produces an answer to a different problem.

**General rule.** When the goal is not invariant under the available freedom, either the problem is ill-posed or you have missed a constraint. Find out which.

### Demonstration 7.3 — The form of the answer dictates the method

*Problem.* Prove that every integer $n \ge 8$ can be written as $n = 3a + 5b$ with integers $a,b \ge 0$.

**Anatomy.** Goal type: universal existence, $\forall n \ge 8\ \exists a,b$. The answer is not a number but a *procedure* that, given $n$, produces $(a,b)$. So the question becomes: what form should that procedure take?

The natural form: since $3$ and $5$ are coprime, the values of $5b$ cycle through all residues mod $3$ as $b$ runs $0,1,2$. So a procedure that chooses $b \in \{0,1,2\}$ to fix the residue of $n$ mod $3$, then takes $a = (n-5b)/3$, will work — provided $a \ge 0$, which requires $n \ge 5b$.

**Solution.** Write $n = 3q + r$ with $r \in \{0,1,2\}$.

- If $r = 0$: $n = 3q$, so $(a,b) = (q, 0)$.
- If $r = 1$: $n = 3q+1 = 3(q-3) + 10$, so $(a,b) = (q-3, 2)$; here $a = q-3 \ge 0$ requires $q \ge 3$, i.e. $n \ge 10$.
- If $r = 2$: $n = 3q+2 = 3(q-1)+5$, so $(a,b) = (q-1,1)$; here $a \ge 0$ requires $q \ge 1$, i.e. $n \ge 5$.

So the construction works for all $n \ge 10$, and for $n \in \{8,9\}$ we check directly: $8 = 3+5$, $9 = 3\cdot3$. Hence every $n\ge8$ works. $\blacksquare$

**What to notice.** Three things.

1. The *form* of the answer — "choose $b$ by residue, then solve for $a$" — was derived from anatomy before any algebra. Without it, one flails.
2. The residue-class split is a **decomposition** (→ Ch. 14) driven by the moduli, and the finite check of $\{8,9\}$ is a **base case** (→ Ch. 10). Principles chain.
3. The bound $n \ge 8$ is *sharp*: $7$ is not representable ($7 = 3a+5b$ forces $b=0$ or $1$; $b=0 \Rightarrow 3\nmid 7$; $b=1\Rightarrow 3a=2$). Sharpness is part of understanding a theorem (→ Ch. 32).

## 5. Connections

- **← Ch. 2, 3.** You cannot classify a goal type or count constraints without precise definitions and correct quantifiers.
- **→ Ch. 8.** Under-determination signals a hidden invariant.
- **→ Ch. 11, 20.** "Find the maximum" is a compound goal: bound plus attainment.
- **→ Ch. 14.** The residue split in Demonstration 7.3 is a decomposition; anatomy tells you to look for one.
- **→ Ch. 17.** The "bridge question" in step 6 is the entry point to working backwards.
- **→ Ch. 25.** In applied problems, the anatomy step is the modeling step: deciding what the state, goal, and constraints *are* is most of the work.

## 6. Limitations

**Counting constraints is a heuristic, not a theorem.** Constraints can be dependent (so $c>k$ may still be consistent) or integrality can act like infinitely many constraints (so $c<k$ may still have finitely many solutions). Use the count to orient, not to conclude.

**Some problems have no clean anatomy.** Research problems often have goals that are not yet well-defined; discovering the right question is part of the work (→ Ch. 34). Anatomy is for problems that are already posed.

**Anatomy can become procrastination.** Listing constraints forever is not solving. Set a time limit: ten minutes of anatomy, then commit to an approach. You can return to anatomy when the approach dies.

**The "form of the answer" can be wrong.** You may predict a closed form and get a procedure, or predict a finite list and get a family. That is fine — a wrong prediction is still information, and it usually reveals a structural feature you missed.

## 7. Applications

- **Requirements engineering.** A specification is an anatomy: state, goal, constraints, freedom. Most project failures are anatomy failures — the freedom was never identified, so nobody noticed that the requirement does not determine the design.
- **Debugging.** State = observed behavior; goal = explain it; constraints = what must remain true; freedom = the space of hypotheses. Under-determined diagnoses are the norm; the skill is finding the observation that pins the freedom down.
- **Experimental design.** Degrees of freedom tell you how many measurements you need; special constraints tell you which measurement is informative.
- **Quantitative finance.** "Price this derivative" is over-determined (many models, one market price); the anatomy tells you that the interesting content is in *which* assumptions are doing the work.
- **AI research.** "Improve this benchmark" is under-determined: many changes could help. Anatomy forces you to name the mechanism you believe is limiting, which is what makes an experiment informative.

## 8. Mastery Criteria

You have this chapter when you can:

1. Restate any problem in one sentence, with the goal type named.
2. Count unknowns and constraints and say which regime the problem is in.
3. Identify the special constraint and predict, before solving, that it will be the load-bearing one.
4. Answer "what would the answer look like?" with a specific form, and use that form to select a method.
5. Recognize an under-determined problem and state what must be added or asked instead.
6. Detect an unused hypothesis in your own solution and decide whether it means redundancy or error.

**Diagnostic question.** "Before solving, tell me the shape of the answer and which hypothesis you expect to use." A learner who can answer both is doing anatomy. A learner who starts manipulating immediately is hoping.

### AI Tutor Brief

- **Generate:** (i) problems with one deliberately superfluous hypothesis, to test whether the learner notices; (ii) under-determined problems that require the learner to state the correct question; (iii) problems whose goal type is ambiguous until parsed carefully ("find the maximum" versus "find all maxima"); (iv) short problems where the learner must predict the answer's form before solving.
- **Probe misconceptions:** jumping to formulas; assuming a unique answer where a family exists; ignoring integrality; treating all hypotheses as equally important.
- **Transfer distance:** medium. The skill is domain-general; vary the domain aggressively.
- **Do not** let the learner skip the anatomy step on hard problems. Require a one-sentence restatement and a goal classification before any algebra.

---

# Chapter 8 — Invariants and Monovariants

## 1. Core Idea

Fix a system with a set of **states** and a set of **allowed moves** between states.

- An **invariant** is a quantity (or property) that is the same in every state reachable from the start. If the target state has a different value, the target is unreachable.
- A **monovariant** is a quantity that changes in only one direction under every allowed move. If it is bounded, the process must terminate; if it is unbounded, the process can run forever.

These are the two most powerful tools for **impossibility** and **termination** — the two questions that direct construction cannot answer. A construction proves *can*; an invariant proves *cannot*; nothing else does.

**Principle signature.** The problem asks whether some configuration can be reached, or whether a process must stop, and the answer does not obviously depend on any numerical detail.

## 2. First Principles

**Why invariants work.** Let $\to$ be the reachability relation generated by the allowed moves. An invariant is a function $I$ with $I(s) = I(s')$ whenever $s \to s'$. By transitivity, $I$ is constant on the entire reachable set. Therefore: **reachable states lie in a single level set of $I$.** If the start and target lie in different level sets, no sequence of moves connects them.

This is a complete and rigorous argument, and it explains the design principle: an invariant should be a quantity that the moves *cannot* change, which usually means a quantity computed from the parts of the state that the moves permute, conserve, or preserve in aggregate.

**Why monovariants work.** If $M$ is integer-valued and strictly decreases with every move, then no infinite sequence of moves exists, because a strictly decreasing sequence of integers bounded below is finite. This is well-ordering of $\mathbb{N}$ in disguise (→ Ch. 10), and it is the standard termination argument for algorithms (→ Ch. 16).

**Where invariants come from.** In practice, invariants are found by looking at what the move *preserves*:

| Move type | Typical invariant |
|---|---|
| Permuting, rearranging | Multiset of values; sum; product |
| Replacing $a,b$ by $a\pm b$ | Sum mod 2; gcd; parity of count of odd entries |
| Coloring, tiling | Weighted sum with a clever coloring |
| Moving a token | Coordinates mod something; color of square |
| Cutting, gluing | Area; perimeter mod 2; number of boundary components |
| Rotating, reflecting | Distances; angles; orientation (sign of determinant) |
| Adding/removing edges | Parity of degree sums; number of components mod 2 |

**Two-level invariants.** Often a single invariant is not enough; you need a *vector* of invariants, or an invariant that lives in a group (e.g. a residue mod $n$, or a complex number). The complex-weighted coloring in Demonstration 8.3 is the model case.

## 3. Reasoning Process

1. **Formalize the state.** What data specifies a configuration? Write it as a tuple.
2. **Formalize the moves.** Exactly which transformations are allowed? Be pedantic — most failed invariant arguments fail because a move was described too loosely.
3. **Hunt for preserved quantities.** For each component of the state, ask: does this move change it? If several moves are allowed, look for a quantity unchanged by *all* of them. Candidates: parity, sum, product, gcd, residue, area, angle sum, color count, degree sequence, number of components, orientation.
4. **Test the invariant on the start and target.** If they differ, you have an impossibility proof.
5. **If they agree, the invariant has not settled the question.** Either find a finer invariant, or switch to a constructive approach. Agreement is never a proof of reachability.
6. **For termination, find a monovariant** that is integer-valued, bounded below, and strictly decreases. If strict decrease fails on some moves, look for a lexicographic monovariant (a tuple that decreases in the first coordinate that changes).

## 4. Demonstrations

### Demonstration 8.1 — The classic coloring invariant

*Problem.* Can a $8\times8$ chessboard with two opposite corner squares removed be tiled by $1\times2$ dominoes?

*Formalization.* State: a set of covered squares. Move: place a domino on two adjacent uncovered squares.

*Invariant.* Color the board as a chessboard. Every domino covers exactly one black and one white square, so for any tileable region, $\#\text{black} = \#\text{white}$.

*Test.* The full board has $32$ black and $32$ white. Removing two opposite corners — say $(1,1)$ and $(8,8)$ — removes two squares of the *same* color, since both have $i+j$ even. The remaining region has $30$ of one color and $32$ of the other.

*Conclusion.* Since $30 \ne 32$, no tiling exists. $\blacksquare$

**What to notice.** The invariant did not merely fail to find a tiling; it *proved* none exists. Also notice how much the argument depends on the precise choice of corners: removing two corners of *opposite* colors leaves $31$ and $31$, and the invariant no longer obstructs a tiling (and indeed a tiling exists — worth constructing to see that the invariant was the only obstruction in this case). **The invariant is sensitive to exactly the feature that matters.**

### Demonstration 8.2 — A monovariant that proves termination

*Process.* Start with a finite multiset of positive integers. A move consists of choosing two elements $a, b$, removing them, and inserting $|a-b|$ if it is nonzero.

*Claim.* Every sequence of moves terminates.

*Proof.* Let $S$ be the sum of all elements. A move replaces $a+b$ by $|a-b|$, so
$$S \mapsto S - (a+b) + |a-b| = S - 2\min(a,b).$$
Since $a,b \ge 1$, we have $\min(a,b) \ge 1$, so $S$ decreases by at least $2$ at every move. $S$ is a non-negative integer, so it cannot decrease strictly infinitely often. Hence every sequence of moves is finite. $\blacksquare$

**What to notice.** The monovariant is not the *number* of elements (which stays the same or drops by one) but the *sum*, which decreases by a quantity that is bounded away from zero. **A monovariant must decrease by a definite amount, not merely "decrease".** If the decrease could be arbitrarily small, the argument fails for real-valued quantities (though it can still work if the state space is finite).

### Demonstration 8.3 — A weighted invariant with complex numbers

*Problem.* Can a $6\times6$ board be tiled by $1\times4$ rectangles (in either orientation)?

*Formalization.* State: covered cells. Move: place a $1\times4$ or $4\times1$ rectangle on four consecutive uncovered cells in a row or column.

*Invariant.* Index cells by $(i,j)$ with $0 \le i,j \le 5$. Assign to cell $(i,j)$ the weight $\omega^{i+j}$, where $\omega = i$ (the imaginary unit), so $\omega^4 = 1$ and $1+\omega+\omega^2+\omega^3 = 1+i-1-i = 0$.

Any four consecutive cells in a row have weights $\omega^{i+j}, \omega^{i+j+1}, \omega^{i+j+2}, \omega^{i+j+3}$, whose sum is $\omega^{i+j}(1+\omega+\omega^2+\omega^3) = 0$. The same holds for four consecutive cells in a column. Therefore **the total weight of any tileable region is $0$.**

*Test.* The total weight of the whole $6\times6$ board is
$$\left(\sum_{i=0}^{5}\omega^i\right)\left(\sum_{j=0}^{5}\omega^j\right) = \left(\sum_{i=0}^{5}\omega^i\right)^2.$$
Now $\sum_{i=0}^{5}\omega^i = (1+\omega+\omega^2+\omega^3) + (\omega^4+\omega^5) = 0 + (1+\omega) = 1+i$. Hence the total is $(1+i)^2 = 2i \ne 0$.

*Conclusion.* No tiling exists. $\blacksquare$

**What to notice.** The area count is not an obstruction: $36 = 9\cdot4$. A parity or two-coloring argument does not settle it either. The obstruction requires an invariant valued in $\mathbb{C}$, chosen precisely so that a tile sums to zero. **This is the general technique: choose weights so that every tile has weight zero, then compute the board's weight.** The choice of $\omega$ as a fourth root of unity is forced by the tile length $4$ — the invariant is *designed*, not discovered by luck.

### Demonstration 8.4 — Invariant plus monovariant: Euclid's algorithm

*Process.* Given integers $a > b \ge 0$, repeatedly replace $(a,b)$ by $(b,\ a \bmod b)$ until $b = 0$.

*Invariant.* $\gcd(a,b)$ is unchanged: every common divisor of $a$ and $b$ divides $a - qb = a \bmod b$, and conversely, so the two pairs have identical sets of common divisors, hence the same gcd.

*Monovariant.* The second component strictly decreases: $a \bmod b < b$.

*Conclusion.* The process terminates (monovariant, bounded below by $0$), and at termination $b=0$, where $\gcd(a,0) = a$. By the invariant, that $a$ equals the original gcd. Hence the algorithm is correct. $\blacksquare$

**What to notice.** This is the template for **all** correctness proofs of algorithms: an invariant that captures *what is being preserved*, and a monovariant that guarantees *the process ends*. Neither alone suffices. The pair is the proof (→ Ch. 16).

## 5. Connections

- **← Ch. 4.** Invariant arguments are usually packaged as proofs by contradiction: assume the target is reachable, derive equal invariants, contradict.
- **← Ch. 7.** Under-determination signals that an invariant exists; anatomy tells you to look for one.
- **→ Ch. 9.** Symmetry is an invariant under a group of transformations — the continuous analogue of this chapter.
- **→ Ch. 10.** Monovariants are well-ordering in motion; the descent in Demonstration 8.2 is the same mechanism as minimal counterexamples.
- **→ Ch. 14.** Canonical forms are invariants used *constructively*: reduce to a canonical representative, then compare.
- **→ Ch. 16.** Every algorithm correctness proof is an invariant plus a termination measure.
- **→ Ch. 27.** Conservation laws in physics are invariants under symmetry groups; Noether's theorem is the structural reason.

## 6. Limitations

**Agreement of invariants proves nothing.** If the start and target share the invariant, you have learned only that this particular obstruction is absent. Reachability may still fail for other reasons. The logic is one-directional: different invariant $\Rightarrow$ unreachable; same invariant $\Rightarrow$ unknown.

**The invariant may be too coarse.** A parity invariant cannot distinguish states that differ in a subtler way. When your invariant fails to obstruct, the fix is usually a *finer* invariant (a residue mod $n$, a vector, a group-valued quantity), not a different argument style.

**Finding the invariant can be as hard as the problem.** There is no algorithm for choosing the right quantity. The practical method is: enumerate candidates from the table in §2, test each on small cases, and use the *structure of the target* to guess what must be preserved.

**Monovariants require a discrete or well-founded order.** A real-valued quantity that decreases by smaller and smaller amounts does not prove termination. You need either integer-valued decrease bounded below, or a finite state space, or a lexicographic order on a well-founded set.

**Invariants do not construct.** They prove impossibility. If the answer is "yes, it can be done", you must build it — and the invariant gives you no help, though it may tell you which constructions are worth trying.

## 7. Applications

- **Physics.** Energy, momentum, and charge are invariants; conservation laws are the reason processes are constrained. Noether's theorem explains *why*: each continuous symmetry yields an invariant.
- **Distributed systems.** "Exactly-once delivery", "no lost updates", and "monotonic reads" are invariants; a protocol is correct exactly when it preserves them under all interleavings.
- **Blockchain and consensus.** The total supply, the validity of the chain, and the absence of double-spends are invariants; forks are failures of an invariant under concurrent moves.
- **Program analysis.** Loop invariants are the standard verification technique; termination proofs are monovariants (ranking functions).
- **Chemistry and biology.** Stoichiometry, conservation of mass, and (in models) conserved moieties are invariants that constrain which reaction networks are feasible.
- **Economics.** Budget constraints and conservation of value in a closed market are invariants; "free lunch" arguments are invariant arguments.

## 8. Mastery Criteria

You have this chapter when you can:

1. Formalize a process as a state space plus moves, precisely enough that the moves cannot be reinterpreted.
2. Generate at least three candidate invariants for a given process and test each against the target.
3. Design a weighted invariant (with residues, roots of unity, or group elements) when a simple parity argument fails.
4. Prove termination with an explicit monovariant, including a lexicographic one when no single quantity works.
5. State clearly why agreement of invariants is not a proof of reachability, and switch to construction in that case.
6. Use an invariant-plus-monovariant pair to prove an algorithm correct.

**Diagnostic question.** "Here is a process and a target. Prove it is impossible, or build it." A learner who tries constructions for a long time before looking for an invariant has not internalized the signature. A learner who writes down three candidate invariants in the first two minutes has.

### AI Tutor Brief

- **Generate:** (i) reachability/impossibility problems where a naive area or parity count is insufficient; (ii) termination problems requiring a lexicographic monovariant; (iii) problems where the invariant exists but is *insufficient*, to test whether the learner overclaims; (iv) algorithm-correctness problems requiring an invariant plus a ranking function.
- **Probe misconceptions:** "same invariant therefore reachable"; monovariants that decrease by a variable amount; invariants that only work for the specific small case; forgetting to prove the moves preserve the quantity.
- **Transfer distance:** high. Invariants are the most transferable principle in the guide — test them in graphs, games, geometry, and algorithms.
- **Do not** accept "by symmetry" or "clearly invariant". Require the computation that shows each move preserves the quantity.

---

# Chapter 9 — Symmetry and "Without Loss of Generality"

## 1. Core Idea

A **symmetry** of a problem is a transformation that maps valid configurations to valid configurations while preserving the goal. Symmetries partition the configuration space into **orbits** — sets of configurations that are equivalent for the purposes of the problem.

Two consequences:

1. **Reduction.** If the goal is invariant on each orbit, you may solve the problem on a single representative of each orbit. This is what "without loss of generality" (WLOG) means, and it is a *claim requiring proof*.
2. **Averaging.** If a configuration is not symmetric, averaging it over its orbit produces a symmetric configuration. For problems with convex or linear structure, the average is at least as good — which is how symmetry produces extremal solutions (→ Ch. 11, 20).

**Principle signature.** The problem's data can be permuted, relabeled, reflected, rotated, or rescaled without changing the question; or the goal asks for an extremum and the constraints are symmetric.

## 2. First Principles

**Group actions, minimally.** A set $G$ of transformations acts on a set $X$ of configurations. The **orbit** of $x$ is $Gx = \{gx : g \in G\}$. Orbits partition $X$. A function $f$ on $X$ is **invariant** if $f(gx) = f(x)$ for all $g,x$.

**The WLOG criterion.** "WLOG we may assume $P$" is legitimate exactly when:

- **(i) Invariance:** the goal is unchanged by every $g \in G$.
- **(ii) Surjectivity on orbits:** every orbit contains at least one element satisfying $P$.

Both must be checked. (i) fails when the goal distinguishes configurations that the symmetry identifies; (ii) fails when the restriction $P$ excludes entire orbits.

**The averaging principle.** If $f$ is invariant and the goal is to maximize $f$, and if the constraint set is convex and $G$-invariant, then the average $\bar x = \frac{1}{|G|}\sum_g gx$ is feasible and $f(\bar x) \ge f(x)$ when $f$ is concave. Hence a maximizer can be taken symmetric. This is the rigorous version of "the answer should be symmetric", and it is the engine behind many extremal results.

**Symmetry breaking.** Sometimes symmetry is a nuisance: a symmetric configuration has degenerate perturbations, and you learn more by *breaking* it deliberately (fixing a representative, perturbing one parameter). Symmetry breaking is a computational strategy, not a logical one: it does not lose generality, it just organizes the search.

## 3. Reasoning Process

1. **Identify the group.** What can you relabel, permute, reflect, rotate, translate, or rescale without changing the problem? Write the transformations down.
2. **Check invariance of the goal.** Does the quantity to be found (or the property to be proved) take the same value on every element of an orbit? If not, symmetry cannot be used for reduction — but it may still be used for *structure*.
3. **Choose a canonical representative.** Order the variables ($a \le b \le c$), fix a vertex, put the largest first, choose the lexicographically least. Then prove every orbit has such a representative.
4. **Check the restriction is achievable.** This is where WLOG fails most often: the canonical condition may be incompatible with the constraints (e.g. "assume all variables are non-negative" when the constraints permit negatives).
5. **Solve on the representative.** The problem should now be smaller or more concrete.
6. **Lift the conclusion.** Because the goal is invariant, the conclusion holds for the whole orbit, hence for all configurations.
7. **Consider averaging** if the problem is an extremum: the symmetric candidate is often the answer, and the averaging argument proves it.

## 4. Demonstrations

### Demonstration 9.1 — Ramsey $R(3,3) = 6$: symmetry plus pigeonhole

*Problem.* Show that among any $6$ people, there are either $3$ mutual acquaintances or $3$ mutual strangers. (Model: color each edge of $K_6$ red for "acquaintance", blue for "stranger". Show there is a monochromatic triangle.)

*Solution.* Pick a person $P$. Of the other $5$ people, each is connected to $P$ by a red or blue edge. By the pigeonhole principle (→ Ch. 13), at least $3$ of them are connected to $P$ by edges of the same color. **WLOG** (swapping the names of the two colors is a symmetry of the problem — the claim is symmetric in "acquaintance" and "stranger") assume these three people $A, B, C$ are all acquainted with $P$.

Now consider the three edges among $A, B, C$.

- If any one of them is red — say $AB$ — then $P, A, B$ are pairwise acquainted: a red triangle.
- If none is red, then all three are blue, so $A, B, C$ are pairwise strangers: a blue triangle.

Either way, a monochromatic triangle exists. $\blacksquare$

**What to notice.** The WLOG here is legitimate and must be justified: the goal ("there is a monochromatic triangle") is invariant under swapping the two colors, and every configuration has an orbit representative in which the three same-colored edges from $P$ are red. Both clauses of the criterion are satisfied.

Also notice the *combination*: symmetry alone does not solve it, and pigeonhole alone does not. The symmetry reduces the two cases to one; the pigeonhole produces the three edges. **Most olympiad solutions are such combinations** (→ Ch. 24).

### Demonstration 9.2 — An illegitimate WLOG

*Claim.* If $x+y=1$, then $x^2+y^2 \ge \tfrac12$.

*Flawed proof.* The problem is symmetric in $x$ and $y$, so WLOG $x \ge y \ge 0$. Then $x \ge \tfrac12$ and $y \le \tfrac12$, and
$$x^2+y^2 = \left(\tfrac12+t\right)^2 + \left(\tfrac12-t\right)^2 = \tfrac12 + 2t^2 \ge \tfrac12$$
where $t = x - \tfrac12 \ge 0$. $~\blacksquare$

*Diagnosis.* The conclusion is true, but the proof is invalid: the restriction $y \ge 0$ is **not** WLOG. The symmetry group is $\{x \leftrightarrow y\}$, and the configuration $(x,y) = (2,-1)$ satisfies the hypothesis; its orbit is $\{(2,-1),(-1,2)\}$, and neither element has both coordinates non-negative. So the restriction excludes entire orbits, violating condition (ii).

*Repair.* Drop the non-negativity assumption and keep only $x \ge y$: WLOG $x \ge \tfrac12$ (since $x + y = 1$ and $x\ge y$ force $x \ge 1/2$). Write $x = \tfrac12 + t$ with $t \ge 0$ and $y = \tfrac12 - t$. Then $x^2+y^2 = \tfrac12 + 2t^2 \ge \tfrac12$, with no sign assumption needed. $\blacksquare$

**What to notice.** The repaired proof is *shorter*. The illegitimate hypothesis was not just unjustified — it was unnecessary. This is typical: **WLOG abuses usually add assumptions that the argument does not need**, which is a strong hint that they are illegitimate.

### Demonstration 9.3 — Symmetry as a computational device

*Claim.* For $n \ge 2$ and $\omega = e^{2\pi i/n}$,
$$\sum_{k=0}^{n-1}\omega^k = 0.$$

*Proof.* Let $S = \sum_{k=0}^{n-1}\omega^k$. Multiplying by $\omega$ merely permutes the terms (since $\omega^n = 1$):
$$\omega S = \sum_{k=0}^{n-1}\omega^{k+1} = \sum_{k=1}^{n}\omega^{k} = \sum_{k=1}^{n-1}\omega^k + \omega^n = (S - 1) + 1 = S.$$
So $(\omega - 1)S = 0$. Since $\omega \ne 1$ for $n \ge 2$, $S = 0$. $\blacksquare$

*Consequence.* Taking real parts, $\sum_{k=0}^{n-1}\cos(2\pi k/n) = 0$, hence $\sum_{k=1}^{n-1}\cos(2\pi k/n) = -1$. A trigonometric identity obtained with no trigonometry.

**What to notice.** The symmetry is *multiplication by $\omega$ permutes the index set*. This is the same mechanism as a group acting on a set, and it is the reason roots of unity appear everywhere: they are the coordinates in which cyclic symmetry becomes linear (→ Ch. 15). The technique — "apply the symmetry to the whole sum and use the fact that it permutes the terms" — is one of the most reusable moves in mathematics.

## 5. Connections

- **← Ch. 8.** Symmetry is invariance under a group; invariants are the discrete shadow of the same idea.
- **→ Ch. 11.** Extremal configurations are often forced to be symmetric by an averaging or exchange argument.
- **→ Ch. 13.** The pigeonhole step in Demonstration 9.1 is what converts symmetry into a concrete configuration.
- **→ Ch. 19.** Isomorphism is "the same structure"; symmetry is "the same configuration". Both are group actions in disguise.
- **→ Ch. 20.** Symmetry reduces the feasible set, which is often how an optimization becomes tractable.
- **→ Ch. 27.** Dimensional analysis is symmetry under change of units; scaling laws are its consequences.

## 6. Limitations

**Symmetry can be broken by the goal.** If the problem asks you to distinguish two configurations that a symmetry identifies, WLOG is unavailable. "Find the number of ways to seat people at a round table" is not symmetric under rotation *if* seats are labeled, but is if they are not — the group depends on what counts as the same.

**The symmetric candidate may not be optimal.** Symmetry of the constraints does not guarantee symmetry of the optimum when the objective is not concave, or when the feasible set is not convex. Symmetric problems can have asymmetric optima (spontaneous symmetry breaking). Always check with an explicit example.

**WLOG can hide a case split.** A legitimate WLOG may still leave several orbits, each needing separate treatment. The reduction is to *one representative per orbit*, not to one configuration.

**Orbit counting is not free.** Counting orbits requires Burnside's lemma or careful casework; the symmetry reduces the problem but does not eliminate it.

**Naming a symmetry is not using it.** "By symmetry" is acceptable only when the symmetry and its invariance are both evident. Otherwise write the transformation.

## 7. Applications

- **Combinatorics.** Counting up to rotation and reflection (necklaces, bracelets, polyominoes) is orbit counting under a group action.
- **Physics.** Symmetries of the Lagrangian produce conservation laws; gauge symmetry determines the form of interactions.
- **Crystallography.** The 230 space groups classify all possible crystal symmetries; the classification is a group-theoretic theorem with direct physical content.
- **Optimization.** Symmetric problems admit symmetric solutions under convexity; exploiting symmetry reduces the search space by orders of magnitude.
- **Machine learning.** Equivariant architectures (convolutional networks, graph networks) build symmetry into the model, which is why they generalize across translations and permutations.
- **Engineering design.** Symmetric designs are easier to analyze and often more robust, but symmetric structures can have degenerate failure modes — a reason to break symmetry deliberately in some designs.

## 8. Mastery Criteria

You have this chapter when you can:

1. Identify the symmetry group of a problem explicitly and check that the goal is invariant.
2. State and verify both clauses of the WLOG criterion, and construct a canonical representative.
3. Produce an illegitimate WLOG and explain which clause fails.
4. Use a symmetry to simplify a computation (as in Demonstration 9.3) rather than merely to assert a reduction.
5. Decide when the symmetric candidate is *provably* optimal, and when symmetry may break.
6. Count orbits when the problem asks "how many essentially different" configurations exist.

**Diagnostic question.** "You wrote 'WLOG'. Prove it." A learner who can articulate invariance plus orbit-surjectivity has the concept. A learner who says "it's symmetric" has a slogan.

### AI Tutor Brief

- **Generate:** (i) problems with a genuine WLOG and problems with a plausible but invalid one, mixed; (ii) orbit-counting problems; (iii) extremal problems where the symmetric candidate is optimal and ones where it is not; (iv) computations simplified by a symmetry of the index set.
- **Probe misconceptions:** "symmetric problem implies symmetric answer"; WLOG that silently restricts signs or ordering without justification; confusing relabeling symmetry with geometric symmetry.
- **Transfer distance:** high. Test in geometry, combinatorics, algebra, and probability.
- **Do not** accept "by symmetry" without the transformation and the invariance check. Require the two-clause justification at least once per session.

---

# Chapter 10 — Induction, Recursion, and Well-Ordering

## 1. Core Idea

Induction is not a trick for proving sums. It is the **structural axiom of the natural numbers**, and it has three faces:

- **Well-ordering:** every nonempty set of positive integers has a least element.
- **Induction:** if $P(1)$ holds and $P(n) \Rightarrow P(n+1)$, then $P(n)$ holds for all $n$.
- **Strong induction:** if $(\forall k < n\ P(k)) \Rightarrow P(n)$, then $P(n)$ holds for all $n$.

These are logically equivalent. **Descent** is induction run backwards: to prove no counterexample exists, show that any counterexample yields a smaller one. **Recursion** is the construction-side dual: to build an object of size $n$, build one of size $n-1$ and extend.

The single most important practical fact about induction is this:

> **The hypothesis you induct on is often not the theorem you were asked to prove.** Strengthening the statement frequently makes the induction go through.

**Principle signature.** The problem involves a discrete parameter $n$; the answer for $n$ plausibly depends on the answer for smaller values; or the problem asserts that some process must terminate; or it claims a universal statement over $\mathbb{N}$ with a recursive structure.

## 2. First Principles

**Why induction is valid.** It is the content of well-ordering. Suppose $P(1)$ holds and $P(n) \Rightarrow P(n+1)$, but some $P(n)$ fails. Let $m$ be the least failure (well-ordering). Then $m \ne 1$, so $m-1 \ge 1$ and $P(m-1)$ holds; by the inductive step, $P(m)$ holds — contradiction. So no failure exists.

Note what this proof does: it *uses* well-ordering to justify induction. You cannot justify well-ordering by induction without circularity. One of them is an axiom; the choice of which is a matter of exposition.

**Why strong induction is equivalent.** Assume strong induction. Then in particular $P(n) \Rightarrow P(n+1)$ (take the hypothesis for all $k<n$, which includes $k=n$). Conversely, given ordinary induction, strong induction follows by applying ordinary induction to the statement $Q(n) = $ "$P(k)$ holds for all $k \le n$".

**Structural induction.** For objects built recursively (trees, formulas, strings, graphs built by adding edges), the same principle applies with "smaller" meaning "built earlier". The base cases are the *minimal* objects, and there may be several — all must be checked. A proof that forgets a base case is not a proof.

**Descent.** To prove that no object with property $Q$ exists, suppose one does, and derive a strictly smaller one with $Q$. This contradicts well-ordering. Descent is the natural engine for irrationality, for impossibility of integer solutions, and for minimal-counterexample arguments (→ Ch. 32).

**Recursion and induction are duals.** An inductive proof establishes a property of all $n$; a recursive definition constructs an object for all $n$. The correctness of the construction is proved by induction, and the structure of the proof mirrors the structure of the definition. This duality is why "define $a_{n+1} = f(a_n)$ and prove $P(a_n)$" is a single act of thought, not two.

## 3. Reasoning Process

1. **Identify the parameter.** What is $n$? It may be a size, a count, a dimension, a number of moves, or a depth.
2. **Ask what smaller objects look like.** How do you get from $n$ to $n-1$ (or to something smaller)? The move must be *structural*, not merely numerical.
3. **Choose the form.** Weak induction if $P(n)$ follows from $P(n-1)$; strong induction if $P(n)$ needs several earlier cases; descent if you are proving nonexistence; structural induction if the object is recursive.
4. **Check the base case(s).** All of them. For structural induction, every minimal object.
5. **Strengthen if necessary.** If the inductive step does not close, the hypothesis is probably too weak. Add the extra information you needed (a bound, a parity condition, a second statement) and prove the stronger claim.
6. **Verify the step uses the hypothesis essentially.** If the step proves $P(n+1)$ without using $P(n)$, you have a direct proof, not an induction — which is fine, but say so.
7. **Check for the classic errors.** Circularity (using $P(n+1)$ to prove $P(n+1)$); a base case that does not cover the minimal objects; a "smaller" relation that is not well-founded; an induction that silently assumes $n \ge$ some threshold without handling the gap.

## 4. Demonstrations

### Demonstration 10.1 — Strong induction: prime factorization

*Claim.* Every integer $n \ge 2$ is a product of primes.

*Proof.* Strong induction on $n$. Base case $n = 2$: $2$ is prime, so it is a product of one prime.

Inductive step: assume every integer $k$ with $2 \le k < n$ is a product of primes. Consider $n$. If $n$ is prime, it is a product of one prime. Otherwise $n = ab$ with $1 < a, b < n$. By the inductive hypothesis (applied to both $a$ and $b$, which are smaller), each is a product of primes; concatenating the two factorizations gives one for $n$. $\blacksquare$

**What to notice.** Weak induction would fail here: $n = ab$ does not give $b = n-1$, so knowing $P(n-1)$ is useless. **The choice between weak and strong induction is dictated by the structure of the reduction, not by preference.** Here the reduction splits $n$ into two factors, so we need *all* smaller values.

### Demonstration 10.2 — Strengthening the hypothesis to make the induction work

*Claim.* For all $n \ge 1$, $\displaystyle\sum_{k=1}^{n}\frac{1}{k^2} < 2$.

*Naive attempt.* Assume $S_n < 2$; then $S_{n+1} = S_n + \frac{1}{(n+1)^2} < 2 + \frac{1}{(n+1)^2}$, which is *not* $< 2$. The induction fails — not because the claim is false, but because the hypothesis is too weak to survive the step.

*Strengthened claim.* For all $n \ge 1$, $\displaystyle S_n \le 2 - \frac{1}{n}$.

*Proof by induction.* Base case $n=1$: $S_1 = 1 \le 2 - 1 = 1$. ✓

Inductive step: assume $S_n \le 2 - \frac1n$. Then
$$S_{n+1} = S_n + \frac{1}{(n+1)^2} \le 2 - \frac{1}{n} + \frac{1}{(n+1)^2}.$$
It suffices to show $\frac{1}{(n+1)^2} \le \frac{1}{n} - \frac{1}{n+1} = \frac{1}{n(n+1)}$, i.e. $n \le n+1$, which is true. Hence $S_{n+1} \le 2 - \frac{1}{n+1}$. $\blacksquare$

Since $2 - \frac1n < 2$, the original claim follows.

**What to notice.** This is the most important induction technique in practice. The strengthened statement is *stronger* (it says more) yet *easier* to prove, because it carries the slack needed to close the step. **When an induction fails, do not abandon induction — strengthen the hypothesis.** The extra term is not guessed from nowhere: it is exactly the "slack" that the failed step revealed was missing.

### Demonstration 10.3 — Structural induction: the handshake lemma

*Claim.* In every finite graph, the number of vertices of odd degree is even.

*Proof.* Induct on the number of edges $m$.

*Base case* $m=0$: all degrees are $0$, so there are no odd-degree vertices, and $0$ is even. ✓

*Inductive step:* assume the claim for all graphs with $m$ edges, and let $G$ have $m+1$ edges. Choose an edge $e = uv$ and let $G' = G - e$, which has $m$ edges. In passing from $G'$ to $G$, the degrees of $u$ and $v$ each increase by $1$ (or, if $u=v$, the degree of $u$ increases by $2$); all other degrees are unchanged.

- If $u \ne v$: each of $u,v$ changes parity. So the count of odd-degree vertices changes by $+2$, $0$, or $-2$ — always by an even amount. By hypothesis the count in $G'$ is even, so the count in $G$ is even.
- If $u = v$ (a loop): the degree of $u$ changes by $2$, so no parity changes; the count is unchanged, hence even.

$\blacksquare$

**What to notice.** The induction is on the *structure* (adding an edge), not on a number in the statement. The case split on loops is exactly the kind of case that a careless proof omits — and the omission would be fatal for multigraphs. **Structural induction forces you to enumerate the ways an object can be built, which is the same as enumerating the cases.**

### Demonstration 10.4 — A failed induction, diagnosed

*Claim (false).* Every person in any group of $n$ people has the same height.

*Flawed proof.* Base case $n=1$: trivial. Inductive step: assume the claim for groups of size $k$. Given a group of $k+1$ people, remove person $A$; the remaining $k$ all have the same height. Reinsert $A$ and remove person $B \ne A$; the remaining $k$ (which includes $A$) all have the same height. Therefore $A$ has the same height as everyone else, and all $k+1$ agree. $\blacksquare$

*Diagnosis.* The step from $k$ to $k+1$ requires that the two groups of size $k$ *overlap*, so that a common person transmits the equality. For $k+1 \ge 3$ they do overlap. For $k+1 = 2$, the two groups are the singletons $\{B\}$ and $\{A\}$, which are disjoint — there is no common person. So the inductive step is valid only for $k \ge 2$, and the chain breaks at the very first link ($1 \to 2$).

**What to notice.** The base case was correct and the step was correct *for most $k$*. The proof failed because the step's validity depended on $k$, and that dependence was not checked. **The lesson: an inductive step is a theorem about $k$; it must hold for every $k$ in the range, including the smallest.**

## 5. Connections

- **← Ch. 4.** Induction is a proof engine; descent is contradiction plus well-ordering.
- **← Ch. 8.** Monovariants are well-ordering in disguise; termination proofs are descent.
- **→ Ch. 12.** Recursive counting (Fibonacci, Catalan) is proved correct by induction; generating functions solve the recurrences (→ Ch. 15).
- **→ Ch. 14.** Structural induction requires a canonical decomposition of objects, which is a canonical-form problem.
- **→ Ch. 32.** Minimal counterexamples are descent; the extremal principle (Ch. 11) is the same idea with an optimization attached.
- **→ Ch. 22.** Asymptotics of recursively defined sequences (divide-and-conquer recurrences) is induction over scales.

## 6. Limitations

**Induction proves, it does not explain.** An inductive proof of a closed form tells you the formula is right, not why. When you can find a bijective or structural proof, it usually generalizes further (→ Ch. 12).

**Induction does not discover formulas.** You must know (or guess) the statement before you can induct. Guessing is a separate skill (→ Ch. 31, 33).

**Well-ordering fails outside $\mathbb{N}$.** The integers are not well-ordered (no least element), the rationals are not well-ordered (no least positive element), and the reals are not well-ordered in the usual order. Descent arguments must stay within a well-founded set.

**Transfinite and structural subtleties.** For objects of infinite size, induction requires a well-founded relation, and "smaller" must be checked carefully. Naive induction on infinite structures produces paradoxes.

**Induction can obscure the mechanism.** A long induction can hide the fact that the real content is a single structural observation. If the induction has many cases, look for the invariant or the bijection underneath.

## 7. Applications

- **Algorithm analysis.** Recursive algorithms are proved correct by structural induction; their running times satisfy recurrences solved by induction or the master theorem.
- **Formal verification.** Inductive invariants over program states are the basis of model checking and theorem proving.
- **Combinatorics.** Counting recursive structures (trees, triangulations, paths) is induction plus a decomposition.
- **Number theory.** Descent is the classical engine for Diophantine impossibility (Fermat's method of infinite descent).
- **Finance.** Backward induction prices options on trees; the principle of optimality is induction run backwards.
- **Game theory.** Zermelo's theorem (finite games are determined) is proved by induction on the game tree.

## 8. Mastery Criteria

You have this chapter when you can:

1. Choose weak, strong, structural, or descent induction based on the *reduction structure*, and justify the choice.
2. Strengthen a hypothesis when the inductive step fails, and explain what slack the strengthening supplies.
3. Check all base cases, including the minimal objects of a structural induction.
4. Diagnose a broken induction by locating the $k$ at which the step fails.
5. Convert a termination question into a descent or monovariant argument.
6. Recognize when an induction is merely certifying a formula whose explanation lies elsewhere.

**Diagnostic question.** "This induction fails at the step. Fix it without changing the theorem." A learner who immediately strengthens the hypothesis has the skill. A learner who searches for a different theorem does not yet.

### AI Tutor Brief

- **Generate:** (i) inductions requiring a strengthened hypothesis; (ii) structural inductions with multiple base cases and a tempting missing case; (iii) descent problems in number theory and graph theory; (iv) broken inductions to diagnose, especially ones with a correct base case and a step that fails at small $k$.
- **Probe misconceptions:** "induction = plug in $n$ and $n+1$"; forgetting a base case; using $P(n+1)$ in the proof of $P(n+1)$; assuming the step is uniform in $k$.
- **Transfer distance:** high, but always include at least one problem where induction is the *wrong* tool, so the learner must recognize the signature rather than apply the method reflexively.
- **Do not** accept an induction whose base case is "obvious" without verification, or whose step omits the range of $k$ for which it is valid.

---

# Chapter 11 — The Extremal Principle

## 1. Core Idea

To prove that something exists, exhibit the object that is **largest**, **smallest**, **closest**, **farthest**, **most**, or **least** in some respect. Extremal objects are special: they satisfy additional constraints *because* they are extremal. Any local modification that would improve the quantity is forbidden, and that prohibition is a new equation or inequality you can use.

**Principle signature.** The problem asks to prove existence, or to prove a universal statement, and there is a natural finite or compact set of candidates together with a natural quantity to optimize. The phrase "among all such configurations, choose one that..." is the giveaway.

The extremal principle is the most *generative* of the classical techniques: when you are stuck on a "prove there exists" problem, choosing an extremal object is almost always worth trying, because it manufactures structure out of nothing.

## 2. First Principles

**Existence is not automatic.** Before choosing a maximum, you must know one exists. Two standard sources:

- **Finiteness.** A nonempty finite set of real numbers has a maximum and a minimum.
- **Compactness.** A continuous function on a closed bounded set attains its extrema (extreme value theorem).

If neither applies, the extremal object may not exist: $\{1 - 1/n : n \ge 1\}$ has a supremum but no maximum. **Assuming a maximum exists when it does not is one of the most common errors in olympiad writing**, and it is exactly the error that produces false proofs about "the smallest counterexample" when the set of counterexamples is not known to be nonempty.

**Why extremality gives structure.** Let $x^*$ maximize $f$ over a set $S$. Then for every $y \in S$, $f(y) \le f(x^*)$. If you can construct, for any $x$ that fails to have property $P$, a $y \in S$ with $f(y) > f(x)$, then $x^*$ must have property $P$. This is the whole technique: **turn a property into an inequality, and let the extremal object satisfy the inequality with equality.**

In optimization language, at an extremum the first-order conditions hold: the gradient is orthogonal to the constraint surface. In combinatorial settings, the analogue is an **exchange argument**: if swapping two elements improves the objective, the extremal configuration cannot have that pattern.

**Sharpness.** An extremal argument often produces both a bound and the configuration attaining it. A bound without attainment is only half a result (→ Ch. 20).

## 3. Reasoning Process

1. **Find the quantity.** What are you optimizing? Distance, area, sum, product, degree, number of intersections, length of a chain, size of a set, number of regions?
2. **Prove existence.** Is the candidate set finite? Compact? If not, restrict it (e.g. to integer solutions, to configurations within a bounded region) until it is.
3. **Choose the extremal object** — usually the maximum or minimum, occasionally the *lexicographically* extremal one when a single quantity is insufficient.
4. **Extract consequences.** Assume the object is not of the desired form, and construct a modification that improves the quantity. Contradiction.
5. **Combine.** Extremality often gives one equation; a second principle (parity, symmetry, counting) supplies the rest.
6. **Check attainment.** Exhibit the extremal configuration, or prove the bound is not attained and state the correct conclusion.

## 4. Demonstrations

### Demonstration 11.1 — Sylvester–Gallai by minimal distance

*Theorem.* Let $S$ be a finite set of points in the plane, not all collinear. Then there is a line passing through exactly two points of $S$.

*Proof (Kelly).* Consider all pairs $(p, \ell)$ where $\ell$ is a line through at least two points of $S$ and $p \in S$ is a point not on $\ell$. Since $S$ is not all collinear, at least one such pair exists. Let $d(p,\ell) > 0$ denote the perpendicular distance. The set of such distances is a finite set of positive reals, so it has a minimum. Choose a pair $(p, \ell)$ attaining the minimum.

Suppose, for contradiction, that $\ell$ contains at least three points of $S$. Let $A, B, C$ be three of them, in order along $\ell$. Let $H$ be the foot of the perpendicular from $p$ to $\ell$. Among $A, B, C$, at least two lie on the same side of $H$ (pigeonhole: three points, two sides). Relabel so that $B$ and $C$ lie on the same side of $H$ with $B$ between $H$ and $C$.

Consider the line $pC$. It passes through two points of $S$ (namely $p$ and $C$), and $B$ is a point of $S$ not on it (since $B \ne C$ and $B$ lies on $\ell$, which meets $pC$ only at $C$). So $(B, pC)$ is a valid pair, with positive distance $d(B, pC)$.

We claim $d(B, pC) < d(p,\ell)$. To see this, place coordinates with $\ell$ as the $x$-axis, $H = (0,0)$, $p = (0,h)$ with $h = d(p,\ell) > 0$, and $B = (b,0)$, $C = (c,0)$ with $0 < b < c$. The line through $(0,h)$ and $(c,0)$ has equation $hx + cy - hc = 0$, so
$$d(B, pC) = \frac{|hb - hc|}{\sqrt{h^2+c^2}} = h\cdot\frac{c-b}{\sqrt{h^2+c^2}}.$$
Since $b < c$, we have $c - b < c < \sqrt{h^2+c^2}$, so the ratio is $< 1$ and $d(B,pC) < h = d(p,\ell)$.

This contradicts the minimality of $d(p,\ell)$. Hence $\ell$ cannot contain three points of $S$; it contains exactly two. $\blacksquare$

**What to notice.** The proof has three ingredients, each doing distinct work:

1. **Finiteness** guarantees the minimum exists. Without it, there is no argument.
2. **Extremality** converts "$\ell$ has three points" into a construction of a *smaller* distance — the extremal object is used only through the inequality it satisfies.
3. **Pigeonhole** produces the two points on the same side, which is what makes the distance strictly smaller.

This is a canonical extremal proof: the extremal choice is the *only* hypothesis, and everything else is construction. Study it until you can reproduce it from memory, because the pattern — *choose the minimal bad configuration, then perturb it into a worse one* — recurs constantly.

### Demonstration 11.2 — Extremality plus an exchange argument

*Claim.* Among all triangles with a fixed perimeter $2s$, the equilateral triangle has the largest area.

*Proof.* By Heron's formula, for a triangle with sides $a,b,c$ and semiperimeter $s$,
$$A^2 = s(s-a)(s-b)(s-c).$$
The triangle inequalities give $s-a, s-b, s-c > 0$, and $(s-a)+(s-b)+(s-c) = 3s - (a+b+c) = 3s - 2s = s$. By AM–GM (→ Ch. 6),
$$(s-a)(s-b)(s-c) \le \left(\frac{s}{3}\right)^3,$$
with equality iff $s-a = s-b = s-c$, i.e. $a=b=c=2s/3$. Hence
$$A^2 \le s\cdot\frac{s^3}{27} = \frac{s^4}{27}, \qquad A \le \frac{s^2}{3\sqrt3},$$
with equality exactly for the equilateral triangle. $\blacksquare$

**What to notice.** The "exchange" is hidden inside AM–GM: if two of $s-a, s-b, s-c$ differ, replacing both by their average keeps the sum fixed and increases the product. That is exactly an exchange argument, and it is why the extremum has all three equal. **In optimization problems with a sum constraint, the extremum is usually at equality of all terms** — a heuristic worth carrying.

### Demonstration 11.3 — When the extremum does not exist

*Problem.* Find the maximum of $f(x) = x(1-x)$ on the open interval $\left(0, \tfrac12\right)$.

*Trap.* Completing the square gives
$$f(x) = \frac14 - \left(x - \frac12\right)^2 \le \frac14.$$
It is tempting to conclude that the maximum is $\tfrac14$.

*Reality.* Equality holds only at $x = \tfrac12$, which is **not** in the domain $\left(0, \tfrac12\right)$. For every $x$ in the domain, $f(x) < \tfrac14$. So $f$ has no maximum on this interval; it has a supremum of $\tfrac14$, approached but never attained.

*Correct statement.* The supremum of $f$ on $\left(0,\tfrac12\right)$ is $\tfrac14$, and it is not attained. On the closed interval $\left[0,\tfrac12\right]$ the maximum is $\tfrac14$, attained at the endpoint $x = \tfrac12$.

**What to notice.** The lesson is procedural, not arithmetical: **before writing "let $x^*$ be the maximum", verify that the maximum exists** (→ Ch. 3). The check is usually one line — a finite candidate set, or a compact domain with a continuous objective — but omitting it invalidates every subsequent step. The standard repair in practice is to enlarge the domain to a closed one, locate the extremum, and then check whether it lies in the original domain.

The distinction between supremum and maximum is not pedantry: a bound that is not attained is a statement about the *closure* of the feasible set, and optimization problems that assume attainment produce confident answers to questions that have none (→ Ch. 20).

## 5. Connections

- **← Ch. 3.** "The maximum exists" is an existence quantifier; it must be proved, not assumed.
- **← Ch. 8.** Monovariants are extremal arguments in motion: a strictly decreasing quantity shows the process cannot continue, which is an extremal statement about the set of reachable states.
- **← Ch. 9.** Symmetric problems often have symmetric extremal solutions, provable by averaging.
- **→ Ch. 20.** The extremal principle is the combinatorial core of optimization; bounds and attainment are its two halves.
- **→ Ch. 32.** Minimal counterexamples are extremal objects in the set of counterexamples.
- **→ Ch. 26, 27.** Physical extremal principles (least action, minimum energy) are the same idea in continuous form.

## 6. Limitations

**Existence can fail.** Without finiteness or compactness, there may be no extremal object. Supremum is not maximum. This is the most common fatal flaw in extremal proofs.

**The extremal object may be degenerate.** The minimum-distance pair might be a degenerate configuration (a loop, a coincident point, a zero-length segment), and the argument may not apply there. Always check the degenerate cases separately.

**Extremality may give too little structure.** If the extremal object satisfies many constraints simultaneously, the argument can branch into cases. Sometimes a *lexicographic* extremal choice (minimize $d$, then among those minimize something else) is needed to break ties.

**The perturbation must be admissible.** Constructing a "better" object is only a contradiction if the better object is in the same feasible set. Modifications that violate a constraint prove nothing. This is the analogue of "the exchange must preserve feasibility" in optimization.

**Extremal arguments rarely compute.** They prove existence and structure, not values. If you need the actual maximum, you need attainment plus a bound (→ Ch. 20).

## 7. Applications

- **Combinatorics.** Extremal set theory (how large can a family be without a given pattern?) is built on this principle; Turán's theorem and Sperner's theorem are extremal results.
- **Graph theory.** Longest paths, maximum matchings, and minimal cuts are all extremal objects whose extremality yields structural theorems (e.g. a longest path's endpoints have all neighbors on the path).
- **Physics.** The principle of least action, minimum energy configurations, and Fermat's principle are extremal formulations; the Euler–Lagrange equations are the "extremality gives structure" step.
- **Economics.** Equilibrium as a maximum of utility or a minimum of cost; the first-order conditions are the extremality consequences.
- **Machine learning.** Empirical risk minimization is extremal reasoning; the structure of the optimum (sparsity, margin maximization) follows from extremality conditions.
- **Engineering.** Worst-case analysis and bottleneck identification are extremal arguments: the weakest link determines the failure.

## 8. Mastery Criteria

You have this chapter when you can:

1. Identify a natural extremal quantity and prove that the extremum exists.
2. Convert a hypothetical failure of the desired property into a strict improvement of the extremal quantity.
3. Use an exchange argument to show that an extremum has all relevant quantities equal.
4. Recognize when the extremal object is degenerate and handle that case.
5. Distinguish supremum from maximum, and state the correct conclusion when the maximum is not attained.
6. Combine an extremal argument with a second principle (parity, counting, symmetry) to close a proof.

**Diagnostic question.** "Prove that among all such configurations, one has property $P$." A learner who immediately asks "what should I maximize, and does the maximum exist?" has the principle. A learner who starts constructing examples does not.

### AI Tutor Brief

- **Generate:** (i) existence problems solvable by a minimal/maximal choice; (ii) problems where the naive extremal quantity does not exist (open domains, unbounded sets); (iii) exchange-argument problems in scheduling and partitioning; (iv) problems where the extremal object is degenerate and the learner must handle it.
- **Probe misconceptions:** assuming a maximum exists; perturbing into an infeasible configuration; forgetting the tie-breaking case; treating supremum as maximum.
- **Transfer distance:** high. Extremal arguments appear in every branch of mathematics; test across at least three.
- **Do not** accept "choose the largest one" without the existence proof and the improvement construction.

---

# Chapter 12 — Counting Two Ways: Bijection and Double Counting

## 1. Core Idea

Two techniques, one idea: **the same set can be described in two ways, and both descriptions must give the same count.**

- A **bijection** is a structure-preserving pairing between two sets. It proves $|A| = |B|$ without counting either, and it often proves an identity by exhibiting the *reason* it holds.
- **Double counting** counts a single set of objects along two different decompositions. The two totals are equal, and that equality *is* the identity you wanted to prove.

**Principle signature.** The problem asks for a count, or asks you to prove an identity between combinatorial expressions, or asks to prove existence of an object with a property (a nonzero count proves existence). The presence of binomial coefficients, factorials, sums of products, or "the number of ways" is the giveaway.

Bijections are strictly stronger than algebraic verification: an algebraic proof of a binomial identity confirms it, while a bijective proof *explains* it and usually generalizes (→ Ch. 18, 23).

## 2. First Principles

**Bijections preserve cardinality.** If $f : A \to B$ is injective and surjective, then $|A| = |B|$ (for finite sets). The proof is the definition of counting. The practical content is that a bijection is a **reversible encoding**: every element of $A$ has exactly one code in $B$, and every code decodes to exactly one element.

**Double counting is the same principle applied to a set of pairs.** Let $R \subseteq A \times B$ be a relation. Counting $R$ by summing over $A$ gives $\sum_{a} |\{b : (a,b) \in R\}|$; counting by summing over $B$ gives $\sum_b |\{a : (a,b)\in R\}|$. These are equal because both equal $|R|$. **The art is choosing $R$.**

**Overcounting is the main hazard.** If you count each object $k$ times, the total is $k$ times the answer. The discipline: for every object, determine its multiplicity, and prove the multiplicity is constant (or account for the variation). This is where most counting errors occur, and they are usually invisible in the final formula.

**Existence from counting.** If a count is positive, the object exists. This is the counting route to existence, and it is often easier than construction: "the number of such objects is $\binom{n}{k} > 0$, hence one exists". The probabilistic method (→ Ch. 21) is the quantitative version of this idea.

**Inclusion–exclusion is the correction for overcounting.** For sets $A_1,\dots,A_n$,
$$\left|\bigcup A_i\right| = \sum |A_i| - \sum_{i<j}|A_i \cap A_j| + \sum_{i<j<k}|A_i\cap A_j\cap A_k| - \cdots$$
Each element counted $m$ times on the right (where $m$ is the number of sets containing it) is counted $\binom{m}{1} - \binom{m}{2} + \cdots = 1$ time net. This is double counting applied to the indicator functions.

## 3. Reasoning Process

1. **Name the set you are counting.** Precisely. "The number of ways to choose..." is not precise until you say what counts as the same.
2. **Look for a second description.** Can each object be encoded as a binary string, a lattice path, a subset, a pair of subsets, a tiling, a function?
3. **Build the map and prove it is a bijection.** Two directions: every object maps to a valid code, and every valid code comes from exactly one object. Both directions are usually short but both are necessary.
4. **For identities, count a set of *pairs* or *triples* two ways.** Choose the relation $R$ so that one direction is easy (count by the first coordinate) and the other direction is the expression you want.
5. **Check multiplicities.** If you counted with multiplicity, divide by it — and prove it is constant.
6. **Sanity check** with small values: $n=1,2,3$. A binomial identity that fails at $n=2$ is wrong, and the check costs ten seconds.

## 4. Demonstrations

### Demonstration 12.1 — A bijection that explains a formula

*Claim.* $\displaystyle\sum_{k=1}^{n}(2k-1) = n^2$.

*Bijective proof.* Consider an $n \times n$ grid of cells, which has $n^2$ cells. Partition it into "L-shaped shells": the $k$-th shell consists of the cells in row $k$ up to column $k$, plus the cells in column $k$ above row $k$ — that is, $k + (k-1) = 2k-1$ cells. The shells for $k=1,\dots,n$ partition the grid, so the total number of cells is $\sum_{k=1}^n (2k-1)$, and it is also $n^2$. $\blacksquare$

**What to notice.** The algebraic proof (induction) is three lines and explains nothing. The bijection shows *why* the sum of the first $n$ odd numbers is a square: the odd numbers are the sizes of the successive shells of a square. This is the kind of understanding that transfers: the same shell decomposition proves that a sum of consecutive odd numbers starting from $1$ is a square, and suggests how to handle sums of consecutive integers starting elsewhere.

### Demonstration 12.2 — Double counting proves an identity

*Claim (Vandermonde).* For $m,n \ge 0$ and $k \ge 0$,
$$\binom{m+n}{k} = \sum_{i=0}^{k}\binom{m}{i}\binom{n}{k-i}.$$

*Proof.* Let $A$ and $B$ be disjoint sets with $|A| = m$, $|B| = n$. Count the $k$-element subsets of $A \cup B$.

*First way:* directly, $\binom{m+n}{k}$.

*Second way:* classify a $k$-subset $S$ by $i = |S \cap A|$. Then $|S \cap B| = k - i$, and there are $\binom{m}{i}$ ways to choose $S\cap A$ and $\binom{n}{k-i}$ ways to choose $S \cap B$. Summing over the possible $i$ (from $0$ to $k$, with the convention $\binom{a}{b}=0$ when $b>a$ or $b<0$) gives $\sum_i \binom{m}{i}\binom{n}{k-i}$.

Both count the same set, so the totals are equal. $\blacksquare$

**What to notice.** The identity is not proved by algebra; it is proved by *finding the set that both sides count*. This is the general method for binomial identities: ask "what is the set?" before asking "how do I manipulate the symbols?" Also note the role of the convention $\binom{a}{b}=0$ for out-of-range $b$: it makes the sum range irrelevant, which is a small but essential piece of bookkeeping.

### Demonstration 12.3 — Double counting a set of incidences

*Claim (handshake lemma).* In any finite graph, $\displaystyle\sum_{v \in V}\deg(v) = 2|E|$.

*Proof.* Let $R = \{(v,e) : v \in V,\ e \in E,\ v \text{ is an endpoint of } e\}$.

*Count by vertices:* for each $v$, there are $\deg(v)$ edges incident to it, so $|R| = \sum_v \deg(v)$.

*Count by edges:* each edge has exactly two endpoints, so $|R| = 2|E|$.

Hence $\sum_v \deg(v) = 2|E|$. $\blacksquare$

**What to notice.** The set $R$ is a set of *incidences*, not of vertices or edges. Choosing the right relation is the whole trick, and it is a general recipe: **when two quantities should be equal, look for a set of pairs that each side counts naturally.** The corollary — the number of odd-degree vertices is even — follows immediately, and gives a second proof of Demonstration 10.3.

### Demonstration 12.4 — A bijection between two apparently unrelated families

*Claim.* The number of compositions of $n$ into parts $1$ and $2$ equals $F_{n+1}$, where $F_1 = F_2 = 1$.

*Bijection.* A composition of $n$ into $1$s and $2$s corresponds to a tiling of a $1 \times n$ strip by monominoes (length $1$) and dominoes (length $2$): read the parts left to right and place tiles of those lengths. The correspondence is clearly reversible.

Now let $a_n$ be the number of such tilings. Consider the leftmost tile: it is either a monomino (leaving a strip of length $n-1$) or a domino (leaving a strip of length $n-2$). Hence
$$a_n = a_{n-1} + a_{n-2}, \qquad a_1 = 1,\ a_2 = 2.$$
This is the Fibonacci recurrence with $a_1 = F_2$, $a_2 = F_3$, so by induction $a_n = F_{n+1}$. $\blacksquare$

**What to notice.** The bijection converted a question about *arithmetic decompositions* into a question about *geometric objects*, and the geometric objects have an obvious recursive structure (look at the leftmost tile). This is a change of representation (→ Ch. 15) implemented by a bijection, and it is why tilings, compositions, and Fibonacci numbers are the same subject.

## 5. Connections

- **← Ch. 5.** A bijection is an isomorphism of sets-with-structure; the "structure" preserved is the combinatorial decomposition.
- **← Ch. 10.** Recursive counting produces recurrences; induction proves the closed form.
- **→ Ch. 13.** Pigeonhole is counting applied to a partition; the two chapters are the same tool used for different conclusions.
- **→ Ch. 14.** Canonical forms are what make bijections work: you need a unique representative to have a well-defined inverse.
- **→ Ch. 15.** Generating functions are the algebraic shadow of a bijection; the coefficient counts the objects.
- **→ Ch. 21.** The probabilistic method converts a counting bound into an existence statement.

## 6. Limitations

**Bijections are hard to find and easy to get wrong.** The inverse direction is where errors hide: a map that is injective but not surjective gives an inequality, not an equality. Always check both directions, and check the boundary cases ($n=0$, empty set).

**Not every identity has a natural bijective proof.** Some binomial identities are most easily proved by generating functions or by algebra. Insisting on a bijection can waste time; the bijection is preferable when found, not mandatory.

**Double counting requires a well-defined multiplicity.** If objects are counted with varying multiplicity, the naive double count is wrong. The repair is to count a *weighted* set or to restrict to a canonical representative.

**Counting does not produce the objects.** A count proves existence (if positive) but gives no construction. For algorithmic purposes you need an unranking procedure, which is a separate problem.

**Asymptotics need more than exact counts.** Exact formulas can be useless for large $n$; you need estimates (→ Ch. 22).

## 7. Applications

- **Algorithm analysis.** Counting the number of operations of an algorithm is double counting over loop iterations; the analysis of sorting networks and hash tables is combinatorial counting.
- **Statistical mechanics.** Counting microstates is the definition of entropy; the combinatorics of configurations determines thermodynamic quantities.
- **Information theory.** Counting codewords and error patterns gives the sphere-packing bound; the entire subject is combinatorial counting with a metric.
- **Population genetics.** Counting genotypes and allele configurations under Mendelian inheritance is a bijection problem.
- **Computer science.** Unranking (mapping an index to the $k$-th object) is the inverse bijection, used in random sampling and combinatorial testing.
- **Finance.** Counting paths in a binomial tree (and their probabilities) is the combinatorial core of option pricing.

## 8. Mastery Criteria

You have this chapter when you can:

1. Given a combinatorial identity, identify the set that both sides count, or explain why no such set is apparent.
2. Construct a bijection and verify both directions explicitly.
3. Choose the right relation for a double count, and prove the multiplicity is uniform.
4. Use inclusion–exclusion correctly, including the sign pattern and the truncation.
5. Use a positive count to prove existence, and say what the count does and does not deliver.
6. Sanity-check any counting formula on small cases before trusting it.

**Diagnostic question.** "Prove this identity." A learner who reaches for algebra first is not yet thinking combinatorially. A learner who asks "what does each side count?" has the principle.

### AI Tutor Brief

- **Generate:** (i) identities with a clean bijective proof and identities that resist one; (ii) double-counting problems where the relation must be discovered; (iii) overcounting traps (circular arrangements, identical objects, symmetry); (iv) existence-by-counting problems; (v) inclusion–exclusion problems with a twist (at least one, exactly one, none).
- **Probe misconceptions:** treating "number of ways" as unambiguous; forgetting to divide by multiplicity; assuming a map is a bijection because it is injective; sign errors in inclusion–exclusion.
- **Transfer distance:** medium-high. Combinatorial reasoning is highly transferable; vary the objects (sets, graphs, strings, paths, partitions).
- **Do not** accept an algebraic verification when the task explicitly asks for a combinatorial proof. When the task says only "prove", accept either — but ask the learner which one explains *why* the identity holds.

---

# Chapter 13 — Pigeonhole and Density Arguments

## 1. Core Idea

**Pigeonhole principle.** If $n$ objects are placed into $m$ boxes with $n > m$, some box contains at least two objects. More generally, some box contains at least $\lceil n/m \rceil$ objects.

The principle is trivial to prove and hard to apply, because the entire difficulty lies in **choosing the boxes**. Nothing in the statement tells you what the boxes are; the boxes are a construction you must invent, and the correct choice is usually dictated by the quantity you want to force.

**Density version.** If a subset of a space is large enough relative to the space's structure, it must contain a prescribed configuration. Pigeonhole is the finite, crude version of this idea; the sophisticated versions (Szemerédi's theorem, Ramsey theory) are its descendants.

**Principle signature.** The problem asks you to prove the *existence* of two objects that are close, equal in some respect, or related in a prescribed way, and the hypothesis gives you more objects than "slots".

## 2. First Principles

**Why it works.** If every box contained at most $k$ objects, the total would be at most $km < n$. Contradiction. The proof is a one-liner; the content is entirely in the identification of objects and boxes.

**Where boxes come from.** The boxes are almost always a partition of a domain by a *structure*, not an arbitrary grouping:

| To force | Partition the domain by |
|---|---|
| Two numbers congruent mod $m$ | Residue classes mod $m$ |
| Two numbers close together | Intervals of length $\delta$ |
| Two numbers with the same sign pattern | The $2^k$ sign patterns of $k$ quantities |
| Two objects with the same "profile" | The possible profiles (e.g. degree, length, sum) |
| Two of a pair from a fixed pairing | The pairs themselves |
| A repeated state in a process | The finite state space |

**The continuous version.** If $N+1$ real numbers lie in $[0,1)$, two of them differ by less than $1/N$: partition $[0,1)$ into $N$ intervals of length $1/N$. This is how pigeonhole produces *approximation* results (Demonstration 13.3), and it is the finite seed of compactness arguments.

**Density versus counting.** Counting arguments say "there are many objects"; density arguments say "the objects are spread out, so some region must be crowded". The second is stronger when the structure of the space matters, and it is the right frame for extremal problems (→ Ch. 11).

## 3. Reasoning Process

1. **Identify what must be forced.** Two objects with equal residue? Two within distance $\delta$? A repeated value? A monochromatic structure?
2. **Identify the objects** (the pigeons). These are usually the $n+1$ items the hypothesis gives you.
3. **Invent the boxes** so that *being in the same box implies the desired conclusion*. This is the creative step; work backwards from the conclusion.
4. **Count.** Show #objects > #boxes. If not, refine the boxes or use a sharper version ($\lceil n/m\rceil$).
5. **Extract the conclusion** and check that it is exactly what was asked — pigeonhole often gives you "at least two", when you need "two with an additional property".
6. **If pigeonhole is too crude**, upgrade to a *weighted* or *structural* argument: assign capacities to boxes, or use a partition adapted to the geometry.

## 4. Demonstrations

### Demonstration 13.1 — Choosing the boxes: coprime pairs

*Problem.* Prove that among any $n+1$ integers chosen from $\{1,2,\dots,2n\}$, two are coprime.

*Objects:* the $n+1$ chosen integers. *Desired conclusion:* two consecutive integers (since consecutive integers are coprime).

*Boxes:* the $n$ pairs $\{1,2\}, \{3,4\}, \dots, \{2n-1,2n\}$.

*Count:* $n+1$ objects in $n$ boxes, so some box contains both of its elements. Those two are consecutive, hence coprime. $\blacksquare$

**What to notice.** The boxes were chosen by working backwards from the conclusion: "coprime" is hard to force directly, but "consecutive" is easy, and consecutive implies coprime. **The pigeonhole conclusion is usually weaker than the target, and the skill is to choose boxes whose collision implies the target.**

Also notice that the bound is sharp: the $n$ even numbers $2,4,\dots,2n$ are all in the set, any two of them share the factor $2$, and so there is no coprime pair among them. Hence $n$ objects are genuinely insufficient, and the pigeonhole argument is tight.

### Demonstration 13.2 — Pigeonhole with a *constructed* profile

*Theorem (Erdős–Szekeres).* Every sequence of $(r-1)(s-1)+1$ distinct real numbers contains an increasing subsequence of length $r$ or a decreasing subsequence of length $s$.

*Proof.* Let the sequence be $a_1,\dots,a_N$ with $N = (r-1)(s-1)+1$. For each $i$, let
$$I_i = \text{length of the longest increasing subsequence ending at } a_i,$$
$$D_i = \text{length of the longest decreasing subsequence ending at } a_i.$$

*Key claim:* the pairs $(I_i, D_i)$ are all distinct.

Indeed, suppose $i < j$. If $a_i < a_j$, then an increasing subsequence of length $I_i$ ending at $a_i$ can be extended by $a_j$, so $I_j \ge I_i + 1 > I_i$. If $a_i > a_j$, then similarly $D_j \ge D_i + 1 > D_i$. Either way, $(I_i,D_i) \ne (I_j,D_j)$.

Now suppose, for contradiction, that there is no increasing subsequence of length $r$ and no decreasing subsequence of length $s$. Then $1 \le I_i \le r-1$ and $1 \le D_i \le s-1$ for all $i$, so there are at most $(r-1)(s-1)$ possible pairs. But we have $N = (r-1)(s-1)+1$ distinct pairs. Pigeonhole gives a contradiction. $\blacksquare$

**What to notice.** The "boxes" here are pairs of integers, and they are not given by the problem — they are *manufactured* from the sequence. This is the deepest form of pigeonhole: **invent a profile function whose collisions are impossible, then count the profiles.** The same technique proves that any sequence of $n^2+1$ distinct reals has a monotone subsequence of length $n+1$, and it is the prototype for many results in extremal combinatorics.

### Demonstration 13.3 — The continuous version: Dirichlet approximation

*Theorem.* Let $\alpha$ be irrational and $N \ge 1$ an integer. Then there exist integers $p$ and $q$ with $1 \le q \le N$ such that
$$\left|\alpha - \frac{p}{q}\right| < \frac{1}{qN}.$$

*Proof.* Consider the $N+1$ fractional parts $\{k\alpha\}$ for $k = 0,1,\dots,N$. Each lies in $[0,1)$. Partition $[0,1)$ into $N$ intervals $[j/N, (j+1)/N)$ for $j = 0,\dots,N-1$. By pigeonhole, two of the $N+1$ numbers lie in the same interval: there are $0 \le i < j \le N$ with
$$|\{j\alpha\} - \{i\alpha\}| < \frac{1}{N}.$$
Let $q = j - i \in [1,N]$. Since $\{j\alpha\} - \{i\alpha\} = (j-i)\alpha - m$ for some integer $m$ (the fractional parts differ by an integer multiple adjustment), we get $|q\alpha - m| < 1/N$. Dividing by $q$,
$$\left|\alpha - \frac{m}{q}\right| < \frac{1}{qN}. \qquad \blacksquare$$

**What to notice.** Three features make this the model continuous pigeonhole argument:

1. The objects are *real numbers in a bounded interval*, and the boxes are *intervals of equal length*. The partition is chosen so that "same box" means "close".
2. The conclusion is an **approximation**, not an equality. Pigeonhole gives you proximity, which is often all you need in analysis.
3. The irrationality of $\alpha$ is used to ensure the fractional parts are distinct, so the inequality is strict. (If $\alpha$ is rational, the argument still gives a bound, but the interesting content is the irrational case.)

This is the seed of the theory of Diophantine approximation: iterating the argument and refining it yields infinitely many good rational approximations, and the continued fraction expansion gives the best ones (→ Ch. 15, 22).

## 5. Connections

- **← Ch. 4.** Pigeonhole is proved by contradiction; the "boxes" are a partition, which is a decomposition (→ Ch. 14).
- **← Ch. 12.** Pigeonhole is a counting argument: the total capacity of the boxes is less than the number of objects.
- **→ Ch. 9.** The Ramsey argument in Demonstration 9.1 is pigeonhole plus symmetry.
- **→ Ch. 11.** Extremal arguments often need a pigeonhole step to produce the configuration that the extremality then constrains.
- **→ Ch. 21.** The probabilistic method is the quantitative refinement: instead of "some box has two", you get "the expected number is large".
- **→ Ch. 31.** Pigeonhole on a finite state space proves that a process must repeat a state, which is how cycles and eventual periodicity are detected.

## 6. Limitations

**The boxes must be a partition.** Overlapping boxes break the count. If boxes overlap, an object may be in several, and the capacity argument fails.

**Pigeonhole gives existence, not identification.** It tells you *some* pair exists, never which. For constructive purposes you need an algorithm (often a search or a greedy procedure).

**The bound may be far from sharp.** Pigeonhole typically gives a crude threshold. Improving it usually requires a structural argument (Ramsey theory, density results), not a better partition.

**Infinite versions require care.** "Infinitely many objects in finitely many boxes" gives a box with infinitely many, which is valid, but "infinitely many boxes" gives nothing. Compactness arguments are the correct infinite generalization.

**Choosing boxes is not algorithmic.** There is no procedure for inventing the partition. The method is: work backwards from the conclusion, and look for the quantity whose equality or proximity is what you want to force.

## 7. Applications

- **Hashing and collisions.** Any hash function mapping more keys than buckets has collisions; pigeonhole is the reason perfect hashing requires as many buckets as keys.
- **Data compression.** No lossless compressor can shorten every message: there are more long strings than short ones, so some must expand.
- **Number theory.** Residue-class arguments (two of $n+1$ numbers are congruent mod $n$) are pigeonhole, and they underlie the pigeonhole proofs of Fermat's little theorem and the periodicity of decimal expansions.
- **Scheduling.** With more jobs than time slots, some slot must be overloaded; capacity arguments are pigeonhole with weights.
- **Genetics.** With more individuals than genotypes, some genotype repeats; this is the basis of the pigeonhole argument for the existence of identical twins in a large enough population.
- **Analysis.** The Bolzano–Weierstrass theorem (every bounded sequence has a convergent subsequence) is the continuous descendant of the interval partition.

## 8. Mastery Criteria

You have this chapter when you can:

1. State what must be forced, and construct boxes whose collision implies it.
2. Recognize the standard box constructions: residues, intervals, sign patterns, profiles, pairs.
3. Use the sharpened form ($\lceil n/m\rceil$) when two objects are not enough.
4. Apply the continuous version to obtain approximation results.
5. Invent a profile function whose distinctness is provable, as in Demonstration 13.2.
6. Explain why pigeonhole gives existence but not construction, and say what additional work a constructive answer needs.

**Diagnostic question.** "Prove that among any $n+1$ of these objects, two are related." A learner who says "pigeonhole" without naming the boxes has not solved anything. A learner who says "partition by the residue of the sum mod $n$" has.

### AI Tutor Brief

- **Generate:** (i) problems requiring a non-obvious partition (residues, intervals, profiles); (ii) problems where the naive partition gives the wrong threshold; (iii) continuous pigeonhole problems producing approximation bounds; (iv) problems where pigeonhole is insufficient and a structural argument is needed.
- **Probe misconceptions:** overlapping boxes; forgetting to prove the boxes partition the objects; using pigeonhole to claim a *specific* pair exists; applying the finite version to infinite sets without care.
- **Transfer distance:** high. The signature (more objects than slots) appears everywhere; test in number theory, geometry, combinatorics, and analysis.
- **Do not** accept "by pigeonhole" as an explanation. Require the objects, the boxes, the count, and the implication.

---

# Chapter 14 — Decomposition and Canonical Form

## 1. Core Idea

Two linked techniques for making a hard object tractable:

- **Decomposition.** Partition the problem into parts that are *exhaustive* (every case is covered), *independent* (the parts can be solved separately), and *simpler* (each part is easier than the whole). Then solve each part and reassemble.
- **Canonical form.** Within each equivalence class of objects, choose a unique representative with a recognizable structure. Then "is there an object with property $P$?" becomes "does its canonical form have property $P$?", and "how many objects?" becomes "how many canonical forms?".

Decomposition answers *where to split*; canonical form answers *what to compare*. Together they are the reason finite mathematics is possible: without canonical forms, you cannot tell whether two objects are the same, and without decomposition, you cannot enumerate.

**Principle signature.** The problem involves a classification, a count of "essentially different" objects, an algorithm that must terminate in a normal state, or a proof whose cases are naturally suggested by a residue, a sign, an ordering, or a degeneracy.

## 2. First Principles

**Partitions come from equivalence relations.** A decomposition is a partition of the object set into classes. The partition is *valid* if the classes are disjoint and their union is everything — and the second condition is the one that is usually left unproved. "Case 1: $n$ even. Case 2: $n$ odd." is valid because every integer is one or the other. "Case 1: the triangle is acute. Case 2: the triangle is obtuse." is **invalid** — it omits right triangles.

**Canonical form requires a reduction and a uniqueness proof.** A canonical form is a function $c$ from objects to objects such that (i) $c(x) \sim x$ (the reduction preserves the equivalence class), (ii) $c(c(x)) = c(x)$ (idempotence), and (iii) $c(x) = c(y)$ whenever $x \sim y$ (uniqueness). The third condition is what makes comparison meaningful, and it is the one that needs proof.

**Examples of canonical forms.** Lowest terms for rationals; reduced row echelon form for matrices; cycle decomposition for permutations; prime factorization for integers; sorted order for multisets; disjunctive normal form for Boolean formulas; the Jordan form for matrices. Each one converts a *class* of equivalent descriptions into a single *object*.

**Divide and conquer.** A decomposition that splits the input into independent subproblems of the same type, solves them recursively, and merges the results. The correctness proof is structural induction (→ Ch. 10); the cost analysis is a recurrence (→ Ch. 22).

**Independence is the multiplier.** If the parts are independent, the number of combined configurations is the *product* of the counts (→ Ch. 12). If they interact, the product is wrong, and the decomposition must be refined until independence holds — this is the origin of most inclusion–exclusion arguments.

## 3. Reasoning Process

1. **Find the splitting variable.** Which feature changes the structure qualitatively? Sign, residue, parity, ordering, degeneracy, dimension, connectivity.
2. **Prove exhaustiveness.** For every object, at least one case applies. This is a one-line argument that is omitted in most incorrect solutions.
3. **Check independence.** Do the cases overlap? If an object can be in two cases, you will double count; refine or use inclusion–exclusion.
4. **Solve each case.** Each should be strictly easier; if a case is as hard as the original, the split was wrong.
5. **Reassemble.** Combine the case results, respecting any interactions.
6. **For canonical forms: define the reduction, prove it preserves the class, prove uniqueness, then use it.** The uniqueness proof is where the mathematics is.

## 4. Demonstrations

### Demonstration 14.1 — A decomposition that must be exhaustive

*Claim.* For every integer $n$, $12 \mid n^2(n^2-1)$.

*Proof.* Factor: $n^2(n^2-1) = n^2(n-1)(n+1) = (n-1)\,n\cdot n\,(n+1)$.

*Divisibility by $3$:* among the three consecutive integers $n-1, n, n+1$, exactly one is divisible by $3$. Hence $3 \mid n(n-1)(n+1) \mid n^2(n^2-1)$.

*Divisibility by $4$:* split on the parity of $n$.

- If $n$ is even, then $4 \mid n^2$.
- If $n$ is odd, then $n-1$ and $n+1$ are consecutive even numbers, so one is divisible by $2$ and the other by $4$; hence $8 \mid (n-1)(n+1)$, and in particular $4 \mid (n-1)(n+1)$.

Either way, $4 \mid n^2(n^2-1)$.

Since $\gcd(3,4) = 1$ and both divide the number, $12$ divides it. $\blacksquare$

**What to notice.** The two decompositions are on *different variables* — one on the residue mod $3$, one on parity. This is normal: a problem may need several independent decompositions, and each must be exhaustive on its own. Note also that the parity split is exhaustive by construction (even/odd), while the mod-3 argument is not a case split at all but a *counting* observation. **Choose the decomposition that makes each piece trivial; there is no requirement to use the same split everywhere.**

### Demonstration 14.2 — Canonical form: cycle decomposition

*Construction.* Every permutation $\sigma$ of $\{1,\dots,n\}$ decomposes uniquely into disjoint cycles: start at any $x$, iterate $\sigma$ until it returns to $x$; that is one cycle. Repeat on the remaining elements. The result is a partition of $\{1,\dots,n\}$ into cycles, unique up to the order in which cycles are listed and the starting point within each cycle.

*Canonical form.* Write each cycle starting from its smallest element, and list cycles in increasing order of their smallest elements. This gives a unique representative for each permutation.

*Application.* The **order** of $\sigma$ (the least $k>0$ with $\sigma^k = \mathrm{id}$) is the least common multiple of its cycle lengths. Proof: $\sigma^k$ fixes a point iff $k$ is a multiple of the length of the cycle containing it; so $\sigma^k = \mathrm{id}$ iff $k$ is a common multiple of all cycle lengths.

*Consequence.* In $S_5$, the possible orders are the lcm's of the partitions of $5$:

| Cycle type | lcm |
|---|---|
| $5$ | $5$ |
| $4+1$ | $4$ |
| $3+2$ | $6$ |
| $3+1+1$ | $3$ |
| $2+2+1$ | $2$ |
| $2+1+1+1$ | $2$ |
| $1+1+1+1+1$ | $1$ |

So the maximum order of an element of $S_5$ is $6$.

**What to notice.** The canonical form (cycle type) converted a question about *permutations* into a question about *integer partitions*, which is a finite and easily enumerated set. This is the archetypal use of canonical form: **transport the problem to the classification of invariants.** The invariant here is the multiset of cycle lengths; the canonical form makes it visible and comparable.

### Demonstration 14.3 — Canonical form via long division

*Claim.* Every rational number has a decimal expansion that is eventually periodic.

*Proof.* Let $r = a/b$ in lowest terms with $b > 0$. Perform long division: at each step, the remainder $\rho_k$ satisfies $0 \le \rho_k < b$, and the next remainder is determined by $\rho_{k+1} = 10\rho_k \bmod b$. There are only $b$ possible remainders, so among $\rho_1,\dots,\rho_{b+1}$ two are equal, say $\rho_i = \rho_j$ with $i<j$. From that point the sequence of remainders — and hence the sequence of digits — repeats with period $j-i$. $\blacksquare$

*Worked instance.* $1/7$: remainders $1,3,2,6,4,5,1,\dots$, so the period is $6$ and $1/7 = 0.\overline{142857}$. The period is the multiplicative order of $10$ modulo $7$, which is $6$ since $10^k \not\equiv 1 \pmod 7$ for $k=1,\dots,5$ and $10^6 \equiv 1$.

**What to notice.** The pigeonhole step (→ Ch. 13) guarantees a repeat; the *canonical form* is the repeating block, and the *period* is an invariant of the rational. This is a case where a canonical form is not just a convenience but the object of study: the eventual period is a number-theoretic invariant of $b$, and understanding it is a research question (the period of $1/p$ for prime $p$ is the order of $10$ mod $p$, which is conjecturally related to deep questions about primes).

## 5. Connections

- **← Ch. 2.** Well-definedness is the prerequisite for canonical forms; a canonical form is a well-defined choice of representative.
- **← Ch. 5.** Canonical forms are quotients made computable.
- **← Ch. 12.** Counting canonical forms is how you count objects up to equivalence; independence is what makes the counts multiply.
- **→ Ch. 15.** A canonical form is a change of representation; the transformation chapter generalizes the idea.
- **→ Ch. 22.** Divide-and-conquer decompositions produce recurrences, whose asymptotics are the subject of Chapter 22.
- **→ Ch. 32.** Case analysis is the decomposition used to *find* counterexamples: enumerate the cases, and look for the one where the theorem fails.

## 6. Limitations

**Non-exhaustive casework is the most common fatal error.** Always prove that the cases cover everything, including the degenerate and boundary cases (right triangles, zero, empty set, $n=1$).

**Canonical forms can be expensive to compute.** A canonical form that exists in principle may be intractable in practice (graph isomorphism is the canonical example). Existence of a canonical form is not the same as an efficient algorithm for it.

**Decomposition can create interaction.** Splitting a problem into parts that are not independent produces double counting or missing cases. The repair is usually inclusion–exclusion or a more refined split.

**Choosing the wrong split wastes the most time of any error.** A split that produces cases as hard as the original is a signal to change the splitting variable, not to try harder.

**Canonical forms can hide structure.** Reducing a matrix to echelon form loses the geometric information in the original columns. Choose the canonical form that preserves the properties you need (→ Ch. 5, limitations).

## 7. Applications

- **Databases and normalization.** Canonical forms (normal forms) remove redundancy and make comparison and query optimization possible.
- **Compilers.** Abstract syntax trees, SSA form, and normal forms are canonical representations that make optimization passes correct and composable.
- **Algebra and number theory.** Prime factorization, Smith normal form, and Jordan form are canonical forms that classify objects up to isomorphism.
- **Probability.** Partitioning a sample space by the value of a random variable is a decomposition; the law of total probability is the reassembly step.
- **Engineering.** Failure mode and effects analysis is a decomposition; the requirement that it be exhaustive is exactly the exhaustiveness condition.
- **Operations research.** Branch and bound is decomposition plus bounding; the branching variable is the splitting variable.

## 8. Mastery Criteria

You have this chapter when you can:

1. Choose a splitting variable that makes each case strictly easier, and prove exhaustiveness.
2. Detect overlapping cases and repair them with refinement or inclusion–exclusion.
3. Define a canonical form, prove it preserves the equivalence class, and prove uniqueness.
4. Use a canonical form to count objects up to equivalence.
5. Recognize when a canonical form destroys information you need, and choose a different one.
6. Analyze a divide-and-conquer algorithm's correctness by structural induction.

**Diagnostic question.** "Your proof has two cases. Prove there are no others." A learner who can do this routinely has internalized the discipline. A learner who says "those are the only possibilities" without argument has not.

### AI Tutor Brief

- **Generate:** (i) classification problems requiring exhaustive casework with a degenerate case; (ii) counting-up-to-equivalence problems requiring a canonical form; (iii) problems where a natural split creates overlap; (iv) problems where the right canonical form is non-obvious (cycle type, normal form, reduced fraction).
- **Probe misconceptions:** "even/odd" or "acute/obtuse" splits that omit a case; assuming a canonical form is unique without proof; forgetting the degenerate case ($n=0$, empty, collinear, zero-length).
- **Transfer distance:** medium-high. Test canonical forms in algebra, combinatorics, and algorithms.
- **Do not** accept a case split without an exhaustiveness argument. Require the uniqueness proof for any canonical form.

---

# Chapter 15 — Transformation: Changing the Representation

## 1. Core Idea

A **transformation** replaces a problem by an equivalent problem in a different representation, chosen so that the structure becomes transparent. The problem does not change; the *coordinates* change.

Standard transformations:

| Awkward feature | Transformation |
|---|---|
| A sum you cannot evaluate | Generating function; telescoping; pairing |
| A product or power | Logarithms; roots of unity |
| A constraint coupling variables | Substitution (e.g. $u = x + 1/x$, $x = a+b$, $y = a-b$) |
| A geometric relation | Coordinates; vectors; complex numbers; inversion |
| A recurrence | Generating function; matrix power; characteristic equation |
| A divisibility condition | Modular arithmetic; $p$-adic valuation |
| A "for all" statement | Complement; contrapositive (→ Ch. 3) |
| A counting problem | Bijection to a known family (→ Ch. 12) |
| A hard primal problem | Dual problem (→ Ch. 19, 20) |

**Principle signature.** The problem is *almost* easy: one operation, one constraint, or one object type is resisting, and everything else is straightforward. The resistance usually indicates that you are in the wrong representation.

## 2. First Principles

**A transformation must be reversible, or its information loss must be tracked.** If $T$ is a bijection between problem instances, then solving $T(P)$ solves $P$ exactly. If $T$ is not injective (squaring, taking absolute values, dropping the imaginary part), then solutions of $T(P)$ may not be solutions of $P$, and a verification pass is mandatory (→ Ch. 3, Demonstration 3.3).

**A transformation must preserve the goal.** If the goal is "find the maximum", the transformation must preserve order, or at least map maxima to maxima. A transformation that scrambles the objective is worse than useless.

**Representations are not neutral.** Each representation makes some things easy and others hard:

- **Coordinates** make incidence and distance algebraic, but destroy symmetry.
- **Synthetic geometry** makes symmetry and incidence visible, but resists computation.
- **Generating functions** make convolution into multiplication, but make positivity invisible.
- **Modular arithmetic** makes divisibility decidable, but discards magnitude.

The skill is choosing the representation whose *easy* operations are the ones the problem needs.

**The transform-and-solve cycle.** Transform, solve, transform back, then **verify against the original**. The verification step is not optional, because the transformation may have introduced spurious solutions or lost constraints.

## 3. Reasoning Process

1. **Locate the resistance.** Which step of the obvious approach is hard? A sum, a product, a nonlinearity, a constraint, a repeated operation?
2. **Pick the representation that trivializes that step.** Use the table above; if the resistance is a sum, think generating function or telescoping; if it is a product, think logs; if it is a coupling, think substitution.
3. **Check reversibility.** Is the transformation injective on the relevant domain? If not, record exactly what is lost.
4. **Transform the goal, not just the data.** Write down what the goal becomes in the new representation. If it becomes unrecognizable, the transformation is wrong.
5. **Solve in the new representation.**
6. **Transform back, and verify.** Substitute into the original; check boundary cases; discard spurious solutions.

## 4. Demonstrations

### Demonstration 15.1 — Substitution that reveals structure

*Problem.* Solve $x^4 + x^3 + x^2 + x + 1 = 0$ over the reals.

*Observation.* The polynomial is **reciprocal**: the coefficient list reads the same forwards and backwards. Such polynomials are invariant under $x \mapsto 1/x$, which suggests the substitution $u = x + 1/x$.

*Transformation.* Since $x = 0$ is not a root, divide by $x^2$:
$$x^2 + x + 1 + \frac1x + \frac1{x^2} = 0 \implies \left(x^2 + \frac{1}{x^2}\right) + \left(x + \frac1x\right) + 1 = 0.$$
Now $x^2 + 1/x^2 = u^2 - 2$, so the equation becomes
$$(u^2-2) + u + 1 = 0 \implies u^2 + u - 1 = 0 \implies u = \frac{-1 \pm \sqrt5}{2}.$$

*Return.* We need real $x$ with $x + 1/x = u$. But for real $x \ne 0$, $|x + 1/x| \ge 2$ (AM–GM, → Ch. 6), whereas $|u| = \left|\frac{-1\pm\sqrt5}{2}\right| \approx 0.618$ or $1.618$, both $< 2$. So there are no real solutions.

*Cross-check.* The roots of $x^4+x^3+x^2+x+1$ are the primitive fifth roots of unity $e^{2\pi i k/5}$, $k=1,2,3,4$ — none real. ✓

**What to notice.** The substitution did three things at once: it halved the degree, it exposed the symmetry $x \leftrightarrow 1/x$, and it converted the question "are there real roots?" into a question about the *range* of $x + 1/x$. That last step is the crucial one: the transformed equation had solutions, but they were not in the range of the transformation. **A transformation's image matters as much as its formula** — this is where spurious solutions come from, and why step 6 of the Reasoning Process is mandatory.

### Demonstration 15.2 — Generating functions: recurrence becomes algebra

*Problem.* Let $a_n$ be the number of compositions of $n$ into parts $1$ and $2$. Find a closed form.

*Step 1: recurrence.* From Demonstration 12.4, $a_n = a_{n-1} + a_{n-2}$ with $a_0 = 1$, $a_1 = 1$.

*Step 2: transform.* Let $A(x) = \sum_{n\ge0} a_n x^n$. Then
$$A(x) = a_0 + a_1 x + \sum_{n\ge2}(a_{n-1}+a_{n-2})x^n = 1 + x + x\sum_{n\ge2}a_{n-1}x^{n-1} + x^2\sum_{n\ge2}a_{n-2}x^{n-2}.$$
The two sums are $A(x) - a_0 = A(x)-1$ and $A(x)$ respectively, so
$$A(x) = 1 + x + x(A(x)-1) + x^2A(x) \implies A(x)\,(1 - x - x^2) = 1 \implies A(x) = \frac{1}{1-x-x^2}.$$

*Step 3: solve.* Partial fractions with $1-x-x^2 = (1-\varphi x)(1-\psi x)$, where $\varphi = \frac{1+\sqrt5}{2}$ and $\psi = \frac{1-\sqrt5}{2}$ (note $\varphi\psi = -1$, $\varphi+\psi = 1$), give
$$A(x) = \frac{1}{\sqrt5}\left(\frac{\varphi}{1-\varphi x} - \frac{\psi}{1-\psi x}\right) \implies a_n = \frac{\varphi^{n+1} - \psi^{n+1}}{\sqrt5} = F_{n+1}.$$

*Step 4: verify.* $a_0 = (\varphi - \psi)/\sqrt5 = 1$ ✓; $a_1 = (\varphi^2-\psi^2)/\sqrt5 = (\varphi-\psi)(\varphi+\psi)/\sqrt5 = 1$ ✓; $a_2 = 2$ (compositions $1+1$ and $2$) ✓.

**What to notice.** The transformation converted a *recursive* description into an *algebraic equation* for a single object $A(x)$, and the algebra is mechanical. The price: the coefficients must be extracted, which requires partial fractions and the roots of the denominator. **Generating functions are the standard tool when a problem has a convolution or a linear recurrence**, because multiplication of series is convolution of coefficients (→ Ch. 12, 22).

### Demonstration 15.3 — Coordinates make a geometric theorem algebraic

*Claim.* The three medians of a triangle are concurrent, and they meet at a point that divides each median in the ratio $2:1$.

*Transformation.* Place the triangle in a vector space: let the vertices have position vectors $\mathbf a, \mathbf b, \mathbf c$. Medians and ratios are affine notions, so they are preserved by the translation that sends one vertex to the origin; we may compute with vectors freely.

*Computation.* The midpoint of $BC$ is $\mathbf m_a = \frac{\mathbf b + \mathbf c}{2}$. The median from $A$ is the segment from $\mathbf a$ to $\mathbf m_a$. Let
$$\mathbf g = \frac{\mathbf a + \mathbf b + \mathbf c}{3}.$$
Then
$$\mathbf g = \mathbf a + \frac23\left(\mathbf m_a - \mathbf a\right),$$
because $\mathbf a + \frac23\left(\frac{\mathbf b+\mathbf c}{2} - \mathbf a\right) = \mathbf a - \frac23\mathbf a + \frac13(\mathbf b+\mathbf c) = \frac13(\mathbf a+\mathbf b+\mathbf c)$. ✓

So $\mathbf g$ lies on the median from $A$, two-thirds of the way from $A$ to the midpoint of $BC$. By the same computation (which is symmetric in $\mathbf a, \mathbf b, \mathbf c$), $\mathbf g$ lies on all three medians, at the same ratio. Hence the medians are concurrent at $\mathbf g$. $\blacksquare$

**What to notice.** The vector representation converted a statement about *lines meeting* into a statement about *an affine combination*, and the symmetry of the expression $\frac13(\mathbf a+\mathbf b+\mathbf c)$ made the concurrency automatic. This is the characteristic advantage of coordinates: **it turns "prove these objects coincide" into "prove these expressions are equal", which is mechanical.** The cost is that you lose the synthetic insight into *why* the point is where it is — but for concurrency, the algebraic proof is shorter and less error-prone.

## 5. Connections

- **← Ch. 3.** Non-reversible transformations require a verification pass; this chapter is the practical form of that warning.
- **← Ch. 5.** A transformation is a change of structure-preserving representation; a canonical form is a transformation to a standard representative.
- **← Ch. 12.** Bijections are transformations of counting problems.
- **→ Ch. 19.** Isomorphism and duality are the structural versions of transformation.
- **→ Ch. 22.** Asymptotic transformations (logs, rescaling) are how you compare growth rates.
- **→ Ch. 23.** The unity of mathematics is the claim that the right transformation usually exists; this chapter is the technique.

## 6. Limitations

**Transformations can introduce spurious solutions.** Squaring, clearing denominators, and applying non-injective functions all enlarge the solution set. Always verify in the original representation.

**Transformations can lose solutions.** Dividing by an expression that may be zero, or restricting to a subset of the range, can discard valid solutions. Check the excluded cases.

**The transformed problem may be harder.** A transformation that makes one step easy can make another step impossible. Generating functions make recurrences easy and coefficient extraction hard; coordinates make incidence easy and symmetry invisible.

**Not every problem has a good transformation.** Some problems are genuinely about the original representation, and searching for a transformation wastes time. Set a budget: if no natural transformation appears in ten minutes, solve in the original representation.

**The transformation must be *natural* to generalize.** A transformation invented for one problem often fails on the next. The ones worth learning are the ones attached to a structure: reciprocity, convolution, symmetry, duality.

## 7. Applications

- **Signal processing.** The Fourier transform converts convolution into multiplication; the Laplace transform converts differential equations into algebra. Both are transformations chosen to make a hard operation easy.
- **Probability.** The characteristic function is the Fourier transform of a distribution; sums of independent variables become products.
- **Control theory.** The Laplace domain turns stability questions into pole locations.
- **Computer graphics.** Homogeneous coordinates turn translation into a linear map, which is why the whole pipeline is matrix multiplication.
- **Machine learning.** Kernel methods transform data into a feature space where a nonlinear problem becomes linear.
- **Finance.** The risk-neutral measure is a change of representation under which pricing becomes an expectation; the transform is the content of the fundamental theorem of asset pricing.

## 8. Mastery Criteria

You have this chapter when you can:

1. Identify the resisting step in an approach and name a representation that would trivialize it.
2. Choose a substitution that exploits a visible symmetry (reciprocal, homogeneous, translational).
3. Set up and solve a generating function for a linear recurrence, and verify the first few coefficients.
4. Use coordinates or vectors to convert a geometric statement into algebra, and check the result against a special case.
5. Track what a non-injective transformation loses, and perform the verification pass.
6. Say what each representation makes easy and what it makes hard.

**Diagnostic question.** "This problem is hard in its current form. What representation would make it easy, and what would it cost?" A learner who can answer both halves has the principle.

### AI Tutor Brief

- **Generate:** (i) problems with a hidden symmetry that a substitution exposes; (ii) recurrence-to-generating-function problems; (iii) geometry problems where coordinates are dramatically shorter than synthetic proofs; (iv) problems where a tempting transformation introduces spurious solutions, to test verification discipline.
- **Probe misconceptions:** forgetting to verify after a non-injective step; transforming the data but not the goal; believing a transformation is free; ignoring the range/image of a substitution.
- **Transfer distance:** high. Transformations are the most domain-portable technique in the guide.
- **Do not** accept a transformed solution without the back-substitution check and the boundary-case check.

---

# Chapter 16 — Constructive Reasoning and the Algorithmic Stance

## 1. Core Idea

The **algorithmic stance** is the habit of asking, of every existence claim: *can I produce the object, and at what cost?*

A constructive proof delivers more than a non-constructive one: it delivers a **procedure**. That procedure can be run, tested, and composed. In exchange, constructive proofs are usually harder, and some true statements have no known constructive proof.

The stance also imports a new obligation that pure existence proofs ignore: **termination and correctness must be proved**, and **cost matters**. An existence proof that requires $10^{100}$ steps is, for practical purposes, no proof at all.

**Principle signature.** The problem says "find", "construct", "give an example", "describe an algorithm", or "show how to"; or you have a non-constructive existence proof and want to know whether it can be made effective.

## 2. First Principles

**Correctness = invariant + termination.** To prove an algorithm correct:

1. State a **loop invariant** $I$: a property true before and after every iteration.
2. Prove **initialization**: $I$ holds before the first iteration.
3. Prove **preservation**: if $I$ holds and the loop body executes, $I$ holds afterward.
4. Prove **termination**: a monovariant decreases and is bounded below (→ Ch. 8).
5. Prove **exit condition implies the goal**: when the loop stops, $I$ plus the stopping condition gives the answer.

This is the algorithmic form of induction, and it is the only reliable way to prove an algorithm correct. Testing is not proof: a program can pass every test and fail on an untested input.

**Greedy algorithms need an exchange argument.** A greedy algorithm makes the locally best choice at each step. It is correct only if you can prove that some optimal solution contains the greedy choice — an **exchange argument**: take an optimal solution, replace its first choice with the greedy one, and show the result is still optimal (or better). Without this, greedy is a heuristic.

**Constructive existence from recursion.** Many existence proofs are naturally recursive: to build an object of size $n$, build one of size $n-1$ and extend it. The correctness proof is structural induction; the cost analysis is a recurrence.

**Non-constructive existence is not a failure.** Sometimes the guarantee is all you need (e.g. "a solution exists, so the search will not run forever"). But you should always know *which kind* of proof you have, because the two deliver different things (→ Ch. 4).

## 3. Reasoning Process

1. **Decide what kind of existence you need.** A guarantee, a witness, or an efficient procedure? The answer determines the standard of proof.
2. **Look for a recursive construction.** Can the object be built from a smaller one? What is the extension step?
3. **For an algorithm, write the invariant first.** What is true at every stage? Then write the loop. (Writing the invariant first is the single most effective habit in algorithm design.)
4. **Find the termination measure.** What decreases? Prove it is bounded below.
5. **For greedy, find the exchange.** Prove that the greedy choice can be part of an optimum. If you cannot, the greedy algorithm is probably wrong — look for a counterexample (→ Ch. 32).
6. **Analyze the cost.** Count the operations as a function of input size; identify the dominant term (→ Ch. 22).
7. **Test on the smallest cases and on adversarial cases.** Small cases catch base-case errors; adversarial cases catch greedy failures.

## 4. Demonstrations

### Demonstration 16.1 — Euclid's algorithm, proved correct

*Algorithm.* Given integers $a > b \ge 0$, while $b \ne 0$ replace $(a,b) \leftarrow (b,\ a \bmod b)$; return $a$.

*Invariant.* $I$: $\gcd(a,b)$ equals the gcd of the original pair.

*Initialization.* Trivially true.

*Preservation.* If $a = qb + r$ with $0 \le r < b$, then any common divisor of $a,b$ divides $r = a - qb$, and any common divisor of $b,r$ divides $a = qb + r$. So the sets of common divisors are equal, hence the gcds are equal. ✓

*Termination.* $b$ strictly decreases (since $r < b$) and is a non-negative integer. ✓

*Exit.* When $b = 0$, $\gcd(a,0) = a$, which by the invariant equals the original gcd. ✓

**What to notice.** The invariant is not "the answer is $a$" — that is only true at the end. The invariant is the *preserved relationship*, and the exit condition converts it into the answer. This separation is what makes the proof work, and it is the same separation that makes inductive proofs work (→ Ch. 10).

### Demonstration 16.2 — A constructive existence proof

*Claim.* Every integer $n \ge 1$ can be written as a sum of distinct powers of $2$.

*Constructive proof (recursive).* If $n = 1$, write $1 = 2^0$. If $n > 1$, let $2^k \le n < 2^{k+1}$ (such $k$ exists by well-ordering). Then $n - 2^k < 2^k \le n$, so $n - 2^k$ is a non-negative integer smaller than $n$; by induction it is a sum of distinct powers of $2$, all of them $\le 2^{k-1} < 2^k$. Adding $2^k$ gives a representation of $n$ as a sum of distinct powers of $2$. $\blacksquare$

*The procedure.* Repeatedly subtract the largest power of $2$ not exceeding the remainder. This terminates because the remainder strictly decreases.

*Uniqueness.* Suppose $n = \sum_{i\in S}2^i = \sum_{i\in T}2^i$ with $S \ne T$, and let $k$ be the largest index in the symmetric difference. WLOG $k \in S \setminus T$. Then the left side is at least $2^k$, while the right side is at most $\sum_{i<k}2^i = 2^k - 1 < 2^k$ — contradiction. Hence the representation is unique. $\blacksquare$

**What to notice.** The construction gives existence; the uniqueness proof is separate and uses a *maximality* argument (→ Ch. 11). Constructive existence proofs rarely give uniqueness for free, and the combination is what makes the binary representation a canonical form (→ Ch. 14).

### Demonstration 16.3 — When greedy fails, and why

*Problem.* Given coin denominations $\{1, 3, 4\}$, make change for $6$ using the fewest coins.

*Greedy.* Take the largest coin not exceeding the remainder: $4$, then remainder $2$; take $1$, remainder $1$; take $1$. Total: $4+1+1$, **three coins**.

*Optimal.* $3 + 3$, **two coins**.

*Diagnosis.* The greedy choice (take $4$) is not contained in any optimal solution. There is no exchange argument available, because replacing $3$ by $4$ in the optimal solution leaves $2$, which cannot be made with one coin.

**What to notice.** Greedy is correct exactly when the coin system has a **matroid-like exchange property**. For the US system $\{1,5,10,25\}$ (and for any system where each denomination is a multiple of the previous one), greedy is optimal, and the exchange argument is: if an optimal solution uses fewer than the maximum number of the largest coin, replacing smaller coins by one larger coin does not increase the count. For $\{1,3,4\}$, the exchange fails at the first step.

**The general lesson.** A greedy algorithm is a *conjecture* until you have an exchange argument. The counterexample is not an anomaly; it is the rule. Always test greedy on small cases with awkward denominations, weights, or orderings.

### Demonstration 16.4 — Non-constructive versus constructive, side by side

*Claim.* There exist two irrational numbers $x,y$ with $x^y$ rational.

- *Non-constructive proof:* Demonstration 4.2. Splits on whether $\sqrt2^{\sqrt2}$ is rational; in one branch it names the pair, in the other it does not.
- *Constructive proof:* take $x = \sqrt2$ and $y = 2\log_2 3$. Then $y$ is irrational (if $2\log_2 3 = p/q$ were rational, then $2^p = 3^q$, impossible by unique factorization), and
$$x^y = \left(\sqrt2\right)^{2\log_2 3} = 2^{\log_2 3} = 3,$$
which is rational. $\blacksquare$

**What to notice.** The constructive proof is *shorter* and gives an explicit pair. It also required a different idea (using logs to manufacture an irrational exponent). The non-constructive proof required only the law of excluded middle. **Neither is universally better**: the non-constructive proof is available in situations where no explicit construction is known, and it still establishes the theorem. But when you need an algorithm, only the constructive one will do.

## 5. Connections

- **← Ch. 8.** Invariant plus monovariant is the correctness template; this chapter applies it.
- **← Ch. 10.** Recursive constructions are structural induction; termination is descent.
- **← Ch. 11.** Greedy correctness is an exchange argument, which is extremal reasoning.
- **→ Ch. 20.** Optimization algorithms are greedy or exchange-based; the certificate of optimality is the exchange argument.
- **→ Ch. 22.** Cost analysis is asymptotic analysis of the operation count.
- **→ Ch. 28.** Numerical algorithms add a new failure mode: floating-point error. Correctness in exact arithmetic is not correctness in practice.

## 6. Limitations

**Constructive proofs can be much harder, or unknown.** Some existence theorems have no known constructive proof, and some have proofs that are constructive in principle but computationally infeasible. Insisting on constructivity can block progress.

**Correctness does not imply efficiency.** An algorithm that is provably correct but exponential is, for large inputs, useless. Both properties matter, and they are proved by different methods.

**The algorithmic stance can mislead in pure mathematics.** Asking "what is the algorithm?" is not always the right question; sometimes the structure is the point, and the algorithm is a distraction.

**Greedy heuristics are seductive.** A greedy algorithm that works on the examples you tried is not correct. Without an exchange argument, you have a conjecture.

**Termination proofs can be subtle.** A measure that decreases but is not bounded below (e.g. a real-valued measure approaching $0$) does not prove termination. Use integer-valued measures or well-founded orders.

## 7. Applications

- **Software engineering.** Correctness proofs, invariants, and complexity analysis are the professional core of the discipline.
- **Operations research.** Scheduling, routing, and packing are constructive optimization; greedy with exchange proofs (e.g. earliest deadline first) is the standard tool.
- **Cryptography.** Security reductions are constructive arguments: an attack on the protocol yields an algorithm for a hard problem.
- **Numerical analysis.** Iterative methods are algorithms with convergence proofs; the convergence rate is the cost analysis.
- **Machine learning.** Training algorithms are constructive optimizers; generalization is a separate, non-constructive guarantee.
- **Mathematics.** The constructivist program in logic takes the algorithmic stance to its limit, and its disagreements with classical mathematics are precisely about which existence proofs are acceptable.

## 8. Mastery Criteria

You have this chapter when you can:

1. Write a loop invariant, prove initialization, preservation, and termination, and derive the answer from the exit condition.
2. Convert a recursive existence proof into an explicit procedure.
3. State and use an exchange argument to justify a greedy algorithm.
4. Produce a counterexample to a plausible greedy algorithm.
5. Distinguish constructive from non-constructive existence in your own proofs, and say what each delivers.
6. Analyze the cost of a simple algorithm and identify its dominant term.

**Diagnostic question.** "You proved this exists. Now produce one, or explain precisely why you cannot." A learner who can convert the proof into a procedure, or explain the obstruction, has the stance.

### AI Tutor Brief

- **Generate:** (i) algorithm-correctness problems requiring an invariant and a ranking function; (ii) greedy problems where the naive greedy fails; (iii) recursive construction problems (representations, tilings, trees); (iv) pairs of existence claims, one with a constructive proof and one without.
- **Probe misconceptions:** "it works on my examples, so it's correct"; invariants that are only true at the end; termination by "it obviously stops"; confusing correctness with efficiency.
- **Transfer distance:** medium-high. The invariant-plus-termination template is universal; test it in graph algorithms, number theory, and scheduling.
- **Do not** accept "the algorithm is obvious" without an invariant. Do accept informal complexity arguments at the level of "each step halves the input".

---

# Chapter 17 — Working Backwards and Auxiliary Objects

## 1. Core Idea

**Working backwards** means starting from the goal and asking: *what would be sufficient?* Repeat until you reach something you already have. The chain of sufficient conditions is the plan.

**Auxiliary objects** are things you introduce that were not in the problem: an extra line, an extra variable, an extra function, an extra set, an extra invariant. They are legal because mathematics lets you introduce any well-defined object; they are useful when they make the goal reachable.

The two techniques are the same technique. Working backwards identifies *what is missing*; the auxiliary object *supplies* it.

**Principle signature.** The problem is a "prove that" with no obvious starting move, or a "find the value" where the value is determined by several conditions that must be satisfied simultaneously. Working backwards is also the right move whenever the forward direction produces a combinatorial explosion.

## 2. First Principles

**Sufficient conditions compose.** If $A \Rightarrow B$ and $B \Rightarrow C$, then $A \Rightarrow C$. So if the goal is $C$ and you can find $B$ with $B \Rightarrow C$, and then $A$ with $A \Rightarrow B$, and $A$ is something you know, you are done. The chain is a proof written in reverse.

**The chain must terminate at an asset.** Working backwards is only useful if it reaches a hypothesis, a definition, or a known theorem. An infinite backward chain is a sign that the goal is too strong or the hypotheses too weak.

**Auxiliary objects must be justified.** You may introduce an object only if it is well-defined (→ Ch. 2) and if the properties you claim for it are proved. An auxiliary point that "must exist" needs an existence proof; an auxiliary variable that "must satisfy" an equation needs the equation derived.

**The wishful-thinking heuristic.** Pretend the goal is true and ask what else would then be true. If the consequences are consistent and recognizable, you have found the shape of the proof. If they are contradictory, the goal is false and you have found the start of a counterexample. This is Hamming's *"if I had a solution, what would it look like?"* made operational.

**Auxiliary objects are how geometry gets done.** Almost every synthetic geometry proof adds a line. The line is not arbitrary: it is chosen so that it creates similar triangles, cyclic quadrilaterals, or equal angles — that is, so that it converts the goal into a known relation.

## 3. Reasoning Process

1. **Write the goal in its most explicit form.** "Prove $PA \cdot PB = PC \cdot PD$" is more useful than "prove the theorem".
2. **Ask: what would imply this?** List two or three sufficient conditions. Prefer ones that are *recognizable* (similar triangles, equal angles, a known identity).
3. **Recurse.** For each sufficient condition, ask what would imply *it*. Stop when you hit an asset.
4. **Identify the missing object.** The gap between the last sufficient condition and the assets is where the auxiliary object goes.
5. **Construct it and verify legality.** Prove it exists and has the properties you need.
6. **Write the proof forwards.** The reader should see assets $\to$ auxiliary $\to$ goal, not the reverse.

## 4. Demonstrations

### Demonstration 17.1 — Working backwards in a geometry problem

*Problem.* In triangle $ABC$, $AB = AC$. Point $D$ lies on $AC$ with $AD = BD = BC$. Find $\angle A$.

*Backward analysis.* The goal is a numerical angle. What would determine it? A relation among angles. Where do angle relations come from? Isosceles triangles — and there are three: $AB=AC$, $AD=BD$, $BD=BC$. So the plan is: **express every angle in the figure in terms of $\angle A$, then use the angle sum of a triangle.**

*Execution.* Let $\angle A = x$.

- $AB = AC$ gives $\angle ABC = \angle BCA = \frac{180^\circ - x}{2}$.
- $AD = BD$ gives $\angle ABD = \angle DAB = x$.
- Hence $\angle DBC = \angle ABC - \angle ABD = \frac{180^\circ - x}{2} - x = \frac{180^\circ - 3x}{2}$.
- $BD = BC$ gives $\angle BDC = \angle BCD = \frac{180^\circ - x}{2}$.
- In triangle $BCD$: $\angle DBC + \angle BCD + \angle BDC = 180^\circ$, so
$$\frac{180^\circ - 3x}{2} + 2\cdot\frac{180^\circ - x}{2} = 180^\circ.$$
Multiply by $2$: $(180 - 3x) + 2(180 - x) = 360$, so $540 - 5x = 360$, giving $x = 36^\circ$.

*Check.* With $x = 36^\circ$: $\angle ABC = \angle BCA = 72^\circ$, $\angle ABD = 36^\circ$, $\angle DBC = 36^\circ$, $\angle BDC = \angle BCD = 72^\circ$. Triangle $BCD$ has angles $36+72+72 = 180$ ✓. And $D$ lies inside segment $AC$ since $\angle ABD = 36 < 72 = \angle ABC$ ✓.

**What to notice.** The backward analysis was one sentence: *find the source of angle relations*. Everything else was bookkeeping. The auxiliary object — the variable $x$ — is what made the bookkeeping possible: it converted a geometric configuration into a system of linear equations. **Working backwards identifies the *type* of auxiliary object you need; here, a parameter.**

### Demonstration 17.2 — Working backwards in an inequality

*Problem.* Let $a,b > 0$ with $\frac1a + \frac1b = 1$. Find the maximum of $\left(1+\frac1a\right)\left(1+\frac1b\right)$.

*Backward analysis.* The goal is a maximum of a product. What would give a bound? An inequality relating the factors to a single quantity. So: expand and see what quantity appears.

*Execution.*
$$\left(1+\frac1a\right)\left(1+\frac1b\right) = 1 + \frac1a + \frac1b + \frac{1}{ab} = 1 + 1 + \frac{1}{ab} = 2 + \frac{1}{ab}.$$
So the problem reduces to: **minimize $ab$** subject to $\frac1a+\frac1b=1$.

The constraint gives $ab = a + b$. By AM–GM, $a + b \ge 2\sqrt{ab}$, so $ab \ge 2\sqrt{ab}$, hence $\sqrt{ab} \ge 2$ and $ab \ge 4$, with equality iff $a = b = 2$.

Therefore the maximum is $2 + \frac14 = \frac94$, attained at $a = b = 2$.

*Check.* $a=b=2$: $\frac12+\frac12=1$ ✓, and $(1+\frac12)^2 = \frac94$ ✓.

**What to notice.** The auxiliary object was the quantity $ab$: the expansion revealed that the goal depends on $ab$ alone, so the problem became a one-variable optimization. **This is the general pattern for working backwards in optimization: expand the objective until a single auxiliary quantity appears, then bound that quantity.** The auxiliary object is not invented — it is *exposed* by the expansion.

### Demonstration 17.3 — Auxiliary lines forced by the goal

*Claim (intersecting chords).* Let two chords $AB$ and $CD$ of a circle meet at a point $P$ inside the circle. Then
$$PA \cdot PB = PC \cdot PD.$$

*Backward analysis.* The goal is a *product equality*. What produces product equalities? Similar triangles: if $\triangle PAC \sim \triangle PDB$, then $\frac{PA}{PD} = \frac{PC}{PB}$, which rearranges to $PA\cdot PB = PC \cdot PD$. So the goal would follow from a similarity. What produces similarity? Equal angles. What produces equal angles here? Inscribed angles subtending the same arc. Which segments create inscribed angles? The chords $AC$ and $BD$ — **which are not in the problem.** Draw them. The auxiliary lines are forced by the backward chain.

*Execution.* Draw $AC$ and $BD$. Then:

- $\angle PAC = \angle BAC = \angle BDC = \angle PDB$, since both subtend arc $BC$.
- $\angle PCA = \angle DCA = \angle DBA = \angle DBP$, since both subtend arc $AD$.
- Therefore $\triangle PAC \sim \triangle PDB$ (AA similarity).

Hence $\frac{PA}{PD} = \frac{PC}{PB}$, so $PA\cdot PB = PC\cdot PD$. $\blacksquare$

**What to notice.** The auxiliary lines were not a guess; they were the unique way to satisfy the backward chain *product equality $\leftarrow$ similarity $\leftarrow$ equal angles $\leftarrow$ inscribed angles $\leftarrow$ chords $AC$, $BD$*. This is why experienced geometers "see" the auxiliary line: they are running the chain backwards. **If you cannot see the line, run the chain explicitly.**

### Demonstration 17.4 — Auxiliary object: introducing a variable to count

*Problem.* In how many ways can you tile a $2 \times n$ rectangle with $1\times2$ dominoes?

*Backward analysis.* The goal is a count depending on $n$. What would determine it? A recurrence, which requires looking at the first column. So: introduce $a_n$ as the count, and analyze the leftmost part of the tiling.

*Execution.* In a $2\times n$ rectangle, the leftmost column is covered either by one vertical domino (leaving a $2\times(n-1)$ rectangle) or by two horizontal dominoes (which force the next column, leaving a $2\times(n-2)$ rectangle). These cases are exhaustive and disjoint. Hence
$$a_n = a_{n-1} + a_{n-2}, \qquad a_1 = 1,\ a_2 = 2.$$
So $a_n = F_{n+1}$ (Fibonacci), by the same argument as Demonstration 12.4.

**What to notice.** The auxiliary object here is the *sequence* $a_n$ itself — a variable that names the unknown count. Naming the unknown is the most underrated auxiliary move in mathematics: it converts "how many?" into "what does $a_n$ satisfy?", which is a question you have tools for. **When you cannot compute something, name it and find an equation.**

## 5. Connections

- **← Ch. 4.** Working backwards builds the chain that a forward-written proof will present.
- **← Ch. 7.** The "form of the answer" question is the first step of working backwards.
- **→ Ch. 11.** Backward chains often terminate at "choose an extremal object", which supplies the auxiliary.
- **→ Ch. 15.** An auxiliary object is a change of representation in miniature.
- **→ Ch. 20.** Optimization proofs are backward chains: goal $\leftarrow$ bound $\leftarrow$ inequality $\leftarrow$ known inequality.
- **→ Ch. 34.** Research often consists of running the backward chain and discovering that the missing object is a new concept.

## 6. Limitations

**Backward chains can branch explosively.** Every goal has many sufficient conditions, and most lead nowhere. The skill is choosing *recognizable* intermediate goals, not enumerating all of them. Set a depth limit (three or four steps) before reassessing.

**Sufficient conditions can be too strong.** Proving a stronger statement than needed may be impossible even when the goal is true. If the chain demands something false, back up and choose a weaker sufficient condition.

**Auxiliary objects can be unjustified.** Introducing a point, a line, or a variable that does not exist (or whose existence is unproved) invalidates the argument. The classic geometry error — drawing the auxiliary line in the wrong place, or assuming an intersection that does not occur — is exactly this failure (→ Ch. 32).

**Working backwards can hide a non-reversible step.** The chain "goal $\Leftarrow$ sufficient condition" is one-directional. If you later write the proof forwards, each step must be a valid implication in the forward direction, not just a sufficient condition you hoped for.

**Not every problem rewards it.** Problems with a natural constructive algorithm are often better solved forwards. Working backwards is for problems where the goal is a *relation* or a *value*, not where it is a *procedure*.

## 7. Applications

- **Proof engineering.** Most theorem proving in practice is backward search from the goal, with forward search from the hypotheses, meeting in the middle.
- **Algorithm design.** Dynamic programming is working backwards from the final state; the auxiliary object is the table of subproblem values.
- **Root-cause analysis.** Start from the failure and ask what would cause it; recurse until you reach a controllable cause. This is the same chain, with "cause" in place of "sufficient condition".
- **Requirements and design.** Start from the desired property and derive what the system must satisfy; the auxiliary object is the design constraint.
- **Physics.** Deriving an equation of motion from a conservation law is a backward chain from the goal (the conserved quantity) to the dynamics.
- **Finance.** Replicating a payoff by a portfolio is working backwards from the terminal value; the auxiliary object is the replicating portfolio.

## 8. Mastery Criteria

You have this chapter when you can:

1. Write a backward chain from a goal to a known asset in at most four steps, and say why each link is sufficient.
2. Identify the missing object in a gap and construct it legally.
3. Choose auxiliary lines in a geometry problem by running the chain (product $\leftarrow$ similarity $\leftarrow$ equal angles $\leftarrow$ chords).
4. Name an unknown as a variable and derive an equation or recurrence for it.
5. Recognize when the backward chain has become too strong, and weaken it.
6. Write the final proof forwards, with every step a valid forward implication.

**Diagnostic question.** "You are stuck. What would be sufficient to finish?" A learner who can answer with a *specific, recognizable* intermediate goal is working backwards. A learner who answers "I need to prove the theorem" is not.

### AI Tutor Brief

- **Generate:** (i) geometry problems requiring an auxiliary construction, with a hint ladder that reveals the backward chain rather than the line; (ii) inequality problems where expanding the objective exposes an auxiliary quantity; (iii) counting problems where naming the unknown yields a recurrence; (iv) problems with a tempting but too-strong sufficient condition.
- **Probe misconceptions:** adding auxiliary objects without justification; treating a sufficient condition as necessary; drawing the figure as if it were the proof; branching instead of committing to a recognizable intermediate goal.
- **Transfer distance:** high. Working backwards is domain-independent; test in geometry, algebra, counting, and proof strategy.
- **Do not** give the auxiliary object directly. Give the *backward chain* and let the learner construct the object — that is the skill being trained.

---

## Part II checkpoint

Before Part III, verify without notes:

1. Given a problem, name the goal type, count the degrees of freedom, and predict the form of the answer. (Ch. 7)
2. For a process, produce an invariant and a monovariant, and state what each proves. (Ch. 8)
3. Justify a WLOG with both clauses, and produce an illegitimate one. (Ch. 9)
4. Strengthen a hypothesis to rescue a failing induction. (Ch. 10)
5. Prove an extremum exists before using it, and construct the improvement that contradicts extremality. (Ch. 11)
6. Prove a binomial identity by finding the set both sides count. (Ch. 12)
7. Invent boxes for a pigeonhole argument whose collision implies the target. (Ch. 13)
8. Prove a case split is exhaustive, and define a canonical form with a uniqueness proof. (Ch. 14)
9. Choose a representation that trivializes the resisting step, and verify the back-substitution. (Ch. 15)
10. Write a loop invariant and a termination measure for an algorithm. (Ch. 16)
11. Run a backward chain from a goal to a known asset and identify the auxiliary object. (Ch. 17)

If three or more of these fail, do not proceed to Part III. The advanced chapters assume all eleven.

---
