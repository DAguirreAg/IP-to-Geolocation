from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

import requests

PORT = 8102

def call_api(url: str):
    response = requests.get(url)
    
    if not (200<=response.status_code<=299):
        raise Exception('Something went wrong.')

def _download_country_data():
    url = f"http://localhost:{PORT}/download_country_data"    
    call_api(url)
    
def _etl_country_data():
    url = f"http://localhost:{PORT}/etl_country_data"    
    call_api(url)

with DAG("ip_to_geolocation_country_dag", # Dag id
    start_date=datetime(2023, 10 ,5), # start date, the 1st of January 2023 
    schedule='@weekly', # Cron expression, here @daily means once every day.
    catchup=False):

    # Tasks are implemented under the dag object
    download_country_data = PythonOperator(
        task_id="download_country_data",
        python_callable=_download_country_data
    )

    etl_country_data = PythonOperator(
        task_id="etl_country_data",
        python_callable=_etl_country_data
    )

    download_country_data >> etl_country_data