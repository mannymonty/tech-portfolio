# C&S Service Analytics Platform
*Enterprise Revenue Analytics & Executive Reporting*

## The Problem
A portfolio of cloud container services generates hundreds of millions in weekly revenue across thousands of customers. Leadership needs a clear, weekly picture: what moved, why, and what's the trajectory — delivered as executive-ready commentary, not raw spreadsheets.

## What I Built
A full analytics platform that pulls data from Redshift, applies business logic (gross-to-net revenue reconciliation, CRF rate adjustments, cohort classification), and produces:

- **Automated WBR commentary** — narrative paragraphs covering revenue trends, customer cohort movements, YoY/WoW deltas, and concentration risk, generated directly from data
- **Condensed executive dashboard** — self-contained notebook that queries, caches, validates, and visualizes the full weekly business review in one run
- **Customer analytics suite** — per-service notebooks tracking top-100 customers, increasers/decreasers, cohort migration, and growth signals
- **UE (Unit Economics) breakdown** — weekly cost analysis with detail for margin visibility

## Tech Stack
Python, pandas, NumPy, Matplotlib, psycopg2 (Redshift), Jupyter, SQL (50+ queries), Parquet caching, openpyxl, automated email delivery

## PMM Skills Demonstrated
- **Data storytelling**: The commentary generator turns raw revenue data into business narratives
- **Customer segmentation**: Cohort analysis (top 1-10, 11-100, 101-1000, long tail)
- **Executive communication**: Every output designed for VP/SVP audience
- **Market intelligence**: Weekly tracking of customer movements and growth signals
- **Systems thinking**: Caching layer, validation framework, modular SQL library

## Portfolio Angle
I built the analytics engine behind a weekly executive review covering a multi-billion-dollar cloud services portfolio. The system doesn't just query data — it generates the narrative. Revenue trends, customer cohort movements, concentration risk, YoY growth signals — all auto-produced and delivered as business-ready commentary.

---

## What's Included in This Repo (Sanitized)

### Code Samples (`../samples/service-analytics/`)

**1. `commentary_generator_pattern.py`** — Sanitized excerpt showing the commentary generation architecture. Demonstrates how raw data gets transformed into narrative paragraphs. All real revenue numbers, customer names, and service names replaced with generic examples.

**2. `cohort_analysis_pattern.py`** — Sanitized excerpt showing the cohort pivot + YoY/WoW computation pattern. Shows the analytical framework without any real data.

**3. `cache_engine_pattern.py`** — The SQL caching architecture (run → parquet → freshness check). This is fully generic and contains no proprietary data.

### Architecture Diagrams (`../visuals/service-analytics/`)

**4. `architecture_diagram.png`** — Hand-drawn or diagrammed data flow:
```
Six Blockers Excel → Python Loader → Structured DataFrames
                                          ↓
Redshift (5 clusters) → SQL Queries → Parquet Cache
                                          ↓
                              Cohort Analysis Engine
                                          ↓
                    ┌─────────────────────┼──────────────────────┐
                    ↓                     ↓                      ↓
            WBR Commentary      Executive Dashboard      Customer Deep Dives
            (auto-generated      (Jupyter notebook)      (per-service notebooks)
             narrative text)
                    ↓                     ↓                      ↓
              Email delivery      Rendered HTML/PDF        Stakeholder review
```

**5. `notebook_structure_screenshot.png`** — Screenshot of the Jupyter notebook TABLE OF CONTENTS / cell headers only (collapse all cells, show just the markdown headers). This shows the analytical structure without exposing any data.

**6. `commentary_output_mockup.png`** — A MOCKUP of what the generated commentary looks like, using fake numbers. Example:

> "Service X revenue was $XX.XM in Wk 14, up +2.3% WoW. The strong YoY growth (+18.2%) is mainly attributed to 1/ growing adoption of Product A by top 1-10 and 11-100 customer cohorts driving +$X.XM revenue increase YoY and 2/ growth in Product B revenue (+12.1% YoY). Top 3 increasers: Customer Alpha (+$XXK), Customer Beta (+$XXK), Customer Gamma (+$XXK)."

Create this as a styled text block or screenshot from a markdown renderer with fake data.

### What NOT to Include
- ❌ No real revenue numbers (not even ranges or orders of magnitude)
- ❌ No customer names (not even anonymized like "Customer A" if the pattern could be reverse-engineered)
- ❌ No SQL queries that reference internal table names, schemas, or database endpoints
- ❌ No screenshots of actual notebook output cells with data
- ❌ No credentials.env or any connection strings
- ❌ No Six Blockers Excel file or any reference to its internal structure
- ❌ No Redshift cluster hostnames or internal URLs
