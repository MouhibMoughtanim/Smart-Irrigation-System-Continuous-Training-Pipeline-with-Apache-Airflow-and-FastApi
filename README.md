# OpenWeatherMap API Data Pipeline

This project entails creating a comprehensive data pipeline that fetches weather data from the OpenWeatherMap API, conducts preprocessing on the data, utilizes a random forest model for training, and finally deploys the trained model using FastAPI to create a RESTful API for consumption. The orchestration of the entire pipeline is managed through Apache Airflow, ensuring regular updates are seamlessly incorporated from the OpenWeatherMap API.

## Repository Structure

- `/dags`
  - `/scripts`
    - `file_fastapi.py` : FastAPI file
    - `main.py ` : Consume the api and update the dataset
    - `random-forest_ML.py` : Dataset Training
  - `weather_dag.py` : Main Apache Airflow DAG configuration file
- `/models` : Directory to store trained machine learning models
- `/data ` : Directory to store datasets

## Getting Started

1. Clone this repository:

   
      ```bash
      
      git clone https://github.com/MouhibMoughtanim/Smart-Irrigation-System-Continuous-Training-Pipeline-with-Apache-Airflow-and-FastApi/
      
     ```


2. Navigate to the Project Directory:


   ```bash

    cd Smart-Irrigation-System-Continuous-Training-Pipeline-with-Apache-Airflow-and-FastApi

   ```
   
3. Start Docker Containers:

   ```bash
   docker compose up
   ```
   ### Upon successful execution, the containers will be launched. Here is the expected outcome:
   
![image](https://github.com/MouhibMoughtanim/Smart-Irrigation-System-Continuous-Training-Pipeline-with-Apache-Airflow-and-FastApi/assets/101598112/8af1eef8-2ac4-4721-93b9-3e5c8300f476)


5. Access the Airflow UI at `http://localhost:8080` and trigger the DAG.
   

