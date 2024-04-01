#IMPORTS
import pyodbc
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import boto3



#TRANSFER DATA FROM MS SQL SERVER TO POSTGRES

#def src_to_data_platform(src_server, src_username, src_password, src_database, src_table_name, 
 #                    postgres_username, postgres_password, postgres_host, postgres_port, 
  #                   postgres_database, destination_table_name):
   # """
    #This function extracts data from MS SQL Server data source and loads data to a PostgreSQL datawarehouse.
    
    #Args:
     #   src_server: MS SQL  server connection
      #  src_username: Username for MS SQL server
       # src_password: Login password to MS SQL
        #src_database: MS SQL server source database of interest 
        #src_table_name: Source table of interest in MS SQL Server 
        #postgres_username: Username for Postgres datawarehouse
        #postgres_password: Login password to Postgres
        #postgres_host: Host for Postgres datawarehouse
        #postgres_port: Port that Postgres is on
        #postgres_database: Postgres source database of interest
        #destination_table_name: Destination table of interest in Postgres

    #"""

    # Initialize connection to SQL Server
    #cnxn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={src_server};DATABASE={src_database};Encrypt=no;UID={src_username};PWD={src_password}')
    
    # Use parameterized query to avoid SQL injection
    #query = f"SELECT * FROM {src_table_name}"
    #data = pd.read_sql(query, cnxn)

    # Create a SQLAlchemy engine to connect to the PostgreSQL database
    #engine = create_engine(f'postgresql+psycopg2://{postgres_username}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}')

    # Use the to_sql method to insert the data into the PostgreSQL table
    #data.to_sql(destination_table_name, engine, if_exists='replace', index=False)

    # Close the connections
    #cnxn.close()
    #engine.dispose()

# Example Usage:
#src_to_data_platform('DESKTOP-O9JQMI9\MSSQLSERVER01,51781', 'src_database', 'sa', 'Supremejulz3456~',
                # 'src_table_name', 'your_postgres_username', 'your_postgres_password', 'host.docker.internal', '5432',
                 #'your_postgres_database', 'your_destination_table_name')




def src_to_data_platform(src_server, src_username, src_password, src_database, src_schema, src_table_name, 
                     postgres_username, postgres_password, postgres_host, postgres_port, 
                     postgres_database, dest_schema, destination_table_name):
    """
    This function extracts data from MS SQL Server data source and loads data to a PostgreSQL datawarehouse.
    
    Args:
        src_server: MS SQL  server connection
        src_username: Username for MS SQL server
        src_password: Login password to MS SQL
        src_database: MS SQL server source database of interest
        scr_schema: schema of source database 
        src_table_name: Source table of interest in MS SQL Server 
        postgres_username: Username for Postgres datawarehouse
        postgres_password: Login password to Postgres
        postgres_host: Host for Postgres datawarehouse
        postgres_port: Port that Postgres is on
        postgres_database: Postgres source database of interest
        dest_schema: Destination schema
        destination_table_name: Destination table of interest in Postgres

    """
    cnxn = None
    engine = None
    
    try:
        # Initialize connection to SQL Server
        cnxn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={src_server};DATABASE={src_database};Encrypt=no;UID={src_username};PWD={src_password}')
    
        # Use parameterized query to avoid SQL injection
        query = f"SELECT * FROM {src_schema}.{src_table_name}"
        data = pd.read_sql(query, cnxn)

        # Create a SQLAlchemy engine to connect to the PostgreSQL database
        engine = create_engine(f'postgresql+psycopg2://{postgres_username}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}')

        # Use the to_sql method to insert the data into the PostgreSQL table
        data.to_sql(name= destination_table_name, con = engine, schema = dest_schema, if_exists='replace', index=False)
        print(f'Data successfully loaded to {destination_table_name} in {postgres_database}!')
        # Close the connections
        #cnxn.close()
        #engine.dispose()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cnxn:
            cnxn.close()
        if engine:
            engine.dispose()
        
# Example Usage:
#src_to_data_platform('DESKTOP-O9JQMI9\MSSQLSERVER01,51781', 'src_database', 'sa', 'Supremejulz3456~',
                # 'src_table_name', 'your_postgres_username', 'your_postgres_password', 'host.docker.internal', '5432',
                 #'your_postgres_database', 'your_destination_table_name')



def postgres_src_to_data_platform(src_server, src_username, src_password, src_database, src_schema, src_table_name, 
                         postgres_username, postgres_password, postgres_host, postgres_port, 
                         postgres_database, dest_schema, destination_table_name):
    """
    This function extracts data from one PostgreSQL database and loads it into another PostgreSQL database.
    
    Args:
        src_server: Source PostgreSQL server connection
        src_username: Username for source PostgreSQL server
        src_password: Login password to source PostgreSQL
        src_database: Source PostgreSQL server database of interest
        src_schema: Schema of source PostgreSQL database 
        src_table_name: Source table of interest in source PostgreSQL Server 
        postgres_username: Username for destination PostgreSQL database
        postgres_password: Login password to destination PostgreSQL
        postgres_host: Host for destination PostgreSQL database
        postgres_port: Port that destination PostgreSQL is on
        postgres_database: Destination PostgreSQL database of interest
        dest_schema: Destination schema
        destination_table_name: Destination table of interest in destination PostgreSQL

    """
    src_cnxn = None
    dest_engine = None
    
    try:
        # Initialize connection to source PostgreSQL database
        src_cnxn = psycopg2.connect(host=src_server, database=src_database, user=src_username, password=src_password)

        # Use parameterized query to avoid SQL injection
        query = f"SELECT * FROM {src_schema}.{src_table_name}"
        data = pd.read_sql(query, src_cnxn)

        # Create a SQLAlchemy engine to connect to the destination PostgreSQL database
        dest_engine = create_engine(f'postgresql+psycopg2://{postgres_username}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}')

        # Use the to_sql method to insert the data into the destination PostgreSQL table
        data.to_sql(name=destination_table_name, con=dest_engine, schema=dest_schema, if_exists='replace', index=False)
        print(f'Data successfully loaded to {destination_table_name} in {postgres_database}!')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if src_cnxn:
            src_cnxn.close()
        if dest_engine:
            dest_engine.dispose()



#FUNCTION TO MOVE FILES TO S3 BUCKET
def transfer_to_s3(file_path, bucket_name, object_name, extra_args):
    print(extra_args)
    #s3 client initialization
    s3_client = boto3.client("s3")
    try:
        #transfer files
        print(f'Now uploading {object_name}...')
        s3_client.upload_file(file_path, bucket_name, object_name, ExtraArgs = extra_args)
        print(f"file uplaoded successfully to s3://{bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error {e}")

