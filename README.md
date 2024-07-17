
# Car Price Prediction

This repository contains an API for predicting car prices using a Random Forest Regressor model trained on a Kaggle dataset.

## Overview

The project utilizes a machine learning model to predict car prices. The model is trained on a Kaggle dataset and is deployed via an API for easy access and integration.

## Features

- Car price prediction using Random Forest Regressor
- RESTful API for model inference
- Dockerized for easy deployment

## Getting Started

### Prerequisites

- Docker
- Python 3.x
- pip

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/MatijaMikulic/car-price-prediction.git
   ```
2. Navigate to the project directory:
   ```sh
   cd car-price-prediction
   ```
3. Build the Docker image:
   ```sh
   docker build -t car-price-prediction .
   ```
4. Run the Docker container:
   ```sh
   docker-compose up
   ```

### Usage

The API can be accessed at `http://localhost:5000`. You can make a POST request to the `/predict` endpoint with the necessary car features to get a price prediction.

Example request:
```sh
curl -X POST "http://localhost:5000/predict" -H "Content-Type: application/json" -d '{
  "feature1": value1,
  "feature2": value2,
  ...
}'
```

## Repository Structure

- `app/`: Contains the Flask application code.
- `script/`: Contains scripts for data preprocessing and model training.
- `Dockerfile`: Docker configuration file.
- `compose.yaml`: Docker Compose configuration file.
- `requirements.txt`: Python dependencies.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Kaggle for providing the dataset.
- Open-source community for their support.
