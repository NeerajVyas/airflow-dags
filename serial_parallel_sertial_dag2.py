
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator


from datetime import datetime

default_args = {
	'start_date': datetime(2019, 1, 1),
	'owner': 'Airflow',
}


#to run in parallel use localExecutor and check parallelism value in airflow.cfg
with DAG('serial_parallel_serial_dag2', default_args=default_args, description='serial - parallel - serial', schedule_interval='@once', catchup=False) as dag:
	start_dummy_task1 = DummyOperator(task_id='sdt1')
	serial1_task = BashOperator(task_id='s1', bash_command='echo "neo"')
	serial2_task = BashOperator(task_id='s2', bash_command='sleep 2')
	execute_parallel0_task 	= BashOperator(task_id='ep', bash_command='sleep 3')
	parallel1_task 	= BashOperator(task_id='p1', bash_command='sleep 3')
	parallel2_task 	= BashOperator(task_id='p2', bash_command='echo {{ ti.xcom_push("KEY01","VALUE01") }} echo {{ ti.xcom_push("KEY02","VALUE02") }} echo {{ ti.xcom_push("KEY03","VALUE03") }}')
	parallel3_task 	= BashOperator(task_id='p3', bash_command='sleep 3')
	parallel4_task 	= BashOperator(task_id='p4', bash_command='echo {{ ti.xcom_push("KEY04","VALUE04") }} ')
	execute_serial0_task = BashOperator(task_id='es', bash_command='sleep 3')
	serial3_task = BashOperator(task_id='s3', bash_command='echo "{{ ti.xcom_pull(KEY01) }}" ')
	serial4_task = BashOperator(task_id='s4', bash_command='echo "{{ ti.xcom_pull(KEY04) }}" echo "{{ ti.xcom_pull(KEY03) }}" echo "{{ ti.xcom_pull(KEY02) }}" ')
	start_dummy_task1 >> serial1_task >> serial2_task >> execute_parallel0_task

	execute_parallel0_task >> [ parallel1_task , parallel2_task , parallel3_task, parallel4_task ] >> execute_serial0_task >> serial3_task >> serial4_task
