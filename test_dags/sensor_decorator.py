from airflow.sdk import dag, task
from datetime import datetime
import requests

from airflow.providers.standard.sensors.python import PokeReturnValue


@dag(
    schedule="@daily",
    start_date=datetime(2023, 1, 1),
    tags=['sensor_decorator'],
    catchup=False
)
def sensor_decorator():
    @task.sensor(poke_interval=30, timeout=3600, mode="poke")
    def check_shibe_availability():
        response = requests.get("https://publicapis.io/_next/data/build/alternatives/shibe-online-api.json?slug=shibe-online-api")
        print(response.status_code)

        if response.status_code == 200:
            condition_met = True
            operator_return_value = response.json()
        else:
            condition_met = False
            operator_return_value = None
            print(f"Shibe Online API is not available yet...: {response.status_code}")

        return PokeReturnValue(is_done=condition_met, xcom_value=operator_return_value)
    
    def print_shiba_json(json_content):
        print(f"The shiba json is: {json_content}")


    print_shiba_json(check_shibe_availability())

sensor_decorator()