from joblib import load, dump
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_percentage_error

class Model:

    def __init__(self):
        self.model = load('./assets/pipe.joblib')

    def make_predictions(self, data):
        predictions = self.model.predict(data)
        # Add predictions to the data
        data["Admission Points"] = predictions
        return data

    def update_model(self, data):
        
        # Drop rows with null values in Admission Points
        data = data.dropna(subset=['Admission Points'])

        # Creación de la variable objetivo y de las variables explicativas
        y = data['Admission Points']
        X = data.drop(['Admission Points'], axis=1)

        self.model.fit(X,y)

        y_pred = self.model.predict(X)

        # Save the model
        dump(self.model, "assets/pipe.joblib")
        metrics = {"R2": self.model.score(X,y), "MSE": mse(y, y_pred), "MAPE": mean_absolute_percentage_error(y, y_pred)}
        return metrics
