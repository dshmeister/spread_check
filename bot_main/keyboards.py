from telebot import types
from keyboa.keyboards import keyboa_maker
#from bot_main.vars.variables import  *
from variables import *

"""
Клавиатуры Reply
"""
# keyboardReply  MENU
keyboard_main = types.ReplyKeyboardMarkup()

item1 = types.KeyboardButton(text='Выбрать связку 💵⛓💶')
item2 = types.KeyboardButton(text='Выбрать биржу 💸')
item3 = types.KeyboardButton(text='Установить минимальную сумму 💰')
item4 = types.KeyboardButton(text='Добавить API ‍💻')
item5 = types.KeyboardButton(text='Обменник ‍💱')
item6 = types.KeyboardButton(text='Техническая поддержка ‍🦺')
item7 = types.KeyboardButton(text='Оплатить бота💲')
item8 = types.KeyboardButton(text='Выбрать спред📈')


keyboard_main.row(item1, item2)
keyboard_main.row(item3, item4)
keyboard_main.row(item5, item6)
keyboard_main.row(item7,item8)


""" 
Клавиатуры Inline
"""


#KeyboardInline bundles
param = []
for i in range(len(coins)):
    param.append({coins[i]:coins[i]})


bundles = keyboa_maker(items=[param])
# bundles = keyboa_maker(items=[[{'USDT':'USDT'},{'BTC':'BTC'},{'ETH':'ETH'}]])


#KeyboarfInline tech_support
kb_tech = keyboa_maker(items=[{'Нет, обратиться в техническую поддержку 🦺':'support'}])


# #KeyboardInline usdt_yes_no
# usdt_yes_no = keyboa_maker(items=[{'Добавить RUB/USDT':'usdt_add'}, {'Удалить RUB/USDT':'usdt_del'}])

