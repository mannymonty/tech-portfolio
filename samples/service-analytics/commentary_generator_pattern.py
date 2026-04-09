"""
Commentary Generator Pattern (Sanitized)
=========================================
This is a sanitized excerpt showing how the WBR commentary engine
transforms raw cohort data into executive-ready narrative paragraphs.

All service names, customer names, revenue figures, and internal
references have been replaced with generic examples.

Architecture:
  Cached Data (parquet) → Cohort Pivot → YoY/WoW Computation → Narrative Builder
"""
import pandas as pd
import numpy as np


# ── Formatting helpers ────────────────────────────────────────────────────
def fmt_revenue(x):
    """Format a dollar amount for executive audiences."""
    if pd.isna(x) or x == 0: return '$0'
    if abs(x) >= 1e6: return f'${x/1e6:,.1f}M'
    if abs(x) >= 1e3: return f'${x/1e3:,.0f}K'
    return f'${x:,.0f}'

def fmt_delta(x):
    """Format a signed dollar change."""
    if pd.isna(x): return 'N/A'
    if abs(x) >= 1e6: return f'${x/1e6:+,.1f}M'
    if abs(x) >= 1e3: return f'${x/1e3:+,.0f}K'
    return f'${x:+,.0f}'

def fmt_pct(x):
    return f'{x:+.1f}%' if pd.notna(x) else 'N/A'


# ── Cohort YoY computation ───────────────────────────────────────────────
COHORT_ORDER = ['a. 1-10', 'b. 11-100', 'c. 101-1000',
                'd. 1001-10000', 'e. 10001+', 'f. Others']

def cohort_yoy_weekly(pivot_df, latest_week, yoy_reference_week):
    """
    Compute single-week YoY by customer cohort from a weekly pivot.
    
    Parameters
    ----------
    pivot_df : DataFrame with week dates as index, cohort names as columns
    latest_week : Timestamp of the current reporting week
    yoy_reference_week : Timestamp of the same week last year
    
    Returns
    -------
    DataFrame with columns: curr, prior, yoy_pct, yoy_abs per cohort
    """
    records = []
    for cohort in COHORT_ORDER + ['Total']:
        if cohort not in pivot_df.columns:
            continue
        curr = pivot_df.loc[latest_week, cohort] if latest_week in pivot_df.index else 0
        prior = pivot_df.loc[yoy_reference_week, cohort] if yoy_reference_week in pivot_df.index else 0
        yoy_pct = (curr / prior - 1) * 100 if prior > 0 else None
        records.append({
            'cohort': cohort,
            'curr': curr,
            'prior': prior,
            'yoy_pct': yoy_pct,
            'yoy_abs': curr - prior,
        })
    return pd.DataFrame(records).set_index('cohort')


# ── Narrative builder ────────────────────────────────────────────────────
def generate_commentary(service_name, cohort_yoy_df, sub_product_drivers):
    """
    Generate executive-ready commentary from cohort YoY data.
    
    This is the core pattern: take structured analytical output
    and transform it into natural language suitable for a WBR deck.
    
    Parameters
    ----------
    service_name : str
    cohort_yoy_df : DataFrame from cohort_yoy_weekly()
    sub_product_drivers : list of (product_name, yoy_abs, yoy_pct) tuples
    
    Returns
    -------
    str : narrative paragraph
    """
    total = cohort_yoy_df.loc['Total']
    total_yoy_pct = fmt_pct(total['yoy_pct'])
    
    # Identify which cohorts are driving growth
    growing_cohorts = []
    declining_cohorts = []
    for cohort in COHORT_ORDER:
        if cohort not in cohort_yoy_df.index:
            continue
        row = cohort_yoy_df.loc[cohort]
        label = cohort.split('. ')[1]  # "1-10" from "a. 1-10"
        if pd.notna(row['yoy_pct']) and row['yoy_abs'] > 0:
            growing_cohorts.append((label, row['yoy_pct'], row['yoy_abs']))
        elif pd.notna(row['yoy_pct']) and row['yoy_abs'] < 0:
            declining_cohorts.append((label, row['yoy_pct'], row['yoy_abs']))
    
    # Build attribution sentence
    drivers = sorted(sub_product_drivers, key=lambda x: -abs(x[1]))
    driver_parts = []
    for i, (prod, yoy_abs, yoy_pct) in enumerate(drivers[:3], 1):
        driver_parts.append(
            f"{i}/ {'growing adoption of' if yoy_abs > 0 else 'decline in'} "
            f"{prod} ({fmt_delta(yoy_abs)} YoY)"
        )
    
    commentary = (
        f"The {'strong' if total['yoy_pct'] > 10 else 'steady'} YoY growth "
        f"({total_yoy_pct}) is mainly attributed to "
        + " and ".join(driver_parts)
    )
    
    # Add cohort color
    if growing_cohorts:
        top_growers = sorted(growing_cohorts, key=lambda x: -x[1])[:2]
        cohort_str = ', '.join(f'{c[0]} ({fmt_pct(c[1])} YoY)' for c in top_growers)
        commentary += f", with momentum in the {cohort_str} cohorts"
    
    if declining_cohorts:
        top_decliners = sorted(declining_cohorts, key=lambda x: x[1])[:1]
        dec_str = ', '.join(f'{c[0]} ({fmt_pct(c[1])})' for c in top_decliners)
        commentary += f", partially offset by softness in {dec_str}"
    
    commentary += "."
    return commentary
