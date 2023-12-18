
# OpenWeatherMap API Data Pipeline

This project involves building a comprehensive data pipeline that fetches weather data from the OpenWeatherMap API. The pipeline includes preprocessing the data, training a random forest model, and deploying the trained model using FastAPI to create a RESTful API for weather predictions. Apache Airflow is used for orchestrating the entire pipeline, ensuring regular updates from the OpenWeatherMap API.

## Repository Structure

- **/dags**
  - **/scripts**
    - *file_fastapi.py*: FastAPI file
    - *main.py*: Consume the API and update the dataset
    - *random-forest_ML.py*: Dataset Training
  - *weather_dag.py*: Main Apache Airflow DAG configuration file
- **/models**: Directory to store trained machine learning models
- **/data**: Directory to store datasets

## Getting Started

1. **Clone this repository:**

   ```bash
   git clone https://github.com/MouhibMoughtanim/Smart-Irrigation-System-Continuous-Training-Pipeline-with-Apache-Airflow-and-FastApi/
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd Smart-Irrigation-System-Continuous-Training-Pipeline-with-Apache-Airflow-and-FastApi
   ```

3. **Start Docker Containers:**

   ```bash
   docker compose up
   ```

   Upon successful execution, the containers will be launched.
   ![image](https://github.com/MouhibMoughtanim/Smart-Irrigation-System-Continuous-Training-Pipeline-with-Apache-Airflow-and-FastApi/assets/101598112/45272a84-70fe-46ad-b87f-eaf2959e771f)


5. **Access the Airflow UI at `http://localhost:8080` and trigger the DAG.**

# Weather Prediction Service

## Overview

This service provides an API for making weather predictions based on input parameters.

## API Endpoints

### 1. Predict Weather

- **Endpoint:** `POST /predict`
- **Description:** Make weather predictions based on input parameters.
- **Request:**
  - Method: `POST`
  - Headers:
    - `Accept: application/json`
    - `Content-Type: application/json`
  - Body: JSON payload with weather parameters

    ```json
    {
      "Temperature": 25.6,
      "Temp_Min": 20.6,
      "Temp_Max": 30.6,
      "Pressure": 1015.0,
      "Sea_Level": 1020.0,
      "Humidity": 60.0,
      "Wind_Speed": 10.0,
      "Lon": 45.0,
      "Lat": -30.0
    }
    ```

- **Example Request using curl:**

  ```bash
  curl -X POST "http://localhost:8000/predict" -H "Accept: application/json" -H "Content-Type: application/json" -d "{\"Temperature\": 25.6, \"Temp_Min\": 20.6, \"Temp_Max\": 30.6, \"Pressure\": 1015.0, \"Sea_Level\": 1020.0, \"Humidity\": 60.0, \"Wind_Speed\": 10.0, \"Lon\": 45.0, \"Lat\": -30.0}"
  ```

- **Response:**

  - JSON response with weather prediction:

    ```json
    {
      "prediction": 0
    }
    ```

    - **The `prediction` field can have values 0 (no snow or rain) or 1 (snow or rain).**

## Usage

To use this service, send a POST request to the `/predict` endpoint with the required input parameters. The service will respond with the predicted weather information, and the `prediction` field will indicate whether there is snow or rain (1) or not (0).

Feel free to replace the example values in the request payload with your actual weather parameters.
```
