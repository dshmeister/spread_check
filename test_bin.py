"""
from binance.client import Client
from bin_token import *

client = Client(api_key, api_secret)


depth = client.get_order_book(symbol='BNBBTC')
print(depth)
"""

from binance_api import Binance
bot = Binance('EX6MDOimBKbV242hex9Zqa21RcozF2wbgdIT4bYB9UTXyA2tXmkv44WMMH0jgsNo',
              'gSH3V2CnmIyHC0SDjKR4xXkfZmOo9ccGWw9xW7uGLmDQJlQuSC8IV9Q3D1oo4D0B')
print('p2pTrade', bot.p2pTrade(
# левое значение - курс BNB BTC
# правое значение - количество то ли BNB, то ли BTC
    symbol='USDTRUB',
    limit = 2

))
