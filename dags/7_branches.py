from airflow.sdk import dag, task
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=['branch_dags'],
    catchup=False,
)
def branch_dags():

    @task
    def extract_data():
        return {
            'api_data': [1, 2, 3],
            'db_data': [4, 5, 6],
            's3_data': [7, 8, 9],
            'weekend_flag': datetime.now().weekday() >= 5,
        }

    @task
    def transform_api_data(data):
        return [x * 10 for x in data['api_data']]

    @task
    def transform_db_data(data):
        return [x * 100 for x in data['db_data']]

    @task
    def transform_s3_data(data):
        return [x * 1000 for x in data['s3_data']]

    @task.branch(task_id="branching_task")
    def branching_task(data):
        return "no_load_data" if data['weekend_flag'] else "load_data"

    @task
    def load_data(**kwargs):
        ti = kwargs['ti']
        api = ti.xcom_pull(task_ids='transform_api_data')
        db = ti.xcom_pull(task_ids='transform_db_data')
        s3 = ti.xcom_pull(task_ids='transform_s3_data')
        print(f"Loading transformed data: API: {api}, DB: {db}, S3: {s3}")
        return "Data loaded successfully!"

    @task
    def no_load_data():
        print("No data to load today. Enjoy your weekend!")
        return "No data loaded."

    raw = extract_data()
    api = transform_api_data(raw)
    db = transform_db_data(raw)
    s3 = transform_s3_data(raw)

    branch = branching_task(raw)
    [api, db, s3] >> branch

    branch >> [load_data(), no_load_data()]

branch_dags()