import time
from spread.bot_token import BOT_TOKEN as token
import telebot
import requests
import sqlite3
from spread.test_gar import *
from spread.gar_tokens import *

bot = telebot.TeleBot(token)

#___________________________________GAR_TOKENS____________________________________

#private_key = 'LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcFFJQkFBS0NBUUVBdUMvQWRuWHVWTFNDRHJlSlhpbElCam83aTJqd0I4ZzVSWjZvOGhJcXNNNmprVi9yCkxYbHYvUXh1eEZhMk5LQnJmMVUzc0NPUmROSldHaTFsbGFuenZaZ2ViMHVUUGw4RGZpdHhINHBLNHVPRWx5TDQKWjcvTEd4bWpJMmNGOEN5SkNqT2VkN0g2aGYwTWtrbXNYUHB3em1PS3gyb1ByTWM3SmtXRmlkRTBNaHZBWjJKcgozRVNjTENwVi84M3JuNm8zeHdQSXg3VU4wZDVIVXBRSjhXSGYvSUxxd0pMZnZqV09yYjNvOTVYY3VKaDhIU1JjCnJRTklmZjBPbHZxZmJKWVd5OURra0hvZlVoNFFiTU5HeGwwZnE1OFNELzFuWmFzS21sVENHY0I3OUZVYnVJeDIKOHZGSzk0TVpLTXNRS0VUQ2Q5U0loWVdTdmwxTmFEaWEwZ05icXdJREFRQUJBb0lCQVFDY3hoQjFCR1pyZFFXcQp6ekErbExhNGprSjJwRWlDNXp0UWRmN3BwT3J2ZWNPaUR0blg2Q0NaYkVhd0dmcVhDdURWRGswTFFRc2pPNUdNClVJM0IrVm45VEFqRHhMazlBcFN2aFB5UjB4MXd5Q1hvbXh5QytxNC9qKy9iUjJxM2hzRFNqU05hVUlTa0hjTGcKbFpML3hTL1ZqTWJvZSsrQnFrYy9pVGRrR2t6cVJHRERLL25CMFhwWUR1d0tJQW9IMXVEOHczQlZ5bWw5TzVISQoxWEdUdkU4SGg3TmtRcE9tVGpGaDkzL3lwTTBMUkN1ek1QWTR6SWZWYXlyamg3djRFbjA5SXZielNSREVVejFZCk95OXZOdVJpbDlTV0JCdGZNU1V0UDRSYkdkVEpyS3IrcXJHR0crTk4yamhFS3pFd2NoMmZiTHJIWWtOcjJBL1YKd2JBUzNwTEJBb0dCQU9RU2YzY3VOOWRrWEEycDNhdDB2MGZ3eUxQZWZNMFZLYmZxNVJ1Nm9TVjlIVEIrbnlmcwpvRHNhNHZYNk5MM1FZRVZXSlllOGJla1YrNERyaFNwSHhlbHdqaXozT3dlWVBSTk1hYkpXZzBNM0lvRk9JSVY0CllTZ3Y3RXVoUldGRy8wODE1M0h1ZFRiazkxUnhDeXg4OTRBWnU4K3B4b0RsN1ZtTTM2OGdFZzhoQW9HQkFNNjkKaTNMeXltVG5vWGtadHNHY2pBbVBub1V3aXJYbXZnSmdibXNIeXI1RlRjU0U3N0dYZDF3L0hLTzVaN1pYYzdDNApYd1VRTjlMQ3pJMGFJa3g5SmhsOHBwblpwc0RwQVdVTUFoTUR4TnpkcHVlYXJubUIxL2I1T0p6bDJhRHpWUklaCmYzNGtPTWFWdFRReFNjUVdmWmpib3k2cHRjSlQ0N1V0bnM1VXJFMUxBb0dCQUs0MVB1MisvT0ptZ3pYZ21UUmMKMGJyV3ZjYytXNStlMmFYbEl5bGlEYkwvOVNyVW5TYzJ4RkZCUVRsWDY2OU5HaXY4R0dDczJsdGU4aVBRUW9CQQpJSGttQTBOdmVNUmRVZEdLM1hWZVJaY3k1d1ZUc3QyZ1RMNFFsUEpUOWhYTzBEY2wybXFaRlNsZ0RWZVBuVlJYCkJBbnlIaFlKL1ZqNXg2bE9SSkdVOHBaaEFvR0JBS0FmVUUxRVhKdlFoMURyS0pCR05uUUZSMnF6RVF3WDNkeXIKWVhvR08vSW9iVFlqSEI2NVNKb3F5M3pIVWR0NVdrSnFXalhxdk1IQlhIcUEza1hOdkYrTEd1SVlJRDVUZVdBUQo3OTVZVWZZYXVuV3hhU2IwK1JieEtmYmpVeTZFcU1QdStiN3lRUU1WMnBYRkF2UWIwMFU3LytSWlQweG1ldnZOCmpLMFVDYXVIQW9HQUc3NEJ6Qlh0TmdUN3hkNW5Kc0RKYTlwbkdEL0F5UkpFdStsckl4MTNZYSt2WVFnamViN2cKMm5ud25xcjdhOUt3QUJieGozOWs4aTlNVmNCT1FmVVpDb0NVbTNjMWJwUkUzNDBjVVhmay9mR0k4MXpOSGVMcwppYzh2MUR0Wi9POFRTTHA3QjJhQ2pGZ2w0U3lxUUY5dTMzWmpkVSt0S09WUVA4VThldlRLV1FBPQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQo='
#uid = 'fce93f89-7068-484c-9e5d-06d380a0e94a'
#host = 'garantex.io' # для тестового сервера используйте stage.garantex.biz


#jwt_token= 'eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NzMzNjE4MTcsImV4cCI6MTY3MzQ0ODIxNywic3ViIjoic2Vzc2lvbiIsImlzcyI6ImJhcm9uZyIsImF1ZCI6WyJwZWF0aW8iXSwianRpIjoiNTE0NzlFQzgyRTIxQThCNkQzOUUwRjUzIiwidWlkIjoiSURBQTdBNjc4Q0U4IiwiZW1haWwiOiJnMjJrdXR1a292QGdtYWlsLmNvbSIsInJvbGUiOiJtZW1iZXIiLCJsZXZlbCI6Mywic3RhdGUiOiJhY3RpdmUiLCJhcGlfa2lkIjoiZmNlOTNmODktNzA2OC00ODRjLTllNWQtMDZkMzgwYTBlOTRhIn0.PyIJDwwbaH_VuO849Yu7X8pENd9Iw5TGigame8JTGuFcw9FgzNt67OTsqwWP35zutbE0VXquSo2b5V1TIDK4KIZkALySe7F3q7j4LRtLtP7qqzWURWeN6NrP3QCAZcm24zlKl4i8rJepb3nv_oB19yWhqzaW7Lwx7ipydhLVLQAXIN-xM-9vmdyeEK7405Xu0RVHiIPU1FOwQfdFSbn0eq_0dnxaLrFR3hOV5HMn9TbajZBBRBwJDXvYZJcdIzA3CplV5odKvWKdFaF6bNMUsMMOV4cgIMhBgVnLvBlHYCylF3kT8EWrzJVcl5PKfugk2X8CcnfNOq0uBE4ywwj6SQ'
#jwt_token = gen_gar_token()

#_________________________________________________________________________________






def count_spread_usdt(gar_buy,gar_sell,bin_buy,bin_sell):
    spread1, spread2 = (float(gar_sell) - float(bin_buy)) / float(gar_sell), (float(bin_sell) - float(gar_buy)) / float(bin_sell)
    if spread1 > spread2:
        return 'Binance', spread1, float(bin_buy)
    else:
        return 'Garantex', spread2, float(gar_buy)
def count_spread_btc(gar_buy,gar_sell,bin_buy,bin_sell):
    spread1, spread2 = (float(gar_sell) - float(bin_buy)) / float(gar_sell), (float(bin_sell) - float(gar_buy)) / float(bin_sell)
    if spread1 > spread2:
        return 'Binance', spread1, float(bin_buy)
    else:
        return 'Garantex', spread2, float(gar_buy)
def count_spread_eth(gar_buy,gar_sell,bin_buy,bin_sell):
    spread1, spread2 = (float(gar_sell) - float(bin_buy)) / float(gar_sell), (float(bin_sell) - float(gar_buy)) / float(bin_sell)
    if spread1 > spread2:
        return 'Binance', spread1, float(bin_buy)
    else:
        return 'Garantex', spread2, float(gar_buy)

def check_spread_usdt(spread):
    db = sqlite3.connect('C:/users/dshme/Desktop/spread_check/bot_main/users.db')
    c = db.cursor()
    c.execute(f"SELECT user_id FROM users WHERE spread < {spread}")
    return c.fetchall()



def check_spread_btc(spread):
    db = sqlite3.connect('C:/users/dshme/Desktop/spread_check/bot_main/users.db')
    c = db.cursor()
    c.execute(f"SELECT user_id FROM users WHERE spread < {spread}")
    return c.fetchall()

def check_spread_eth(spread):
    db = sqlite3.connect('C:/users/dshme/Desktop/spread_check/bot_main/users.db')
    c = db.cursor()
    c.execute(f"SELECT user_id FROM users WHERE spread < {spread}")
    return c.fetchall()



def gar_usdt():
    """
    returns sell_usdt, buy_usdt
    """
    # написать ловушку на ошибку KeyError: 'asks', с авоматическим обновлением jwt_token'а
    ret_gar_usdt = requests.get('https://garantex.io/api/v2/depth', headers={'Authorization': 'Bearer ' + jwt_token},
                                data={'market': 'usdtrub'})

    # print(ret_gar_usdt.json())

    best_gar_sell_usdt = ret_gar_usdt.json()['asks'][0]['price']  # asks - мы продаем крипту за руб, bids - покупка крипты за руб
    best_gar_buy_usdt = ret_gar_usdt.json()['bids'][0]['price']

    return best_gar_sell_usdt, best_gar_buy_usdt


def gar_btc():
    """
    returns sell_bin, buy_bin
    """
    ret_gar_btc = requests.get('https://garantex.io/api/v2/depth', headers={'Authorization': 'Bearer ' + jwt_token},
                               data={'market': 'btcrub'})
    best_gar_sell_btc = ret_gar_btc.json()['asks'][0][
        'price']  # asks - мы продаем крипту за руб, bids - покупка крипты за руб
    best_gar_buy_btc = ret_gar_btc.json()['bids'][0]['price']

    return best_gar_sell_btc, best_gar_buy_btc


def gar_eth():
    """
    returns sell_eth, buy_eth
    """
    ret_gar_eth = requests.get('https://garantex.io/api/v2/depth', headers={'Authorization': 'Bearer ' + jwt_token},
                               data={'market': 'ethrub'})
    best_gar_sell_eth = ret_gar_eth.json()['asks'][0][
        'price']  # asks - мы продаем крипту за руб, bids - покупка крипты за руб
    best_gar_buy_eth = ret_gar_eth.json()['bids'][0]['price']

    return best_gar_sell_eth, best_gar_buy_eth


def bin_usdt():
    """
    returns sell_usdt, buy_usdt
    """
    data_sell_usdt = {
        "asset": "USDT",
        "fiat": "RUB",
        "merchantCheck": False,
        "page": 1,
        "payTypes": [],
        "publisherType": None,
        "rows": 10,
        "tradeType": "SELL"
    }
    data_buy_usdt = {
        "asset": "USDT",
        "fiat": "RUB",
        "merchantCheck": False,
        "page": 1,
        "payTypes": [],
        "publisherType": None,
        "rows": 10,
        "tradeType": "SELL"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "123",
        "content-type": "application/json",
        "Host": "p2p.binance.com",
        "Origin": "https://p2p.binance.com",
        "Pragma": "no-cache",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }

    r_sell = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',headers=headers, json=data_sell_usdt).json()['data'][0]['adv']['price']
    r_buy = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',headers=headers, json=data_buy_usdt).json()['data'][0]['adv']['price']
    # print(r.json()['data'][0]['adv']['price'])  # r.json()['data'][0]['adv']['price'] - продать p2p
    return r_sell, r_buy


def bin_btc():
    """
    returns sell_btc, buy_btc
    """
    data_sell_btc = {
        "asset": "BTC",
        "fiat": "RUB",
        "merchantCheck": False,
        "page": 1,
        "payTypes": [],
        "publisherType": None,
        "rows": 10,
        "tradeType": "SELL"
    }
    data_buy_btc = {
        "asset": "BTC",
        "fiat": "RUB",
        "merchantCheck": False,
        "page": 1,
        "payTypes": [],
        "publisherType": None,
        "rows": 10,
        "tradeType": "SELL"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "123",
        "content-type": "application/json",
        "Host": "p2p.binance.com",
        "Origin": "https://p2p.binance.com",
        "Pragma": "no-cache",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }

    r_sell = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',headers=headers, json=data_sell_btc).json()['data'][0]['adv']['price']
    r_buy = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',headers=headers, json=data_buy_btc).json()['data'][0]['adv']['price']
    # print(r.json()['data'][0]['adv']['price'])  # r.json()['data'][0]['adv']['price'] - продать p2p
    return r_sell, r_buy


def bin_eth():
    """
    returns sell_eth, buy_eth
    """
    data_sell_eth = {
        "asset": "ETH",
        "fiat": "RUB",
        "merchantCheck": False,
        "page": 1,
        "payTypes": [],
        "publisherType": None,
        "rows": 10,
        "tradeType": "SELL"
    }
    data_buy_eth = {
        "asset": "ETH",
        "fiat": "RUB",
        "merchantCheck": False,
        "page": 1,
        "payTypes": [],
        "publisherType": None,
        "rows": 10,
        "tradeType": "SELL"
    }

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "123",
        "content-type": "application/json",
        "Host": "p2p.binance.com",
        "Origin": "https://p2p.binance.com",
        "Pragma": "no-cache",
        "TE": "Trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }

    r_sell = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',headers=headers, json=data_sell_eth).json()['data'][0]['adv']['price']
    r_buy = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',headers=headers, json=data_buy_eth).json()['data'][0]['adv']['price']
    # print(r.json()['data'][0]['adv']['price'])  # r.json()['data'][0]['adv']['price'] - продать p2p
    return r_sell, r_buy



t = 4  # [t] - seconds
time_gar_token = 0 # 0 seconds from start  =>   update when 600 seconds


if __name__ == "__main__":

    while True:
        time.sleep(t)

        # generate jwt_token each 10 minute
        #time_gar_token += 4
        #if time_gar_token % 600 == 0:
        #    jwt_token = gen_gar_token()


        best_gar_sell_usdt, best_gar_buy_usdt = gar_usdt()
        best_gar_sell_btc, best_gar_buy_btc = gar_btc()
        best_gar_sell_eth, best_gar_buy_eth = gar_eth()

        best_bin_sell_usdt, best_bin_buy_usdt = bin_usdt()
        best_bin_sell_btc, best_bin_buy_btc = bin_btc()
        best_bin_sell_eth, best_bin_buy_eth = bin_eth()

        # ex - название биржи где покупаем, spread - спред
        # для USDT
        ex, spread_usdt, price_usdt = count_spread_usdt(best_gar_buy_usdt, best_gar_sell_usdt, best_bin_buy_usdt, best_bin_sell_usdt)
        user_list_usdt = check_spread_usdt(spread_usdt)
        for i in range(len(user_list_usdt)):
            bot.send_message(user_list_usdt[i][0], 'Покупайте USDT = '+ str(price_usdt) +' со спредом => ' + str(round(spread_usdt, 4)) + ' на ' + ex)

        # ex - название биржи где покупаем, spread - спред
        # для BTC
        ex, spread_btc, price_btc = count_spread_btc(best_gar_buy_btc, best_gar_sell_btc, best_bin_buy_btc, best_bin_sell_btc)
        user_list_btc = check_spread_btc(spread_btc)
        for i in range(len(user_list_btc)):
            bot.send_message(user_list_btc[i][0], 'Покупайте BTC = '+ str(price_btc) +' со спредом => ' + str(round(spread_btc,4)) + ' на ' + ex)

        # ex - название биржи где покупаем, spread - спред
        # для ETH
        ex, spread_eth, price_eth = count_spread_eth(best_gar_buy_eth, best_gar_sell_eth, best_bin_buy_eth, best_bin_sell_eth)
        user_list_eth = check_spread_eth(spread_eth)
        for i in range(len(user_list_eth)):
            bot.send_message(user_list_eth[i][0], 'Покупайте ETH по цене = '+ str(price_eth) +' со спредом => ' + str(round(spread_eth, 4)) + ' на ' + ex)

        print('GARANTEX')
        print('USDT     ', 'sell', best_gar_sell_usdt , 'buy', best_gar_buy_usdt)
        print('BTC     ', 'sell', best_gar_sell_btc , 'buy', best_gar_buy_btc)
        print('ETH     ', 'sell', best_gar_sell_eth, 'buy', best_gar_buy_eth)
        print()
        print()
        print()
        print('BINANCE')
        print('USDT     ', 'sell', best_bin_sell_usdt , 'buy', best_bin_buy_usdt)
        print('BTC     ', 'sell', best_bin_sell_btc , 'buy', best_bin_buy_btc)
        print('ETH     ', 'sell', best_bin_sell_eth, 'buy', best_bin_buy_eth)
        print()
        print()
        print()
        #bot.send_message(id, best_bin_buy_usdt)