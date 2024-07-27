import pytest
from fastapi.testclient import TestClient
from main import app
import os

# Set up the test client
client = TestClient(app)

# Environment variables for testing
os.environ["BASIC_AUTH_USERNAME"] = "testuser"
os.environ["BASIC_AUTH_PASSWORD"] = "testpass"

def get_auth_headers(username: str = "testuser", password: str = "testpass"):
    return {
        "Authorization": f"Basic {username}:{password}"
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
    coin_id = "bitcoin"  # Use a valid coin_id for testing
    response = client.get(f"/coins/{coin_id}", headers=get_auth_headers())
    assert response.status_code == 200
    # Further checks can be made based on the expected response structure

def test_authentication_failed():
    response = client.get("/categories", headers={})
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}
