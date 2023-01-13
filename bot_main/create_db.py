import sqlite3
from datetime import datetime
#
# init or connect to db
db = sqlite3.connect('users.db')
#
# # create cursor
c = db.cursor()
#
# write and run sql command
"""
stakan:
0 - default before choice
1 - buy as a taker
2 - buy as a maker
3 - sell as a taker
4 - sell as a maker
"""
# c.execute('''CREATE TABLE users(
#      user_id integer,
#      stakan integer,
#      spread real,
#      min_sum integer,
#      payment_actual integer,
#      date_of_actuality_payment text,
#      bundle text,
#      alerts integer,
#      api_binance text,
#      api_garantex text,
#      ref_for_friends text,
#      ref_ invite text
# )''')
# #
# #
# # c.execute("INSERT INTO users (user_id) VALUES (582648838);")
# #
# c.execute("DROP TABLE users;")
c.execute("SELECT * FROM users;")
# # need this string to print the result
print(c.fetchall())
#update db
# db.commit()

#
db.close()



# Создание таблы с нуля

# db = sqlite3.connect('users.db')
# c = db.cursor()
# c.execute('''CREATE TABLE users(
#      user_id integer,
#      stakan integer,
#      spread real,
#      min_sum integer,
#      payment_actual integer,
#      date_of_actuality_payment text,
#      bundle text,
#      alerts integer,
#      api_binance text,
#      api_garantex text
#      ref_for_friends text,
#      ref_ invite text
# )''')
# db.commit()
# db.close()
