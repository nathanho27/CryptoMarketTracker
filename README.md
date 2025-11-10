## CryptoMarketTracker

Crypto dashboards usually answer one question:
"What is the price doing?"

This project answers a better set of questions:

- Is the asset recovering or still far from its previous peak

- Is the return worth the volatility and risk

- What is the worst historical loss someone could have experienced

- Is the current market calm or unstable

CryptoMarketTracker pulls historical price data, stores it in a SQLite database for structured querying, computes performance and risk KPIs in Python, and visualizes insights in an interactive Tableau dashboard.

The goal is not to visualize price movement.
The goal is to measure performance.

---

## Live Dashboard

Tableau Public:  
https://public.tableau.com/app/profile/nathan.ho2158/viz/CryptoMarketTrackerBTCETH/Dashboard1

Dashboard includes:

- Interactive selection between assets (BTC and ETH)
- Price trend with moving average overlays
- Daily returns and volatility behavior
- A visual layer to explore short-term movement and momentum

---

## What makes this useful

Most crypto analysis stops at price.
This project quantifies risk-adjusted performance.

# Performance KPIs (investment focused)

- Percent from All Time High
Shows how far the asset still needs to recover

- Sharpe Ratio (annualized)
Measures return relative to volatility and risk

- Maximum Drawdown
The worst historical loss from peak to bottom

- Win Rate (overall + rolling 90 days)
How often the asset closes positive

# Market Behavior KPIs (analytics focused)

- 30-day correlation vs Bitcoin
Detects whether the asset behaves independently or just follows BTC

- Volatility Regime Classification
Labels the environment as Low / Medium / High volatility

# These metrics allow you to answer:

- Are we recovering or sinking

- Is this asset moving on its own or in Bitcoin's shadow

- Are we in a stable or unstable environment

This turns crypto from speculation into risk-aware decision making.

---

Pipeline Overview

1. Raw historical price data is pulled or imported into data/raw/

2. LoadToSQLite.py loads all CSV files into a SQLite database and enforces structure

3. SQL.ipynb builds a daily_summary table with OHLC data, volume, and daily returns

4. BtcKPI.ipynb calculates performance and risk KPIs

5. ExportExcel.py exports cleaned tables for Tableau and external analysis

6. Tableau consumes the final exports for interactive exploration

No manual transformations.
No spreadsheet cleanup.
Fully reproducible.

---

## Repository Structure

```
CryptoMarketTracker/
│── Workbook/              # Tableau workbook
│── data/raw/              # Historical CSV price data
│── exports/               # Exported KPI tables and output files
│── BtcKPI.ipynb           # KPI and performance analysis notebook
│── SQL.ipynb              # SQL queries and daily aggregation logic
│── LoadToSQLite.py        # Loads raw CSVs into SQLite
│── DataFetch.py           # Data pull script (optional)
│── ExportExcel.py         # Exports SQLite tables to Excel
│── CryptoData.db          # SQLite database (not committed; ignored via .gitignore)
│── README.md
└── .gitignore
```

---

## Tech Stack

- Python (pandas, numpy, sqlite3, matplotlib)
- SQLite for structured storage
- Jupyter Notebooks for analysis
- Tableau for dashboard visualization
- Git and GitHub for version control

---

## KPIs and Metrics Calculated

### Core Performance Metrics
- Percent From All Time High
- Sharpe Ratio (annualized)
- Max Drawdown

### Market Behavior Metrics
- 30-day correlation vs Bitcoin
- Win Rate (all time and rolling 90 days)
- Volatility regime classification (Low / Medium / High)

These metrics answer:

- Is the asset recovering or still far from previous highs?
- Is it generating return efficiently relative to volatility?
- What is the worst-case historical decline?
- Is the asset behaving independently or following market beta?
- Is today’s volatility environment stable or elevated?

---

## How to Run

1. Load all CSV price data into SQLite  
   ```sh
   python LoadToSQLite.py
   ```

2. Build aggregated daily tables  
   Open and run:
   ```
   SQL.ipynb
   ```

3. Compute performance and risk KPIs  
   Open and run:
   ```
   BtcKPI.ipynb
   ```

Results are exported to:

```
exports/coreKpis.csv
exports/extraKpis.csv

```
---
## Insights observed

During the build, several patterns showed up:

BTC’s Sharpe ratio improves significantly only when volatility shifts into low regime

ETH shows higher upside during positive momentum but worse drawdown severity

High volatility regimes consistently follow large negative daily return clusters

Correlation increases during market stress (flight-to-Bitcoin behavior)

The project made it obvious that:

Crypto returns are only impressive when viewed in context of risk.
---

## Summary

Price charts show movement.  
This project measures performance.

By combining database storage, Python-based analytics, and a Tableau front end, it enables both quantitative KPI analysis and intuitive visualization. The pipeline is modular, reusable, and can be scaled to additional assets or time periods.

