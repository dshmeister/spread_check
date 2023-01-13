import sqlite3
from datetime import datetime, date


def add_user_to_db(user_id, stakan = 0, spread = 0.3, min_sum = 0, payment_actual = 0.3, date_of_actuality_payment = None, bundle = 'None', alerts = 1 ):
    """
    function adds data to db, without APIs.
    """
    db = sqlite3.connect('users.db')
    c = db.cursor()
    params = [user_id,stakan,spread,min_sum,payment_actual, date_of_actuality_payment, bundle, alerts]
    c.execute(f"INSERT INTO users (user_id, stakan, spread, min_sum, payment_actual, date_of_actuality_payment, bundle, alerts ) VALUES (?, ?,?,?,?, ?, ?, ?);", params)
    db.commit()
    db.close()


def gen_ref_for_friends(user_id):
    pass


def check_user_new(user_id):
    """
    function checks if user is new, or not.
    True - new, False - old.
    """
    db = sqlite3.connect('users.db')
    c = db.cursor()
    c.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    if len(c.fetchall()) == 0:
        db.close()
        return True
    db.close()
    return False


def check_date_of_actuality_payment(user_id, mode=0):
    """
    function checks if subscribe is actual by date
    True - subscribe is actual
    False - subscribe is not actual

    mode:
    0 - check
    1 - give actuall date
    """
    if mode == 0:
        db = sqlite3.connect('users.db')
        c = db.cursor()
        c.execute(f"SELECT date_of_actuality_payment FROM users WHERE user_id = {user_id} ")
        # current date
        current_date = str(datetime.now().date()).split('-')
        current_year, current_month, current_day = map(int, current_date)
        # check subscribtion date
        if c.fetchone()[0] == None or date(current_year,current_month, current_day) > c.fetchone()[0]:
            db.close()
            return False
        else:
            db.close()
            return True
    else:
        db = sqlite3.connect('users.db')
        c = db.cursor()
        c.execute(f"SELECT date_of_actuality_payment FROM users WHERE user_id = {user_id} ")
        db.close()
        return c.fetchone()[0]


def create_correct_list_for_sql(lst):
    lst = lst.replace('[', '').replace(']','').replace(' ','')
    # print('vivod func', '&'+lst+'&')
    return lst


def check_user_bundle(user_id):
    """
    funtion checks user's bundles
    response is ['RUB/USDT', 'RUB/BTC'] etc
    """
    db = sqlite3.connect('users.db')
    c = db.cursor()
    c.execute(f"SELECT bundle FROM users WHERE user_id = {user_id} ")
    bundles = list(c.fetchone())
    bundles = create_correct_list_for_sql(str(bundles))
    return bundles


def add_del_bundle(user_id, bundle):
    """
    function adds bundle if it is not added, and delets if it is added\
    bundle must be in format RUB/USDT or similar
    return 'del' - if deleted
    return 'add' - if added
    """
    db = sqlite3.connect('users.db')
    c = db.cursor()
    c.execute(f"SELECT bundle FROM users WHERE user_id = {user_id}")

    # список в виде строки возвращаемых связок
    bundles = c.fetchone()[0]
    list_bund = bundles.split(',')

    if bundles != 'None' and bundle in list_bund: # удаляем найденную связку
        # создаем строку без необходимой связки
        buf = ''
        bundles = list_bund

        # проходимся до последнего элемента(не включительно)
        for i in range(len(bundles)-1):
            if bundles[i] != bundle:
                buf += bundles[i] + ','

        # если последний эл не тот который нужно удалить, просто его добавляем, иначе убираем запятую в конце
        if bundles[-1] != bundle:
            buf += bundle
        else:
            buf = buf[:-1]

        if buf == '':
            buf = 'None'
        params = [buf, user_id]

        c.execute(f"UPDATE users SET bundle= ? WHERE user_id= ? ;", params)
        db.commit()
        db.close()
        return 'del'

    elif bundles == 'None':
        # c.execute(f"UPDATE users SET bundle={bundles} WHERE user_id={user_id};")
        params = [bundle, user_id]
        c.execute(f"UPDATE users SET bundle = ? WHERE user_id = ?;", params)
        db.commit()
        db.close()
        return 'add'

    else: # добавляем выбранную связку

        bundles += ','+bundle
        # print(bundles)
        # print(type(bundles))
        # bundles = create_correct_list_for_sql(str(bundles))
        # print(bundles)
        # print(type(bundles))
        params = [bundles, user_id]
        c.execute(f"UPDATE users SET bundle = ? WHERE user_id = ?;", params)
        db.commit()
        db.close()
        return 'add'


def check_payment_actual(user_id):
    """
    function checks if user's payment is actual.
    True - actual, False - not actual.
    """
    db = sqlite3.connect('users.db')
    c = db.cursor()
    c.execute(f"SELECT * FROM users WHERE user_id = {user_id} AND payment_actual = 1")
    if len(c.fetchall()) != 0:
        db.close()
        return True
    db.close()
    return False

def adding_spread(user_id, spread):
    """
    function that adds spread to database of user_id
    """
    db = sqlite3.connect('users.db')
    c = db.cursor()
    #c.execute(f"INSERT INTO users (spread) WHERE user_id = {user_id} VALUES {spread}")
    c.execute(f'UPDATE users SET spread = {spread} WHERE user_id = {user_id}')
    c.execute(f'SELECT spread FROM users WHERE user_id = {user_id} ')
    spread_s = c.fetchone()[0]
    db.commit()
    db.close()
    #return spread_s
    
    
def check_spread(user_id):
    """
    function returns spread from db
    """
    db = sqlite3.connect('users.db')
    c = db.cursor()
    c.execute(f'SELECT spread FROM users WHERE user_id = {user_id} ')
    spread = c.fetchone()[0]
    return spread

def check_min_sum(user_id):
    """
    function returns
    """
    db = sqlite3.connect('users.db')
    c = db.cursor()
    c.execute(f'SELECT min_sum FROM users WHERE user_id = {user_id} ')
    mins = c.fetchone()[0]
    return mins


def set_min_sum_db(user_id, min_sum):
    """
    function sets min_sum to db
    """
    db = sqlite3.connect('users.db')
    c = db.cursor()
    param = [min_sum, user_id]
    c.execute(f'UPDATE users SET min_sum = ? WHERE user_id = ?', param)
    db.commit()
    db.close()

