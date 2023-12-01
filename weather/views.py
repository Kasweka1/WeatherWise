import requests
from django.shortcuts import render
from datetime import datetime


# Create your views here.


def home(request):
    # Check for search term in GET parameters
    search_term = request.GET.get('search')

    # Make API request with search term if provided
    if search_term:
        url = "https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=2d6ff54dc1bbff70b99f638b9d61dbc6".format(search_term)
            
    else:
        url = "https://api.openweathermap.org/data/2.5/forecast?q=London,UK&units=metric&appid=2d6ff54dc1bbff70b99f638b9d61dbc6"

    response = requests.get(url)
    data = response.json()

    # Current time
    current_time = datetime.now()

    # Convert current time to string
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')

    current_index = -1
    # Find the index of the current time in the list
    for index, item in enumerate(data['list']):
        if item['dt_txt'] == current_time_str:
            current_index = index
            break

    
    forecast_data_list = []

    #extracts the needed data from the api json response
    city = data['city']['name']
    current_date = data['list'][current_index]['dt_txt'].split()[0]
    current_day = datetime.strptime(current_date, '%Y-%m-%d').strftime('%A')
    current_temperature = data['list'][current_index]['main']['temp']
    current_pop = data['list'][current_index]['pop']
    current_wind_speed = data['list'][current_index]['wind']['speed']
    current_wind_direction = data['list'][current_index]['wind']['deg']
    current_humidity = data['list'][current_index]['main']['humidity']

    # context dictionary
    context = {
        'city': city,
        'current_date': current_date,
        'current_day': current_day,
        'current_temperature' : current_temperature,
        'current_pop' : current_pop,
        'current_wind_speed' : current_wind_speed,
        'current_wind_direction' : current_wind_direction,
        'current_humidity' : current_humidity,
    }

    # method that converts wind direction degrees to North East South and West
    def convert_wind_direction(wind_direction):
        if wind_direction >= 0 and wind_direction < 45:
            return "North"
        elif wind_direction >= 45 and wind_direction < 135:
            return "Northeast"
        elif wind_direction >= 135 and wind_direction < 225:
            return "East"
        elif wind_direction >= 225 and wind_direction < 315:
            return "Southeast"
        elif wind_direction >= 315 and wind_direction < 360:
            return "South"


    for index in range(current_index + 8, len(data['list']), 8):
        dt_object = datetime.strptime(data['list'][index]['dt_txt'], '%Y-%m-%d %H:%M:%S')
        forecast_date = dt_object.strftime('%Y-%m-%d')
        forecast_day = dt_object.strftime('%A')
        forecast_temperature = round(data['list'][index]['main']['temp'])
        forecast_pop = data['list'][index]['pop']
        forecast_wind_speed = data['list'][index]['wind']['speed']
        forecast_wind_direction = data['list'][index]['wind']['deg']
        forecast_humidity = data['list'][index]['main']['humidity']

        #converted using method
        converted_wind_direction = convert_wind_direction(forecast_wind_direction)

        forecast_data_list.append({
            'city': city,
            'forecast_date': forecast_date,
            'forecast_day': forecast_day,
            'forecast_temperature': forecast_temperature,
            'forecast_pop': forecast_pop,
            'forecast_wind_speed': forecast_wind_speed,
            'converted_wind_direction': converted_wind_direction,
            'forecast_humidity': forecast_humidity,
            # 'description': data['weather'][0]['description'],
            # 'icon': data['weather'][0]['icon'],
        })
    
    context['forecast_data_list'] = forecast_data_list


    # Check if API request was successful
    if response.status_code == 200:
        return render(request, 'weather/weather.html', context)
        
    else:
        # Handle error response from API
        if response.status_code == 404:
            error_message = "City not found: {}".format(search_term)
        else:
            error_message = "Error retrieving weather data"

        context = {'error_message': error_message}
        return render(request, 'weather/error.html', context)

