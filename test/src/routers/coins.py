from fastapi import APIRouter, HTTPException, Query
import requests
import os

router = APIRouter()

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

@router.get("/coins")
def list_coins(page_num: int = 1, per_page: int = 10):
    url = f"{COINGECKO_API_URL}/coins/markets"
    params = {
        "vs_currency": "cad",
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": page_num,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.get("/coins/{coin_id}")
def get_coin_details(coin_id: str):
    url = f"{COINGECKO_API_URL}/coins/{coin_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()