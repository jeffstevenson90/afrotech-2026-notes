**Speaker:** Gregory Green (introduced as both "King" and "Green"; confirm), Solutions Architect, VMware / Broadcom · **Note:** the transcript ends just as the speaker starts on how to make local AI faster.

## Summary in plain terms

Platforms like ChatGPT run on millions of AI chips across hundreds of thousands of servers, so you can't run *that* on a laptop. You can, however, run smaller open-source models (Llama, Gemma, Qwen, Mistral, open GPT variants) locally on everyday hardware, with no internet and no special AI chip. This is "AI at the edge": running models outside the data center.

Why it matters: cloud AI capacity is getting strained, new data centers face pushback, costs get "astronomical" at scale, and many places have no reliable internet. His motivating example was medical mission trips to remote areas with no hospital. A local AI could take a patient's vitals and suggest assessments or medications, with the doctor making the final call.

How he built it:

- **Download a model like a movie.** Tools like Ollama let you pull a model once and run it offline on a Mac, Windows or Linux laptop using just the CPU. Many models need only a few GB of disk and around 8–16 GB of RAM.
- **Embed it in existing apps.** He used Java with Spring AI, so AI goes into the systems where enterprise data already lives (banking, insurance, healthcare). The whole app was about 60 MB.
- **Give it domain knowledge through RAG.** He turned expert instructions into embeddings, stored them in a vector database (Postgres, or an in-memory option), and retrieved only the relevant instructions for each question.
- **Use guardrail prompts.** The system prompt tells the model to recommend with caution and say "I don't know" rather than make things up.

The catch: the full flow on a CPU-only laptop took about **5 minutes per question**.

## Key callouts

- **Small, local models are now viable** on standard laptops, small devices and phones. You don't need a GPU to start, though one helps.
- **Drivers toward the edge:** cloud capacity limits, cost at scale, connectivity gaps, and keeping data local.
- **Bring AI to the data, not the data to AI.** Add AI to existing enterprise apps instead of standing up new stacks.
- **RAG beats stuffing the prompt.** Retrieve only the relevant pieces through similarity search.
- **Latency is the real constraint on edge hardware.**
- **Keep a human in the loop** in high-stakes domains.

## Learnings and signals for the team

- **Local models as a privacy and cost lever.** Running a small model plus RAG on internal infrastructure avoids sending sensitive data to external providers and avoids per-call costs.
- **Small model + good retrieval beats a big model with no context** for narrow, domain-specific Q&A.
- **Postgres can be our vector store.** No new database is needed to experiment with RAG.
- **Plan for latency up front.** Set expectations and size the hardware before showing stakeholders.
- **The "cost surprise" signal is real.** Estimate inference costs early in any AI project.
