from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from pytz import timezone

# Set the timezone to Casablanca
casablanca_tz = timezone('Africa/Casablanca')

default_args = {
    'owner': 'akram_fouguir',
    'depends_on_past': False,
    'start_date': datetime.now(casablanca_tz),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Weather_app',
    default_args=default_args,
    description='An Airflow DAG to fetch weather data and update the CSV file',
    schedule_interval='0 */3 * * *',  # Run every 3 hours
    max_active_runs=1,  # Ensure only one run at a time
    catchup=False,  # Do not run backfill for the intervals between start_date and the current date
)

# Define the Bash command to install necessary packages
install_command = 'pip install scikit-learn pandas fastapi uvicorn imblearn'  # Add other packages as needed
install_packages_task = BashOperator(
    task_id='install_packages',
    bash_command=install_command,
    dag=dag,
)

# Define the Bash command to execute the Python script
bash_command_main = 'python /opt/airflow/dags/scripts/main.py'

# Task to execute the Python script
execute_script_task_1 = BashOperator(
    task_id='task_1',
    bash_command=bash_command_main,
    dag=dag
)

# Task to execute the Python script
execute_script_task_2 = BashOperator(
    task_id='task_2',
    bash_command='python /opt/airflow/dags/scripts/Projet_ML2.py',
    dag=dag
)

# Task to execute the Python script
execute_script_task_3 = BashOperator(
    task_id='task_3',
    bash_command='python /opt/airflow/dags/scripts/file_fastapi.py',
    dag=dag
)

# Set task dependencies
install_packages_task >> execute_script_task_1 >> execute_script_task_2 >> execute_script_task_3
