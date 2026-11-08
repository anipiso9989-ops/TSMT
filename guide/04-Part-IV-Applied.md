# Part IV — Applied Mathematical Reasoning

> *In pure mathematics the problem is given. In applied mathematics the problem must be constructed — and the construction, not the solution, is where most of the errors live.*

**Chapters in this part**

25. Modeling: World → Mathematics → World
26. Estimation and Fermi Reasoning
27. Dimensional Analysis and Scaling
28. Computation, Simulation, and Numerical Thinking
29. Uncertainty, Data, and Inference
30. Systems Thinking

**What changes in the applied setting**

Four things, and each one breaks a habit that pure training instills:

1. **There is no correct answer, only an adequate one.** Adequacy is relative to a purpose, and the purpose must be stated before the model can be judged.
2. **The assumptions are the model.** In pure mathematics the hypotheses are given and true by stipulation. In applied work they are guesses, and they carry all the risk.
3. **Error is part of the answer.** A number without an error bar is not a result. An estimate without a range is not an estimate.
4. **The system fights back.** Parts interact, feedback loops appear, and the decomposition that made the problem tractable may be the thing that makes the answer wrong.

---

# Chapter 25 — Modeling: World → Mathematics → World

## 1. Core Idea

**Modeling** is the construction of a mathematical structure $\mathcal{M}$ together with an interpretation that maps statements about $\mathcal{M}$ to statements about a target system $S$.

A model is therefore a *conditional*: *if* the target behaves as the assumptions say, *then* the theorems of $\mathcal{M}$ hold of the target. The assumptions are not a preliminary; they **are** the model. Two models with the same equations and different assumptions are different models.

The cycle:

$$\text{question} \to \text{entities and relations} \to \text{assumptions} \to \text{model} \to \text{analysis} \to \text{prediction} \to \text{comparison} \to \text{revision}$$

The cycle is the point. A model is not a thing you build once; it is a hypothesis you iterate. The iteration is driven by **discrepancy**: where the prediction and the observation disagree is where the model is wrong, and the *pattern* of disagreement tells you which assumption to revise.

**Principle signature.** The question is about a real system; the data are noisy or incomplete; the answer must be actionable; and someone will make a decision based on it.

## 2. First Principles

**Models are partial homomorphisms.** A model preserves *some* structure of the target and discards the rest. The discarded structure is the model's **scope**: the set of questions it can answer. A model that is excellent for one question can be worthless for another, with no contradiction — the difference is which structure was preserved.

**All models are wrong; some are useful.** The aphorism is not cynicism; it is a criterion. Usefulness is relative to a purpose, so the first question about any model is not "is it true?" but "is it adequate for this decision?".

**The three sources of model error.**

1. **Structural error:** the equations have the wrong form (linear where the system is nonlinear; deterministic where it is stochastic).
2. **Parameter error:** the form is right but the constants are wrong or uncertain.
3. **Observation error:** the data used to calibrate or validate are noisy, biased, or selected (→ Ch. 29).

These have different remedies. Better data fixes (3); better calibration fixes (2); only a different model fixes (1). Confusing them is the most common failure in applied work: adding data to a structurally wrong model makes the wrong answer more precise.

**Verification versus validation.** *Verification* asks: does the implementation solve the equations I wrote? *Validation* asks: are these the right equations for the target? A model can be perfectly verified and completely invalid. Both are necessary; neither implies the other.

**Sensitivity is part of the result.** A prediction that changes drastically when a parameter moves by 10% is not a prediction; it is a coin flip dressed as a number. Sensitivity analysis — varying each assumption and re-running — is not optional.

## 3. Reasoning Process

1. **State the decision the model must support.** Not "understand X" but "should we do A or B, and by how much?". The decision determines the required precision and the relevant structure.
2. **Name the entities and the relations.** What are the objects, what interacts with what, what is conserved?
3. **Write the assumptions as a numbered list.** Each assumption should be a sentence that could be false. Rank them by confidence.
4. **Build the simplest model that could possibly answer the question.** Simplicity is a feature: it makes the assumptions visible and the analysis tractable.
5. **Analyze.** Solve, simulate, or bound. Derive the qualitative behavior (thresholds, equilibria, growth) before the numbers.
6. **Compare with data or with a limiting case.** Does it reproduce a known case? Does it satisfy a conservation law? Does it have the right units (→ Ch. 27)?
7. **Stress-test.** Vary each assumption by a plausible amount. Identify which ones the conclusion depends on.
8. **Report with scope conditions.** "Under assumptions 1–5, the model predicts X ± δ; the conclusion is sensitive to assumption 3, which is the weakest link."

## 4. Demonstrations

### Demonstration 25.1 — Two models of the same phenomenon

*Question.* How does a quantity $N(t)$ — a population, a rumor's spread, the adoption of a product — grow over time?

*Model A (unlimited growth).* Assumption: the growth rate is proportional to the current size.
$$\frac{dN}{dt} = rN \implies N(t) = N_0 e^{rt}.$$
*Qualitative behavior:* exponential growth; doubling time $\ln 2 / r$, independent of $N_0$; unbounded.

*Model B (limited growth).* Assumption: the growth rate is proportional to the current size *and* to the remaining capacity $1 - N/K$, where $K$ is the carrying capacity.
$$\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right) \implies N(t) = \frac{K}{1 + \left(\frac{K-N_0}{N_0}\right)e^{-rt}}.$$

*Check.* At $t=0$: $N = K/\left(1 + (K-N_0)/N_0\right) = N_0$ ✓. As $t\to\infty$: $N \to K$ ✓. And substituting into the ODE verifies the solution.

*Qualitative behavior:* initial exponential growth with rate $r$; inflection at $N = K/2$; saturation at $K$; the growth rate is maximal at $K/2$.

**What to notice.** The two models agree at small $t$ (both $\approx N_0 e^{rt}$) and diverge completely at large $t$. **The data that distinguishes them is precisely the data that is hardest to get: the long-time behavior.** This is a general fact about model discrimination — models that agree on the easy data differ on the hard data, and the hard data is expensive.

The choice between them is not a matter of mathematical taste; it is a claim about the target. If the target has a finite capacity (a market, a population with limited food, a finite social network), Model B is structurally correct and Model A is not, regardless of how well A fits the early data.

### Demonstration 25.2 — Same data, different models, different predictions

*Data.* $f(0) = 1$, $f(1) = 2$, $f(2) = 4$.

*Model A (exponential).* $f(n) = 2^n$. Fits all three points.

*Model B (quadratic).* $f(n) = \frac12 n^2 + \frac12 n + 1$. Check: $f(0)=1$ ✓, $f(1)=1/2+1/2+1=2$ ✓, $f(2)=2+1+1=4$ ✓.

*Predictions at $n = 10$:*
$$f_A(10) = 1024, \qquad f_B(10) = 50 + 5 + 1 = 56.$$

**What to notice.** Both models fit the data exactly; they differ by a factor of $18$ at $n=10$. **Three data points cannot distinguish a two-parameter family from a one-parameter family**, and the difference is invisible in the fitting range. This is the mathematical core of overfitting (→ Ch. 29) and of the danger of extrapolation.

The resolution is not "use the simpler model" (Model B has more parameters but is not thereby wrong). The resolution is **structural knowledge**: if the mechanism is multiplicative (each unit produces more units), the exponential is right; if the mechanism is additive with a quadratic correction, Model B is right. Data alone cannot decide; data plus mechanism can.

### Demonstration 25.3 — A model that reveals a threshold

*Model.* A single server with arrivals at rate $\lambda$ and service rate $\mu$ (jobs per unit time), with random arrivals and service times (M/M/1). Let $\rho = \lambda/\mu$ be the **utilization**.

*Result.* The expected time a job spends waiting in the queue is
$$W_q = \frac{\rho}{\mu - \lambda} = \frac{\rho}{\mu(1-\rho)}.$$

*Behavior.* As $\lambda \to \mu$ (utilization $\to 1$), $W_q \to \infty$. Numerically, with $\mu = 1$:

| $\rho$ | $W_q$ |
|---|---|
| 0.5 | 1 |
| 0.8 | 4 |
| 0.9 | 9 |
| 0.95 | 19 |
| 0.99 | 99 |

**What to notice.** A 10% increase in load from $\rho=0.9$ to $\rho=0.99$ multiplies the wait by $11$. The nonlinearity is not a modeling artifact; it is the reason queueing systems are fragile near capacity, and it is a *qualitative* prediction that survives changes in the detailed assumptions (the same $1/(1-\rho)$ blowup appears in most single-server models).

**The modeling lesson.** The value of the model was not the number $9$; it was the discovery of the **threshold** and the **functional form** of the blowup. A model that gets the qualitative behavior right is useful even when its constants are wrong, because the qualitative behavior is what drives decisions (provision capacity for peak load, not average load).

## 5. Connections

- **← Ch. 1.** A model is a structure plus an interpretation; the transfer principle tells you what the model's theorems say about the target.
- **← Ch. 6.** The dependency audit of a model is the list of assumptions, ranked by confidence.
- **← Ch. 18.** Generalizing a model is changing its scope; specializing it is calibrating it.
- **→ Ch. 26.** Estimation supplies the parameters and the sanity checks.
- **→ Ch. 27.** Dimensional analysis constrains the *form* of the model before any data is collected.
- **→ Ch. 28.** Simulation is the analysis tool when the model has no closed form.
- **→ Ch. 29.** Validation is inference from noisy data; the failure modes are statistical.

## 6. Limitations

**The map is not the territory.** Every model discards structure, and the discarded structure is exactly where surprises come from. A model's success in its scope is not evidence of correctness outside it.

**Fitting is not validation.** A model with enough parameters can fit any finite dataset. Validation requires *out-of-sample* prediction, preferably on data the model was not tuned on.

**Models can be self-fulfilling.** Economic and social models change the system they describe (agents react to the model). This is a failure mode with no analogue in physics, and it invalidates the standard validation logic.

**Complexity is not realism.** Adding detail makes a model harder to analyze and its assumptions harder to see, without necessarily improving prediction. The right complexity is the minimum that captures the mechanism the decision depends on.

**Parameter uncertainty can dominate structural uncertainty.** Sometimes the model form is right and the constants are so uncertain that the prediction is useless. Distinguishing this from structural error requires sensitivity analysis.

## 7. Applications

- **Epidemiology.** Compartmental models (SIR) are the canonical example: simple structure, identifiable parameters, qualitatively correct thresholds (the basic reproduction number $R_0$), and well-known failures when heterogeneity and behavior change are ignored.
- **Finance.** Derivative pricing models are conditional on no-arbitrage and market completeness; the 2008 crisis was a failure of the assumptions (independence, liquidity, Gaussian tails), not of the mathematics.
- **Climate.** General circulation models are high-dimensional simulations validated on historical data; the structural uncertainty (cloud feedback) dominates the parameter uncertainty.
- **Engineering.** A digital twin is a model calibrated to a specific asset; its value depends on the sensor data quality and on the model's scope.
- **Operations.** Queueing and inventory models determine capacity and safety stock; the threshold behavior of Demonstration 25.3 is why capacity planning is nonlinear.
- **Machine learning.** A trained model is a model in this sense: structure (architecture) plus parameters, validated out-of-sample, with a scope (the training distribution).

## 8. Mastery Criteria

You have this chapter when you can:

1. Write a model as an explicit list of numbered assumptions plus a mathematical structure.
2. State the decision the model is meant to support, and judge adequacy relative to it.
3. Distinguish structural, parameter, and observation error, and prescribe the right remedy for each.
4. Produce two models of the same phenomenon that agree on some data and disagree on other data, and say which data discriminates.
5. Perform a sensitivity analysis and identify the weakest assumption.
6. State a model's scope conditions and the observations that would falsify it.

**Diagnostic question.** "What would have to be true for this model's prediction to be wrong?" A learner who can answer with a specific assumption and a specific observation has understood the model.

### AI Tutor Brief

- **Generate:** (i) phenomena to be modeled, with a requirement to state assumptions before equations; (ii) pairs of models fitting the same data with divergent predictions; (iii) sensitivity-analysis tasks (vary an assumption, recompute); (iv) "which error is this?" diagnoses (structural vs parameter vs observation).
- **Probe misconceptions:** fitting = validation; more detail = more accurate; a model's success in one regime transfers to another; the equations are the model (they are not — the assumptions are).
- **Transfer distance:** maximal. Every problem should be an unfamiliar system.
- **Do not** accept a model without its assumption list, its scope, and its falsification condition.

---

# Chapter 26 — Estimation and Fermi Reasoning

## 1. Core Idea

**Fermi reasoning** is the construction of a quantitative answer from rough, individually unreliable estimates, in a way that is accurate to within an order of magnitude.

It works because of two structural facts:

1. **Decomposition converts an impossible question into several easy ones.** "How many piano tuners are in Chicago?" is unanswerable directly; "how many households, what fraction own a piano, how often is it tuned, how many tunings per tuner per day?" are each answerable to within a factor of two.
2. **Multiplicative errors partially cancel.** If each of $k$ factors is off by a factor of $2$ in a random direction, the product is off by roughly $2^{\sqrt{k}}$ — much less than $2^k$. Working in logarithms makes this explicit: errors add, and independent errors add in quadrature.

Estimation is not a lesser form of computation. It is the only form of computation available when the data do not exist, and it is the primary defense against quantitative nonsense.

**Principle signature.** The question is quantitative but the data are unavailable, expensive, or disputed; or you need to check whether a claimed number is plausible before investing in a precise calculation.

## 2. First Principles

**Logarithmic arithmetic.** Work with powers of $10$. The useful anchors:

$$2^{10} \approx 10^3, \qquad e^3 \approx 20, \qquad \pi^2 \approx 10, \qquad \sqrt{10} \approx 3.16.$$

$$1 \text{ year} \approx \pi \times 10^7 \text{ s} \approx 3.15\times10^7\text{ s}.$$

**Bounds beat point estimates.** An upper bound and a lower bound that agree to within a factor of $10$ are usually enough. Bounds are also more robust: they are valid even when the point estimate is wrong.

**The 70 rule.** A quantity growing at $p\%$ per year doubles in about $70/p$ years. (Because $\ln 2 \approx 0.693$ and $\ln(1+p/100) \approx p/100$.)

**Independent routes.** Estimate the same quantity two ways, with different decompositions. If the two answers agree within a factor of $3$, you have a real estimate. If they disagree by $10^3$, one decomposition has a structural error, and finding it is the valuable part.

**Calibration.** Estimation improves with feedback. Keep a record of estimates and actual values; the errors are usually systematic (you consistently overestimate one kind of quantity), and systematic errors can be corrected.

## 3. Reasoning Process

1. **Write the quantity with its units.** "$X$ kilograms", not "$X$".
2. **Decompose multiplicatively** into factors you can estimate independently. Aim for 3–6 factors.
3. **Estimate each factor to one significant figure**, with a range. Use anchors you know (a person is ~$10^2$ kg, a year is ~$3\times10^7$ s, a city block is ~$10^2$ m).
4. **Combine in log space.** Add the exponents; multiply the mantissas.
5. **Sanity-check with a second decomposition.** If the two routes disagree by more than $10\times$, find the error.
6. **State the answer as a range**, with the dominant uncertainty named.

## 4. Demonstrations

### Demonstration 26.1 — The mass of the atmosphere

*Question.* What is the total mass of Earth's atmosphere?

*Decomposition.* Surface pressure is the weight of the atmosphere per unit area:
$$p = \frac{Mg}{A} \implies M = \frac{pA}{g}.$$

*Inputs.* $p \approx 1.01\times10^5\ \mathrm{Pa}$ (known). $g \approx 9.8\ \mathrm{m/s^2}$. Earth's radius $R \approx 6.37\times10^6\ \mathrm{m}$, so
$$A = 4\pi R^2 \approx 4\pi \times 4.06\times10^{13} \approx 5.1\times10^{14}\ \mathrm{m^2}.$$

*Combine.*
$$M \approx \frac{1.01\times10^5 \times 5.1\times10^{14}}{9.8} \approx \frac{5.15\times10^{19}}{9.8} \approx 5.3\times10^{18}\ \mathrm{kg}.$$

*Check.* The accepted value is about $5.15\times10^{18}$ kg. The estimate is within 3% — and it required no knowledge of the atmosphere's composition, temperature profile, or height.

**What to notice.** The estimate is accurate because the *physics* gave an exact relation ($p = Mg/A$), not because the inputs were precise. **A good decomposition can turn a rough estimate into an accurate one.** This is the ideal case: the structure does the work, and the numbers only need one significant figure.

### Demonstration 26.2 — How many digits in $100!$?

*Question.* Estimate the number of decimal digits of $100!$.

*Decomposition.* The number of digits is $\lfloor \log_{10}(100!)\rfloor + 1$. By Stirling's approximation,
$$\log_{10}(n!) \approx n\log_{10}\frac{n}{e} + \frac12\log_{10}(2\pi n).$$
With $n = 100$: $\log_{10}(100/e) = 2 - \log_{10} e = 2 - 0.4343 = 1.5657$. So
$$100 \times 1.5657 = 156.57, \qquad \frac12\log_{10}(2\pi\cdot100) = \frac12\log_{10}(628.3) \approx \frac12(2.798) = 1.399.$$
Total: $156.57 + 1.40 = 157.97$. Hence $\log_{10}(100!) \approx 157.97$, so $100!$ has $\lfloor 157.97 \rfloor + 1 = 158$ digits.

*Check.* The exact value of $100!$ has 158 digits. ✓

**What to notice.** Stirling's formula is doing the real work, and the estimation is really an *asymptotic* calculation (→ Ch. 22). The distinction between estimation and asymptotics is one of intent: asymptotics asks for the growth law with an error term; estimation asks for a number to one significant figure. Here they coincide.

Note also the correction term: without $\frac12\log_{10}(2\pi n)$, the estimate would be $156.57$, giving $157$ digits — off by one, which matters when the question is "how many digits". **When the answer is an integer near a boundary, the correction term is not optional.**

### Demonstration 26.3 — Detecting a nonsense claim

*Claim.* "Our new data center processes one billion customer transactions per day on a single server."

*Check.* One billion transactions per day is
$$\frac{10^9}{24\times3600} \approx \frac{10^9}{8.64\times10^4} \approx 1.16\times10^4 \text{ transactions per second}.$$
That is about $11{,}600$ transactions per second, i.e. about $86$ microseconds per transaction, sustained, on one machine, with no time for network, storage, or failures.

*Verdict.* Physically possible only for extremely simple transactions (an in-memory key-value update), and implausible for anything involving a database write, a network round trip, or a consistency protocol — each of which costs hundreds of microseconds to milliseconds. The claim is off by one to three orders of magnitude for any realistic workload.

**What to notice.** The check took thirty seconds and required no domain expertise beyond "a network round trip is ~$10^{-4}$ s". **The most valuable use of estimation is not producing numbers but rejecting them.** A quantitative claim that survives a thirty-second order-of-magnitude check is worth taking seriously; one that does not is worth ignoring, regardless of the credentials of the source.

### Demonstration 26.4 — Two routes, and what disagreement means

*Question.* How many cells are in the human body?

*Route A (mass per cell).* A typical human cell is about $10\ \mu\mathrm{m}$ across, so its volume is about $(10^{-5})^3 = 10^{-15}\ \mathrm{m^3}$, and with density $\approx 10^3\ \mathrm{kg/m^3}$ its mass is about $10^{-12}\ \mathrm{kg}$. A $70$ kg human therefore contains about
$$N \approx \frac{70}{10^{-12}} = 7\times10^{13} \text{ cells}.$$

*Route B (cell count by type).* Red blood cells are about $5\times10^{12}$ per liter of blood and there are about $5$ liters, giving $2.5\times10^{13}$; add roughly the same again for everything else, giving $\sim 5\times10^{13}$.

*Agreement.* Both routes give $\sim 10^{13}$–$10^{14}$, consistent with the accepted value of about $3.7\times10^{13}$ (bacterial cells add more, but they are much smaller).

**What to notice.** The two routes used different decompositions and agreed within a factor of $2$. That agreement is what licenses confidence. **A single route gives a number; two routes give an estimate.** When the routes disagree, the disagreement is the finding: it locates the factor that one route got structurally wrong.

## 5. Connections

- **← Ch. 7.** Anatomy determines which quantity is worth estimating.
- **← Ch. 22.** Asymptotics is estimation with an error term; the same logarithms are used.
- **→ Ch. 27.** Dimensional analysis constrains the decomposition before any numbers are chosen.
- **→ Ch. 28.** Simulation results should be sanity-checked by estimation before being trusted.
- **→ Ch. 29.** Estimation is the antidote to statistical claims that are numerically absurd.
- **→ Ch. 35.** Research judgment includes knowing which sub-problems are worth an estimate before a computation.

## 6. Limitations

**Estimation cannot distinguish close alternatives.** If two options differ by 20%, estimation is useless; you need measurement or computation. Estimation is for order-of-magnitude decisions.

**Systematic bias does not cancel.** Multiplicative errors cancel only if they are independent and symmetric. If you consistently underestimate a class of quantities (a common pattern), the errors compound. Calibration is the remedy.

**The decomposition can be structurally wrong.** A correct arithmetic combination of wrong factors gives a confident wrong answer. The second route is the defense.

**Fermi reasoning can create false confidence.** A number with a range looks more authoritative than a guess, but the range may be fictional. State the uncertainty honestly, and distinguish "I bounded this" from "I guessed this".

**Some quantities are not decomposable.** If you have no anchor for any factor, no decomposition helps. In that case, the honest answer is "unknown, and here is what it would take to know".

## 7. Applications

- **Engineering feasibility.** Before designing a system, estimate its power, bandwidth, mass, and cost. If the estimate is off by $100\times$, the design is dead and no detailed analysis will save it.
- **Business and policy.** Market sizing, cost projections, and policy impact estimates are Fermi problems; the value is in identifying which factor dominates the uncertainty.
- **Science.** Order-of-magnitude estimates decide which experiments are worth running and which theories are worth testing.
- **Medicine.** Dosage, incidence, and risk estimates are order-of-magnitude reasoning with safety factors.
- **Software.** Back-of-the-envelope capacity planning (requests per second, storage per user, latency budgets) is the standard first step in system design.
- **Personal decisions.** Time, money, and energy budgets are Fermi problems; most errors come from ignoring a factor, not from misestimating one.

## 8. Mastery Criteria

You have this chapter when you can:

1. Decompose a quantity into 3–6 independently estimable factors and combine them in log space.
2. Produce two independent routes to the same quantity and interpret their agreement or disagreement.
3. Reject a quantitative claim by a thirty-second order-of-magnitude check.
4. Use anchors ($2^{10}\approx10^3$, a year $\approx 3\times10^7$ s, a person $\approx 10^2$ kg) fluently.
5. State an estimate as a range with the dominant uncertainty identified.
6. Distinguish "bounded" from "guessed", and say which you have done.

**Diagnostic question.** "Is this number plausible?" A learner who reaches for a decomposition and a bound has the skill. A learner who says "it depends" has not.

### AI Tutor Brief

- **Generate:** (i) Fermi questions with no lookup available; (ii) implausible claims to be rejected with a calculation; (iii) two-route estimation tasks where the routes disagree; (iv) estimates requiring a correction term (Stirling, log corrections) where the naive answer is off by one.
- **Probe misconceptions:** single-route confidence; ignoring units; treating a point estimate as exact; forgetting the correction term when the answer is an integer near a boundary.
- **Transfer distance:** maximal. Use quantities from physics, biology, economics, and software.
- **Do not** require precision. Grade the decomposition, the anchors, and the honesty of the range.

---

# Chapter 27 — Dimensional Analysis and Scaling

## 1. Core Idea

Physical quantities carry **dimensions** — mass $M$, length $L$, time $T$, and others — and any equation relating them must be **dimensionally homogeneous**: both sides must have the same dimensions.

This constraint is far stronger than it looks. It often determines the *form* of a physical law up to a dimensionless constant, without solving any equations. The procedure is the **Buckingham $\Pi$ theorem**:

> If a phenomenon depends on $n$ dimensional variables involving $k$ independent dimensions, then the variables can be combined into $n-k$ independent **dimensionless groups**, and the law relating them is a relation among those groups.

**Scaling** is the corollary: when all lengths are multiplied by $\lambda$, quantities transform as powers of $\lambda$, and the exponents are determined by the dimensions. This is how you predict how a design behaves when it is scaled up — and why some designs cannot be scaled up at all.

**Principle signature.** A physical law is sought; the variables are known but the equation is not; or a design must be scaled; or a quantity's dependence on size, speed, or temperature is at issue.

## 2. First Principles

**Dimensions form a vector space.** Each quantity has a dimension vector in the basis $(M, L, T, \Theta, \ldots)$. Multiplication adds vectors; powers multiply them; addition requires equal vectors. Dimensionless quantities have the zero vector.

**Homogeneity forces the form.** If $y = f(x_1,\dots,x_n)$ and the dimensions are known, then $f$ must be such that the dimension vectors match. In the simplest case, $f$ is a monomial $C\prod x_i^{a_i}$, and the exponents solve a linear system.

**The Buckingham $\Pi$ theorem, concretely.** With $n$ variables and $k$ independent dimensions, there are $n-k$ dimensionless groups $\Pi_1,\dots,\Pi_{n-k}$, and the law has the form $\Pi_1 = \Phi(\Pi_2,\dots,\Pi_{n-k})$ for some function $\Phi$ of $n-k-1$ arguments. Dimensional analysis determines the groups but **not** the function $\Phi$ — that requires physics, experiment, or a deeper theory.

**Scaling laws.** If a system is scale-invariant (no intrinsic length scale), then the dimensionless groups are constant, and every quantity is a power law in the scale. The exponents are the **critical exponents**, and they are determined by dimensional analysis plus the assumption of scale invariance.

**The limits.** Dimensional analysis cannot determine dimensionless constants ($2\pi$, $1/2$, the fine-structure constant). It cannot distinguish regimes (laminar vs turbulent) — the regime is set by the *magnitude* of a dimensionless group, not its existence. And it requires the correct variable list: omit a relevant variable and the analysis gives a wrong (but dimensionally consistent) law.

## 3. Reasoning Process

1. **List the variables** that could plausibly matter, with their dimensions. Be generous at first, then prune by physical reasoning.
2. **Write the dimension matrix** (rows = dimensions, columns = variables) and find its rank $k$.
3. **Form the dimensionless groups.** Solve for the null space: each null vector gives a group $\prod x_i^{a_i}$.
4. **Write the law** as a relation among the groups.
5. **Determine the function** by experiment, by a limiting case, or by a deeper theory.
6. **Check the scaling.** How does each quantity change when the scale changes? Are the exponents physically sensible?
7. **Check the regime.** Which dimensionless group is large or small, and does the law change when it crosses a threshold?

## 4. Demonstrations

### Demonstration 27.1 — The period of a pendulum

*Question.* A pendulum of length $L$, bob mass $m$, in gravity $g$, has period $T$. What is the form of $T$?

*Variables and dimensions.* $T\,[T]$, $L\,[L]$, $g\,[L T^{-2}]$, $m\,[M]$. Four variables, three independent dimensions ($M,L,T$), so $4-3 = 1$ dimensionless group.

*Find the group.* Seek exponents $a,b,c,d$ with
$$T^a L^b g^c m^d \text{ dimensionless} \implies [T]^{a}\,[L]^{b}\,[LT^{-2}]^{c}\,[M]^{d} = 1.$$
Matching: $M$: $d = 0$. $T$: $a - 2c = 0$. $L$: $b + c = 0$. Take $c = 1$: then $a = 2$, $b = -1$, $d = 0$. So the group is
$$\Pi = \frac{T^2 g}{L}.$$

*Conclusion.* $\Pi = \Phi(\text{no other groups}) = \text{constant}$, so
$$T = C\sqrt{\frac{L}{g}}.$$

**What to notice.** Three things were obtained without solving any differential equation:

1. **The mass does not appear.** The exponent $d=0$ is forced, because $m$ is the only variable carrying mass and the group must be dimensionless. This is a real physical prediction, and it is correct (to the extent that the pendulum is ideal).
2. **The scaling $T \propto \sqrt L$** is forced.
3. **The constant $C$ is not determined.** For small oscillations, $C = 2\pi$, but that requires the small-angle approximation and the ODE. Dimensional analysis gives the form; the dynamics gives the constant.

This is the characteristic yield of the method: **the exponents are free, the constant is not.**

### Demonstration 27.2 — The square–cube law

*Question.* How does the strength of a structure scale with its size?

*Analysis.* Strength is proportional to the cross-sectional area of the load-bearing material: $S \propto L^2$. Weight is proportional to volume: $W \propto L^3$. Hence the **strength-to-weight ratio** scales as
$$\frac{S}{W} \propto \frac{L^2}{L^3} = \frac{1}{L}.$$

*Consequence.* A structure scaled up by a factor of $10$ has $1/10$ the relative strength. This is why large animals have disproportionately thick bones (Galileo's observation), why insects can lift many times their body weight while elephants cannot, and why skyscrapers cannot simply be scaled-up houses.

*Refinement.* If the bone must support a weight that also scales as $L^3$, and the bone's strength scales as its cross-section $d^2$ where $d$ is the bone diameter, then $d^2 \propto L^3$, so $d \propto L^{3/2}$. This is the **3/2 scaling law** for bone dimensions, and it is observed across species.

**What to notice.** The scaling law is a *constraint*, not a prediction of the exact shape. It says: any structure that supports its own weight and is scaled up must violate geometric similarity. The exponent $3/2$ came from matching two scaling relations, not from any detailed mechanics. **Scaling arguments tell you what cannot be scaled, which is often more valuable than telling you what can.**

### Demonstration 27.3 — Kepler's third law from dimensions alone

*Question.* A planet orbits a star of mass $M$ at radius $a$. How does the period $T$ depend on $a$ and $M$?

*Variables.* $T\,[T]$, $a\,[L]$, $M\,[M]$, $G\,[L^3 M^{-1} T^{-2}]$. Four variables, three dimensions, so one group.

*Find it.* Seek $T^p a^q M^r G^s$ dimensionless:
- $M$: $r - s = 0 \implies r = s$.
- $T$: $p - 2s = 0 \implies p = 2s$.
- $L$: $q + 3s = 0 \implies q = -3s$.

Take $s = 1$: the group is $\dfrac{T^2 G M}{a^3}$. Setting it equal to a constant gives
$$T^2 = \frac{4\pi^2}{GM}\,a^3 \implies T \propto a^{3/2}.$$

**What to notice.** The $3/2$ exponent is forced by dimensions; the constant $4\pi^2$ is not (it comes from the circular-orbit solution). The mass dependence $T \propto M^{-1/2}$ is also forced, and it is the reason a satellite's period depends on the central mass but not on its own mass.

This is one of the most striking successes of dimensional analysis: a law that Newton derived from a force law and Kepler inferred from data is *also* implied by the dimensions of $G$ alone. That is strong evidence that the law is over-determined — many independent constraints point to the same form.

### Demonstration 27.4 — Where dimensional analysis stops

*Question.* What is the period of a pendulum at large amplitude?

*Failure of the naive analysis.* The group $\Pi = T^2g/L$ is still the only dimensionless combination of $T, L, g, m$. But the amplitude $\theta_0$ is also dimensionless, so it must be included: $\Pi = \Phi(\theta_0)$. Dimensional analysis gives
$$T = \sqrt{\frac{L}{g}}\,\Phi(\theta_0),$$
with $\Phi$ an unknown function.

*What is missing.* The function $\Phi$ requires the equation of motion, which gives
$$T = 2\pi\sqrt{\frac{L}{g}}\left(1 + \frac{\theta_0^2}{16} + O(\theta_0^4)\right).$$
So the period *increases* with amplitude — a fact that dimensional analysis cannot see, because it cannot determine $\Phi$.

**What to notice.** The failure is precise and instructive: dimensional analysis found the correct *scaling* and identified the correct *dimensionless argument*, but could not determine the function. **This is the general situation.** Dimensional analysis reduces the problem; it does not solve it. Knowing exactly what it leaves undetermined is what lets you combine it with a theory, an experiment, or an asymptotic expansion (→ Ch. 22).

## 5. Connections

- **← Ch. 1.** Dimensions are a structure; homogeneity is a structural constraint on laws.
- **← Ch. 18.** Scaling is generalization along the size parameter; the exponents are the general statement.
- **→ Ch. 22.** Asymptotics determines the functions that dimensional analysis leaves free, in the limits where a small parameter exists.
- **→ Ch. 25.** Dimensional analysis constrains model form before any data is collected; it is the cheapest validation available.
- **→ Ch. 26.** Estimation uses the same power-of-ten reasoning; dimensional analysis adds the exponents.
- **→ Ch. 30.** Scaling laws determine how systems behave when components are added or the system grows.

## 6. Limitations

**The variable list is the weak point.** Omit a relevant variable and the analysis is wrong but dimensionally consistent. Include an irrelevant one and you get a spurious group. Physical judgment, not mathematics, determines the list.

**Dimensionless constants are invisible.** The method cannot produce $2\pi$, $1/2$, or any pure number. If the answer requires a constant, dimensional analysis will not give it.

**Regimes are invisible.** The same dimensionless group can be small or large, and the law can change qualitatively between regimes (laminar/turbulent, elastic/plastic, subsonic/supersonic). The method gives the group; the *value* of the group determines the regime.

**Scale invariance can fail.** If there is an intrinsic length (an atomic scale, a correlation length), the scaling law has corrections, and pure power-law scaling is only asymptotic. Critical phenomena are the classic case: scaling holds only near the critical point.

**Not all laws are monomials.** The Buckingham theorem gives a relation among groups, but if the relation is not a monomial (e.g. an exponential), dimensional analysis alone cannot find it.

## 7. Applications

- **Engineering.** Every physical model is dimensionally checked; a dimensional error is the most common and most easily caught modeling mistake.
- **Fluid dynamics.** The Reynolds, Froude, and Mach numbers determine the regime; wind-tunnel testing relies on matching dimensionless groups between model and prototype.
- **Biology.** Allometric scaling (metabolic rate $\propto M^{3/4}$, lifespan $\propto M^{1/4}$) is an empirical scaling law whose explanation is an active research area.
- **Climate and geophysics.** Scaling laws for boundary layers, convection, and turbulence organize enormous parameter spaces.
- **Finance.** Scaling in market microstructure (impact $\propto$ volume$^{1/2}$) and in firm size distributions; dimensional analysis is less applicable because the "dimensions" are economic, not physical, but the scaling logic transfers.
- **Numerical methods.** Non-dimensionalization is the first step in making a simulation well-conditioned; it reveals which parameters are actually independent (→ Ch. 28).

## 8. Mastery Criteria

You have this chapter when you can:

1. List variables with dimensions, compute the rank, and form the dimensionless groups.
2. Derive a scaling law and state what it does and does not determine.
3. Use a scaling argument to show that a design cannot be geometrically scaled.
4. Identify the dimensionless group that controls a regime change.
5. Explain why a dimensional analysis can be dimensionally correct and physically wrong (wrong variable list).
6. Combine dimensional analysis with an asymptotic or theoretical argument to determine the free function.

**Diagnostic question.** "What are the units, and what does homogeneity force?" A learner who can go from a variable list to a scaling law, and then say what is left undetermined, has the method.

### AI Tutor Brief

- **Generate:** (i) scaling-law derivations from variable lists; (ii) "can this be scaled up?" problems; (iii) regime-identification problems (which dimensionless group, and what happens when it crosses 1?); (iv) problems with a deliberately missing variable, to test whether the learner checks the physical reasoning.
- **Probe misconceptions:** believing dimensional analysis determines constants; forgetting dimensionless arguments (angles, ratios); assuming power-law scaling always holds; ignoring regime changes.
- **Transfer distance:** high, but constrained to settings with genuine dimensions. Use physics, engineering, and biology; for pure mathematics, use scaling of algorithms or geometric similarity.
- **Do not** accept a scaling law without the dimension matrix and the explicit statement of what remains undetermined.

---

# Chapter 28 — Computation, Simulation, and Numerical Thinking

## 1. Core Idea

Computation is a third mode of mathematical reasoning, alongside proof and experiment. It has its own epistemology:

- **It produces evidence, not proof.** A numerical result is a very large number of examples, which is strong evidence and zero proof.
- **It has its own error modes**, which are not the error modes of hand mathematics: discretization error, roundoff error, ill-conditioning, instability.
- **Its purpose is insight, not numbers.** A simulation that produces a table of numbers has failed unless it changes what you understand.

Hamming's formulation is the right standard: *the purpose of computing is insight, not numbers.* The output of a computation should be a **structural claim** — a scaling law, a threshold, a mechanism, a counterexample — not a data dump.

**Principle signature.** The model has no closed form; the exact answer is intractable; you need to know whether a conjecture is plausible before trying to prove it; or a numerical result is being used as evidence for a real-world decision.

## 2. First Principles

**Floating point is not the real numbers.** The basic operations are not associative: $(a+b)+c \ne a+(b+c)$ in general. There are finitely many numbers, with a relative spacing of about $2^{-53} \approx 10^{-16}$ (double precision). Every operation introduces a relative error of order $10^{-16}$, and errors can grow.

**Conditioning is a property of the problem.** The **condition number** measures how much the output changes for a small relative change in the input. A problem with a large condition number is *ill-conditioned*: no algorithm can solve it accurately in floating point, because the information is destroyed before the algorithm starts.

**Stability is a property of the algorithm.** A **stable** algorithm does not amplify the errors it introduces. An unstable algorithm can fail on a well-conditioned problem. Conditioning is the problem's fault; stability is the algorithm's fault.

**Discretization error.** Replacing a continuum by a grid introduces an error that scales as a power of the step size $h$: $O(h^p)$ for a $p$-th order method. The order is a property of the scheme, and it must be *measured* (halve $h$, see how the error changes) rather than assumed.

**Verification versus validation.** Verification: does the code solve the equations? (Check against exact solutions, conservation laws, convergence rates.) Validation: are these the right equations? (Compare with experiment.) These are different questions with different tests, and passing one says nothing about the other.

## 3. Reasoning Process

1. **State the insight you want.** Not "run the model" but "does the error grow exponentially?" or "where is the threshold?".
2. **Non-dimensionalize.** Reduce the parameter count; identify the small parameters (→ Ch. 27).
3. **Choose a discretization** whose order you know, and a step size you can refine.
4. **Verify.** Check convergence: halve $h$, confirm the error scales as predicted. Check conservation laws and exact solutions.
5. **Check conditioning.** Perturb the input slightly; see how much the output moves. If the problem is ill-conditioned, reformulate it.
6. **Check stability.** Look for oscillation or divergence that is not in the model.
7. **Validate.** Compare with a known case, an experiment, or an independent method.
8. **Extract the insight.** Fit a scaling law, locate a threshold, identify the mechanism. Report the structural finding, not the table.

## 4. Demonstrations

### Demonstration 28.1 — Catastrophic cancellation

*Problem.* Compute $f(x) = \sqrt{x+1} - \sqrt{x}$ for large $x$.

*Naive computation.* For $x = 10^8$, we have $\sqrt{x+1} \approx 10000.0000499999$ and $\sqrt{x} = 10000$. Their difference is about $5\times10^{-5}$. Each square root is computed with a relative error of about $10^{-16}$, i.e. an absolute error of about $10^{-12}$. The difference has absolute error $\sim 10^{-12}$ and magnitude $5\times10^{-5}$, so the **relative error is about $2\times10^{-8}$** — eight digits lost.

*Stable computation.* Rationalize:
$$f(x) = \frac{1}{\sqrt{x+1}+\sqrt{x}} \approx \frac{1}{2\sqrt x} \approx 5\times10^{-5}.$$
Now the numerator is exact ($1$), the denominator is a sum of two positive quantities of similar size, and the relative error is about $10^{-16}$.

**What to notice.** The two formulas are algebraically identical and numerically different by eight orders of magnitude in accuracy. **The error came from subtracting nearly equal numbers** — the leading digits cancelled, leaving only the noise. The cure is always the same: rewrite the expression so that no subtraction of nearly equal quantities occurs.

This is the most common numerical error in practice, and it is invisible if you only check the answer against a rough expectation (both methods give "about $5\times10^{-5}$").

### Demonstration 28.2 — Instability in a simple integrator

*Problem.* Solve $y' = -\lambda y$, $y(0)=1$, with $\lambda = 100$, using forward Euler with step $h$:
$$y_{n+1} = y_n + h(-\lambda y_n) = (1 - \lambda h)y_n \implies y_n = (1-\lambda h)^n.$$

*Stability condition.* For the numerical solution to decay (as the true solution does), we need $|1-\lambda h| \le 1$, i.e.
$$h \le \frac{2}{\lambda} = 0.02.$$

*Failure.* With $h = 0.03$: $1 - \lambda h = 1 - 3 = -2$, so $y_n = (-2)^n$ — the numerical solution *oscillates and grows* while the true solution decays to zero. The computation is not merely inaccurate; it is qualitatively wrong.

**What to notice.** The step size is not a resolution parameter here; it is a **stability** parameter. The condition $h \le 2/\lambda$ is a hard threshold, and crossing it changes the qualitative behavior. This is why stiff equations (large $\lambda$) require implicit methods, whose stability regions are unbounded.

**The general lesson.** An algorithm can be *consistent* (it approximates the right equation as $h\to0$) and still be *unstable* (the approximation diverges for finite $h$). Consistency plus stability gives convergence — the Lax equivalence principle — and neither alone suffices.

### Demonstration 28.3 — Monte Carlo, and the cost of precision

*Method.* Estimate $\pi$ by sampling uniform points in the unit square and counting the fraction inside the quarter circle: $\hat\pi = 4 \cdot (\text{hits}/N)$.

*Error.* Each sample is Bernoulli with variance $\le 1/4$, so the standard error of $\hat\pi$ is about
$$\text{SE} \approx \frac{4\cdot(1/2)}{\sqrt N} = \frac{2}{\sqrt N}.$$
To get three decimal digits (SE $\approx 5\times10^{-4}$), we need $N \approx (2/5\times10^{-4})^2 = 1.6\times10^7$ samples.

**What to notice.** The convergence is $O(N^{-1/2})$: **each additional decimal digit costs $100\times$ more samples.** This is the fundamental limitation of Monte Carlo, and it is why deterministic quadrature (which can converge much faster in low dimensions) is preferred when available.

The method's advantage is that the rate is *independent of dimension* — which is why Monte Carlo is the method of choice in high-dimensional integration, despite the poor rate.

### Demonstration 28.4 — Verification versus validation

*Scenario.* A team implements a model of heat conduction, verifies it against an exact solution (a steady-state linear profile), and gets agreement to $10^{-10}$. They then use it to predict the temperature in a new material and are wrong by 40%.

*Diagnosis.* The verification succeeded: the code solves *their equations* correctly. The validation failed: the equations assumed constant conductivity, and the new material's conductivity varies strongly with temperature. The code is right; the model is wrong.

**What to notice.** Verification and validation answer different questions, and the second is the one that matters for decisions. **A verified model can be invalid, and a validated model can be unverified** (it agrees with experiment for the wrong reason). Both tests are necessary, and they are not substitutes.

## 5. Connections

- **← Ch. 22.** Error analysis is asymptotics; convergence rates are dominant-balance arguments.
- **← Ch. 25.** Simulation is the analysis step of the modeling cycle; validation is shared.
- **← Ch. 26.** Every simulation result should be sanity-checked by estimation before it is trusted.
- **→ Ch. 29.** Numerical output is data, with all the statistical hazards of data.
- **→ Ch. 33.** Computation is the laboratory of experimental mathematics; the methodology here is the methodology there.
- **→ Ch. 35.** Knowing when a computation is trustworthy is a research-judgment skill.

## 6. Limitations

**A numerical result is not a proof.** It is evidence. For a universal claim, a million confirmations do not establish the theorem; one counterexample refutes it. Use computation to conjecture, and proof to establish (→ Ch. 31, 33).

**Chaos destroys long-term prediction.** In a chaotic system, errors grow exponentially, so the horizon of prediction is logarithmic in the precision. Doubling the precision adds only a constant to the prediction horizon.

**The discretization can be the model.** If the grid is coarse relative to the phenomenon, the simulation is solving a different problem. Convergence studies are the only defense.

**Floating point can produce plausible wrong answers.** Overflow, underflow, cancellation, and accumulation of error all produce numbers that look reasonable. Verification against exact cases is mandatory.

**Computational cost can be mistaken for difficulty.** An intractable computation may reflect a bad formulation, not an intrinsically hard problem. Reformulating (better coordinates, better conditioning) often reduces cost by orders of magnitude.

## 7. Applications

- **Scientific computing.** Weather, climate, fluid dynamics, and materials are simulation-first disciplines; verification and validation are the core methodology.
- **Engineering.** Finite element analysis, computational fluid dynamics, and circuit simulation are the design tools; the error analysis is what makes them engineering rather than guessing.
- **Machine learning.** Training is numerical optimization with all the pathologies above: ill-conditioning, instability, and the difference between training loss (verification) and test loss (validation).
- **Finance.** Monte Carlo pricing, PDE solvers, and calibration are numerical; the stability of the calibration is often the binding constraint.
- **Operations research.** Large-scale optimization is numerical; the conditioning of the LP determines whether the solution is trustworthy.
- **Experimental mathematics.** Computation discovers conjectures (identities, patterns, counterexamples) that are then proved; this is the subject of Chapter 33.

## 8. Mastery Criteria

You have this chapter when you can:

1. Identify catastrophic cancellation and rewrite an expression to avoid it.
2. Determine the stability condition for a simple explicit scheme, and explain what happens when it fails.
3. Distinguish conditioning from stability, and give an example of each.
4. Estimate the cost of achieving a given precision with a method of known order.
5. Design a convergence study and interpret the observed error scaling.
6. Distinguish verification from validation, and design a test for each.

**Diagnostic question.** "Your simulation agrees with the exact solution. Are you done?" A learner who says "that's verification; now validate" has the epistemology.

### AI Tutor Brief

- **Generate:** (i) cancellation problems to be rewritten; (ii) stability-condition derivations for explicit schemes; (iii) precision-versus-cost calculations (Monte Carlo, quadrature); (iv) "verify or validate?" scenarios; (v) chaos/error-growth problems.
- **Probe misconceptions:** "the computer says so, therefore it is true"; confusing precision with accuracy; assuming a fine grid implies a correct model; treating consistency as convergence.
- **Transfer distance:** high. Test in numerical analysis, optimization, and scientific computing.
- **Do not** require code. Grade the reasoning about error, stability, and verification.

---

# Chapter 29 — Uncertainty, Data, and Inference

## 1. Core Idea

Data are not facts. They are **measurements**, produced by a process that includes selection, instrumentation, and aggregation. Inference is the reconstruction of the underlying quantity from the measurements, and it fails in characteristic, predictable ways:

- **Noise:** random error that averages out with enough data.
- **Bias:** systematic error that does *not* average out, no matter how much data you collect.
- **Selection:** the data are not a random sample of the population you care about.
- **Aggregation:** the pattern in the whole is not the pattern in the parts (Simpson's paradox).
- **Regression to the mean:** extreme measurements are extreme partly by luck, so they move toward the average on re-measurement.
- **Multiple comparisons:** with enough tests, something will look significant by chance.
- **Overfitting:** a model with enough freedom fits noise and fails out of sample.

The unifying principle: **more data reduces noise and does nothing for bias, selection, or aggregation.** This is why "big data" does not solve bad measurement, and why the most dangerous errors are the ones that more data makes *more* confident.

**Principle signature.** A conclusion is being drawn from data; a comparison is being made between groups; a measurement is being used as if it were the quantity itself.

## 2. First Principles

**Signal and noise.** A measurement is $X = \theta + \varepsilon$, where $\theta$ is the quantity and $\varepsilon$ is error. The mean of $\varepsilon$ is the bias; the variance is the noise. Averaging $n$ independent measurements reduces the noise by $\sqrt n$ and leaves the bias unchanged.

**Selection changes the distribution.** If you observe only a subset $S$ of the population, the distribution of $X \mid S$ is not the distribution of $X$. Every conclusion is about $X \mid S$, not about $X$ — unless you can argue the selection is ignorable.

**Aggregation is not additive.** A relationship that holds within each stratum need not hold in the pooled data, because the strata may have different sizes and different base rates. This is Simpson's paradox, and it is not a paradox — it is a warning that the *unit of analysis* must be chosen deliberately.

**Regression to the mean.** If $X = \theta + \varepsilon$ with $\varepsilon$ independent across measurements, then conditional on observing a large $X$, the expected $\theta$ is closer to the mean than $X$ was. The re-measurement is expected to be less extreme *even if nothing changed*. Any intervention evaluated on extreme cases will appear to work.

**Multiple comparisons.** With $m$ independent tests at significance $\alpha$, the probability of at least one false positive is $1 - (1-\alpha)^m$. For $m=20$, $\alpha=0.05$, this is about $64\%$. Correction (Bonferroni, FDR) is mandatory when many hypotheses are tested.

**Correlation is not causation.** $X$ and $Y$ can be correlated because $X$ causes $Y$, $Y$ causes $X$, a third variable $Z$ causes both, or the selection mechanism induces the correlation. Distinguishing these requires an intervention or a natural experiment, not more observational data.

## 3. Reasoning Process

1. **State the quantity and the population.** What is $\theta$, and what is the set of units you want to generalize to?
2. **Ask how the data were produced.** Who was measured, who was excluded, how was the measurement made, what was the protocol?
3. **Separate noise from bias.** Can the error be reduced by averaging? If not, it is bias, and more data will not help.
4. **Check for selection.** Is the sample representative? What is the mechanism that put units in the sample?
5. **Check the unit of analysis.** Are you comparing strata with different sizes or base rates? Compute both the stratified and pooled results.
6. **Check for regression to the mean** whenever the data are selected on an extreme value.
7. **Correct for multiple comparisons** if many hypotheses were tested.
8. **Distinguish association from causation**, and state what evidence would be needed for the causal claim.

## 4. Demonstrations

### Demonstration 29.1 — Simpson's paradox

*Setup.* Two treatments, A and B, are compared on easy and hard cases.

| | Easy cases | Hard cases | Overall |
|---|---|---|---|
| **A** | $9/10 = 90\%$ | $20/90 \approx 22.2\%$ | $29/100 = 29\%$ |
| **B** | $80/90 \approx 88.9\%$ | $2/10 = 20\%$ | $82/100 = 82\%$ |

*Observation.* A has a higher success rate in *both* strata ($90\% > 88.9\%$ and $22.2\% > 20\%$), but B has a much higher overall rate ($82\% > 29\%$).

*Mechanism.* A was applied mostly to hard cases ($90$ of $100$), where success is rare; B was applied mostly to easy cases ($90$ of $100$), where success is common. The pooled rate is dominated by the stratum composition, not by the treatment effect.

**What to notice.** Both the stratified comparison and the pooled comparison are arithmetically correct. They answer *different questions*: the stratified comparison answers "for a patient like this, which treatment is better?"; the pooled comparison answers "which treatment had a better record overall?". **The unit of analysis is a modeling decision, not a fact** (→ Ch. 25), and it must be made explicitly.

The general lesson: whenever a pooled statistic and a stratified statistic disagree, the composition of the groups is doing the work. This is the mathematical form of confounding.

### Demonstration 29.2 — Regression to the mean

*Model.* Suppose true ability $\theta \sim N(0,1)$ across a population, and a test measures $X = \theta + \varepsilon$ with $\varepsilon \sim N(0,1)$ independent of $\theta$. Select the top $10\%$ of scorers and re-test them.

*Computation.* Given $X = x$, the conditional expectation of ability is
$$\mathbb{E}[\theta \mid X = x] = \frac{1}{1+1}x = \frac{x}{2}$$
(by the standard normal-normal update: the posterior mean is a precision-weighted average, and here the precisions are equal, so the weight is $1/2$).

So a person who scored $x = 1.64$ (the $95$th percentile) has expected ability $0.82$ — and their expected *re-test* score is also $0.82$, because $\mathbb{E}[X' \mid X=x] = \mathbb{E}[\theta\mid X=x] = x/2$.

*Conclusion.* The top decile's average score falls by a factor of about $2$ on re-testing, with no change in anyone's ability.

**What to notice.** Any intervention applied to the worst performers will show improvement, and any intervention applied to the best will show decline — *even if the intervention does nothing*. This is the single most common error in program evaluation, sports commentary ("the Sports Illustrated cover jinx"), and medical follow-up.

The defense is a control group: compare the treated group's change to the change in an untreated group selected the same way.

### Demonstration 29.3 — Selection bias: the missing data

*Story.* During WWII, engineers examined returning aircraft and proposed reinforcing the areas with the most bullet holes: the wings and fuselage. Abraham Wald pointed out that the relevant sample was the *returning* aircraft, and that the areas with *no* holes on returning planes were the areas where a hit was fatal — because planes hit there did not return.

*Analysis.* Let $H$ be the set of hit locations and $R$ the event of returning. The data are drawn from $H \mid R$, not from $H$. The correct inference is about the locations where $P(R \mid \text{hit at } h)$ is low, and those are *under-represented* in the data.

*Conclusion.* Reinforce where the returning planes have *no* holes.

**What to notice.** The data were real, abundant, and accurately measured. The error was in the **sampling frame**: the population of interest (all aircraft hit) was not the population observed (aircraft that returned). No amount of additional data on returning planes would fix this, because the missing planes are missing by construction.

This is the general form of survivorship bias, and it is why "the data show" is not an argument until you know what data are absent.

### Demonstration 29.4 — Multiple comparisons

*Setup.* Twenty independent hypotheses are tested, each at significance level $\alpha = 0.05$, and all null hypotheses are true.

*Computation.* The probability that at least one test is significant is
$$1 - (1-0.05)^{20} = 1 - 0.95^{20} \approx 1 - 0.358 = 0.642.$$
So there is about a $64\%$ chance of at least one false positive, even though nothing is real.

*Correction.* Bonferroni: test each at $\alpha/m = 0.05/20 = 0.0025$, which restores the family-wise error rate to $0.05$. The cost is reduced power: real effects must be larger to be detected.

**What to notice.** The individual tests are each valid; the *collection* of tests is not, because the error rate compounds. This is why pre-registration, correction, and replication are not bureaucratic formalities — they are the mathematical consequence of testing many hypotheses.

The same arithmetic explains why "a study found that X is linked to Y" is weak evidence when many links were examined, and why replication is essential.

## 5. Connections

- **← Ch. 21.** Base rates, Bayes, and the mean-versus-typical distinction are the probabilistic foundation.
- **← Ch. 25.** The unit of analysis and the sampling frame are modeling decisions; this chapter is their statistical consequence.
- **← Ch. 26.** Estimation is the antidote to numerically absurd claims; this chapter is the antidote to statistically absurd ones.
- **→ Ch. 31.** Conjectures from data inherit every bias in the data.
- **→ Ch. 33.** Experimental mathematics has its own selection effects (you notice the patterns you look for).
- **→ Ch. 35.** Research judgment includes knowing which claims are supported by the evidence and which are supported by the sample.

## 6. Limitations

**Noise can be irreducible.** Sometimes the quantity is genuinely random, and no amount of data will reduce the variance. Distinguishing irreducible noise from measurement error requires repeated measurements and a model.

**Bias can be undetectable from the data alone.** If the bias affects every measurement equally, no internal check can find it. External validation (a different instrument, a different population) is the only defense.

**Correction for multiple comparisons can be too conservative.** Bonferroni controls the family-wise error rate at the cost of power; in exploratory work, false discovery rate control is often more appropriate. The choice is a judgment call, not a theorem.

**Causal inference requires assumptions that data cannot verify.** Instrumental variables, difference-in-differences, and regression discontinuity all rest on assumptions (exclusion, parallel trends, continuity) that are not testable from the data they use.

**Statistical significance is not practical significance.** A tiny effect can be significant with enough data, and a large effect can be non-significant with little data. Report effect sizes and intervals, not just p-values.

## 7. Applications

- **Medicine.** Clinical trials, screening, and diagnosis are the canonical setting for base rates, regression to the mean, and selection effects.
- **Finance.** Backtested strategies suffer from selection (many strategies tried), survivorship (failed funds disappear), and overfitting (parameters tuned to the past).
- **Public policy.** Program evaluation is regression to the mean plus selection; randomized controlled trials are the response.
- **Machine learning.** Train/test splits address selection; cross-validation addresses overfitting; distribution shift is the modern form of sampling frame error.
- **Science.** Publication bias, p-hacking, and the replication crisis are all instances of multiple comparisons and selection.
- **Engineering.** Reliability testing has its own selection effects (units that fail early are removed from the sample).

## 8. Mastery Criteria

You have this chapter when you can:

1. Separate noise from bias in a measurement process and say which can be reduced by more data.
2. Identify the sampling frame and the mechanism that selected the data.
3. Detect Simpson's paradox by computing both stratified and pooled statistics.
4. Predict the direction and magnitude of regression to the mean for a selected group.
5. Correct for multiple comparisons and explain the cost.
6. State what evidence would be required to move from association to causation.

**Diagnostic question.** "The data show that X works. What would make this conclusion wrong?" A learner who names selection, regression to the mean, and multiple comparisons has the skill.

### AI Tutor Brief

- **Generate:** (i) Simpson's-paradox datasets requiring both analyses; (ii) regression-to-the-mean predictions; (iii) selection-bias scenarios with a missing subpopulation; (iv) multiple-comparison calculations; (v) "association or causation?" case studies.
- **Probe misconceptions:** "more data means more truth"; pooled statistics as automatically correct; significance as importance; correlation as causation.
- **Transfer distance:** high. Use medicine, finance, sports, and policy settings, since the mathematics is identical and the surface is not.
- **Do not** accept a conclusion from data without the sampling frame and the unit of analysis stated.

---

# Chapter 30 — Systems Thinking

## 1. Core Idea

A **system** is a collection of interacting components whose behavior is not determined by the components in isolation. Four properties distinguish systems from mere collections:

1. **Feedback:** the output affects the input. Feedback creates stability, oscillation, or explosion, and it invalidates any analysis that treats the components as independent.
2. **Emergence:** the aggregate exhibits behavior no component has. Majorities can cycle, markets can crash, traffic can jam with no accident.
3. **Nonlinearity:** thresholds, saturation, and multiple equilibria. Small changes can have large effects, and large changes can have none.
4. **Interfaces:** the boundaries between components are where the assumptions of each component meet, and where most failures occur.

The central methodological claim: **decomposition is necessary and dangerous.** You cannot analyze a system without breaking it into parts, and the breaking is exactly what can make the analysis wrong.

**Principle signature.** The problem involves multiple interacting agents, feedback loops, aggregation, or a whole whose behavior is not the sum of its parts.

## 2. First Principles

**Feedback and stability.** A discrete-time system $x_{t+1} = f(x_t)$ has a fixed point $x^*$ with $f(x^*) = x^*$. It is **stable** if $|f'(x^*)| < 1$: small perturbations decay. It is unstable if $|f'(x^*)| > 1$, and the boundary $|f'(x^*)| = 1$ is where oscillation or slow convergence begins. Continuous-time systems are analogous with $f'(x^*) < 0$ for stability.

**Oscillation and overshoot.** Feedback with delay produces oscillation: the system responds to a state that no longer exists. The period and the damping are determined by the loop gain and the delay, and this is why control systems need damping, not just gain.

**Nonlinearity and multiple equilibria.** A nonlinear system can have several fixed points, some stable and some unstable. Which one the system reaches depends on initial conditions (path dependence), and the boundary between basins is a **threshold**.

**Emergence: aggregation paradoxes.** Aggregating individual preferences can produce collective preferences with properties no individual has. Condorcet's paradox is the canonical example: individual preferences are transitive, collective majority preferences can cycle.

**Interfaces and coupling.** A system's components are designed against assumptions about each other. When the assumptions are violated at an interface, the failure is usually attributed to the wrong component. **Most system failures are interface failures**, and interfaces are exactly what decomposition ignores.

**Robustness–fragility tradeoff.** Optimizing a system for one environment makes it fragile to another. Diversity and redundancy buy robustness at the cost of efficiency. This is not a design flaw; it is a structural tradeoff.

## 3. Reasoning Process

1. **Draw the boundary.** What is inside the system, what is outside, and what crosses the boundary?
2. **Identify the components and the couplings.** Which components affect which, and through what channel?
3. **Find the feedback loops.** Positive (amplifying) and negative (stabilizing). Every loop is a potential source of instability.
4. **Identify the nonlinearities.** Thresholds, saturation, capacity limits, step changes.
5. **Analyze the aggregate.** Simulate or reason about the whole; do not assume the aggregate is the sum of the parts.
6. **Check the interfaces.** What does each component assume about its neighbors, and what happens when the assumption fails?
7. **Test the decomposition.** Compare the whole-system behavior with the behavior predicted by the parts. The difference is the coupling, and it is the finding.

## 4. Demonstrations

### Demonstration 30.1 — Feedback, stability, and the route to chaos

*System.* The logistic map $x_{t+1} = r x_t(1 - x_t)$ on $[0,1]$, a standard model of a population with feedback.

*Fixed point.* Solve $x^* = r x^*(1-x^*)$: either $x^*=0$ or $x^* = 1 - 1/r$ (valid for $r>1$).

*Stability.* $f'(x) = r(1-2x)$, so at $x^* = 1-1/r$:
$$f'(x^*) = r\left(1 - 2 + \frac{2}{r}\right) = 2 - r.$$
Stability requires $|2-r| < 1$, i.e. $1 < r < 3$.

*Behavior.*
- $1 < r < 3$: the population converges to $x^* = 1-1/r$. (For $r=2.5$: $x^* = 0.6$.)
- $r > 3$: the fixed point is unstable; the system settles into a 2-cycle. (For $r=3.2$: the cycle is approximately $0.513$ and $0.799$.)
- $r \approx 3.57$: the period-doubling cascade accumulates and the system becomes chaotic.
- $r = 4$: fully chaotic, with sensitive dependence on initial conditions.

**What to notice.** The *same* system changes qualitatively as a parameter crosses a threshold. There is no way to predict the 2-cycle from the stable regime by extrapolation; the qualitative change is a **bifurcation**, and it is invisible to any analysis that linearizes at the fixed point.

This is the mathematical core of systems thinking: **the regime is a property of the parameter, not of the components.** A model calibrated in one regime can be qualitatively wrong in another.

### Demonstration 30.2 — Emergence: Condorcet's cycle

*Setup.* Three voters with preferences over three options:

| Voter | Preference |
|---|---|
| 1 | $A \succ B \succ C$ |
| 2 | $B \succ C \succ A$ |
| 3 | $C \succ A \succ B$ |

*Pairwise majority:*
- $A$ vs $B$: voters 1 and 3 prefer $A$ $\implies A$ wins.
- $B$ vs $C$: voters 1 and 2 prefer $B$ $\implies B$ wins.
- $C$ vs $A$: voters 2 and 3 prefer $C$ $\implies C$ wins.

*Result.* $A \succ B \succ C \succ A$ — a cycle.

**What to notice.** Each individual preference is transitive (a total order). The collective preference is **intransitive**. This is not a failure of the voters or of the aggregation rule's implementation; it is a structural property of majority rule (Arrow's theorem generalizes it). **The aggregate has a property that no component has**, which is the definition of emergence.

The practical consequence: "the will of the majority" may not be a coherent object. Any procedure that claims to aggregate preferences must either accept cycles or restrict the domain of preferences, and both choices have costs.

### Demonstration 30.3 — Braess's paradox: adding capacity can hurt

*Setup.* $4000$ drivers travel from $S$ to $T$. Two routes:

- Route 1: $S \to A \to T$, where the $S\to A$ link takes $x/100$ minutes when $x$ cars use it, and $A \to T$ takes $45$ minutes (constant).
- Route 2: $S \to B \to T$, where $S \to B$ takes $45$ minutes and $B \to T$ takes $y/100$ minutes when $y$ cars use it.

*Equilibrium without the new link.* By symmetry, $x = y = 2000$, and each route takes
$$\frac{2000}{100} + 45 = 20 + 45 = 65 \text{ minutes}.$$

*Adding a link.* Now add a very fast link $A \to B$ (time $\approx 0$). Consider the new equilibrium. If everyone takes $S \to A \to B \to T$, the time is
$$\frac{4000}{100} + 0 + \frac{4000}{100} = 40 + 40 = 80 \text{ minutes}.$$
Is this an equilibrium? A driver who deviates to $S\to A \to T$ faces $\frac{4000}{100} + 45 = 85$ minutes; one who deviates to $S \to B \to T$ faces $45 + \frac{4000}{100} = 85$ minutes. Both are worse than $80$. So everyone using the new route is indeed an equilibrium — with a travel time of $80$ minutes, worse than the $65$ minutes before the link existed.

**What to notice.** Adding a zero-cost link *increased* everyone's travel time. This is Braess's paradox, and it is a genuine instance of a system whose parts (links) have a property (adding capacity helps) that the whole does not.

The mechanism: the new link creates a *dominant* route that concentrates all the traffic on the two congestible links, destroying the balancing that the old equilibrium achieved. **The system was efficient because of a constraint, and removing the constraint made it worse.** This is the strongest possible argument against the intuition that more options are always better.

### Demonstration 30.4 — The interface failure

*Scenario.* A system has two components: a service that returns results and a client that consumes them. The service's contract says "results are returned in unspecified order". The client assumes they are sorted. Each component is correct against its own specification; the system fails.

*Analysis.* The failure is not in either component. It is at the **interface**, where one component's assumption meets another's guarantee. The specification was satisfied and the system was broken, because the *composition* of the specifications was not checked.

*Diagnosis method.* For each interface, list what each side guarantees and what each side assumes. The failure modes are exactly the assumptions that are not guaranteed. This is a finite, mechanical audit, and it finds most integration bugs.

**What to notice.** Decomposition created the interface, and the interface is where the decomposition's assumptions are tested. **The more you decompose, the more interfaces you create, and the more assumptions you must audit.** This is the fundamental tension of systems design: decomposition makes each part tractable and makes the whole fragile.

## 5. Connections

- **← Ch. 8.** Invariants in a system are what feedback loops preserve or destroy.
- **← Ch. 11.** Multiple equilibria and thresholds are extremal structure: which basin you land in is determined by an extremal boundary.
- **← Ch. 19.** Duality between descriptions (state space and transfer function) is a systems-analysis tool.
- **← Ch. 25.** A system model is a model with feedback; the modeling cycle applies, with validation across regimes.
- **→ Ch. 29.** Emergent aggregate behavior is a statistical phenomenon; Simpson's paradox is the static analogue of Condorcet's cycle.
- **→ Ch. 35.** Research on complex systems requires judgment about which level of description is the right one.

## 6. Limitations

**Systems thinking can become a substitute for analysis.** "It's a complex system" is sometimes true and sometimes an excuse for not doing the mathematics. The value is in identifying the *specific* feedback loop, nonlinearity, or interface — not in invoking complexity.

**Emergence is often claimed without proof.** Genuine emergence requires showing that the aggregate property is not derivable from the components; usually it is derivable, just not obvious. Distinguish "surprising" from "emergent".

**Simulation is the usual tool, with its usual limits.** System dynamics models are notoriously sensitive to assumptions and difficult to validate (→ Ch. 28). A simulation of a complex system is evidence, not proof.

**The boundary is a choice.** What counts as inside the system determines what counts as an external shock. Different boundaries give different analyses, and the choice is a modeling decision, not a fact.

**Optimization can destroy robustness.** A system optimized for one objective is fragile to others; the robustness–fragility tradeoff is real, and ignoring it produces systems that fail catastrophically rather than gracefully.

## 7. Applications

- **Engineering.** Control systems, power grids, and communication networks are feedback systems; stability analysis is mandatory, and cascading failures are the emergent failure mode.
- **Economics.** Markets are feedback systems with strategic agents; bubbles, crashes, and bank runs are emergent phenomena, and Braess-type paradoxes appear in traffic and network design.
- **Ecology.** Predator–prey cycles, tipping points, and resilience are systems properties; the logistic map is the simplest model of a population with feedback.
- **Organizations.** Incentive systems are feedback loops; Goodhart's law ("when a measure becomes a target, it ceases to be a good measure") is the organizational form of the observer effect.
- **Public health.** Epidemic dynamics are feedback systems with behavioral response; the feedback can stabilize (behavior change) or destabilize (risk compensation).
- **Software.** Distributed systems are systems with partial failure, asynchronous communication, and emergent inconsistency; the interface audit is the core design discipline.

## 8. Mastery Criteria

You have this chapter when you can:

1. Draw a system boundary and identify the couplings that cross it.
2. Find the feedback loops and determine their stability from the local dynamics.
3. Identify thresholds, multiple equilibria, and the basins that determine outcomes.
4. Produce an example of emergence (an aggregate property no component has) and prove it.
5. Perform an interface audit: list guarantees and assumptions on each side, and find the mismatches.
6. Explain why adding capacity or options can degrade a system's performance.

**Diagnostic question.** "The parts are each correct, but the system fails. Where do you look?" A learner who goes to the interfaces has the systems stance.

### AI Tutor Brief

- **Generate:** (i) stability analysis of simple feedback maps; (ii) threshold/bifurcation problems; (iii) aggregation paradoxes (voting, traffic) requiring a proof; (iv) interface-audit scenarios; (v) "adding capacity hurts" puzzles.
- **Probe misconceptions:** "the whole is the sum of the parts"; more options are always better; a stable component implies a stable system; emergence as an explanation rather than a phenomenon.
- **Transfer distance:** high. Test in engineering, economics, ecology, and software.
- **Do not** accept "it's complex" as an analysis. Require the specific loop, threshold, or interface.

---

## Part IV checkpoint

1. Write a model as numbered assumptions plus structure, and state its scope and falsification condition. (Ch. 25)
2. Estimate a quantity two ways and interpret the agreement. (Ch. 26)
3. Derive a scaling law and say what remains undetermined. (Ch. 27)
4. Identify catastrophic cancellation and the stability condition of an explicit scheme. (Ch. 28)
5. Detect Simpson's paradox and predict regression to the mean. (Ch. 29)
6. Find the feedback loop, the threshold, and the interface in a system. (Ch. 30)

Part V is where the problem is no longer given to you at all.

---
