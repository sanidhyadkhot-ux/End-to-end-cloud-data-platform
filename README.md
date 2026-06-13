# End-to-End Cloud Data Platform  
## Automated Data Pipeline with Real-Time Analytics Dashboard

![Project](https://img.shields.io/badge/Project-Cloud%20Data%20Platform-blue)
![Learning](https://img.shields.io/badge/Student%20Project-Master's%20Level-green)
![Stack](https://img.shields.io/badge/Stack-Airflow%20%7C%20Databricks%20%7C%20dbt%20%7C%20Snowflake%20%7C%20Power%20BI-purple)
![Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-orange)

## 1. Overview

This is a master's-level student portfolio project I developed to practise building a modern cloud-style data engineering platform from end to end.

The project simulates a real data platform that ingests market, weather and macroeconomic data, processes it through a medallion architecture, applies data quality checks, creates analytics-ready Gold models, and serves insights through dashboard mockups and a Streamlit live demo.

The focus is not only on showing tools, but on demonstrating how I am learning to think like a data engineer:

- How should raw data be ingested?
- How should pipelines be orchestrated?
- How should data quality be checked?
- How should raw data become analytics-ready?
- How should CI/CD and infrastructure be documented?
- How should a data product be monitored after deployment?

---

## 2. Project Scenario

The simulated business use case is:

> A financial analytics team needs a near real-time data platform to monitor ASX-style market activity, enrich it with weather and macroeconomic indicators, and deliver trusted analytics to business users through dashboards.

The platform is designed to process high-frequency market data and reduce reporting latency from daily batch reporting to near real-time analytics.

---

## 3. Architecture

```text
API / Streaming Sources
ASX Market Data | Weather Data | Macro Indicators
        |
        v
Kafka / Kinesis Simulation
        |
        v
Apache Airflow Orchestration
        |
        v
Azure Data Lake / Bronze Layer
        |
        v
Databricks + Spark Transformations
        |
        v
Silver Cleaned Layer
        |
        v
dbt Models + Data Tests
        |
        v
Gold Analytics Layer
        |
        v
Snowflake / Warehouse Serving Layer
        |
        v
Power BI Dashboard + Streamlit Demo
        |
        v
Monitoring, Data Quality, CI/CD
```

---

## 4. Why I Built This

As a Master of IT / Data Analytics student, I wanted to build a project that goes beyond a simple notebook or dashboard.

This project helps me practise:

- Data ingestion patterns
- Orchestration with Airflow
- Spark and Databricks-style transformation logic
- dbt modelling concepts
- Medallion architecture
- Data quality testing
- Warehouse modelling
- CI/CD thinking
- Terraform-style infrastructure planning
- Dashboard and monitoring design
- Live demo presentation

---

## 5. Tech Stack

| Layer | Tools Used / Simulated |
|---|---|
| Ingestion | Python, API simulation, Kafka/Kinesis design |
| Orchestration | Apache Airflow DAGs |
| Processing | Databricks-style PySpark notebooks |
| Transformation | dbt models |
| Storage | Azure Data Lake / Snowflake-style layers |
| Modelling | Bronze, Silver, Gold Medallion Architecture |
| Dashboard | Power BI mockups and Streamlit live demo |
| CI/CD | GitHub Actions workflow |
| IaC | Terraform templates |
| Monitoring | Data quality, freshness and latency checks |

---

## 6. Data Sources

This project includes synthetic but realistic sample datasets:

| Dataset | File |
|---|---|
| ASX-style market tick data | `data/raw/asx_market_ticks.csv` |
| Weather hourly data | `data/raw/weather_hourly.csv` |
| RBA/ABS-style macro indicators | `data/raw/rba_abs_macro_indicators.csv` |

The project is designed so real APIs can be added later.

---

## 7. Medallion Architecture

### Bronze Layer

Raw ingested data.

```text
data/bronze/bronze_asx_market_ticks.csv
```

Purpose:

- Preserve raw source records
- Enable replay and auditability
- Support schema evolution

### Silver Layer

Cleaned and standardised records.

```text
data/silver/silver_market_ticks.csv
```

Transformations:

- Timestamp standardisation
- Duplicate removal
- Minute-level buckets
- Type validation
- Derived fields

### Gold Layer

Business-ready analytics.

```text
data/gold/gold_market_daily_metrics.csv
```

Metrics:

- Open price
- Close price
- High price
- Low price
- Total volume
- Total trade value
- Average price
- Daily return percentage

---

## 8. Airflow Orchestration

The Airflow DAG is located in:

```text
airflow/dags/market_data_pipeline.py
```

It includes tasks for:

1. Extracting market data
2. Validating raw files
3. Loading Bronze layer
4. Running Databricks transformations
5. Running dbt models
6. Running data quality checks
7. Publishing dashboard-ready outputs

---

## 9. Databricks / Spark Layer

Databricks-style notebooks are included in:

```text
databricks/notebooks/
```

Notebook files:

```text
01_bronze_ingestion.py
02_silver_transformations.py
03_gold_aggregations.py
04_delta_live_tables_design.py
05_databricks_workflow_notes.py
```

These explain how the project would be implemented in Databricks with Spark and Delta Lake concepts.

---

## 10. dbt Layer

The dbt project includes:

```text
dbt/models/bronze/
dbt/models/silver/
dbt/models/gold/
dbt/tests/
```

The dbt models show how data would be transformed into analytics-ready views and tested for quality.

---

## 11. Data Quality

Data quality checks are included in:

```text
src/quality/data_quality_checks.py
sql/data_quality_checks.sql
```

Checks include:

- Null validation
- Duplicate validation
- Price range checks
- Volume checks
- Freshness checks
- Row count checks
- Schema checks

---

## 12. CI/CD

GitHub Actions workflow:

```text
.github/workflows/data_platform_ci.yml
```

The workflow is designed to run:

- Python checks
- dbt tests
- SQL validation
- Data quality tests
- Project structure checks

---

## 13. Terraform / Infrastructure as Code

Terraform templates are included in:

```text
terraform/
```

They document planned cloud resources:

- Storage account / data lake
- Databricks workspace
- Snowflake warehouse
- Airflow environment
- Key vault / secrets
- Monitoring resources

This is a student project, so the Terraform is designed as a portfolio-ready infrastructure plan rather than a deployed production environment.

---

## 14. Live Demo

A Streamlit demo app is included:

```text
streamlit_app/app.py
```

Run locally:

```bash
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

The app shows:

- Market metrics
- Trade value trends
- Symbol-level performance
- Pipeline status
- Data quality summary

---

## 15. Dashboard Mockups

Dashboard screenshots are included in:

```text
outputs/dashboard_mockups/
```

Included mockups:

- `powerbi_live_market_dashboard.png`
- `data_engineering_monitoring_dashboard.png`

These mockups show how I would present the final data product in Power BI.

---

## 16. Monitoring Strategy

Monitoring documents are included in:

```text
monitoring/
```

Monitoring areas:

- Pipeline freshness
- Row count anomalies
- Data quality score
- Pipeline latency
- Failed DAG tasks
- Dashboard refresh status
- Cost and compute monitoring

---



---

## 18. How to Run Locally

```bash
pip install -r requirements.txt
python src/ingestion/generate_sample_data.py
python src/quality/data_quality_checks.py
streamlit run streamlit_app/app.py
```

---

## 19. Skills Practised

This project helped me practise:

- Python data engineering
- SQL analytics modelling
- Apache Airflow design
- Databricks / Spark architecture
- dbt modelling
- Data quality engineering
- CI/CD workflow design
- Terraform infrastructure planning
- Dashboard design
- Data product documentation
- Monitoring and observability

---

## 20. Future Improvements

In future versions, I would like to:

- Connect to a real ASX or financial market API
- Deploy the Streamlit app to Streamlit Cloud
- Deploy the pipeline on Azure
- Add real Kafka streaming
- Add Delta Live Tables
- Add Snowflake trial warehouse deployment
- Add dbt docs site
- Add Great Expectations
- Add Power BI Service dashboard link
- Add cost monitoring dashboard

---
