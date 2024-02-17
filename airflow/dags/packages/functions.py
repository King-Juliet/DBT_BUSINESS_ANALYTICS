#IMPORTS
import pyodbc
import pandas as pd
from sqlalchemy import create_engine



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
