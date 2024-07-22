import requests

API_KEY = '8cb4c9ea658f92d0269af583b79b3cb1'
API_URL = "https://api.openweathermap.org/data/2.5/weather"
print (f"they Api key: {API_KEY}")
def get_weather (city):
    req_url = f"{API_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(req_url)
    data = response.json()

    weather = {
        'city' : data['name'],
        'temprature' : data['main']['temp'],
        'humidity' : data['main']['humidity'],
        'description' : data['weather'][0]['description']
    }
    print(weather)

get_weather('sacramento')