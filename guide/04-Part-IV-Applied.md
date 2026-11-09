# Part IV — Applied Mathematical Reasoning

A proof tells you what follows from stated assumptions. In an application, you also have to decide whether those assumptions fit the situation. Practice keeping the calculation, the model, and the evidence separate.

# Chapter 25 — Build a Model and Test It

## Start here

A shuttle carries 20 passengers per trip. In two trips it carried 40. How many will it carry in six trips? A model that assumes every trip fills all seats predicts 120. The prediction depends on demand as well as capacity.

## Worked example

A pop-up kitchen can serve at most 30 lunches per hour. Its first two hourly sales counts are 20 and 25. Two models fit exactly.

| Assumption | Sales in hour 3 | Sales in hour 4 |
|---|---:|---:|
| Sales grow by five each hour with unlimited supply | 30 | 35 |
| Demand grows by five each hour, and supply caps sales at 30 | 30 | 30 |

Hour 3 cannot distinguish the predictions. Hour 4 can. A **model** is a set of assumptions and rules that connects a real question to a calculation. To test a model, look for an observation where plausible alternatives disagree. Also decide what the observation actually measures. Sales count completed purchases. A line of people turned away could reveal additional demand.

## Try it

- **Practice.** A tank holds 10 liters at minute 1 and 20 at minute 2. A constant-rate model predicts 40 at minute 4. Make a second model that agrees with both observations and predicts less at minute 4.
- **Stretch.** In the kitchen example, what additional observations would help distinguish a shortage of meals from a drop in demand when sales are 30?

## Check your work

**Practice.** Add a tank capacity of 25 liters and let incoming water spill when full. The model predicts 25 at minute 4.

**Stretch.** Record whether the kitchen sold out, how long it stayed sold out, and how many attempted purchases it turned away. Reaching capacity by itself leaves the demand above capacity unknown.

# Chapter 26 — Estimate Before You Calculate

## Start here

How many ping-pong balls fit in a classroom? Before hunting for an exact answer, get the scale. Break the question into quantities you can estimate and write the units next to each one. This is **Fermi estimation**.

## Worked example

Take a classroom about 8 m long, 6 m wide, and 3 m tall. Its empty volume is about $144\,\text{m}^3$. Suppose each ball occupies roughly a cube 4 cm on a side in a loose grid. Each cube takes up about $0.04^3=0.000064\,\text{m}^3$. The quotient gives a little over two million balls in that grid model.

Check by another route. You could fit about 200 ball widths along the length, 150 along the width, and 75 along the height. Multiply to get $2{,}250{,}000$. This verifies the units and arithmetic. Both routes share the same packing assumption. To test that assumption, count how many balls fit in a small box and use the count per liter as a separate estimate.

## Try it

- **Practice.** Estimate how many one-liter bottles a school of 800 students could fill if each used about 0.6 liters of water each day. State the assumption about days.
- **Stretch.** Give a plausible low and high daily estimate if the school has 750–850 students present and each uses 0.4–0.8 liters. Which range contributes the larger relative uncertainty?

## Check your work

**Practice.** One school day gives $800\cdot0.6=480$ liters, or 480 one-liter bottles' worth.

**Stretch.** The stated ranges imply 300–680 liters. The per-student estimate varies by a factor of 2. Attendance varies by a factor of $850/750$, so consumption per student accounts for the larger relative variation.

# Chapter 27 — Check Units and Scaling

## Start here

At 60 kilometers per hour, a 90-kilometer trip takes $90/60=1.5$ hours. The units tell you to divide distance by speed. Multiplying would give square kilometers per hour, which is a different kind of quantity.

## Worked example

Double every edge of a solid cube. Each face becomes four times as large, while the volume becomes eight times as large. In general, multiplying every length by $k$ multiplies area by $k^2$ and volume by $k^3$. This is the **square–cube law**.

Suppose the cube represents a block of uniform material. Its mass grows with volume, and the area available for a coating grows with surface area. A scaled block therefore needs eight times the material and four times the coating when $k=2$, assuming the same density and coating use per unit area. Ratios can change when the shape remains identical.

## Try it

- **Practice.** A cube's edge length triples. By what factors do surface area, volume, and the ratio of area to volume change?
- **Stretch.** A vehicle travels at speed $v$ for time $t$. If the distance is modeled as $Cv^a t^b$, where $C$ is a pure number, use units to find $a$ and $b$. What does this say about $C$?

## Check your work

**Practice.** The area factor is 9, the volume factor is 27, and the ratio changes by a factor of $1/3$.

**Stretch.** The length unit appears with power $a$, so $a=1$. The time unit appears with power $b-a$, so $b=1$. Units give the form $Cvt$. If $v$ is the constant speed over the full time, the definition of speed supplies $C=1$.

# Chapter 28 — Compute, Simulate, and Check

## Start here

A simulation repeatedly applies a rule to see what happens. A computation can answer a question quickly and still mislead you through rounding, a faulty implementation, or a poor model. Test the simplest cases you can solve by hand.

## Worked example

Suppose a calculator rounds to four significant digits. Evaluate $\sqrt{10001}-100$. The square root is about 100.005, which rounds to 100.0. Subtracting gives zero. The rounding error was small relative to the square root and large relative to the difference you wanted. This is **cancellation**.

Multiply by the conjugate to rewrite the expression before evaluating it.

$$\sqrt{10001}-100=\frac{10001-10000}{\sqrt{10001}+100}=\frac{1}{\sqrt{10001}+100}.$$

With the same rounded square root, the result is about 0.005. An exact algebraic rewrite improved the rounded computation. To check a simulation, distinguish **verification** (did the computation follow your rules?) from **validation** (do those rules describe the thing you care about?).

## Try it

- **Practice.** Rewrite $\sqrt{n+1}-\sqrt n$ so it avoids subtracting nearly equal square roots for large positive $n$.
- **Stretch.** Estimate the chance that two fair six-sided dice sum to 7 by simulation. Give a way to verify the answer exactly, then say what evidence you would need to validate the fair, independent dice model for a real pair.

## Check your work

**Practice.** The equivalent expression is $1/(\sqrt{n+1}+\sqrt n)$.

**Stretch.** Simulate independent pairs of uniform integers from 1 to 6 and count the fraction whose sum is 7. Exactly six of the 36 equally likely ordered pairs work, giving $1/6$. For real dice, collect repeated pairs and compare observed face frequencies and joint frequencies with the model. A close match is evidence with sampling uncertainty.

# Chapter 29 — Ask What the Data Can Tell You

## Start here

Two routes have the same average travel time. One is usually steady, and the other alternates between very fast trips and long delays. The average alone hides the difference. Ask how the observations were produced and what statistic answers your question.

## Worked example

Compare success rates for two practice methods on easy and hard problems.

| Method | Easy | Hard | Total |
|---|---:|---:|---:|
| A | 9 of 10 | 30 of 100 | 39 of 110 |
| B | 80 of 100 | 2 of 10 | 82 of 110 |

A has a higher success rate within each difficulty group. B has a higher pooled rate because B attempted many more easy problems. This reversal is an example of **Simpson's paradox**. A pooled rate weights groups according to how often they appear. Whether you should compare within groups depends on the question. These counts alone also leave open whether a method caused a difference in success.

## Try it

- **Practice.** Compute the four within-group percentages and the two pooled percentages.
- **Stretch.** Imagine each method is assigned to an equal mix of easy and hard problems, and the within-group rates stay the same. Predict each pooled rate. Which assumption would you test before acting on the prediction?

## Check your work

**Practice.** For A the rates are 90%, 30%, and about 35.5%. For B they are 80%, 20%, and about 74.5%.

**Stretch.** Equal weights give 60% for A and 50% for B. Test whether the within-group rates carry over to the new population. Check whether assignment, preparation, or differences within the difficulty groups could affect success.

# Chapter 30 — Follow Feedback Through a System

## Start here

A queue grows whenever more people arrive than can be served. Even if the server works at full speed, the queue can keep growing. The result depends on how arrivals, service, and the current backlog interact.

## Worked example

At the start of each round there are $q$ waiting customers. Four arrive, and the team serves up to five. The next queue is $\max(0,q-1)$. Starting with six people, the queues after each round are $5,4,3,2,1,0$. Once the queue is zero, arrivals are handled in the same round.

Now suppose a long queue attracts walk-up customers who assume the service is popular. When $q\ge5$, six arrive instead of four. Above the threshold the queue grows by one per round, which keeps it above the threshold. The output affects the next input. That is **feedback**. In this model, queues starting at 4 and 5 move in opposite directions.

## Try it

- **Practice.** With the feedback rule, write the next three queue sizes starting from 4 and from 5.
- **Stretch.** If a second worker raises total service capacity to six, what happens above the threshold? Find the smallest whole-number capacity that reduces every positive queue under this model.

## Check your work

**Practice.** From 4, the sizes are 3, 2, 1. From 5, they are 6, 7, 8.

**Stretch.** With capacity six, a queue at or above five stays the same because arrivals equal service. Capacity seven makes every positive queue decrease, regardless of which arrival rate applies.

## When the parts hide the whole

Three voters rank options A, B, and C. Their orders are A–B–C, B–C–A, and C–A–B, with the best option first. A beats B by two votes to one. B beats C by the same margin. C also beats A by that margin. The majority preference cycles even though each person's ranking has a fixed order.

This is an example of **emergence**. A rule for combining individual choices produces a property you cannot see by inspecting any one person. To check a claim about a group, write down how the group result is made and test a tiny case.

## Part IV checkpoint

Choose a question with a measurable answer, such as how many people a line can serve in 30 minutes. Build a simple model, state its assumptions, and calculate a plausible range. Propose an observation that could distinguish two reasonable models. Explain what the observation would establish and what uncertainty would remain.

### Further challenge

A desk can serve five customers per minute. Compare two six-minute arrival schedules, $(5,5,5,5,5,5)$ and $(0,10,0,10,0,10)$. In each minute, add arrivals before serving people. Compute the largest queue left after service and the total number of customer-minutes of waiting, counted by adding the six after-service queues. Then test whether capacity six prevents all waiting under either schedule. Explain what the average arrival rate does and does not determine.
