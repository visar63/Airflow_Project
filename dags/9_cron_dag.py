from datetime import timedelta

from airflow.sdk import dag, task
# from airflow.providers.standard.sensors.filesystem import FileSensor
from pendulum import datetime, duration
from airflow.timetables.trigger import CronTriggerTimetable, DeltaTriggerTimetable

@dag(
    # schedule = CronTriggerTimetable("0 16 * * Mon-Fri", timezone="UTC"),  # Daily at 4 PM on weekdays
    schedule = DeltaTriggerTimetable(duration(days=3)),  # Every 3 days
    start_date = datetime(2026, 4, 11),
    end_date=datetime(2026, 4, 17),
    tags = ['cron'],
    catchup = False
)
def cron_dag():

    @task
    def runme():
        print("Hi")

    runme()

cron_dag()