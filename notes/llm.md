**Speaker:** Name not captured · **Note:** figures and company details are as the speaker presented them.

## Summary in plain terms

Roughly 80% of AI projects fail, about twice the rate of regular software. Citing a RAND survey, the speaker said the cause is usually **not the technology**: teams misunderstand the problem or pick the wrong success metric.

The central question: if AI can write code, design UIs and answer users, **what's left for us?** His answer is judgment. He quickly built a study app with AI but never pinned down what he wanted, and wasted time and money. Fast doesn't mean valuable.

## Why AI products fail: four case studies

- **Cost (OpenAI Sora app):** hit the top of the App Store, but inference was reportedly costing on the order of $1M a day, retention was very low, and it was scaled back.
- **Evaluation (McDonald's + IBM drive-thru):** 85% accuracy hid edge-case failures that went viral (an order of 260 nuggets). The pilot ended in 2024.
- **Human-in-the-loop (a fintech's AI customer service, likely Klarna):** resolution time fell from ~11 to ~2 minutes, but customers wanted people, and the company began rehiring in 2025.
- **Trust (Microsoft Recall):** screenshots every few seconds raised privacy concerns; it was reworked to be opt-in.

## The framework: demo vs. product

### Before you build

- **Start from the user, not the model.**
- **Set clear expectations** about what the product can and can't do.
- **Control cost:** route simple tasks to small models and hard ones to strong models; use semantic caching for repeat questions.
- **Build trust in:** guardrails, cited sources, explicit consent (opt-in, not default).

### While you build

- **Define three bars:** "good," "acceptable" on edge cases, and "never ship."
- **Evaluate in stages:** offline test set with edge cases, internal dogfooding, then online testing. Don't save your hardest tests for production.
- **Use LLM-as-judge, but calibrate it** against human graders (Cohen's kappa around 0.8 is good).
- **Improve through** prompts and context first, fine-tuning only if needed.

### After launch

- Start with simple rules, collect feedback, then move to learned models and agent memory. Keep humans in the loop and protect privacy.

## Learnings and signals for the team

- **Define the problem and the success metric before any AI build.** A natural lane for a BI team that owns metrics.
- **Adopt "good / acceptable / never ship" bars** for AI-assisted reports, models and agents.
- **Build an evaluation habit:** edge-case test sets, human-calibrated scoring, production cases fed back in.
- **Estimate run cost early;** consider routing and caching before scaling.
- **Position the team's value as judgment:** problem framing, metrics, evaluation and trust.
