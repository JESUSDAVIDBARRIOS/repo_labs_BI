# Laboratorio 2 - Clustering

[Objetivos](#objetivos)

[Herramientas](#herramientas)

[Enunciado](#enunciado)

[Entregables](#entregables)

[Rúbrica de clasificación](#rubrica)

[Sugerencias y aclaraciones](#sugerencias)

## <a name="objetivos"></a> Objetivos

- Comprender y aplicar el proceso asociado con una tarea de segmentación (*clustering*), incluyendo pasos previos de preparación de datos y posteriores de interpretación del resultados.
- Aplicar tres algoritmos de clústering (k-means y dos de libre elección) para resolver el objetivo de la organización. 
- Analizar e identificar los hiperparámetros adecuados dependiendo de los algoritmos utilizados.
- Comparar los 3 algoritmos seleccionados y definir cuál recomiendan a la organización.
- Obtener conclusiones a partir de los mejores grupos identificados que sean útiles para la organización.
- Comunicar los hallazgos encontrados a la organización y explicar por qué tienen valor para el negocio.

## <a name="herramientas"></a> Herramientas

Durante este laboratorio trabajaremos con las siguientes herramientas:

 - Python
	 - Distribución sugerida: [Anaconda](https://www.continuum.io/downloads) 
		 - La versión de Anaconda es 4.4
		 - La versión usada es la de python 2.7, usar python 3 no debería requerir muchos cambios.
	 - Ambiente de desarrollo
	   	 - JupyterLab
	   	 - Google Colab
	 - Librerías
	 	 - Pandas
		 - Scikit-learn
		 - Matplot
		 - Seaborn 

## <a name="enunciado"></a> Enunciado

### Descripción de negocio

ConsultAlpes es una consultora que se especializa en el análisis de finanzas de empresas colombianas. Con esos datos, ConsultAlpes toma decisiones
sobre las inversiones que realizarán y realiza análisis más profundos para diferentes empresas.

En este momento están interesados en caracterizar las empresas del mercado colombiano. Con esto, buscan identificar patrones sobre el crecimiento 
económico de las empresas de diferentes sectores del mercado colombiano. Para esto decidieron tomar datos recopilados por la Superintendencia de Sociedades
de las empresas con mayor participación del mercado real no financiero, los cuales encuentran en este [enlace](./data/Empresas_mas_grandes_del_pais_2018.csv), acompañados de su [diccionario de datos](./data/directorio.md).

ConsultAlpes los ha contactado para realizar este proceso de caracterización e identificación de patrones para construir perfiles de las empresas seleccionadas. Ellos esperan que estos perfiles les permitan
entender cómo son los diferentes grupos de empresas que hay en el país.

### Instrucciones 

La empresa quiere seguir apropiando la metodología Crisp-DM, en específico en su nueva versión ASUM-DM, para el desarrollo de estas iniciativas en analítica de datos, por lo cual le sugiere realizar los siguientes pasos: 

1. **Entendimiento de los datos:** en esta etapa es importante saber si los datos son o no suficientes para el alcance del proyecto y en caso de serlo entener bien las características de los datos y determinar las preparaciones que se requieren para lograr el objetivo del proyecto.
En particular, deben incluir cuántos datos se tienen (filas y columnas), el tipo de datos de las columnas, cuál es la distribución (discreta o continua). Para esto, es útil aplicar estadística descriptiva y utilizar gráficos sobre los datos, señalando sus principales estadísticos: media, 
varianza, desviación estándar, etc., para el caso de las columnas numéricas. En caso de datos categóricos recuerde que es importante conocer las categorías, los números de 
registro por categoría, en especial para las categorías con mayor representación en los datos. Recuerde que una segunda parte importante de esta etapa está relacionada con el análisis a nivel de calidad de datos y en particular a nivel de las dimensiones de calidad (completitud, unicidad, consistencia, validez) para identificar las actividades de preparación que requieren los datos.

2. **Preparación de datos:** es el procedimiento llevado a cabo para transformar los valores actuales de acuerdo con los algoritmos a utilizar y el objetivo de negocio a resolver.
Por ejemplo, manejar los datos nulos (missing values) o los valores atípicos (outliers).

3. **Modelamiento:** en este paso se lleva a cabo la elección del modelo con el que queremos cumplir nuestra tarea y su refinamiento.
En este caso, deben usar el algoritmo de K-Means y deberán compararlo con otros dos algoritmos como clustering jerárquico, DBScan, HDBScan, Gaussian Mixture.
Tengan en cuenta que, en ambientes profesionales, la elección y justificación del algoritmo y sus hiperparámetros  hace parte de su tarea de consultoría.
Se sugiere explorar la generación de clústeres que puedan llevar a mejores valores de coeficiente de silueta, al igual que a mejor comprensión de los grupos por parte de la organización.

4. **Validación:** En modelos de aprendizaje no supervisado la validación de los modelos es un reto importante que deben asumir los consultores.
    
    4.1 **Validación cuantitativa:** la calidad desde el punto de vista cuantitativo puede validarse utilizando el coeficiente de silueta
y ser ajustado siguiendo guías como el método del codo. Información adicional para complementar su interpretación puede encontrarla en este [enlace](https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a). Esta métrica tiene sentido con el algoritmo de k-means. Revise lo apropiado según el algoritmo utilizado.
    
    4.2 **Validación cualitativa:** una vez realizada la validación cuantitativa, se debe hacer una descripción de los grupos obtenidos y relacionarlo con el objetivo que tenía el negocio para ver si es posible utilizar el resultado obtenido o hay que seguir trabajando en alguna direccióne específica que recomienden. 
(clústers y conclusiones del proceso) para la comprensión por parte de la empresa.

5. **Visualización:** El estudiante debe proponer una visualización de los resultados obtenidos en un tablero de control,
de tal manera que el cliente tenga la capacidad de entender los resultados obtenidos en su labor de consultoría.

## <a name="entregables"></a> Entregables
- Informe que debe incluir:
    - Descripción detallada de cada etapa según las instrucciones dadas previamente
    - Indicar el nombre del estudiante que desarrolló cada algoritmo y una descripción general de cómo funciona.
    - Se espera que el informe no supere las 8 páginas.
- A nivel de visualización recuerde incluir el tablero de control construido
- Presentación con los resultados
- Notebook ejecutado

    
Algunas preguntas que pueden guiar su desarrollo son: 

1. ¿Qué criterios son importantes para la selección del modelo? 

2. ¿Cómo medir la calidad del modelo construido? ¿Cómo saber que el modelo construido tiene una buena calidad?  

3. ¿Qué retos tienen estos modelos no supervisados, si se quisieran aplicar a nivel profesional?

4. ¿Cómo varía la calidad del modelo obtenido si aplicó diferentes algoritmos?

5. ¿Qué pasa en la ejecución de los algortimos si se incluyen variables categóricas nominales. ¿Qué tratamiento se les debe aplicar? 


**Nota:** 
Recuerde que la presentación debe estar orientada al área de marketing, por lo que se recomienda evitar el uso de términos muy técnicos
y utilizar un lenguaje con el que el área esté familiarizada. Se les sugiere centrarse en la interpretación de los resultados.


## Instrucciones de Entrega
- El laboratorio se entrega en grupos de máximo 3 estudiantes. Estos estudiantes pueden ser de diferentes secciones.
- Recuerde hacer la entrega por la sección unificada en Bloque Neón, antes del miércoles 14 de septiembre a las 22:00.   
  Ese será el único medio por el cual se recibirán entregas.

## <a name="rubrica"></a> Rúbrica de Calificación

A continuación se encuentra la rúbrica de calificación.

**Nota:** Los siguientes porcentajes hacen referencia a la nota grupal, que corresponde a un 80% de la nota inidiviudal.  
El 20% restante se calcula según el puntaje obtenido en la implementación del algoritmo del cual el estudiante estuvo a cargo dentro del grupo.

| Concepto | Porcentaje |
|:---:|:---:|
| Descripción y análisis del entendimiento de los datos y de las tareas sugeridas de transformación | 15% |
| Descripción del preprocesamiento realizado, el genérico y el relacionado con el algoritmo utilizado. Justitificar utilizando el entendimiento de los datos | 10% |
| Implementación de K-means, descripción de las decisiones más importantes asociadas a la implementación del algoritmo y los hiperparámetros configurados | 6% |
| Implementación de un segundo algoritmo, descripción corta del algoritmo y de las decisiones más importantes asociadas a la implementación del algoritmo y los hiperparámetros configurados | 10% |
| Implementación de un tercer algoritmo de libre elección, descripción corta del algoritmo y de las decisiones más importantes asociadas a la implementación del algoritmo y los hiperparametros configurados | 10% |
| Análisis de los resultados obtenidos y justificación del modelo recomendado para el caso propuesto | 24% |
| Presentación para ConsultAlpes con resultados, recomendaciones dadas a la empresa y visualización usando el tablero de control construido| 20% |
| Notebook asociado, ejecutado | 5% |

## <a name="sugerencias"></a> Sugerencias y aclaraciones

 - Nota 1: la interpretación de los clusters se debe hacer en términos de las variables que considere importantes (incluya las usadas para la construcción de los clusters
 pero también otras variables, en especial las categóricas que no hayan incluido)
 - Nota 2: Analizar si los valores de cada columna corresponden a valores adecuados para el negocio, en caso de que no lo sean, deben tratar dichos valores y justificar sus decisiones.

Los siguientes enlaces pueden serle de utilidad para la implementación en Python. 

* [Ejemplo de K-Means usando Sklearn](https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html)

* [Artículo de Towards Data Science: K-means with Sklearn](https://towardsdatascience.com/k-means-clustering-with-scikit-learn-6b47a369a83c)

* [Artículo de Towards Data Science: Introducción al análisis de datos con Python](https://towardsdatascience.com/tips-and-tricks-for-fast-data-analysis-in-python-f108ad32fa90) 

 - Cada integrante del grupo debe estar encargado de la implementación de un algoritmo distinto. Sin embargo, todos los integrantes del grupo
deben tener la capacidad de explicar lo realizado por los demás compañeros
 - El análisis de resultados y su justificación debe ser realizado en grupo.
 - Las notas de los integrantes dentro de un mismo grupo de laboratorio pueden variar ya que cada integrante está encargado de la implementación de un algoritmo distinto. 
