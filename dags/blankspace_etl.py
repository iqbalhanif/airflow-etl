from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1, 
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id = 'blankspace_etl',
    start_date = datetime(2020,9,11),
    schedule_interval = '0 0 * * *',
    default_args=default_args
)

# Extract from MySQL example

mysql_extract = MySqlOperator(
    dag=dag, 
    mysql_conn_id='airflow_mysql',
    task_id='mysql_extract',
    sql=r"""use hr; select * from countries limit 10;"""
	)

# Extract from PostgreSQL example

psql_extract = PostgresOperator(
    dag=dag,
	postgres_conn_id='airflow_psql',
	task_id='psql_extract',
    sql='''select * from postgres.public."Album" limit 10;'''
    )

# Extract with bash	example 

bash_extract = BashOperator(
    task_id='airflow_bash',
    bash_command='mysql -h 127.0.0.1 -P 3306 -u root -pabcd1234 -N -e "use hr; select * from countries limit 10;"',
    dag=dag,
)
	
# Extract with python example

def callable_python():
    from sqlalchemy import create_engine
    import pandas as pd
    import pymysql

    ## create postgresql_engine & mysql_engine
    engine1 = create_engine('postgresql://postgres:abcd1234@127.0.0.1:5432/postgres')
    engine2 = create_engine('mysql+pymysql://root:abcd1234@127.0.0.1:3306/hr')

    def etl_function(table_name):
        ##extract_table
        sql_query1 = 'select * from postgres.public."%s";'%(table_name)
        df=pd.read_sql_query(sql_query1,con=engine1)

        ##load_table
        new_table = str.lower(table_name) + '2'
        df.to_sql(new_table, con=engine2, if_exists="replace", index=False)

    table_name = [
    'Album'
    ,'Artist'
    ,'Customer'
    ,'Employee'
    ,'Genre'
    ,'Invoice'
    ,'InvoiceLine'
    ,'MediaType'
    ,'Playlist'
    ,'PlaylistTrack'
    ,'Track']
        
    for i in table_name:
        etl_function(i)
        

python_task = PythonOperator(
    dag=dag,
    task_id='python_task',
    python_callable=callable_python,
)
	
#DAG order

mysql_extract >> psql_extract >> bash_extract >> python_task