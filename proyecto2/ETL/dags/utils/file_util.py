import pandas as pd
import os


def cargar_datos(name):
    df = pd.read_csv("data/" + name + ".csv", sep=',', encoding = 'latin1', index_col=False)
    return df



def guardar_datos(df, nombre):
    df.to_csv("data/" + nombre + ".csv",
              encoding='latin1', sep=',', index=False)


def procesar_datos():

    print("Hello World")

    # Cargar datos desde mineriaInfo.json
    df_mineria = pd.read_json('data/mineriaInfo.json')
    # Replace column name 'codigo_dane' with 'Código Entidad'
    df_mineria.rename(columns={'codigo_dane': 'Código Entidad'}, inplace=True)
    # Replace column name 'municipio_productor' with 'Entidad'
    df_mineria.rename(columns={'municipio_productor': 'Entidad'}, inplace=True)
    # Replace column name 'departamento' with 'Departamento'
    df_mineria.rename(columns={'departamento': 'Departamento'}, inplace=True)
    # Replace column name 'a_o_produccion' with 'Año'
    df_mineria.rename(columns={'a_o_produccion': 'Año'}, inplace=True)

    # Dimension conflicto
    df_conflicto = pd.read_csv('data/Conflicto Armado.csv', sep=';')

    # Drop columns with null values in 'Código Departamento' column
    df_conflicto.dropna(subset=['Código Departamento'], inplace=True)

    # In the column Dato Numérico, replace '.' with ''
    df_conflicto['Dato Numérico'] = df_conflicto['Dato Numérico'].str.replace('.', '')
    df_conflicto['Dato Numérico'] = df_conflicto['Dato Numérico'].str.replace(',', '.')

    # Convert column 'Dato Numérico' to float
    df_conflicto['Dato Numérico'] = df_conflicto['Dato Numérico'].astype(float)

    # Replace null values in 'Dato Numérico' column with -1
    df_conflicto['Dato Numérico'].fillna(-1, inplace=True)

    # In 'Dato Cualitativo' column, replace null values with 'N/A o Sin valor'
    df_conflicto['Dato Cualitativo'].fillna('N/A o Sin valor', inplace=True)

    # Dimension Demografia
    df_demografia = pd.read_csv('data/Demografía Y Poblacion.csv', sep=';')
    # Drop rows with null values in 'Código Departamento' column
    df_demografia.dropna(subset=['Código Departamento'], inplace=True)

    # Drop column 'Dato Cualitativo'
    df_demografia.drop('Dato Cualitativo', axis=1, inplace=True)

    # In the column Dato Numérico, replace '.' with ''
    df_demografia['Dato Numérico'] = df_demografia['Dato Numérico'].str.replace('.', '')
    df_demografia['Dato Numérico'] = df_demografia['Dato Numérico'].str.replace(',', '.')

    # Convert column 'Dato Numérico' to float
    df_demografia['Dato Numérico'] = df_demografia['Dato Numérico'].astype(float)

    # Replace null values in 'Dato Numérico' column with -1
    df_demografia['Dato Numérico'].fillna(-1, inplace=True)

    # Dimension Desempleo
    df_desempleo = pd.read_csv('data/Medicion de desempleo municipal.csv', sep=';')
    # Drop rows with null values in 'Código Departamento' column
    df_desempleo.dropna(subset=['Código Departamento'], inplace=True)

    # In the column Dato Numérico, replace '.' with ''
    df_desempleo['Dato Numérico'] = df_desempleo['Dato Numérico'].str.replace('.', '')
    df_desempleo['Dato Numérico'] = df_desempleo['Dato Numérico'].str.replace(',', '.')

    # Convert column 'Dato Numérico' to float
    df_desempleo['Dato Numérico'] = df_desempleo['Dato Numérico'].astype(float)

    # Replace null values in 'Dato Numérico' column with -1
    df_desempleo['Dato Numérico'].fillna(-1, inplace=True)

    # In 'Dato Cualitativo' column, replace null values with 'N/A o Sin valor'
    df_desempleo['Dato Cualitativo'].fillna('N/A o Sin valor', inplace=True)

    # Dimension Vivienda
    df_vivienda = pd.read_csv('data/TerriData_Dim3_viviendaServiciosPublicos.csv', sep=';')
    # Drop rows with null values in 'Código Departamento' column
    df_vivienda.dropna(subset=['Código Departamento'], inplace=True)

    # In the column Dato Numérico, replace '.' with ''
    df_vivienda['Dato Numérico'] = df_vivienda['Dato Numérico'].str.replace('.', '')
    df_vivienda['Dato Numérico'] = df_vivienda['Dato Numérico'].str.replace(',', '.')

    # Convert column 'Dato Numérico' to float
    df_vivienda['Dato Numérico'] = df_vivienda['Dato Numérico'].astype(float)

    # Replace null values in 'Dato Numérico' column with -1
    df_vivienda['Dato Numérico'].fillna(-1, inplace=True)

    # In 'Dato Cualitativo' column, replace null values with 'N/A o Sin valor'
    df_vivienda['Dato Cualitativo'].fillna('N/A o Sin valor', inplace=True)

    # Dimension Educación
    df_educacion = pd.read_csv('data/TerriData_Dim4_Educacion.csv', sep=';')
    # Drop rows with null values in 'Código Departamento' column
    df_educacion.dropna(subset=['Código Departamento'], inplace=True)

    # In the column Dato Numérico, replace '.' with ''
    df_educacion['Dato Numérico'] = df_educacion['Dato Numérico'].str.replace('.', '')
    df_educacion['Dato Numérico'] = df_educacion['Dato Numérico'].str.replace(',', '.')

    # Convert column 'Dato Numérico' to float
    df_educacion['Dato Numérico'] = df_educacion['Dato Numérico'].astype(float)

    # Replace null values in 'Dato Numérico' column with -1
    df_educacion['Dato Numérico'].fillna(-1, inplace=True)

    # Drop column 'Dato Cualitativo'
    df_educacion.drop('Dato Cualitativo', axis=1, inplace=True)


    # Dimension Salud
    df_salud = pd.read_csv('data/TerriData_Dim5_salud.csv', sep=';')
    # Drop rows with null values in 'Código Departamento' column
    df_salud.dropna(subset=['Código Departamento'], inplace=True)

    # Drop column 'Dato Cualitativo'
    df_salud.drop('Dato Cualitativo', axis=1, inplace=True)

    # In the column Dato Numérico, replace '.' with ''
    df_salud['Dato Numérico'] = df_salud['Dato Numérico'].str.replace('.', '')
    df_salud['Dato Numérico'] = df_salud['Dato Numérico'].str.replace(',', '.')

    # Convert column 'Dato Numérico' to float
    df_salud['Dato Numérico'] = df_salud['Dato Numérico'].astype(float)

    # Replace null values in 'Dato Numérico' column with -1
    df_salud['Dato Numérico'].fillna(-1, inplace=True)


    # Dimension Pobreza
    df_pobreza = pd.read_csv('data/TerriData_Dim14_pobreza.csv', sep=';')
    # To Do: Limpiar los datos y guardarlos
    # Drop rows with null values in 'Código Departamento' column
    df_pobreza.dropna(subset=['Código Departamento'], inplace=True)

    # Drop column 'Dato Cualitativo'
    df_pobreza.drop('Dato Cualitativo', axis=1, inplace=True)

    # In the column Dato Numérico, replace '.' with ''
    df_pobreza['Dato Numérico'] = df_pobreza['Dato Numérico'].str.replace('.', '')
    df_pobreza['Dato Numérico'] = df_pobreza['Dato Numérico'].str.replace(',', '.')

    # Convert column 'Dato Numérico' to float
    df_pobreza['Dato Numérico'] = df_pobreza['Dato Numérico'].astype(float)

    # Replace null values in 'Dato Numérico' column with -1
    df_pobreza['Dato Numérico'].fillna(-1, inplace=True)

    #Creacion tabla municipio

    ## Create new dataframe 'df_municipio' with the following columns: 'Código Entidad', 'Entidad', 'Departamento'
    df_municipio = pd.DataFrame(columns=['Código Entidad', 'Entidad', 'Departamento'])

    # Iterate over the rows of 'df_conflicto' dataframe
    for index, row in df_conflicto.iterrows():
        # If the value of 'Código Entidad' column is not in 'df_departamentos' dataframe, add it
        if row['Código Entidad'] not in df_municipio['Código Entidad'].values:
            df_municipio = df_municipio.append({'Código Entidad': row['Código Entidad'], 'Entidad': row['Entidad'], 'Departamento': row['Departamento']}, ignore_index=True)

    # In df_conflicto drop columns 'Entidad', 'Código Departamento' and 'Departamento'
    df_conflicto.drop(['Entidad', 'Código Departamento', 'Departamento'], axis=1, inplace=True)

    # Iterate over the rows of 'df_demografia' dataframe
    for index, row in df_demografia.iterrows():
        # If the value of 'Código Entidad' column is not in 'df_departamentos' dataframe, add it
        if row['Código Entidad'] not in df_municipio['Código Entidad'].values:
            df_municipio = df_municipio.append({'Código Entidad': row['Código Entidad'], 'Entidad': row['Entidad'], 'Departamento': row['Departamento']}, ignore_index=True)

    # In df_demografia drop columns 'Entidad', 'Código Departamento' and 'Departamento'
    df_demografia.drop(['Entidad', 'Código Departamento', 'Departamento'], axis=1, inplace=True)
        
    # Iterate over the rows of 'df_desempleo' dataframe
    for index, row in df_desempleo.iterrows():
        # If the value of 'Código Entidad' column is not in 'df_departamentos' dataframe, add it
        if row['Código Entidad'] not in df_municipio['Código Entidad'].values:
            df_municipio = df_municipio.append({'Código Entidad': row['Código Entidad'], 'Entidad': row['Entidad'], 'Departamento': row['Departamento']}, ignore_index=True)

    # In df_desempleo drop columns 'Entidad', 'Código Departamento' and 'Departamento'
    df_desempleo.drop(['Entidad', 'Código Departamento', 'Departamento'], axis=1, inplace=True)

    # Iterate over the rows of 'df_vivienda' dataframe
    for index, row in df_vivienda.iterrows():
        # If the value of 'Código Entidad' column is not in 'df_departamentos' dataframe, add it
        if row['Código Entidad'] not in df_municipio['Código Entidad'].values:
            df_municipio = df_municipio.append({'Código Entidad': row['Código Entidad'], 'Entidad': row['Entidad'], 'Departamento': row['Departamento']}, ignore_index=True)

    # In df_vivienda drop columns 'Entidad', 'Código Departamento' and 'Departamento'
    df_vivienda.drop(['Entidad', 'Código Departamento', 'Departamento'], axis=1, inplace=True)

    # Iterate over the rows of 'df_educacion' dataframe
    for index, row in df_educacion.iterrows():
        # If the value of 'Código Entidad' column is not in 'df_departamentos' dataframe, add it
        if row['Código Entidad'] not in df_municipio['Código Entidad'].values:
            df_municipio = df_municipio.append({'Código Entidad': row['Código Entidad'], 'Entidad': row['Entidad'], 'Departamento': row['Departamento']}, ignore_index=True)

    # In df_educacion drop columns 'Entidad', 'Código Departamento' and 'Departamento'
    df_educacion.drop(['Entidad', 'Código Departamento', 'Departamento'], axis=1, inplace=True)

    # Iterate over the rows of 'df_salud' dataframe
    for index, row in df_salud.iterrows():
        # If the value of 'Código Entidad' column is not in 'df_departamentos' dataframe, add it
        if row['Código Entidad'] not in df_municipio['Código Entidad'].values:
            df_municipio = df_municipio.append({'Código Entidad': row['Código Entidad'], 'Entidad': row['Entidad'], 'Departamento': row['Departamento']}, ignore_index=True)

    # In df_salud drop columns 'Entidad', 'Código Departamento' and 'Departamento'
    df_salud.drop(['Entidad', 'Código Departamento', 'Departamento'], axis=1, inplace=True)

    # Iterate over the rows of 'df_pobreza' dataframe
    for index, row in df_pobreza.iterrows():
        # If the value of 'Código Entidad' column is not in 'df_departamentos' dataframe, add it
        if row['Código Entidad'] not in df_municipio['Código Entidad'].values:
            df_municipio = df_municipio.append({'Código Entidad': row['Código Entidad'], 'Entidad': row['Entidad'], 'Departamento': row['Departamento']}, ignore_index=True)

    # In df_pobreza drop columns 'Entidad', 'Código Departamento' and 'Departamento'
    df_pobreza.drop(['Entidad', 'Código Departamento', 'Departamento'], axis=1, inplace=True)

    # Iterate over the rows of 'df_mineria' dataframe
    for index, row in df_mineria.iterrows():
        # If the value of 'Código Entidad' column is not in 'df_departamentos' dataframe, add it
        if row['Código Entidad'] not in df_municipio['Código Entidad'].values:
            df_municipio = df_municipio.append({'Código Entidad': row['Código Entidad'], 'Entidad': row['Entidad'], 'Departamento': row['Departamento']}, ignore_index=True)

    # In df_mineria drop columns 'Entidad', and 'Departamento'
    df_mineria.drop(['Entidad', 'Departamento'], axis=1, inplace=True)

    #Escogencia de columnas

    # En df_mineria eliminar columnas 'nombre_del_proyecto', 'tipo_contraprestacion', 'cantidad_producci_n'
    df_mineria.drop(['nombre_del_proyecto', 'tipo_contraprestacion', 'cantidad_producci_n', 'unidad_medida'], axis=1, inplace=True)

    # Borrar filas en df_conflicto donde 'Indicador' es diferente a 'Número de personas desplazadas'
    df_conflicto = df_conflicto[df_conflicto['Indicador'] == 'Número de personas desplazadas']

    # Eliminar columnas 'Dato Cualitativo', 'Indicador', 'Subcategoría', 'Dimensión'
    df_conflicto.drop(['Dato Cualitativo', 'Indicador', 'Subcategoría', 'Dimensión', 'Fuente', 'Unidad de Medida'], axis=1, inplace=True)

    # En df_demografia eliminar filas donde 'Indicador' no sea igual a 'Puntaje SISBEN: Promedio - Total'
    df_demografia = df_demografia[df_demografia['Indicador'] == 'Puntaje SISBEN: Promedio - Total']
    df_demografia.drop(['Indicador', 'Subcategoría', 'Dimensión', 'Fuente', 'Unidad de Medida'], axis=1, inplace=True)

    # En df_desempleo eliminar filas donde 'Indicador' no sea igual a 'MDM'
    df_desempleo = df_desempleo[df_desempleo['Indicador'] == 'MDM']
    df_desempleo.drop(['Indicador', 'Subcategoría', 'Dimensión', 'Fuente', 'Unidad de Medida', 'Dato Cualitativo'], axis=1, inplace=True)

    # En df_desempleo eliminar filas donde 'Indicador' no sea igual a 'MDM'
    df_vivienda = df_vivienda[df_vivienda['Indicador'] == 'Cobertura de acueducto (REC)']
    df_vivienda.drop(['Indicador', 'Subcategoría', 'Dimensión', 'Fuente', 'Unidad de Medida', 'Dato Cualitativo'], axis=1, inplace=True)

    # Eliminar filas donde 'Indicador' no tienen la palabra 'Puntaje promedio Pruebas Saber 11'
    df_educacion = df_educacion[df_educacion['Indicador'].str.contains('Puntaje promedio Pruebas Saber 11')]
    df_educacion.drop(['Subcategoría', 'Dimensión', 'Fuente', 'Unidad de Medida'], axis=1, inplace=True)

    # Elimiinar filas donde 'Indicador' no sea igual a 'Tasa de mortalidad neonatal'
    df_salud = df_salud[df_salud['Indicador'] == 'Tasa de mortalidad neonatal']
    df_salud.drop(['Indicador', 'Subcategoría', 'Dimensión', 'Fuente', 'Unidad de Medida'], axis=1, inplace=True)

    # Eliminar filas donde 'Indicador' no sea igual a 'Índice de pobreza multidimensional - IPM'
    df_pobreza = df_pobreza[df_pobreza['Indicador'] == 'Índice de pobreza multidimensional - IPM']
    df_pobreza.drop(['Indicador', 'Subcategoría', 'Dimensión', 'Fuente', 'Unidad de Medida'], axis=1, inplace=True)

    # Rename Código Entidad column to CodigoEntidad
    df_municipio.rename(columns={'Código Entidad': 'Codigo_entidad'}, inplace=True)

    df_mineria.rename(columns={'Código Entidad': 'Codigo_entidad', "Año":"Anio"}, inplace=True)

    df_conflicto.rename(columns={'Código Entidad': 'Codigo_entidad', 'Dato Numérico': 'DatoNumerico', "Año":"Anio"}, inplace=True)

    df_demografia.rename(columns={'Código Entidad': 'Codigo_entidad', 'Dato Numérico': 'DatoNumerico', "Año":"Anio"}, inplace=True)

    df_desempleo.rename(columns={'Código Entidad': 'Codigo_entidad', 'Dato Numérico': 'DatoNumerico', "Año":"Anio"}, inplace=True)

    df_vivienda.rename(columns={'Código Entidad': 'Codigo_entidad', 'Dato Numérico': 'DatoNumerico', "Año":"Anio"}, inplace=True)

    df_educacion.rename(columns={'Código Entidad': 'Codigo_entidad', 'Dato Numérico': 'DatoNumerico', "Año":"Anio"}, inplace=True)

    df_salud.rename(columns={'Código Entidad': 'Codigo_entidad', 'Dato Numérico': 'DatoNumerico', "Año":"Anio"}, inplace=True)

    df_pobreza.rename(columns={'Código Entidad': 'Codigo_entidad', 'Dato Numérico': 'DatoNumerico', "Año":"Anio"}, inplace=True)

    df_demografia.dropna(inplace=True)
    df_conflicto.dropna(inplace=True)
    df_desempleo.dropna(inplace=True)
    df_educacion.dropna(inplace=True)
    df_mineria.dropna(inplace=True)
    df_municipio.dropna(inplace=True)
    df_pobreza.dropna(inplace=True)
    df_salud.dropna(inplace=True)
    df_vivienda.dropna(inplace=True)

    guardar_datos(df_conflicto, "dimension_conflicto")
    guardar_datos(df_demografia, "dimension_demografia")
    guardar_datos(df_desempleo, "dimension_desempleo")
    guardar_datos(df_vivienda, "dimension_vivienda")
    guardar_datos(df_educacion, "dimension_educacion")
    guardar_datos(df_salud, "dimension_salud")
    guardar_datos(df_pobreza, "dimension_pobreza")
    guardar_datos(df_mineria, "hecho_mineria")
    guardar_datos(df_municipio, "dimension_municipio")