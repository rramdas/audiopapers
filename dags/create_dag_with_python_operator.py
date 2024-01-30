from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 1, 1)
}


def greet():
    print("Helo world!")


with DAG(
        default_args=default_args,
        dag_id='create_dag_with_python_operator',
        description='A simple tutorial DAG',
        start_date=datetime(2020, 1, 1),
) as dag:
    task1 = PythonOperator(
        task_id='task1',
        python_callable=greet
    )

task1
