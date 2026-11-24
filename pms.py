import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("PMS_URL")
API_KEY = os.getenv("PMS_API_KEY")

print("BASE_URL =", BASE_URL)
print("API_KEY =", API_KEY)

def get_tasks():
    url = f"{BASE_URL}/api/v3/time_entries?pageSize=2"

    response = requests.get(
        url,
        auth=("apikey", API_KEY)
    )

    return response.json()