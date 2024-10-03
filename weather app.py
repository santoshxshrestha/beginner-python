import requests
api_key = '08f05e346ce847f630cc2a04c0a464d6'
city = input("Enter the name of city: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {city} is: {weather}")
    print(f"The temperature in {city} is: {temp}ºF")