from datetime import datetime, timedelta
import calendar
import requests
from SAPP.models import Soil

def fetch_soil_type(lat,lng):
    url=f"https://api-test.openepi.io/soil/type?lon={lng}&lat={lat}&top_k=1"
    response = requests.get(url)
    return response.json()

def get_soil_ph(lat,lng):
    soil_data = fetch_soil_type(lat,lng)
    try:
        print(soil_data)
        soil_name = soil_data['properties']['most_probable_soil_type']

        soil = Soil.objects.get(name__iexact=soil_name)
        return soil.min_ph, soil.max_ph  
    except Soil.DoesNotExist:
        return None
    except Exception:
        return None