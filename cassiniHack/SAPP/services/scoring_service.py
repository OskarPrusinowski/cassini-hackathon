from django.db.models import Q,Avg
from SAPP.models import SeedPrice
from datetime import datetime, timedelta



def get_prices_for_end_month(grain):
    # Define the start and end dates for the end month
    current_year = datetime.now().year
    start_date = datetime(current_year, grain.stop_month, 1)
    # Use the last day of the month
    end_date = (start_date.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
    
    # Query for prices in the given month
    prices = SeedPrice.objects.filter(
        seed=grain,
        date__range=[start_date, end_date]
    )
    
    average_price = prices.aggregate(Avg('price'))['price__avg']
    
    return average_price

def calculate_score(value, min_value, max_value,factor=2):
    if min_value <= value and  value <= max_value:
        return 100
    elif value < min_value:
        deviation = min_value - value
        return max(0, 100 -  (deviation ** factor))
    else:
        deviation = value - max_value
        return max(0, 100 -  (deviation ** factor))

def calculate_average(values, start_month, stop_month):
    return sum(values[start_month-1:stop_month]) / (stop_month - start_month + 1)

def rank_grains_for_location(location, grains):
    grain_rankings = []
    
    weights = {
        'temperature': 0.4,
        'rainfall': 0.4,
        'soil_ph': 0.2
    }
    for grain in grains:
        messages = []
        
        avg_temp = calculate_average(location['temperature'], grain.start_month, grain.stop_month)
        avg_rainfall = calculate_average(location['rain'], grain.start_month, grain.stop_month)
        
        temp_score = calculate_score(avg_temp, grain.min_temp, grain.max_temp)
        
        if avg_temp < grain.min_temp:
            message = f"Temperatura jest za niska. Minimalna: {grain.min_temp}, aktualna: {round(avg_temp,2)}"
            messages.append(message)
        elif avg_temp > grain.max_temp:
            message = f"Temperatura jest za wysoka. Maksymalna: {grain.max_temp}, aktualna: {round(avg_temp,2)}"
            messages.append(message)

        rainfall_score = calculate_score(avg_rainfall, grain.min_rainfall, grain.max_rainfall)
        
        if avg_rainfall < grain.min_rainfall:
            message = f"Sumy opadów są za niskie. Minimalne: {grain.min_rainfall}, aktualne: {round(avg_rainfall,2)}"
            messages.append(message)
        elif avg_rainfall > grain.max_rainfall:
            message = f"Sumy opadów są za wysokie. Maksymalne: {grain.max_rainfall}, aktualne: {round(avg_rainfall,2)}"
            messages.append(message)

        ph_score = calculate_score(location['soil_ph'], grain.min_ph_soil, grain.max_ph_soil)
        
        if location['soil_ph'] < grain.min_ph_soil:
            message = f"Ph gleby jest za niskie. Minimalne: {grain.min_ph_soil}, aktualne: {location['soil_ph']}"
            messages.append(message)
        elif location['soil_ph'] > grain.max_ph_soil:
            message = f"Ph gleby jest za wysokie. Maksymalne: {grain.max_ph_soil}, aktualne: {location['soil_ph']}"
            messages.append(message)

        total_score = ((temp_score * weights['temperature']+0.1) *
                      (0.1 + rainfall_score * weights['rainfall']) *
                      (ph_score * weights['soil_ph']+0.1))
        
        diff_ha = grain.max_t_ha - grain.min_t_ha
        sum_t_ha =  grain.min_t_ha + ((total_score/100)*diff_ha)
        sum_t_ha =  float(sum_t_ha)
        price_end_month = get_prices_for_end_month(grain)
        price = round(price_end_month if price_end_month else 0,2)
        price_as_float = float(price)
        sum_price = round(sum_t_ha*price_as_float,2)
        print(total_score)

        grain_rankings.append({
            "grain": grain.name,
            "score": total_score,
            "messages": messages,
            "avg_temp": avg_temp,
            "avg_rainfall": avg_rainfall,
            "sum_price":sum_price
        })
        print(grain_rankings)


    
    grain_rankings.sort(key=lambda x: x['score'], reverse=True)
    
    return grain_rankings