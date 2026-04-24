# from airflow.sdk import dag, task
# from airflow.providers.standard.operators.bash import BashOperator
# from datetime import datetime

# @dag(
#     schedule=None,
#     start_date=datetime(2022, 1, 1),
#     tags=['backfill-trigger-cli'],
#     catchup=False
# )

# def backfill_trigger_dag():
#     # Use the UI to trigger a DAG run with conf to trigger a backfill, passing in start/end dates and dag_id etc:
#     trigger_backfill = BashOperator(
#         task_id='trigger_backfill',
#         bash_command="""
#         /home/airflow/.local/bin/airflow backfill create \
#         --dag-id {{ dag_run.conf['dag_id'] }} \
#         --from-date {{ dag_run.conf['date_start'] }} \
#         --to-date {{ dag_run.conf['date_end'] }} \
#         --reprocess-behavior completed
#         """,
#         env={
#             "AIRFLOW_HOME": "/opt/airflow",
#             "AIRFLOW__DATABASE__SQL_ALCHEMY_CONN": "postgresql+psycopg2://airflow:airflow@postgres/airflow"
#         }
#     )

#     return trigger_backfill

# backfill_trigger_dag()



from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.sdk import dag
from datetime import datetime

@dag(schedule=None, start_date=datetime(2022,1,1), catchup=False)
def backfill_trigger_dag():
    trigger = TriggerDagRunOperator(
        task_id="trigger_cli_backfill",
        trigger_dag_id="cli",
        conf={
            "date_start": "2023-04-01",
            "date_end": "2023-04-05"
        },
        wait_for_completion=True
    )
    return trigger

backfill_trigger_dag()