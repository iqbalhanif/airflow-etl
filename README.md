# ETL with Airflow

This is ETL script by using Airflow (using local databases)

Tools:
1. Python 3.x.x
2. Apache Airflow 2.x.x
3. Ubuntu (OS)
4. Database (MySQL & PostgreSQL, installed locally)

Dataset:
1. Chinook Dataset (stored in PostgreSQL)
2. Human Resource Dataset (stored in MySQL)

Airflow Set Up in Windows: 
1. Enable Windows Subsystem for Linux
2. Install Ubuntu in Microsoft Store
3. Install python pip
   · sudo apt-get install software-properties-common
   · sudo apt-add-repository universe
   · sudo apt-get update
   · sudo apt-get install python3-pip
4. InstalL Airflow
   · export SLUGIFY_USES_TEXT_UNIDECODE=yes
   · sudo pip3 install apache-airflow
5. Initialize Airflow database, run airflow scheduler and webserver
   · airflow db init
   · airflow scheduler
   · airflow webserver -p 8080
6. Create admin user and access Airflow GUI
   · airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
   · airflow GUI in http://localhost:8080/ (access via browser)
   
   
(reference: https://medium.com/analytics-vidhya/data-engineering-installing-apache-airflow-on-windows-10-without-docker-93635c3819c3)

DAGs:
Directed Acyclic Graph – is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies. DAGs are located in 'dags' folder
1. You can set up the connection first before creating DAGs  https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html
2. Type of operator: MySqlOperator, PostgresOperator, PythonOperator, BashOperator
3. Example of each operator task can be seen on dags/blankspace_etl.py
4. If DAGS is unable to be executed, check permission (ls -l), if the file is not granted yet, use chmod 777 (dags name).py

Some airflow command for DAGs:
1. DAGs list: airflow dags list
2. Task list in DAG: airflow tasks list (dag_id)
3. Testing task in DAG: airflow tasks test (dag_id) (task_id) (date_execution in yyyy-mm-dd)
4. Check next execution schedule: airflow dags next-execution (dag_id)
5. Pause/unpause DAG: airflow dags pause/unpause (dag_id)
6. You can test the DAGs that you have created by using python: python3 (dag_file.py)
