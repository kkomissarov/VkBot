import requests


city = 'Tbilisi'                                 #Название города (лучше посмотреть на сервисе нужный)
api_key = 'f0250678fddd837fede2e1f7cb6eb315'     #Выдается при регистрации

#Формируем url
url = 'http://api.openweathermap.org/data/2.5/find?q=' + city + '&type=like&APPID=' + api_key


def get_weather(url):
    ping = requests.get(url, params = {'units': 'metric', 'lang': 'ru'})
    all_weather = ping.json()
    return all_weather



weather = get_weather(url)

temp = weather['list'][0]['main']['temp']
status = weather['list'][0]['weather'][0]['description']