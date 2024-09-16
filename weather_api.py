import requests

API_KEY = "ba430379809d45632fbe4e51200ac5f8"  

def get_real_time_weather(location):
    
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the weather API request
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"  # For Celsius; use "imperial" for Fahrenheit
    }
    
    # Make the GET request to fetch weather data
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"The weather forcast for {location}: is {description}, and {temp}°C"
    else:
        return f"Unable to fetch weather data for {location}: {response.status_code}"
