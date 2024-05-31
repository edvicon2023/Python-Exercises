# Exercise 8: Weather Information Fetcher

import requests

def fetch_weather(city):
    api_key = 'your_api_key_here'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    
    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']
        
        print(f"Temperature: {temperature}")
        print(f"Pressure: {pressure}")
        print(f"Humidity: {humidity}")
        print(f"Weather description: {description}")
    else:
        print("City not found.")

# Example usage
city_name = input("Enter city name: ")
fetch_weather(city_name)
