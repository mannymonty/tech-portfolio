# BI Queries Automation Platform
*WBR Production Pipeline & Cross-Team Reporting Infrastructure*

## The Problem
Every Monday, the extended team started early to produce the Weekly Business Review. The process: manually run 80+ SQL queries one-by-one across multiple Redshift clusters, copy results into an extremely heavy Excel workbook, format everything, and email it out. ~6 hours every week, every week, for months. It was the team's biggest recurring time sink, and it left no time for the actual analysis the WBR was supposed to enable.

## What I Built
An end-to-end automation platform that reduced WBR production from 6 hours to 25 minutes:

- **Config-driven batch execution**: `runFolders.txt` specifies which SQL folders to run; per-folder `db_map.txt` routes each query to the correct Redshift cluster (5 clusters). Add a new reporting suite by adding a folder, no code changes.
- **Dual output strategy**: Dated historical archives for audit trail + canonical `_latest.xlsx` files that Power Query dashboards auto-refresh from. This enabled migration from the heavy manual Excel workbook to Power Query.
- **Smart email distribution**: Auto-attaches results via Outlook COM, detects oversized files (>20MB), sends follow-up with shared-drive links instead, archives to the team document store.
- **Interactive query runner**: For ad-hoc stakeholder requests. Remembers last recipients, lets you preview emails before sending.
- **Jupyter analysis toolkit**: Reusable notebook templates with pre-wired DB connections and a pandas cheat sheet for less technical teammates.

Running in production weekly for 6+ months (117 logged runs). Adopted by other teams across the org for their own reporting.

## Tech Stack
Python 3.13, pandas, psycopg2, openpyxl, matplotlib, numpy, tqdm, python-dotenv, Win32 COM / Outlook API, PowerShell (Task Scheduler), Amazon Redshift Serverless (5 clusters)

## What This Shows
- **Operational excellence**: 6 hours → 25 minutes (93% reduction), freeing the team for actual analysis
- **Platform thinking**: Config-driven architecture that other teams adopted without code changes
- **Customer empathy**: Interactive runner with email preview, shared-drive fallback, notebook templates with cheat sheets
- **Data storytelling**: 80+ SQL queries structured as narratives: cohort segmentation, WoW/YoY analysis, GenAI breakdowns
- **Cross-functional collaboration**: Serves finance, product, and customer analytics teams with different cadences and consumption patterns
- **Iterative evolution**: 7+ archived iterations from single-query CSV exports to the current platform

## Portfolio Angle
I inherited a 6-hour weekly reporting process and turned it into a 25-minute automated pipeline. But the real story is what happened next: I built it as a config-driven platform, and other teams across the org started using it for their own reporting, replacing manual DataGrip sessions with a single command. I didn't just solve my team's problem; I built infrastructure that scaled.
