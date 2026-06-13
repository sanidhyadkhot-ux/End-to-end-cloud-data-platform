import pandas as pd
from pathlib import Path

silver_path = Path("data/silver/silver_market_ticks.csv")
gold_path = Path("data/gold/gold_market_daily_metrics.csv")

df = pd.read_csv(silver_path, parse_dates=["event_timestamp"])
gold = df.groupby(["symbol", "event_date"]).agg(
    open_price=("price", "first"),
    close_price=("price", "last"),
    high_price=("price", "max"),
    low_price=("price", "min"),
    total_volume=("volume", "sum"),
    total_trade_value=("trade_value", "sum"),
    avg_price=("price", "mean")
).reset_index()

gold["daily_return_pct"] = ((gold["close_price"] - gold["open_price"]) / gold["open_price"] * 100).round(2)
gold.to_csv(gold_path, index=False)
print("Gold metrics created.")
