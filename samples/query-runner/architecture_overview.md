# BI Queries Automation — Architecture Overview

## How It Works

```
runFolders.txt (config)          db_map.txt (per folder)
┌──────────────────────┐         ┌─────────────────────────┐
│ Q/CustomerAnalytics   │         │ query_1.sql: cluster_a  │
│ Q/Monthly             │  ───►   │ query_2.sql: cluster_b  │
│ Q/UnitEconomics       │         │ query_3.sql: cluster_a  │
│ # Q/Disabled (skip)   │         └─────────────────────────┘
└──────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────┐
│              SQL Execution Engine                      │
│                                                        │
│  • Reads config → resolves folder paths                │
│  • Per-query DB routing via db_map.txt                 │
│  • Connection pooling (one conn per cluster)           │
│  • Sequential execution with timing + logging          │
│  • Error recovery: reconnect on failure, continue      │
└──────────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────┐
│              Dual Output Strategy                      │
│                                                        │
│  Outputs/03282026/FolderName/foldername_03282026.xlsx  │  ← dated archive
│  Outputs/Latest/FolderName/foldername_latest.xlsx      │  ← canonical (Power Query reads this)
│  W:\SharedDrive\Current\foldername_latest.xlsx         │  ← external copy for other teams
└──────────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────┐
│              Smart Email Distribution                  │
│                                                        │
│  • Auto-attaches all _latest.xlsx files                │
│  • Detects files > 20MB → skips attachment             │
│  • Sends follow-up with shared drive links instead     │
│  • Archives to team document store                    │
└──────────────────────────────────────────────────────┘
```

## Config-Driven Design

Adding a new reporting suite requires zero code changes:

1. Create a folder with `.sql` files
2. Add a `db_map.txt` mapping each query to a database cluster
3. Add the folder path to `runFolders.txt`
4. Done — next scheduled run picks it up automatically

This is why other teams adopted it: they just add their own folders.

## Production Stats
- 80+ SQL queries across 5 database clusters
- 20+ reporting suites (weekly, monthly, ad-hoc)
- 117+ logged production runs over 6 months
- Reduced Monday WBR production from ~6 hours to ~25 minutes
