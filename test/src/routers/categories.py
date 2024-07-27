from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

@router.get("/categories")
def list_categories():
    url = f"{COINGECKO_API_URL}/coins/categories"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()