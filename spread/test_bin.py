import requests
import json

data = {
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

r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
                  headers=headers, json=data)

print(json.dumps(r.json(), indent=4, ensure_ascii=False))
#item = json.loads(r.json())
#print(item["data"][0], item["adv"], item["price"])
# print(json.dumps(response.json(), indent=4, ensure_ascii=False))








"""
from binance.client import Client
from bin_token import *

client = Client(api_key, api_secret)


depth = client.get_order_book(symbol='BNBBTC')
print(depth)


from binance_api import Binance
bot = Binance('EX6MDOimBKbV242hex9Zqa21RcozF2wbgdIT4bYB9UTXyA2tXmkv44WMMH0jgsNo',
              'gSH3V2CnmIyHC0SDjKR4xXkfZmOo9ccGWw9xW7uGLmDQJlQuSC8IV9Q3D1oo4D0B')
print('p2pTrade', bot.p2pTrade(
# левое значение - курс BNB BTC
# правое значение - количество то ли BNB, то ли BTC
    symbol='USDTRUB',
    limit = 2

))
"""
