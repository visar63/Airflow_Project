from airflow.sdk import dag, task
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from pendulum import datetime

@dag(
    # dag_id="sensor2_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    tags=["aws", "s3", "sensor"],
)

def sensor2_dag():
    wait_for_file = S3KeySensor(
        task_id="wait_for_file",
        aws_conn_id="aws_s3",
        # bucket_name="visar-airflow--eun1-az1--x-s3",
        bucket_key="s3://visar-airflow2/data_*",
        wildcard_match=True,
    )

    @task
    def process_file():
        print("File is processed!")

    wait_for_file >> process_file()

sensor2_dag()