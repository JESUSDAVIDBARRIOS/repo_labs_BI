Instrucciones de instalación, despliegue y funcionamiento del API

En la aplicación PostMan ingresar este url https://college-application-api-app.herokuapp.com/ 
Si se desea hacer una predicción de la probabilidad de ser aceptado en una universidad, se debe ingresar el siguiente url https://college-application-api-app.herokuapp.com/predict y en el body de la petición de tipo Post ingresar los datos de la siguiente manera:

{
    "gre_score": 300,
    "toefl_score": 100,
    "university_rating": 1,
    "sop": 1.5,
    "lor": 1.5,
    "cgpa": 6.8,
    "research": 0
}

Se puede ingresar varios datos en el body de la petición, por ejemplo:

{
    "gre_score": 300,
    "toefl_score": 100,
    "university_rating": 1,
    "sop": 1.5,
    "lor": 1.5,
    "cgpa": 6.8,
    "research": 0
},
{
    "gre_score": 300,
    "toefl_score": 100,
    "university_rating": 1,
    "sop": 1.5,
    "lor": 1.5,
    "cgpa": 6.8,
    "research": 0
}

Para actualizar el modelo se debe ingresar el siguiente url https://college-application-api-app.herokuapp.com/update_model y en el body de la petición de tipo ingresar los datos de la siguiente manera (Puede copiar y pegar el resultado obtenido en el literal anterior):

{
    "gre_score": 300,
    "toefl_score": 100,
    "university_rating": 1,
    "sop": 1.5,
    "lor": 1.5,
    "cgpa": 6.8,
    "research": 0,
    "chance_of_admit": 0.5
}

Se puede ingresar varios datos en el body de la petición, por ejemplo:

{
    "gre_score": 300,
    "toefl_score": 100,
    "university_rating": 1,
    "sop": 1.5,
    "lor": 1.5,
    "cgpa": 6.8,
    "research": 0,
    "chance_of_admit": 0.5
},
{
    "gre_score": 300,
    "toefl_score": 100,
    "university_rating": 1,
    "sop": 1.5,
    "lor": 1.5,
    "cgpa": 6.8,
    "research": 0,
    "chance_of_admit": 0.5
}

Si se desea correr directamente desde el dispositivo local, se debe tener instalado Python 3.8.5 y ejecutar los siguientes comandos en la terminal en el caso de no tener las librerías de fastapi instaladas:

pip install fastapi
pip install "uvicorn[standard]"

Para correr el servidor se debe ejecutar el siguiente comando en la terminal (recuerde estar en el directorio donde se encuentra el archivo main.py):

uvicorn main:app --reload

Si todo corre correctamente, se debe ver el siguiente mensaje en la terminal:

INFO:     Will watch for changes in these directories: ["Directorio donde se encuentra el archivo main.py"]
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [18400] using WatchFiles
INFO:     Started server process [27660]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

A partir de este momento el servidor se encuentra corriendo y se puede hacer las peticiones desde PostMan utilizando el siguiente link en PostMan:
http://127.0.0.1:8000/predict (Para hacer predicciones)
http://127.0.0.1:8000/update_model (Para actualizar el modelo)