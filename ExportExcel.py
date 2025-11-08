import sqlite3
import pandas as pd
from pathlib import Path
import re

# Config
DatabasePath = "CryptoData.db"
OutputDir = Path("exports")
CoinsDir = OutputDir / "coins"
OutputDir.mkdir(parents=True, exist_ok=True)
CoinsDir.mkdir(parents=True, exist_ok=True)

EXPORT_CSV = True
EXPORT_XLSX = True

def SafeName(s: str) -> str:
    """Make a filesystem-safe lowercase name (spaces -> _)."""
    if s is None:
        return "unknown"
    s = str(s).strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s-]+", "_", s)
    return s or "unknown"

# Connect to DB
connect = sqlite3.connect(DatabasePath)

try:
    print("Reading crypto_prices table...")
    df = pd.read_sql_query("SELECT coin, symbol, timestamp, price, market_cap, volume FROM crypto_prices", connect)

    if df.empty:
        print("No data found in table")
    else:
        df.columns = df.columns.str.lower()

        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
            df["timestamp"] = df["timestamp"].dt.tz_convert("UTC").dt.strftime("%Y-%m-%d %H:%M:%S")

        if "coin" in df.columns and not df["coin"].isna().all():
            group = "coin"
        elif "symbol" in df.columns and not df["symbol"].isna().all():
            group = "symbol"
        else:
            group = None

        columns = ["coin", "symbol", "timestamp", "price", "market_cap", "volume"]
        columns = [c for c in columns if c in df.columns]

        if group:
            print(f"Exporting by {group}...")
            for name, data in df.groupby(group):
                file = SafeName(name)
                csvPath = CoinsDir / f"{file}.csv"
                xlsxPath = CoinsDir / f"{file}.xlsx"

                out = data[columns]

                if EXPORT_CSV:
                    out.to_csv(csvPath, index=False)
                if EXPORT_XLSX:
                    out.to_excel(xlsxPath, index=False)

                print(f"Wrote {csvPath} and {xlsxPath}")
        else:
            csvPath = OutputDir / "crypto_prices.csv"
            xlsxPath = OutputDir / "crypto_prices.xlsx"

            out = df[columns]

            if EXPORT_CSV:
                out.to_csv(csvPath, index=False)
            if EXPORT_XLSX:
                out.to_excel(xlsxPath, index=False)

            print(f"Wrote {csvPath} and {xlsxPath}")

finally:
    connect.close()

print("Export complete")




