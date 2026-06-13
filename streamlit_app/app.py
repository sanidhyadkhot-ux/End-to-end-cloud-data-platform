import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Cloud Data Platform Demo", layout="wide")

ROOT = Path(__file__).resolve().parents[1]
gold = pd.read_csv(ROOT / "data" / "gold" / "gold_market_daily_metrics.csv")

st.title("End-to-End Cloud Data Platform Demo")
st.write("Student portfolio demo for a real-time analytics data platform.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Records in Gold", f"{len(gold):,}")
col2.metric("Symbols", gold["symbol"].nunique())
col3.metric("Total Volume", f"{gold['total_volume'].sum()/1_000_000:.1f}M")
col4.metric("Trade Value", f"${gold['total_trade_value'].sum()/1_000_000_000:.2f}B")

symbol = st.selectbox("Select symbol", sorted(gold["symbol"].unique()))
filtered = gold[gold["symbol"] == symbol]

st.subheader("Daily Trade Value")
st.line_chart(filtered.set_index("event_date")["total_trade_value"])

st.subheader("Market Metrics Table")
st.dataframe(filtered.head(100))

st.subheader("Pipeline Design")
st.code("API -> Kafka/Kinesis -> Airflow -> Databricks -> dbt -> Snowflake -> Power BI")
