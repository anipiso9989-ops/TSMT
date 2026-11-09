# Part I — Foundations of Mathematical Thought

Start with small problems you can work through on paper. By the end of this part, you should be able to say exactly what a claim means, decide what would prove it, and write an argument someone else can check.

# Chapter 1 — Spot the Structure

## Start here

Stack three boxes on each of four shelves. Now mark three squares in each of four rows. How many boxes or marks are there? Both answers are 12. Shelves and rows play the same role, as do boxes and marks. The arrangement you kept when you changed the story is the **structure**.

## Worked example

Ana beat Bo at chess, and Bo beat Cam. Did Ana necessarily beat Cam? No. Cam could have beaten Ana in a third game. Now change “beat” to “finished ahead of” in one race with no ties. If Ana finished ahead of Bo and Bo ahead of Cam, then Ana finished ahead of Cam.

Both stories have the same shape on paper. Only the race order has the rule “if A is ahead of B and B is ahead of C, then A is ahead of C.” We call that rule **transitivity**. A useful analogy preserves the rules the reasoning needs.

## Try it

- **Practice.** Three towns lie on one road in the order A, B, C. A to B is 5 km and B to C is 7 km. Can you conclude A to C is 12 km if the distances now come from the shortest routes in a road network?
- **Stretch.** Find a relation from your own life that is transitive and one that fails. For the second, give three specific objects and show where the chain breaks.

## Check your work

**Practice.** The route through B is 12 km, so the shortest route is at most 12 km. A direct 9 km road would make the answer smaller.

**Stretch.** “Is older than” is transitive because it follows the order of birth dates. “Is within 2 km of” can fail. Place three stops at 0, 1.5, and 3 km on a line.

# Chapter 2 — Make Definitions Precise

## Start here

Is 0 even? Try the definition. An integer is **even** if it can be written as twice an integer. Since $0=2\cdot0$, it qualifies. So does $-6=2\cdot(-3)$. A useful definition tells you how to decide borderline cases.

## Worked example

Call two integers **equivalent modulo 5** when their difference is a multiple of 5. For example, 2 and 7 are equivalent because $7-2=5$.

Suppose a game tracks only this equivalence and tells you to add 3. Starting from 2 gives 5, and starting from 7 gives 10. Both results are still equivalent. In general, if $a-b$ is a multiple of 5, then $(a+3)-(b+3)=a-b$ is too. The rule is **well-defined** because the outcome, as measured by equivalence, does not depend on the representative you chose.

A quick definition check is to name the allowed objects, test a clear example and a boundary example, then ask whether a change of representation changes the answer.

## Try it

- **Practice.** A teammate defines a square as “a shape with four equal sides.” Give an example that passes the test but should be excluded. Repair the definition for ordinary quadrilaterals.
- **Stretch.** Fractions can represent the same number in different ways. Someone proposes taking the numerator as a property of the number. Show why this fails and give a property that survives changing the fraction.

## Check your work

**Practice.** A rhombus with angles of $60^\circ$ and $120^\circ$ passes. Require four equal sides and four right angles.

**Stretch.** $1/2=2/4$, but the numerators are 1 and 2. Whether the fraction is greater than 0 is a property of the number, independent of the fraction used to represent it.

# Chapter 3 — Follow the Logic

## Start here

“If a number is divisible by 4, then it is even” tells you what follows when the first condition is true. Reversing the statement gives its **converse**. That converse is false because 6 is even and is not divisible by 4.

## Worked example

What would disprove “Every player scored in at least one game”? Find one player who scored in no game. The order of the phrases matters.

- “Every player scored in some game” lets each player have a different scoring game.
- “Some game had every player score” asks for one game that works for everyone.

Two players and two games separate the claims. Ana scores only in game 1 and Bo scores only in game 2. Everyone scored somewhere, but neither game had both players score.

When handling an “if $P$, then $Q$” claim, you can also prove its **contrapositive**. Assume $Q$ is false and show $P$ must be false. A number that is not even cannot be divisible by 4. This expresses the same rule as the original claim.

## Try it

- **Practice.** Negate “Some student solved every problem.” Say what evidence would establish your negation.
- **Stretch.** Show that if $n^2$ is even, then the integer $n$ is even. Start from the contrapositive and write an odd integer as $2k+1$.

## Check your work

**Practice.** Every student missed at least one problem. Check each student individually. Different students may miss different problems.

**Stretch.** If $n=2k+1$, then $n^2=2(2k^2+2k)+1$, which is odd. Thus an even square cannot come from an odd integer.

# Chapter 4 — Write a Proof Someone Can Check

## Start here

The sum of 7 and 9 is even. So is the sum of 11 and 13. Examples suggest a rule. A **proof** explains why the rule holds for every allowed pair.

## Worked example

To prove that any two odd integers add to an even integer, take arbitrary odd integers $a$ and $b$. By definition, $a=2j+1$ and $b=2k+1$ for some integers $j$ and $k$. Then

$$a+b=2(j+k+1).$$

The quantity inside the parentheses is an integer, so the sum is even. The proof works because the letters can stand for any two odd integers. Writing the sum in the form required by the definition closes the argument.

| What the claim asks for | A first approach |
|---|---|
| Show that a rule always holds | Start with an arbitrary allowed example and reason from the assumptions. |
| Show that something exists | Build one and check every requirement. |
| Show that something is impossible | Assume you have it and look for a contradiction. |
| Disprove a rule | Give one allowed case where the conclusion fails. |

## Try it

- **Practice.** Prove that the product of two odd integers is odd. Explain what justifies the final step.
- **Stretch.** Prove that $\sqrt{2}$ is irrational. Use Chapter 3 and begin by assuming $\sqrt{2}=a/b$ with the fraction in lowest terms.

## Check your work

**Practice.** $(2j+1)(2k+1)=2(2jk+j+k)+1$. The term $2jk+j+k$ is an integer.

**Stretch.** Squaring gives $a^2=2b^2$, so $a$ is even. Writing $a=2k$ yields $b^2=2k^2$, so $b$ is also even. Both share a factor of 2, contradicting lowest terms.

# Chapter 5 — Abstract the Rule

## Start here

You can pair up six gloves, six names, or six dots. What mattered about the objects? For this task, only the number of objects mattered. **Abstraction** means keeping the features your reasoning needs and setting aside the rest.

## Worked example

Suppose you want to know how many matches happen when everyone in a group plays everyone else once. Draw a dot for each player and a line between each pair. With five dots, each dot touches four lines. That makes $5\cdot4=20$ touches. Every line has two ends, so there are $20/2=10$ lines.

The reasoning works for five people exchanging gifts in pairs or five towns connected by a road for every pair. It depends on what you mean by a pair. If each person gives a separate gift to each other person, direction matters and the total is 20.

The diagram is a **graph**, a collection of points called vertices and connections called edges. A graph can preserve who is connected while leaving out names, distances, and how the lines happen to be drawn.

## Try it

- **Practice.** Use the dot-and-line model to count handshakes among eight people if each pair shakes hands once.
- **Stretch.** Explain how the argument changes if only some pairs shake hands. Give a rule for finding the total from a list of each person's handshake count.

## Check your work

**Practice.** There are $8\cdot7/2=28$ handshakes.

**Stretch.** Add everyone's counts and divide by 2. Each actual handshake appears in exactly two counts, regardless of which pairs meet.

# Chapter 6 — Rebuild a Result From Scratch

## Start here

Suppose you forget how to add the integers from 1 to 100. Can you rebuild the shortcut? First look for a fact you can explain about how the numbers are arranged.

## Worked example

Write the sum twice, once forwards and once backwards. Align the terms.

$$
\begin{aligned}
S&=1+2+\cdots+99+100,\\
S&=100+99+\cdots+2+1.
\end{aligned}
$$

Each column adds to 101. There are 100 columns, so $2S=100\cdot101$. Divide by 2 to get $S=5050$. This argument avoids having to pair terms within one list, where an odd number of terms leaves a middle term.

For the list from 1 to any positive integer $n$, there are $n$ columns, each summing to $n+1$. Therefore $S=n(n+1)/2$. This is first-principles reasoning. Start with facts you can defend, derive the result, and name the assumptions the derivation uses.

## Try it

- **Practice.** Derive the sum of $4,7,10,13,16$ by pairing forward and reverse lists.
- **Stretch.** Show that the average of any finite list with constant spacing equals the average of the first and last terms. Explain why constant spacing matters.

## Check your work

**Practice.** Every column totals 20. Two copies total $5\cdot20$, so one copy totals 50.

**Stretch.** Moving one place inward from each end adds the spacing on the left and subtracts the same spacing on the right. The paired sum stays equal to the sum of the endpoints. Divide the doubled sum by twice the number of terms. A list like $1,2,9$ shows what can happen when the spacing changes.

## Part I checkpoint

Prove that among any three integers, two have an even sum. First define even and odd. Then explain why some two integers must share a parity (both even or both odd), and prove their sum is even in each case. Finally, show why the claim can fail with two integers. You are ready to move on when your proof covers every case and your counterexample respects the new rules.

### Further challenge

Which positive integers can be written as the difference of two integer squares? Find a rule and prove both directions. Try listing square remainders upon division by 4. For the cases that work, look at differences of squares whose bases are one or two apart.
