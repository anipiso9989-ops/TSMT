# The AI Tutor Protocol

A tutor can generate problems, give a small hint, or check a proof. Use it to help you make the next move yourself. Keep a record of which problems you can solve from a blank page.

## Start a session

Pick a chapter and try its worked example or practice problem. Send the tutor the claim, your attempt, and the exact point where you got stuck. Include any terms you are still learning.

You can paste this prompt.

```text
Tutor me on Chapter [number], [topic], of The Structure of Mathematical Thought.
Use only arithmetic, algebra, discrete mathematics, elementary geometry, or finite probability as appropriate. Explain any term I have not learned.

My goal is [goal]. My attempt is [paste attempt].
Ask me to identify what is given and what would count as a solution.
When I ask for help, give one hint at the smallest useful level.
Wait for my next attempt before escalating. Give a full solution only if I request one.

When I submit a solution, identify the first gap and ask me to repair it.
Check assumptions, both directions when needed, all cases, and the conclusion.
After I repair it, give me one new problem that tests the same reasoning in a different setting. Keep the method hidden until I try it.
```

## Use the hint ladder

| Level | What to ask for |
|---|---|
| 0 · Restatement | Ask me to say what is given and what I am trying to show. |
| 1 · Attention | Point to a condition or a small example worth examining. |
| 2 · Method | Name a family of approaches I could try. |
| 3 · Structure | Suggest a useful quantity, representation, or intermediate claim. |
| 4 · Local step | Help me justify one step, then let me finish. |
| 5 · Solution | Walk through the full argument on request. Ask me to rebuild it afterwards. |

After a hint, make a fresh attempt. If you need a full solution, close it and write the proof from memory. Return later and solve a similar problem without help.

## Ask for the kind of practice you need

| Goal | Prompt |
|---|---|
| Get started | “Give me one small problem with numbers I can check by hand. Define any unfamiliar term.” |
| Choose a method | “Give me two problems that look similar but need different moves. Leave the method names out.” |
| Repair a proof | “Find the earliest step my argument does not justify. Give me a question that helps me fix it.” |
| Test transfer | “Change the setting and remove the chapter label. Keep the prerequisites within what we have studied.” |
| Explore a question | “Help me design small cases that could disprove my conjecture. Let me make and test the prediction.” |

A good practice problem has a clear domain and a verified answer. Ask the tutor to check the conditions before assigning it. If a solution uses an unfamiliar result, ask for an explanation or choose a problem you can solve with earlier chapters.

## Review your reasoning

Score each solution separately on setup, method choice, justification, and checking. For each dimension, mark **needs help**, **independent**, or **can explain and adapt**. A correct answer can still have a proof gap. A wrong answer can contain a good method worth keeping.

| What went wrong | What to practice next |
|---|---|
| You could not restate the goal | Rewrite the claim with its domain and conditions. See Chapters 2, 3, and 7. |
| You tried several methods at random | Name the missing step, then use the Principle Map. See Chapter 24. |
| A step used an assumption you did not have | Find the first gap and try a case that breaks the step. See Chapters 4 and 32. |
| The math was right but the conclusion did not fit the situation | Check units, measurements, and model assumptions. See Chapters 25, 27, and 29. |
| You solved it only after a strong hint | Redo it later from a blank page, then try a new setting. |

## Fade the help

First solve a familiar problem with no hints. Next solve a different-looking problem that uses the same reasoning. Then solve a mixed problem a week later, when the method is unknown. On each attempt, explain what gave the method away and why the proof works. If you still need a hint, record the smallest one that helped and practice that step directly.

Treat the tutor's assessment as another argument to check. Ask for an explicit reason for any disputed step and test it with a small example. You can use the same process with a study partner or on your own.
