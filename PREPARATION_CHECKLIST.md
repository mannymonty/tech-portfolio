# Portfolio Repo — Preparation Checklist

## What's Already Done (ready to push)
- [x] README.md (landing page)
- [x] 6 case study markdown files in case-studies/
- [x] Sanitized code samples: commentary_generator_pattern.py, cache_engine_pattern.py
- [x] Architecture overview for BI Queries (query-runner/architecture_overview.md)
- [x] videos/README.md (template for FinAI video links)

## What You Need to Add

### Visuals — Service Analytics (`visuals/service-analytics/`)

1. **Notebook structure screenshot**
   - Open `notebooks/WBR_Condensed_Dashboard_v2.ipynb` in Jupyter
   - Collapse ALL code cells (View → Collapse All Code)
   - Screenshot showing just the markdown section headers
   - This shows analytical structure without any data
   - SAFE: no data visible, just headers like "Setup", "Load Data", "Validation", etc.

2. **Architecture diagram**
   - Use draw.io, Excalidraw, or even PowerPoint
   - Recreate the text diagram from case-studies/01-service-analytics.md
   - Shows: Data Sources → Processing → Outputs flow
   - SAFE: no internal names needed, use generic labels

3. **Commentary output mockup**
   - Open any text editor or markdown renderer
   - Type a FAKE commentary paragraph using the pattern from the code sample
   - Use completely made-up numbers and generic service/customer names
   - Screenshot that rendered text
   - SAFE: entirely fabricated data
   - Example:
     > "Service Alpha revenue was $42.3M in Wk 14, up +2.1% WoW.
     > The strong YoY growth (+17.8%) is mainly attributed to
     > 1/ growing adoption of Product Beta by top 1-10 and 11-100
     > customer cohorts driving +$3.2M revenue increase YoY..."

### Visuals — BI Queries (`visuals/bi-queries/`)

4. **runFolders.txt screenshot**
   - Open `runFolders.txt` in your editor
   - Screenshot it — this is just folder paths, no sensitive data
   - Shows the declarative config-driven architecture
   - REVIEW FIRST: make sure no folder names reveal sensitive project names
   - If needed, blur or redact specific folder names

5. **Terminal output screenshot**
   - Run the script (or find a log in `logs/`)
   - Screenshot showing the progress output: "[query] name... 1,234 rows (2.3s)"
   - REDACT: any query names that reveal internal project names
   - KEEP: the timing, row counts, and "[cache]" / "[query]" pattern — that's the story

6. **Outputs directory tree**
   - Screenshot of the `Outputs/Latest/` folder in Windows Explorer
   - Shows 20+ subfolders = 20+ reporting suites
   - REDACT: blur any folder names that are sensitive

### Visuals — Snapshot (`visuals/snapshot/`)

7. **Screenshots from your live app**
   - app.takesnapshot.com — this is YOUR product, fully safe
   - Dashboard waterfall chart
   - Player profile / character sheet
   - Mobile home screen
   - Snapshot comparison view
   - Promo site hero section + pricing page
   - Use the demo personas (not your real financial data)

### Visuals — ARI (`visuals/ari/`)

8. **GUI app screenshot**
   - Run `ARI App/dist/ARI_Data_Processor.exe`
   - Screenshot the GUI (file browser, progress bar, log output)
   - SAFE: the GUI itself contains no data, just the interface

9. **Script evolution diagram**
   - Create a simple timeline graphic:
     v1 CLI → v2 Summary → v3 Auto-discovery → v4 Paste-path → v5 GUI
   - Add one-line user feedback that drove each iteration
   - SAFE: no data involved

### Visuals — PCS (`visuals/pcs/`)

10. **Widget UI screenshot**
    - Open the Jupyter notebook, show the ipywidgets dropdowns
    - SAFE if: region names are public (AWS region names are public)
    - REDACT: any internal service names or pricing numbers
    - Best approach: screenshot with dropdowns visible but no results calculated yet

11. **HTML output table with FAKE data**
    - Run the tool with a test case, then replace all dollar amounts with fake numbers
    - Or: create a mockup table in HTML showing the format (gold headers, green/red deltas)
    - SAFE: if all numbers are fabricated

### Videos — FinAI (`videos/`)

12. **Video links**
    - If videos are on internal platforms: re-record short highlight clips (30-60s) on Loom
    - If you can't share the actual videos: screenshot title cards / key frames
    - Add descriptions to videos/README.md
    - REVIEW: make sure no internal dashboards, customer data, or proprietary tools are visible

## Final Sanitization Checklist (before `git push`)

- [ ] `grep -ri "amazon" .` — remove any Amazon-specific references
- [ ] `grep -ri "@amazon" .` — remove email addresses
- [ ] `grep -ri "mannymv" .` — replace with your public identity
- [ ] `grep -ri "redshift" .` — OK in generic context, remove specific endpoints
- [ ] `grep -ri "password\|credential\|secret\|token" .` — must be zero results
- [ ] `grep -ri "\.amazon\.com" .` — remove internal URLs
- [ ] No `.env` files, no `credentials.env`
- [ ] No parquet/xlsx data files
- [ ] No SQL files that reference internal schemas/tables
- [ ] Review every screenshot for visible data, customer names, or internal URLs
