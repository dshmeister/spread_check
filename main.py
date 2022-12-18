import time
from bot_token import BOT_TOKEN as token
from bin_token import *
import telebot
import requests
from gar_tokens import *
from functions import *
from variables import *
from keyboa.keyboards import keyboa_maker
from keyboards import *


bot = telebot.TeleBot(token)
t = 1  # [t] - seconds

print()

if __name__ == '__main__':
    while True:
        time.sleep(t)
        # написать ловушку на ошибку KeyError: 'asks', с авоматическим обновлением jwt_token'а
        ret_gar_usdt = requests.get('https://garantex.io/api/v2/depth', headers={'Authorization': 'Bearer ' + jwt_token},
                                    data={'market': 'usdtrub'})
        # print(ret_gar_usdt.json())

        best_gar_sell_usdt = ret_gar_usdt.json()['asks'][0]['price'] # asks - мы продаем крипту за руб, bids - покупка крипты за руб
        best_gar_buy_usdt = ret_gar_usdt.json()['bids'][0]['price']

        ret_gar_btc = requests.get('https://garantex.io/api/v2/depth', headers={'Authorization': 'Bearer ' + jwt_token},
                               data={'market': 'btcrub'})
        best_gar_sell_btc = ret_gar_btc.json()['asks'][0]['price'] # asks - мы продаем крипту за руб, bids - покупка крипты за руб
        best_gar_buy_btc = ret_gar_btc.json()['bids'][0]['price']

        ret_gar_eth = requests.get('https://garantex.io/api/v2/depth', headers={'Authorization': 'Bearer ' + jwt_token},
                                   data={'market': 'ethrub'})
        best_gar_sell_eth = ret_gar_eth.json()['asks'][0]['price'] # asks - мы продаем крипту за руб, bids - покупка крипты за руб
        best_gar_buy_eth = ret_gar_eth.json()['bids'][0]['price']


        print('USDT     ', 'sell', best_gar_sell_usdt , 'buy', best_gar_buy_usdt)
        print('BTC     ', 'sell', best_gar_sell_btc , 'buy', best_gar_buy_btc)
        print('ETH     ', 'sell', best_gar_sell_eth, 'buy', best_gar_buy_eth)
        print()
        print()
        print()