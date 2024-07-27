import sys
import os
from dotenv import load_dotenv
import pytest
from fastapi.testclient import TestClient

# Load environment variables from .env file
load_dotenv()

# Add the src directory to the path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from main import app

# Set up the test client
client = TestClient(app)

def get_auth_headers(username: str = os.getenv("BASIC_AUTH_USERNAME"), password: str = os.getenv("BASIC_AUTH_PASSWORD")):
    import base64
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()
    return {
        "Authorization": f"Basic {encoded_credentials}"
    }

def test_read_root():
    response = client.get("/", headers=get_auth_headers())
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_health_check():
    response = client.get("/health", headers=get_auth_headers())
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_version_info():
    response = client.get("/version", headers=get_auth_headers())
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_list_categories():
    response = client.get("/categories", headers=get_auth_headers())
    assert response.status_code == 200
    # Further checks can be made based on the expected response structure

def test_list_coins():
    response = client.get("/coins", headers=get_auth_headers(), params={"page_num": 1, "per_page": 10})
    assert response.status_code == 200
    # Further checks can be made based on the expected response structure

def test_get_coin_details():
    coin_id = "bitcoin"  # Replace with a valid coin_id for testing
    response = client.get(f"/coins/{coin_id}", headers=get_auth_headers())
    assert response.status_code == 200
    # Further checks can be made based on the expected response structure

def test_authentication_failed():
    response = client.get("/categories", headers={})
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
