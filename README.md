# WeatherWise
 A comprehensive weather app for informed decision-making.
WeatherWise: A Django Weather App with Bootstrap

WeatherWise is a web application built with Django and Bootstrap that provides real-time weather information for various locations worldwide.
Features

    Real-time weather data: Get current temperature, humidity, wind speed, and UV index.
    Detailed forecasts: View hourly and daily forecasts for the next few days.
    Weather alerts: Receive notifications about severe weather warnings.
    Location search: Search for weather information by city name or zip code.
    Customizable interface: Choose from a variety of themes and layouts.

Technologies

    Backend: Django (Python web framework)
    Frontend: Bootstrap (HTML, CSS, JavaScript framework)
    API: OpenWeatherMap API

Installation

    Clone the repository:

Bash

git clone https://github.com/Kasweka1/WeatherWise.git

Use code with caution. Learn more

    Install the required Python libraries:

Bash

pip install -r requirements.txt

Use code with caution. Learn more

    Set up the environment variables:

Bash

cp .env.example .env

Use code with caution. Learn more

Edit the .env file with your OpenWeatherMap API key.

    Migrate the database:

Bash

python manage.py migrate

Use code with caution. Learn more

    Run the server:

Bash

python manage.py runserver

Use code with caution. Learn more
Usage

    Visit http://localhost:8000 in your web browser.
    Enter a city name or zip code in the search bar.
    Click the "Search" button.
    View the current weather conditions and forecast for the selected location.

Contributing

Feel free to contribute to the project by creating pull requests with improvements or bug fixes. Make sure to follow the code style guidelines and contribute tests for your changes.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
