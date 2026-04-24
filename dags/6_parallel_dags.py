from airflow.sdk import dag, task
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=['parallel_dags'],
    catchup=False,
)
def parallel_dags():

    @task
    def extract_data():
        return {
            'api_data': [1, 2, 3],
            'db_data': [4, 5, 6],
            's3_data': [7, 8, 9],
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

    @task
    def load_data(api, db, s3):
        print(f"Loading transformed data: API: {api}, DB: {db}, S3: {s3}")
        return "Data loaded successfully!"

    raw = extract_data()
    api = transform_api_data(raw)
    db = transform_db_data(raw)
    s3 = transform_s3_data(raw)
    load_data(api, db, s3)

parallel_dags()