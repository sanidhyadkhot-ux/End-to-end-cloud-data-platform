import json
import time
import pandas as pd

def stream_rows(csv_path: str):
    df = pd.read_csv(csv_path)
    for _, row in df.head(10).iterrows():
        message = row.to_dict()
        print(json.dumps(message, default=str))
        time.sleep(0.1)

if __name__ == "__main__":
    stream_rows("data/raw/asx_market_ticks.csv")
