# AI & ML Architecture Perspective
*How I think about AI/ML systems — and what I've built with them*

This document exists for one reason: the projects in this portfolio were built inside Amazon, which means the most AI-relevant work can't be shown directly. This is my attempt to be explicit about how I think about AI/ML architecture, what I've built, and how that maps to the problems AWS AI services like SageMaker and Bedrock are designed to solve.

---

## What I've Actually Built with AI

### 1. LLM Inference Pipeline — Service Analytics Commentary Engine

The commentary generator in the Service Analytics platform is, architecturally, an inference pipeline:

```
Structured Data (DataFrames)
        ↓
  Feature Extraction
  (cohort YoY deltas, momentum signals, sub-product drivers)
        ↓
  Prompt Construction
  (templated context injection with computed values)
        ↓
  LLM Inference
  (narrative generation — revenue trends, cohort attribution, risk flags)
        ↓
  Post-processing
  (formatting, validation, insertion into WBR deck)
```

The key design decisions here mirror what you'd make in a production ML system:
- **Determinism vs. creativity**: commentary needs to be factually grounded, so the "model" is mostly template-driven with LLM used for fluency, not for reasoning
- **Latency vs. freshness**: results are cached (Parquet) so the commentary engine runs against pre-computed analytical output, not live queries
- **Output validation**: generated paragraphs are cross-checked against the underlying numbers before delivery

This is the same set of tradeoffs a team building on **Amazon Bedrock** faces when designing a document generation or summarization workflow.

### 2. AI Coaching Integration — Snapshot (Claude API)

Snapshot's Snappy AI Coach is a production Claude integration with real cost and latency constraints:

- **Prompt engineering**: system prompt encodes the user's financial context (account balances, recent deltas, streak data, debt payoff progress) as structured input; the model returns a personalized briefing
- **Cost optimization**: ~$0.01/call achieved through DB-level response caching — identical financial states return cached responses rather than re-invoking the model
- **Inference architecture**: stateless API calls with context injected per-request (no fine-tuning, no RAG) — appropriate for a use case where the "knowledge" is the user's own data, not a corpus

This is a practical example of **inference optimization** — the same problem SageMaker Inference and Bedrock's on-demand vs. provisioned throughput modes are designed to solve at scale.

---

## How I Think About the ML Stack

### The Three Problems Every ML Team Has

Having worked alongside data scientists and ML engineers at Amazon, I've seen the same three problems repeat:

**1. The experiment-to-production gap**
Models get trained in notebooks, then there's a painful handoff to engineering to "productionize" them. The friction is real: different environments, no reproducibility guarantees, manual deployment steps. This is the core problem **SageMaker Pipelines** and **MLflow** solve — making the path from experiment to endpoint repeatable and auditable.

**2. Inference cost vs. latency tradeoffs**
Not all inference is equal. A real-time customer-facing prediction (fraud detection, recommendation) has different requirements than a batch job running overnight. Teams often over-provision for batch workloads or under-provision for real-time ones. **SageMaker Inference** (real-time endpoints, serverless inference, batch transform, async inference) exists specifically to match deployment mode to workload shape.

**3. The "last mile" problem**
Models produce outputs. Someone has to turn those outputs into decisions, content, or actions that a business user can act on. This is where most ML value gets lost — the model works, but nobody knows what to do with it. My commentary generator, my BI automation platform, and Snapshot's AI coach are all "last mile" solutions: they take model output and make it immediately actionable for a non-technical audience.

### Reference Architecture: Financial Services on Bedrock

Here's how I'd think about a customer use case relevant to this role — a financial services firm using AWS AI to automate analyst workflows:

```
                        ┌─────────────────────────────────────────┐
                        │         DATA SOURCES                     │
                        │  S3 (reports, filings, transcripts)      │
                        │  RDS / Redshift (structured financials)  │
                        └──────────────┬──────────────────────────┘
                                       │
                        ┌──────────────▼──────────────────────────┐
                        │      KNOWLEDGE LAYER (RAG)               │
                        │  Amazon Bedrock Knowledge Bases          │
                        │  • Chunking + embedding (Titan)          │
                        │  • Vector store (OpenSearch Serverless)  │
                        │  • Retrieval at query time               │
                        └──────────────┬──────────────────────────┘
                                       │
                        ┌──────────────▼──────────────────────────┐
                        │      INFERENCE LAYER                     │
                        │  Amazon Bedrock (Claude / Titan)         │
                        │  • On-demand for interactive queries     │
                        │  • Batch inference for weekly reports    │
                        │  • Guardrails for compliance/PII         │
                        └──────────────┬──────────────────────────┘
                                       │
                        ┌──────────────▼──────────────────────────┐
                        │      ORCHESTRATION                       │
                        │  Amazon Bedrock Agents                   │
                        │  • Multi-step reasoning                  │
                        │  • Tool use (query DB, fetch filing)     │
                        │  • Action groups for workflow automation │
                        └──────────────┬──────────────────────────┘
                                       │
                        ┌──────────────▼──────────────────────────┐
                        │      OUTPUT / LAST MILE                  │
                        │  • Analyst briefing (narrative text)     │
                        │  • Risk flag summary (structured JSON)   │
                        │  • Auto-drafted client communication     │
                        └─────────────────────────────────────────┘
```

**Why this matters for PMM:** The customer's problem isn't "I need a model." It's "my analysts spend 6 hours every Monday pulling data and writing the same paragraphs." The architecture above is the answer — but a PMM's job is to translate that architecture into a value proposition the head of AI at a bank can act on: *"Cut your weekly reporting cycle from days to minutes, with outputs your compliance team can trust."*

That's the bridge I build.

---

## What I'd Learn Next

I'm direct about where my gaps are:

- **SageMaker hands-on**: I understand the architecture and the problems it solves. I haven't built a training pipeline or deployed a custom endpoint. That's a gap I'm actively closing.
- **MLOps tooling depth**: I understand the concepts (model registry, drift detection, A/B deployment, shadow mode) but my hands-on experience is with data pipelines, not model lifecycle management.
- **Bedrock fine-tuning and model customization**: I've used foundation models via API. I haven't run a fine-tuning job or evaluated custom model performance at scale.

What I bring that's harder to teach: I've worked inside the business problems these tools are supposed to solve. I know what a finance analyst actually needs from an AI output. I know what makes an executive trust a model-generated narrative. I know where the "last mile" breaks down. That's the PMM lens — and it's what I'd bring to positioning SageMaker and Bedrock for the customers who need them most.

---

*See also: [Service Analytics Platform](./01-service-analytics.md) · [Snapshot AI Coach](./02-snapshot.md) · [FinAI Adoption](./06-finai-adoption.md)*
