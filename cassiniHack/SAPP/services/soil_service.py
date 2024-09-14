from datetime import datetime, timedelta
import calendar
import requests

def fetch_soil_type(lat,lng):
    url=f"https://api-test.openepi.io/soil/type?lon={lng}&lat={lat}&top_k=1"
    print(url)
    response = requests.get(url)
    return response.json()

def get_soil_ph(lat,lng):
    return fetch_soil_type(lat,lng)