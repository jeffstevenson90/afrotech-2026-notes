**Speaker:** Jonathan Yeldo (confirm), Solutions Architect, AWS · **Format:** 30-minute talk with live demo

## Summary in plain terms

Most companies run their order and data flows on rigid "middleware": software that passes clean, perfectly formatted data between systems (CRM, inventory, shipping, orders) in a fixed sequence. It's fast, cheap and easy to test, but it breaks the moment input arrives messy, like a customer email that says "send a couple more of the pro ones, like last time."

Jonathan's argument: don't replace that middleware with AI. Embed an AI agent inside it to handle the messy cases. The agent uses the same existing APIs as "tools," reasons about what the customer means, looks up context (e.g., order history), and translates the request into the exact format the systems expect.

His live demo (Claude on Amazon Bedrock) compared the two approaches across three tests:

- **Clean input:** both worked. The rigid pipeline was faster.
- **Messy email:** the rigid pipeline failed. The agent resolved the vague product reference from CRM history, placed the order, and listed the assumptions it made.
- **Mid-run outage (inventory API down):** the rigid pipeline failed. The agent fell back to a secondary inventory feed, judged a small order was safe, and completed it.

The agent orchestration took about 16 lines of code with current frameworks.

## Key callouts

- **Hybrid, not replacement.** Keep the deterministic workflow as the backbone, and add an AI reasoning layer only where ambiguity enters.
- **The 80/20 rule (speaker's own estimate):** roughly 80% of workflows are better off *without* agents. Only about 20% benefit. Hype is driving over-adoption.
- **You can't code every edge case.** Regex and if/else patching for messy input is slow, never complete, and each gap is a frustrated customer.
- **Route only the messy cases to the agent.** That limits the extra latency and cost to the cases that need reasoning.
- **When NOT to use agents:** low-latency needs, highly predictable inputs, or cases where cost matters more than flexibility.

## How to make agents trustworthy (the four controls)

1. **Bounded authority:** the agent only gets the tools (APIs) it needs, so it can't take actions it wasn't granted.
2. **Observability:** stream and log the agent's reasoning and tool calls for debugging and improvement.
3. **Deterministic guardrails:** downstream APIs still validate every request. The agent can't push bad data past them.
4. **Human review:** especially early on, a person approves agent-created actions before they hit production.

**Testing non-deterministic output:** test for "acceptably similar" answers rather than one exact expected output. **Prompt injection risk** (e.g., malicious emails) is real but contained by bounded tools plus server-side validation.

## Learnings and signals for the team

- **Look for "messy intake" points in our own workflows** (free-text requests, emailed asks, inconsistent report specs). These are the 20% where an agent layer earns its cost.
- **Agents should surface their assumptions.** Listing every assumption made is a good standard for any AI-assisted BI output we build.
- **Wrap existing APIs as tools; don't rebuild systems.** A low-cost way to pilot agentic AI on top of what we already run.
- **Graceful degradation is a real differentiator.** It also raises governance questions about when stale data is "good enough."
- **Push back on agents-everywhere pressure.** Use the 80/20 framing when stakeholders ask to "add AI" to a process that's already working.
