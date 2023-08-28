import requests

def get_weather_forecast(location):
    api_key = '6d245c2ee8f835556aebf74a3a7fb90f'  # Replace with your OpenWeatherMap API Key
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    params = {
        'units': 'metric'  # Units in Celsius
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        city = data['name']

        print(f"Weather in {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Error fetching weather data. Status Code: {response.status_code}")
        print(data.get('message', ''))
        
if __name__ == "__main__":
    location = input("Enter city name or coordinates: ")
    get_weather_forecast(location)
