from airflow import DAG
from pendulum import datetime
from airflow.providers.standard.sensors.python import PythonSensor

"""In the example below, the Sensor checks  _condition to be true every 60 seconds by default (poke_interval). Since _condition always returns False, the Sensor will continue checking every 60 seconds until it times out after 7 days (7 * 24 * 60 * 60 by default). When the Sensor times out, it is marked failed."""

def _condition():
    return False

with DAG(
    dag_id="sensor_dag",
    start_date=datetime(2021, 1, 1),
    schedule="@daily",
    catchup=False,
):
    waiting_for_condition = PythonSensor(
        task_id="waiting_for_condition",
        python_callable=_condition,
        poke_interval=60,
        timeout=7 * 24 * 60 * 60
    )