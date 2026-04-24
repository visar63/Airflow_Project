from airflow.sdk import dag, task, Context
from pendulum import datetime
import logging

logging.basicConfig(level=logging.INFO)

@dag
def xcom3_dag():
    
    @task
    def task_a(ti):
        val = 69
        logging.info(f'**Hello from task A! I am returning {val}!')
        ti.xcom_push(key='my_key', value=val)

    @task
    def task_b(ti):
        val =ti.xcom_pull(task_ids='task_a', key='my_key')
        logging.info(f'**Hello from task B! I am receiving {val}!')

    task_a() >> task_b()


xcom3_dag()
# print('Done!')