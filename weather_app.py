import requests 

def get_weather(city, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = (f"{base_url}q={city}&appid={api_key}&units=metric")
    response = requests.get(complete_url)
    weather_data = response.json()
    

    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        pressure = main_data["pressure"]

        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather Description: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
    else:
        print(f"City {city} not found!")

if __name__ == "__main__":
    api_key = '08f05e346ce847f630cc2a04c0a464d6'
    city = input("Enter your city name: ")
    get_weather(city, api_key)

