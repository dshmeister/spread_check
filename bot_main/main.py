from bot_token import BOT_TOKEN as token
#import telebot
import telebot
from functions import *
from keyboards import *
#from variables import *

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    '''
    function starts the bot
    '''
    user_id = message.chat.id
    bot.send_message(user_id, f"Приветствую, {message.from_user.first_name}! ✌", reply_markup=keyboard_main)
    bot.send_message(user_id, welcome_message)

    if check_user_new(user_id) == True:
        add_user_to_db(user_id)


@bot.message_handler(commands=['pay'])
def payment_check(message):
    """
    function checks
    """
    user_id = message.chat.id
    if check_payment_actual(user_id) == True:
        bot.send_message(user_id, f'Ваша подписка актуальна. Она действует до {check_date_of_actuality_payment(user_id, mode=1)}')
    else:
        bot.send_message(user_id, f'У вас нет подписки или ее срок действия истек')
    payment(message)


def payment(message):
    """
    function that recieve payment from user
    """
    pass


@bot.message_handler(commands=['exchanger'])
def exchanger(message):
    """
    function gives user contacts of exchanger
    """
    bot.send_message(message.chat.id, exchanger_message)

    
@bot.message_handler(commands=['spread'])
def add_spread(message):
    """
    function that checks spread
    """
    bot.send_message(message.chat.id, 'У вас установлен минимальный спред: <b>'+str(check_spread(message.chat.id))+'</b>', parse_mode='html')
    msg = bot.send_message(message.chat.id, 'Введите спред, который хотите установить')
    bot.register_next_step_handler(msg, set_spread)


@bot.message_handler(commands=['bundle'])
def choose_bundle(message):
    """
    function of choosing bundles
    """
    bund = check_user_bundle(message.chat.id)[1:-1]
    if bund == 'None':
        bot.send_message(message.chat.id, 'Выберите пару из списка доступных:', reply_markup=bundles)
    else:
        bot.send_message(message.chat.id, f'Выбранные пары: {bund}')
        bot.send_message(message.chat.id, f'Выберите какую пару удалить или добавить: ', reply_markup=bundles)


@bot.callback_query_handler(func=lambda call: call.data in coins)
def token(call):
    """
    function allows user to add or delete bundle
    """
    resp = add_del_bundle(call.message.chat.id, 'RUB/'+ call.data)
    if resp == 'del':
        bot.send_message(call.message.chat.id, 'Связка <b>RUB/'+call.data+'</b> удалена.', parse_mode="html")
    else:
        bot.send_message(call.message.chat.id, 'Связка <b>RUB/'+call.data+'</b> успешно добавлена.', parse_mode="html")
    choose_bundle(call.message)



@bot.message_handler(commands=['exchange'])
def choose_exchange(message):
    """
    function of choosing exchanges
    """
    pass



def check_actual_api(message):
    """
    function checks which APIs are added to bot
    """
    pass


@bot.message_handler(commands=['minsum'])
def choose_min_sum(message):
    """
    function of choosing min_sum
    """
    bot.send_message(message.chat.id, 'У вас установлена минимальная сумма ордера: <b>'+str(check_min_sum(message.chat.id))+'</b>', parse_mode='html')
    bot.send_message(message.chat.id, 'Введите мининмальную сумму ордера, которую хотите установить')


def choose_min_sum_again(message):
    """
    function of choosing min_sum
    """
    bot.send_message(message.chat.id, 'У вас установлена минимальная сумма ордера: <b>'+str(check_min_sum(message.chat.id))+'</b>', parse_mode='html')
    bot.send_message(message.chat.id, 'Введите сумму еще раз, если хотите ее изменить')


def set_min_sum(message):
    """
    function checks sets the min_sum
    """
    set_min_sum_db(message.chat.id, message.text)
    choose_min_sum_again(message)
    
def set_spread(message):
    """
    function that adds spread to db
    """
    adding_spread(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Ваш спред успешно установлен!')


    
def set_spread_again(message):
    """
    function that checks spread
    """
    bot.send_message(message.chat.id, 'У вас установлен минимальный спред: <b>'+str(check_spread(message.chat.id))+'</b>', parse_mode='html')
    bot.send_message(message.chat.id, 'Введите спред, который хотите установить')



@bot.message_handler(commands=['api'])
def add_api(message):
    """
    function adds APIs
    """
    pass


def actual_exchanges(message):
    """
    function checks what exchanges are in work
    """
    pass


@bot.message_handler(commands=['support_FAQ'])
def tech_support_FAQ(message):
    """
    function gives gives file FAQ
    """
    bot.send_message(message.chat.id, 'https://telegra.ph/FAQ-C4Crypto-bot-11-22')
    bot.send_message(message.chat.id, 'Нашли в файле ответ на свой вопрос?', reply_markup=kb_tech)
    pass


@bot.callback_query_handler(func=lambda call: call.data == 'support')
# @bot.message_handler(commands=['support'])
def tech_support(call):
    """
    function gives contacts of technical supports
    """
    bot.send_message(call.message.chat.id, tech_sup_message)



@bot.message_handler(content_types=['text'])
def message_reply(message):
    """
    function checks messages, and sends user to needed func
    """
    # bot.send_message(message.chat.id, "&&&&&&")
    if message.text == 'Выбрать связку 💵⛓💶':
        choose_bundle(message)
    elif message.text == 'Выбрать биржу 💸':
        choose_exchange(message)
    elif message.text == 'Установить минимальную сумму 💰':
        choose_min_sum(message)
    elif message.text == 'Добавить API ‍💻':
        add_api(message)
    elif message.text == 'Обменник ‍💱':
        exchanger(message)
    elif message.text == 'Техническая поддержка ‍🦺':
        tech_support_FAQ(message)
    elif message.text == 'Выбрать спред📈':
        add_spread(message)
    elif message.text.isdigit() == True:
        set_min_sum(message)
    elif message.text.isdigit() == True and int(message.text) <= 1:
        set_spread(message)



if __name__ == "__main__":
    bot.infinity_polling()

