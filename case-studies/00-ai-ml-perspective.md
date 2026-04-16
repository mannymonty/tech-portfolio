# AI & ML Architecture Perspective
*How I think about AI/ML systems — and what I've built with them*

The projects in this portfolio were built inside Amazon, which means the most AI-relevant work can't be shown directly. This document is an attempt to be explicit about how I think about AI/ML architecture and what I've actually built.

---

## What I've Built with AI

### 1. Narrative Generation Pipeline — Service Analytics Commentary Engine

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
  Narrative Generation
  (revenue trends, cohort attribution, risk flags)
        ↓
  Post-processing
  (formatting, validation, insertion into WBR deck)
```

The key design decisions here mirror what you'd make in any production AI system:
- **Determinism vs. creativity**: commentary needs to be factually grounded, so the system is mostly template-driven with LLM used for fluency, not for reasoning
- **Latency vs. freshness**: results are cached (Parquet) so the commentary engine runs against pre-computed analytical output, not live queries
- **Output validation**: generated paragraphs are cross-checked against the underlying numbers before delivery

### 2. AI Coaching Integration — Snapshot (Claude API)

Snapshot's Snappy AI Coach is a production Claude integration with real cost and latency constraints:

- **Prompt engineering**: system prompt encodes the user's financial context (account balances, recent deltas, streak data, debt payoff progress) as structured input; the model returns a personalized briefing
- **Cost optimization**: ~$0.01/call achieved through DB-level response caching — identical financial states return cached responses rather than re-invoking the model
- **Inference architecture**: stateless API calls with context injected per-request (no fine-tuning, no RAG) — appropriate for a use case where the "knowledge" is the user's own data, not a corpus

---

## Patterns I've Seen Repeat

Working alongside data scientists and ML engineers at Amazon, I've noticed the same problems come up across teams:

**The experiment-to-production gap.** Models get trained in notebooks, then there's a painful handoff to engineering to "productionize" them. Different environments, no reproducibility guarantees, manual deployment steps. The friction is real.

**Inference cost vs. latency tradeoffs.** Not all inference is equal. A real-time customer-facing prediction has different requirements than a batch job running overnight. Teams often over-provision for batch workloads or under-provision for real-time ones. I dealt with a version of this in Snapshot — caching AI responses at the DB level to avoid redundant API calls.

**The "last mile" problem.** Models produce outputs. Someone has to turn those outputs into decisions, content, or actions that a business user can act on. This is where most ML value gets lost — the model works, but nobody knows what to do with it. My commentary generator, my BI automation platform, and Snapshot's AI coach are all "last mile" solutions: they take model output and make it immediately actionable for a non-technical audience.

---

## Where I'm Honest About Gaps

- **Model training and deployment**: I've consumed models via API. I haven't built a training pipeline or deployed a custom endpoint.
- **MLOps tooling**: I understand the concepts (model registry, drift detection, A/B deployment) but my hands-on experience is with data pipelines, not model lifecycle management.
- **Fine-tuning**: I've used foundation models out of the box. I haven't run a fine-tuning job or evaluated custom model performance at scale.

What I bring that's harder to teach: I've worked inside the business problems these tools are supposed to solve. I know what a finance analyst actually needs from an AI output. I know what makes an executive trust a model-generated narrative. I know where the "last mile" breaks down — and I've built the systems that fix it.

---

*See also: [Service Analytics Platform](./01-service-analytics.md) · [Snapshot AI Coach](./02-snapshot.md) · [FinAI Adoption](./06-finai-adoption.md)*
