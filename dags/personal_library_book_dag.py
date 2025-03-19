from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from transformation_scripts import extract_books, transform_books, load_books

default_args = {
    'owner': 'Lauren',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    'book_library_etl',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    extract_task = PythonOperator(
        task_id='extract_books',
        python_callable=extract_books.run,
    )

    transform_task = PythonOperator(
        task_id='transform_books',
        python_callable=transform_books.run,
    )

    load_task = PythonOperator(
        task_id='load_books',
        python_callable=load_books.run,
    )

    extract_task >> transform_task >> load_task
