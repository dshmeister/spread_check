# requirements:
# pip3 install 'pyjwt[crypto]'

from spread.gar_tokens import *
import base64
import time
import datetime
import random
import requests
import jwt

# private_key = '{приватный ключ, полученный на этапе создания API ключей}'
# uid = '{UID, полученный на этапе создания API ключей}'
# host = 'garantex.io' # для тестового сервера используйте stage.garantex.biz


def gen_gar_token():
    key = base64.b64decode(private_key)
    iat = int(time.mktime(datetime.datetime.now().timetuple()))

    claims = {
        "exp": iat + 1*60*60, # JWT Request TTL in seconds since epoch
        "jti": hex(random.getrandbits(12)).upper()
    }

    jwt_token = jwt.encode(claims, key, algorithm="RS256")

    print("JWT request token: %s\n" % jwt_token)

    ret = requests.post('https://dauth.' + host + '/api/v1/sessions/generate_jwt',
                        json={'kid': uid, 'jwt_token': jwt_token})

    print("JWT response code: %d" % ret.status_code)
    print("JWY response text: %s\n" % ret.text)

    token = ret.json().get('token')

    print("JWT token: %s\n" % token)

    print()
    print()
    print()
    print(token)
    return str(token)



# # ret = requests.get('https://' + host + '/api/v2/members/me', headers = {'Authorization': 'Bearer ' + token})
# ret = requests.get('https://garantex.io/api/v2/depth', headers = {'Authorization': 'Bearer ' + jwt_token}, data = {'market':'usdtrub'})
# print(ret.json())
# # d = ret.json()
# #
# # for key in d:
# #     print(key)