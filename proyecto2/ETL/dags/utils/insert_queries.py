from utils.file_util import cargar_datos

# city insertion
def insert_query_municipio(**kwargs):
    
    insert = f"INSERT INTO municipio (Codigo_entidad,Entidad,Departamento) VALUES "
    insertQuery = ""
    # Es necesario colocar este try porque airflow comprueba el funcionamiento de las tareas en paralelo y al correr el DAG no existe el archivo dimension_city. Deben colocar try y except en todas las funciones de insert
    try:
        dataframe =cargar_datos(kwargs['csv_path'])
        for index, row in dataframe.iterrows():
            try:
                insertQuery += insert + f"({row.Codigo_entidad},\'{row.Entidad}\',\'{row.Departamento}\');\n"
            except:
                continue
        return insertQuery
    except Exception as e:
        pass

# customer insertion
def insert_query_mineria(**kwargs):
    # To Do
    insert = f"INSERT INTO hecho_produccion_minera (HPM_PKDWH,Codigo_entidad,Recurso_natural,Año,Trimestre,Valor_contraprestacion) VALUES "
    insertQuery = ""
    # Es necesario colocar este try porque airflow comprueba el funcionamiento de las tareas en paralelo y al correr el DAG no existe el archivo dimension_city. Deben colocar try y except en todas las funciones de insert
    try:
        dataframe =cargar_datos(kwargs['csv_path'])
        for index, row in dataframe.iterrows():
            try:
                insertQuery += insert + f"(DEFAULT,{row.Codigo_entidad},\'{row.recurso_natural}\',\'{row.Anio}\',\'{row.trimestre}\',\'{row.valor_contraprestacion}\');\n"
            except:
                continue
        return insertQuery
    except Exception as e:
        pass
# date insertion
def insert_query_conflicto(**kwargs):
    # To Do: recuerden que tratar con variables de tipo "DATE" en sql se hace uso de la instrucción TO_DATE. ejemplo: TO_DATE('31-12-2022','DD-MM-YYYY')
    insert = f"INSERT INTO numPersonasDesplazadas_Conflicto (NPD_PKDWH,Codigo_entidad,DatoNumerico,Año,Mes) VALUES "
    insertQuery = ""
    # Es necesario colocar este try porque airflow comprueba el funcionamiento de las tareas en paralelo y al correr el DAG no existe el archivo dimension_city. Deben colocar try y except en todas las funciones de insert
    try:
        dataframe =cargar_datos(kwargs['csv_path'])
        for index, row in dataframe.iterrows():
            try:
                insertQuery += insert + f"(DEFAULT,\'{row.Codigo_entidad}\',\'{row.DatoNumerico}\',\'{row.Anio}\',\'{row.Mes}\');\n"
            except:
                continue
        return insertQuery
    except:
        pass

# employee insertion
def insert_query_demografia(**kwargs):
    # To Do
    insert = f"INSERT INTO PuntajeSisben_Demografia (Codigo_entidad,DatoNumerico,Año,Mes) VALUES "
    insertQuery = ""
    # Es necesario colocar este try porque airflow comprueba el funcionamiento de las tareas en paralelo y al correr el DAG no existe el archivo dimension_city. Deben colocar try y except en todas las funciones de insert
    try:
        dataframe =cargar_datos(kwargs['csv_path'])
        for index, row in dataframe.iterrows():
            try:
                insertQuery += insert + f"(\'{row.Codigo_entidad}\',\'{row.DatoNumerico}\',\'{row.Anio}\',\'{row.Mes}\');\n"
            except:
                continue
        return insertQuery
    except Exception as e:
        pass


# stock item insertion
def insert_query_desempleo(**kwargs):
    # To Do
    insert = f"INSERT INTO MDM_desempleo (MDM_PKDWH,Codigo_entidad,DatoNumerico,Año,Mes) VALUES "
    insertQuery = ""
    # Es necesario colocar este try porque airflow comprueba el funcionamiento de las tareas en paralelo y al correr el DAG no existe el archivo dimension_city. Deben colocar try y except en todas las funciones de insert
    try:
        dataframe =cargar_datos(kwargs['csv_path'])
        for index, row in dataframe.iterrows():
            try:
                insertQuery += insert + f"(DEFAULT,\'{row.Codigo_entidad}\',\'{row.DatoNumerico}\',\'{row.Anio}\',\'{row.Mes}\');\n"
            except:
                continue
        return insertQuery
    except Exception as e:
        pass
    
# fact order insert
def insert_query_fact_CoberturaAcueducto_vivienda(**kwargs):
    # To Do
    insert = f"INSERT INTO CoberturaAcueducto_vivienda (CAV_PKDWH,Codigo_entidad,DatoNumerico,Año,Mes) VALUES "
    insertQuery = ""
    # Es necesario colocar este try porque airflow comprueba el funcionamiento de las tareas en paralelo y al correr el DAG no existe el archivo dimension_city. Deben colocar try y except en todas las funciones de insert
    try:
        dataframe =cargar_datos(kwargs['csv_path'])
        for index, row in dataframe.iterrows():
            try:
                insertQuery += insert + f"(DEFAULT,\'{row.Codigo_entidad}\',\'{row.DatoNumerico}\',\'{row.Anio}\',\'{row.Mes}\');\n"
            except:
                continue
        return insertQuery
    except Exception as e:
        pass

def insert_query_fact_educacion(**kwargs):
    # To Do
    insert = f"INSERT INTO PuntajePromedioICFES_educacion (PSD_PKDWH,Codigo_entidad,Indicador,DatoNumerico,Año,Mes) VALUES "
    insertQuery = ""
    # Es necesario colocar este try porque airflow comprueba el funcionamiento de las tareas en paralelo y al correr el DAG no existe el archivo dimension_city. Deben colocar try y except en todas las funciones de insert
    try:
        dataframe =cargar_datos(kwargs['csv_path'])
        for index, row in dataframe.iterrows():
            try:
                insertQuery += insert + f"(DEFAULT,\'{row.Codigo_entidad}\',\'{row.Indicador}\',\'{row.DatoNumerico}\',\'{row.Anio}\',\'{row.Mes}\');\n"
            except:
                continue
        return insertQuery
    except Exception as e:
        pass

def insert_query_fact_salud(**kwargs):
    # To Do
    insert = f"INSERT INTO MortalidadNeonatal_salud (MNS_PKDWH,Codigo_entidad,DatoNumerico,Año,Mes) VALUES "
    insertQuery = ""
    # Es necesario colocar este try porque airflow comprueba el funcionamiento de las tareas en paralelo y al correr el DAG no existe el archivo dimension_city. Deben colocar try y except en todas las funciones de insert
    try:
        dataframe =cargar_datos(kwargs['csv_path'])
        for index, row in dataframe.iterrows():
            try:
                insertQuery += insert + f"(DEFAULT,\'{row.Codigo_entidad}\',\'{row.DatoNumerico}\',\'{row.Anio}\',\'{row.Mes}\');\n"
            except:
                continue
        return insertQuery
    except Exception as e:
        pass

def insert_query_fact_pobreza(**kwargs):
    # To Do
    insert = f"INSERT INTO IPM_pobreza (IPM_PKDWH,Codigo_entidad,DatoNumerico,Año,Mes) VALUES "
    insertQuery = ""
    # Es necesario colocar este try porque airflow comprueba el funcionamiento de las tareas en paralelo y al correr el DAG no existe el archivo dimension_city. Deben colocar try y except en todas las funciones de insert
    try:
        dataframe =cargar_datos(kwargs['csv_path'])
        for index, row in dataframe.iterrows():
            try:
                insertQuery += insert + f"(DEFAULT,\'{row.Codigo_entidad}\',\'{row.DatoNumerico}\',\'{row.Anio}\',\'{row.Mes}\');\n"
            except:
                continue
        return insertQuery
    except Exception as e:
        pass
    
