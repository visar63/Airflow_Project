from airflow.sdk import dag, task
# from pendulum import datetime
import logging
    
logging.basicConfig(level=logging.INFO)

@dag
def xcom2_dag():
    
    @task
    def task_a():
        val = 70
        logging.info(f'**Hello from task A! I am returning {val}!')
        return val # This will automatically push the value to XCom with the key 'return_value'

    @task
    def task_b(val: int):
        logging.info(f'**Hello from task B! I am receiving {val}!')

    val = task_a()
    task_b(val)

    # task_a() >> task_b()


xcom2_dag()
# print('Done!')