from airflow.sdk import task, dag
from pendulum import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=['orchestrator_dags'],
    catchup=False,
)

def orchestrator_1_dag():
    @task
    def task_a():
        print("Running Task A")
        return "Data from Task A"

    @task
    def task_b(data_from_a):
        print(f"Running Task B with input: {data_from_a}")
        return f"Processed {data_from_a} in Task B"

    @task
    def task_c(data_from_b):
        print(f"Running Task C with input: {data_from_b}")
        return f"Final result: {data_from_b}"

    a = task_a()
    b = task_b(a)
    c = task_c(b)

orchestrator_1_dag()