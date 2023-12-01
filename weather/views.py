import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.


def home(request):
    # Check for search term in GET parameters
    search_term = request.GET.get('search')

    # Make API request with search term if provided
    if search_term:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=2d6ff54dc1bbff70b99f638b9d61dbc6".format(search_term)
    else:
        url = "https://api.openweathermap.org/data/2.5/weather?q=London,UK&units=metric&appid=2d6ff54dc1bbff70b99f638b9d61dbc6"

    response = requests.get(url)
    data = response.json()

    # Check if API request was successful
    if response.status_code == 200:
        context = {
            'city': data['name'],
            'temperature': round(data['main']['temp']),
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'wind_speed': round(data['wind']['speed']),  # Wind speed in meters per second
            'wind_direction': data['wind']['deg'],
        }
        return render(request, 'weather/weather.html', context)
    else:
        # Handle error response from API
        if response.status_code == 404:
            error_message = "City not found: {}".format(search_term)
        else:
            error_message = "Error retrieving weather data"

        context = {'error_message': error_message}
        return render(request, 'weather/error.html', context)

