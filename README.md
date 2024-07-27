# Cryptocurrency Market Updates API

## Overview:

This project is a FastAPI-based HTTP REST API that fetches cryptocurrency market updates from the CoinGecko API. The application provides various endpoints to list coins, coin categories, and specific coin details with market data against the Canadian Dollar (CAD). It is designed with authentication, comprehensive documentation, unit tests, and is dockerized for easy deployment.

## Features
List all coins including coin ID.
List coin categories.
List specific coins according to ID or category.
Pagination support.
Authentication using HTTP Basic Authentication.
Health check and version information endpoints.
Dockerized setup for containerized deployment.
Integrated linting and quality control.


## Create and activate a virtual environment:
```
python3 -m venv venv
venv/Scripts/activate
```
## Install dependencies:
```
pip install fastapi uvicorn requests

pip install -r requirements.txt
```

## Set up environment variables:
```
COINGECKO_API_KEY=<your_coingecko_api_key>
BASIC_AUTH_USERNAME=test
BASIC_AUTH_PASSWORD=test
```

## Running the Application:
```
uvicorn src.main:app --reload
```

## API Endpoints:
1. List all coins
Endpoint: GET /coins
2. List coin categories
Endpoint: GET /categories
3. List specific coins
Endpoint: GET /coins/{coin_id}

## Authentication
This application uses HTTP Basic Authentication. You need to provide the correct username and password to access the endpoints.

## Testing:
```
pytest
```
My Response: 7 items collected and 7 passed.

## Docker
```
docker build -t crypto-api .
docker run -p 8000:8000 coin-api
```
## Conclusion
This project is designed to provide an easy and efficient way to fetch and display cryptocurrency market updates. With proper authentication, documentation, and testing, it ensures reliability and security. The dockerized setup makes it easy to deploy and run the application in any environment.
