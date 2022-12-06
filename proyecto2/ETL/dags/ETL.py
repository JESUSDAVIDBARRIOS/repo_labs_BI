# Utilidades de airflow
from airflow.models import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.task_group import TaskGroup

# Utilidades de python
from datetime  import datetime

# Funciones ETL
from utils.crear_tablas import crear_tablas
from utils.file_util import procesar_datos
from utils.insert_queries import *

default_args= {
    'owner': 'Estudiante',
    'email_on_failure': False,
    'email': ['estudiante@uniandes.edu.co'],
    'start_date': datetime(2022, 5, 5) # inicio de ejecución
}

with DAG(
    "ETL",
    description='ETL',
    schedule_interval='@daily', # ejecución diaría del DAG
    default_args=default_args, 
    catchup=False) as dag:

    # task: 1 - preprocesamiento
    preprocesamiento = PythonOperator(
        task_id='preprocesamiento',
        python_callable=procesar_datos
    )

    # task: 2 crear las tablas en la base de datos postgres
    crear_tablas_db = PostgresOperator(
    task_id="crear_tablas_en_postgres",
    postgres_conn_id="postgres_localhost", # Nótese que es el mismo ID definido en la conexión Postgres de la interfaz de Airflow
    sql= crear_tablas()
    )

    # task: 3 poblar las tablas de dimensiones en la base de datos
    with TaskGroup('poblar_tablas') as poblar_tablas_dimensiones:

        # task: 3.1 poblar tabla municipio
        poblar_city = PostgresOperator(
            task_id="poblar_municipio",
            postgres_conn_id='postgres_localhost',
            sql=insert_query_municipio(csv_path = "dimension_city")
        )

        # task: 3.2 poblar tabla vivienda
        poblar_customer = PostgresOperator(
            task_id="poblar_vivienda",
            postgres_conn_id='postgres_localhost',
            sql=insert_query_fact_CoberturaAcueducto_vivienda(csv_path ="dimension_customer")
        )

        # task: 3.3 poblar tabla conflicto
        poblar_date = PostgresOperator(
            task_id="poblar_conflicto",
            postgres_conn_id='postgres_localhost',
            sql=insert_query_conflicto(csv_path = "dimension_date")
        )

        # task: 3.4 poblar tabla demografia
        poblar_employee = PostgresOperator(
            task_id="poblar_demografia",
            postgres_conn_id='postgres_localhost',
            sql=insert_query_demografia(csv_path = "dimension_employee")
        )

        # task: 3.5 poblar tabla desempleo
        poblar_stock_item = PostgresOperator(
            task_id="poblar_desempleo",
            postgres_conn_id='postgres_localhost',
            sql=insert_query_desempleo(csv_path = "dimension_stock_item")
        )

        # task: 3.6 poblar tabla educacion
        poblar_stock_item = PostgresOperator(
            task_id="poblar_educacion",
            postgres_conn_id='postgres_localhost',
            sql=insert_query_fact_educacion(csv_path = "dimension_stock_item")
        )

        # task: 3.7 poblar tabla salud
        poblar_stock_item = PostgresOperator(
            task_id="poblar_salud",
            postgres_conn_id='postgres_localhost',
            sql=insert_query_fact_salud(csv_path = "dimension_stock_item")
        )

        # task: 3.8 poblar tabla pobreza
        poblar_stock_item = PostgresOperator(
            task_id="poblar_pobreza",
            postgres_conn_id='postgres_localhost',
            sql=insert_query_fact_pobreza(csv_path = "dimension_stock_item")
        )


    # task: 4 poblar la tabla de hechos
    poblar_fact_order = PostgresOperator(
            task_id="construir_tabla_de_hechos_mineria",
            postgres_conn_id='postgres_localhost',
            sql=insert_query_mineria(csv_path = "fact_order")
    )

    # flujo de ejecución de las tareas  
    preprocesamiento >> crear_tablas_db >> poblar_tablas_dimensiones >> poblar_fact_order
