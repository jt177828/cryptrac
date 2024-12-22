import requests
import os
from dotenv import load_dotenv

COINAPI_KEY = os.getenv("COINAPI_KEY")
BASE_URL = "https://rest.coinapi.io/v1/exchangerate/"

def fetch_crypto_prices(base_currency, quote_currency):
    """
    Fetches a cryptocurrency price.
    
    :param base_currency: Cryptocurrency symbol (e.g., BTC)
    :param quote_currency: Quote currency symbol (e.g., USD)
    :return: A dictionary with price data or an error message
    """

    url = f"{BASE_URL}/{base_currency}/{quote_currency}"

    payload = {}
    header = {
        'Accept': 'text/plain',
        'X-CoinAPI-Key': COINAPI_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return {
            "base_currency": data["asset_id_base"],
            "quote_currency": data["asset_id_quote"],
            "rate": data["rate"],
            "time": data["time"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}