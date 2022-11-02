import json
from fastapi import FastAPI, Response, status
import pandas as pd
from DataModel import DataModel
from PredictionModel import Model
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
   return {"Msg": "Hi! Welcome to the College Application API. Please use the /predict endpoint to get predictions or the /update-model to update the model with new data."}

@app.post("/predict")
def make_predictions(data: List[DataModel], response: Response):
   try:
      rows = []
      for i, row in enumerate(data):
         filaJson = row.dict()
         if filaJson['gre_score'] < 0 or filaJson['gre_score'] > 340:
            raise Exception(f"GRE score must be between 0 and 340 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['toefl_score'] < 0 or filaJson['toefl_score'] > 120:
            raise Exception(f"TOEFL score must be between 0 and 120 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['university_rating'] < 0 or filaJson['university_rating'] > 5:
            raise Exception(f"University rating must be between 0 and 5 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['sop'] < 0 or filaJson['sop'] > 5:
            raise Exception(f"SOP must be between 0 and 5 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['lor'] < 0 or filaJson['lor'] > 5:
            raise Exception(f"LOR must be between 0 and 5 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['cgpa'] < 0 or filaJson['cgpa'] > 10:
            raise Exception(f"CGPA must be between 0 and 10 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['research'] < 0 or filaJson['research'] > 1:
            raise Exception(f"Research must be 0 or 1 in the row with serial no. {filaJson['serial_no']}")
         rows.append(filaJson)
      df = pd.DataFrame(rows)

      # Change column names to title case
      df.columns = [col.title() for col in df.columns]
      # In the column names, replace "_" with " "
      df.columns = [col.replace("_", " ") for col in df.columns]

      # Rename columns
      df = df.rename(columns={"Serial No": "Serial No.", "Gre Score": "GRE Score", "Toefl Score": "TOEFL Score","Sop":"SOP", "Lor": "LOR", "Cgpa": "CGPA"})

      model = Model()

      result = model.make_predictions(df)

      # Convert column names to lower case
      result.columns = [col.lower() for col in result.columns]
      result.columns = [col.replace(" ", "_") for col in result.columns]

      # Convert result to JSON
      return json.loads(result.to_json(double_precision=2, orient="records"))

   except Exception as e:
      response.status_code = status.HTTP_400_BAD_REQUEST
      return {"Error": "Error: " + str(e)}

@app.post("/update-model")
def update_model(data: List[DataModel], response: Response):
   try:
      rows = []
      for i, row in enumerate(data):
         filaJson = row.dict()
         if filaJson['gre_score'] < 0 or filaJson['gre_score'] > 340:
            raise Exception(f"GRE score must be between 0 and 340 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['toefl_score'] < 0 or filaJson['toefl_score'] > 120:
            raise Exception(f"TOEFL score must be between 0 and 120 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['university_rating'] < 0 or filaJson['university_rating'] > 5:
            raise Exception(f"University rating must be between 0 and 5 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['sop'] < 0 or filaJson['sop'] > 5:
            raise Exception(f"SOP must be between 0 and 5 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['lor'] < 0 or filaJson['lor'] > 5:
            raise Exception(f"LOR must be between 0 and 5 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['cgpa'] < 0 or filaJson['cgpa'] > 10:
            raise Exception(f"CGPA must be between 0 and 10 in the row with serial no. {filaJson['serial_no']}")
         if filaJson['research'] < 0 or filaJson['research'] > 1:
            raise Exception(f"Research must be 0 or 1 in the row with serial no. {filaJson['serial_no']}")
         if filaJson["admission_points"] < 0 or filaJson["admission_points"] > 150:
            raise Exception(f"Admission points must be between 0 and 150 in the row with serial no. {filaJson['serial_no']}")

         rows.append(filaJson)
      df = pd.DataFrame(rows)

      # Change column names to title case
      df.columns = [col.title() for col in df.columns]
      # In the column names, replace "_" with " "
      df.columns = [col.replace("_", " ") for col in df.columns]

      # Rename columns
      df = df.rename(columns={"Serial No": "Serial No.", "Gre Score": "GRE Score", "Toefl Score": "TOEFL Score","Sop":"SOP", "Lor": "LOR", "Cgpa": "CGPA"})

      model = Model()

      result = model.update_model(df)

      return result

   except Exception as e:
      response.status_code = status.HTTP_400_BAD_REQUEST
      return {"Error": "Error: " + str(e)}