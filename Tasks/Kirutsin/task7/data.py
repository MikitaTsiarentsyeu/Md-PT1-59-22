import hashlib
import hmac
import sqlite3
import datetime
from config import key, path_bd, user_table, user_column_login, user_column_password, shop_table, shop_column_product, \
    shop_column_price, shop_column_currency, user_cart_table, user_cart_column_user, user_cart_column_product, \
    user_cart_column_price, user_cart_column_currency


def error_logs(responce, parametrs):
    """

    :param responce: response def
    :param parametrs: params def
    :return:
    """
    with open('error_file.txt', 'r') as f:
        errors = f'{str(datetime.datetime.now())}, {responce}, {parametrs}, {f.read()},'
        f.close()

    with open('error_file.txt', 'w') as x:
        x.write(errors)
        x.close()
    return None
def hash_key(secret_key, password_user):
    """

    :param secret_key:
    :param password_user:
    :return:
    """
    secret_hash = hmac.new(key=secret_key, msg=str(password_user).encode(), digestmod=hashlib.sha256, ).hexdigest()
    return secret_hash

def create_user(login_user, password_user):
    """

    :param login_user:
    :param password_user:
    :return:
    """
    secret_hash = hash_key(key, password_user)
    con = sqlite3.connect(path_bd)
    cur = con.cursor()
    data = [
        (login_user, secret_hash)
    ]
    x = cur.executemany(f"INSERT INTO {user_table} VALUES(?, ?)", data)
    con.commit()
    res = x.fetchone()
    if res is not None:
        error_logs(res, [f'parametrs=[{login_user}, {password_user}]', f'db={path_bd}'])
        return res
    else:
        return res

def select_user(value):
    """
    :param value: login user
    :return: True == User created success, False == user always been here
    """
    con = sqlite3.connect(path_bd)
    cur = con.cursor()
    x = cur.execute(f"select {user_column_login} from {user_table} where login = '{value}'")
    res = x.fetchall()
    res_bool = bool(res)
    if res is not None:
        error_logs(res_bool, [f'parametrs={value}', f'db={path_bd}'])
        return res_bool
    else:
        return None

def validation_password(login_user, password_user):
    """

    :param login_user: user login
    :param password_user: password login
    :return: True == Success authorization ; False == failed authorization
    """
    secret_hash = hash_key(key, password_user)
    con = sqlite3.connect(path_bd)
    cur = con.cursor()
    x = cur.execute(f"select {user_column_password} from {user_table} where login = '{login_user}'")
    result = x.fetchone()
    if result is None:
        error_logs(result, [f'parametrs=[{login_user}, {password_user}]', f'db={path_bd}'])
    if result[0] == secret_hash:
        return True
    else:
        return False

def view_shop():
    """

    :return: contents
    """
    result = []
    con = sqlite3.connect(path_bd)
    cur = con.cursor()
    x = cur.execute(f"select count(*) from {shop_table}")
    index = x.fetchone()[0]
    for i in range(index):
        x = cur.execute(f"select {shop_column_product},{shop_column_price},{shop_column_currency},ROWID from {shop_table} where ROWID = {i + 1}")
        result += x.fetchall()
    return result

def user_cart(username):
    """

    :param username: login user
    :return: contents
    """
    result = []
    con = sqlite3.connect(path_bd)
    cur = con.cursor()
    x = cur.execute(f"select ROWID from {user_cart_table} where {user_cart_column_user} == '{username}'")
    index = x.fetchall()
    for i in index:
        x = cur.execute(f"select {user_cart_column_product}, {user_cart_column_price}, {user_cart_column_currency},ROWID from {user_cart_table} where ROWID = {i[0]}")
        result += x.fetchall()
    return result

def select_product_info(id_row):
    """

    :param id_row: id product
    :return: content
    """
    result = []
    con = sqlite3.connect(path_bd)
    cur = con.cursor()
    x = cur.execute(f"select {shop_column_product},{shop_column_price}, {shop_column_currency} from {shop_table} where ROWID = {int(id_row)}")
    result += x.fetchall()
    return result

def add_product(user_login, product, price, currency):
    """

    :param user_login: user
    :param product: product
    :param price: price
    :param currency: currency
    :return: True
    """
    con = sqlite3.connect(path_bd)
    cur = con.cursor()
    data = [
        (user_login, product, price, currency)
    ]
    x = cur.executemany(f"INSERT INTO {user_cart_table} VALUES(?, ?, ?, ?)", data)
    con.commit()
    x.fetchall()
    return True

def delete_product(id_row, user):
    """

    :param id_row: id product
    :param user: user
    :return:
    """
    con = sqlite3.connect(path_bd)
    cur = con.cursor()
    x = cur.execute(f"DELETE FROM {user_cart_table} WHERE (ROWID = {int(id_row)}) and {user_cart_column_user} = '{user}'")
    con.commit()
    return x.fetchall()

if __name__ == "__main__":
    # test config
    path_bd = 'secure_bd'
    user_table = "personal_data"
    key = b'B2sb3twsFKJd36sj'
    user = 'test'
    password = '123123123sadasdasd'

    # tests
    # print(select_user("te34st"))
    # create_user(user, password)
    # print(validation_password('admin', '123'))
    # print(view_shop())
    # print(user_cart('admin'))
    # print(select_product_info(5))
    # print(add_product('admin', 'fhfgh', '123', 'USD'))
    print(delete_product('1','admin228'))