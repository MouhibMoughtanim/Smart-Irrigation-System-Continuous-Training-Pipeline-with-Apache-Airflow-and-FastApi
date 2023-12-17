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


