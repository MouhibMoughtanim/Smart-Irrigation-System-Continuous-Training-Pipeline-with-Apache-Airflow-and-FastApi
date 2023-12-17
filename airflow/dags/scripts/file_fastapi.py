from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle 
import numpy as np
import uvicorn

app = FastAPI()

# Load the Random Forest model from the joblib file
with open('/opt/airflow/dags/scripts/random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

class PredictionRequest(BaseModel):
    # Define the input features required for prediction
    Temperature: float
    Temp_Min: float
    Temp_Max: float
    Pressure: float
    Sea_Level: float
    Humidity: float
    Wind_Speed: float
    Lon: float
    Lat: float

@app.post("/predict")
async def predict(data: PredictionRequest):
    # Convert input data to a numpy array for prediction
    input_data = np.array([[data.Temperature, data.Temp_Min, data.Temp_Max,
                            data.Pressure, data.Sea_Level, data.Humidity,
                            data.Wind_Speed, data.Lon, data.Lat]])
    
    # Make prediction using the loaded model
    prediction = model.predict(input_data)
    
    # Return the prediction as a JSON response
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
