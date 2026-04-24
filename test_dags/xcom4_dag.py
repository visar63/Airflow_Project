from airflow.sdk import dag, task, Context
from pendulum import datetime
import logging

logging.basicConfig(level=logging.INFO)

@dag
def xcom4_dag():
    
    @task
    def task_a():
        val = {'val_1': 12, 'val_2': 34}
        logging.info(f'**Hello from task A! I am returning {val}!')
        return val # This will automatically push the value to XCom with the key 'return_value'

    @task
    def task_b(val):
        logging.info(f'**Hello from task B! I am receiving {val}!')

    task_b(task_a())


xcom4_dag()
# print('Done!')