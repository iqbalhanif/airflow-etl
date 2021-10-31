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

Airflow Set Up in Windows (reference: https://medium.com/analytics-vidhya/data-engineering-installing-apache-airflow-on-windows-10-without-docker-93635c3819c3)
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
