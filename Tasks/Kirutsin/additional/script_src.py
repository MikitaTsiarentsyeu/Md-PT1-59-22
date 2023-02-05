import hashlib
import sqlite3
import hmac
import uuid


# call DB
# PATH == PATH to db
# header == header of column
def select_all(PATH, table_name):
    con = sqlite3.connect(PATH)
    cur = con.cursor()
    x = cur.execute(f"SELECT * FROM {table_name}")
    res = x.fetchall()
    return res


# select from db by column header
# If res_bool = False, that new user, elif res_bool == True, it has always been here

# PATH == PATH to db
# header == header of column
# table_name == table where contains users
# value == cell in the table

def select_user(PATH, header, table_name, value):
    con = sqlite3.connect(PATH)
    cur = con.cursor()
    x = cur.execute(f"select {header} from {table_name} where login = '{value}'")
    res = x.fetchall()
    res_bool = bool(res)
    return res_bool


# create user

# PATH == PATH to db
# table_name == table where contains users
# login_user == login user
# password_user == password user

def create_user(PATH, table_name, login_user, password_user, key):
    secret_hash = hmac.new(key=key, msg=str(password_user).encode(), digestmod=hashlib.sha256, ).hexdigest()
    con = sqlite3.connect(PATH)
    cur = con.cursor()
    data = [
        (login_user, secret_hash)
    ]
    x = cur.executemany(f"INSERT INTO {table_name} VALUES(?, ?)", data)
    con.commit()
    res = x.fetchone()
    return res


# check users password

# PATH == PATH to db
# header_password == column where your contains passwords from users
# table_name == table where contains users
# header_login == column where your contains login from users
# value == login user
# password_user == password user


def login_validation(PATH, header_password, table_name, header_login, value, password_user, key):
    secret_hash = hmac.new(key=key, msg=str(password_user).encode(), digestmod=hashlib.sha256, ).hexdigest()
    con = sqlite3.connect(PATH)
    cur = con.cursor()
    x = cur.execute(f"select {header_password} from {table_name} where {header_login} ='{value}'")
    res = x.fetchone()
    if res:
        if secret_hash == ''.join(res) and res is not None:
            result = True
        else:
            result = False
    else:
        return False
    return result


# select_shoplist

# PATH == PATH to db
# user == login user


def select_shoplist(PATH, user):
    con = sqlite3.connect(PATH)
    cur = con.cursor()
    x = cur.execute(f"select ROWID from shop_info where user = '{user}'")
    res = x.fetchall()
    index = ''
    for i in res:
        # id
        cur = con.cursor()
        x = cur.execute(f"select id from shop_info where ROWID = '{i[0]}'")
        pos_id = x.fetchone()
        index = index + pos_id[0] + '|\v'

        # product
        cur = con.cursor()
        x = cur.execute(f"select product from shop_info where ROWID = '{i[0]}'")
        product = x.fetchone()
        index = index + product[0] + '|\v'

        # price
        cur = con.cursor()
        x = cur.execute(f"select price from shop_info where ROWID = '{i[0]}'")
        price = x.fetchone()
        index = index + price[0] + '|\v'

        # currency
        cur = con.cursor()
        x = cur.execute(f"select currency from shop_info where ROWID = '{i[0]}'")
        currency = x.fetchone()
        index = index + currency[0] + '\n'

    shop_table = 'id|\vproduct|\vprice|\vcurrency:\n' + index

    return shop_table


# add_product

# PATH == PATH to db
# table_name == table where contains shop info
# message == source
# user == login user


def add_product(PATH, table_name, message, user):
    # parse message
    product = (str(message).split('|'))[1]
    price = (str(message).split('|'))[2]
    currency = (str(message).split('|'))[3]
    tr_id = str(uuid.uuid4())

    # add parametrs in db
    con = sqlite3.connect(PATH)
    cur = con.cursor()
    data = [
        (user, product, price, currency, tr_id)
    ]
    x = cur.executemany(f"INSERT INTO {table_name} VALUES(?, ?, ?, ?, ?)", data)
    con.commit()
    res = x.fetchone()
    return res


# delete_product
# PATH == PATH to db
# table_name == table where contains shop info
# id == id product

def delete_product(PATH, table_name, message):
    final_id = (str(message).split('|'))[1]
    con = sqlite3.connect(PATH)
    cur = con.cursor()
    x = cur.execute(f"delete from {table_name} where id = '{final_id}'")
    con.commit()
    res = x.fetchone()
    return res