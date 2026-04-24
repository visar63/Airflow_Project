from airflow.sdk import task, dag, Variable
from pendulum import datetime

@dag(start_date=datetime(2023, 1, 1), schedule=None, catchup=False)
def variable_dag():

    @task
    def print_variable():
        my_var = Variable.get("api", deserialize_json=True)
        print(f"The value of my_variable is: {my_var}")

    print_variable()

variable_dag()
