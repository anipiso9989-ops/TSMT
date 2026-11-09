# Part V — Independent Mathematical Research

Here you begin with questions instead of assigned methods. Keep a record of examples, guesses, failed arguments, and changes of mind. An exact counterexample or a smaller claim with a proof can be a stronger result than a large claim you cannot defend.

# Chapter 31 — Turn a Pattern Into a Conjecture

## Start here

The rule $n^2+n+41$ gives 41, 43, 47, 53, and 61 at $n=0,1,2,3,4$. Each is prime. Does the rule always give primes? At $n=41$, the value is $41\cdot43$, which is composite.

## Worked example

A **conjecture** is a precise mathematical claim you suspect is true and have yet to prove. “This looks prime often” leaves too much unspecified. “For every nonnegative integer $n$, $n^2+n+41$ is prime” has a clear domain and a clear way to fail.

The failed guess suggests a new question. When is the expression divisible by 41? Since it is $n(n+1)+41$, divisibility by 41 is equivalent to 41 dividing $n(n+1)$. A prime dividing a product divides at least one factor, so this occurs exactly when $n$ or $n+1$ is a multiple of 41. A guess about all primes became a precise, provable statement about one factor.

## Try it

- **Practice.** State a precise conjecture about $n^2+n$ for all integers and prove it.
- **Stretch.** For a prime $p$, characterize all integers $n$ for which $p$ divides $n^2+n+p$. Then find a composite $p$ for which the corresponding statement fails.

## Check your work

**Practice.** $n^2+n=n(n+1)$ is even because one of two consecutive integers is even.

**Stretch.** For prime $p$, $p$ divides the expression exactly when $p$ divides $n$ or $n+1$. With $p=6$ and $n=2$, the product $2\cdot3$ is divisible by 6, while neither factor is.

# Chapter 32 — Find Counterexamples and Test the Boundaries

## Start here

“Every odd integer is prime” sounds plausible if you look only at 3, 5, and 7. The integer 9 meets the condition and fails the conclusion. One **counterexample** settles a claim about every member of a group.

## Worked example

Take the statement “If positive integers $a$ and $b$ have no common factor greater than 1, and $a$ divides $bc$, then $a$ divides $c$.” Test the role of the first assumption by dropping it and keeping everything else. Choose $a=6$, $b=4$, and $c=3$. Then 6 divides 12 and 6 does not divide 3. The shared factor 2 in $a$ and $b$ supplies a factor that $c$ lacks.

This is **boundary hunting**. Choose one assumption to remove, keep the others, and search for a case that breaks the conclusion. If a candidate also violates a condition you meant to keep, discard it and try again.

## Try it

- **Practice.** Find a counterexample to “If $a^2>b^2$, then $a>b$” for integers. Find a restriction on both variables that repairs the implication.
- **Stretch.** For positive integers $a$ and $b$, prove that whenever they share a factor greater than 1, there is a positive $c$ with $a$ dividing $bc$ and $a$ failing to divide $c$.

## Check your work

**Practice.** $a=-3$ and $b=2$ give $9>4$ but $-3<2$. For nonnegative $a,b$, if $a\le b$ then $a^2\le b^2$, so the implication holds.

**Stretch.** Let $d>1$ divide both $a$ and $b$. Choose $c=a/d$. Then $bc=a(b/d)$ is a multiple of $a$, while $0<c<a$ rules out divisibility of $c$ by $a$.

# Chapter 33 — Run an Experiment That Can Surprise You

## Start here

How many pieces can $n$ straight cuts make in a sheet of paper? Sketch several cases. For zero through four cuts, the maximum counts are 1, 2, 4, 7, and 11. The increases are 1, 2, 3, and 4. What mechanism could explain them?

## Worked example

Treat the sheet as a convex region, such as a rectangle, and make each cut a straight line through it. The $k$th cut meets at most $k-1$ earlier cuts at distinct points inside the sheet. These points divide the cut into at most $k$ segments. Each segment splits one existing region. The maximum increase is therefore $k$.

To attain the bound for a fixed number of cuts, draw lines of distinct directions through the center, then move each line by a small distance. Move the lines one at a time. When placing a line, avoid the finitely many shifts that would make it pass through an intersection of two already placed lines. For each pair, a sufficiently small shift keeps its intersection near the center because their directions are distinct. There are only finitely many pairs, so you can keep every intersection inside the sheet. Now the increases attain $1,2,\dots,n$. The maximum count is $1+n(n+1)/2$.

The sketches suggested an exact claim. The intersection argument explains both the upper bound and when it is attainable.

## Try it

- **Practice.** Predict the maximum number of pieces after six cuts. Explain what happens if all six are parallel.
- **Stretch.** Suppose $n\ge1$ cuts all pass through the center with distinct directions. Find the number of pieces and explain exactly where the maximum-count proof loses pieces.

## Check your work

**Practice.** The maximum is $1+6\cdot7/2=22$. Six parallel cuts through the interior give seven pieces because each cut adds only one.

**Stretch.** The first cut makes two pieces. Each subsequent cut meets all earlier cuts at the same point, producing only two segments and two new pieces. The total is $2n$. The loss comes from several intersections occupying one point.

# Chapter 34 — Invent a Problem Worth Solving

## Start here

Start with a solved problem. Any 11 distinct integers from 1 through 20 include two that sum to 21. What changes if you want the pair to sum to 20? Changing one number can reveal which part of the original argument mattered.

## Worked example

For sum 21, the boxes are ten pairs, $(1,20),(2,19),\dots,(10,11)$. For sum 20, there are nine pairs, $(1,19),(2,18),\dots,(9,11)$, and two unpaired numbers, 10 and 20. The two chosen integers must be distinct, so 10 cannot pair with itself.

You can avoid a sum of 20 by taking one number from each pair plus both unpaired numbers. That gives 11 choices. Any 12 must take a full pair. The change produced a new sharp threshold and explained why it moved.

To invent a problem, change one rule, predict which step of the solution will break, and see whether the new version has a clean answer or an interesting obstruction.

## Try it

- **Practice.** In the same range, find the smallest number of distinct choices that guarantees a pair summing to 19.
- **Stretch.** For choices from 1 through $N$, give a rule for the threshold for any target sum $s$ for which at least one distinct pair exists.

## Check your work

**Practice.** There are nine pairs $(1,18),\dots,(9,10)$, plus unpaired 19 and 20. One from each pair plus the two unpaired numbers gives 11. The guarantee begins at 12.

**Stretch.** Each number has at most one distinct partner, namely $s-x$, so the valid pairs are disjoint. If there are $p$ pairs, the largest pair-free selection has $N-p$ elements, one from each pair plus every unpaired number. The threshold is $N-p+1$. Count $p$ by counting allowed $x$ with $x<s-x$ and $1\le s-x\le N$.

# Chapter 35 — Decide What to Work On Next

## Start here

You have tried a proof for 30 minutes. “I am stuck” gives you little to work with. “I can construct a case that reaches 12, but I have no upper bound” tells you what to look for next.

## Worked example

Suppose you ask how many squares a knight can visit on a $3\times3$ chessboard without revisiting a square. You find a path through six squares. Before searching randomly for a longer path, list the legal moves. The center is isolated. From each noncentral square there are exactly two legal moves. Tracing one gives the cycle

$$(1,1),(2,3),(3,1),(1,2),(3,3),(2,1),(1,3),(3,2),(1,1).$$

This supplies a path through eight distinct squares and an upper bound of eight because the center is unreachable from any other square. A failed search became a structural question about which positions connect.

Keep a short research log. Record the precise claim, what you checked, the first gap in the argument, and one action that could close it. If you find a mistake, state which conclusions depend on it and revisit those conclusions.

## Try it

- **Practice.** Write a one-sentence upper bound and a separate one-sentence construction for the knight problem.
- **Stretch.** What changes on a $3\times4$ board? Before searching for a path, identify a property that every knight move preserves or changes. State what your observation proves and what is still open in your own attempt.

## Check your work

**Practice.** The center has no legal moves, so a path visiting more than one square can use only the eight outer squares. Following the displayed cycle and stopping before returning to the start visits all eight.

**Stretch.** Every move flips the square's color, since it changes the sum of the coordinates by an odd number. This forces the two color counts on any path to differ by at most one. On this board there are six of each color, so the coloring alone leaves a full path possible. You still need a construction or a stronger obstruction.

## Part V checkpoint

Choose an earlier result and change one condition. Write a question with a precise domain. Explore small and extreme cases, then state a conjecture and the evidence that would disprove it. Produce a proof, a counterexample, or a partial result with the remaining gap stated explicitly. Ask another person to audit the argument or reread it the next day. Record the strongest claim that survived.

### Further challenge

In a row of $n$ squares, how many ways can you choose exactly $k$ squares with no two adjacent? Make a small table and look for a pattern. Try describing a selection by the lengths of the gaps between its chosen squares. Record where your argument uses the fact that the squares form a row. Then investigate what changes when the first and last squares are adjacent too.
