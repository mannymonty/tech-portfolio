# ARI Invoice Data Automation
*Process Automation for Finance Teams*

## The Problem
Finance analysts spent hours every month manually filtering 200K+ invoice rows in Excel — classifying expenses across 7 categories, cleaning supplier names, splitting data for stakeholder reports. Error-prone, tedious, and repeated every single month. The time cost wasn't just the hours — it was the cognitive load of doing high-stakes data work manually with no audit trail.

## What I Built
An automated data pipeline that applies the same business rules in under 2 minutes. Iterated through 5 versions based on real user feedback:

1. **v1 — Basic CLI**: Core processing engine, manual file paths
2. **v2 — Enhanced summary**: Added reconciliation reports and audit trail
3. **v3 — Auto-discovery**: Detects monthly/quarterly folder naming conventions automatically
4. **v4 — Paste-path hybrid**: Users paste paths for custom folders ("I don't want to type paths")
5. **v5 — GUI desktop app**: Packaged as .exe with PySimpleGUI for non-technical teammates

Also built: automated stakeholder email templates, Excel formula-driven narrative generators, data quality safeguards with dropped-row reconciliation.

## Tech Stack
Python 3.13, pandas, openpyxl, PySimpleGUI, PyInstaller (.exe packaging), tqdm

## What This Shows
- **Customer empathy**: Each version was a direct response to real user friction — iterative product development driven by actual feedback
- **Product sense**: Same engine, multiple interfaces for different user contexts (power user CLI vs. non-technical GUI)
- **Process optimization**: Multi-hour manual workflow → < 2-minute automated pipeline
- **Data storytelling**: Automated summary reports and Excel templates that generate ready-to-send stakeholder narratives
- **Root cause analysis**: Traced a 20x data volume anomaly to a misconfigured dashboard filter — knowing when the problem isn't your product

## Key Visuals (`../visuals/ari/`)

- `ARI_GUI.png` — GUI application (file browser, progress bar, live log)

## Portfolio Angle
I inherited a manual, error-prone Excel workflow that finance analysts spent hours on every month. I built an automated pipeline that processes 200K+ rows in under 2 minutes, then iterated through 5 versions based on real user feedback — from CLI to auto-discovery to a packaged .exe that non-technical teammates run with zero setup. Each version was a direct response to a specific friction point a real user hit. The evolution story is the point: I listen, I ship, I iterate. That's the product development loop, applied to an internal tool.
