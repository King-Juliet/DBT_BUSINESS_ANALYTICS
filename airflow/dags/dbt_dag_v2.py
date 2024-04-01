# # IMPORTS
# from airflow import DAG
# from airflow.operators.bash_operator import BashOperator
# from datetime import datetime, timedelta
# from airflow.operators.email_operator import EmailOperator
# from airflow.utils.edgemodifier import Label
# from airflow.operators.python_operator import PythonOperator
# from packages.functions import transfer_to_s3

# import os

# # set environment variableS
# os.environ["AWS_SHARED_CREDENTIALS_FILE"] = "/opt/airflow/aws_cli_access/Juliet_CLI_accessKeys.csv"


# #Set up defaults arguments
# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2024, 3, 17),
#     'schedule_interval': 'None',
#     'email_on_failure': True,
#     'email_on_success': True,
#     'retries': 1,
#     'retry_delay': timedelta(seconds = 1)

# }

# #dag 
# dbt_dag = DAG(
#     'dbt_tasks_dag',
#     default_args = default_args,
#     description = 'This DAG runs dbt commands',
#     schedule_interval = None
# )

# #Define task to navigate to dbt directory and build the dbt models
# run_dbt_build = BashOperator(
#     task_id = 'run_dbt',
#     bash_command = 'cd /opt/airflow/dbt && dbt run --profiles-dir . && dbt snapshot --profiles-dir . && dbt docs generate ',
#     dag = dbt_dag
# )

# s3_bucket = "business-dbt-docs-site"  

# # using boto3 method to upload file
# transfer_catalog_to_boto3_task = PythonOperator(
#     task_id = 'catalog_to_s3',
#     python_callable = transfer_to_s3,
#     op_kwargs = {
#                 'file_path':  '/opt/airflow/dbt/target/catalog.json', 
#                 'bucket_name': s3_bucket, 
#                 'object_name': 'dbt-catalog.json', 
#                 'extra_args': {'ContentType': 'application/json'}
#                 },
#                 dag = dbt_dag
#                 )

# transfer_index_to_boto3_task = PythonOperator(
#     task_id = 'index_to_s3',
#     python_callable = transfer_to_s3,
#     op_kwargs = {
#                 'file_path':  '/opt/airflow/dbt/target/index.html', 
#                 'bucket_name': s3_bucket, 
#                 'object_name': 'dbt-index.html', 
#                 'extra_args': {'ContentType': 'text/html'}
#                 },
#                 dag = dbt_dag
#                 )

# transfer_manifest_to_boto3_task = PythonOperator(
#     task_id = 'manifest_to_s3',
#     python_callable = transfer_to_s3,
#     op_kwargs = {
#                 'file_path':  '/opt/airflow/dbt/target/manifest.json', 
#                 'bucket_name': s3_bucket, 
#                 'object_name': 'dbt-manifest.json', 
#                 'extra_args': {'ContentType': 'application/json'}
#                 },
#                 dag = dbt_dag
#                 )

# transfer_run_results_to_boto3_task = PythonOperator(
#     task_id = 'run_results_to_s3',
#     python_callable = transfer_to_s3,
#     op_kwargs = {
#                 'file_path':  '/opt/airflow/dbt/target/run_results.json', 
#                 'bucket_name': s3_bucket, 
#                 'object_name': 'dbt-run-results.json', 
#                 'extra_args': {'ContentType': 'application/json'}
#                 },
#                 dag = dbt_dag
#                 )

