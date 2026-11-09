# Part II — Problem-Solving Principles

You have the basics of definitions and proof. Now build a set of approaches for problems that give you no method. When you solve one, write down the clue that suggested your first useful move.

# Chapter 7 — Read the Shape of a Problem

## Start here

A pen and a notebook cost $8 together. What does each cost? You can give many answers, such as $2 and $6 or $3 and $5. The information fixes the total and still leaves room to choose a price.

## Worked example

Now suppose the notebook costs $2 more than the pen. Name the four parts of the problem.

| Part | In this problem |
|---|---|
| Given | A total of $8 and a difference of $2 |
| Goal | The two prices |
| Constraints | Prices must have the stated sum and difference |
| Freedom | You can choose one price before applying the total |

Subtract the notebook's extra $2 from the total. The $6 left is twice the pen price, so the pen costs $3 and the notebook $5. Check both conditions. Ask what form the answer should take before solving. Finding one possibility, listing every possibility, and showing there is no possibility require different arguments.

## Try it

- **Practice.** There are 12 red and blue tokens, with more red than blue and at least one of each. Is the number of red tokens determined? List every possible count.
- **Stretch.** Add one condition about the difference between the counts that gives a unique answer. Then choose a different difference that makes the problem impossible. Explain the difference between the two cases.

## Check your work

**Practice.** The red count can be 7, 8, 9, 10, or 11. Each leaves a smaller positive blue count.

**Stretch.** A difference of 2 gives 7 and 5. A difference of 3 is impossible because the difference and the sum of two integers differ by twice the smaller number. They must have the same parity.

# Chapter 8 — Track What Stays the Same or Moves One Way

## Start here

A row of coins starts all tails. A move flips exactly two coins. Can you get exactly one head? After any move, the head count changes by $-2$, 0, or 2. It remains even, so one head is unreachable.

## Worked example

A value preserved by every legal move is an **invariant**. Here the value is parity, which records whether a count is even or odd. Look for a simpler value when the exact state changes too much to track.

A **monovariant** changes only one way. Start with any pile of stones. If every legal move removes at least one stone, the pile size strictly decreases. Since the count is a nonnegative integer, the process must stop. The lower bound and the strict decrease both matter. A real-valued quantity can halve forever.

## Try it

- **Practice.** Start at 5. Each move adds or subtracts 6. Can you reach 28? Find an invariant that rules it out.
- **Stretch.** Remove opposite corners from an $8\times8$ chessboard. Can you cover all remaining squares with dominoes, each covering two adjacent squares?

## Check your work

**Practice.** The remainder upon division by 6 is always 5. The remainder of 28 is 4.

**Stretch.** The removed corners have the same color. Every domino covers one square of each color, so a tiling would require equal numbers of the two colors. The remaining counts are 30 and 32.

# Chapter 9 — Use Symmetry Without Losing Cases

## Start here

For two numbers $a$ and $b$, can you assume $a\le b$? You can when swapping the names leaves both the problem and its conclusion unchanged. Check what the labels mean before choosing an order.

## Worked example

To show $a+b\le 2\max(a,b)$, suppose $a\le b$. Then $a+b\le b+b$. The other ordering follows by swapping the names. This is what **without loss of generality** means.

Now suppose you are given $a+b=10$ and $a$ is a multiple of 3. Swapping $a$ and $b$ can break the condition about $a$. The pair $(6,4)$ is allowed, but $(4,6)$ is excluded. An apparent symmetry can disappear as soon as one label has a special role.

## Try it

- **Practice.** Two fair coins are flipped. Use symmetry to explain why “first heads, second tails” and “first tails, second heads” have equal probabilities. Assume independent flips.
- **Stretch.** Show that among any six people, some three are either all mutual acquaintances or all mutual strangers. Assume acquaintance is symmetric. Pick one person and look at their five relationships.

## Check your work

**Practice.** Swapping the flips exchanges the two outcomes and preserves their probabilities. Each has probability $1/4$.

**Stretch.** The chosen person has at least three relationships of one kind. Suppose they know three people. If any two of those three know each other, those two and the chosen person form an acquaintance triple. Otherwise the three form a stranger triple. If the chosen person has three stranger relationships, swap the words “acquaintance” and “stranger” throughout.

# Chapter 10 — Prove a Pattern by Induction

## Start here

Imagine a row of numbered tiles. You know tile 1 can fall and that falling tile $k$ knocks over tile $k+1$. Together those facts cover every tile with a positive integer label. **Induction** uses that same chain of implications.

## Worked example

Show that the sum of the first $n$ odd positive integers equals $n^2$. At $n=1$ the sum is 1. Assume it equals $k^2$ after $k$ terms. The next odd number is $2k+1$, so the sum after the next term is

$$k^2+2k+1=(k+1)^2.$$

The first calculation is the **base case**. The second is the **inductive step**, which proves the next case from the current one. Make sure the step starts where the base case leaves off.

## Try it

- **Practice.** Prove that $2^n\ge n+1$ for every integer $n\ge0$.
- **Stretch.** Prove every integer $n\ge2$ is either prime or a product of primes. Use **strong induction**, where the step can use all earlier cases.

## Check your work

**Practice.** $2^0=1$. If $2^k\ge k+1$, then $2^{k+1}\ge2(k+1)\ge k+2$ for $k\ge0$.

**Stretch.** The base case 2 is prime. If $n$ is composite, write $n=ab$ with $2\le a,b<n$. Apply the assumption to both smaller factors and combine their prime factorizations.

# Chapter 11 — Look at the Smallest or Largest Case

## Start here

In a finite group, choose a shortest person. Nobody in the group is shorter than that person. That sounds trivial, but in a hard problem an extreme choice often gives you an inequality or rules out a move before you do any calculation.

## Worked example

Suppose several people sit in a row and each person claims someone immediately beside them is taller. Choose a tallest person in the row. Neither neighbor can be taller, so the claims cannot all be true. Ties are fine because the claim requires someone strictly taller.

This is the **extremal principle**. Decide what to maximize or minimize, establish that an extreme case exists, then ask what would violate its defining property. Finite nonempty collections of numbers have a largest and a smallest element. Infinite collections need care. The positive fractions $1,1/2,1/3,\dots$ have no smallest member.

## Try it

- **Practice.** At a tournament each player played a different positive number of matches, and each pair played at most once. Show this is impossible with at least two players.
- **Stretch.** A finite set of distinct integer points on a line has at least two points. Prove that some pair of consecutive points realizes the smallest distance among all pairs.

## Check your work

**Practice.** With $n$ players the largest match count is $n-1$. There are only $n-1$ possible positive counts. Equivalently, a player with the smallest count needs at least $n-1$ larger, distinct counts above theirs, which would force the largest to be at least $n$.

**Stretch.** Choose a pair with minimum distance. If another point lies between them, one of the smaller distances to that point contradicts minimality.

# Chapter 12 — Count the Same Objects Two Ways

## Start here

A **bijection** matches each object on one side to exactly one on the other, and vice versa. For instance, match each subset of a five-item menu with the five yes/no choices that describe it. There are $2^5=32$ subsets.

## Worked example

In a club, count attendance across a week. You can count the names on each day's sign-in sheet and add the daily totals. Or you can count the days each person attended and add the personal totals. These methods agree because both count the same pairs $(\text{person},\text{day})$.

That is **double counting**. Write down one item you are counting before you count by either method. This makes it easier to catch accidental repeats or gaps.

## Try it

- **Practice.** Six people each send one card to every other person. How many cards are there? Explain why the answer differs from the handshake count.
- **Stretch.** In a finite group, every person has an integer number of friendships, and friendship is mutual. Prove the number of people with an odd friendship count is even.

## Check your work

**Practice.** There are $6\cdot5=30$ cards. A card from Ana to Bo is distinct from a card from Bo to Ana.

**Stretch.** Count friendship ends. The sum of the individual counts is twice the number of friendships, hence even. The even counts contribute an even total, so the number of odd counts must be even.

# Chapter 13 — Use the Pigeonhole Principle

## Start here

If 13 people each choose a favorite month, some month must be chosen by at least two people. If every month were chosen at most once, the total could be at most 12.

## Worked example

Choose six distinct integers from 1 through 10. At least two are consecutive. To see why, put the integers into five boxes.

$$(1,2),\quad(3,4),\quad(5,6),\quad(7,8),\quad(9,10).$$

Six choices in five boxes force one box to contain two choices. Its two members are consecutive. The interesting work was designing boxes that make a collision prove the desired claim.

## Try it

- **Practice.** Prove that among eight integers, some two differ by a multiple of 7.
- **Stretch.** Pick any $n+1$ distinct integers from 1 through $2n$, with $n\ge1$. Prove one picked integer divides another. Try repeatedly dividing each chosen integer by 2 while it is even.

## Check your work

**Practice.** Use the seven possible remainders modulo 7 as boxes. Two integers with the same remainder differ by a multiple of 7.

**Stretch.** Each chosen number has the form $2^k m$, with $m$ odd. There are only $n$ possible odd values of $m$ up to $2n$. Two choices share $m$, so the smaller divides the larger.

# Chapter 14 — Split Problems and Choose a Standard Form

## Start here

To count socks in a drawer, you could separate them by color. This works when every sock lands in one pile. **Decomposition** breaks a problem into manageable parts and makes you check whether they cover what you started with.

## Worked example

Fractions such as $2/6$, $3/9$, and $1/3$ represent the same number. Dividing numerator and denominator by their greatest common divisor gives $1/3$ each time. With a positive denominator, lowest terms give a **canonical form**, a standard representative for each rational number.

Two duties come with a standard form. Show that every allowed object can be put in the form. Then show that two allowed descriptions of the same object lead to the same result. A convenient-looking description alone leaves the second duty open.

## Try it

- **Practice.** Count the integers from 1 to 30 that are divisible by 2 or 3. Give cases that do not overlap.
- **Stretch.** Show that a positive rational number has just one lowest-terms fraction with a positive denominator. You may use the fact that if $b$ divides $ad$ and $a,b$ have no common factor greater than 1, then $b$ divides $d$.

## Check your work

**Practice.** Count all 15 multiples of 2, then the five odd multiples of 3. That gives 20.

**Stretch.** From $a/b=c/d$ get $ad=bc$. Since $a,b$ are coprime, $b$ divides $d$. By the same argument $d$ divides $b$. Their positivity forces $b=d$, and then $a=c$.

# Chapter 15 — Change the Representation

## Start here

A problem about who can reach whom by road may be easier on a sketch. A problem about area may be easier in algebra. A **representation** is how you choose to describe the objects and relationships.

## Worked example

Find real numbers $x,y$ with $x+y=10$ and $xy=21$. The two numbers sit equally far from their average, 5. Write $x=5+t$ and $y=5-t$. The product becomes $25-t^2$. Setting it to 21 gives $t^2=4$, so $t=2$ or $t=-2$. The ordered pairs are $(7,3)$ and $(3,7)$.

The new description builds in the sum condition. It covers all solutions because $t=x-5$ and then $y=5-t$. Check the original conditions after translating back. Some transformations, such as squaring both sides, can admit extra candidates.

## Try it

- **Practice.** Find two numbers with sum 12 and product 32 using the same representation.
- **Stretch.** Solve $\sqrt{x+5}=x-1$. State the restriction before squaring and check the candidates in the original equation.

## Check your work

**Practice.** Write them as $6+t$ and $6-t$. Then $36-t^2=32$, so the two numbers are 4 and 8.

**Stretch.** The right side must be nonnegative, so $x\ge1$. Squaring gives $x^2-3x-4=0$ and candidates $4,-1$. Only 4 respects the restriction, and $\sqrt9=3=4-1$.

# Chapter 16 — Build an Object or an Algorithm

## Start here

To prove that an object exists, try giving explicit instructions to build it. If you claim a procedure always works, show both why its steps are correct and why it eventually finishes.

## Worked example

Find the greatest common divisor of 48 and 18. Divide 48 by 18 to get a remainder of 12. A number divides both 48 and 18 exactly when it divides both 18 and 12, because $48=2\cdot18+12$. Repeat with $(18,12)$ to get $(12,6)$, then $(6,0)$.

This is **Euclid's algorithm**. The shared divisors stay the same at each step. The nonnegative second entry decreases until it reaches 0. At that point the first entry is the greatest common divisor, since all its divisors also divide 0. Here the answer is 6.

## Try it

- **Practice.** Use Euclid's algorithm to find the greatest common divisor of 84 and 30. Explain why you can discard 84 after the first step.
- **Stretch.** Given any finite list of positive integers, construct a positive integer that has remainder 1 when divided by every list entry greater than 1.

## Check your work

**Practice.** The pairs are $(84,30)$, $(30,24)$, $(24,6)$, and $(6,0)$. The common divisors stay the same because $84=2\cdot30+24$.

**Stretch.** Multiply all entries, then add 1. Every entry divides the product, so each entry greater than 1 leaves remainder 1.

# Chapter 17 — Work Backwards From the Goal

## Start here

Suppose you want to prove $x^2-6x+9\ge0$. A square is always nonnegative. Can you find a square that matches the expression? Expanding $(x-3)^2$ gives the expression exactly.

## Worked example

Prove $a^2+b^2\ge2ab$. Read backwards. What would guarantee the result? If $a^2+b^2-2ab$ were a square, it would be nonnegative. The missing object is $(a-b)^2$. Now write the proof forwards.

$$(a-b)^2\ge0\quad\Longrightarrow\quad a^2+b^2-2ab\ge0\quad\Longrightarrow\quad a^2+b^2\ge2ab.$$

An **auxiliary object** is something you introduce to make the argument possible, such as this square or a line in a diagram. When reasoning backwards, check that each condition you find is sufficient to get back to the goal.

## Try it

- **Practice.** Prove $x^2+4x+5\ge1$ for every real $x$.
- **Stretch.** Prove $ab\le25$ when $a+b=10$, and determine exactly when equality holds. Find an auxiliary square involving the difference.

## Check your work

**Practice.** $x^2+4x+5=(x+2)^2+1\ge1$.

**Stretch.** $(a+b)^2-4ab=(a-b)^2\ge0$, so $4ab\le100$. Equality requires $a=b$, and the sum then forces $a=b=5$.

## Part II checkpoint

Choose any 11 distinct integers from 1 through 20. Prove that some two sum to 21. Then give ten choices with no such pair. Try to derive the boxes from the desired sum before recalling the method's name. In your review, explain which half proves the guarantee and which shows the number of choices is sharp.

### Further challenge

Start with a row of $n$ tails. A move flips two **adjacent** coins. Characterize exactly which final patterns are reachable. A parity argument gives a necessary condition. For the other direction, pair off the desired heads and ask what happens when you flip every adjacent pair along the interval between two paired positions.
