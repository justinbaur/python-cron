import os
import logging
import requests
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

api_url: str = os.getenv("API_URL")
if(api_url is None):
    raise ValueError("API_URL is missing")

name: str = os.getenv("NAME", "justin")

generator_response = requests.get(f"{api_url}/name/generate?category=dragon&limit=1")
dragon_name: str = "bad dragon"

if(200 == generator_response.status_code):
    generator_data = generator_response.json()
    dragon_name = generator_data.get("contents").get("names")[0]

logging.info(f"Welcome, {name}, your dragon name is {dragon_name}")