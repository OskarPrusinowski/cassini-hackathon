from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from SAPP.services.soil_service import get_soil_ph
from SAPP.services.seeds_service import list_seeds
from SAPP.services.location_service import fetch_location_data
from SAPP.services.scoring_service import rank_grains_for_location

@csrf_exempt
def welcome(request): 
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        
        soil_data = get_soil_ph(lat,lng)
        seeds = list_seeds()

        list_temp = fetch_location_data(lat,lng)
        location ={'temperature':list_temp['temperature'],
                   'rain':list_temp['rain'],
                   "soil_ph":(soil_data[0]+soil_data[1])/2
                #    "soil_ph":3
                   }

        ranking = rank_grains_for_location(location,seeds)

        context = {
            'ranking': ranking
        }
        return render(request, 'newpages/welcome.html',context)
    else:
        return render(request, 'newpages/welcome.html')




    