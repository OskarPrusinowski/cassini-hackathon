from datetime import datetime, timedelta
import calendar
import requests
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

def fetch_location_data(lat,lng):
    cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lng,
        "start_date": "2023-06-29",
        "end_date": "2023-09-12",
        "hourly": ["temperature_2m", "rain"]
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]

    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_rain = hourly.Variables(1).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}
    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["rain"] = hourly_rain

    hourly_dataframe = pd.DataFrame(data = hourly_data)
    avg_temperature = float(hourly_dataframe["temperature_2m"].mean())
    avg_rain = float(hourly_dataframe["rain"].sum())

    return avg_temperature, avg_rain



