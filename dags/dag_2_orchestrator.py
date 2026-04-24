import os
from airflow.sdk import task, dag
from pendulum import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=['orchestrator_dags'],
    catchup=False,
)

def orchestrator_2_dag():
    @task
    def task_a():
        print("Running Task A")

    @task.python
    def task_b():
    # Ensure the directory exists
        os.makedirs(os.path.dirname("/opt/airflow/logs/data"), exist_ok=True)

        # Simulate data processing by writing to a file
        with open("/opt/airflow/logs/data/output_X.txt", 'w') as f:
            f.write(f"Data processed successfully")


    task_a() >> task_b()

orchestrator_2_dag()