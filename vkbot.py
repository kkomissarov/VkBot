import vk_api
from days_count import days_count
from weather import temp, status
from exchange_rates import gel_to_rub

vk = vk_api.VkApi(login = '', password = '')
vk.auth()

#Отправка сообщений в личку
def send_mesage(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

#Отправка сообщений в чат
def send_mesage_to_chat(message, chat):
    vk.method('messages.send', {'message': message, 'chat_id': chat})


#Список id кому отправлять сообщения
id_list = [
	
]

#Словоформы слов в предложении :(
if str(days_count)[-1] == '1' and str(days_count) != '11':
    days = 'день'

elif str(days_count)[-1] in ('4', '3', '2') and str(days_count) not in ('14', '13', '12'):
    days = 'дня'

else:
    days = 'дней'


msg = '✈✈✈✈✈✈✈\n\nГамарджоба, генацвале!\n \n📅 До Грузии осталось: ' + str(days_count) + ' ' + days + '!\n\n☀ Сейчас в Тбилиси ' + str(temp) + '°C' + ', ' + status + '.\n\n💰 10 лари - это ' + str(round(gel_to_rub * 10, 2)) + ' руб.'



if __name__ == '__main__':
    for id in id_list:
        send_mesage(id, msg)


