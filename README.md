# CryptoMarketTracker

A full data pipeline and analytics project that pulls crypto price history, stores it in SQLite, computes performance and risk KPIs in Python, and visualizes insights in an interactive Tableau dashboard.

The objective is to move beyond simple price charts and quantify:

- How far an asset is from its All-Time High
- How much return it generates relative to risk (Sharpe Ratio)
- How severe losses can get (maximum drawdown)
- Whether current volatility indicates stability or danger

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

## Summary

Price charts show movement.  
This project measures performance.

By combining database storage, Python-based analytics, and a Tableau front end, it enables both quantitative KPI analysis and intuitive visualization. The pipeline is modular, reusable, and can be scaled to additional assets or time periods.

