from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta 
from packages.functions import src_to_data_platform
from airflow.operators.email_operator import EmailOperator
from airflow.utils.edgemodifier import Label
import os

#Default dag task

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 17),
    'schedule_interval' : 'None',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Instantiate the DAG

dag = DAG(
    'src_to_data_platform',
    default_args=default_args,
    description='Extract data from MS SQL server to Postgres Data platform',
    schedule_interval= None,
    catchup=False,
)

# Configue Email On Failure Task

#1. Define Email subject and body 
#email_subject = 'Airflow Alert - {{ dag.dag_id }} - {{ task.task_id }} - {{ ts }}'
#email_body = 'Task {{ task.task_id }} failed. Please investigate.'
#2. set up the Email operator
#email_on_failure_task = EmailOperator(
    #task_id = 'email_on_failure',
    #to = 'chibuokejuliet@gmail.com',  # Replace with your email address
    #subject = email_subject,
    #html_content = email_body,
    #dag = dag
#)

#Extract data from MS SQL Server to Postgres tasks

src_to_platform_customer_reviews_table_task = PythonOperator(
    task_id = 'src_to_platform_customer_reviews_table',
    python_callable = src_to_data_platform,
    op_kwargs = {
                'src_server':  'host.docker.internal', #'DESKTOP-O9JQMI9\\MSSQLSERVER01,51968', 
                'src_username': 'sa', 
                'src_password': 'Supremejulz3456~', 
                'src_database' : 'DiversifyShop',
                'src_schema': 'shop', 
                'src_table_name':'customer_reviews_table',
                'postgres_username': 'postgres',
                'postgres_password': 'chibuoke3456',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'shop',
                'destination_table_name': 'customer_reviews_table'
                },
    dag = dag
)

src_to_platform_customers_table_task = PythonOperator(
    task_id = 'src_to_platform_customers_table',
    python_callable = src_to_data_platform,
    op_kwargs = {
                'src_server': 'host.docker.internal', #'DESKTOP-O9JQMI9\\MSSQLSERVER01,51968', 
                'src_username': 'sa', 
                'src_password': 'Supremejulz3456~', 
                'src_database' : 'DiversifyShop',
                'src_schema': 'shop', 
                'src_table_name':'customers_table',
                'postgres_username': 'postgres',
                'postgres_password': 'chibuoke3456',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'shop',
                'destination_table_name': 'customers_table'
                },
    dag = dag
)

src_to_platform_orders_table_task = PythonOperator(
    task_id = 'src_to_platform_orders_table',
    python_callable = src_to_data_platform,
    op_kwargs = {
                'src_server': 'host.docker.internal',#'DESKTOP-O9JQMI9\\MSSQLSERVER01,51968', 
                'src_username': 'sa', 
                'src_password': 'Supremejulz3456~', 
                'src_database' : 'DiversifyShop', 
                'src_schema': 'shop',
                'src_table_name':'orders_table',
                'postgres_username': 'postgres',
                'postgres_password': 'chibuoke3456',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'shop',
                'destination_table_name': 'orders_table'
                },
    dag = dag
)


src_to_platform_products_table_task = PythonOperator(
    task_id = 'src_to_platform_products_table',
    python_callable = src_to_data_platform,
    op_kwargs = {
                'src_server': 'host.docker.internal', #'DESKTOP-O9JQMI9\\MSSQLSERVER01,51968', 
                'src_username': 'sa', 
                'src_password': 'Supremejulz3456~', 
                'src_database' : 'DiversifyShop', 
                'src_schema': 'shop',
                'src_table_name':'products_table',
                'postgres_username': 'postgres',
                'postgres_password': 'chibuoke3456',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'shop',
                'destination_table_name': 'products_table'
                },
    dag = dag
)

src_to_platform_card_details_table_task = PythonOperator(
    task_id = 'src_to_platform_card_details_table',
    python_callable = src_to_data_platform,
    op_kwargs = {
                'src_server': 'host.docker.internal', #'DESKTOP-O9JQMI9\\MSSQLSERVER01,51968', 
                'src_username': 'sa', 
                'src_password': 'Supremejulz3456~', 
                'src_database' : 'DiversifyShop',
                'src_schema': 'payments', 
                'src_table_name':'card_details_table',
                'postgres_username': 'postgres',
                'postgres_password': 'chibuoke3456',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'payments',
                'destination_table_name': 'card_details_table'
                },
    dag = dag
)

src_to_platform_payments_table_task = PythonOperator(
    task_id = 'src_to_platform_payments_table',
    python_callable = src_to_data_platform,
    op_kwargs = {
                'src_server': 'host.docker.internal', #DESKTOP-O9JQMI9\\MSSQLSERVER01,51968 
                'src_username': 'sa', 
                'src_password': 'Supremejulz3456~', 
                'src_database' : 'DiversifyShop',
                'src_schema': 'payments', 
                'src_table_name':'payments_table',
                'postgres_username': 'postgres',
                'postgres_password': 'chibuoke3456',
                'postgres_host': 'host.docker.internal',
                'postgres_port': '5432',
                'postgres_database': 'diversifyshop',
                'dest_schema': 'payments',
                'destination_table_name': 'payments_table'
                },
    dag = dag
)




#email_on_failure_task >> 
Label("Load dataset from SQL Server to Postgres Data platform") >> [src_to_platform_customer_reviews_table_task, src_to_platform_customers_table_task, src_to_platform_orders_table_task, src_to_platform_products_table_task, src_to_platform_card_details_table_task, src_to_platform_payments_table_task]
