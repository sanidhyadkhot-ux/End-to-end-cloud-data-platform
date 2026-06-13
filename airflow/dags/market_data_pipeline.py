from datetime import datetime, timedelta

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except Exception:
    DAG = None
    PythonOperator = None

def extract_market_data():
    print("Extracting market data from API simulation")

def validate_raw_data():
    print("Running raw data validation")

def load_bronze():
    print("Loading raw files to Bronze layer")

def run_databricks_job():
    print("Triggering Databricks Spark transformations")

def run_dbt_models():
    print("Running dbt Silver and Gold models")

def publish_dashboard_outputs():
    print("Publishing Power BI / Streamlit-ready outputs")

if DAG:
    default_args = {
        "owner": "student-data-engineering-project",
        "retries": 1,
        "retry_delay": timedelta(minutes=5)
    }

    with DAG(
        dag_id="market_data_platform_pipeline",
        default_args=default_args,
        start_date=datetime(2025, 1, 1),
        schedule_interval="@hourly",
        catchup=False
    ) as dag:
        extract = PythonOperator(task_id="extract_market_data", python_callable=extract_market_data)
        validate = PythonOperator(task_id="validate_raw_data", python_callable=validate_raw_data)
        bronze = PythonOperator(task_id="load_bronze", python_callable=load_bronze)
        databricks = PythonOperator(task_id="run_databricks_job", python_callable=run_databricks_job)
        dbt = PythonOperator(task_id="run_dbt_models", python_callable=run_dbt_models)
        publish = PythonOperator(task_id="publish_dashboard_outputs", python_callable=publish_dashboard_outputs)

        extract >> validate >> bronze >> databricks >> dbt >> publish
