# IMPORTS
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.email import send_email
from datetime import datetime, timedelta
from packages.functions import transfer_to_s3

#Set s3_bucket variable
s3_bucket = "business-dbt-docs-site"

#define function that uploads dbt artifacts for the dbt project docs site
def upload_dbt_artifacts():
    dbt_docs_files = ['catalog.json', 'manifest.json', 'run-results.json','index.html']
    #for file in os.listdir('/opt/airflow/dbt/target/'):
    for file in dbt_docs_files:
        content_type = {'ContentType': 'application/json'} if file.endswith('json') else {'ContentType': 'text/html'}
        transfer_to_s3('/opt/airflow/dbt/target/', s3_bucket, file, content_type)   

#Email configurations
def success_email(context):
    task_instance = context['task_instance']
    task_status = 'Success'#task_instance.current_state()
    subject = f'Airflow Task {task_instance.task_id} {task_status}'
    body = f'The task {task_instance.task_id} completed with status : {task_status}. \n\n'\
        f'The task execution date is: {context['execution_date']}\n'\
        f'Log url: {task_instance.log_url}\n\n'
    to_email = 'xxxxx@gmail.com' #recepient mail
    send_email(to = to_email, subject = subject, html_content = body)

def failure_email(context):
    task_instance = context['task_instance']
    task_status = 'Failed'#task_instance.current_state()
    subject = f'Airflow Task {task_instance.task_id} {task_status}'
    body = f'The task {task_instance.task_id} completed with status : {task_status}. \n\n'\
        f'The task execution date is: {context['execution_date']}\n'\
        f'Log url: {task_instance.log_url}\n\n'
    to_email = 'xxxxxx@gmail.com' #recepient mail
    send_email(to = to_email, subject = subject, html_content = body)

#Set up defaults arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 17),
    'schedule_interval': 'None',
    'email_on_failure': True,
    'email_on_success': True,
    'retries': 1,
    'retry_delay': timedelta(seconds = 1)
}

#dag 
dbt_dag = DAG(
    'dbt_tasks_dag',
    default_args = default_args,
    description = 'This DAG runs dbt commands',
    schedule_interval = None
)

#Define task to navigate to dbt directory and build the dbt models
run_dbt_build = BashOperator(
    task_id = 'run_dbt',
    bash_command = 'cd /opt/airflow/dbt && dbt run --profiles-dir . && dbt snapshot --profiles-dir . && dbt docs generate ',
    on_success_callback=lambda context: success_email(context),
    on_failure_callback=lambda context: failure_email(context),
    dag = dbt_dag
)

#Define task to upload dbt docs site artifacts to s3 bucket
upload_dbt_docs_task = PythonOperator(
    task_id = 'upload_dbt_docs',
    python_callable = upload_dbt_artifacts,
    on_success_callback=lambda context: success_email(context),
    on_failure_callback=lambda context: failure_email(context),
    provide_context = True,
    dag = dbt_dag
                )

#Set task dependencies
run_dbt_build >> upload_dbt_docs_task 