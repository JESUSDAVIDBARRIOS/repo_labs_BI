# Laboratorio  - Regresión

## Objetivos

- Construir modelos analíticos para estimar una variable objetivo continua a partir de una serie de variables observadas.

- Comprender el proceso para la construcción de modelos analíticos que responden a una tarea de regresión.

- Automatizar el proceso de construcción de modelos analíticos con el uso de pipelines de tal forma que puedan ser usados en ambiente de producción.

- Extraer información útil para el negocio a partir de los resultados de los modelos de regresión.


## Herramientas

- Librerías principales de Python para procesamiento y visualización de datos como: pandas, sklearn, seaborn, numpy y matplotlib.  
    Se recomienda usar la última distribución disponible de Anaconda Individual Edition, pueden encontrar el instalador en este [enlace](https://www.anaconda.com/products/individual). 

- Ambiente de desarrollo: JupyterLab en distribución de Anaconda o trabajar sobre Google Colab.  

## Enunciado

### Descripción de negocio

La Universidad de los Alpes es una institución educativa de alta calidad y una de las más prestigiosas de su región. Anualmente, la universidad realiza un proceso selectivo de admisión para programas de maestría que consta de un examen que evalúa distintas competencias en los aspirantes.

El puntaje obtenido en dicho examen determina no solo si el aspirante es admitido en el programa de maestría desado, sino también, si dicho aspirante puede aplicar a incentivos y becas brindados por la institución.

Es por ello, que la Universidad desea hacer un análisis que le permita identificar los diferentes perfiles de los estudiantes que aspiran a ser parte de la institución, y particularmente, los factores que más influyen en el puntaje de admisión. 

La  Universidad cuenta con un conjunto de datos sobre el puntaje de aceptación de diferentes aspirantes a lo largo de los últimos años, junto con algunos indicadores de sus antecedentes académicos.
Esta información quieren utilizarla para construir un modelo que les pueda ayudar para resolver las siguientes tareas:

* Identificar las variables que más impactan en el puntaje de admisión.
* Predecir el puntaje de admisión a partir de las variables de interés.

La Universidad ha puesto a su disposición la base de datos con información del [puntaje de admisión](data/university_admission_train.csv).

El detalle de cada una de las variables se encuentra en el siguiente [diccionario](data/dictionary.md)

Adicionalmente, usted cuenta con unos [datos de prueba](data/university_admission_test.csv), los cuales serán utilizados por la Universidad para probar el resultado de su modelo y validar si cumple 
con las expectativas.


### Instrucciones 


La Universidad desea que usted lo ayude a realizar el análisis de los datos, para lo cual, su equipo debe desarrollar un modelo que permita estimar el puntaje de admisión dada la información académica de un aspirante. Al igual que seguir los siguientes pasos para garantizar el uso de la metodología "ASUM-DM":

1. **Entendimiento de los datos:** en esta etapa recuerde que debe describir la característica de los datos e incluir el análisis de calidad de datos.

2. **Identificación de variables a utilizar**: su equipo debe identificar las variables más relevantes que puedan utilizarse en el proceso de estimación. 

3. **Preparación de datos:** en esta etapa su equipo debe identificar y solucionar cualquier problema de inconsistencia o ruido que se pueda tener en los datos. Además, deben tener en cuenta el preprocesamiento necesario para el uso de regresiones. No olvide ejecutar un esquema de manejo de variables faltantes, identificación/manejo de datos atípicos y de normalizar en caso de ser necesario.

4. **Modelamiento:** a partir de las variables identificadas anteriormente, se debe plantear una regresión que estime la variable objetivo y medir su desempeño.

5. **Evaluación cuantitativa:** a partir de las métricas seleccionadas para comparar y seleccionar el mejor modelo, explicar el resultado obtenido desde el punto de vista cuantitativo y contestar la pregunta:
    * ¿Su equipo recomienda instalar el modelo de estimación en producción o es mejor continuar usando expertos para la tarea?
	* En caso de no recomendar el uso de un modelo de regresión ¿Qué otras posibilidades tiene la empresa? ¿Hacia dónde debe seguir con esta tarea?

6. **Evaluación cualitativa:** responder a la pregunta del negocio 	¿Qué obtuvieron con el ejercicio de regresión? ¿Cuáles son las variables más influyentes y que tan confiables son los resultados?.

      **- Validación de supuestos:** realice los ajustes necesarios para que su modelo cumpla con las suposiciones necesarias para la inferencia estadística con regresiones.

      **- Interpretación de los coeficientes:** realice una interpretación de los coeficientes de la regresión, identificando los más relevantes para la tarea y cómo afectan la variable objetivo.

7. **Exportar el modelo:** su equipo debe exportar el modelo (creado utilizando pipelines) para poder ser usado sobre datos recientes en el ambiente de producción del cliente.



## Entregables

* Informe del laboratorio, que puede ser el mismo notebook, con el desarrollo y la evidencia de las etapas del 1 al 6.
* Modelo completo exportado en un archivo .joblib, usando la librería *joblib*. 
* Presentación con los resultados para la Universidad de los Alpes
* Visualización de los resultados 
* El notebook a entregar debe estar ejecutado.
	
Se espera que el informe no supere las 8 páginas y que incluya **JUSTIFICACIONES** de las decisiones tomadas en la construcción e interpretación de los modelos.



**Nota:** 
El modelo entregado será utilizado para estimar la variable objetivo de unos datos que separó el cliente. 
El cliente cargará el modelo entregado se lo aplicará a los datos y comparará el resultado con el valor real de la variable  objetivo. 
Ustedes tienen acceso a una copia de estos datos (sin la variable objetivo). Recuerde que el cliente no planea hacer ningún tipo de alteración sobre estos datos antes de entregárselos al modelo, por lo que su equipo debe exportar un *pipeline* capaz de hacer la manipulaciones  necesarias para hacer la tarea de estimación. Este archivo de datos se llama: *university_admission_test.csv*.

El código que usará el cliente es el siguiente:

```python
import numpy as np
import pandas as pd
import joblib

# Proceso de prubea del cliente
filename = 'modelo.joblib' # Ubicación del archivo entregado
df_recent = pd.read_csv('university_admission_test.csv') # Lectura de los datos recientes

# Lee el archivo y carga el modelo
pipeline = load(filename)

y_true = pd.read_csv('Recientes_Validacion.csv') # La columna que solo el cliente tiene
y_predicted =  pipeline.predict(df_recent)

# Calcula el desempeño del modelo
np.sqrt(mse(y_true, y_predicted))

```


## Instrucciones de Entrega
- El laboratorio se entrega en grupos de máximo 3 estudiantes
- Recuerde hacer la entrega por la sección unificada en Bloque Neón, antes del domingo 25 de septiembre a las 22:00.   
  Este será el único medio por el cual se recibirán entregas.
- En la entrega indique la etapa o etapas realizada por cada uno de los miembros del grupo.

## Rúbrica de Calificación

A continuación se encuentra la rúbrica de calificación.


| Concepto | Porcentaje |
|:---:|:---:|
| 1. Descripción del entendimiento de datos  | 5% |
| 2. Descripción del proceso de identificación de variables | 10% |
| 3. Descripción de la limpieza y preparación de los datos  | 5% |
| 4. Implementación de la regresión lineal y extracción de sus métricas de calidad  | 10% |
| 5. Exploración de los supuestos a partir del modelo de regresión planteado | 15% |
| 6. Realizar las transformaciones necesarias  para cumplir los supuestos | 15% |
| 7. Incorporar las transformaciones y el estimador al modelo en un *pipeline* y exportarlo | 10% |
| 8. Presentación para Universidad de los Alpes con resultados a nivel cuantitativo y cualitativo del modelo construido, recomendaciones dadas a la empresa y visualización | 15% |
| 9. Resultado del modelo al estimar el conjunto de datos que separó el cliente | 10% |
| 10. Notebook asociado y ejecutado junto con el código de la visualización del resultado del modelo| 5% |

La nota individual se calculará de acuerdo con las etapas realizadas por cada miembro del grupo. Se espera que el estudiante 1 del grupo se encargue del modelo analítico, el estudiante 2 del proceso del pipeline y el estudiante 3 de la visualización.

