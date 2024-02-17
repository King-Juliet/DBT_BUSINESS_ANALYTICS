# IMPORTS
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.email_operator import EmailOperator
from airflow.utils.edgemodifier import Label

#Set up defaults arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 17),
    'schedule_interval': 'None',
    'email_on_failure': True,
    'retries': 1,
    'retry_delay': timedelta(minutes = 1)

}

#dag 
dbt_dag = DAG(
    'dbt_tasks_dag',
    default_args = default_args,
    description = 'This DAG runs dbt commands',
    schedule_interval = None
)

# Configue Email On Failure Task

#1. Define Email subject and body 
email_subject = 'Airflow Alert - {{ dag.dag_id }} - {{ task.task_id }} - {{ ts }}'
email_body = 'Task {{ task.task_id }} failed. Please investigate.'
#2. set up the Email operator
email_on_failure_task = EmailOperator(
    task_id = 'email_on_failure',
    to = 'chibuokejuliet@gmail.com',  # Replace with your email address
    subject = email_subject,
    html_content = email_body,
    dag = dbt_dag,
)

#Define task to navigate to dbt directory and build the dbt models
run_dbt_build = BashOperator(
    task_id = 'run_dbt',
    bash_command = 'cd /opt/airflow/dbt && dbt build --profiles-dir . && dbt snapshot --profiles-dir . && dbt docs generate && dbt docs serve',
    dag = dbt_dag
)

#assuming you have an s3 bucket for storing documentation
s3_sync_command = 'aws s3 sync /opt/airflow/dbt/target/paths/to/generated/docs/ s3://your-s3-bucket/dbt_docs/',

#task to upload documentation to s3
upload_dbt_docs_to_s3 = BashOperator(
    task_id = 'upload_dbt_docs_to_s3',
    bash_command = s3_sync_command,
    dag = dbt_dag
)


#task to store test results in the data platform 
#save_dbt_test_results = BashOperator(
        #task_id = 'save_dbt_test',
        #bash_command =  ,
        #dag = dbt_dag
#)

email_on_failure_task >> Label("Run dbt workflow") >> run_dbt_build #  >> [run_dbt_build, upload_dbt_docs_to_s3] #, save_dbt_test_results]