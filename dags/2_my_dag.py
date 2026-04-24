from airflow.sdk import dag, task, chain
from pendulum import datetime
# from airflow.providers.standard.operators.python import PythonOperator

@dag(
    schedule="@daily",
    start_date=datetime(2026, 3, 30),
    description="This dag does...",
    tags=["team_a", "source_a"],
    max_consecutive_failed_dag_runs=3
)
def my_dag():
    
    @task
    def task_a():
        print('Hello from task A!')

    @task
    def task_b():
        print('Hello from task B!')


    @task
    def task_c():
        print('Hello from task C!')

    @task
    def task_d():
        print('Hello from task D!')

    @task
    def task_e():
        print('Hello from task E!')

    chain(task_a(), [task_b(), task_d()], [task_c(), task_e()])
    # a = task_a()
    # a >>  task_b() >> task_c()
    # a >>  task_d() >> task_e()

my_dag()
print('Done!')