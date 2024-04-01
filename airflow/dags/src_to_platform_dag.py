from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.email import send_email
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime, timedelta 
from packages.functions import postgres_src_to_data_platform

#Email configuration

def success_email(context):
    task_instance = context['task_instance']
    task_status = 'Success' #task_instance.current_state()
    subject = f'Airflow Task {task_instance.task_id} {task_status}'
    body = f'The task {task_instance.task_id} completed with status : {task_status}. \n\n'\
        f'The task execution date is: {context["execution_date"]}\n'\
        f'Log url: {task_instance.log_url}\n\n'
    to_email = 'xxxx@gmail.com' #recepient mail
    send_email(to = to_email, subject = subject, html_content = body)

def failure_email(context):
    task_instance = context['task_instance']
    task_status = 'Failed' #task_instance.current_state()
    subject = f'Airflow Task {task_instance.task_id} {task_status}'
    body = f'The task {task_instance.task_id} completed with status : {task_status}. \n\n'\
        f'The task execution date is: {context["execution_date"]}\n'\
        f'Log url: {task_instance.log_url}\n\n'
    to_email = 'xxxxxxx@gmail.com' #recepient mail
    send_email(to = to_email, subject = subject, html_content = body)

#Default dag task

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 17),
    'schedule_interval' : 'None',
    'email_on_failure': True,
    'email_on_success': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

# Instantiate the DAG
dag = DAG(
    'src_to_data_platform',
    default_args = default_args,
    description = 'Extract data from transactional Postgres database to Postgres Data platform',
    schedule_interval = None,
    catchup = False,
)

#Extract data from OLTP database to Analytics dataplatform

src_to_platform_customer_reviews_table_task = PythonOperator(
    task_id = 'src_to_platform_customer_reviews_table',
    python_callable = postgres_src_to_data_platform,
    op_kwargs = {
                'src_server':  'host.docker.internal',  
                'src_username': 'postgres', 
                'src_password': '###', 
                'src_database' : 'srcdiversifyshop',
                'src_schema': 'shop', 
                'src_table_name':'customer_reviews_table',
                'postgres_username': 'postgres',
                'postgres_password': '###',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'shop',
                'destination_table_name': 'customer_reviews_table'
                },
    on_success_callback=lambda context: success_email(context),
    on_failure_callback=lambda context: failure_email(context),
    provide_context = True,
    dag = dag
)

src_to_platform_customers_table_task = PythonOperator(
    task_id = 'src_to_platform_customers_table',
    python_callable = postgres_src_to_data_platform,
    op_kwargs = {
                'src_server': 'host.docker.internal',  
                'src_username': 'postgres', 
                'src_password': '###', 
                'src_database' : 'srcdiversifyshop',
                'src_schema': 'shop', 
                'src_table_name':'customers_table',
                'postgres_username': 'postgres',
                'postgres_password': '###',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'shop',
                'destination_table_name': 'customers_table'
                },
    on_success_callback=lambda context: success_email(context),
    on_failure_callback=lambda context: failure_email(context),
    provide_context = True,
    dag = dag
)

src_to_platform_orders_table_task = PythonOperator(
    task_id = 'src_to_platform_orders_table',
    python_callable = postgres_src_to_data_platform,
    op_kwargs = {
                'src_server': 'host.docker.internal', 
                'src_username': 'postgres', 
                'src_password': '###', 
                'src_database' : 'srcdiversifyshop', 
                'src_schema': 'shop',
                'src_table_name':'orders_table',
                'postgres_username': 'postgres',
                'postgres_password': '###',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'shop',
                'destination_table_name': 'orders_table'
                },
    on_success_callback=lambda context: success_email(context),
    on_failure_callback=lambda context: failure_email(context),
    provide_context = True,
    dag = dag
)


src_to_platform_products_table_task = PythonOperator(
    task_id = 'src_to_platform_products_table',
    python_callable = postgres_src_to_data_platform,
    op_kwargs = {
                'src_server': 'host.docker.internal',  
                'src_username': 'postgres', 
                'src_password': '###', 
                'src_database' : 'srcdiversifyshop', 
                'src_schema': 'shop',
                'src_table_name':'products_table',
                'postgres_username': 'postgres',
                'postgres_password': '###',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'shop',
                'destination_table_name': 'products_table'
                },
    on_success_callback=lambda context: success_email(context),
    on_failure_callback=lambda context: failure_email(context),
    provide_context = True,
    dag = dag
)

src_to_platform_card_details_table_task = PythonOperator(
    task_id = 'src_to_platform_card_details_table',
    python_callable = postgres_src_to_data_platform,
    op_kwargs = {
                'src_server': 'host.docker.internal',  
                'src_username': 'postgres', 
                'src_password': '###', 
                'src_database' : 'srcdiversifyshop',
                'src_schema': 'payments', 
                'src_table_name':'card_details_table',
                'postgres_username': 'postgres',
                'postgres_password': '###',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'payments',
                'destination_table_name': 'card_details_table'
                },
    on_success_callback=lambda context: success_email(context),
    on_failure_callback=lambda context: failure_email(context),
    provide_context = True,
    dag = dag
)

src_to_platform_payments_table_task = PythonOperator(
    task_id = 'src_to_platform_payments_table',
    python_callable = postgres_src_to_data_platform,
    op_kwargs = {
                'src_server': 'host.docker.internal',  
                'src_username': 'postgres', 
                'src_password': '###', 
                'src_database' : 'srcdiversifyshop',
                'src_schema': 'payments', 
                'src_table_name':'payments_table',
                'postgres_username': 'postgres',
                'postgres_password': '###',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'payments',
                'destination_table_name': 'payments_table'
                },
    on_success_callback=lambda context: success_email(context),
    on_failure_callback=lambda context: failure_email(context),
    provide_context = True,
    dag = dag
)

# Define trigger task to trigger the dbt_dag.py 
trigger_dbt_dag_task = TriggerDagRunOperator(
    task_id ='trigger_dbt_dag',
    trigger_dag_id = 'dbt_tasks_dag', # Dag id of the dag to trigger -- dbt_dag.py
    dag = dag,
    wait_for_completion = True
)


src_to_platform_customer_reviews_table_task >> src_to_platform_customers_table_task >> src_to_platform_orders_table_task >> src_to_platform_products_table_task >> src_to_platform_card_details_table_task >> src_to_platform_payments_table_task >> trigger_dbt_dag_task
