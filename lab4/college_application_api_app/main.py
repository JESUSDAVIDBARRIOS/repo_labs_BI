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
         rows.append(row.dict())
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
         rows.append(row.dict())
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