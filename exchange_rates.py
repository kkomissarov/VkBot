import requests

api_key = 'f4ff557c4e642de08cb03d19c0cb4f66' #ключ авторизации api



#формируем адрес запроса
url = 'http://data.fixer.io/api/latest?access_key=' + api_key

def get_rates(url):
    jsonrates = requests.get(url)
    rates = jsonrates.json()
    return rates


all_currency = get_rates(url)['rates'] #все курсы в одном dict


eur_to_rub = all_currency['RUB']
eur_to_gel = all_currency['GEL']
gel_to_rub = eur_to_rub / eur_to_gel

