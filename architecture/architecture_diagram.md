# Architecture Diagram

```text
ASX API + Weather API + Macro Data
        |
        v
Kafka / Kinesis Simulation
        |
        v
Airflow DAG
        |
        v
Bronze Data Lake
        |
        v
Databricks / Spark
        |
        v
Silver Cleaned Data
        |
        v
dbt Gold Models
        |
        v
Snowflake / Warehouse
        |
        v
Power BI + Streamlit
        |
        v
Monitoring + CI/CD
```
