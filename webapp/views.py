from django.shortcuts import render , redirect
from geopy.geocoders import Nominatim
import requests, json
from django.conf import settings
from django.contrib import messages
from.models import *
from django.contrib.gis.geos import Point

weather_api_key = settings.WEATHER_API_KEY

def home(request):
    weather_obj = Weather.objects.all().last()
    if request.method == 'POST':
        city_name       = request.POST.get("city_name")
        base_url        = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url    = base_url + "appid=" + weather_api_key + "&q=" + city_name
        response        = requests.get(complete_url)
        output          = response.json()
        if output["cod"] != "404":
            main_output         = output["main"]
            kelvin_temperature = main_output["temp"]
            current_humidity    = main_output["humidity"]
            print("Temperature (in kelvin unit) :",str(kelvin_temperature),"\nhumidity (in percentage):",str(current_humidity))

            # Find latitude and longitude by city name

            geolocator          = Nominatim(user_agent='myapplication')
            location            = geolocator.geocode(city_name)
            latitude            = location.raw['lat']
            longitude           = location.raw['lon']
            point_location      = Point(float(longitude), float(latitude), srid=4326)
            celcisus_temp = kelvin_temperature - 273.15
            weather_obj     = Weather.objects.create(
                city_name   = city_name,
                latitude    = latitude,
                longitude   = longitude,
                temperature = celcisus_temp,
                humidity    = current_humidity,
                location    = point_location
            )

            context = {
                "latitude":latitude,
                "longitude":longitude,
                "celcisus_temp":celcisus_temp,
                "current_humidity":current_humidity
            }
            return render(request,'home.html',context)
        else:
            messages.warning(request, "Opps ! City Not Found.")
            return redirect("/")
    context = {
        "latitude": weather_obj.latitude,
        "longitude": weather_obj.longitude,
        "celcisus_temp": weather_obj.temperature,
        "current_humidity": weather_obj.humidity
    }
    return render(request,'home.html',context)