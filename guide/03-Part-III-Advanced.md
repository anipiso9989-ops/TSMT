# Part III — Advanced Mathematical Thinking

This part combines earlier moves. Work through the first example in each chapter, then try the stretch problem before checking it. When you get stuck, identify the specific thing you need, such as a better bound or a way to translate the problem.

# Chapter 18 — Generalize Without Breaking the Argument

## Start here

A $3\times5$ rectangular grid has 15 cells. The same argument gives $ab$ cells for any grid with $a$ rows and $b$ columns. **Generalizing** means finding a family of problems that share an argument.

## Worked example

With three positive numbers, each at most 5, the sum is at most 15. For $n$ numbers, each at most $M$, the sum is at most $nM$. Add the $n$ individual inequalities. The reasoning never used positivity, so the bound also holds for negative numbers and negative $M$. It does use the upper bound on every term. Knowing that only the first term is at most $M$ is insufficient.

To generalize a result, look at the steps of its proof. Replace the specific quantities by variables and keep the conditions that make each step legal.

## Try it

- **Practice.** A $4\times4$ grid has 16 cells. Generalize the number of cells to a rectangular grid and then to a stack of such grids.
- **Stretch.** A tournament with six players has 15 games if every pair plays once. Give a formula for $n$ players. Then adapt it when each pair plays exactly twice and some of the games are canceled. What extra information determines the new total?

## Check your work

**Practice.** There are $ab$ cells in an $a\times b$ grid and $abc$ cells in a stack of $c$ such grids.

**Stretch.** Each player contributes $n-1$ game ends, giving $n(n-1)/2$ games. Two games per pair give $n(n-1)$ scheduled games. Subtract the number canceled. If you know only which players had cancellations, you may still need the cancellation count.

# Chapter 19 — Recognize the Same Structure in Disguise

## Start here

Two road maps can look different and still connect towns in exactly the same way. If you can rename the towns and preserve precisely which pairs have roads, every conclusion about connectivity carries over.

## Worked example

Consider a graph with edges $AB,BC,CD,DA$. Another graph has edges $24,41,13,32$. Match $A\leftrightarrow2$, $B\leftrightarrow4$, $C\leftrightarrow1$, and $D\leftrightarrow3$. The four edges match in both directions. This is a graph **isomorphism**, a one-to-one correspondence that preserves adjacency and non-adjacency.

A **duality** can swap roles instead. Think of a seating chart as a table with people as rows and seats as columns. Turn the chart sideways. “Each person has exactly one seat” says each original row has one mark. In the turned chart, each column has one mark. The turned chart also lets you ask a different question about its rows, which now represent seats. A seat shared by two people would appear as a row with two marks. A duality is useful when you have checked the dictionary of what swaps and what stays true.

## Try it

- **Practice.** Can a four-vertex chain and a four-vertex star (one center joined to three leaves) be isomorphic? Use the number of neighbors at a vertex.
- **Stretch.** Can a six-vertex ring be isomorphic to two separate triangles? Every vertex has two neighbors. Find a property the graphs do not share and explain why any isomorphism would preserve it.

## Check your work

**Practice.** The star has a vertex with three neighbors. The chain has none.

**Stretch.** In the ring, there is a path between every pair of vertices. There is no path between vertices in different triangles. Renaming vertices while preserving all edges preserves paths, so it preserves this property.

# Chapter 20 — Prove an Answer Is Best

## Start here

Which rectangle with perimeter 20 has the largest area? Finding a rectangle with area 25 gives you a candidate. To prove it is best, you also need a reason every allowed rectangle has area at most 25.

## Worked example

Let the positive side lengths be $a$ and $b$. The perimeter condition gives $a+b=10$. Then

$$4ab=(a+b)^2-(a-b)^2\le100.$$

Every area is at most 25. The $5\times5$ rectangle attains 25, so the upper bound and the example meet. The identity and the example are a **certificate**, a short way for someone else to verify the optimum.

One way to get a bound is a **relaxation**. Allow more choices than the original rules permit and solve that easier problem. For a maximum, this can only raise the best value, so it gives an upper bound. Check whether an original choice actually reaches it.

## Try it

- **Practice.** With perimeter 22 and positive integer sides, find the maximum area and prove it. What does allowing fractional sides change?
- **Stretch.** You have positive integer sides summing to $n\ge2$. Show why moving 1 unit from the longer side to the shorter side improves the area whenever the sides differ by at least 2.

## Check your work

**Practice.** The same identity gives $ab\le121/4=30.25$. Integer areas are therefore at most 30, and sides 5 and 6 attain 30. Fractional sides can reach 30.25 with sides 5.5 and 5.5.

**Stretch.** If $b\ge a+2$, then $(a+1)(b-1)-ab=b-a-1>0$. Repeat until the sides differ by at most 1. This is an **exchange argument** because it rules out any unbalanced optimum by improving it.

# Chapter 21 — Reason With Probability

## Start here

Suppose 1 in 100 emails is spam. A filter flags nearly all spam, but it also flags some ordinary emails. To judge a flag, you need to compare the number of true flags with the total number of flags.

## Worked example

Imagine 2,000 emails in the given proportions. Suppose there are 20 spam emails and the filter flags 18 of them. Suppose it also flags 5% of the 1,980 ordinary emails, which is 99. Among 117 flags, only 18 are spam, or about 15%.

The spam rate before seeing the flag is the **base rate**. The chance of spam among flagged emails is a **conditional probability**, calculated within the flagged group. Writing down the group in the denominator prevents you from confusing “flagged among spam” with “spam among flagged.”

## Try it

- **Practice.** An audit finds 20 faulty parts in a lot of 200. A scanner flags 16 faulty parts and 18 good parts. What fraction of flagged parts are faulty?
- **Stretch.** You draw two cards without replacement from a deck of ten cards, three of them red. What is the expected number of red cards drawn? The expected number is the long-run average over repeated draws. Does the calculation need the draws to be independent?

## Check your work

**Practice.** There are 34 flags and 16 flagged faulty parts, so the fraction is $16/34=8/17$.

**Stretch.** Each draw position has a $3/10$ chance of being red. Count 1 for red and 0 otherwise in each position. The average of the sum is the sum of the averages, $3/10+3/10=3/5$. The draws are dependent, but adding these averages does not require independence.

## Use an average to prove existence

Can you color the vertices of any finite graph without loops red or blue so at least half its edges join different colors? Assign the colors independently by fair coin flips. For each edge, the two ends get different colors with probability $1/2$. Count 1 when an edge crosses between colors and 0 otherwise. Adding these averages gives an expected crossing count of half the edges, even though crossing events can depend on one another.

If every coloring had fewer crossings than the average, their average would be smaller too. So at least one coloring reaches half. This is the **probabilistic method**. Use a random construction to prove some choice works. The proof here tells you such a coloring exists.

# Chapter 22 — Estimate Growth With Bounds

## Start here

An exact value can be expensive to find. Two simple bounds can still tell you how the value grows when the input gets large. **Asymptotic reasoning** compares growth at large input sizes.

## Worked example

Let $H_k=1+1/2+\cdots+1/k$. At $k=8$, group the terms after 1 in blocks with indices 2, then 3 through 4, then 5 through 8. Each block after 1 adds between $1/2$ and 1. For example, the last block has four terms, each at least $1/8$ and at most $1/4$.

For $k=2^m$ there are $m$ such blocks. Block $j$ has $2^{j-1}$ terms, with denominators greater than $2^{j-1}$ and at most $2^j$. Thus

$$1+m/2\le H_{2^m}\le1+m.$$

Doubling the cutoff adds only one block. Both bounds show logarithmic growth, because $m$ is the number of doublings needed to reach $2^m$. Compare an arbitrary cutoff with the powers of two on either side.

## Try it

- **Practice.** Use the bounds above to put $H_{32}$ in an interval.
- **Stretch.** Prove that $1+1/4+1/9+\cdots+1/n^2\le2$ for every positive integer $n$. Compare $1/k^2$ with $1/(k(k-1))$ when $k\ge2$ and look for cancellation.

## Check your work

**Practice.** Since $32=2^5$, the interval is $[3.5,6]$.

**Stretch.** $1/k^2\le 1/(k(k-1))=1/(k-1)-1/k$. Summing the differences from 2 to $n$ leaves $1-1/n$. Add the first term to get at most $2-1/n$.

# Chapter 23 — See the Same Fact in Two Ways

## Start here

A drawing can make a fact easy to discover. Algebra can make it easy to generalize. Comparing the two helps you see which step does the work.

## Worked example

Take an $n\times n$ square of unit cells. Add a row of $n$ cells, a column of $n$ cells, and one corner cell to make the next square. The extra cells total $2n+1$. Algebra gives the same fact.

$$(n+1)^2-n^2=2n+1.$$

The picture shows why the terms are two strips and a corner. The algebra confirms the equality and suggests a new question. If both sides grow by $k$ units instead of 1, how many cells are added?

## Try it

- **Practice.** Answer the new question in both ways. Assume $n,k$ are positive integers.
- **Stretch.** Use a pairing argument and a picture of dots to explain why $1+2+\cdots+n=n(n+1)/2$. Explain where the factor of 2 appears in each version.

## Check your work

**Practice.** The strips have $nk$ cells each and the new corner has $k^2$, so the total is $2nk+k^2$. Expanding $(n+k)^2-n^2$ gives the same expression.

**Stretch.** Pair forward and reverse lists to get $n$ pairs of sum $n+1$. For the picture, draw left-aligned rows of lengths $1,2,\dots,n$. A second copy rotated by $180^\circ$ fills the complementary space in an $n\times(n+1)$ rectangle. In each case the construction counts two copies of the original sum.

# Chapter 24 — Combine Strategies and Know When to Switch

## Start here

One method often opens the door and another finishes. If a direct proof stalls, write down what would finish it. Then choose a method that can supply that missing step.

## Worked example

Show that the only integer solution of $x^2=2y^2$ is $(0,0)$. The parity argument from Chapter 4 forces $x$ and $y$ to be even. If a nonzero solution exists, choose one with the smallest positive $|y|$. Such a minimum exists because every nonempty set of positive integers has a least member. Also, $y=0$ would force $x=0$.

Now halve both coordinates. The equation still holds, and the new $|y|$ is positive and smaller. That contradiction rules out every nonzero solution. The chain uses parity to produce a legal move, an extremal choice to make the move decisive, and **descent** to name the smaller-solution argument.

## Try it

- **Practice.** Name one method that could help when legal moves seem to preserve something. Name a different method when you need to show a candidate is best.
- **Stretch.** Prove that $x^2+y^2=3z^2$ has no nonzero integer solution. Start by listing possible square remainders upon division by 3.

## Check your work

**Practice.** Look for an invariant for the first problem. For the second, look for a bound and an example that attains it.

**Stretch.** Squares have remainders 0 and 1 modulo 3. A sum of two such remainders is 0 modulo 3 only when both are 0, so 3 divides $x$ and $y$. Their squared sum is divisible by 9, so $3\mid z^2$ and hence $3\mid z$. Divide all three coordinates by 3. A solution with smallest positive $|z|$ would give a smaller one. If $z=0$, then $x=y=0$.

### Stretch further

Write a positive integer $n$ as the sum of an ordered list of 1s and 2s. Count these lists in two ways. First sort by the last entry and find a rule relating consecutive counts. Then sort by the number $k$ of 2s. In the second approach there are $n-k$ entries in total, so ask how many ways you can choose the $k$ positions for the 2s. Compare what the two descriptions help you compute.

## Part III checkpoint

Find the largest product of two positive integers whose sum is 17. Prove your result with an exchange argument and then with a bound. Change the sum to an arbitrary integer $n\ge2$ and explain how the best pair depends on whether $n$ is odd or even. Compare what each proof reveals about equality.

### Further challenge

Prove the coloring claim from Chapter 21 without using chance. Pick a coloring with as many crossing edges as possible. What would happen if you changed one vertex's color? Show that each vertex must have at least half its neighbors in the other color, then count the ends of the crossing edges. Compare the local guarantee you get here with the existence argument from probability.
