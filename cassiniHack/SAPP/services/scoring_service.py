def calculate_score(value, min_value, max_value,factor=2):
    if min_value <= value and  value <= max_value:
        return 100
    elif value < min_value:
        deviation = min_value - value
        return max(0, 100 -  (deviation ** factor))
    else:
        deviation = value - max_value
        return max(0, 100 -  (deviation ** factor))

def rank_grains_for_location(location, grains):
    grain_rankings = []
    
    for grain in grains:
        messages = []
        temp_score = calculate_score(location['temperature'], grain.min_temp, grain.max_temp)
        
        if location['temperature'] < grain.min_temp:
            message = f"Temperatura jest za niska. Minimalna: {grain.min_temp}, aktualna: {round(location['temperature'],2)}"
            messages.append(message)
        elif location['temperature'] > grain.max_temp:
            message = f"Temperatura jest za wysoka. Maksymalna: {grain.max_temp}, aktualna: {round(location['temperature'],2)}"
            messages.append(message)

        rainfall_score = calculate_score(location['rainfall'], grain.min_rainfall, grain.max_rainfall)
        
        if location['rainfall'] < grain.min_rainfall:
            message = f"Sumy opadów są za niskie. Minimalne: {grain.min_rainfall}, aktualne: {round(location['rainfall'],2)}"
            messages.append(message)
        elif location['rainfall'] > grain.max_rainfall:
            message = f"Sumy opadów są za wysokie. Maksymalne: {grain.max_rainfall}, aktualne: {round(location['rainfall'],2)}"
            messages.append(message)

        ph_score = calculate_score(location['soil_ph'], grain.min_ph_soil, grain.max_ph_soil)
        
        if location['soil_ph'] < grain.min_ph_soil:
            message = f"Ph gleby jest za niskie. Minimalne: {grain.min_ph_soil}, aktualne: {location['soil_ph']}"
            messages.append(message)
        elif location['soil_ph'] > grain.max_ph_soil:
            message = f"Ph gleby jest za wysokie. Maksymalne: {grain.max_ph_soil}, aktualne: {location['soil_ph']}"
            messages.append(message)

        total_score = (temp_score * 0.4) + (rainfall_score * 0.4) + (ph_score * 0.2)
        
        grain_rankings.append({
            "grain": grain.name,
            "score": total_score,
            "messages": messages
        })
    
    grain_rankings.sort(key=lambda x: x['score'], reverse=True)
    
    return grain_rankings