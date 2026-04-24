from airflow.sdk import dag, task
from pendulum import datetime   

@dag(
    schedule="@daily",
    start_date=datetime(2026, 4, 1),
)

def test_dag():

    @task
    def task_a():
        print('Hello from task A!')

    @task
    def task_b():
        print('Hello from task B!')

    task_a() >> task_b()

test_dag()
print('Done!')