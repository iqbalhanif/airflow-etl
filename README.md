# ETL/ELT with Airflow

This is ETL/ELT script by using Airflow (using local databases)

### Tools:
1. Python 3.x.x
2. Apache Airflow 2.x.x
3. Ubuntu (OS)
4. Database (MySQL & PostgreSQL, installed locally)
5. Several python packages (sqlalchemy, pandas, pymysql, etc)

### Dataset:
1. Chinook Dataset (stored in PostgreSQL)
2. Human Resource Dataset (stored in MySQL)

### Airflow Set Up in Windows: 
1. Enable Windows Subsystem for Linux
2. Install Ubuntu in Microsoft Store
3. Install python pip <br />
   · sudo apt-get install software-properties-common <br />
   · sudo apt-add-repository universe <br />
   · sudo apt-get update <br />
   · sudo apt-get install python3-pip <br />
4. InstalL Airflow <br />
   · export SLUGIFY_USES_TEXT_UNIDECODE=yes <br />
   · sudo pip3 install apache-airflow <br />
5. Initialize Airflow database, run airflow scheduler and webserver <br />
   · airflow db init <br />
   · airflow scheduler <br />
   · airflow webserver -p 8080 <br />
6. Create admin user and access Airflow GUI <br />
   · airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin <br />
   · airflow GUI in http://localhost:8080/ (access via browser) <br />
   
(reference: https://medium.com/analytics-vidhya/data-engineering-installing-apache-airflow-on-windows-10-without-docker-93635c3819c3)

![1635732825090](https://user-images.githubusercontent.com/18484807/139690676-3a3eebce-9ece-4a64-bba9-20a549befe5c.png)


### DAGs:
Directed Acyclic Graph – is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies. DAGs are located in 'dags' folder, for detail check $AIRFLOW_HOME/airflow.cfg,
1. You can set up the connection first before creating DAGs  https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html
2. Type of operator: MySqlOperator, PostgresOperator, PythonOperator, BashOperator
3. Example of each operator task can be seen on dags/blankspace_etl.py
4. If DAGS is unable to be executed, check permission (ls -l), if the file is not granted yet, use chmod 777 (dags name).py

### Some airflow command for DAGs:
1. DAGs list            : airflow dags list
2. Task list in DAG     : airflow tasks list (dag_id)
3. Testing task in DAG  : airflow tasks test (dag_id) (task_id) (date_execution in yyyy-mm-dd)
4. Check next schedule  : airflow dags next-execution (dag_id)
5. Pause/unpause DAG    : airflow dags pause/unpause (dag_id)
6. You can test the DAGs that you have created by using python: python3 (dag_file.py)
7. Run the taskin DAG   : airflow tasks run (dag_id) (task_id) (date_execution in yyyy-mm-dd)
8. Run DAG backfill     : airflow dag backfill (dag_id) --start-date (yyy-mm-dd) --end-date (yyyy-mm-dd)

# Data Warehouse

Data warehouse (DWH) adalah salah satu jenis sistem manajemen data yang terdiri dari berbagai jenis data dalam jumlah yang besar dan dari sumber yang beragam. Semua data tersebut bisa dianalisis agar bisa menghasilkan informasi penting demi menunjang keputusan perusahaan. Itulah mengapa, warehouse ini disebut sebagai salah satu penunjang aktivitas business intelligence. Dalam bahasa Indonesia, istilah ini kerap disebut gudang data (https://glints.com/id/lowongan/data-warehouse-adalah/#.YX_-UG1Bw2w).

### DWH Schema
1. Star Schema <br />
· In a star schema, as the structure of a star, there is one fact table in the middle and a number of associated dimension tables. This structure resembles a star and hence it is known as a star schema. <br />
· The fact table here consists of primary information in the data warehouse. It surrounds the smaller dimension lookup tables which will have details for different fact tables. The primary key which is present in each dimension is related to a foreign key which is present in the fact table. <br />
2. Snowflake Schema <br />
· Snowflake schema acts like an extended version of a star schema. There are additional dimensions added to Star schema. This schema is known as snowflake due to its structure. <br />
· In this schema, the centralized fact table will be connected to different multiple dimensions. The dimensions present are in normalized form from the multiple related tables which are present. The snowflake structure is detailed and structured when compared to star schema. <br />
3. Galaxy Schema <br />
· A fact constellation can consist of multiple fact tables. These are more than two tables that share the same dimension tables. This schema is also known as galaxy schema. <br />
· It is viewed as a collection of stars and hence the name galaxy. The shared dimensions in this schema are known as conformed dimensions. The dimensions in this schema are separated into segregated dimensions which are having different levels of hierarchy. <br />
(https://www.educba.com/data-warehouse-schema/)

### Creating DWH

