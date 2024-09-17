import requests

url = 'http://api.weatherapi.com/v1/current.json?key=4586f4d00dmsh1ae8ec9a164bc06p1a0644jsnf02ff2bc57ed&q=Orlando&aqi=no'
response = requests.get(url)
weather_json = response.json()

print(weather_json)


