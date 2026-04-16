# C&S Service Analytics Platform
*Enterprise Customer Analytics, Revenue Intelligence & Executive Reporting*

## The Problem
A portfolio of cloud container services (EKS, ECS/Fargate, ECR, Lambda) generates hundreds of millions in weekly revenue across thousands of customers. Leadership needs a clear, weekly picture: what moved, why, who's driving it, and what's the trajectory. The existing process was manual, slow, and produced static spreadsheets that couldn't answer follow-up questions — WBR prep consumed 4–6 hours every Monday before anyone could start actual analysis.

## What I Built
A comprehensive analytics platform with three layers, each building on the last:

### Layer 1 — Customer Analytics Engine (the centerpiece)
Full-service customer analytics notebooks for EKS, ECS/Fargate, and ECR — each a 6+ MB, 13-section analytical workbook running against Redshift. These are the most sophisticated pieces in the platform:

- **WBR View**: Top-N customer tables with WoW $, WoW %, YoY% (single-week and 4-week avg), and compound weekly growth rates at 5 time horizons (CWGR4/8/13/26/52). Configurable from top-10 to top-100.
- **Customer Health Signals**: Momentum classification (Accelerating / Recovering / Decelerating / Declining), CWGR trajectory heatmaps, health quadrant scatter plots (WoW vs YoY, sized by revenue), and revenue Pareto analysis.
- **Cohort Analysis**: 6 customer cohorts (1-10, 11-100, 101-1000, 1001-10000, 10001+, Others) tracked weekly — revenue share, concentration trends, WoW/YoY by cohort, usage metrics (NIH, vCPU), Savings Plan mix, and Graviton adoption rates.
- **Top Increasers/Decreasers**: WoW driver summary decomposing service-level movement into individual customer contributions.
- **Individual Customer Deep-Dives**: Revenue + Usage + ASP 3-panel trend charts, pricing model mix, revenue decomposition (usage vs. ASP contribution), and auto-generated per-customer narratives.
- **Rank Streaks**: Win/loss streak tracking per customer per product — who's been climbing vs. falling in the rankings.
- **YoY Movers**: Identifying which customers are driving year-over-year growth or decline, with Top 10 vs. Rest of Service growth trajectory comparison.
- **Monthly Cohort View**: YoY, ASP trends, pricing mix evolution, churn signals, and auto-generated cohort narrative.
- **Executive Summary**: Cross-product KPI dashboard pulling all signals into one view with auto-generated executive narrative and risk flags.

All queries run in parallel via ThreadPoolExecutor (~5-10 min wall clock vs. ~23 min sequential). Results cached as Parquet with freshness checks.

### Layer 2 — WBR Dashboard & Revenue Reconciliation
A self-contained executive dashboard that blends two data sources (closed-month actuals with CRF rate adjustments + open-month FDM unified revenue) to produce validated net revenue figures that match the official WBR Summary. Includes DDC rate comparison (CRF vs. FDM implied vs. WBR implied) and a two-level proportional scaling methodology for gross-to-net customer attribution.

### Layer 3 — Auto-Generated Commentary
Python scripts and a dedicated notebook that transform the analytical output into business-ready narrative paragraphs — the kind you paste directly into a WBR deck. Revenue trends, cohort attribution, sub-product YoY decomposition, Extended Support vs. OP2 tracking, and portfolio-level summaries.

## Tech Stack
Python, pandas, NumPy, Matplotlib, psycopg2 (Redshift), Jupyter, SQL (80+ queries across 5 Redshift clusters), ThreadPoolExecutor (parallel query execution), Parquet caching, openpyxl, holidays (actualization logic), automated email delivery

## What This Shows
- **Customer intelligence at scale**: Not just "who are our top customers" but "what's their momentum, where are they in their growth trajectory, what's driving their spend, and what's the risk signal" — across 7 product dimensions simultaneously
- **Data storytelling**: Every analytical layer produces narrative output. The commentary generator, the executive summary, the per-customer deep-dives — all designed to be consumed by non-technical stakeholders
- **Segmentation thinking**: 6-tier cohort framework, product-level decomposition (Core vs. GenAI vs. Auto Mode vs. Extended Support), pricing model mix analysis
- **Executive communication**: Health quadrant scatter plots, CWGR heatmaps, Pareto charts, momentum donut charts — visual language designed for VP/SVP audiences
- **Systems thinking**: Parallel query execution, Parquet caching with freshness checks, actualization logic (WD7 business day calculation), fallback data sources for missing customers, validation framework cross-checking SQL output against Excel source of truth

## Portfolio Angle
I built the customer intelligence engine behind the weekly executive review for a multi-billion-dollar cloud services portfolio. What used to take 4–6 hours of manual work every Monday now runs in 25–30 minutes — freeing the team to spend Monday morning on analysis instead of data wrangling. The platform doesn't just query data — it classifies customer momentum, decomposes revenue drivers across product dimensions, tracks cohort migration, and generates the narrative. Each service (EKS, ECS/Fargate, ECR) has its own 13-section analytical workbook with health quadrant analysis, CWGR trajectory heatmaps, Pareto concentration charts, and auto-generated commentary. The WBR dashboard layer reconciles gross-to-net revenue across data sources, and the commentary engine produces paragraphs you paste directly into the executive deck. This is the kind of customer analytics that PMMs use to inform positioning, identify expansion opportunities, and build competitive intelligence — I just built the system that produces it.

---

## What's Included in This Repo

### Code Samples (`../samples/service-analytics/`)

**1. `commentary_generator_pattern.py`** — Sanitized excerpt showing the commentary generation architecture. Demonstrates how raw cohort data gets transformed into narrative paragraphs with YoY attribution, sub-product decomposition, and cohort-level drivers. All real numbers replaced with generic examples.

**2. `cache_engine_pattern.py`** — The SQL caching architecture (run → parquet → freshness check). Fully generic, no proprietary data.

### Architecture Diagrams (`../visuals/service-analytics/`)

**3. Architecture diagram** — Create using draw.io or similar:
```
Redshift (5 clusters) ──→ 80+ SQL Queries (parallel) ──→ Parquet Cache
                                                              ↓
Six Blockers Excel ──→ Python Loader ──→ Structured DataFrames
                                                              ↓
                                    ┌─────────────────────────┼──────────────────────────┐
                                    ↓                         ↓                          ↓
                          Customer Analytics           WBR Dashboard              Commentary Engine
                          (per-service notebooks)      (revenue reconciliation)   (auto-generated narrative)
                                    ↓                         ↓                          ↓
                          • Top-N WBR tables          • Gross-to-net bridge       • WBR deck paragraphs
                          • Health quadrant           • DDC rate validation       • Cohort attribution
                          • CWGR heatmaps             • CRF rate comparison       • Sub-product YoY
                          • Cohort analysis                                       • Portfolio summary
                          • Customer deep-dives
                          • Momentum classification
                          • Rank streaks
                          • Executive summary
```

**4. Notebook structure screenshot** — Open `EKS_CustomerAnalytics_Weekly.ipynb`, collapse all code cells, screenshot the 13 section headers. Shows analytical depth without exposing data.

**5. Visualization mockups** — Recreate with fake data:
- CWGR trajectory heatmap (customers × time horizons, red-yellow-green)
- Health quadrant scatter (WoW $ vs YoY %, bubble size = revenue)
- Revenue Pareto bar chart with cumulative % line
- Cohort stacked area chart (6 tiers over time)
- Momentum donut chart (Accelerating/Recovering/Decelerating/Declining)

**6. Commentary output mockup** — Fake-data example:
> "The strong YoY growth (+18.2%) is mainly attributed to 1/ growing adoption of Product Alpha by top 1-10 and 11-100 customer cohorts driving +$X.XM revenue increase YoY and 2/ growth in Product Beta revenue (+12.1% YoY) with momentum in the 1-10 (+22.3% YoY), 11-100 (+15.1% YoY) cohorts, partially offset by softness in 101-1000 (-3.2%)."

### What NOT to Include
- ❌ No real revenue numbers, customer names, or internal endpoints
- ❌ No SQL referencing internal schemas/tables
- ❌ No credentials, connection strings, or cluster hostnames
- ❌ No screenshots of actual notebook output cells with real data
- ❌ No Six Blockers Excel file
