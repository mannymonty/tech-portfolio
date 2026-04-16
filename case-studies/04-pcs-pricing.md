# PCS Region Cost & Availability Analyzer
*Pricing Intelligence for Global Expansion*

## The Problem
Cloud services aren't priced uniformly across 114 global regions, and many regions lack published pricing entirely. The team needed to know: which regions are ready for service launch, and what should pricing look like where it doesn't exist yet? The manual process — pulling pricing data, cross-referencing availability, estimating gaps — took weeks and required someone technical to run it each time.

## What I Built
A pricing intelligence toolkit with two components:

- **Region Availability Audit**: Scans 11 services across 50+ regions, produces a color-coded Excel matrix (green = full SKU coverage), outputs a prioritized TRUE/FALSE matrix grouped by P0/P1/P2 regions
- **Missing-Region Cost Estimator**: Uses EC2 (or any anchor service) price differentials to extrapolate estimated costs. Processes 1.15M+ pricing records, computes median deltas, exports estimated rows formatted for direct import into the pricing system

Interactive widget-based UI (dropdowns, multi-select, search-and-add) so non-technical stakeholders run their own analyses.

## Tech Stack
Python 3.13, Jupyter, pandas, openpyxl, ipywidgets, CSV/Excel I/O

## What This Shows
- **GTM thinking**: Availability matrix directly supports go-to-market expansion decisions
- **Data storytelling**: 1.15M raw pricing records → visual availability heatmap and color-coded cost comparisons
- **Product sense**: Real bottleneck wasn't "we need data" but "we need to estimate and fill gaps systematically"
- **Cross-functional collaboration**: Outputs designed for handoff to pricing, finance, and regional ops teams
- **Customer empathy**: Interactive UI so business users pick regions from dropdowns instead of writing code

## Key Visuals (`../visuals/pcs/`)

- Jupyter widget UI (dropdowns, multi-select, "Calculate" button)
- HTML output table with gold headers, green/red delta coloring, ★-marked estimates
- Region availability heatmap (TRUE/FALSE matrix, P0/P1/P2 grouped)
- Color-coded Excel output (green cells = full availability)
- Before/after: raw 1.15M-row CSV vs. clean actionable summary

## Portfolio Angle
When the team needed to expand cloud services into new regions, I built a pricing intelligence toolkit that ingests 1.15M+ cost records, audits availability across 114 regions, and estimates missing pricing using a statistical anchor-delta methodology. The interactive widget UI meant non-technical stakeholders — pricing, finance, regional ops — could run their own analyses without writing a line of code. A process that previously took weeks of manual work became a same-day self-serve workflow. The outputs were formatted for direct import into the pricing system, removing the last manual handoff step.
