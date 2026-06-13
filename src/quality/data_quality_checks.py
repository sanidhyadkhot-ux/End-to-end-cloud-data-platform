import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/asx_market_ticks.csv")

def run_checks():
    df = pd.read_csv(DATA_PATH)
    checks = {
        "row_count_positive": len(df) > 0,
        "timestamp_not_null": df["event_timestamp"].notna().all(),
        "symbol_not_null": df["symbol"].notna().all(),
        "price_positive": (df["price"] > 0).all(),
        "volume_positive": (df["volume"] > 0).all(),
        "duplicate_rows": df.duplicated().sum() == 0
    }
    for check, result in checks.items():
        print(f"{check}: {'PASS' if result else 'FAIL'}")
    return checks

if __name__ == "__main__":
    run_checks()
