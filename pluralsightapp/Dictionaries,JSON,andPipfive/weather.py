import requests

url = 'http://api.weatherapi.com/v1/current.json?key=a6952c0015cdc9c7403395a4e52d4608&q=Orlando&aqi=no'
response = requests.get(url)
weather_json = response.json()

print(weather_json)


