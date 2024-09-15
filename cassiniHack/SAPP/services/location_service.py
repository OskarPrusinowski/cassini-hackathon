from datetime import datetime, timedelta
import calendar
import requests
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

def fetch_location_data(lat, lng):
    cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lng,
        "start_date": "2023-01-01",
        "end_date": "2023-12-31",
        "hourly": ["temperature_2m", "rain"]
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_rain = hourly.Variables(1).ValuesAsNumpy()
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31, 23, 59)

    # Generate a list of hourly timestamps
    timestamps = pd.date_range(start=start_date, end=end_date, freq='H')
    hourly_data = {
        "date":timestamps,
        "temperature": hourly_temperature_2m,
        "rain": hourly_rain
    }
    hourly_dataframe = pd.DataFrame(data=hourly_data)


    hourly_dataframe.set_index("date", inplace=True)
    monthly_summary = hourly_dataframe.resample('M').agg({
        'rain': 'sum',
        'temperature': 'mean'
    })

    return monthly_summary



