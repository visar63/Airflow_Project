from airflow.sdk import task, dag
from pendulum import datetime
from dag_1_orchestrator import orchestrator_1_dag
from dag_2_orchestrator import orchestrator_2_dag
# from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator


@dag(
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=['orchestrator_dags'],
    catchup=False,
    dag_id="parent_orchestrator_dag"
)
def parent_orchestrator_dag():
    trigger_dag_1 = TriggerDagRunOperator(
        task_id = "trigger_orchestrator_1",
        trigger_dag_id = "orchestrator_1_dag",
        wait_for_completion=True
    )

    trigger_dag_2 = TriggerDagRunOperator(
        task_id = "trigger_orchestrator_2",
        trigger_dag_id = "orchestrator_2_dag",
        wait_for_completion=True
    )

    trigger_dag_1 >> trigger_dag_2

parent_orchestrator_dag()