"""
SQL Caching Engine Pattern (Sanitized)
=======================================
This is the caching layer that sits between SQL queries and analysis notebooks.
It ensures queries only re-run when the cache is stale, dramatically reducing
iteration time during weekly reporting cycles.

Pattern: SQL → Execute → Parquet cache → Freshness check → Serve from cache or re-query

No internal endpoints, credentials, or proprietary data included.
"""
import time
from pathlib import Path
from datetime import datetime, timedelta
import pandas as pd


class CachedQueryEngine:
    """
    Cached SQL execution engine.
    
    - Runs SQL against a database connection
    - Caches results as parquet files with timestamps
    - Serves from cache if fresh enough
    - Supports forced refresh for production runs
    """
    
    def __init__(self, cache_dir, max_age_hours=12):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.max_age_hours = max_age_hours
        self._conn_pool = {}
    
    def is_fresh(self, cache_name):
        """Check if a cached parquet file is fresh enough to serve."""
        pq = self.cache_dir / f'{cache_name}.parquet'
        if not pq.exists():
            return False
        age = datetime.now() - datetime.fromtimestamp(pq.stat().st_mtime)
        return age < timedelta(hours=self.max_age_hours)
    
    def run_cached(self, sql_text, cache_name, conn, force=False):
        """
        Run SQL and cache result as parquet. Returns DataFrame.
        
        If cache is fresh and force=False, serves from cache.
        Otherwise executes the query and updates the cache.
        """
        pq = self.cache_dir / f'{cache_name}.parquet'
        
        if not force and self.is_fresh(cache_name):
            df = pd.read_parquet(pq)
            age = self._format_age(pq)
            print(f'  [cache] {cache_name}: {df.shape} (age: {age})')
            return df
        
        print(f'  [query] {cache_name}...', end=' ', flush=True)
        t0 = time.time()
        df = pd.read_sql(sql_text, conn)
        elapsed = time.time() - t0
        df.to_parquet(pq, index=False)
        print(f'{df.shape} ({elapsed:.1f}s)')
        return df
    
    def run_file_cached(self, sql_path, cache_name, conn, force=False):
        """Read SQL from file, execute, and cache."""
        pq = self.cache_dir / f'{cache_name}.parquet'
        
        if not force and self.is_fresh(cache_name):
            df = pd.read_parquet(pq)
            age = self._format_age(pq)
            print(f'  [cache] {cache_name}: {df.shape} (age: {age})')
            return df
        
        sql_text = Path(sql_path).read_text(encoding='utf-8')
        print(f'  [query] {cache_name} from {Path(sql_path).name}...', end=' ', flush=True)
        t0 = time.time()
        df = pd.read_sql(sql_text, conn)
        elapsed = time.time() - t0
        df.to_parquet(pq, index=False)
        print(f'{df.shape} ({elapsed:.1f}s)')
        return df
    
    @staticmethod
    def _format_age(pq_path):
        age = datetime.now() - datetime.fromtimestamp(pq_path.stat().st_mtime)
        hrs = age.total_seconds() / 3600
        return f'{hrs:.1f}h' if hrs >= 1 else f'{age.total_seconds()/60:.0f}m'
