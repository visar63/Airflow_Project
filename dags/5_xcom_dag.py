from airflow.sdk import dag, task, Context
from pendulum import datetime

@dag
def xcom_dag():
    
    @task
    def task_a(**context: Context):
        val = 69
        print(f'**Hello from task A! I am returning {val}!')
        context['ti'].xcom_push(key='my_key', value=val)

    @task
    def task_b(**context: Context):
        val = context['ti'].xcom_pull(task_ids='task_a', key='my_key')
        print(f'**Hello from task B! I am receiving {val}!')

    task_a() >> task_b()


xcom_dag()
# print('Done!')