from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from SAPP.services.soil_service import fetch_soil_type

@csrf_exempt
def welcome(request): 
    if request.method == 'POST':
        print("POST")
        print(request.POST)
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        
        soil_data = fetch_soil_type(lat,lng)
        ph = 7
        temp = 20
        rain = 200
        print(soil_data)

        items =[
            {'name':'Żyto','score':'100','description':"Przykładowy opis"},
            {'name':'Ryż','score':'80','description':"Przykładowy opis ryżu"},
            {'name':'Ziemniak','score':'20','description':"Przykładowy opis ziemniaka"},
                ]


        return render(request, 'newpages/welcome.html',context={items})
    else:
        print("GETTT")
        return render(request, 'newpages/welcome.html')




    